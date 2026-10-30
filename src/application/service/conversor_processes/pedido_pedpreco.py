from typing import Any

from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.pedido import PedidoRequestDTO

from application.mapper.pedido_pedpreco import PedidoPedprecoMapper
from application.ports.process import Process


class PedidoPedprecoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        protheus_dto = PedidoRequestDTO(**payload)
        middleware_dto = PedidoPedprecoMapper.to_middleware(protheus_dto, PedprecoPlatformDTO(**platform_data))
        if not allow_send:
            return middleware_dto.model_dump(mode="json", by_alias=True)

        middleware_response = self._middleware_client().send_pedido_pedpreco(middleware_dto, self._nome_config_obrigatorio(nome_config))
        return middleware_response.model_dump()
