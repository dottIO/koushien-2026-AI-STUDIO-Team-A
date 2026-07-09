"""Tests for todo.py."""

from todo import create_todo, add_todo


def test_create_todo():
    """Test creating a TODO item."""
    todo = create_todo("Test task")
    assert todo == {"title": "Test task"}


def test_add_todo():
    """Test adding a TODO item to the list."""
    todos = []
    result = add_todo(todos, "Task 1")
    assert len(result) == 1
    assert result[0]["title"] == "Task 1"


def test_add_multiple_todos():
    """Test adding multiple TODO items."""
    todos = []
    todos = add_todo(todos, "Task 1")
    todos = add_todo(todos, "Task 2")
    assert len(todos) == 2
    assert todos[0]["title"] == "Task 1"
    assert todos[1]["title"] == "Task 2"


def test_add_todo_intentionally_fails():
    """Intentionally failing test for CI failure demo."""
    todos = []
    result = add_todo(todos, "Task 1")
    # Intentionally wrong expectation for CI failure demo.
    assert len(result) == 2
