import json
from os import environ
from typing import Any

from homero.aws.s3 import get_s3_object
from homero.enum import JobNameEnum

from app.domain.ports.get_payload_port import GetPayloadPort


class GetPayloadData(GetPayloadPort):
    def get_object(self, key: str) -> tuple[JobNameEnum, str, dict[str, Any]]:
        s3_object = get_s3_object(
            bucket_name=environ["TRANSACTION_BUCKET"],
            object_key=key,
        )

        message_data = json.loads(s3_object["Body"].read())

        [process_key, platform_key, id_key] = message_data.keys()
        return JobNameEnum(process_key), platform_key, message_data[process_key]
