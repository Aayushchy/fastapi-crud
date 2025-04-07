from fastapi import FastAPI

from configuration.database import Base
from configuration.database import engine
from exception.exception_handler import register_exception_handlers
from routers import routers

#Reading from config.yml file, Logging, Rest API call
app = FastAPI()

Base.metadata.create_all(bind=engine)

#Registering exception handler
register_exception_handlers(app)

#Importing all routers
for router in routers:
    app.include_router(router)
