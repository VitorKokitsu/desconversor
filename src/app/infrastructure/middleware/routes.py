from typing import Any

from httpx import Request


class MiddlewareRoutes:
    def __init__(self, api_url: str) -> None:
        self.__api_url = api_url.removesuffix("/")

    def autenticacao(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/fetchautenticacao",
            params={"use_zt": False},
            method="POST",
            json=data,
        )

    def condpgto(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchcondicoespagamento",
            params={"use_zt": False},
            method="POST",
            json=data,
        )

    def cotacao(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchrespostacotacao",
            method="POST",
            json=data,
        )

    def retorno(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchretornopedido",
            method="POST",
            json=data,
        )
