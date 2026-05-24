from typing import Any

from odysseia.request.condpgto import CondicaoPagamentoRequestDTO

from app.application.dtos.request.autenticacao import AutenticacaoRequestDTO, AutenticacaoClienteRequestDTO


class AutenticacaoMapper:

    @staticmethod
    def to_middleware(request: CondicaoPagamentoRequestDTO, pp_platform: dict[str, Any]):
        return AutenticacaoRequestDTO(
            clientes=[
                AutenticacaoClienteRequestDTO(
                    cnpj_cliente=request.cliente.cnpj,
                    usuario=request.login.usuario if request.login else None,
                    senha=request.login.senha if request.login else None,
                    id_loja=pp_platform["id_loja"],
                )
            ],
            id_integracao=pp_platform["id_integracao"],
            cnpj_fornecedor=request.fornecedor.cnpj,
            url_acesso=request.fornecedor.url_acesso,
            use_zt="false",
            id_laboratorio=pp_platform["id_laboratorio"],
            id_lab_integracao=pp_platform["id_lab_integracao"],
        )
