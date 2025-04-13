
from hex_arch.domain import User
from hex_arch.interface import UserRepository

# Adapter for In-memory Repository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: dict[str, User] = {}

    def add_user(self, user: User) -> User:
        self.users[user.id] = user
        print(user)
        return user

    def get_user(self, user_id: str) -> User | None:
        return self.users.get(user_id)


# Dependency Injection of the repository. Note: I use a global variable here.
# Normally, you would connect to a database.
REPOSITORY = InMemoryUserRepository()


def get_repository():
    return REPOSITORY
