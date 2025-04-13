from abc import ABC, abstractmethod
from hex_arch.domain import User

# Port (Interface)


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> User | None:
        pass
