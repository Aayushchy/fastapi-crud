from pydantic import BaseModel

class PostDto(BaseModel):
    id: int
    type: str
    content: str