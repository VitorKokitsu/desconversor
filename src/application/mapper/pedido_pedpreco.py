from odysseia.enums import TipoEmbalagemPedidoEnum
from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.pedido import PedidoRequestDTO
from odysseia.request.pedpreco.pedido import PPPedidoRequestDTO

from application.service.protheus_payment import ProtheusPayment


class PedidoPedprecoMapper:

    @staticmethod
    def to_middleware(request: PedidoRequestDTO, platform: PedprecoPlatformDTO) -> PPPedidoRequestDTO:
        fornecedor = request.fornecedor
        cliente = request.cliente
        login = request.login

        return PPPedidoRequestDTO.model_validate(
            {
                "cnpj_fornecedor": fornecedor.cnpj,
                "url_acesso": fornecedor.url_acesso,
                "dadoAuxiliar": fornecedor.dado_auxiliar,
                "usuario": login.usuario if login else None,
                "senha": login.senha if login else None,
                "use_zt": "true" if request.conexao.zt else "false",
                "id_integracao": platform.id_integracao,
                "id_laboratorio": platform.id_laboratorio,
                "clientes": [
                    {
                        "cnpj_cliente": cliente.cnpj,
                        "codigo": cliente.codigo,
                        "codigo_auxiliar": cliente.dado_auxiliar,
                        "id_loja": platform.id_loja,
                        "codigo_cotacao": request.id_cotacao,
                        "codigo_pedido_cotefacil": request.id,
                        "numero_pedido_site": request.codigo_pedido_fornecedor,
                        "codigo_pedido_cliente": request.codigo_pedido_cliente,
                        "codigo_condicao_pagamento": ProtheusPayment.build(request.pagamento),
                        "itens": [
                            {
                                "ean": item.gtin,
                                "codigo_produto": item.codigo,
                                "descricao": item.descricao,
                                "tipo_embalagem": TipoEmbalagemPedidoEnum(item.embalagem.tipo.value.lower()),
                                "quantidade_embalagem": item.embalagem.quantidade,
                                "quantidade": item.quantidade,
                                "codigo_faturamento": item.promocao or "",
                                "preco_fabrica": item.preco_bruto,
                                "descontoInformado": item.desconto,
                                "preco_sem_st": item.valor_sem_st or 0.0,
                                "preco_com_st": item.valor_liquido or 0.0,
                                "preco_liquido": item.valor_liquido or 0.0,
                            }
                            for item in request.itens
                        ],
                    }
                ],
            }
        )
