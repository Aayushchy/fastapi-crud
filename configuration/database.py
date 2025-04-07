from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config_loader import ConfigLoader
from configuration.config_constants import ConfigConstants


class Database:
    def __init__(self, config_path: str = "config.yml"):
        self.config_loader = ConfigLoader(config_path)
        self.config = self.config_loader._load_config()
        self.engine = self._create_engine()
        self.session_local = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        self.base = declarative_base()

    def _create_engine(self):
        db_config = self.config[ConfigConstants.DATASOURCE]
        db_url = db_config[ConfigConstants.DB_URL]
        return create_engine(
            db_url,
            pool_size=db_config.get(ConfigConstants.DB_MAX_POOL, 10),
            pool_recycle=db_config[ConfigConstants.DB_POOL_RECYCLE],
            pool_pre_ping=db_config[ConfigConstants.DB_POOL_PRE_PING],
            max_overflow=db_config[ConfigConstants.DB_MAX_OVERFLOW],
            pool_timeout=db_config[ConfigConstants.DB_POOL_TIMEOUT],
        )

    def get_db(self):
        db = self.session_local()  # Create a new database session
        try:
            yield db  # Provide the session to the dependent function
        finally:
            db.close()  # Close the session after use


db_instance = Database()
get_db = db_instance.get_db
db_dependency = Annotated[Session, Depends(get_db)]

# It creates a base class for all ORM schema.
# Any class that inherits from Base is a model representing a table in the database
Base = db_instance.base
