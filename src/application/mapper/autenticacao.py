from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.condpgto import CondicaoPagamentoRequestDTO
from odysseia.request.pedpreco.autenticacao import PPAutenticacaoRequestDTO


class AutenticacaoMapper:
    """Inverso do PPAutenticacaoConverter da lib protheus (autenticação -> condição de pagamento)."""

    @staticmethod
    def to_middleware(request: CondicaoPagamentoRequestDTO, platform: PedprecoPlatformDTO) -> PPAutenticacaoRequestDTO:
        fornecedor = request.fornecedor
        cliente = request.cliente
        login = request.login

        # O DTO usa alias_generator sem validate_by_name: os campos precisam ser informados pelos aliases.
        return PPAutenticacaoRequestDTO.model_validate(
            {
                "cnpj_fornecedor": fornecedor.cnpj,
                "url_acesso": fornecedor.url_acesso,
                "codigo_auxiliar": fornecedor.dado_auxiliar,
                "use_zt": "true" if request.conexao.zt else "false",
                "id_integracao": platform.id_integracao,
                "id_laboratorio": platform.id_laboratorio,
                "id_lab_integracao": platform.id_lab_integracao,
                "clientes": [
                    {
                        "cnpj_cliente": cliente.cnpj,
                        "codigo_cliente": cliente.codigo,
                        "codigo_auxiliar": cliente.dado_auxiliar,
                        "id_loja": platform.id_loja,
                        "usuario": login.usuario if login else None,
                        "senha": login.senha if login else None,
                    }
                ],
            }
        )
