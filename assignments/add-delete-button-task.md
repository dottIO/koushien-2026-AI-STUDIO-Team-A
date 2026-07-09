# 追加修正課題：TODOの削除ボタンを追加する

> この課題は [ワーク②](../docs/work2-ci-pipeline.md) の中で使用します。
> 課題の全体的な流れはワーク②を参照してください。

## この課題で実装すること

- TODO一覧の各TODOの横に「削除」ボタンを表示する
- 削除ボタンを押すと、そのTODOが一覧から消える
- 削除後はトップページにリダイレクトする

## 変更対象ファイル

| ファイル | 変更内容 |
|---------|---------|
| `todo-ci-sample/todo.py` | 削除関数を追加 |
| `todo-ci-sample/app.py` | 削除用ルートを追加 |
| `todo-ci-sample/templates/index.html` | 削除ボタンを追加 |
| `todo-ci-sample/tests/test_todo.py` | 削除関数のテストを追加 |
| `todo-ci-sample/tests/test_app.py` | 削除ルートのテストを追加 |

## 実装要件

### 1. `todo-ci-sample/todo.py` に削除関数を追加

以下の関数を追加してください。

```python
def delete_todo(todos: list, index: int) -> list:
```

- 指定された `index` のTODOを削除する
- 存在しない `index` が指定された場合は、リストを変更せずに返す

### 2. `todo-ci-sample/app.py` に削除ルートを追加

- `POST /delete/<int:index>` のルートを追加する
- 削除後は `/` にリダイレクトする

### 3. `todo-ci-sample/templates/index.html` に削除ボタンを追加

- TODO一覧の各項目の横に削除ボタンを表示する
- ボタンを押すと `POST /delete/<index>` にリクエストを送信する

## テスト要件

### Step 1: テストを追加する（この時点でCIが失敗する）

まず、以下のテストを `todo-ci-sample/tests/test_todo.py` に追加してください。

```python
from todo import delete_todo

def test_delete_todo_removes_item():
    todos = [{"title": "Task 1"}, {"title": "Task 2"}]
    result = delete_todo(todos, 0)
    assert len(result) == 1
    assert result[0]["title"] == "Task 2"

def test_delete_todo_with_invalid_index_does_not_change_list():
    todos = [{"title": "Task 1"}]
    result = delete_todo(todos, 99)
    assert result == [{"title": "Task 1"}]
```

また、`todo-ci-sample/tests/test_app.py` に以下のテストを追加してください。

```python
def test_delete_todo(client):
    client.post("/add", data={"title": "Task to delete"})
    response = client.post("/delete/0", follow_redirects=True)
    assert response.status_code == 200
    assert b"Task to delete" not in response.data
```

### この時点でのCI結果

この時点では、既存コードに `delete_todo` 関数が存在せず、`/delete/<int:index>` ルートも未実装です。

そのため、pytest を実行すると以下のようなエラーが発生します。

```
ImportError: cannot import name 'delete_todo' from 'todo'
```

**これは想定通りの動作です。** CIが失敗することを確認してください。

### Step 2: 実装を追加する（CIを成功させる）

テストが失敗することを確認したら、以下の実装を追加してCIを成功させてください。

1. `todo-ci-sample/todo.py` に `delete_todo` 関数を実装する
2. `todo-ci-sample/app.py` に `POST /delete/<int:index>` ルートを実装する
3. `todo-ci-sample/templates/index.html` に削除ボタンを追加する

## ゴール

最終的に以下の状態を目指してください。

- [ ] 削除ボタンが画面に表示される
- [ ] ボタンを押すとTODOが削除される
- [ ] pytest がすべて成功する
- [ ] GitHub ActionsのCIが成功する
