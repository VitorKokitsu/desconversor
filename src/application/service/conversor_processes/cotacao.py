from typing import Any

from odysseia.request.cotacao import CotacaoRequestDTO

from application.mapper.cotacao import CotacaoMapper
from application.ports.middleware_port import MiddlewareClientPort
from application.ports.process import Process
from application.service.conversor_processes.ingestao import IngestaoProcess
from application.service.identificador_processo import IdentificadorProcesso


class CotacaoProcess(Process):
    def __init__(self, middleware_client: MiddlewareClientPort | None) -> None:
        super().__init__(middleware_client)
        self.ingestao_process = IngestaoProcess(middleware_client)

    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        protheus_dto = CotacaoRequestDTO(**payload)
        if IdentificadorProcesso.deriva_de_ingestao(platform, protheus_dto):
            return self.ingestao_process.execute(payload, platform, platform_data, allow_send, nome_config)

        middleware_dto = CotacaoMapper.to_middleware(protheus_dto, platform_data)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_cotacao(middleware_dto)
        return middleware_response.model_dump()
