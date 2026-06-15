"""
心理テストの共通テンプレート

各心理テストはこのモジュールの ``PsychologicalTest`` を継承し、
質問リスト (``get_questions``) と結果定義 (``get_results``) を実装するだけで、
進捗表示・スコア計算・結果表示までを共通ロジックで実行できる。
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import streamlit as st

from src.affiliate import render_affiliate_cards, render_affiliate_sidebar


# 結果が医療行為ではないことを示す共通の免責文
DISCLAIMER = (
    "このテストは自己理解を深めるための簡易的なものであり、"
    "医学的・心理学的な診断ではありません。気になる症状がある場合は"
    "専門の医療機関にご相談ください。"
)


@dataclass
class Question:
    """1問の質問データ。"""

    text: str
    options: List[str]
    scores: List[int]  # options と同じ並びで、各選択肢に対応するスコア


@dataclass
class Result:
    """スコア範囲に対応する結果データ。"""

    title: str
    description: str
    score_range: Tuple[int, int]  # (最小スコア, 最大スコア) いずれも含む
    advice: Optional[str] = None
    emoji: str = "✨"
    affiliate_group: Optional[str] = None  # 結果に連動したおすすめ枠のグループ名

    def contains(self, score: int) -> bool:
        """``score`` がこの結果の範囲に含まれるか判定する。"""
        low, high = self.score_range
        return low <= score <= high


@dataclass
class PsychologicalTest(ABC):
    """心理テストの基底クラス。

    Attributes:
        test_id: テストを一意に識別するID（セッションキーに使用）。
        name: テスト名。
        description: テストの概要説明。
        icon: トップページや見出しで使う絵文字。
    """

    test_id: str
    name: str
    description: str
    icon: str = "🧠"
    affiliate_group: str = "general"  # 結果に個別指定が無い場合に使う既定のおすすめ枠
    _state_key: str = field(init=False)

    def __post_init__(self) -> None:
        self._state_key = f"{self.test_id}_state"

    # --- サブクラスで実装する部分 ---------------------------------------
    @abstractmethod
    def get_questions(self) -> List[Question]:
        """質問のリストを返す。"""

    @abstractmethod
    def get_results(self) -> List[Result]:
        """スコア範囲ごとの結果定義を返す。"""

    # --- スコア計算 ------------------------------------------------------
    def max_score(self) -> int:
        """理論上の最大スコアを返す。"""
        return sum(max(q.scores) for q in self.get_questions())

    def min_score(self) -> int:
        """理論上の最小スコアを返す。"""
        return sum(min(q.scores) for q in self.get_questions())

    def result_for_score(self, score: int) -> Optional[Result]:
        """スコアに該当する結果を返す。該当なしなら ``None``。"""
        for result in self.get_results():
            if result.contains(score):
                return result
        return None

    # --- セッション状態 --------------------------------------------------
    def _default_state(self) -> Dict:
        return {"current": 0, "answers": {}, "completed": False, "score": 0}

    def _init_state(self) -> None:
        if self._state_key not in st.session_state:
            st.session_state[self._state_key] = self._default_state()

    def _reset_state(self) -> None:
        st.session_state[self._state_key] = self._default_state()

    # --- 描画 ------------------------------------------------------------
    def _render_header(self) -> None:
        st.title(f"{self.icon} {self.name}")
        st.write(self.description)
        st.caption(DISCLAIMER)
        st.divider()

    def _render_question(self, question: Question, index: int, total: int) -> None:
        st.progress((index) / total)
        st.caption(f"質問 {index + 1} / {total}")
        st.subheader(question.text)

        answer = st.radio(
            "もっとも近いものを選んでください",
            options=range(len(question.options)),
            format_func=lambda i: question.options[i],
            key=f"{self.test_id}_q{index}_radio",
        )

        col_back, col_spacer, col_next = st.columns([1, 2, 1])
        with col_back:
            if index > 0 and st.button("⬅️ 戻る", use_container_width=True):
                st.session_state[self._state_key]["current"] -= 1
                st.rerun()

        with col_next:
            label = "結果を見る 🎉" if index == total - 1 else "次へ ➡️"
            if st.button(label, use_container_width=True, type="primary"):
                self._record_answer(index, question, answer, total)
                st.rerun()

    def _record_answer(
        self, index: int, question: Question, answer: int, total: int
    ) -> None:
        state = st.session_state[self._state_key]
        state["answers"][index] = question.scores[answer]
        state["current"] = index + 1
        if state["current"] >= total:
            state["score"] = sum(state["answers"].values())
            state["completed"] = True

    def _render_result(self, score: int) -> None:
        st.balloons()
        st.success("診断が完了しました！")

        result = self.result_for_score(score)
        low, high = self.min_score(), self.max_score()
        ratio = (score - low) / (high - low) if high > low else 0.0

        if result is not None:
            st.header(f"{result.emoji} {result.title}")
        st.metric("あなたのスコア", f"{score} 点", help=f"範囲: {low}〜{high} 点")
        st.progress(ratio)

        if result is not None:
            st.write(result.description)
            if result.advice:
                st.info(f"💡 **アドバイス**\n\n{result.advice}")
        else:
            st.warning("該当する結果が見つかりませんでした。")

        # 結果直下は最も関心が高まる位置。結果に連動したおすすめ枠を表示する。
        group = (
            result.affiliate_group
            if result is not None and result.affiliate_group
            else self.affiliate_group
        )
        render_affiliate_cards(group)

        st.caption(DISCLAIMER)
        st.divider()
        if st.button("🔄 もう一度診断する", use_container_width=True):
            self._reset_state()
            st.rerun()

    # --- エントリーポイント ---------------------------------------------
    def run(self) -> None:
        """テストを実行する。Streamlit ページから呼び出す。"""
        self._init_state()
        self._render_header()

        # サイドバーは常時表示されるためCTRの補完に有効。
        render_affiliate_sidebar(self.affiliate_group)

        state = st.session_state[self._state_key]
        questions = self.get_questions()

        if state["completed"]:
            self._render_result(state["score"])
            return

        current = state["current"]
        self._render_question(questions[current], current, len(questions))
