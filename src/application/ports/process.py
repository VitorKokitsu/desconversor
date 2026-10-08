from abc import ABC, abstractmethod
from typing import Any

from application.ports.middleware_port import MiddlewareClientPort


class Process(ABC):
    def __init__(self, middleware_client: MiddlewareClientPort | None) -> None:
        self.middleware_client = middleware_client

    def _middleware_client(self) -> MiddlewareClientPort:
        if self.middleware_client is None:
            raise RuntimeError("Cliente do middleware não configurado")

        return self.middleware_client

    @staticmethod
    def _nome_config_obrigatorio(nome_config: str | None) -> str:
        # As rotas do PedPreço no middleware exigem o nome da configuração, que não vem no payload do Protheus.
        if not nome_config:
            raise ValueError("nome_config é obrigatório para enviar processos do PedPreço")

        return nome_config

    @abstractmethod
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
        nome_config: str | None = None,
    ) -> dict[str, Any]:
        pass
