from typing import Any

from odysseia.request.pedido import PedidoRequestDTO

from application.mapper.pedido import PedidoMapper
from application.ports.middleware_port import MiddlewareClientPort
from application.ports.process import Process
from application.service.conversor_processes.pedido_pedpreco import PedidoPedprecoProcess
from application.service.identificador_processo import IdentificadorProcesso


class PedidoProcess(Process):
    def __init__(self, middleware_client: MiddlewareClientPort | None) -> None:
        super().__init__(middleware_client)
        self.pedido_pedpreco_process = PedidoPedprecoProcess(middleware_client)

    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        if IdentificadorProcesso.deriva_de_pedpreco(platform):
            return self.pedido_pedpreco_process.execute(payload, platform, platform_data, allow_send, nome_config)

        protheus_dto = PedidoRequestDTO(**payload)
        middleware_dto = PedidoMapper.to_middleware(protheus_dto, platform_data)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_pedido(middleware_dto)
        return middleware_response.model_dump()
