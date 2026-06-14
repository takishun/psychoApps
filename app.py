"""
psychoApps - 心理テストサイト
トップページ（テスト一覧）
"""
from dataclasses import dataclass
from typing import List

import streamlit as st

from src.test_template import DISCLAIMER


@dataclass
class TestEntry:
    """トップページに並べるテストの紹介情報。"""

    icon: str
    name: str
    summary: str
    page_path: str  # st.page_link に渡すページファイルのパス


# サイトに収録するテスト一覧
TESTS: List[TestEntry] = [
    TestEntry(
        icon="🌤️",
        name="ストレス度チェック",
        summary="最近のストレスの溜まり具合を8問でセルフチェック。",
        page_path="pages/1_ストレス度チェック.py",
    ),
    TestEntry(
        icon="🧭",
        name="性格タイプ診断",
        summary="内向／外向の傾向から、あなたの性格タイプを診断。",
        page_path="pages/2_性格タイプ診断.py",
    ),
    TestEntry(
        icon="💬",
        name="コミュニケーションタイプ診断",
        summary="対人関係での関わり方のタイプを6問で診断。",
        page_path="pages/3_コミュニケーションタイプ診断.py",
    ),
]


def main() -> None:
    """トップページを描画する。"""
    st.set_page_config(
        page_title="psychoApps - 心理テストサイト",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.title("🧠 psychoApps")
    st.subheader("かんたん心理テストで自分を知ろう")
    st.write(
        "気軽に取り組める心理テストを集めたサイトです。"
        "気になるテストを選んで、いくつかの質問に答えるだけで結果が分かります。"
    )

    st.divider()
    st.header("📋 テスト一覧")

    for test in TESTS:
        with st.container(border=True):
            st.markdown(f"### {test.icon} {test.name}")
            st.write(test.summary)
            st.page_link(test.page_path, label="このテストを始める ▶️")

    st.divider()
    st.caption(DISCLAIMER)
    st.markdown(
        "<div style='text-align:center;color:#888;'>"
        "<small>psychoApps 🧠 | Made with Streamlit</small></div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
