from abc import ABC, abstractmethod


class Serializer(ABC):
    """Define abstract serialize/deserilize methods"""
    @abstractmethod
    def serialize(self, data: list):
        pass

    @abstractmethod
    def deserialize(self, path: str):
        pass