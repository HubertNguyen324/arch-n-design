from entities.user import User
from interfaces.repository import ICurdRepository


class InMemoryReposity(ICurdRepository[User]):
    def __init__(self) -> None:
        self.database: dict[str, User] = {}

    def get_all(self) -> list[User]:
        return list(self.database.values())

    def get_by_id(self, id: str) -> User:
        try:
            user = self.database.get(id)
            if not user:
                raise Exception("User not found")
            return user
        except Exception as e:
            raise e

    def add(self, entity: User) -> None:
        self.database[str(entity.id)] = entity

    def update(self, entity: User) -> None:
        self.database[str(entity.id)] = entity

    def delete(self, entity: User) -> None:
        del self.database[str(entity.id)]
