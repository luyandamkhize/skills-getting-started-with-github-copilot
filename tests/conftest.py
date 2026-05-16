from copy import deepcopy

from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(scope="function")
def client():
    """Provide a TestClient and restore shared state after each test."""
    original_activities = deepcopy(activities)
    client = TestClient(app)
    try:
        yield client
    finally:
        activities.clear()
        activities.update(original_activities)
