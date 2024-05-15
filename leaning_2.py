from typing import Annotated,Literal
from pydantic import BaseModel
from annotated_types import Gt, Ge, Lt, Le


class User(BaseModel):
    id: Annotated[int, "User ID", Ge(0)]
    name: str
    age: Annotated[int, "User Age", Gt(0), Lt(150)]
    sex: Literal["男", "女"]
    
    
user = User(id=1, name="John", age=30,sex="男")

print(user)