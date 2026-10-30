from odysseia.enums import TipoEmbalagemPedidoEnum
from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.pedpreco.retorno import PPRetornoFaturamentoRequestDTO
from odysseia.request.retorno import RetornoFaturamentoRequestDTO

from application.service.protheus_payment import ProtheusPayment


class RetornoPedprecoMapper:

    @staticmethod
    def to_middleware(
        request: RetornoFaturamentoRequestDTO,
        platform: PedprecoPlatformDTO,
    ) -> PPRetornoFaturamentoRequestDTO:
        fornecedor = request.fornecedor
        cliente = request.cliente
        login = request.login

        return PPRetornoFaturamentoRequestDTO.model_validate(
            {
                "cnpj_fornecedor": fornecedor.cnpj,
                "url_acesso": fornecedor.url_acesso,
                "dadoAuxiliar": fornecedor.dado_auxiliar,
                "usuario": login.usuario if login else "-",
                "senha": login.senha if login else "-",
                "use_zt": "true" if request.conexao.zt else "false",
                "use_proxy": "true" if request.conexao.proxy else "false",
                "id_integracao": platform.id_integracao,
                "id_laboratorio": platform.id_laboratorio,
                "dataEnvio": request.data_envio.strftime("%d/%m/%Y %H:%M:%S"),
                "itens": [
                    {
                        "ean": item.gtin,
                        "codigo_produto": item.codigo,
                        "descricao": item.descricao,
                        "tipo_embalagem": TipoEmbalagemPedidoEnum(item.embalagem.tipo.value.lower()),
                        "quantidade_embalagem": item.embalagem.quantidade,
                        "codigo_faturamento": item.promocao,
                        "quantidade": item.quantidade,
                        "preco_fabrica": item.preco_bruto,
                        "preco_liquido": item.valor_liquido or 0.0,
                        "preco_com_st": item.valor_liquido,
                        "preco_sem_st": item.valor_sem_st or 0.0,
                        "descontoInformado": item.desconto,
                    }
                    for item in request.itens
                ],
                "clientes": [
                    {
                        "cnpj_cliente": cliente.cnpj,
                        "codigo": cliente.codigo,
                        "codigo_auxiliar": cliente.dado_auxiliar,
                        "id_loja": platform.id_loja,
                        "codigo_cotacao": request.id_cotacao,
                        "codigo_pedido_cotefacil": request.id,
                        "codigo_pedido_site": request.codigo_pedido_fornecedor,
                        "motivo": "-",
                        "codigo_condicao_pagamento": ProtheusPayment.build(request.pagamento),
                    }
                ],
            }
        )
