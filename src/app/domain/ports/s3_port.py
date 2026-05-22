from abc import ABC, abstractmethod


class S3Port(ABC):

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass
