from sqlalchemy import text, desc

from schema.user_schema import UserSchema
from configuration.database import db_dependency


class UserRepository:
    def __init__(self,  db: db_dependency):
        self.db = db

    def save(self, user: UserSchema):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find(self, user_id: int):
        return self.db.query(UserSchema).get(user_id)

    def get_all(self):
        users = self.db.query(UserSchema).order_by(desc(UserSchema.id)).all()
        return users