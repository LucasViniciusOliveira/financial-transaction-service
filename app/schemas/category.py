from uuid import UUID
from pydantic import BaseModel, Field

class CreateCategoryRequest(BaseModel):
    name: str = Field(max_length=100)
    description: str | None = None
    color: str
    icon: str
    user_id: UUID