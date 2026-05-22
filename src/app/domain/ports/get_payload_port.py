from abc import ABC, abstractmethod


class GetPayloadPort(ABC):

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass
