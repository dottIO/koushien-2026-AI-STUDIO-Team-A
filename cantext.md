GitHub Actions / Docker / Python Flask TODOアプリを使った授業教材リポジトリを作成してください。

目的は、GitHub ActionsによるCI、Pull Request上でのLint/テスト失敗確認、AIレビューBot導入、修正後の完成形PRフローを段階的に学習するための教材を作ることです。

前提

この教材では、ワーク①〜ワーク④を実施します。

各ワークで使用するファイルは、できるだけ完全に分離してください。
特に、アプリコード、Dockerfile、GitHub Actionsのworkflow yml、README、課題説明ファイルは、ワークごとに分かれている構成にしてください。

学生は、ワーク①で作成した空のGitHubリポジトリに対して、配布された source/work_x 配下のファイルをコピーしながら作業を進める想定です。

作成してほしいディレクトリ構成

以下の構成で作成してください。

repository-root/
├── README.md
├── source/
│   ├── work_1/
│   │   ├── README.md
│   │   └── .github/
│   │       └── workflows/
│   │           └── hello.yml
│   ├── work_2/
│   │   ├── README.md
│   │   ├── app.py
│   │   ├── todo.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── .dockerignore
│   │   ├── templates/
│   │   │   └── index.html
│   │   ├── tests/
│   │   │   ├── test_todo.py
│   │   │   └── test_app.py
│   │   └── .github/
│   │       └── workflows/
│   │           └── lint-test.yml
│   ├── work_3/
│   │   ├── README.md
│   │   ├── app.py
│   │   ├── todo.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── .dockerignore
│   │   ├── templates/
│   │   │   └── index.html
│   │   ├── tests/
│   │   │   ├── test_todo.py
│   │   │   └── test_app.py
│   │   └── .github/
│   │       └── workflows/
│   │           ├── lint-test.yml
│   │           └── ai-review.yml
│   └── work_4/
│       ├── README.md
│       ├── app.py
│       ├── todo.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── .dockerignore
│       ├── templates/
│       │   └── index.html
│       ├── tests/
│       │   ├── test_todo.py
│       │   └── test_app.py
│       └── .github/
│           └── workflows/
│               ├── lint-test.yml
│               └── ai-review.yml
└── assignments/
    ├── work_1.md
    ├── work_2.md
    ├── work_3.md
    └── work_4.md

重要な構成ルール

