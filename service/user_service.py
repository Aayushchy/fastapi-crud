from http import HTTPStatus

from fastapi.params import Depends

from caller.mf_caller import MfCaller
from configuration.logging_config import logger
from exception.generic_exception import GenericException
from models.user_dto import UserDto
from repositories.user_repository import UserRepository
from schema import user_schema


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(), mf_caller: MfCaller = Depends()):
        self.user_repository = user_repository
        self.mf_caller = mf_caller

    def create(self, user: UserDto):
        user_db = user_schema.UserSchema(**user.model_dump())
        return self.user_repository.save(user_db)

    def get_all(self):
        return self.user_repository.get_all()

    def find(self, user_id: int):
        user = self.user_repository.find(user_id)
        if user is None:
            raise GenericException(HTTPStatus.BAD_REQUEST, "User not found", "Service is currently unavailable")
        return user

    async def get_active_plan(self, product_code: str, include_hierarchy: bool, internal_identifier: str):
        plan = await self.mf_caller.get_active_plan(product_code, include_hierarchy, internal_identifier)
        logger.info("Active plan: %s", plan)
        return plan