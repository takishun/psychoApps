"""
アフィリエイト枠の共通モジュール

CTR（クリック率）が高くなりやすい位置に、コンテキストに合った
おすすめ枠を表示するためのコンポーネント。

おすすめ枠の表示位置（CTRが高い順）:
  1. 結果ページの結果直下 …… ユーザーの関心が最も高まる瞬間
  2. サイドバー …… テスト中も常に表示される
  3. トップページ …… 回遊中のユーザーに訴求

------------------------------------------------------------------
★ 実運用にあたっての設定 ★
  下の AFFILIATE_GROUPS の各 ``url`` を、実際のアフィリエイトリンク
  （A8.net / 楽天アフィリエイト / Amazonアソシエイト 等）に
  置き換えてください。``https://example.com/...`` はすべてダミーです。
------------------------------------------------------------------
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import streamlit as st


# ステマ規制（景品表示法）対応のための広告表記。必ず枠とともに表示する。
AD_LABEL = "広告（PR）"


@dataclass
class AffiliateItem:
    """アフィリエイト1件分の表示情報。"""

    title: str
    description: str
    url: str  # TODO: 実際のアフィリエイトリンクに置き換える
    cta: str = "詳しく見る"


# テスト結果のテーマごとにおすすめをまとめたグループ。
# 各テストの結果（Result.affiliate_group）からキーで参照する。
AFFILIATE_GROUPS: Dict[str, List[AffiliateItem]] = {
    # ストレス・リラックス系
    "stress_relief": [
        AffiliateItem(
            title="睡眠の質を高めるアイテム",
            description="寝つきや疲労回復をサポートする快眠グッズ。",
            url="https://example.com/affiliate/sleep",
        ),
        AffiliateItem(
            title="瞑想・マインドフルネスアプリ",
            description="数分の習慣で気持ちを落ち着けるアプリ。",
            url="https://example.com/affiliate/meditation",
        ),
        AffiliateItem(
            title="リラックスできるハーブティー",
            description="ほっと一息つきたい時間のおともに。",
            url="https://example.com/affiliate/herbtea",
        ),
    ],
    # 自己理解・成長系
    "self_growth": [
        AffiliateItem(
            title="性格・心理学の入門書",
            description="自分のタイプをもっと深く理解できる一冊。",
            url="https://example.com/affiliate/psychology-book",
        ),
        AffiliateItem(
            title="自己分析・手帳ツール",
            description="毎日の気づきを記録して自分を知る。",
            url="https://example.com/affiliate/journal",
        ),
    ],
    # コミュニケーション系
    "communication": [
        AffiliateItem(
            title="話し方・伝え方の本",
            description="人間関係がラクになる会話のコツ。",
            url="https://example.com/affiliate/communication-book",
        ),
        AffiliateItem(
            title="オンライン学習講座",
            description="コミュニケーション力を体系的に学べる講座。",
            url="https://example.com/affiliate/course",
        ),
    ],
    # 汎用・セルフケア系（フォールバック）
    "general": [
        AffiliateItem(
            title="毎日のセルフケアグッズ",
            description="自分をいたわる時間をつくるアイテム。",
            url="https://example.com/affiliate/selfcare",
        ),
        AffiliateItem(
            title="話題のベストセラー書籍",
            description="心と暮らしを整えるヒントが詰まった本。",
            url="https://example.com/affiliate/book",
        ),
    ],
}


def get_items(group: str) -> List[AffiliateItem]:
    """グループ名に対応するおすすめ一覧を返す（無ければ汎用にフォールバック）。"""
    return AFFILIATE_GROUPS.get(group) or AFFILIATE_GROUPS["general"]


def render_affiliate_cards(group: str, heading: str = "🎁 あなたへのおすすめ") -> None:
    """結果ページ・トップページ用の横並びカード枠を描画する（高CTR位置向け）。

    Args:
        group: ``AFFILIATE_GROUPS`` のキー。
        heading: 枠の見出し。
    """
    items = get_items(group)
    if not items:
        return

    st.divider()
    st.subheader(heading)
    st.caption(AD_LABEL)

    cols = st.columns(len(items))
    for col, item in zip(cols, items):
        with col:
            with st.container(border=True):
                st.markdown(f"**{item.title}**")
                st.write(item.description)
                st.link_button(item.cta, item.url, use_container_width=True)


def render_affiliate_sidebar(group: str, limit: int = 2) -> None:
    """サイドバー用のコンパクトな枠を描画する（常時表示でCTRを補完）。

    Args:
        group: ``AFFILIATE_GROUPS`` のキー。
        limit: 表示する最大件数。
    """
    items = get_items(group)[:limit]
    if not items:
        return

    with st.sidebar:
        st.divider()
        st.caption(f"{AD_LABEL} ｜ おすすめ")
        for item in items:
            with st.container(border=True):
                st.markdown(f"**{item.title}**")
                st.caption(item.description)
                st.link_button(item.cta, item.url, use_container_width=True)
