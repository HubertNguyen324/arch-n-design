from typing import Annotated
from fastapi import FastAPI, Request, Depends
from contextlib import asynccontextmanager


from schemas import UserCreate, UserUpdate
from entities.user import User
from use_cases.user_crud_service import UserCrudService
from infrastructure.in_memory_repository import InMemoryReposity


def get_user_crud_service(request: Request) -> UserCrudService:
    user_repository = request.app.state.database
    return UserCrudService(user_repository)


UserCrudServiceDep = Annotated[UserCrudService, Depends(get_user_crud_service)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.database = InMemoryReposity()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, crud_service: UserCrudServiceDep) -> User:
    new_user = crud_service.create(user.model_dump())

    return user
