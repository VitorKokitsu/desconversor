from fastapi import APIRouter

from app.presenter.schemas.process_conversor_request import ProcessConversorRequest
from dependencies import build_process_conversor

router = APIRouter()


@router.post("/conversor")
def conversor(request: ProcessConversorRequest):
    use_case = build_process_conversor()

    return use_case.execute(request.transaction_id, request.permite_envio)
