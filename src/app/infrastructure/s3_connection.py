import json
from os import environ
from typing import Any

from homero.aws.s3 import get_s3_object

from app.domain.ports.get_payload_port import PayloadStorage


class S3Connection(PayloadStorage):
    def get_object(self, key: str) -> dict[str, Any]:
        s3_object = get_s3_object(
            bucket_name=environ["TRANSACTION_BUCKET"],
            object_key=key,
        )

        return json.loads(s3_object["Body"].read())
