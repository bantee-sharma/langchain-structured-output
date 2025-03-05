from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name: str = "bantee"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=11,description="decimal value representing the cgpa of student")

 
new_student = {"name":"bantee","age":'25',"email":"abc@mail.com","cgpa":10}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict["age"])