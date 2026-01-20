# services/user-service/tests/test_main.py
from fastapi.testclient import TestClient
from ..app.main import app   # ← two dots: go up one level to the service root, then into app/

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello from User Service" in response.json()["message"]  # adjust if needed

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}