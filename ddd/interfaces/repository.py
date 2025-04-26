from typing import Generic
from abc import ABC, abstractmethod

from value_objects.generic import BaseEntity


class ICurdRepository(ABC, Generic[BaseEntity]):
    @abstractmethod
    def get_all(self) -> list[BaseEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: str) -> BaseEntity:
        raise NotImplementedError

    @abstractmethod
    def add(self, entity: BaseEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: BaseEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity: BaseEntity) -> None:
        raise NotImplementedError
