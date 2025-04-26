from pydantic import BaseModel
from typing import TypeVar

BaseEntity = TypeVar("BaseEntity", bound=BaseModel)
