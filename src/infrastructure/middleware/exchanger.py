import logging
from time import sleep

from httpx import Client, Response, Request, Timeout
from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestDTO
from odysseia.request.cotefacil.cotacao import CTFLCotacaoRequestDTO
from odysseia.request.cotefacil.retorno import CTFLRetornoFaturamentoRequestDTO
from odysseia.request.pedpreco.autenticacao import PPAutenticacaoRequestDTO

from infrastructure.middleware.routes import MiddlewareRoutes


class MiddlewareExchanger:
    logger = logging.getLogger(__name__)

    def __init__(self, client: Client, routes: MiddlewareRoutes) -> None:
        self.client = client
        self.routes = routes

    def autenticacao(self, payload: PPAutenticacaoRequestDTO) -> Response:
        return self._send(
            request=self.routes.autenticacao(
                data=payload.model_dump(mode="json"),
            ),
        )

    def condpgto(self, payload: CTFLCondicaoPagamentoRequestDTO) -> Response:
        return self._send(
            request=self.routes.condpgto(
                data=payload.model_dump(mode="json"),
            ),
        )

    def cotacao(self, payload: CTFLCotacaoRequestDTO) -> Response:
        return self._send(
            request=self.routes.cotacao(
                data=payload.model_dump(mode="json"),
            ),
        )

    def retorno(self, payload: CTFLRetornoFaturamentoRequestDTO) -> Response:
        return self._send(
            request=self.routes.retorno(
                data=payload.model_dump(mode="json"),
            ),
        )

    def _send(self, request: Request, timeout_seconds: int = 60) -> Response:
        request.headers.update(self.client.headers)
        request.extensions["timeout"] = {"pool": Timeout(timeout_seconds)}

        try:
            response = self.client.send(request)
            attempt = 1
            while response.status_code == 429 and attempt < 2:
                attempt += 1
                self.logger.warning("Servidor sobrecarregado, aguardando 10 segundos e tentando novamente...")
                sleep(10)

                response = self.client.send(request)
        except Exception as er:
            self.logger.exception("Erro ao enviar para o middleware", exc_info=er)
            raise

        return response
