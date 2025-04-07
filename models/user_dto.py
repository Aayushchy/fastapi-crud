from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserDto(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

    # Enables mapping of SQLAlchemy ORM objects(Schema) to Pydantic models(DTOs)
    model_config = ConfigDict(from_attributes=True)

