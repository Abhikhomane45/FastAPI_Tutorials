# FastAPI Tutorials

A beginner-friendly FastAPI project that demonstrates the core concepts of building REST APIs in Python. This repository contains multiple small examples covering CRUD operations, request handling, validation, async endpoints, SQLite, and SQLAlchemy integration.

## Project Overview

This project is designed for learning and practice. Each file focuses on a specific FastAPI concept, making it easy to understand how APIs are built and tested.

## Included Examples

- Basic routing and request handling in `main.py`
- Student data CRUD using in-memory data in `main.py`
- Pydantic models and response validation in `main.py`
- HTTP exceptions and dependency injection in `main.py`
- SQLite database example in `database_api.py`
- Async endpoint example in `main2.py`
- SQLAlchemy + SQLite CRUD example in `mainsql.py`
- DTO and mock student data in `dtos.py` and `mockData.py`

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- SQLite
- SQLAlchemy

## Prerequisites

Before running the project, make sure you have:

- Python 3.8+
- pip installed
- A virtual environment recommended

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Abhikhomane45/FastAPI_Tutorials.git
   cd FASTAPI26
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the API

Each FastAPI file can be run separately using Uvicorn.

### Example: run the main API

```bash
uvicorn main:app --reload
```

### Example: run the SQLite API

```bash
uvicorn database_api:app --reload
```

### Example: run the SQLAlchemy API

```bash
uvicorn mainsql:app --reload
```

### Example: run the async example

```bash
uvicorn main2:app --reload
```

After starting the app, open the FastAPI docs in your browser:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Features Covered

- GET, POST, PUT, and DELETE endpoints
- Path parameters and query parameters
- Request body validation with Pydantic
- Response models
- Error handling with `HTTPException`
- Dependency injection
- Async programming in FastAPI
- SQLite database interaction
- SQLAlchemy ORM CRUD operations

## Notes

This repository is intended for learning and experimentation. Some examples use in-memory data and others create local SQLite files automatically when the app runs.

## Project Structure

```text
FASTAPI26/
├── README.md
├── requirements.txt
├── main.py
├── main2.py
├── database_api.py
├── mainsql.py
├── dtos.py
├── mockData.py
├── students.db
├── testsqlal.db
└── __pycache__/
```

## License

This project is for educational purposes and is not licensed for production deployment without proper review.

## Author

Abhijeet Khomane

