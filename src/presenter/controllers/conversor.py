from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from presenter.schemas.process_conversor_request import ProcessConversorRequest
from dependencies import build_process_conversor

router = APIRouter()


@router.post("/conversor")
def conversor(request: ProcessConversorRequest):
    use_case = build_process_conversor()
    return _execute_or_400(lambda: use_case.execute(request.transaction_id, allow_send=False))


@router.post("/conversor/enviar")
def enviar(request: ProcessConversorRequest):
    use_case = build_process_conversor(require_middleware=True)
    return _execute_or_400(lambda: use_case.execute(request.transaction_id, allow_send=True))


@router.post("/conversor/payload")
def payload(payload: dict[str, Any]):
    use_case = build_process_conversor()
    return _execute_or_400(lambda: use_case.payload(raw_payload=payload, allow_send=False))

@router.post("/conversor/payload/enviar")
def payload(payload: dict[str, Any]):
    use_case = build_process_conversor(require_middleware=True)
    return _execute_or_400(lambda: use_case.payload(raw_payload=payload, allow_send=True))

def _execute_or_400(handler):
    try:
        return handler()
    except (KeyError, ValueError, ValidationError) as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
