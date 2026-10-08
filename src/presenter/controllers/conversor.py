from typing import Annotated, Any

from fastapi import APIRouter, HTTPException, Query
from pydantic import ValidationError

from presenter.schemas.process_conversor_request import ProcessConversorRequest
from dependencies import build_process_conversor

router = APIRouter()

NomeConfigQuery = Annotated[
    str | None,
    Query(description="Nome da configuração do middleware. Obrigatório para enviar processos do PedPreço."),
]


@router.post("/conversor")
def conversor(request: ProcessConversorRequest):
    use_case = build_process_conversor()
    return _execute_or_400(lambda: use_case.execute(request.transaction_id, allow_send=False))


@router.post("/conversor/enviar")
def enviar(request: ProcessConversorRequest, nome_config: NomeConfigQuery = None):
    use_case = build_process_conversor(require_middleware=True)
    return _execute_or_400(lambda: use_case.execute(request.transaction_id, allow_send=True, nome_config=nome_config))


@router.post("/conversor/payload")
def payload(payload: dict[str, Any]):
    use_case = build_process_conversor()
    return _execute_or_400(lambda: use_case.payload(raw_payload=payload, allow_send=False))

@router.post("/conversor/payload/enviar")
def payload_enviar(payload: dict[str, Any], nome_config: NomeConfigQuery = None):
    use_case = build_process_conversor(require_middleware=True)
    return _execute_or_400(lambda: use_case.payload(raw_payload=payload, allow_send=True, nome_config=nome_config))

def _execute_or_400(handler):
    try:
        return handler()
    except (KeyError, ValueError, ValidationError) as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
