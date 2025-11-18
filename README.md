# psychoApps 🧠

心理テストサイト - Streamlitベースの対話型心理テストアプリケーション

## 概要

psychoAppsは、様々な心理テストを提供するWebアプリケーションです。
Streamlitを使用して構築されており、直感的なインターフェースで心理テストを受けることができます。

## 機能

- 📊 複数の心理テスト（性格診断、ストレス耐性テストなど）
- 🎯 リアルタイムの結果表示
- 📱 レスポンシブデザイン
- 🔄 テンプレートベースの拡張可能なアーキテクチャ

## セットアップ

### 前提条件

- Python 3.8以上

### インストール

1. リポジトリをクローン
```bash
git clone <repository-url>
cd psychoApps
```

2. 仮想環境を作成・有効化
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 依存関係をインストール
```bash
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
├── app.py                    # メインアプリケーション
├── pages/                    # 各心理テストページ
│   ├── 1_性格診断テスト.py
│   └── 2_ストレス耐性テスト.py
├── src/                      # ソースコード
│   ├── pages/
│   │   └── test_template.py  # 心理テストテンプレート
│   ├── components/           # 再利用可能なコンポーネント
│   └── utils/                # ユーティリティ関数
├── .streamlit/               # Streamlit設定
│   └── config.toml
├── requirements.txt          # Python依存関係
└── README.md                 # このファイル
```

## 新しい心理テストの追加

テンプレートを使用して、簡単に新しい心理テストを追加できます：

1. `pages/` ディレクトリに新しいファイルを作成（例：`3_新しいテスト.py`）
2. `PsychologicalTestTemplate` を継承したクラスを作成
3. `get_questions()` と `get_results()` メソッドを実装

詳細は `src/pages/test_template.py` を参照してください。

## 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **Python 3.8+**: プログラミング言語
- **Pandas**: データ処理（オプション）
- **Plotly**: データ可視化（オプション）

## ライセンス

このプロジェクトは個人使用目的で開発されています。

## 貢献

プロジェクトへの貢献を歓迎します。Issue や Pull Request をお気軽にお送りください。

## 作者

takishun (shun.takinami@gmail.com)
