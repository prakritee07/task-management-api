# Task Management API

A REST API built with Python, FastAPI, and SQLite to manage tasks. This project demonstrates API development, CRUD operations, database storage, and automated testing.

## Features

- View all tasks
- Create a task
- View a task by ID
- Update a task
- Delete a task
- Return a 404 response when a task does not exist
- Store tasks in SQLite
- Run automated API tests with pytest

## Technologies Used

- Python
- FastAPI
- SQLite
- Pytest
- Git and GitHub

## Setup

1. Clone the repository:

   `git clone https://github.com/prakritee07/task-management-api.git`

2. Enter the project folder:

   `cd task-management-api`

3. Create a virtual environment:

   `python -m venv .venv`

4. Activate it on Windows:

   `.venv\Scripts\activate`

5. Install dependencies:

   `python -m pip install -r requirements.txt`

## Run the API

Start the server:

`python -m uvicorn main:app --reload`

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Run Automated Tests

Run:

`python -m pytest -v`

The test suite checks the home endpoint, task retrieval, task creation, task updates, deletion, and missing-task handling.

## Database

Tasks are stored in `tasks.db`, which is created automatically when the application runs. The database file is excluded from Git so that local task data is not uploaded to the repository. Automated tests use a separate temporary database.

## Project Status

This is a learning project that I developed to practice Python backend development, REST APIs, database integration, and automated testing.