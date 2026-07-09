"""TODOのロジックを管理するモジュール"""


def create_todo(title: str) -> dict:
    """TODOを1件作成する

    Args:
        title: TODOのタイトル

    Returns:
        TODOの辞書 例: {"title": "Buy milk"}
    """
    return {"title": title}


def add_todo(todos: list, title: str) -> list:
    """TODOリストにTODOを追加する

    Args:
        todos: 既存のTODOリスト
        title: 追加するTODOのタイトル

    Returns:
        追加後のTODOリスト
    """
    todo = create_todo(title)
    todos.append(todo)
    return todos
