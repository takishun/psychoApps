# psychoApps 🧠

かんたん心理テストサイト - Streamlitベースの自己理解アプリケーション

## 概要

psychoApps は、気軽に取り組める心理テストを集めた Web アプリケーションです。
Streamlit で構築されており、いくつかの質問に答えるだけで結果が分かります。
共通のテンプレート（基底クラス）を使うことで、新しいテストを少ないコードで追加できます。

> **注意**: 収録しているテストは自己理解を深めるための簡易的なものであり、
> 医学的・心理学的な診断ではありません。

## 収録テスト

| テスト | 内容 |
| --- | --- |
| 🌤️ ストレス度チェック | 最近のストレスの溜まり具合を8問でセルフチェック |
| 🧭 性格タイプ診断 | 内向／外向の傾向から性格タイプを診断 |
| 💬 コミュニケーションタイプ診断 | 対人関係での関わり方のタイプを診断 |

## セットアップ

### 前提条件

- Python 3.8以上

### インストール

```bash
git clone <repository-url>
cd psychoApps
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 実行

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスしてください。

## プロジェクト構造

```
psychoApps/
├── app.py                              # トップページ（テスト一覧）
├── pages/                              # 各心理テストのページ
│   ├── 1_ストレス度チェック.py
│   ├── 2_性格タイプ診断.py
│   └── 3_コミュニケーションタイプ診断.py
├── src/
│   └── test_template.py                # 心理テスト共通テンプレート（基底クラス）
├── tests/
│   └── test_template.py                # テンプレートのユニットテスト
├── .streamlit/config.toml              # Streamlit設定
├── requirements.txt
├── CLAUDE.md
└── README.md
```

## 新しいテストの追加方法

1. `src/test_template.py` の `PsychologicalTest` を継承したクラスを作る
2. `get_questions()` で質問（`Question`）のリストを返す
3. `get_results()` でスコア範囲ごとの結果（`Result`）を返す
4. `pages/` に新しいページファイルを作り、`set_page_config` のあとに `run()` を呼ぶ
5. `app.py` の `TESTS` にテストの紹介情報を追加する

```python
from src.test_template import PsychologicalTest, Question, Result


class MyTest(PsychologicalTest):
    def get_questions(self):
        return [Question(text="...", options=["A", "B"], scores=[0, 1])]

    def get_results(self):
        return [Result(title="...", description="...", score_range=(0, 1))]
```

## テスト

```bash
pytest
```

## 技術スタック

- **Streamlit** 1.29.0+ - Webアプリケーションフレームワーク
- **Python** 3.8+

## 作者

takishun (shun.takinami@gmail.com)
