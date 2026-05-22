from app.application.services.job_identifier import JobIdentifier
from app.application.use_cases.process_conversor import ProcessConversorUseCase
from app.infrastructure.middleware.client import MiddlewareClient
from app.infrastructure.s3 import S3Connection


def build_process_conversor() -> ProcessConversorUseCase:
    s3_connection = S3Connection()
    middleware_client = MiddlewareClient()
    process_identifier = JobIdentifier()

    return ProcessConversorUseCase(
        s3=s3_connection,
        middleware_client=middleware_client,
        process_identifier=process_identifier,
    )
