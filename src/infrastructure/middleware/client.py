from odysseia.request.cotefacil.base import CTFLBaseProdutosRequestDTO
from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestDTO
from odysseia.request.cotefacil.cotacao import CTFLCotacaoRequestDTO
from odysseia.request.cotefacil.pedido import CTFLPedidoRequestDTO
from odysseia.request.cotefacil.retorno import CTFLRetornoFaturamentoRequestDTO
from odysseia.request.pedpreco.autenticacao import PPAutenticacaoRequestDTO
from odysseia.request.pedpreco.ingestao import PPIngestaoRequestDTO
from odysseia.request.pedpreco.pedido import PPPedidoRequestDTO
from odysseia.request.pedpreco.retorno import PPRetornoFaturamentoRequestDTO

from application.dtos.response.middleware import MiddlewareResponse, MiddlewareResponseData
from application.ports.middleware_port import MiddlewareClientPort
from infrastructure.middleware.exchanger import MiddlewareExchanger


class MiddlewareClient(MiddlewareClientPort):
    def __init__(self, exchanger: MiddlewareExchanger) -> None:
        self.exchanger = exchanger

    def send_autenticacao(self, payload: PPAutenticacaoRequestDTO, nome_config: str) -> MiddlewareResponse:
        response = self.exchanger.autenticacao(payload=payload, nome_config=nome_config)

        return MiddlewareResponse(data=response.json())

    def send_ingestao(self, payload: PPIngestaoRequestDTO, nome_config: str) -> MiddlewareResponse:
        response = self.exchanger.ingestao(payload=payload, nome_config=nome_config)

        # A rota de ingestão responde uma única transação, e não uma lista.
        return MiddlewareResponse(data=[response.json()])

    def send_base(self, payload: CTFLBaseProdutosRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.base(payload=payload)

        return MiddlewareResponse(data=[response.json()])

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

    def send_pedido_pedpreco(self, payload: PPPedidoRequestDTO, nome_config: str) -> MiddlewareResponse:
        raise ValueError("Processo de pedido bloqueado para envio")

    def send_retorno_pedpreco(self, payload: PPRetornoFaturamentoRequestDTO, nome_config: str) -> MiddlewareResponse:
        response = self.exchanger.retorno_pedpreco(payload=payload, nome_config=nome_config)

        return MiddlewareResponse(data=[response.json()])
