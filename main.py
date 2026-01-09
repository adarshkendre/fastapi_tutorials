from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/data")
def load_data():
    with open("students.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Data API"}


@app.get("/student/{student_id}")
def get_student(student_id: int):
    data = load_data()
    students = data["students"]
    for student in students:
        if student["student_id"] == student_id:
            return student
    return {"error": "Student not found"}