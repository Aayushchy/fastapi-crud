from typing import List, Optional

from fastapi import APIRouter, Depends, Query

from configuration.logging_config import logger
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
    logger.info("Finding user Id")
    return user_service.find(user_id)

@router.post("/active-plan")
def get_active_plan(product_code: str, include_hierarchy: bool, internal_identifier: Optional[str] = Query(default=None), user_service: UserService = Depends()):
    return user_service.get_active_plan(product_code, include_hierarchy, internal_identifier)