from typing import List

from fastapi import APIRouter, Depends

from models.user_dto import UserDto
from service.user_service import UserService

router = APIRouter(prefix="/user", tags=["users"])


@router.post("/create", response_model=UserDto)
def create(user: UserDto, user_service: UserService = Depends()):
    return user_service.create(user)

@router.get("/all", response_model=List[UserDto])
def users(user_service: UserService = Depends()):
    return user_service.get_all()

@router.get("/{user_id}", response_model=UserDto)
def find(user_id: int, user_service: UserService = Depends()):
    return user_service.find(user_id)

