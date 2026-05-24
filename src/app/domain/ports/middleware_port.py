from abc import ABC, abstractmethod

from app.application.dtos.request.autenticacao import AutenticacaoRequestDTO
from app.application.dtos.request.condpgto import CTFCondigcaoPagamentoRequestDTO
from app.application.dtos.request.cotacao import CTFCotacaoRequestDTO
from app.application.dtos.request.retorno import CTFRetornoRequestDTO
from app.application.dtos.response.middleware import MiddlewareResponse


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
