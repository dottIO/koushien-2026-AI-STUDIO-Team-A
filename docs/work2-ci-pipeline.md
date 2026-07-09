# ワーク②：サンプルプロジェクトにCIを追加する

## 目的

TODOアプリに対して、自動テストとLintを実行するCIを構築する。

ワーク①で「Actionsが動く」ことを確認しました。ここでは実際のプロジェクトに対して実用的なCIを追加します。

## 前提

- ワーク①が完了していること（`.github/workflows/ci.yml` が存在する）
- TODOアプリが `todo-ci-sample/` 配下にあること

## 実施内容

### Phase 1：CIにテストを追加する

#### 1. ci.yml を編集する

ワーク①で作成した `.github/workflows/ci.yml` を以下の内容に書き換えてください。

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t todo-ci-sample ./todo-ci-sample

      - name: Run tests
        run: docker run --rm todo-ci-sample pytest
```

#### 各ステップの意味

| ステップ | 意味 |
|---------|------|
| `actions/checkout@v4` | リポジトリのコードを取得する |
| `docker build` | Dockerイメージをビルドする |
| `docker run ... pytest` | コンテナ内でテストを実行する |

#### 変更点（ワーク①との違い）

- `on` に `pull_request` を追加した
- `echo` の代わりに Docker build + pytest を実行するようにした
- `actions/checkout@v4` でコードを取得するステップを追加した

#### 2. pushしてCIが成功することを確認する

```bash
git add .github/workflows/ci.yml
git commit -m "Add Docker build and pytest to CI"
git push
```

Actionsタブで、Docker build → pytest の順に実行され、成功することを確認してください。

---

### Phase 2：Lintを追加する

#### 3. ci.yml にLintステップを追加する

`Run tests` の後に以下を追加してください。

```yaml
      - name: Run lint
        run: docker run --rm todo-ci-sample ruff check .
```

完成形はこうなります。

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t todo-ci-sample ./todo-ci-sample

      - name: Run tests
        run: docker run --rm todo-ci-sample pytest

      - name: Run lint
        run: docker run --rm todo-ci-sample ruff check .
```

#### 4. pushしてCIが成功することを確認する

```bash
git add .github/workflows/ci.yml
git commit -m "Add ruff lint to CI"
git push
```

> **注意**: `todo-ci-sample/requirements.txt` に `ruff` が含まれていることを確認してください。含まれていない場合はDockerイメージ内にruffがインストールされず、CIが失敗します。

---

### Phase 3：PRを作成してCIの動作を確認する

#### 5. featureブランチを作成する

```bash
git checkout -b feature/delete-button
```

#### 6. テストを先に追加する（意図的にCIを失敗させる）

ここで、追加修正課題 [assignments/add-delete-button-task.md](../assignments/add-delete-button-task.md) の **Step 1** を実施します。

`todo-ci-sample/tests/test_todo.py` に以下を追加してください。

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

`todo-ci-sample/tests/test_app.py` に以下を追加してください。

```python
def test_delete_todo(client):
    client.post("/add", data={"title": "Task to delete"})
    response = client.post("/delete/0", follow_redirects=True)
    assert response.status_code == 200
    assert b"Task to delete" not in response.data
```

#### 7. コミットしてpushする

```bash
git add .
git commit -m "Add delete todo tests"
git push -u origin feature/delete-button
```

#### 8. PRを作成する

GitHubでPull Requestを作成してください。

- base: `main`
- compare: `feature/delete-button`

#### 9. CI失敗を確認する

PR上でCIが自動実行され、**失敗**することを確認してください。

失敗理由：

```
ImportError: cannot import name 'delete_todo' from 'todo'
```

`delete_todo` 関数がまだ実装されていないため、テストがImportErrorで失敗します。

> **これは想定通りの動作です。**
> CIは問題を見つけるための仕組みです。失敗は「問題がある」ことを教えてくれています。

#### 10. 実装を追加してCIを成功させる

追加修正課題 [assignments/add-delete-button-task.md](../assignments/add-delete-button-task.md) の **Step 2** を実施します。

実装を追加したら、コミットしてpushしてください。

```bash
git add .
git commit -m "Implement delete todo feature"
git push
```

#### 11. CI成功を確認する

PR上でCIが再実行され、**成功**することを確認してください。

---

## 確認すること

- [ ] `ci.yml` にDocker build + pytest + ruff が含まれている
- [ ] pushトリガーと pull_requestトリガーの両方が設定されている
- [ ] PRを作成するとCIが自動実行される
- [ ] テスト追加後にCIが失敗した
- [ ] 失敗のログを確認した
- [ ] 実装追加後にCIが成功した

## CI実行の流れまとめ

```
push / PR作成
    ↓
GitHub Actionsが起動
    ↓
Checkout（コード取得）
    ↓
Docker build（イメージビルド）
    ↓
pytest（テスト実行）
    ↓
ruff check（Lint実行）
    ↓
全て成功 → ✓ 緑
どれか失敗 → ✗ 赤
```

## 成果物

- Lintとpytestを実行するGitHub Actions workflow
- CIが失敗したPR
- CIを修正して成功したPR

## ワーク②で学んだこと

- CIは「コードを変更するたびに自動でチェックしてくれる仕組み」である
- テストが通らない状態でpushすると、CIが失敗して教えてくれる
- CI失敗は怖いものではなく、問題を早期に発見するための仕組みである
- Lintを入れることで、コードスタイルの問題も自動で検出できる
