from pydantic import BaseModel
from datetime import datetime


class Address(BaseModel):
    zip: str
    city: str
    
    
class Metting(BaseModel):
    when: datetime
    where: Address
    why: str
    
    
addr = Address(city="shanghai",zip="200000")
meeting = Metting(when=datetime.now(),where=addr,why="no")

print(meeting.model_dump_json())
print(meeting.model_dump())