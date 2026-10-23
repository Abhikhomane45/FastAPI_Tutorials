import sqlite3
from fastapi import FastAPI

app=FastAPI()

# Create or connect to a database file
connection = sqlite3.connect("students.db")

# Create a cursor to execute SQL
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Abhi", 23)
)

# Save changes
connection.commit()

# Read data
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Close connection
connection.close()

@app.get("/")
def home():
    return {"message": "SQLite with FastAPI"}