from typing import Any

from homero.enum import JobNameEnum

from application.service.conversor_processes import (
    CondicaoPagamentoProcess,
    CotacaoProcess,
    Process,
    RetornoFaturamentoProcess,
)
from application.service.get_payload import GetPayload
from application.ports.get_payload_port import PayloadStorage
from application.ports.middleware_port import MiddlewareClientPort


class ConversorUseCase:
    retorno_payload_keys = {"id_cotacao", "codigo_pedido_fornecedor", "data_envio"}
    cotacao_payload_keys = {"promocao", "permite_parcial"}

    def __init__(
        self,
        get_payload: PayloadStorage,
        middleware_client: MiddlewareClientPort | None,
    ) -> None:
        self.middleware_client = middleware_client
        self.get_payload = get_payload
        self.processes: dict[JobNameEnum, Process] = {
            JobNameEnum.CONDICAO_PAGAMENTO: CondicaoPagamentoProcess(middleware_client),
            JobNameEnum.COTACAO: CotacaoProcess(middleware_client),
            JobNameEnum.RETORNO_FATURAMENTO: RetornoFaturamentoProcess(middleware_client),
        }

    def execute(
        self,
        transaction_id: str,
        allow_send: bool,
    ) -> dict[str, Any]:
        raw_payload = self.get_payload.get_object(transaction_id)
        return self.payload(raw_payload=raw_payload, allow_send=allow_send)

    def payload(
        self,
        raw_payload: dict[str, Any],
        allow_send: bool = False,
    ) -> dict[str, Any]:
        job_name, platform, payload = GetPayload.separate_data(raw_payload)
        platform_data = raw_payload[platform]

        process = self.processes.get(job_name)
        if not process:
            raise ValueError(f"Processo de {job_name} não suportado")

        return process.execute(
            payload=payload,
            platform=platform,
            platform_data=platform_data,
            allow_send=allow_send,
        )
