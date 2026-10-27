
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    title: str
    completed: bool = False


def create_table():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM tasks")

    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            [
                ("Learn Python", 0),
                ("Build my first API", 1),
            ],
        )

    conn.commit()
    conn.close()


create_table()


@app.get("/")
def home():
    return {"message": "My Task Management API is working!"}


@app.get("/tasks")
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "completed": bool(row[2]),
        }
        for row in rows
    ]


@app.post("/tasks")
def create_task(task: Task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (task.title, int(task.completed)),
    )

    task_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "id": task_id,
        "title": task.title,
        "completed": task.completed,
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, completed FROM tasks WHERE id = ?",
        (task_id,),
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": row[0],
        "title": row[1],
        "completed": bool(row[2]),
    }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (
            updated_task.title,
            int(updated_task.completed),
            task_id,
        ),
    )

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()
    conn.close()

    return {
        "id": task_id,
        "title": updated_task.title,
        "completed": updated_task.completed,
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.commit()
    conn.close()

    return {"message": "Task deleted successfully"}
