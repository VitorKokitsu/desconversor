from app.application.use_cases.process_conversor import ProcessConversorUseCase
from app.infrastructure.middleware.client import MiddlewareClient
from app.infrastructure.get_payload_data import GetPayloadData


def build_process_conversor() -> ProcessConversorUseCase:
    s3_connection = GetPayloadData()

    return ProcessConversorUseCase(
        get_payload=s3_connection,
    )
