from os import environ

from httpx import Client

from application.use_cases.conversor import ConversorUseCase
from infrastructure.middleware.client import MiddlewareClient
from infrastructure.middleware.exchanger import MiddlewareExchanger
from infrastructure.middleware.routes import MiddlewareRoutes
from infrastructure.s3_connection import S3Connection


def build_middleware_client() -> MiddlewareClient:
    api_url = environ["MIDDLEWARE_API_URL"]
    routes = MiddlewareRoutes(api_url=api_url)
    exchanger = MiddlewareExchanger(client=Client(), routes=routes)
    return MiddlewareClient(exchanger=exchanger)


def build_process_conversor(require_middleware: bool = False) -> ConversorUseCase:
    s3_connection = S3Connection()

    return ConversorUseCase(
        get_payload=s3_connection,
        middleware_client=build_middleware_client() if require_middleware else None,
    )
