"""TODO management functions."""


def create_todo(title: str) -> dict:
    """Create a new TODO item."""
    return {"title": title}


def add_todo(todos: list, title: str) -> list:
    """Add a new TODO item to the list."""
    todo = create_todo(title)
    todos.append(todo)
    return todos
