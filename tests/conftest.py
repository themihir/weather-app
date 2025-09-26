import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    Provides a reusable TestClient for FastAPI.
    Scope=module means one client per test file.
    """
    with TestClient(app) as c:
        yield c
