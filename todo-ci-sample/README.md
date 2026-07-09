# TODO App（CI授業用サンプル）

GitHub ActionsでCI（継続的インテグレーション）を学ぶための、シンプルなTODOアプリです。

## アプリ概要

- Python + Flask で作られたTODOアプリ
- TODOの追加と一覧表示ができます
- データはメモリ上で管理（アプリ再起動でリセットされます）

## セットアップ手順

### 1. Dockerイメージをビルドする

```bash
docker build -t todo-ci-sample .
```

### 2. コンテナを起動する

```bash
docker run --rm -p 5001:5001 todo-ci-sample
```

### 3. ブラウザでアクセスする

http://localhost:5001

## テストの実行方法

Dockerを使ってpytestを実行します。

```bash
docker run --rm todo-ci-sample pytest
```

または、より明示的に以下のコマンドでも実行できます。

```bash
docker run --rm todo-ci-sample python -m pytest
```

## ディレクトリ構成

```
todo-ci-sample/
├── app.py              # Flaskアプリ本体
├── todo.py             # TODOロジック
├── requirements.txt    # Python依存パッケージ
├── Dockerfile          # Docker環境定義
├── .dockerignore       # Docker除外ファイル
├── templates/
│   └── index.html      # HTMLテンプレート
├── tests/
│   ├── test_todo.py    # todo.py のテスト
│   └── test_app.py     # app.py のテスト
└── README.md           # このファイル
```
