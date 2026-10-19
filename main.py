from fastapi import FastAPI
from mockData import students

app=FastAPI()

@app.get("/")
def home():
    return "This is a fastAPI Series"

@app.get("/student/{student_id}")
def student(student_id:int):
    if student_id in students:
        return students[student_id]
    
    return {"error": "Student not found"}
    

