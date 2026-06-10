from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    grade: str

class StudentCreate(BaseModel):
    name: str
    grade: str

students: List[Student] = [
    Student(id=1, name="Aisha", grade="A"),
    Student(id=2, name="Noah", grade="B+"),
    Student(id=3, name="Sofia", grade="A-")
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington High School API Portal!"}

@app.get("/students", response_model=List[Student])
def list_students():
    return students

@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    new_id = max((s.id for s in students), default=0) + 1
    new_student = Student(id=new_id, **student.dict())
    students.append(new_student)
    return new_student
