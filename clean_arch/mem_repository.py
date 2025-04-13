from clean_arch.entities import User
from clean_arch.interfaces import UserRepository

# Frameworks and Drivers (Outermost layer: Repositories, Web)


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: dict[str, User] = {}

    def add_user(self, user: User) -> User:
        self.users[user.id] = user
        return user

    def get_user(self, user_id: str) -> User | None:
        return self.users.get(user_id)


# Dependency Injection of the repository. Note: I use a global variable here.
# Normally, you would connect to a database.
REPOSITORY = InMemoryUserRepository()


def get_repository():
    return REPOSITORY
