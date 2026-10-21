from pydantic import BaseModel

class stud(BaseModel):
    id :int
    name: str
    age: int = 0
    course: str
        
    