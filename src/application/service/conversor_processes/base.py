from typing import Any

from odysseia.request.base import BaseProdutosRequestDTO

from application.mapper.base import BaseProdutosMapper
from application.ports.process import Process


class BaseProdutosProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        protheus_dto = BaseProdutosRequestDTO(**payload)
        middleware_dto = BaseProdutosMapper.to_middleware(protheus_dto, platform_data)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_base(middleware_dto)
        return middleware_response.model_dump()
