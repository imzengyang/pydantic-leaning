from pydantic import BaseModel,Field
from typing import Annotated
from uuid import uuid4


class User(BaseModel):
    id: Annotated[str,Field(default_factory=lambda: uuid4().hex)]
    age: int = Field(ge=0, le=150, default=25,strict=True)
    name: str = Field(exclude=True)
    
user = User(name='John',age=30)
print(user)
print(user.model_dump())
print(user.model_dump_json())