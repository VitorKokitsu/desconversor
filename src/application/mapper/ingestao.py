from odysseia.mixins import PagamentoDTO
from odysseia.platform import PedprecoPlatformDTO
from odysseia.request.cotacao import CotacaoRequestDTO
from odysseia.request.pedpreco.ingestao import PPIngestaoRequestDTO


class IngestaoMapper:
    """Inverso do PPIngestaoConverter da lib protheus (ingestão -> cotação)."""

    @staticmethod
    def to_middleware(request: CotacaoRequestDTO, platform: PedprecoPlatformDTO) -> PPIngestaoRequestDTO:
        fornecedor = request.fornecedor
        cliente = request.cliente
        login = request.login

        # O DTO usa alias_generator sem validate_by_name: os campos precisam ser informados pelos aliases.
        return PPIngestaoRequestDTO.model_validate(
            {
                "cnpj_entrega": fornecedor.cnpj,
                "nome_entrega": fornecedor.nome_fantasia,
                "uf_entrega": fornecedor.uf,
                "url_acesso": fornecedor.url_acesso,
                "codigo_auxiliar": fornecedor.dado_auxiliar,
                "cnpj_cliente": cliente.cnpj,
                "uf_cliente": cliente.uf,
                "codigo_cliente": cliente.codigo,
                "codigo_auxiliar_cliente": cliente.dado_auxiliar,
                "usuario": login.usuario if login else None,
                "senha": login.senha if login else None,
                "use_zt": "true" if request.conexao.zt else "false",
                "preferencia_prazo": IngestaoMapper._preferencia_prazo(request.pagamento),
                "id_loja": platform.id_loja,
                "id_integracao": platform.id_integracao,
                "id_laboratorio": platform.id_laboratorio,
                "nome_integracao": platform.nome_integracao,
                "origem_integracao": platform.origem_integracao,
                "codigo_auxiliar_fornecedor_ol": platform.codigo_auxiliar_fornecedor_ol,
                "codigo_auxiliar_lab_integracao": platform.codigo_auxiliar_lab_integracao,
            }
        )

    @staticmethod
    def _preferencia_prazo(pagamento: PagamentoDTO | None) -> set[str]:
        # Sem preferência de prazo, o Protheus envia a ingestão sem pagamento (qualquer prazo).
        if not pagamento or not isinstance(pagamento.prazo, set):
            return set()

        return {"/".join(str(dia) for dia in sorted(pagamento.prazo))}
