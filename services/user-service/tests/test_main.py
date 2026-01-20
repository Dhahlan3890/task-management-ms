# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app          # ← absolute import (no dots!)

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello Dhahlan from User Service" in response.json().get("message", "")  # safer

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "healthy"