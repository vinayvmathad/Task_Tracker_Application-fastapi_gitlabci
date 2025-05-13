# test/test_main.py
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# Create all tables before running tests
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
