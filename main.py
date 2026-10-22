
from fastapi import FastAPI, Request ,HTTPException
from mockData import students
from dtos import stud
from pydantic import BaseModel

# Create a FastAPI application instance
app = FastAPI()


# -------------------- GET METHOD --------------------

# Home endpoint: runs when the user visits the root URL "/"
@app.get("/")
def home():
    return "This is a fastAPI Series"


# Get all students from the students list
@app.get("/get_all_students")
def get_students():
    return students


# -------------------- PATH PARAMETERS --------------------

# The student ID is passed directly through the URL.
# Example: GET /get_student_by/2
@app.get("/get_student_by/{student_id}")
def get_student(student_id: int):

    # Search for the student whose ID matches the URL parameter
    for student in students:
        if student["id"] == student_id:
            return student  # Return the matching student

    # Execute this if no matching student ID is found
    return {"error": "Student not found or may be deleted"}


# -------------------- QUERY PARAMETERS --------------------

# FastAPI automatically reads city and age from the URL query string.
# Example: GET /greet?city=Pune&age=23
@app.get("/greet")
def greet(city: str, age: int):
    return {
        "Greet": f"Hello, I am from {city} and my age is {age}"
    }


# Request allows us to access query parameters manually.
# Example: GET /reqt?name=Abhi&age=23&city=Pune
@app.get("/reqt")
def greet_request(request: Request):

    # Convert query parameters into a normal Python dictionary
    query_params = dict(request.query_params)

    # Read values using their keys and create a response message
    return {
        "message": (
            f"My name is {query_params.get('name')}, "
            f"and age is {query_params.get('age')}, "
            f"from {query_params.get('city')}"
        )
    }


# -------------------- POST METHOD --------------------

# POST is used to add a new student.
# Send the student details in the request body as JSON.
@app.post("/add_Student")
def addstud(data: stud):

    # Convert the Pydantic model into a Python dictionary
    Student_data = data.model_dump()

    # Print the new student's data in the terminal
    print(Student_data)

    # Add the new student dictionary to the students list
    students.append(Student_data)

    # Return a success message and the added student's details
    return {
        "status": "Student added Successfully !!",
        "data": Student_data
    }


# -------------------- PUT METHOD --------------------

# PUT is used here to update an existing student's details.
# Example: PUT /update_student/2
@app.put("/update_student/{student_id}")
def updatestd(data: stud, student_id: int):

    # Search for the student using the ID from the URL
    for student in students:
        if student["id"] == student_id:

            # Update the student's fields using the request body.
            # exclude={"id"} prevents the existing ID from changing.
            student.update(data.model_dump(exclude={"id"}))

            # Return the updated student's details
            return {
                "status": "Student updated successfully!",
                "data": student
            }

    # Return an error if the student ID does not exist
    return {"error": "Student not found"}


# -------------------- DELETE METHOD --------------------

# DELETE is used to remove a student from the list.
# Example: DELETE /delete_student/2
@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):

    # Search for the student that should be deleted
    for student in students:
        if student["id"] == student_id:

            # Remove the matching student from the list
            students.remove(student)

            # Return the details of the deleted student
            return {
                "status": "Student deleted successfully!",
                "data": student
            }

    # Return an error if the ID does not exist in the list
    return {
        "error": "Student not found or it may have already been deleted"
    }
    
    
#------------------Response Model---------------------------

# Class 1: Contains all fields to validate
class UserInput(BaseModel):
    name: str
    age: int
    password: str

# Class 2: Defines the response fields
class UserResponse(BaseModel):
    name: str
    age: int


@app.post("/user", response_model=UserResponse)
def create_user(user: UserInput):
    return {
        "name": user.name,
        "age": user.age,
        "password": user.password
    }
    
    

#------HTTPS Execption-----
@app.get("/get_user_by/{user_id}")  # Don't forget @
def getuserby(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Invalid User Id"
        )

    return {
        "id": 1,
        "name": "Abhi",
        "age": 23
    }