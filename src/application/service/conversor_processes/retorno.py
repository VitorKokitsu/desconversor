from typing import Any

from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from application.mapper.retorno import RetornoMapper
from application.ports.middleware_port import MiddlewareClientPort
from application.ports.process import Process
from application.service.conversor_processes.retorno_pedpreco import RetornoPedprecoProcess
from application.service.identificador_processo import IdentificadorProcesso


class RetornoFaturamentoProcess(Process):
    def __init__(self, middleware_client: MiddlewareClientPort | None) -> None:
        super().__init__(middleware_client)
        self.retorno_pedpreco_process = RetornoPedprecoProcess(middleware_client)

    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        if IdentificadorProcesso.deriva_de_pedpreco(platform):
            return self.retorno_pedpreco_process.execute(payload, platform, platform_data, allow_send, nome_config)

        protheus_dto = RetornoFaturamentoRequestDTO(**payload)
        middleware_dto = RetornoMapper.to_middleware(protheus_dto, platform_data)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_retorno(middleware_dto)
        return middleware_response.model_dump()
