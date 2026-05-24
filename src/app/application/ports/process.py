from abc import ABC, abstractmethod
from typing import Any

from app.domain.ports.middleware_port import MiddlewareClientPort


class Process(ABC):
    def __init__(self, middleware_client: MiddlewareClientPort | None) -> None:
        self.middleware_client = middleware_client

    def _middleware_client(self) -> MiddlewareClientPort:
        if self.middleware_client is None:
            raise RuntimeError("Cliente do middleware não configurado")

        return self.middleware_client

    @abstractmethod
    def execute(
        self,
        payload: dict[str, Any],
        platform: str,
        platform_data: dict[str, Any],
        allow_send: bool,
    ) -> dict[str, Any]:
        pass
