from typing import Any

from homero.enum import JobNameEnum


class JobIdentifier:

    @staticmethod
    def identify(payload: dict) -> tuple[JobNameEnum, dict[str, Any]]:
        if not payload:
            raise ValueError("Payload vazio")

        first_key = next(iter(payload))

        try:
            return JobNameEnum(first_key), payload[first_key]
        except ValueError:
            raise ValueError(f"Processo inválido: {first_key}")
