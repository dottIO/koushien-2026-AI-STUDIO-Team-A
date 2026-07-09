# ワーク① ソースファイル

## 概要

このディレクトリには、ワーク①で使用する最小のGitHub Actions workflowファイルが含まれています。

## 含まれるファイル

```
work_1/
└── .github/
    └── workflows/
        └── hello.yml
```

## 使い方

1. GitHubで空の新規リポジトリを作成する
2. SourceTreeでリポジトリをクローンする
3. VSCodeでクローンしたフォルダを開く
4. このディレクトリの `.github/workflows/hello.yml` の内容を、自分のリポジトリ直下の `.github/workflows/hello.yml` として作成する
5. SourceTreeでステージング・コミット・pushする
6. GitHubのActionsタブでworkflow実行結果を確認する
7. ログに `Hello CI!` が出力されていることを確認する

## 重要

このリポジトリは、以降のワーク②〜④でも継続して使用します。削除しないでください。
