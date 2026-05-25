from typing import Any

from homero.enum import JobNameEnum


class GetPayload:
    IGNORED_METADATA_KEYS = {"id", "id_key", "transaction_id"}

    @staticmethod
    def separate_data(raw_payload: dict[str, Any]) -> tuple[JobNameEnum, str, dict[str, Any]]:
        [process_key, platform_key, _] = raw_payload.keys()

        return JobNameEnum(process_key), platform_key, raw_payload[process_key]
