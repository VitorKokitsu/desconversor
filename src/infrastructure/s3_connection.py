import json
import logging
from os import environ
from typing import Any

from homero.aws.s3 import get_s3_object

from application.ports.get_payload_port import PayloadStorage


class S3Connection(PayloadStorage):
    logger = logging.getLogger(__name__)

    def get_object(self, key: str) -> dict[str, Any]:
        try:
            s3_object = get_s3_object(
                bucket_name=environ["TRANSACTION_BUCKET"],
                object_key=key,
            )
        except Exception as ex:
            self.logger.info("Buscando payload de demo...", exc_info=ex)
            s3_object = get_s3_object(
                bucket_name=environ["TRANSACTION_BUCKET_DEMO"],
                object_key=key,
            )

        return json.loads(s3_object["Body"].read())