* source/work_1 には、最小のGitHub Actions workflowのみを置く
* source/work_2 には、TODOアプリ、Dockerfile、Lint/テスト用workflowを置く
* source/work_3 には、AIレビューBot用workflowを追加した状態のファイルを置く
* source/work_4 には、Lint/テスト/AIレビューがすべて通る完成状態のファイルを置く
* 各ワークは、単体で学生がコピーして使える状態にする
* Dockerfileやworkflow ymlはワークごとに分離する
* GitHub Actionsのworkflowファイルは、各 source/work_x/.github/workflows/ 配下に置く
* 学生は各ワークのタイミングで、該当する .github/workflows/*.yml を自分のリポジトリ直下の .github/workflows/ にコピーする想定

授業全体の流れ

以下の4つのワークに対応する教材を作成してください。

⸻

ワーク①：ベースリポジトリにCIの土台を作る

ゴール

GitHub上でリポジトリを作成し、push をトリガーに動く最小のGitHub Actions workflowを作成・実行する。

このリポジトリは、以降のワークでも継続して使用する。

作成対象

source/work_1/
├── README.md
└── .github/
    └── workflows/
        └── hello.yml

hello.yml の内容

push をトリガーにして、echo "Hello CI!" を出力するだけの最小workflowを作成してください。

例：

name: Hello CI
on:
  push:
jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Show hello message
        run: echo "Hello CI!"

work_1 READMEに含めること

以下を学生向けに説明してください。

* GitHubで空の新規リポジトリを作成する
* SourceTreeでリポジトリをクローンする
* VSCodeでクローンしたフォルダを開く
* .github/workflows/hello.yml を作成する
* SourceTreeでステージング・コミット・pushする
* GitHubのActionsタブでworkflow実行結果を確認する
* ログに Hello CI! が出力されていることを確認する
* このリポジトリを以降のワークでも継続して使用することを明記する

⸻

ワーク②：サンプルプロジェクトにCIを追加する

ゴール

TODOアプリに対して、Lintと自動テストを実行するCI workflowを追加する。

Pull Requestを作成し、CIが自動実行されることを確認する。

さらに、あえてLintまたはテストが失敗する状態を作り、PR上でCIがエラーを検知する様子を確認する。

作成対象

source/work_2/
├── README.md
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

TODOアプリの要件

Python + Flaskで作成してください。

初期機能は以下のみです。

* TODOを追加できる
* TODO一覧を画面に表示できる

以下はまだ実装しないでください。

* TODOの削除
* TODOの完了
* TODOの編集
* DB保存
* ログイン
* Docker Compose

データはメモリ上のリストで管理してください。

Flaskアプリ要件

app.py には、テストしやすいように create_app() を用意してください。

必要なルートは以下です。

* GET /
    * TODO一覧を表示する
* POST /add
    * TODOを追加する
    * 追加後 / にリダイレクトする

todo.py 要件

以下の関数を用意してください。

def create_todo(title: str) -> dict:
    pass
def add_todo(todos: list, title: str) -> list:
    pass

TODOデータは、以下のような形式にしてください。

{"title": "Sample task"}

意図的にCIで引っ掛かる内容

ワーク②では、CIが失敗する様子を確認するため、以下のどちらか、または両方を含めてください。

パターンA：Lintエラー

todo.py または app.py に、ruffで検出される未使用変数を入れてください。

例：

unused_value = "This variable is intentionally unused for CI demo"

この未使用変数にはコメントを付けて、授業用に意図的に残していることが分かるようにしてください。

# Intentionally unused variable for CI failure demo.
unused_value = "This variable is intentionally unused for CI demo"

パターンB：テスト失敗

tests/test_todo.py に、あえて失敗するテストを1つ含めてください。

例：

def test_add_todo_intentionally_fails():
    todos = []
    result = add_todo(todos, "Task 1")
    # Intentionally wrong expectation for CI failure demo.
    assert len(result) == 2

ただし、学生が原因を理解しやすいように、コメントで「授業用に意図的に失敗させている」ことを明記してください。

requirements.txt

以下を含めてください。

Flask
pytest
ruff

Dockerfile

Dockerfileのみで環境を構築してください。

Docker Composeやvenvは使いません。

要件：

* Python公式イメージを使う
* 作業ディレクトリは /app
* requirements.txt をコピーして依存関係をインストールする
* ソースコードをコピーする
* Flaskは 0.0.0.0 で起動する
* ポートは 3000 を使う

例：

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=3000", "--debug"]

lint-test.yml

GitHub Actionsで以下を実行するworkflowを作成してください。

* pushで実行
* pull_requestで実行
* Dockerイメージをビルド
* ruffでLintチェック
* pytestで自動テスト

例：

name: Lint and Test
on:
  push:
  pull_request:
jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t todo-app .
      - name: Run lint
        run: docker run --rm todo-app ruff check .
      - name: Run tests
        run: docker run --rm todo-app pytest

注意：

このworkflowは、学生が source/work_2 の中身をリポジトリ直下にコピーして使う想定です。
そのため、docker build -t todo-app . のように、カレントディレクトリを前提にしてください。

work_2 READMEに含めること

以下を学生向けに説明してください。

* source/work_2 一式をワーク①で作成したリポジトリ直下にコピーする
* Dockerfileを使ってローカルでアプリをビルドする
* Dockerfileを使ってアプリを起動する
* ブラウザで http://localhost:3000 にアクセスする
* .github/workflows/lint-test.yml を追加する
* SourceTreeで新しいブランチを作成する
* 変更をコミットしてpushする
* GitHub上でPull Requestを作成する
* PR上でCIが自動実行されることを確認する
* 意図的に混入されたLintエラーまたはテスト失敗により、CIが失敗することを確認する
* PR上で赤いバツやエラー表示を確認する

⸻

ワーク③：AIレビューBotをリポジトリに導入する

ゴール

同じリポジトリにAIレビューBotを導入し、意図的に書いた問題のあるコードに対する自動コメントを確認する。

作成対象

source/work_3/
├── README.md
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
        ├── lint-test.yml
        └── ai-review.yml

アプリ状態

source/work_3 には、ワーク②と同じTODOアプリを含めてください。

ただし、AIレビューBotが指摘しやすい「問題のあるコード」を意図的に含めてください。

例：

* 無駄なループ処理
* エラーハンドリング漏れ
* 不自然な条件分岐
* 読みにくい命名
* 重複コード
* パフォーマンス上意味のない処理

例：

def add_todo(todos: list, title: str) -> list:
    # Intentionally inefficient code for AI review demo.
    for _ in range(1000):
        pass
    todo = create_todo(title)
    todos.append(todo)
    return todos

コメントで、授業用に意図的に問題を入れていることを明記してください。

ai-review.yml

AIレビューBot用のGitHub Actions workflowを作成してください。

ただし、Copilot CLIやAIレビュー用Actionの正確なコマンド、認証方式、必要なSecrets名は環境によって変わる可能性があるため、以下のようなプレースホルダー付きの教材用ファイルにしてください。

実際の授業環境で使用するCLIコマンドやSecrets名に置き換えやすいようにしてください。

例：

name: AI Review
on:
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  ai-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Run AI review bot
        env:
          AI_REVIEW_TOKEN: ${{ secrets.AI_REVIEW_TOKEN }}
        run: |
          echo "Run AI review here"
          echo "Replace this step with Copilot CLI or your AI review command"

重要

ai-review.yml は、授業環境に合わせて修正する前提のテンプレートとして作成してください。

READMEには、以下を明記してください。

* AIレビューBotを動かすには、GitHub Secretsの設定が必要になる場合がある
* Secrets名やコマンドは授業環境に合わせて変更する
* このテンプレートでは AI_REVIEW_TOKEN を仮のSecrets名としている
* Copilot CLIやAIレビューBotの実行方式は、実際の環境に合わせて調整する

work_3 READMEに含めること

以下を学生向けに説明してください。

* ワーク②と同じブランチを使う
* source/work_3 の差分をリポジトリに反映する
* .github/workflows/ai-review.yml を追加する
* GitHub Secretsを設定する
* AIが指摘しやすい問題のあるコードを確認する
* SourceTreeでコミットしてpushする
* PR画面を開く
* AIレビューBotのworkflowが実行されることを確認する
* AI Botからレビューコメントが投稿されることを確認する

⸻

ワーク④：AIレビューの指摘に対応し、完成形のPRフローを確認する

ゴール

AIレビューの指摘とテスト失敗に対して修正を行い、再度CIとAIレビューが両方とも正常に走る完成形のPRフローを再現する。

作成対象

source/work_4/
├── README.md
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
        ├── lint-test.yml
        └── ai-review.yml

アプリ状態

source/work_4 には、以下を満たす完成版を配置してください。

* Lintが成功する
* pytestが成功する
* AIレビューで大きな指摘が出にくい、読みやすいコードになっている
* ワーク②で意図的に入れたLintエラーや失敗テストを修正済みにする
* ワーク③で入れた問題のあるコードを修正済みにする

修正内容の例

* 未使用変数を削除する
* 意図的に失敗していたテストの期待値を正しい値に直す
* 無駄なループ処理を削除する
* エラーハンドリングを追加する
* 関数名や変数名を分かりやすくする
* テストをすべて通る状態にする

work_4 READMEに含めること

以下を学生向けに説明してください。

* AIレビューBotからの指摘内容を確認する
* Lint/テスト失敗の原因を確認する
* VSCodeでコードを修正する
* Dockerでローカル実行確認をする
* Dockerでpytestを実行する
* SourceTreeで修正内容をコミットする
* 同じPRにpushする
* PR画面でLint/テスト/AIレビューが再実行されることを確認する
* すべて成功したら Merge pull request を押す
* mainブランチにマージして一連の開発フローを完了する

⸻

リポジトリ直下 README.md

リポジトリ直下の README.md には、教材全体の説明を書いてください。

以下の章立てにしてください。

# TODO App CI Teaching Materials
## 概要
## この教材の目的
## 対象者
## 使用技術
## 全体構成
## ワーク一覧
## 進め方
## 注意事項

READMEに含める内容

概要

この教材は、Python + FlaskのTODOアプリを使って、GitHub ActionsによるCI、Pull Request上でのCI確認、AIレビューBot、修正後のPRマージまでを体験するための教材であることを書いてください。

この教材の目的

以下を含めてください。

* GitHub Actionsの基本を理解する
* pushをトリガーにworkflowを実行する
* PRをトリガーにLint/テストを実行する
* CIの失敗をPR上で確認する
* AIレビューBotによる自動レビューを体験する
* CIとレビューを通してPRを完成させる流れを理解する

対象者

以下を想定してください。

* Git/GitHubの基本操作を学習済み
* SourceTreeでcommit/push/branch作成ができる
* VSCodeでファイル編集ができる
* Dockerの基本操作を学習済み
* Pythonの基本文法をある程度理解している

使用技術

以下を記載してください。

Python
Flask
pytest
ruff
Docker
GitHub Actions
GitHub Pull Request
AI Review Bot
SourceTree
VSCode

全体構成

source/work_1 〜 source/work_4 の役割を説明してください。

source/work_1: 最小のGitHub Actions workflow
source/work_2: TODOアプリ + Lint/テストCI + 意図的な失敗
source/work_3: AIレビューBot workflow + AIが指摘しやすい問題コード
source/work_4: Lint/テスト/AIレビューが通る完成状態
assignments/: 各ワークの学生向け手順書

注意事項

以下を記載してください。

* 各ワークのファイルは独立している
* 学生は必要なワークのファイルを自分のリポジトリにコピーして使用する
* Docker Composeは使用しない
* venvは使用しない
* Dockerfileのみで環境を作成する
* GitHub Actionsのworkflowは各ワークごとに分けて配置する
* AIレビューBotのworkflowは授業環境に合わせてSecretsやコマンドを調整する必要がある
* AIレビューBotのworkflowはテンプレートとして作成する

⸻

assignments 配下の手順書

以下の4ファイルを作成してください。

assignments/work_1.md
assignments/work_2.md
assignments/work_3.md
assignments/work_4.md

各ファイルには、学生がそのまま見て作業できるように、以下を含めてください。

* ワーク名
* ゴール
* 前提
* 使用するファイル
* 手順
* 確認ポイント
* よくあるエラー
* 完了条件

assignments/work_1.md

内容は以下をベースにしてください。

* GitHubで空の新規リポジトリを作成
* SourceTreeでクローン
* VSCodeで開く
* source/work_1/.github/workflows/hello.yml の内容を、リポジトリ直下の .github/workflows/hello.yml として作成
* SourceTreeでcommit/push
* GitHub Actionsタブで実行確認
* Hello CI! のログ確認
* 以降のワークでも同じリポジトリを使うことを明記

assignments/work_2.md

内容は以下をベースにしてください。

* source/work_2 一式をワーク①のリポジトリ直下にコピー
* Dockerfileを直接ビルド
* docker build -t todo-app .
* docker run -d -p 3000:3000 todo-app
* http://localhost:3000 でアプリ確認
* .github/workflows/lint-test.yml を追加
* SourceTreeで新しいブランチ作成
* 変更をcommit/push
* GitHubでPR作成
* CIが自動実行されることを確認
* 意図的なLintエラーまたはテスト失敗によりCIが失敗することを確認
* PR上で赤いバツやエラー表示を確認

assignments/work_3.md

内容は以下をベースにしてください。

* AIレビューBot導入のための設定
* .github/workflows/ai-review.yml を追加
* GitHub Secretsに必要な認証情報を登録
* TODOアプリにAIが指摘しやすい問題コードを含める
* SourceTreeでcommit/push
* PR画面でAIレビューworkflowが実行されることを確認
* AI Botからレビューコメントが投稿されることを確認

assignments/work_4.md

内容は以下をベースにしてください。

* AIレビューBotの指摘内容を確認
* ワーク②で失敗したLint/テストの原因を修正
* ワーク③で追加した問題コードを修正
* Dockerでローカル実行確認
* Dockerでpytest実行
* SourceTreeでcommit/push
* PR画面でCIとAIレビューが再実行されることを確認
* すべて成功したらPRをマージ
* mainブランチにマージして一連の開発フローを完了

⸻

実装上の注意

* 学生向け教材なので、コードは短く読みやすくしてください
* Pythonコードには最低限のコメントを入れてください
* TODOアプリは複雑にしないでください
* DB、ログイン、Docker Compose、複雑なJavaScriptは使わないでください
* Dockerfileのみで環境を構築してください
* Flaskのポートは 3000 にしてください
* GitHub Actionsのworkflow ymlはワークごとに分けてください
* ワーク②ではCIが失敗する状態を意図的に含めてください
* ワーク④ではCIが成功する状態にしてください
* AIレビューBotのworkflowはテンプレートとして作成し、Secretsや実行コマンドは後から差し替えやすい形にしてください
