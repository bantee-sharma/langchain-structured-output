from pydantic import BaseModel,EmailStr,Field
from typing import Optional

#Schema

class students(BaseModel):

    name:str 
    age: Optional[int] = None
    score:int
    email: EmailStr
    cgpa: float = Field(gt=0, lt=11,description="score of student")

new_student = {"name":"bantee","score":100,"email":"abc@gmail.com","cgpa":10}


student = students(**new_student)

res = dict(student)

print(res["age"])
