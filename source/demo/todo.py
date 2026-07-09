"""TODO management functions - Complete version."""


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


def delete_todo(todos: list, index: int) -> list:
    """Delete a TODO item by index.

    If the index is out of range, returns the list unchanged.
    """
    if 0 <= index < len(todos):
        todos.pop(index)
    return todos
