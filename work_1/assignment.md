# ワーク① ：ベースリポジトリにCIの土台を作る

## ゴール

GitHub上でリポジトリを作成し、pushをトリガーに動く最小のGitHub Actions workflowを作成・実行する。

このリポジトリは、以降のワーク②〜④でも継続して使用します。

## 前提

- GitHubアカウントを持っている
- SourceTreeがインストールされている
- VSCodeがインストールされている

## 使用するファイル

```
source/work_1/
└── .github/
    └── workflows/
        └── hello.yml
```

## 手順

### 1. GitHubで新規リポジトリを作成する

1. GitHubにログインする
2. 右上の「+」→「New repository」をクリック
3. リポジトリ名を入力する（例: `todo-ci-practice`）
4. 「Public」を選択する
5. 「Add a README file」にチェックを入れる
6. 「Create repository」をクリック

### 2. SourceTreeでクローンする

1. SourceTreeを開く
2. 「新規」→「URLからクローン」を選択
3. GitHubリポジトリのURLを貼り付ける
4. 保存先フォルダを選ぶ
5. 「クローン」をクリック

### 3. VSCodeで開く

1. VSCodeを起動する
2. 「ファイル」→「フォルダーを開く」
3. クローンしたフォルダを選択する

### 4. workflowファイルを作成する

VSCodeで以下のファイルを作成してください。

**ファイルパス:** `.github/workflows/hello.yml`

```yaml
name: Hello CI

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Show hello message
        run: echo "Hello CI!"
```

> **注意:** `.github/workflows/` ディレクトリがまだ存在しない場合は、フォルダごと作成してください。

### 5. SourceTreeでコミット・pushする

1. SourceTreeを開く
2. 変更されたファイルが表示されていることを確認する
3. `.github/workflows/hello.yml` をステージングする
4. コミットメッセージを入力する（例: `Add hello CI workflow`）
5. 「コミット」をクリック
6. 「プッシュ」をクリック

### 6. GitHub Actionsで実行結果を確認する

1. GitHubのリポジトリページを開く
2. 上部の「Actions」タブをクリック
3. 実行されたワークフロー「Hello CI」をクリック
4. ジョブ「hello」をクリック
5. ログに `Hello CI!` と表示されていることを確認する

## 確認ポイント

- [ ] GitHubに新規リポジトリが作成されている
- [ ] `.github/workflows/hello.yml` がリポジトリに存在する
- [ ] Actionsタブにワークフローが表示されている
- [ ] ワークフローが成功（緑のチェック ✓）になっている
- [ ] ログに `Hello CI!` が出力されている

## よくあるエラー

| 症状 | 原因 | 対処 |
|------|------|------|
| Actionsタブにworkflowが表示されない | ファイルの置き場所が間違っている | `.github/workflows/` 配下にあるか確認 |
| YAMLのパースエラー | インデントが間違っている | スペース2つでインデントする |
| workflowが実行されない | ファイル名の拡張子が `.yml` でない | `.yml` または `.yaml` にする |

## 完了条件

- GitHub Actionsが正常に実行され、ログに `Hello CI!` が表示されたらワーク①は完了です
- **このリポジトリは削除しないでください。ワーク②以降も同じリポジトリを使います。**
