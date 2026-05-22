import logging
from time import sleep

from httpx import Client, Response, Request, Timeout

from app.application.dtos.request.condpgto import CTFCondigcaoPagamentoRequestDTO
from app.application.dtos.request.cotacao import CTFCotacaoRequestDTO
from app.application.dtos.request.retorno import CTFRetornoRequestDTO
from app.infrastructure.middleware.routes import MiddlewareRoutes


class MiddlewareExchanger:
    client: Client
    routes: MiddlewareRoutes
    logger = logging.getLogger(__name__)

    def condpgto(self, payload: CTFCondigcaoPagamentoRequestDTO) -> Response:
        return self._send(
            request=self.routes.condpgto(
                data=payload.model_dump(mode="json"),
            ),
        )

    def cotacao(self, payload: CTFCotacaoRequestDTO) -> Response:
        return self._send(
            request=self.routes.cotacao(
                data=payload.model_dump(mode="json"),
            ),
        )

    def retorno(self, payload: CTFRetornoRequestDTO) -> Response:
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
