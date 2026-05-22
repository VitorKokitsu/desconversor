from pydantic import BaseModel


class ProcessConversorRequest(BaseModel):
    transaction_id: str
    permite_envio: bool
