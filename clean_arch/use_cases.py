# Use Cases (one circle outside Entities)
from clean_arch.entities import User
from clean_arch.interfaces import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_id: str, name: str) -> User:
        user = User(user_id, name)
        return self.repository.add_user(user)

    def find_user(self, user_id: str) -> User | None:
        return self.repository.get_user(user_id)
