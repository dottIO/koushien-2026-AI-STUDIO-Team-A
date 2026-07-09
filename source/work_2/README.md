# ワーク② ソースファイル

## 概要

このディレクトリには、TODOアプリ本体とLint/テスト用のCI workflowが含まれています。

意図的にCIが失敗する内容が含まれています。これは授業で「CIの失敗を確認する」ために意図的に入れたものです。

## 含まれるファイル

```
work_2/
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

## 使い方

1. このディレクトリの中身一式を、ワーク①で作成したリポジトリ直下にコピーする
2. `.github/workflows/lint-test.yml` もリポジトリ直下の `.github/workflows/` にコピーする
3. Dockerイメージをビルドする

```bash
docker build -t todo-app .
```

4. コンテナを起動する

```bash
docker run -d -p 3000:3000 todo-app
```

5. ブラウザで http://localhost:3000 にアクセスする

## CIについて

このワークでは、意図的にLintエラーとテスト失敗が含まれています。

- `todo.py` に未使用変数（ruffで検出される）
- `tests/test_todo.py` に意図的に失敗するテスト

PRを作成すると、CIが失敗することを確認してください。
