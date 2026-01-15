"""
psychoApps - 子育てフレーズ集
メインアプリケーション
"""
from typing import Dict, List
import streamlit as st


def main() -> None:
    """メインアプリケーション"""

    # ページ設定（必ず最初に実行）
    st.set_page_config(
        page_title="psychoApps - 子育てフレーズ集",
        page_icon="👶",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # セッション状態の初期化
    if 'visited' not in st.session_state:
        st.session_state.visited = False

    # ヘッダー
    st.title("👶 psychoApps")
    st.subheader("子育てでよく使うフレーズをすぐに送信")

    # ウェルカムメッセージ
    st.markdown("""
    ようこそ！ psychoApps は、子育てでよく使うフレーズを簡単に検索・コピーできる
    アプリケーションです。保育園への連絡、祖父母への依頼、パートナーとの共有など、
    様々な場面で使える100以上のフレーズを収録しています。
    """)

    st.divider()

    # フレーズ集の案内セクション
    st.header("📋 子育てフレーズ集について")

    # フレーズ集の説明
    st.markdown("""
    左のサイドバーから「子育てフレーズ集」を選択してください。
    カテゴリ別に整理された100以上のフレーズから、すぐに使いたいものを検索・選択できます。
    """)

    # 統計情報
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="収録フレーズ数",
            value="100+",
            delta="11カテゴリ"
        )

    with col2:
        st.metric(
            label="利用シーン",
            value="多彩",
            delta="保育園・家族・パートナー"
        )

    with col3:
        st.metric(
            label="使いやすさ",
            value="簡単",
            delta="検索・コピー・送信"
        )

    st.divider()

    # 使い方セクション
    with st.expander("📖 使い方ガイド", expanded=False):
        st.markdown("""
        ### 基本的な使い方

        1. **ページを開く**: 左のサイドバーから「子育てフレーズ集」を選択
        2. **検索する**: キーワードで検索ボックスから絞り込み（例: 「おはよう」「食事」）
        3. **カテゴリを選択**: サイドバーから特定のカテゴリを選択
        4. **フレーズをクリック**: 使いたいフレーズをクリックして選択
        5. **コピー&送信**: 表示されたフレーズをコピーしてLINEなどに送信

        ### こんな場面で便利

        - 🏫 保育園・幼稚園の先生への連絡
        - 👵 祖父母への子育て依頼メッセージ
        - 💑 パートナーとの子育て情報共有
        - 👨‍👩‍👧 ベビーシッターへの指示・お願い

        ### 収録カテゴリ

        朝の挨拶・起床、食事、遊び・外出、励まし・ほめる、しつけ・注意、
        お風呂、就寝・夜、トイレ・おむつ、お出かけ準備、感情のサポート、
        お手伝い・生活習慣
        """)

    # フッター
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <small>
        psychoApps - 子育てフレーズ集 👶<br>
        子育てを応援します | Made with ❤️ using Streamlit
        </small>
    </div>
    """, unsafe_allow_html=True)

    # セッション状態を更新
    st.session_state.visited = True


if __name__ == "__main__":
    main()
