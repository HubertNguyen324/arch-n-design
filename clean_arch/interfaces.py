from abc import ABC, abstractmethod

from clean_arch.entities import User

# Interfaces (Ports)


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> User | None:
        pass
