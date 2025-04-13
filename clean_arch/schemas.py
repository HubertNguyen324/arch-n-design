from pydantic import BaseModel

# model for fastAPI application


class UserCreate(BaseModel):
    id: str
    name: str
