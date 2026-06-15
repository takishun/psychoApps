"""
アフィリエイト枠の共通モジュール（A8.net 対応）

CTR（クリック率）が高くなりやすい位置に広告枠を確保する。
いまは「予約済みの広告枠（プレースホルダ）」を表示し、A8.net の広告リンク
（スニペット）が用意できたら下の ``AFFILIATE_SNIPPETS`` に貼り付けるだけで
有効化できる。

広告枠の表示位置（CTRが高い順）:
  1. 結果ページの結果直下 …… ユーザーの関心が最も高まる瞬間
  2. サイドバー …… テスト中も常に表示される
  3. トップページ …… 回遊中のユーザーに訴求

------------------------------------------------------------------
★ A8.net の広告を設置する手順 ★
  1. A8.net の管理画面で広告リンク（バナー/テキスト）のコードを取得する。
  2. そのHTMLコードを、下の ``AFFILIATE_SNIPPETS`` の該当グループに
     文字列として貼り付ける（複数行は三連クォートで囲む）。
  3. 空文字のままなら「広告枠（設置予定）」のプレースホルダが表示される。
------------------------------------------------------------------
"""
from __future__ import annotations

from typing import Dict

import streamlit as st
import streamlit.components.v1 as components


# ステマ規制（景品表示法）対応のための広告表記。必ず枠とともに表示する。
AD_LABEL = "広告（PR）"

# 広告スニペットを iframe で描画する高さ(px)。バナーサイズに合わせて調整する。
SNIPPET_HEIGHT = 140

# 結果テーマごとの広告枠。各テストの結果からキーで参照する。
# 値には A8.net で発行した広告リンクのHTMLコードを貼り付ける（空ならプレースホルダ表示）。
AFFILIATE_SNIPPETS: Dict[str, str] = {
    # ストレス・リラックス系の結果向け（快眠・瞑想・リラックスグッズ など）
    "stress_relief": "",
    # 自己理解・成長系の結果向け（心理学の本・自己分析ツール など）
    "self_growth": "",
    # コミュニケーション系の結果向け（話し方の本・学習講座 など）
    "communication": "",
    # 汎用（トップページ・フォールバック用）
    "general": "",
}


def get_snippet(group: str) -> str:
    """グループに対応する広告スニペットを返す（未定義のキーは general にフォールバック）。"""
    return AFFILIATE_SNIPPETS.get(group, AFFILIATE_SNIPPETS["general"])


def _render_slot_body(group: str) -> None:
    """広告枠の中身を描画する。スニペット未設定ならプレースホルダを出す。"""
    snippet = get_snippet(group)
    if snippet.strip():
        components.html(snippet, height=SNIPPET_HEIGHT)
    else:
        st.markdown(
            "<div style='border:1px dashed #cbd5e0;border-radius:8px;"
            "padding:28px 16px;text-align:center;color:#9aa5b1;'>"
            "A8.net 広告枠（設置予定）<br>"
            "<small>ここに広告スニペットが表示されます</small></div>",
            unsafe_allow_html=True,
        )


def render_affiliate_cards(group: str, heading: str = "🎁 あなたへのおすすめ") -> None:
    """結果ページ・トップページ用の広告枠を描画する（高CTR位置向け）。

    Args:
        group: ``AFFILIATE_SNIPPETS`` のキー。
        heading: 枠の見出し。
    """
    st.divider()
    st.subheader(heading)
    st.caption(AD_LABEL)
    _render_slot_body(group)


def render_affiliate_sidebar(group: str) -> None:
    """サイドバー用の広告枠を描画する（常時表示でCTRを補完）。

    Args:
        group: ``AFFILIATE_SNIPPETS`` のキー。
    """
    with st.sidebar:
        st.divider()
        st.caption(f"{AD_LABEL} ｜ PR")
        _render_slot_body(group)
