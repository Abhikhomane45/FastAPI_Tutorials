# FastAPI Tutorials

A beginner-friendly FastAPI learning repository with multiple small API examples covering core backend concepts, data validation, database integration, and authentication patterns.

## Overview

This project is designed for learning and practicing FastAPI by building REST APIs step by step. Each module focuses on a specific topic so you can understand how FastAPI works in real-world applications.

## What You'll Learn

- Creating FastAPI applications
- Defining routes and HTTP methods
- Path and query parameters
- Request/response validation with Pydantic
- CRUD operations
- Error handling with HTTP exceptions
- Dependency injection
- Async endpoints
- SQLite database integration
- SQLAlchemy ORM usage
- Authentication-related examples

## Project Structure

```text
FASTAPI26/
├── README.md
├── requirements.txt
├── main.py
├── main2.py
├── dtos.py
├── mockData.py
├── oauth2/
├── Auth/
│   └── main.py
├── sqlite/
│   ├── database_api.py
│   └── students.db
├── sqlAlchemy/
│   ├── mainsql.py
│   └── testsqlal.db
├── vnew/
├── __pycache__/
└── .git/
```

## Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic
- SQLite
- SQLAlchemy

## Prerequisites

Before running the examples, make sure you have:

- Python 3.8 or newer
- pip installed
- A virtual environment (recommended)

## Setup

1. Clone the repository

```bash
git clone https://github.com/Abhikhomane45/FastAPI_Tutorials.git
cd FASTAPI26
```

2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Examples

Start each example with Uvicorn from the project root.

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

### 6. OAuth example

```bash
uvicorn oauth2.main:app --reload
```

> If a module does not exist in your current branch or requires a different entry point, check the folder contents before running it.

Once the server is running, open the following in your browser:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Project Files

- `main.py`: Core FastAPI CRUD examples
- `main2.py`: Async FastAPI example
- `dtos.py`: Pydantic request/response models
- `mockData.py`: Dummy data used by the examples
- `Auth/main.py`: Authentication-related example
- `sqlite/database_api.py`: SQLite-based API example
- `sqlAlchemy/mainsql.py`: SQLAlchemy CRUD implementation
- `oauth2/`: OAuth-related implementation examples

## Notes

This repository is intended for educational use and practice. The examples are intentionally simple and beginner-focused so that the fundamentals of FastAPI can be understood clearly.

## License

This project is for educational purposes only.

## Author

Abhijeet Khomane

