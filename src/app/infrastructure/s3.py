from os import environ
from typing import Any

from homero.aws.s3 import get_s3_object

from app.domain.ports.s3_port import S3Port


class S3Connection(S3Port):
    def get_object(self, key: str) -> dict[str, Any]:
        s3_object = get_s3_object(
            bucket_name=environ["TRANSACTION_BUCKET"],
            object_key=key,
        )

        return s3_object
