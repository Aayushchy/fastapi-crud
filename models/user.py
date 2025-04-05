from typing import Optional

from pydantic import BaseModel

class UserDto(BaseModel):
    id: Optional[int]
    name: str
    email: str
