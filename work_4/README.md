# ワーク④ ソースファイル

## 概要

このディレクトリには、Lint/テスト/AIレビューがすべて通る完成状態のファイルが含まれています。

ワーク②で意図的に入れたLintエラーや失敗テスト、ワーク③で入れた問題コードがすべて修正済みです。

## 含まれるファイル

```
work_4/
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
```

## ワーク③との差分

- 未使用変数を削除
- 意図的に失敗していたテストを修正
- 無駄なループ処理を削除
- 冗長な条件分岐をシンプルに修正
- 非効率なカウント関数を削除

## 使い方

1. ワーク③の状態から、このディレクトリの内容に修正する
2. Dockerでテストを実行して全て成功することを確認する
3. コミットしてpushする
4. PR上でCIが成功することを確認する
5. PRをマージする
