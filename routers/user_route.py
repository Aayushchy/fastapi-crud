from fastapi import APIRouter

import schema.user as user_schema
from configuration.database import db_dependency
from models.user import UserDto

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/create")
async def create_user(user: UserDto, db: db_dependency):
    user_db = user_schema.User(name=user.name, email=user.email)
    db.add(user_db)
    db.commit()
    return {"message": "User created successfully"}
