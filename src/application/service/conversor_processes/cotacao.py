from typing import Any

from odysseia.request.cotacao import CotacaoRequestDTO

from application.mapper.cotacao import CotacaoMapper
from application.ports.process import Process


class CotacaoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
    ) -> dict[str, Any]:
        protheus_dto = CotacaoRequestDTO(**payload)
        middleware_dto = CotacaoMapper.to_middleware(protheus_dto)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_cotacao(middleware_dto)
        return middleware_response.model_dump()
