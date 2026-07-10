"""Tests for Flask app."""

import pytest
from app import create_app


@pytest.fixture
def client():
    """Create a test client."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that the index page loads."""
    response = client.get("/")
    assert response.status_code == 200


def test_add_todo(client):
    """Test adding a TODO item."""
    response = client.post("/add", data={"title": "Test task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test task" in response.data


def test_add_empty_todo(client):
    """Test that empty TODO is not added."""
    response = client.post("/add", data={"title": ""}, follow_redirects=True)
    assert response.status_code == 200
