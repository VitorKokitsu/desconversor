from typing import Any

from odysseia.enums import IDPrazoPromocaoEnum, TipoEmbalagemPedidoEnum
from odysseia.request.cotefacil.pedido import (
    CTFLPedidoRequestDTO,
    CTFLPedidoRequestClienteDTO,
    CTFLPedidoRequestItemDTO,
)
from odysseia.request.pedido import PedidoRequestDTO

from application.service.protheus_payment import ProtheusPayment


class PedidoMapper:

    @staticmethod
    def to_middleware(
        request: PedidoRequestDTO,
        platform: dict[str, Any],
    ) -> CTFLPedidoRequestDTO:
        return CTFLPedidoRequestDTO(
            cnpj_fornecedor=request.fornecedor.cnpj,
            url_acesso=request.fornecedor.url_acesso,
            dadoAuxiliar=request.fornecedor.dado_auxiliar,
            usuario=request.login.usuario if request.login else None,
            senha=request.login.senha if request.login else None,
            use_zt="true" if request.conexao.zt else "false",
            idRepresentante=platform.get("idRepresentante", 0),
            clientes=[
                CTFLPedidoRequestClienteDTO(
                    codigo_pedido_cotefacil=request.id,
                    codigo_cotacao=request.id_cotacao,
                    codigo_pedido_cliente=request.codigo_pedido_cliente,
                    numero_pedido_site=request.codigo_pedido_fornecedor,
                    codigo_condicao_pagamento=ProtheusPayment.build(request.pagamento),
                    idPrazoPromocao=(
                        request.promocao.prazo_promocao
                        if request.promocao
                        else IDPrazoPromocaoEnum.QUALQUER_PRAZO
                    ),
                    cnpj_cliente=request.cliente.cnpj,
                    codigo=request.cliente.codigo,
                    codigo_auxiliar=request.cliente.dado_auxiliar,
                    itens=[
                        CTFLPedidoRequestItemDTO(
                            ean=item.gtin,
                            codigo_produto=item.codigo,
                            descricao=item.descricao,
                            tipo_embalagem=TipoEmbalagemPedidoEnum(item.embalagem.tipo.value.lower()),
                            quantidade_embalagem=item.embalagem.quantidade,
                            quantidade=item.quantidade,
                            codigo_faturamento=item.promocao or "",
                            preco_fabrica=item.preco_bruto,
                            descontoInformado=item.desconto,
                            preco_sem_st=item.valor_sem_st or 0.0,
                            preco_com_st=item.valor_liquido or 0.0,
                            preco_liquido=item.valor_liquido or 0.0,
                        )
                        for item in request.itens
                    ],
                )
            ],
        )
