# TODO CI Teaching Materials

## 概要

このリポジトリは、GitHub ActionsによるCI（継続的インテグレーション）学習のための教材です。

- Python + Flaskで作成したシンプルなTODOアプリを含んでいます
- 初期状態ではTODOの追加と一覧表示のみができます
- 学生がコードを追加修正し、CIの成功・失敗を体験する構成になっています

## この教材の目的

この教材を通じて、以下を学びます。

- CI/CDの概念を理解する
- GitHub ActionsでCIを実装する
- pytestを使って自動テストを実行する
- コード変更時にCIが成功・失敗する流れを確認する

## 使用技術

| 技術 | 用途 |
|------|------|
| Python | アプリケーション言語 |
| Flask | Webフレームワーク |
| pytest | テストフレームワーク |
| Docker | 実行環境 |
| GitHub Actions | CI実行環境 |

## リポジトリ構成

```
repository-root/
├── todo-ci-sample/          ← アプリ本体
│   ├── app.py
│   ├── todo.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── templates/
│   │   └── index.html
│   └── tests/
│       ├── test_todo.py
│       └── test_app.py
├── docs/                    ← ワーク手順書
│   ├── work1-basic-actions.md
│   └── work2-ci-pipeline.md
├── assignments/             ← 実装課題
│   └── add-delete-button-task.md
└── README.md
```

| ディレクトリ | 役割 |
|-------------|------|
| `todo-ci-sample/` | 実際に動かすアプリ本体 |
| `docs/` | ワークの進行手順（授業中に順番に読む） |
| `assignments/` | コーディング課題の実装指示 |

## サンプルアプリの場所

サンプルアプリ本体は `todo-ci-sample/` 配下にあります。

Dockerコマンドやpytestコマンドは、基本的に `todo-ci-sample/` ディレクトリ内で実行します。

## Dockerでの起動方法

まず、サンプルアプリのディレクトリに移動します。

```bash
cd todo-ci-sample
```

Dockerイメージをビルドします。

```bash
docker build -t todo-ci-sample .
```

コンテナを起動します。

```bash
docker run --rm -p 5000:5000 todo-ci-sample
```

ブラウザで以下にアクセスしてください。

```
http://localhost:5000
```

## アプリの使い方

1. ブラウザで `http://localhost:5000` にアクセスする
2. テキスト入力欄にTODOのタイトルを入力する
3. 「追加」ボタンを押すとTODOが一覧に追加される

## テストの実行方法

Dockerを使ってpytestを実行します。

```bash
cd todo-ci-sample
docker run --rm todo-ci-sample pytest
```

または、以下でも実行できます。

```bash
cd todo-ci-sample
docker run --rm todo-ci-sample python -m pytest
```

## ワークの進め方

この教材は2つのワークで構成されています。順番に進めてください。

| ワーク | 内容 | 手順書 |
|--------|------|--------|
| ワーク① | GitHub Actionsの土台を作る | [docs/work1-basic-actions.md](docs/work1-basic-actions.md) |
| ワーク② | TODOアプリにCIを追加する | [docs/work2-ci-pipeline.md](docs/work2-ci-pipeline.md) |

### ワーク①：ベースリポジトリにCIの土台を作る

- `.github/workflows/ci.yml` を作成する
- `echo` を実行する最小ワークフローを書く
- pushしてActionsタブで動作を確認する

### ワーク②：サンプルプロジェクトにCIを追加する

- Docker build + pytest + ruff を実行するCIを構築する
- PRを作成してCIの自動実行を確認する
- 意図的にテストを失敗させ、CI失敗を体験する
- 修正してCIを成功させる

workflowファイルは初期状態では含まれていません。ワーク①で作成します。

## 追加修正課題

ワーク②の中で、TODOの削除ボタンを追加する課題に取り組みます。

実装の詳細は [assignments/add-delete-button-task.md](assignments/add-delete-button-task.md) を参照してください。

この課題では、まずテストを追加してCIを失敗させ、その後実装を追加してCIを成功させます。

## 注意事項

- venvは使用しない（Dockerで環境を構築する）
- Docker Composeは使用しない
- DBは使用しない（データはメモリ上で管理する）
- アプリを再起動するとTODOは消える
- GitHub Actionsのworkflowファイルは授業中に作成するため、初期状態では含めない
- ワーク手順書は `docs/` 配下に置く
- 実装課題の指示ファイルは `assignments/` 配下に置く
- サンプルアプリ本体は `todo-ci-sample/` 配下に置く
