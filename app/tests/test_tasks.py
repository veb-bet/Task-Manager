from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.post("/tasks/", json={"title": "Old Title", "description": "Old Description"})
    task_id = response.json()["id"]

    update_response = client.put(f"/tasks/{task_id}", json={"title": "New Title"})
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "New Title"

def test_delete_task():
    response = client.post("/tasks/", json={"title": "To Be Deleted", "description": "Description"})
    task_id = response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Task deleted successfully"
