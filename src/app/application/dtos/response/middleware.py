from pydantic import BaseModel

class MiddlewareResponseData(BaseModel):
    region: str
    bucket_name: str
    queue_name: str
    transaction_id: str
    message_id: str | None
    job_id: str | None

class MiddlewareResponse(BaseModel):
    data: list[MiddlewareResponseData]
