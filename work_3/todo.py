"""TODO management functions."""


def create_todo(title: str) -> dict:
    """Create a new TODO item."""
    return {"title": title, "completed": False}


def add_todo(todos: list, title: str) -> list:
    """Add a new TODO item to the list."""
    todo = create_todo(title)
    todos.append(todo)
    return todos


def toggle_todo(todos: list, index: int) -> list:
    """Toggle the completed state of a TODO item."""
    if 0 <= index < len(todos):
        todos[index]["completed"] = not todos[index]["completed"]
    return todos


def get_todo_count(todos: list) -> int:
    """Get the number of TODOs.

    Intentionally inefficient implementation for AI review demo.
    """
    # Intentionally inefficient: manually counting instead of using len()
    count = 0
    for _ in todos:
        count = count + 1
    return count
# Demo change

