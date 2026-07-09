# ワーク③：AIレビューBotをリポジトリに導入する

## ゴール

同じリポジトリにAIレビューBotを導入し、意図的に書いた問題のあるコードに対する自動コメントを確認する。

## 前提

- ワーク②が完了していること
- ワーク②で作成したPRがまだオープンであること
- 同じブランチ（`feature/add-ci`）を使い続ける

## 使用するファイル

```
source/work_3/
├── todo.py                  ← AIが指摘しやすい問題コードを含む
└── .github/
    └── workflows/
        └── ai-review.yml   ← AIレビューBot用workflow
```

> **注意:** `source/work_3/` の全ファイルをコピーするのではなく、差分のみを反映してください。

## 手順

### 1. ai-review.yml をコピーする

`source/work_3/.github/workflows/ai-review.yml` を、自分のリポジトリの `.github/workflows/ai-review.yml` にコピーしてください。

コピー後のworkflows構成:

```
.github/workflows/
├── hello.yml         ← ワーク①
├── lint-test.yml     ← ワーク②
└── ai-review.yml     ← 今回追加
```

### 2. todo.py を更新する

`source/work_3/todo.py` の内容で、自分のリポジトリの `todo.py` を置き換えてください。

この `todo.py` には、AIレビューBotが指摘しやすい問題のあるコードが意図的に含まれています:

- 無駄なループ処理（`for _ in range(1000): pass`）
- 冗長な条件分岐（同じ内容を何重にもチェック）
- 非効率な実装（`len()` を使わず手動カウント）

### 3. GitHub Secretsを設定する（講師の指示に従う）

AIレビューBotを動かすには、GitHub Secretsの設定が必要な場合があります。

1. GitHubリポジトリの「Settings」を開く
2. 左メニュー「Secrets and variables」→「Actions」を選択
3. 「New repository secret」をクリック
4. 講師の指示に従ってSecrets名と値を設定する

> **注意:**
> - `ai-review.yml` はテンプレートです
> - Secrets名（`AI_REVIEW_TOKEN`）やコマンドは、授業環境に合わせて変更する場合があります
> - 講師からの指示を確認してください

### 4. SourceTreeでコミット・pushする

1. 変更ファイルをステージングする
   - `.github/workflows/ai-review.yml`
   - `todo.py`
2. コミットメッセージを入力する（例: `Add AI review bot and problematic code`）
3. 「コミット」をクリック
4. 「プッシュ」をクリック

### 5. PR画面を確認する

1. GitHubのPR画面を開く
2. CIが再実行されることを確認する
3. 「AI Review」workflowが実行されることを確認する

### 6. AIレビューコメントを確認する

- PR上にAI Botからのレビューコメントが投稿されることを確認する
- 問題のあるコードに対して、どのような指摘がされているか確認する

期待される指摘の例:
- 無駄なループ処理の削除を提案
- 冗長な条件分岐の簡素化を提案
- `len()` の使用を提案

## 確認ポイント

- [ ] `ai-review.yml` がリポジトリに追加された
- [ ] `todo.py` がAI指摘用の問題コードに更新された
- [ ] GitHub Secretsが設定された（必要な場合）
- [ ] pushしたらPR上でworkflowが再実行された
- [ ] 「AI Review」workflowが実行された
- [ ] AIからレビューコメントが投稿された

## よくあるエラー

| 症状 | 原因 | 対処 |
|------|------|------|
| AI Reviewが実行されない | workflowファイルの配置が間違っている | `.github/workflows/` 配下にあるか確認 |
| AI Reviewが認証エラーで失敗する | Secretsが設定されていない | GitHub Secretsを設定する |
| AIからコメントが来ない | permissions設定が不足 | workflowの `permissions` を確認 |
| 「Resource not accessible」エラー | リポジトリの権限設定 | Settings → Actions → General で権限を確認 |

## 完了条件

- AIレビューBotが動作し、問題のあるコードに対してコメントが投稿されたらワーク③は完了です
- **PRはまだマージしないでください。ワーク④で修正を行います。**
