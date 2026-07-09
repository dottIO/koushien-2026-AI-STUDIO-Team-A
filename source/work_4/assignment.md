# ワーク④：AIレビューの指摘に対応し、完成形のPRフローを確認する

## ゴール

AIレビューの指摘とCI失敗に対して修正を行い、Lint/テスト/AIレビューがすべて正常に通る完成形のPRフローを再現する。

最終的にPRをマージし、一連の開発フローを完了する。

## 前提

- ワーク③が完了していること
- PRがまだオープンであること
- CIが失敗している状態であること
- AIレビューBotからコメントが来ている状態であること

## 使用するファイル

```
source/work_4/
├── app.py
├── todo.py
├── tests/
│   ├── test_todo.py
│   └── test_app.py
└── .github/
    └── workflows/
        ├── lint-test.yml
        └── ai-review.yml
```

> `source/work_4/` は完成形の参考です。自分で修正しても、このファイルを参考にしてもOKです。

## 手順

### 1. AIレビューの指摘内容を確認する

PR画面でAIからのレビューコメントを確認してください。

想定される指摘:
- 無駄なループ処理（`for _ in range(1000): pass`）を削除すべき
- 冗長な条件分岐を簡素化すべき
- `get_todo_count()` は `len()` で代用できる

### 2. Lint/テスト失敗の原因を確認する

CIのエラーログを確認してください。

失敗の原因:
- **Lintエラー:** `unused_value` が未使用変数
- **テスト失敗:** `test_add_todo_intentionally_fails` の期待値が間違っている

### 3. VSCodeでコードを修正する

以下の修正を行ってください。

#### todo.py の修正

- `unused_value` の行を削除する
- 無駄な `for _ in range(1000): pass` を削除する
- 冗長な条件分岐をシンプルにする
- `get_todo_count()` 関数を削除する（使用されていないため）

修正後の `todo.py` は以下のようになります:

```python
"""TODO management functions."""


def create_todo(title: str) -> dict:
    """Create a new TODO item."""
    return {"title": title}


def add_todo(todos: list, title: str) -> list:
    """Add a new TODO item to the list."""
    todo = create_todo(title)
    todos.append(todo)
    return todos
```

#### tests/test_todo.py の修正

- `test_add_todo_intentionally_fails` を削除するか、期待値を正しく修正する

修正例（期待値を修正する場合）:

```python
def test_add_todo_single_item():
    """Test adding a single TODO item."""
    todos = []
    result = add_todo(todos, "Task 1")
    assert len(result) == 1  # 1件追加したので1
```

### 4. Dockerでローカル確認する

修正後、ローカルでテストを実行して確認してください。

```bash
docker build -t todo-app .
```

```bash
docker run --rm todo-app pytest
```

すべてのテストが成功することを確認してください。

Lintも確認:

```bash
docker run --rm todo-app ruff check .
```

エラーが出ないことを確認してください。

### 5. SourceTreeでコミット・pushする

1. 修正したファイルをステージングする
2. コミットメッセージを入力する（例: `Fix lint errors and failing test`）
3. 「コミット」をクリック
4. 「プッシュ」をクリック

### 6. PR上でCIの再実行を確認する

1. GitHubのPR画面を開く
2. CIが再実行されることを確認する
3. 全てのチェックが成功（緑の ✓）になることを確認する

確認項目:
- Lint and Test: ✓ 成功
- AI Review: ✓ 成功（大きな指摘がない）

### 7. PRをマージする

すべてのCIが成功したら:

1. PR画面下部の「Merge pull request」をクリック
2. 「Confirm merge」をクリック
3. マージが完了したことを確認する

### 8. mainブランチを確認する

1. SourceTreeで `main` ブランチに切り替える
2. 「プル」をクリックしてリモートの変更を取得する
3. 修正済みのコードがmainに反映されていることを確認する

## 確認ポイント

- [ ] AIレビューの指摘内容を確認した
- [ ] Lintエラーを修正した（未使用変数を削除）
- [ ] テスト失敗を修正した（期待値を正しく修正）
- [ ] 問題コードを修正した（無駄なループ、冗長な条件分岐）
- [ ] ローカルでpytestが全て成功した
- [ ] ローカルでruff checkがエラーなし
- [ ] pushしたらPR上でCIが再実行された
- [ ] 全てのCIが成功した（緑の ✓）
- [ ] PRをマージした
- [ ] mainブランチに修正が反映された

## よくあるエラー

| 症状 | 原因 | 対処 |
|------|------|------|
| ruff checkでまだエラーが出る | 修正漏れ | エラーメッセージを読んで該当箇所を修正 |
| pytestでまだ失敗する | テストの期待値が間違っている | テストコードの `assert` の値を確認 |
| pushしてもCIが動かない | ブランチが違う | PRのブランチにpushしているか確認 |
| マージボタンが押せない | CIが成功していない | 全てのCIが緑になるまで修正を続ける |

## 完了条件

- 全てのCIが成功し、PRがmainブランチにマージされたらワーク④は完了です

## おめでとうございます！

これで、以下の一連のCI/CD開発フローを体験しました:

1. ✅ GitHub Actionsで最小CIを動かす（ワーク①）
2. ✅ Lint/テストをCIに追加し、失敗を確認する（ワーク②）
3. ✅ AIレビューBotを導入し、自動レビューを受ける（ワーク③）
4. ✅ 指摘に対応してCIを通し、PRをマージする（ワーク④）

実際の開発現場でも、この「PR → CIチェック → レビュー → 修正 → マージ」の流れが日常的に使われています。
