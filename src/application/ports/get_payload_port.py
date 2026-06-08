from abc import ABC, abstractmethod


class PayloadStorage(ABC):

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass
