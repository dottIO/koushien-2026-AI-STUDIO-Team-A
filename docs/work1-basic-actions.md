# ワーク①：ベースリポジトリにCIの土台を作る

## 目的

GitHub Actionsのworkflowがpushで実行されることを確認する。

この段階のゴールは、CIの中身を理解することではなく、**workflowファイルを置くとActionsが動く**ことを体験することです。

## 前提知識

- GitHub Actionsは、pushやpull requestなどのGitHub上のイベントをトリガーにワークフローを実行できる
- workflowファイルは `.github/workflows/` ディレクトリに置く
- ファイル形式はYAML

## 実施内容

以下の手順で進めてください。

### 1. workflowファイルを作成する

リポジトリのルートに `.github/workflows/ci.yml` を作成してください。

```
repository-root/
└── .github/
    └── workflows/
        └── ci.yml
```

### 2. 最小ワークフローを書く

以下の内容を `ci.yml` に書いてください。

```yaml
name: Basic CI

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Show message
        run: echo "GitHub Actions is running!"
```

#### 各項目の意味

| 項目 | 意味 |
|------|------|
| `name` | ワークフローの名前（Actionsタブに表示される） |
| `on: push` | pushされたときに実行する |
| `jobs` | 実行するジョブの定義 |
| `runs-on` | 実行環境（Ubuntu） |
| `steps` | ジョブ内で実行するステップ |
| `run` | シェルコマンドを実行する |

### 3. コミットしてpushする

```bash
git add .github/workflows/ci.yml
git commit -m "Add basic CI workflow"
git push
```

### 4. Actionsタブで実行結果を確認する

1. GitHubのリポジトリページを開く
2. 上部の「Actions」タブをクリックする
3. 実行されたワークフローが表示される
4. 緑のチェックマーク ✓ が付いていれば成功

### 5. 確認すること

- [ ] `.github/workflows/ci.yml` が作成されている
- [ ] pushしたらActionsタブにワークフローが表示された
- [ ] ワークフローが成功（緑）になった
- [ ] ログに `GitHub Actions is running!` と表示されている

## 注意事項

- この段階ではTODOアプリのテストやLintはまだ入れない
- 以降のワーク②でも同じリポジトリを使う
- workflowファイルの場所は必ず `.github/workflows/` 配下にすること（場所を間違えるとActionsが動かない）

## 成果物

- `.github/workflows/ci.yml`
- push時に成功するGitHub Actionsの実行結果

## 次のステップ

ワーク①が完了したら [ワーク②：サンプルプロジェクトにCIを追加する](work2-ci-pipeline.md) に進んでください。
