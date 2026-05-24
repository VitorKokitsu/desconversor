from typing import Any

from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from app.application.mapper.retorno import RetornoMapper
from app.application.ports.process import Process


class RetornoFaturamentoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
    ) -> dict[str, Any]:
        protheus_dto = RetornoFaturamentoRequestDTO(**payload)
        middleware_dto = RetornoMapper.to_middleware(protheus_dto)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_retorno(middleware_dto)
        return middleware_response.model_dump()
