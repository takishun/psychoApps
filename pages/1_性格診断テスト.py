"""
性格診断テスト - サンプルページ
テンプレートを使用した実装例
"""
import sys
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from typing import List
import streamlit as st
from src.pages.test_template import (
    PsychologicalTestTemplate,
    Question,
    Result
)


class PersonalityTest(PsychologicalTestTemplate):
    """性格診断テスト"""

    def __init__(self):
        super().__init__(
            test_id="personality_test",
            test_name="性格診断テスト",
            test_description="""
            この性格診断テストは、あなたの基本的な性格傾向を診断します。
            全5問の質問に答えることで、あなたの性格タイプを判定します。
            直感的に、正直に答えてください。
            """
        )

    def get_questions(self) -> List[Question]:
        """質問リストを取得"""
        return [
            Question(
                question_id="q1",
                text="友人との約束がある日、あなたはどう感じますか？",
                options=[
                    "とても楽しみで、ワクワクする",
                    "楽しみだが、少し疲れそう",
                    "できれば家でゆっくりしたい",
                    "正直、面倒に感じる"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q2",
                text="新しいプロジェクトや課題に取り組むとき、あなたは？",
                options=[
                    "すぐに計画を立てて、段階的に進める",
                    "大まかな方向性を決めてから始める",
                    "とりあえず始めてから考える",
                    "締め切り直前に集中して取り組む"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q3",
                text="意思決定をするとき、あなたが重視するのは？",
                options=[
                    "論理的な分析とデータ",
                    "直感と経験",
                    "他人の意見や感情",
                    "その時の気分"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q4",
                text="ストレスを感じたとき、あなたはどう対処しますか？",
                options=[
                    "一人で冷静に考える",
                    "信頼できる人に相談する",
                    "気分転換に外出する",
                    "特に何もせず、時間が解決するのを待つ"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q5",
                text="週末の理想的な過ごし方は？",
                options=[
                    "新しい場所を探索したり、アクティビティを楽しむ",
                    "友人や家族とゆっくり過ごす",
                    "趣味に没頭する",
                    "何も予定を立てず、のんびりする"
                ],
                scores=[3, 2, 1, 0]
            )
        ]

    def get_results(self) -> List[Result]:
        """結果の定義を取得"""
        return [
            Result(
                result_type="highly_active",
                title="🌟 積極的・外向型",
                description="""
                あなたは非常に積極的で、外向的な性格です。
                新しい経験や人との交流を楽しみ、エネルギッシュに行動します。
                計画性があり、目標に向かって着実に進む傾向があります。
                リーダーシップを発揮し、周囲を巻き込む力があります。
                """,
                score_range=(12, 15),
                advice="""
                あなたの行動力は素晴らしい長所ですが、時には立ち止まって
                休息を取ることも大切です。自分のペースを保ちながら、
                周囲の意見にも耳を傾けることで、さらに成長できるでしょう。
                """
            ),
            Result(
                result_type="balanced",
                title="⚖️ バランス型",
                description="""
                あなたは外向性と内向性のバランスが取れた性格です。
                状況に応じて、積極的に行動したり、慎重に考えたりできます。
                柔軟性があり、さまざまな状況に適応できる能力があります。
                人との交流も楽しめますが、一人の時間も大切にします。
                """,
                score_range=(7, 11),
                advice="""
                あなたのバランス感覚は大きな強みです。ただし、時には
                自分の意見をはっきり主張することも大切です。
                自分らしさを大切にしながら、得意な分野を伸ばしていきましょう。
                """
            ),
            Result(
                result_type="introspective",
                title="🌙 内省的・内向型",
                description="""
                あなたは内省的で、じっくり考えるタイプです。
                一人の時間を大切にし、深く物事を考える傾向があります。
                慎重に行動し、自分のペースを保つことを好みます。
                創造的で、独自の視点を持っています。
                """,
                score_range=(0, 6),
                advice="""
                あなたの深い思考力と創造性は貴重な才能です。
                時には殻を破って、新しい経験にチャレンジすることで、
                さらに視野が広がるでしょう。自分のペースを大切にしながら、
                少しずつ快適ゾーンを広げていきましょう。
                """
            )
        ]


def main():
    """メイン関数"""
    # テストインスタンスを作成
    test = PersonalityTest()

    # テストを実行
    test.run()


if __name__ == "__main__":
    main()
