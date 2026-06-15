"""コミュニケーションタイプ診断 — 対人での関わり方の傾向を診断する。"""
import sys
from pathlib import Path
from typing import List

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.test_template import PsychologicalTest, Question, Result  # noqa: E402


class CommunicationTest(PsychologicalTest):
    """主張と協調のバランスから関わり方の傾向を見る診断。"""

    def get_questions(self) -> List[Question]:
        # スコアが高いほど主張・主導が強く、低いほど協調・傾聴が強い。
        return [
            Question(
                text="グループで物事を決めるとき、あなたは？",
                options=["みんなの意見に合わせる", "意見を聞きつつ調整する", "自分の意見を提案して引っ張る"],
                scores=[0, 2, 4],
            ),
            Question(
                text="意見が対立したとき？",
                options=["相手を立てて譲ることが多い", "落としどころを探す", "納得いくまで主張する"],
                scores=[0, 2, 4],
            ),
            Question(
                text="会話の中での自分の役割は？",
                options=["聞き役になることが多い", "話す・聞くは半々", "話題を引っ張ることが多い"],
                scores=[0, 2, 4],
            ),
            Question(
                text="頼みごとをするとき？",
                options=["遠慮してためらいがち", "様子を見て切り出す", "はっきりとお願いできる"],
                scores=[0, 2, 4],
            ),
            Question(
                text="新しいチームに入ったら？",
                options=["まわりに合わせて溶け込む", "少しずつ関係を築く", "早めに自分の存在を示す"],
                scores=[0, 2, 4],
            ),
            Question(
                text="相手の感情への向き合い方は？",
                options=["相手の気持ちを最優先する", "気持ちと事実の両方を見る", "まず事実や結論を重視する"],
                scores=[0, 2, 4],
            ),
        ]

    def get_results(self) -> List[Result]:
        return [
            Result(
                title="サポータータイプ",
                description="相手の気持ちに寄り添い、場の調和を大切にする"
                "聞き上手なタイプです。安心感を与えます。",
                score_range=(0, 7),
                advice="周囲を支える力が魅力。ときには自分の希望も"
                "言葉にすると、より良い関係が築けます。",
                emoji="🤝",
            ),
            Result(
                title="コーディネータータイプ",
                description="主張と傾聴のバランスが取れた調整役タイプです。"
                "相手と自分の双方を尊重できます。",
                score_range=(8, 16),
                advice="バランス感覚が強み。意見が割れたときの"
                "橋渡し役として頼られる存在です。",
                emoji="🎯",
            ),
            Result(
                title="リーダータイプ",
                description="自分の考えをはっきり伝え、場を主導する行動派タイプです。"
                "決断力と推進力があります。",
                score_range=(17, 24),
                advice="引っ張る力が魅力。相手の意見に耳を傾ける"
                "余白をつくると、信頼がさらに深まります。",
                emoji="🚀",
            ),
        ]


def main() -> None:
    st.set_page_config(page_title="コミュニケーションタイプ診断", page_icon="💬", layout="centered")
    CommunicationTest(
        test_id="communication",
        name="コミュニケーションタイプ診断",
        description="6つの質問から、対人関係での関わり方の傾向を診断します。",
        icon="💬",
        affiliate_group="communication",
    ).run()


if __name__ == "__main__":
    main()
