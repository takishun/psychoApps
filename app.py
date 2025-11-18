"""
psychoApps - 心理テストサイト
メインアプリケーション
"""
from typing import Dict, List
import streamlit as st


def main() -> None:
    """メインアプリケーション"""

    # ページ設定（必ず最初に実行）
    st.set_page_config(
        page_title="psychoApps - 心理テストサイト",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # セッション状態の初期化
    if 'visited' not in st.session_state:
        st.session_state.visited = False

    # ヘッダー
    st.title("🧠 psychoApps")
    st.subheader("あなたの心を知る心理テストサイト")

    # ウェルカムメッセージ
    st.markdown("""
    ようこそ！ psychoApps は、さまざまな心理テストを通じて、
    あなた自身の性格や傾向を知ることができるサイトです。
    """)

    st.divider()

    # 心理テスト一覧セクション
    st.header("📋 利用可能な心理テスト")

    # 心理テストの説明
    st.markdown("""
    左のサイドバーから、お好きな心理テストを選択してください。
    各テストは数分で完了し、すぐに結果を確認できます。
    """)

    # 統計情報（将来の拡張用）
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="利用可能なテスト",
            value="準備中",
            delta="Coming Soon"
        )

    with col2:
        st.metric(
            label="実施回数",
            value="0",
            delta="今すぐ始めましょう"
        )

    with col3:
        st.metric(
            label="平均所要時間",
            value="3-5分",
            delta="簡単・迅速"
        )

    st.divider()

    # 使い方セクション
    with st.expander("📖 使い方ガイド", expanded=False):
        st.markdown("""
        ### 心理テストの受け方

        1. **テストを選択**: 左のサイドバーから興味のある心理テストを選択
        2. **質問に回答**: 各質問に対して、直感的に答えてください
        3. **結果を確認**: すべての質問に答えると、結果が表示されます
        4. **結果を保存**: 必要に応じて結果を保存・シェアできます

        ### 注意事項

        - 心理テストは娯楽目的です。医療診断ではありません
        - 正直に答えることで、より正確な結果が得られます
        - 複数回受けることで、変化を観察できます
        """)

    # フッター
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <small>
        psychoApps - 心理テストサイト<br>
        Made with ❤️ using Streamlit
        </small>
    </div>
    """, unsafe_allow_html=True)

    # セッション状態を更新
    st.session_state.visited = True


if __name__ == "__main__":
    main()
