from typing import Annotated
from fastapi import FastAPI, HTTPException, Request, Depends
from contextlib import asynccontextmanager


from app.schemas import UserCreate, UserUpdate
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

    return new_user


@app.get("/users/", response_model=list[User])
async def read_users(crud_service: UserCrudServiceDep) -> list[User]:
    users = crud_service.read_all()
    if not users:
        return []
    return users


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str, crud_service: UserCrudServiceDep) -> User:
    user = crud_service.read_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: str, user: UserUpdate, crud_service: UserCrudServiceDep):
    try:
        crud_service.update_by_id(user_id, user.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
