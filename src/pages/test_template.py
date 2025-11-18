"""
心理テストページのテンプレートクラス
すべての心理テストページで継承して使用する基底クラス
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import streamlit as st


@dataclass
class Question:
    """質問データクラス"""
    question_id: str
    text: str
    options: List[str]
    scores: List[int]  # 各選択肢のスコア


@dataclass
class Result:
    """結果データクラス"""
    result_type: str
    title: str
    description: str
    score_range: Tuple[int, int]  # (最小スコア, 最大スコア)
    advice: Optional[str] = None


class PsychologicalTestTemplate(ABC):
    """
    心理テストのテンプレート基底クラス

    このクラスを継承して、各心理テストを実装します。
    """

    def __init__(self, test_id: str, test_name: str, test_description: str):
        """
        初期化

        Args:
            test_id: テストの一意ID
            test_name: テスト名
            test_description: テストの説明
        """
        self.test_id = test_id
        self.test_name = test_name
        self.test_description = test_description
        self.session_key = f"{test_id}_state"

    @abstractmethod
    def get_questions(self) -> List[Question]:
        """
        質問リストを取得（サブクラスで実装）

        Returns:
            質問のリスト
        """
        pass

    @abstractmethod
    def get_results(self) -> List[Result]:
        """
        結果の定義を取得（サブクラスで実装）

        Returns:
            結果のリスト
        """
        pass

    def calculate_score(self, answers: Dict[str, int]) -> int:
        """
        スコアを計算

        Args:
            answers: 質問IDと選択した選択肢のインデックスの辞書

        Returns:
            合計スコア
        """
        questions = self.get_questions()
        total_score = 0

        for question in questions:
            if question.question_id in answers:
                choice_index = answers[question.question_id]
                if 0 <= choice_index < len(question.scores):
                    total_score += question.scores[choice_index]

        return total_score

    def get_result_by_score(self, score: int) -> Optional[Result]:
        """
        スコアに基づいて結果を取得

        Args:
            score: 合計スコア

        Returns:
            該当する結果
        """
        results = self.get_results()

        for result in results:
            min_score, max_score = result.score_range
            if min_score <= score <= max_score:
                return result

        return None

    def initialize_session_state(self) -> None:
        """セッション状態を初期化"""
        if self.session_key not in st.session_state:
            st.session_state[self.session_key] = {
                'current_question': 0,
                'answers': {},
                'completed': False,
                'score': 0,
                'result': None
            }

    def render_header(self) -> None:
        """ヘッダーを描画"""
        st.title(f"🧠 {self.test_name}")
        st.markdown(self.test_description)
        st.divider()

    def render_progress(self, current: int, total: int) -> None:
        """
        進捗バーを描画

        Args:
            current: 現在の質問番号
            total: 総質問数
        """
        progress = current / total
        st.progress(progress)
        st.caption(f"進捗: {current} / {total} 問")

    def render_question(self, question: Question, question_num: int) -> None:
        """
        質問を描画

        Args:
            question: 質問オブジェクト
            question_num: 質問番号（表示用）
        """
        st.subheader(f"質問 {question_num}")
        st.markdown(f"**{question.text}**")
        st.write("")  # スペース

        # ラジオボタンで選択肢を表示
        answer = st.radio(
            "選択してください:",
            options=range(len(question.options)),
            format_func=lambda x: question.options[x],
            key=f"{self.test_id}_{question.question_id}_radio"
        )

        return answer

    def render_result(self, result: Result, score: int) -> None:
        """
        結果を描画

        Args:
            result: 結果オブジェクト
            score: 合計スコア
        """
        st.success("テスト完了！")
        st.balloons()

        st.header("📊 あなたの結果")

        # 結果タイプ
        st.subheader(result.title)
        st.metric(label="スコア", value=f"{score} 点")

        st.divider()

        # 説明
        st.markdown("### 📝 説明")
        st.info(result.description)

        # アドバイス
        if result.advice:
            st.markdown("### 💡 アドバイス")
            st.warning(result.advice)

    def render_restart_button(self) -> None:
        """再テストボタンを描画"""
        st.divider()
        if st.button("🔄 もう一度テストする", use_container_width=True):
            # セッション状態をリセット
            st.session_state[self.session_key] = {
                'current_question': 0,
                'answers': {},
                'completed': False,
                'score': 0,
                'result': None
            }
            st.rerun()

    def run(self) -> None:
        """
        テストを実行（メインロジック）
        """
        # セッション状態を初期化
        self.initialize_session_state()

        # ヘッダーを描画
        self.render_header()

        # 現在の状態を取得
        state = st.session_state[self.session_key]
        questions = self.get_questions()

        # テスト完了済みの場合、結果を表示
        if state['completed']:
            self.render_result(state['result'], state['score'])
            self.render_restart_button()
            return

        # 進捗を表示
        current_q = state['current_question']
        self.render_progress(current_q + 1, len(questions))

        # 現在の質問を表示
        if current_q < len(questions):
            question = questions[current_q]
            answer = self.render_question(question, current_q + 1)

            # 次へボタン
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("次へ ➡️", use_container_width=True, type="primary"):
                    # 回答を保存
                    state['answers'][question.question_id] = answer
                    state['current_question'] += 1

                    # 最後の質問の場合、結果を計算
                    if state['current_question'] >= len(questions):
                        score = self.calculate_score(state['answers'])
                        result = self.get_result_by_score(score)
                        state['score'] = score
                        state['result'] = result
                        state['completed'] = True

                    st.rerun()
