import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from hex_arch.interface import UserRepository
from hex_arch.mem_repository import get_repository
from hex_arch.service import UserService

# Adapter for FastAPI
app = FastAPI()


class UserCreate(BaseModel):
    id: str
    name: str


@app.post("/user")
def create_user(user: UserCreate, repo: UserRepository = Depends(get_repository)):
    print("Creating user")
    service = UserService(repo)
    created_user = service.create_user(user.id, user.name)
    print(created_user)
    return created_user


@app.get("/user/{user_id}")
def read_user(user_id: str, repo: UserRepository = Depends(get_repository)):
    service = UserService(repo)
    user = service.find_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
