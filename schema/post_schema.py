from sqlalchemy import Column, Integer, String, ForeignKey

from configuration.database import Base


class PostSchema(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String(50))
    content = Column(String(50))
    user_id = Column(Integer, ForeignKey("user.id"))
