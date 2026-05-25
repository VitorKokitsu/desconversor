from odysseia.request.cotacao import CotacaoRequestDTO
from odysseia.request.cotefacil.cotacao import (
    CTFLCotacaoRequestDTO,
    CTFLCotacaoRequestClienteDTO,
    CTFLCotacaoRequestItemDTO,
)

class CotacaoMapper:

    @staticmethod
    def to_middleware(request: CotacaoRequestDTO) -> CTFLCotacaoRequestDTO:
        prazo = (
            "/".join(str(p) for p in sorted(request.pagamento.prazo))
            if request.pagamento.prazo
            else "7"
        )

        condicao_pagamento =  (
            f"{request.pagamento.codigo}::"
            f"{request.pagamento.forma}::"
            f"{request.pagamento.metodo}::"
            f"{prazo}"
        )

        return CTFLCotacaoRequestDTO(
            cnpj_fornecedor=request.fornecedor.cnpj,
            url_acesso=request.fornecedor.url_acesso,
            dadoAuxiliar=request.fornecedor.dado_auxiliar or "-",
            usuario=request.login.usuario if request.login else None,
            senha=request.login.senha if request.login else None,
            use_zt="true" if request.conexao.zt else "false",
            idRepresentante=request.promocao.prazo_promocao,
            codigo_cotacao_matriz=request.id,
            clientes=[
                CTFLCotacaoRequestClienteDTO(
                    codigo_cotacao=request.id,
                    codigo_condicao_pagamento=condicao_pagamento,
                    itens=[
                        CTFLCotacaoRequestItemDTO(
                            ean=item.gtin,
                            codigo_produto=item.codigo,
                            descricao_produto=item.descricao or "-",
                            quantidade_cotada=item.quantidade,
                            controle_preco=item.controle,
                        )
                        for item in request.itens
                    ],
                    multiplas_respostas=request.promocao.multiplas_ofertas,
                    idPrazoPromocao=request.promocao.prazo_promocao,
                    cnpj_cliente=request.cliente.cnpj,
                    codigo=request.cliente.codigo,
                    codigo_auxiliar=request.cliente.dado_auxiliar or None,
                )
            ],
        )
