"""src.test_template の共通ロジックに対するテスト。"""
from typing import List

import pytest

from src.test_template import PsychologicalTest, Question, Result


class _DummyTest(PsychologicalTest):
    """テスト用の最小構成の心理テスト。"""

    def get_questions(self) -> List[Question]:
        return [
            Question(text="Q1", options=["a", "b", "c"], scores=[0, 1, 2]),
            Question(text="Q2", options=["a", "b", "c"], scores=[0, 1, 2]),
        ]

    def get_results(self) -> List[Result]:
        return [
            Result(title="低", description="low", score_range=(0, 1)),
            Result(title="中", description="mid", score_range=(2, 3)),
            Result(title="高", description="high", score_range=(4, 4)),
        ]


@pytest.fixture
def dummy() -> _DummyTest:
    return _DummyTest(test_id="dummy", name="ダミー", description="テスト用")


def test_min_and_max_score(dummy: _DummyTest) -> None:
    assert dummy.min_score() == 0
    assert dummy.max_score() == 4


def test_result_for_score_within_range(dummy: _DummyTest) -> None:
    assert dummy.result_for_score(0).title == "低"
    assert dummy.result_for_score(2).title == "中"
    assert dummy.result_for_score(4).title == "高"


def test_result_for_score_out_of_range(dummy: _DummyTest) -> None:
    assert dummy.result_for_score(99) is None


def test_result_contains() -> None:
    result = Result(title="t", description="d", score_range=(2, 5))
    assert result.contains(2)
    assert result.contains(5)
    assert not result.contains(1)
    assert not result.contains(6)
