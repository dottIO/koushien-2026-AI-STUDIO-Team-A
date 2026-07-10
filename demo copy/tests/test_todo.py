"""Tests for todo.py - Complete version."""

from todo import create_todo, add_todo, toggle_todo, delete_todo


def test_create_todo():
    """Test creating a TODO item."""
    todo = create_todo("Test task")
    assert todo == {"title": "Test task", "completed": False}


def test_add_todo():
    """Test adding a TODO item to the list."""
    todos = []
    result = add_todo(todos, "Task 1")
    assert len(result) == 1
    assert result[0]["title"] == "Task 1"
    assert result[0]["completed"] is False


def test_add_multiple_todos():
    """Test adding multiple TODO items."""
    todos = []
    todos = add_todo(todos, "Task 1")
    todos = add_todo(todos, "Task 2")
    assert len(todos) == 2
    assert todos[0]["title"] == "Task 1"
    assert todos[1]["title"] == "Task 2"


def test_toggle_todo():
    """Test toggling a TODO item."""
    todos = [{"title": "Task 1", "completed": False}]
    result = toggle_todo(todos, 0)
    assert result[0]["completed"] is True
    result = toggle_todo(todos, 0)
    assert result[0]["completed"] is False


def test_toggle_todo_invalid_index():
    """Test toggling with invalid index does nothing."""
    todos = [{"title": "Task 1", "completed": False}]
    result = toggle_todo(todos, 99)
    assert result[0]["completed"] is False


def test_delete_todo_removes_item():
    """Test deleting a TODO item."""
    todos = [{"title": "Task 1", "completed": False}, {"title": "Task 2", "completed": False}]
    result = delete_todo(todos, 0)
    assert len(result) == 1
    assert result[0]["title"] == "Task 2"


def test_delete_todo_with_invalid_index():
    """Test deleting with an invalid index does not change the list."""
    todos = [{"title": "Task 1", "completed": False}]
    result = delete_todo(todos, 99)
    assert result == [{"title": "Task 1", "completed": False}]
