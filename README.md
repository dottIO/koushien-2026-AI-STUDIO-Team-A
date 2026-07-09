# TODO App CI Teaching Materials

## 概要

この教材は、Python + FlaskのTODOアプリを使って、以下を段階的に体験するための授業教材です。

- GitHub ActionsによるCI（継続的インテグレーション）
- Pull Request上でのLint/テスト失敗の確認
- AIレビューBotによる自動コードレビュー
- 修正後のPRマージまでの一連の開発フロー

## この教材の目的

この教材を通じて、以下を学びます。

- GitHub Actionsの基本を理解する
- pushをトリガーにworkflowを実行する
- PRをトリガーにLint/テストを実行する
- CIの失敗をPR上で確認する
- AIレビューBotによる自動レビューを体験する
- CIとレビューを通してPRを完成させる流れを理解する

## 対象者

以下を想定しています。

- Git/GitHubの基本操作を学習済み
- SourceTreeでcommit/push/branch作成ができる
- VSCodeでファイル編集ができる
- Dockerの基本操作を学習済み
- Pythonの基本文法をある程度理解している

## 使用技術

| 技術 | 用途 |
|------|------|
| Python | アプリケーション言語 |
| Flask | Webフレームワーク |
| pytest | テストフレームワーク |
| ruff | Lintツール |
| Docker | 実行環境 |
| GitHub Actions | CI実行環境 |
| GitHub Pull Request | コードレビュー・マージフロー |
| AI Review Bot | 自動コードレビュー |
| SourceTree | Gitクライアント |
| VSCode | コードエディタ |

## 全体構成

```
repository-root/
├── README.md                  ← この教材全体の説明
├── source/
│   ├── work_1/               ← 最小のGitHub Actions workflow
│   │   ├── assignment.md     ← 学生向け手順書
│   │   └── .github/workflows/hello.yml
│   ├── work_2/               ← TODOアプリ + Lint/テストCI + 意図的な失敗
│   │   ├── assignment.md     ← 学生向け手順書
│   │   ├── app.py, todo.py, Dockerfile, etc.
│   │   └── .github/workflows/lint-test.yml
│   ├── work_3/               ← AIレビューBot workflow + 問題コード
│   │   ├── assignment.md     ← 学生向け手順書
│   │   ├── app.py, todo.py, Dockerfile, etc.
│   │   └── .github/workflows/lint-test.yml + ai-review.yml
│   ├── work_4/               ← Lint/テスト/AIレビューが通る完成状態
│   │   ├── assignment.md     ← 学生向け手順書
│   │   ├── app.py, todo.py, Dockerfile, etc.
│   │   └── .github/workflows/lint-test.yml + ai-review.yml
│   └── demo/                 ← ワーク4完了後の完成形（参考用）
│       ├── app.py, todo.py, Dockerfile, etc.
│       └── .github/workflows/lint-test.yml + ai-review.yml
└── cantext.md
```

各ワークのフォルダはそれぞれ独立しており、zipで配布可能です。
`assignment.md` が学生向け手順書、それ以外がソースファイルです。

## ワーク一覧

| ワーク | 内容 | ゴール |
|--------|------|--------|
| ワーク① | ベースリポジトリにCIの土台を作る | pushで最小workflowが動くことを確認 |
| ワーク② | サンプルプロジェクトにCIを追加する | PR上でLint/テスト失敗を確認 |
| ワーク③ | AIレビューBotを導入する | AIからの自動レビューコメントを確認 |
| ワーク④ | 指摘に対応し完成形PRを作る | CI成功・レビュー通過・PRマージ |

## 進め方

1. ワーク①で空のGitHubリポジトリを作成する
2. 各ワークの `source/work_x` フォルダを配布（またはzip展開）する
3. フォルダ内の `assignment.md` の手順に従って進める
4. 各ワークの完了条件を満たしたら次に進む

## 注意事項

- 各ワークのファイルは独立している
- 学生は必要なワークのファイルを自分のリポジトリにコピーして使用する
- Docker Composeは使用しない
- venvは使用しない
- Dockerfileのみで環境を作成する
- GitHub Actionsのworkflowは各ワークごとに分けて配置する
- AIレビューBotのworkflowは授業環境に合わせてSecretsやコマンドを調整する必要がある
- AIレビューBotのworkflowはテンプレートとして作成している
- `source/demo/` はワーク4まで完了した参考用の完成形
