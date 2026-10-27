import os
import tempfile

TEST_DB_PATH = os.path.join(
    tempfile.gettempdir(),
    "task_management_test.db"
)

if os.path.exists(TEST_DB_PATH):
    os.remove(TEST_DB_PATH)

os.environ["TASKS_DB_PATH"] = TEST_DB_PATH

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "My Task Management API is working!"
    }


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_task_crud_flow():
    response = client.post(
        "/tasks",
        json={
            "title": "Automated test task",
            "completed": False
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    try:
        # Check that the task exists
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Automated test task"

        # Update the task
        response = client.put(
            f"/tasks/{task_id}",
            json={
                "title": "Updated automated test task",
                "completed": True
            }
        )

        assert response.status_code == 200
        assert response.json()["completed"] is True

        # Delete the task
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 200

        # Confirm that the task was deleted
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 404

    finally:
        # Clean up the test task if it still exists
        client.delete(f"/tasks/{task_id}")


def test_missing_task_returns_404():
    response = client.get("/tasks/987654321")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}