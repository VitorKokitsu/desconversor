from odysseia.request.condpgto import CondicaoPagamentoRequestDTO
from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestClienteDTO, CTFLCondicaoPagamentoRequestDTO


class CondpgtoMapper:

    @staticmethod
    def to_middleware(request_dto: CondicaoPagamentoRequestDTO) -> CTFLCondicaoPagamentoRequestDTO:
        return CTFLCondicaoPagamentoRequestDTO(
            cnpj=request_dto.cliente.cnpj,
            codigocliente=request_dto.cliente.codigo,
            siteFornecedor=request_dto.fornecedor.url_acesso,
            cnpjFornecedor=request_dto.fornecedor.cnpj,
            novoPadrao=True,
            clientes=[
                CTFLCondicaoPagamentoRequestClienteDTO(
                    codigo=request_dto.cliente.codigo,
                    cnpj_cliente=request_dto.cliente.cnpj,
                    codigo_auxiliar=request_dto.cliente.dado_auxiliar,
                )
            ],
            urlAcesso=request_dto.fornecedor.url_acesso,
            usuario=request_dto.login.usuario if request_dto.login else "-",
            senha=request_dto.login.senha if request_dto.login else "-",
            cnpj_fornecedor=request_dto.fornecedor.cnpj,
            idRepresentante=0,
            url_acesso=request_dto.fornecedor.url_acesso,
            dadoAuxiliar=request_dto.fornecedor.dado_auxiliar,
            use_zt="true" if request_dto.conexao.zt else "false",
        )
