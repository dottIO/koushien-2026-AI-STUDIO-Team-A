"""todo.py のユニットテスト"""

from todo import create_todo, add_todo


def test_create_todo_returns_dict():
    """create_todo でTODOの辞書が作成されること"""
    result = create_todo("Buy milk")
    assert result == {"title": "Buy milk"}


def test_add_todo_adds_one_item():
    """add_todo でTODOリストに1件追加されること"""
    todos = []
    result = add_todo(todos, "Buy milk")
    assert len(result) == 1
    assert result[0]["title"] == "Buy milk"


def test_add_todo_adds_multiple_items():
    """複数件追加できること"""
    todos = []
    add_todo(todos, "Buy milk")
    add_todo(todos, "Read book")
    add_todo(todos, "Write code")
    assert len(todos) == 3
    assert todos[0]["title"] == "Buy milk"
    assert todos[1]["title"] == "Read book"
    assert todos[2]["title"] == "Write code"
