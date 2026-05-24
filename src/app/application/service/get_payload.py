from typing import Any

from homero.enum import JobNameEnum


class GetPayload:
    IGNORED_METADATA_KEYS = {"id", "id_key", "transaction_id"}

    @staticmethod
    def separate_data(raw_payload: dict[str, Any]) -> tuple[JobNameEnum, str, dict[str, Any]]:
        job_key = next(
            (key for key in raw_payload if key in {job.value for job in JobNameEnum}),
            None,
        )
        if not job_key:
            raise ValueError("Payload sem processo suportado")

        platform_key = next(
            (
                key
                for key in raw_payload
                if key != job_key and key not in GetPayload.IGNORED_METADATA_KEYS
            ),
            None,
        )
        if not platform_key:
            raise ValueError("Payload sem dados de plataforma")

        return JobNameEnum(job_key), platform_key, raw_payload[job_key]
