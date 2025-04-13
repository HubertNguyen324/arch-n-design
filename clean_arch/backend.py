
from fastapi import Depends, FastAPI, HTTPException

from clean_arch.interfaces import UserRepository
from clean_arch.mem_repository import get_repository
from clean_arch.schemas import UserCreate
from clean_arch.use_cases import UserService

# Web Framework as an adapter (FastAPI)
app = FastAPI()

# API endpoints


@app.post("/user")
def create_user(user: UserCreate, repo: UserRepository = Depends(get_repository)):
    service = UserService(repo)
    created_user = service.create_user(user.id, user.name)
    return created_user


@app.get("/user/{user_id}")
def read_user(user_id: str, repo: UserRepository = Depends(get_repository)):
    service = UserService(repo)
    user = service.find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
