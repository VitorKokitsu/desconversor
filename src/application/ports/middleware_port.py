from abc import ABC, abstractmethod

from application.dtos.request.autenticacao import AutenticacaoRequestDTO
from application.dtos.request.condpgto import CTFCondigcaoPagamentoRequestDTO
from application.dtos.request.cotacao import CTFCotacaoRequestDTO
from application.dtos.request.retorno import CTFRetornoRequestDTO
from application.dtos.response.middleware import MiddlewareResponse


class MiddlewareClientPort(ABC):

    @abstractmethod
    def send_autenticacao(self, payload: AutenticacaoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_condpgto(self, payload: CTFCondigcaoPagamentoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_cotacao(self, payload: CTFCotacaoRequestDTO) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_pedido(self, payload) -> MiddlewareResponse:
        pass

    @abstractmethod
    def send_retorno(self, payload: CTFRetornoRequestDTO) -> MiddlewareResponse:
        pass
