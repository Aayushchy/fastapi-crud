from http import HTTPStatus
from logging import exception

from fastapi.params import Depends

from exception.generic_exception import GenericException
from models.user_dto import UserDto
from repositories.user_repository import UserRepository
from schema import user_schema


class UserService:
    def __init__(self,  user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def create(self, user: UserDto):
        user_db = user_schema.UserSchema(**user.model_dump())
        return self.user_repository.save(user_db)

    def find(self, user_id: int):
        user = self.user_repository.find(user_id)
        if user is None:
            raise GenericException(HTTPStatus.BAD_REQUEST, "User not found", "Service is currently unavailable")
        return user

    def get_all(self):
        return self.user_repository.get_all()

    def validate(self, user_id: int):
        user = self.user_repository.find(user_id)
        #call mf with rest template
        if user is None:
            return True
        else:
            return False