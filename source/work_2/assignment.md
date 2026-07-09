# ワーク②：サンプルプロジェクトにCIを追加する

## ゴール

TODOアプリに対して、LintとテストをPR上で自動実行するCIを構築する。

さらに、意図的にCIが失敗する状態を確認し、PR上でエラー表示を確認する。

## 前提

- ワーク①が完了していること
- ワーク①で作成したリポジトリを使用する
- Dockerがインストールされていること

## 使用するファイル

```
source/work_2/
├── app.py
├── todo.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── templates/
│   └── index.html
├── tests/
│   ├── test_todo.py
│   └── test_app.py
└── .github/
    └── workflows/
        └── lint-test.yml
```

## 手順

### 1. ソースファイルをリポジトリにコピーする

`source/work_2/` の中身を、ワーク①で作成したリポジトリの直下にコピーしてください。

コピー後のリポジトリ構成:

```
your-repository/
├── .github/
│   └── workflows/
│       ├── hello.yml        ← ワーク①で作成済み
│       └── lint-test.yml    ← 今回追加
├── app.py
├── todo.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── templates/
│   └── index.html
└── tests/
    ├── test_todo.py
    └── test_app.py
```

### 2. Dockerでアプリをビルド・起動する

ターミナル（VSCodeのターミナルでも可）で以下を実行してください。

```bash
docker build -t todo-app .
```

```bash
docker run -d -p 3000:3000 todo-app
```

### 3. ブラウザで確認する

ブラウザで以下にアクセスしてください。

```
http://localhost:3000
```

- TODOの入力欄が表示される
- テキストを入力して「追加」ボタンを押すとTODOが追加される

確認が終わったらコンテナを停止してください。

```bash
docker stop $(docker ps -q --filter ancestor=todo-app)
```

### 4. SourceTreeで新しいブランチを作成する

1. SourceTreeを開く
2. 「ブランチ」→「新規ブランチ」を選択
3. ブランチ名を入力する（例: `feature/add-ci`）
4. 「ブランチを作成」をクリック

### 5. SourceTreeでコミット・pushする

1. 全ての変更ファイルをステージングする
2. コミットメッセージを入力する（例: `Add TODO app with CI workflow`）
3. 「コミット」をクリック
4. 「プッシュ」をクリック

### 6. GitHubでPull Requestを作成する

1. GitHubのリポジトリページを開く
2. 「Pull requests」タブをクリック
3. 「New pull request」をクリック
4. base: `main` ← compare: `feature/add-ci` を選択
5. 「Create pull request」をクリック

### 7. CIの実行結果を確認する

PR画面の下部に、CIの実行状況が表示されます。

**このワークでは、CIが失敗します。** これは意図的です。

失敗の原因:
- `todo.py` に未使用変数があるため、ruffのLintチェックで失敗する
- `tests/test_todo.py` に意図的に失敗するテストが含まれている

### 8. エラーの内容を確認する

1. PR画面で赤い ✗ マークをクリック
2. 「Details」をクリック
3. エラーのログを確認する

確認すべきこと:
- Lintエラー: `unused_value` が未使用変数として検出されている
- テスト失敗: `test_add_todo_intentionally_fails` が `assert len(result) == 2` で失敗している

## 確認ポイント

- [ ] Dockerでアプリが起動し、ブラウザで確認できた
- [ ] featureブランチを作成できた
- [ ] PRを作成できた
- [ ] PR上でCIが自動実行された
- [ ] CIが失敗した（赤い ✗ マーク）
- [ ] エラーログの内容を確認した

## よくあるエラー

| 症状 | 原因 | 対処 |
|------|------|------|
| Docker buildが失敗する | Dockerが起動していない | Docker Desktopを起動する |
| ポート3000が使えない | 他のプロセスが使用中 | 別のポートを使うか、既存プロセスを停止 |
| CIでDocker buildが失敗する | Dockerfileがリポジトリ直下にない | ファイルの配置を確認する |
| workflowが実行されない | `.github/workflows/` の配置が間違っている | パスを確認する |

## 完了条件

- PR上でCIが実行され、**意図的に失敗する**ことを確認できたらワーク②は完了です
- **PRはまだマージしないでください。ワーク③で引き続き使用します。**
