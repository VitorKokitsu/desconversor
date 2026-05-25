from application.dtos.request.autenticacao import AutenticacaoRequestDTO
from application.dtos.request.condpgto import CTFCondigcaoPagamentoRequestDTO
from application.dtos.request.cotacao import CTFCotacaoRequestDTO
from application.dtos.request.retorno import CTFRetornoRequestDTO
from application.dtos.response.middleware import MiddlewareResponse, MiddlewareResponseData
from domain.ports.middleware_port import MiddlewareClientPort
from infrastructure.middleware.exchanger import MiddlewareExchanger


class MiddlewareClient(MiddlewareClientPort):
    def __init__(self, exchanger: MiddlewareExchanger) -> None:
        self.exchanger = exchanger

    def send_autenticacao(self, payload: AutenticacaoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.autenticacao(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_condpgto(self, payload: CTFCondigcaoPagamentoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.condpgto(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_cotacao(self, payload: CTFCotacaoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.cotacao(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_pedido(self, payload) -> MiddlewareResponse:
        return None

    def send_retorno(self, payload: CTFRetornoRequestDTO) -> MiddlewareResponseData:
        response = self.exchanger.retorno(payload=payload)

        return MiddlewareResponseData(**response.json())
