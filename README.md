# 🚀 FastAPI Student Data API 

This project is a **learning-focused FastAPI tutorial** that demonstrates how to build REST APIs using **FastAPI** with data stored in a **JSON file**.  
It is designed for beginners who want to understand FastAPI fundamentals before moving to databases.

---

## 📌 Features

- ✅ FastAPI basics
- ✅ Read data from a JSON file
- ✅ API routing (`GET`)
- ✅ Path parameters
- ✅ Clean JSON responses
- ✅ Beginner-friendly project structure

---

## 🛠 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Uvicorn**
- **JSON (as data source)**

---

## 📁 Project Structure
.
├── main.py
├── students.json
├── README.md



---

## 📄 students.json (Sample Data)

```json
{
  "students": [
    {
      "id": 1,
      "name": "Aarav Sharma",
      "email": "aarav.sharma@example.com",
      "age": 20,
      "course": "Computer Science",
      "cgpa": 8.6
    }
  ]
}



🧠 Learning Goals

By completing this tutorial, you will understand:

How FastAPI works internally

JSON serialization vs deserialization

Path & query parameters

Clean API responses

Basic backend architecture

----------------------------------

🚧 Future Improvements

🔜 POST /student (add student)

🔜 PUT /student/{id} (update student)

🔜 DELETE /student/{id}

🔜 Pydantic validation

🔜 Database integration (SQLAlchemy)

🔜 JWT Authentication
