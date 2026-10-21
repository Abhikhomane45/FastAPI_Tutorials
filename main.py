from fastapi import FastAPI,Request
from mockData import students
from dtos import stud


app=FastAPI()

#Create FastApi server
@app.get("/")
def home():
    return "This is a fastAPI Series"

@app.get("/get_all_students")
def get_students():
    return students


#Path Params
#@app.get("/student/{student_id}")
#def student(student_id:int):
 #   if student_id in students:
  #      return students[student_id]
    
  #  return {"error": "Student not found"}


@app.get("/get_student_by/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"error": "Student not found"}


#query parameters

@app.get("/greet")
def greet(city:str,age:int):
    return { "Greet":f"hello i am from {city} and my age is {age}"}

@app.get("/reqt")
def greet(request:Request):
    query_params=dict(request.query_params)
    
    return { f"my name is {query_params.get("name")}, and age is {query_params.get("age")}, from {query_params.get("city")}"}


#Post Method

@app.post("/add_Student")
def addstud(data:stud):
    Student_data=data.model_dump()
    print(Student_data)
    students.append(Student_data)
    return {"status":"Student added Successfully !!", "data":Student_data}

#Put Method

@app.put("/update_student/{student_id}")
def updatestd(data:stud , student_id:int):
    
    for student in students:
        if student["id"]==student_id:
            student.update(data.model_dump(exclude={"id"}))
            return {
                "status": "Student updated successfully!",
                "data": student
            }
    
    return {"error": "Student not found"}


