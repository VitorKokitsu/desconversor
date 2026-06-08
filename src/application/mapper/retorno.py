from odysseia.enums import TipoEmbalagemPedidoEnum
from odysseia.request.cotefacil.retorno import (
    CTFLRetornoFaturamentoRequestClienteDTO,
    CTFLRetornoFaturamentoRequestItemDTO, CTFLRetornoFaturamentoRequestDTO,
)
from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from application.service.protheus_payment import ProtheusPayment


class RetornoMapper:

    @staticmethod
    def to_middleware(request: RetornoFaturamentoRequestDTO) -> CTFLRetornoFaturamentoRequestDTO:
        return CTFLRetornoFaturamentoRequestDTO(
            itens=[
                CTFLRetornoFaturamentoRequestItemDTO(
                    ean=item.gtin,
                    codigo_produto=item.codigo,
                    tipo_embalagem=TipoEmbalagemPedidoEnum(item.embalagem.tipo.value.lower()),
                    quantidade_embalagem=item.embalagem.quantidade,
                    codigo_faturamento=item.promocao,
                    quantidade=item.quantidade,
                    preco_fabrica=item.preco_bruto,
                    preco_liquido=item.valor_liquido or 0.0,
                    preco_com_st=item.valor_liquido,
                    preco_sem_st=item.valor_sem_st or 0.0,
                    descricao=item.descricao,
                    descontoInformado=item.desconto,
                )
                for item in request.itens
            ],
            clientes=[
                CTFLRetornoFaturamentoRequestClienteDTO(
                    codigo=request.cliente.codigo,
                    cnpj_cliente=request.cliente.cnpj,
                    codigo_auxiliar=request.cliente.dado_auxiliar,
                    codigo_cotacao=request.id_cotacao,
                    codigo_pedido_cotefacil=request.id,
                    codigo_pedido_site=request.codigo_pedido_fornecedor,
                    motivo="-",
                    codigo_condicao_pagamento=ProtheusPayment.build(request.pagamento),
                )
            ],
            dataEnvio=request.data_envio.strftime("%d/%m/%Y %H:%M:%S"),
            fila=None,
            cnpj_fornecedor=request.fornecedor.cnpj,
            usuario=request.login.usuario if request.login else "-",
            senha=request.login.senha if request.login else "-",
            idRepresentante=0,
            url_acesso=request.fornecedor.url_acesso,
            dadoAuxiliar=request.fornecedor.dado_auxiliar,
            use_zt="true" if request.conexao.zt else "false",
            use_proxy="true" if request.conexao.proxy else "false",
        )
