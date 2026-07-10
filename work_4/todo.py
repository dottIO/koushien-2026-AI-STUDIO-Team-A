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


def find_todo(todos: list, title: str) -> dict:
    """Find a TODO item by title."""
    for i in range(len(todos)):
        if todos[i]["title"] == title:
            return todos[i]
    return None


def get_completed_count(todos: list) -> int:
    """Get the number of completed TODOs."""
    count = 0
    for i in range(len(todos)):
        if todos[i]["completed"] == True:  # noqa: E712
            count = count + 1
    return count
