from typing import Any

from odysseia.request.pedido import PedidoRequestDTO

from application.mapper.pedido import PedidoMapper
from application.ports.process import Process


class PedidoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
    ) -> dict[str, Any]:
        protheus_dto = PedidoRequestDTO(**payload)
        middleware_dto = PedidoMapper.to_middleware(protheus_dto, platform_data)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_pedido(middleware_dto)
        return middleware_response.model_dump()
