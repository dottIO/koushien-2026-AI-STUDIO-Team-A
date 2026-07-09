# ワーク③ ソースファイル

## 概要

このディレクトリには、AIレビューBot用のworkflowを追加した状態のファイルが含まれています。

また、AIレビューBotが指摘しやすい「問題のあるコード」が意図的に含まれています。

## 含まれるファイル

```
work_3/
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

## ワーク②との差分

- `.github/workflows/ai-review.yml` が追加されている
- `todo.py` にAIが指摘しやすい問題コードが含まれている
- 未使用変数や意図的失敗テストはワーク②と同じ

## AIレビューBotについて

- `ai-review.yml` はテンプレートです
- 実際に動かすには、GitHub Secretsの設定が必要です
- Secrets名やコマンドは授業環境に合わせて変更してください
- このテンプレートでは `AI_REVIEW_TOKEN` を仮のSecrets名としています
