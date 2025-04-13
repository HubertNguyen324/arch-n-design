from hex_arch.domain import User
from hex_arch.interface import UserRepository

# Core Application Service


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_id: str, name: str):
        user = User(user_id, name)
        return self.repository.add_user(user)

    def find_user(self, user_id: str):
        return self.repository.get_user(user_id)
