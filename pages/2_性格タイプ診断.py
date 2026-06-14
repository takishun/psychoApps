"""性格タイプ診断 — 内向的〜外向的の傾向をざっくり診断する。"""
import sys
from pathlib import Path
from typing import List

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.test_template import PsychologicalTest, Question, Result  # noqa: E402


class PersonalityTest(PsychologicalTest):
    """エネルギーの向き（内向／外向）を測る簡易タイプ診断。"""

    def get_questions(self) -> List[Question]:
        # スコアが高いほど外向的、低いほど内向的になるよう設計。
        return [
            Question(
                text="休日の過ごし方として理想に近いのは？",
                options=["家でゆっくり一人で過ごす", "気が向けば誰かと会う", "友人や仲間と賑やかに過ごす"],
                scores=[0, 2, 4],
            ),
            Question(
                text="初対面の人が多い場では？",
                options=["緊張して疲れてしまう", "様子を見ながら少しずつ話す", "自分から積極的に話しかける"],
                scores=[0, 2, 4],
            ),
            Question(
                text="考えごとをするとき、あなたは？",
                options=["じっくり一人で考える", "場合によって使い分ける", "誰かに話しながら整理する"],
                scores=[0, 2, 4],
            ),
            Question(
                text="新しいことを始めるとき？",
                options=["慎重に準備してから動く", "ある程度考えてから動く", "まず行動して試していく"],
                scores=[0, 2, 4],
            ),
            Question(
                text="大人数の集まりに誘われたら？",
                options=["できれば遠慮したい", "内容次第で参加する", "楽しみで参加したくなる"],
                scores=[0, 2, 4],
            ),
            Question(
                text="自分の気持ちやエネルギーが回復するのは？",
                options=["一人の静かな時間", "状況による", "人と関わっているとき"],
                scores=[0, 2, 4],
            ),
        ]

    def get_results(self) -> List[Result]:
        return [
            Result(
                title="じっくり型（内向タイプ）",
                description="自分の内面と向き合い、深く考えることが得意なタイプです。"
                "落ち着いた環境で力を発揮します。",
                score_range=(0, 7),
                advice="一人の時間を大切にしつつ、信頼できる相手との"
                "少人数の交流が心地よさにつながります。",
                emoji="🌙",
            ),
            Result(
                title="バランス型（両向タイプ）",
                description="状況に応じて一人の時間も人との交流も楽しめる、"
                "柔軟なバランス型です。",
                score_range=(8, 16),
                advice="場面に合わせて切り替えられるのが強み。"
                "自分が心地よいペースを意識すると疲れにくくなります。",
                emoji="⚖️",
            ),
            Result(
                title="アクティブ型（外向タイプ）",
                description="人との関わりからエネルギーを得る行動派タイプです。"
                "場を盛り上げる力があります。",
                score_range=(17, 24),
                advice="行動力が魅力。ときには立ち止まって"
                "一人で振り返る時間をとると、より深みが増します。",
                emoji="☀️",
            ),
        ]


def main() -> None:
    st.set_page_config(page_title="性格タイプ診断", page_icon="🧭", layout="centered")
    PersonalityTest(
        test_id="personality",
        name="性格タイプ診断",
        description="6つの質問から、あなたのエネルギーの向き（内向／外向）の傾向を診断します。",
        icon="🧭",
    ).run()


if __name__ == "__main__":
    main()
