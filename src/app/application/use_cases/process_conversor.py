from typing import Any

from homero.enum import JobNameEnum
from odysseia.request.condpgto import CondicaoPagamentoRequestDTO
from odysseia.request.cotacao import CotacaoRequestDTO
from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from app.application.mapper.condpgto import CondpgtoMapper
from app.application.mapper.cotacao import CotacaoMapper
from app.application.mapper.retorno import RetornoMapper
from app.domain.ports.get_payload_port import GetPayloadPort
from app.infrastructure.middleware.client import MiddlewareClient


class ProcessConversorUseCase:

    def __init__(
        self,
        get_payload: GetPayloadPort,
        middleware_client: MiddlewareClient,
    ) -> None:
        self.middleware_client = middleware_client
        self.get_payload = get_payload

    def execute(self, s3_key: str, allow_send: bool) -> dict[str, Any]:
        job_name, platform, raw_payload = self.get_payload.get_object(s3_key)

        match job_name:
            case JobNameEnum.CONDICAO_PAGAMENTO:
                protheus_dto = CondicaoPagamentoRequestDTO(**raw_payload)
                middleware_dto = CondpgtoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()

                middleware_response = self.middleware_client.send_condpgto(middleware_dto)
                return middleware_response.model_dump()

            case JobNameEnum.COTACAO:
                protheus_dto = CotacaoRequestDTO(**raw_payload)
                middleware_dto = CotacaoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()

                middleware_response = self.middleware_client.send_cotacao(middleware_dto)
                return middleware_response.model_dump()

            case JobNameEnum.PEDIDO:
                print()

            case JobNameEnum.RETORNO_FATURAMENTO:
                protheus_dto = RetornoFaturamentoRequestDTO(**raw_payload)
                middleware_dto = RetornoMapper.to_middleware(protheus_dto)
                if not allow_send:
                    return middleware_dto.model_dump()

                middleware_response = self.middleware_client.send_retorno(middleware_dto)
                return middleware_response.model_dump()

            case _:
                raise ValueError("Processo não suportado")
