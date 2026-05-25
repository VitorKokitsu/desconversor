from typing import Annotated

from odysseia.request.cotefacil.retorno import CTFLRetornoFaturamentoRequestDTO
from pydantic import StringConstraints


class CTFRetornoRequestDTO(CTFLRetornoFaturamentoRequestDTO):
    cnpj_fornecedor: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    usuario: Annotated[str, StringConstraints(strip_whitespace=False)]
    senha: Annotated[str, StringConstraints(strip_whitespace=False)]
    idRepresentante: int = 0
    url_acesso: str | None
    dadoAuxiliar: str | None
    use_zt: str = "true"
    use_proxy: str = "true"
