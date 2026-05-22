from app.application.dtos.request.condpgto import CTFCondigcaoPagamentoRequestDTO
from app.application.dtos.request.cotacao import CTFCotacaoRequestDTO
from app.application.dtos.request.retorno import CTFRetornoRequestDTO
from app.application.dtos.response.middleware import MiddlewareResponse, MiddlewareResponseData
from app.domain.ports.middleware_port import MiddlewareClientPort
from app.infrastructure.middleware.exchanger import MiddlewareExchanger


class MiddlewareClient(MiddlewareClientPort):
    exchanger: MiddlewareExchanger

    def send_condpgto(self, payload: CTFCondigcaoPagamentoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.condpgto(payload=payload)

        return MiddlewareResponse(data=response.json())

    def send_cotacao(self, payload: CTFCotacaoRequestDTO) -> MiddlewareResponse:
        response = self.exchanger.cotacao(payload=payload)

        return MiddlewareResponse(data=response.json())

    # def send_pedido(self, payload: dict[str, Any]) -> MiddlewareResponse:
    #     response = self.exchanger.pedido(params=HecateParams(), payload=payload)
    #
    #     return MiddlewareResponse(data=response.json())

    def send_retorno(self, payload: CTFRetornoRequestDTO) -> MiddlewareResponseData:
        response = self.exchanger.retorno(payload=payload)

        return MiddlewareResponseData(**response.json())
