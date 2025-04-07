from sqlalchemy import Column, Integer, String

from configuration.database import Base


class UserSchema(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), index=True, unique=True)

