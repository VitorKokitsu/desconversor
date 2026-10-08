from odysseia.request.cotacao import CotacaoRequestDTO

from application.enums import PlataformaEnum


class IdentificadorProcesso:
    """Identifica de qual processo antigo do middleware o payload do Protheus foi derivado."""

    @staticmethod
    def deriva_de_ingestao(platform: str, cotacao: CotacaoRequestDTO) -> bool:
        # A ingestão (PedPreço) é uma cotação sem itens: o fornecedor devolve o catálogo inteiro.
        return platform == PlataformaEnum.PEDPRECO or not cotacao.itens

    @staticmethod
    def deriva_de_autenticacao(platform: str) -> bool:
        # A autenticação (PedPreço) é convertida pelo Protheus em uma condição de pagamento.
        return platform == PlataformaEnum.PEDPRECO
