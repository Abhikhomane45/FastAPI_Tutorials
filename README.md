# FastAPI Tutorials

This repository is a practical learning project for building REST APIs with FastAPI. It contains multiple small examples that cover core FastAPI concepts such as routing, validation, CRUD operations, async endpoints, dependency injection, SQLite, and SQLAlchemy.

## Overview

The project is organized as a set of beginner-friendly API examples. Each module demonstrates a specific concept so it is easy to understand how FastAPI works in real-world use cases.

## Features Covered

- Basic API routing and endpoint creation
- GET, POST, PUT, and DELETE operations
- Path and query parameters
- Request validation with Pydantic
- Response models
- HTTP exception handling
- Dependency injection
- Async API functions
- SQLite database usage
- SQLAlchemy ORM with CRUD operations

## Project Structure

```text
FASTAPI26/
├── README.md
├── requirements.txt
├── main.py
├── main2.py
├── dtos.py
├── mockData.py
├── Auth/
│   └── main.py
├── sqlite/
│   ├── database_api.py
│   └── students.db
├── sqlAlchemy/
│   ├── mainsql.py
│   └── testsqlal.db
├── vnew/
└── __pycache__/
```

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- SQLite
- SQLAlchemy

## Prerequisites

Before running the project, make sure you have:

- Python 3.8 or above
- pip installed
- A virtual environment (recommended)

## Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Abhikhomane45/FastAPI_Tutorials.git
   cd FASTAPI26
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Examples

### 1. Basic FastAPI example

```bash
uvicorn main:app --reload
```

### 2. Async example

```bash
uvicorn main2:app --reload
```

### 3. SQLite example

```bash
uvicorn sqlite.database_api:app --reload
```

### 4. SQLAlchemy example

```bash
uvicorn sqlAlchemy.mainsql:app --reload
```

### 5. Auth example

```bash
uvicorn Auth.main:app --reload
```

Once the server is running, open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## File Overview

- `main.py`: Core FastAPI concepts with student CRUD examples
- `main2.py`: Async programming with FastAPI
- `dtos.py`: Pydantic model definitions for request/response data
- `mockData.py`: Mock data used by the API examples
- `Auth/main.py`: Authentication-related or simple example module
- `sqlite/database_api.py`: SQLite integration example
- `sqlAlchemy/mainsql.py`: SQLAlchemy CRUD example

## Notes

This project is intended for learning and practice. The examples are simple and designed to help beginners understand the fundamentals of FastAPI development.

## License

This project is for educational purposes.

## Author

Abhijeet Khomane

