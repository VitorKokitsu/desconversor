from typing import Any

from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.condpgto import CondicaoPagamentoRequestDTO

from application.mapper.autenticacao import AutenticacaoMapper
from application.ports.process import Process


class AutenticacaoProcess(Process):
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        protheus_dto = CondicaoPagamentoRequestDTO(**payload)
        middleware_dto = AutenticacaoMapper.to_middleware(protheus_dto, PedprecoPlatformDTO(**platform_data))
        if not allow_send:
            return middleware_dto.model_dump(mode="json", by_alias=True)

        middleware_response = self._middleware_client().send_autenticacao(middleware_dto, self._nome_config_obrigatorio(nome_config))
        return middleware_response.model_dump()
