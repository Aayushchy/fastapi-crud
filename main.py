from fastapi import FastAPI

from configuration.database import Base
from configuration.database import engine

from routers.user_route import router as user_router
from routers.post_route import router as post_router

# from schema import user
# from schema import post

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)

