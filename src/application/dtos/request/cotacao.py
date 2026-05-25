from typing import Annotated, Optional

from pydantic import StringConstraints
from pydantic.main import BaseModel


class CotacaoClienteItemDTO(BaseModel):
    ean: str
    codigo_produto: str
    descricao_produto: str
    quantidade_cotada: int | float
    controle_preco: str


class CotacaoClienteDTO(BaseModel):
    codigo: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    cnpj_cliente: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    codigo_condicao_pagamento: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    codigo_cotacao: int
    idPrazoPromocao: int = 0
    codigo_auxiliar: Optional[str] = ...
    multiplas_respostas: bool
    itens: list[CotacaoClienteItemDTO]


class CTFCotacaoRequestDTO(BaseModel):
    cnpj_fornecedor: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    usuario: str
    senha: str
    codigo_cotacao_matriz: int
    idRepresentante: int = 0
    clientes: list[CotacaoClienteDTO]
    url_acesso: str | None = ""
    dadoAuxiliar: str = ""
    use_zt: str = "true"
