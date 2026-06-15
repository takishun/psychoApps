"""ストレス度チェック — 最近のストレスの溜まり具合をセルフチェックする。"""
import sys
from pathlib import Path
from typing import List

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.test_template import PsychologicalTest, Question, Result  # noqa: E402


# 各設問は「あてはまらない(0)」〜「とてもあてはまる(3)」の4段階。
_FREQUENCY_OPTIONS = ["あてはまらない", "ややあてはまる", "あてはまる", "とてもあてはまる"]
_FREQUENCY_SCORES = [0, 1, 2, 3]


class StressTest(PsychologicalTest):
    """日常のストレスサインを問う簡易チェック。"""

    def get_questions(self) -> List[Question]:
        statements = [
            "最近、よく眠れない・寝ても疲れが取れない",
            "些細なことでイライラしてしまう",
            "気分が落ち込んだり、やる気が出ないことが多い",
            "頭痛・肩こり・胃の不調など体の不調を感じる",
            "やるべきことに集中できないと感じる",
            "誰かと話したり外出したりするのが億劫だ",
            "食欲が普段と変わった（増えた・減った）",
            "将来や仕事のことを考えると不安になる",
        ]
        return [
            Question(text=s, options=_FREQUENCY_OPTIONS, scores=_FREQUENCY_SCORES)
            for s in statements
        ]

    def get_results(self) -> List[Result]:
        return [
            Result(
                title="ストレスは穏やかな状態です",
                description="今のところ大きなストレスサインは見られません。"
                "良いコンディションを保てています。",
                score_range=(0, 6),
                advice="今の生活リズムや息抜きの習慣を大切に続けていきましょう。",
                emoji="🌱",
                affiliate_group="general",
            ),
            Result(
                title="ややストレスが溜まり気味です",
                description="いくつかのストレスサインが出はじめています。"
                "無理を続けると負担が大きくなるかもしれません。",
                score_range=(7, 14),
                advice="意識して休息をとり、好きなことに時間を使ってみましょう。"
                "睡眠時間の確保も効果的です。",
                emoji="⛅",
                affiliate_group="stress_relief",
            ),
            Result(
                title="ストレスがかなり溜まっています",
                description="心身ともに負担が大きい状態のようです。"
                "セルフケアだけで抱え込まないことが大切です。",
                score_range=(15, 24),
                advice="信頼できる人に気持ちを話したり、必要に応じて"
                "専門家に相談することも検討してみてください。",
                emoji="🌧️",
                affiliate_group="stress_relief",
            ),
        ]


def main() -> None:
    st.set_page_config(page_title="ストレス度チェック", page_icon="🌤️", layout="centered")
    StressTest(
        test_id="stress",
        name="ストレス度チェック",
        description="最近2週間のあなたの状態について、8つの質問に答えてください。",
        icon="🌤️",
        affiliate_group="stress_relief",
    ).run()


if __name__ == "__main__":
    main()
