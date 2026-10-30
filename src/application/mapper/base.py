from typing import Any

from odysseia.request.base import BaseProdutosRequestDTO
from odysseia.request.cotefacil.base import CTFLBaseProdutosRequestDTO


class BaseProdutosMapper:

    @staticmethod
    def to_middleware(
        request: BaseProdutosRequestDTO,
        platform: dict[str, Any],
    ) -> CTFLBaseProdutosRequestDTO:
        return CTFLBaseProdutosRequestDTO(
            cnpj_fornecedor=request.fornecedor.cnpj,
            url_acesso=request.fornecedor.url_acesso,
            dadoAuxiliar=request.fornecedor.dado_auxiliar,
            usuario=request.login.usuario if request.login else None,
            senha=request.login.senha if request.login else None,
            use_zt="true" if request.conexao.zt else "false",
            idRepresentante=platform.get("idRepresentante", 0),
            cnpj_cliente=request.cliente.cnpj,
            codigo=request.cliente.codigo,
            codigo_auxiliar=request.cliente.dado_auxiliar,
        )
