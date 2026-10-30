from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/healthcheck", status_code=204)
def healthcheck() -> Response:
    return Response(status_code=204)
