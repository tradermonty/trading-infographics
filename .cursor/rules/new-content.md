# 新しいコンテンツ追加時の手順

## 依頼方法
以下のいずれかの方法で依頼してください：

1. シンプルな依頼：
```
新しいコンテンツを追加しました。いつものようにgit statusで差分を確認して、目次に項目を追加して、git commit , pushまでお願い。
```

2. 詳細な依頼：
```
新しいコンテンツ「[日本語タイトル]」を追加しました。
ファイルパス: infographics/[ファイル名].html
カテゴリ: [カテゴリ名]
```

## 1. 変更の確認
```bash
git status
```
- 新しいコンテンツファイルの確認
- 変更が必要なファイルの確認

## 2. index.htmlの更新
- 適切なカテゴリに新しいコンテンツのリンクを追加
- リンクの形式：
```html
<li><a href="infographics/[ファイル名].html">[日本語タイトル]</a></li>
```

## 3. 変更のコミット
```bash
# 変更したファイルをステージングエリアに追加
git add [新しいコンテンツファイル] index.html

# 変更をコミット
git commit -m "feat: [日本語タイトル]を追加"

# 変更をリモートリポジトリにプッシュ
git push origin main
```

## 注意事項
- コミットメッセージは日本語で記述
- ファイル名は英語で記述
- タイトルは日本語で記述
- カテゴリは適切なものを選択