
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective
Build a REST API with FastAPI by creating endpoints that return JSON responses, use structured data models, and support both retrieval and creation of records.

## 📝 Tasks

### 🛠️ Task 1: Initialize FastAPI and Create a Root Endpoint
#### Description
Set up a basic FastAPI application and create a GET endpoint at the root URL (`/`) that returns a welcome message.
#### Requirements
Completed assignment should:

- Import `FastAPI` from the `fastapi` module.
- Initialize the app instance: `app = FastAPI()`.
- Create a `@app.get("/")` route that returns:
  ```json
  {"message": "Welcome to the Mergington High School API Portal!"}
  ```

### 🛠️ Task 2: Create a Student Data Endpoint
#### Description
Create a GET endpoint at `/students` that returns a list of student records in JSON format.
#### Requirements
Completed assignment should:

- Create a `@app.get("/students")` route.
- Return a list with at least 2-3 student dictionaries.
- Use fields like `id`, `name`, and `grade`.

### 🛠️ Task 3: Add a Student Creation Endpoint
#### Description
Add a POST endpoint at `/students` to accept a new student record and return the created student.
#### Requirements
Completed assignment should:

- Define a `StudentCreate` model using Pydantic.
- Create a `@app.post("/students")` route.
- Accept student payloads with `name` and `grade`.
- Return the new student data including a generated `id`.

## 🚀 Run the API

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Run the server:
   ```bash
   uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
   ```
3. Open `http://127.0.0.1:8000/docs` to explore the API documentation.
