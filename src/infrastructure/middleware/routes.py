from typing import Any

from httpx import Request


class MiddlewareRoutes:
    # O middleware sobrescreve o use_zt do corpo pelo da query, cujo padrão é true. Nas rotas da Cotefacil
    # o parâmetro se chama useZT; nas do PedPreço, use_zt.
    def __init__(self, api_url: str) -> None:
        self.__api_url = api_url.removesuffix("/")

    def autenticacao(self, data: dict[str, Any], nome_config: str) -> Request:
        return Request(
            url=f"{self.__api_url}/pedpreco/autenticacao",
            params={"nome_config": nome_config, "use_zt": data["use_zt"]},
            method="POST",
            json=data,
        )

    def ingestao(self, data: dict[str, Any], nome_config: str) -> Request:
        return Request(
            url=f"{self.__api_url}/pedpreco/ingestao",
            params={"nome_config": nome_config, "use_zt": data["use_zt"]},
            method="POST",
            json=data,
        )

    def condpgto(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchcondicoespagamento",
            params={"useZT": data["use_zt"]},
            method="POST",
            json=data,
        )

    def cotacao(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchrespostacotacao",
            params={"useZT": data["use_zt"]},
            method="POST",
            json=data,
        )

    def retorno(self, data: dict[str, Any]) -> Request:
        return Request(
            url=f"{self.__api_url}/cotefacil/fetchretornopedido",
            params={"useZT": data["use_zt"]},
            method="POST",
            json=data,
        )
