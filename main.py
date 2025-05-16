from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

@app.get("/api/users", response_model=List[User])
def get_users():
    return users_db

@app.post("/api/users", response_model=User, status_code=201)
def create_user(user: User):
    users_db.append(user)
    return user

@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    global users_db
    users_db = [user for user in users_db if user.id != user_id]
    return
