"""src.affiliate のロジックに対するテスト。"""
from src.affiliate import AFFILIATE_SNIPPETS, get_snippet


def test_expected_groups_exist() -> None:
    for key in ("stress_relief", "self_growth", "communication", "general"):
        assert key in AFFILIATE_SNIPPETS


def test_get_snippet_known_group() -> None:
    assert get_snippet("general") == AFFILIATE_SNIPPETS["general"]


def test_get_snippet_unknown_group_falls_back_to_general() -> None:
    assert get_snippet("does-not-exist") == AFFILIATE_SNIPPETS["general"]
