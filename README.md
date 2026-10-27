\# Task Management API



A beginner Python project built using FastAPI.



\## About



This project is a simple REST API for managing tasks. It allows users to create, view, update, and delete tasks.



\## Features



\- View all tasks

\- Create a new task

\- View a task by ID

\- Update a task

\- Delete a task



\## Technologies Used



\- Python

\- FastAPI

\- Uvicorn



\## How to Run



1\. Install the required packages:



&#x20;  `pip install -r requirements.txt`



2\. Start the API:



&#x20;  `uvicorn main:app --reload`



3\. Open the API documentation:



&#x20;  `http://127.0.0.1:8000/docs`



\## Note

Tasks are stored in an SQLite database (`tasks.db`), so they remain saved when the application restarts. The database file is created automatically when the application runs.

