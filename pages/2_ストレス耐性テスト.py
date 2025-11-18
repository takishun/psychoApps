"""
ストレス耐性テスト - サンプルページ
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


class StressResilienceTest(PsychologicalTestTemplate):
    """ストレス耐性テスト"""

    def __init__(self):
        super().__init__(
            test_id="stress_resilience_test",
            test_name="ストレス耐性テスト",
            test_description="""
            このテストは、あなたのストレス耐性を診断します。
            全5問の質問に答えることで、ストレスへの対処能力を判定します。
            最近の状況を思い浮かべながら、正直に答えてください。
            """
        )

    def get_questions(self) -> List[Question]:
        """質問リストを取得"""
        return [
            Question(
                question_id="q1",
                text="予期せぬ問題が発生したとき、あなたの反応は？",
                options=[
                    "冷静に状況を分析し、解決策を考える",
                    "少し動揺するが、すぐに立て直せる",
                    "かなり不安になり、混乱する",
                    "パニックになり、どうすればいいか分からなくなる"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q2",
                text="複数の締め切りが重なったとき、あなたは？",
                options=[
                    "優先順位をつけて、計画的に進める",
                    "多少焦るが、なんとか乗り切れる",
                    "非常にストレスを感じ、効率が落ちる",
                    "圧倒されて、何も手につかなくなる"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q3",
                text="失敗やミスをしたとき、どう感じますか？",
                options=[
                    "学びの機会と捉え、次に活かす",
                    "少し落ち込むが、すぐに気持ちを切り替える",
                    "しばらく引きずってしまう",
                    "自分を強く責め、長期間落ち込む"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q4",
                text="批判やネガティブな意見を受けたとき、あなたは？",
                options=[
                    "建設的な意見として受け止め、改善に活かす",
                    "最初は気になるが、客観的に考えられる",
                    "深く傷つき、気分が沈む",
                    "非常に動揺し、自信を失う"
                ],
                scores=[3, 2, 1, 0]
            ),
            Question(
                question_id="q5",
                text="日常的なストレスにどう対処していますか？",
                options=[
                    "定期的な運動やリラックス法を実践している",
                    "時々気分転換をする程度",
                    "特に対処法はなく、我慢している",
                    "ストレスが蓄積し、よく体調を崩す"
                ],
                scores=[3, 2, 1, 0]
            )
        ]

    def get_results(self) -> List[Result]:
        """結果の定義を取得"""
        return [
            Result(
                result_type="high_resilience",
                title="💪 高いストレス耐性",
                description="""
                あなたは非常に高いストレス耐性を持っています。
                困難な状況でも冷静に対処でき、プレッシャーの中でも
                良いパフォーマンスを発揮できます。
                ストレス管理のスキルが身についており、
                失敗や批判を成長の機会として捉えられます。
                """,
                score_range=(12, 15),
                advice="""
                あなたのストレス耐性は素晴らしいですが、
                完璧を求めすぎないことも大切です。
                時には自分の限界を認め、適切に休息を取りましょう。
                また、ストレスに弱い人への理解と配慮も忘れずに。
                """
            ),
            Result(
                result_type="moderate_resilience",
                title="🌱 中程度のストレス耐性",
                description="""
                あなたは平均的なストレス耐性を持っています。
                多くの状況では適切に対処できますが、
                時々ストレスに圧倒されることがあります。
                ストレス管理の基本は身についていますが、
                さらに改善の余地があります。
                """,
                score_range=(7, 11),
                advice="""
                ストレス管理スキルを向上させる良い機会です。
                定期的な運動、十分な睡眠、リラックス法の実践など、
                セルフケアの習慣を取り入れましょう。
                また、信頼できる人に相談することも効果的です。
                小さな成功体験を積み重ねることで、自信がつきます。
                """
            ),
            Result(
                result_type="low_resilience",
                title="🆘 ストレス耐性が低い",
                description="""
                現在、ストレスへの対処に困難を感じているようです。
                日常的なストレスでも大きな負担に感じられ、
                心身ともに疲弊している可能性があります。
                ストレス管理のスキルを学び、実践することが重要です。
                """,
                score_range=(0, 6),
                advice="""
                まずは、自分の状態を認識することが第一歩です。
                専門家（カウンセラーや医師）に相談することを
                強くお勧めします。小さなストレス管理法から始めましょう：
                - 深呼吸やマインドフルネス
                - 規則正しい生活リズム
                - 軽い運動（散歩など）
                - 十分な睡眠
                焦らず、少しずつ改善していきましょう。
                """
            )
        ]


def main():
    """メイン関数"""
    # テストインスタンスを作成
    test = StressResilienceTest()

    # テストを実行
    test.run()


if __name__ == "__main__":
    main()
