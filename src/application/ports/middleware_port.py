from abc import ABC, abstractmethod

from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestDTO
from odysseia.request.cotefacil.cotacao import CTFLCotacaoRequestDTO
from odysseia.request.cotefacil.pedido import CTFLPedidoRequestDTO
from odysseia.request.cotefacil.retorno import CTFLRetornoFaturamentoRequestDTO
from odysseia.request.pedpreco.autenticacao import PPAutenticacaoRequestDTO

from application.dtos.response.middleware import MiddlewareResponse


class MiddlewareClientPort(ABC):

    @abstractmethod
    def send_autenticacao(self, payload: PPAutenticacaoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_condpgto(self, payload: CTFLCondicaoPagamentoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_cotacao(self, payload: CTFLCotacaoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_pedido(self, payload: CTFLPedidoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_retorno(self, payload: CTFLRetornoFaturamentoRequestDTO) -> MiddlewareResponse:
        pass
