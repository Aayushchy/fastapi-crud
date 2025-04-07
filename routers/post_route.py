from fastapi import APIRouter

from configuration.database import db_dependency
from models.post_dto import PostDto

router = APIRouter(
    prefix="/post",
    tags=["posts"]
)


@router.post("/create")
async def create_post(post: PostDto, db: db_dependency):
    pass
