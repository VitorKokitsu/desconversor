from os import environ
from secrets import compare_digest
from typing import Annotated

from fastapi import Header, HTTPException


def validar_api_key(api_key: Annotated[str | None, Header(alias="X-API-Key")] = None) -> None:
    api_key_esperada = environ.get("API_KEY")
    if not api_key_esperada or not api_key or not compare_digest(api_key, api_key_esperada):
        raise HTTPException(status_code=401, detail="API key inválida")
