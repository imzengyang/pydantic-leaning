from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    age: int
    friends: List[str]
    is_vip: bool = False
    
user = User(id=1, name='Tom', age=20, friends=['Alice', 'Bob'])

print(user)
print(user.model_dump_json()) # json
print(user.model_dump())