from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, User, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("639fc76b-92b4-429f-a28e-0a5d28fc477b"),
        first_name="Kemisola",
        last_name="Oyeyinka",
        gender=Gender.female,
        role=[Role.admin]
    ),
    User(
        id=UUID("a702ab77-d950-4602-90d9-8fcbb13286d9"),
        first_name="Alex",
        last_name="Jone",
        middle_name="M",
        gender=Gender.male,
        role=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"The user with id: {user_id} does not exist"
    )
    
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.role is not None:
                user.role = user_update.role
    raise HTTPException(
        status_code=404,
        detail=f"The user with id: {user_id} does not exist"
    )