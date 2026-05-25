from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestDTO
from odysseia.request.cotefacil.cotacao import CTFLCotacaoRequestDTO
from odysseia.request.cotefacil.pedido import CTFLPedidoRequestDTO
from odysseia.request.cotefacil.retorno import CTFLRetornoFaturamentoRequestDTO
from odysseia.request.pedpreco.autenticacao import PPAutenticacaoRequestDTO

from application.dtos.response.middleware import MiddlewareResponse, MiddlewareResponseData
from application.ports.middleware_port import MiddlewareClientPort
from infrastructure.middleware.exchanger import MiddlewareExchanger


class MiddlewareClient(MiddlewareClientPort):
    def __init__(self, exchanger: MiddlewareExchanger) -> None:
        self.exchanger = exchanger

    def send_autenticacao(self, payload: PPAutenticacaoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.autenticacao(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_condpgto(self, payload: CTFLCondicaoPagamentoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.condpgto(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_cotacao(self, payload: CTFLCotacaoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.cotacao(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_pedido(self, payload: CTFLPedidoRequestDTO) -> MiddlewareResponse:
        raise ValueError("Processo de pedido bloqueado para envio")

    def send_retorno(self, payload: CTFLRetornoFaturamentoRequestDTO) -> MiddlewareResponseData:
        response = self.exchanger.retorno(payload=payload)

        return MiddlewareResponseData(**response.json())
