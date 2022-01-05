from abc import ABC, abstractmethod

from finance.models import Customer


class IEntityDAO(ABC):
    @staticmethod
    @abstractmethod
    def get_all(name: str) -> Customer:
        """ get all entities"""
