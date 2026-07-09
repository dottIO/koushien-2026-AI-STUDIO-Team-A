"""app.py の統合テスト"""

import pytest
from app import create_app


@pytest.fixture
def client():
    """テスト用のFlaskクライアントを作成する"""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    """GET / がステータスコード200を返すこと"""
    response = client.get("/")
    assert response.status_code == 200


def test_add_redirects_to_index(client):
    """POST /add でTODOを追加した後、トップページにリダイレクトされること"""
    response = client.post("/add", data={"title": "Test TODO"})
    assert response.status_code == 302
    assert "/" in response.headers["Location"]


def test_added_todo_is_displayed(client):
    """追加したTODOが画面に表示されること"""
    client.post("/add", data={"title": "Buy milk"})
    response = client.get("/")
    assert b"Buy milk" in response.data
