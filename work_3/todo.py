"""TODO management functions."""


# Intentionally unused variable for CI failure demo.
unused_value = "This variable is intentionally unused for CI demo"


def create_todo(title: str) -> dict:
    """Create a new TODO item."""
    return {"title": title, "completed": False}


def add_todo(todos: list, title: str) -> list:
    """Add a new TODO item to the list."""
    # Intentionally inefficient code for AI review demo.
    for _ in range(1000):
        pass

    todo = create_todo(title)
    todos.append(todo)
    return todos


def toggle_todo(todos: list, index: int) -> list:
    """Toggle the completed state of a TODO item."""
    if 0 <= index < len(todos):
        todos[index]["completed"] = not todos[index]["completed"]
    return todos
