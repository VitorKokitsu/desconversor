from typing import Annotated

from odysseia.request.cotefacil.condpgto import CTFLCondicaoPagamentoRequestDTO
from pydantic import StringConstraints


class CTFCondigcaoPagamentoRequestDTO(CTFLCondicaoPagamentoRequestDTO):
    usuario: Annotated[str, StringConstraints(min_length=1)]
    senha: Annotated[str, StringConstraints(min_length=1)]
    cnpj_fornecedor: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    idRepresentante: int = 0
    url_acesso: str | None = None
    dadoAuxiliar: str | None = None
    use_zt: str = "false"
