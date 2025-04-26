from typing import Any

from pydantic import ValidationError
from interfaces.repository import ICurdRepository
from entities.user import User


class UserCrudService:
    def __init__(self, repository: ICurdRepository[User]) -> None:
        self.repository = repository

    def create(self, data: dict[str, Any]) -> User:
        try:
            new_user = User.model_validate(data)
        except ValidationError as e:
            raise e
        self.repository.add(new_user)
        return new_user

    def read_by_id(self, id: int) -> User:
        try:
            return self.repository.get_by_id(id)
        except Exception as e:
            raise e

    def update_by_id(self, id: int, data: dict[str, Any]) -> None:
        try:
            user = self.repository.get_by_id(id)
            if user:
                updated_user = user.model_copy(update=data)
                self.repository.update(updated_user)
        except Exception as e:
            raise e

    def delete_by_id(self, id: int) -> None:
        try:
            user = self.repository.get_by_id(id)
            if user:
                self.repository.delete(user)
        except Exception as e:
            raise e
