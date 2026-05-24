from typing import Any

from odysseia.request.condpgto import CondicaoPagamentoRequestDTO

from app.application.mapper.autenticacao import AutenticacaoMapper
from app.application.mapper.condpgto import CondpgtoMapper
from app.application.ports.process import Process


class CondicaoPagamentoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
    ) -> dict[str, Any]:
        protheus_dto = CondicaoPagamentoRequestDTO(**payload)
        if platform == "PedprecoPlatformDTO":
            middleware_dto = AutenticacaoMapper.to_middleware(protheus_dto, platform_data)
            if not allow_send:
                return middleware_dto.model_dump()

            middleware_response = self._middleware_client().send_autenticacao(middleware_dto)
            return middleware_response.model_dump()

        middleware_dto = CondpgtoMapper.to_middleware(protheus_dto)
        if not allow_send:
            return middleware_dto.model_dump()

        middleware_response = self._middleware_client().send_condpgto(middleware_dto)

        return middleware_response.model_dump()
