from typing import Any

from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from application.mapper.retorno_pedpreco import RetornoPedprecoMapper
from application.ports.process import Process


class RetornoPedprecoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        protheus_dto = RetornoFaturamentoRequestDTO(**payload)
        middleware_dto = RetornoPedprecoMapper.to_middleware(protheus_dto, PedprecoPlatformDTO(**platform_data))
        if not allow_send:
            return middleware_dto.model_dump(mode="json", by_alias=True)

        middleware_response = self._middleware_client().send_retorno_pedpreco(middleware_dto, self._nome_config_obrigatorio(nome_config))
        return middleware_response.model_dump()
