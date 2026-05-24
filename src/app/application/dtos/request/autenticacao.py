from typing import Annotated

from pydantic import BaseModel, StringConstraints


class AutenticacaoClienteRequestDTO(BaseModel):
    cnpj_cliente: str | None = ""
    usuario: str | None = ""
    senha: str | None = ""
    id_loja: int


class AutenticacaoRequestDTO(BaseModel):
    clientes: list[AutenticacaoClienteRequestDTO]
    id_integracao: int | None = None
    cnpj_fornecedor: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] | None = None
    url_acesso: str | None = ""
    use_zt: str = "false"
    id_laboratorio: int | None = None
    id_lab_integracao: int | None = None
