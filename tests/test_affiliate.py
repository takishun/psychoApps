"""src.affiliate のロジックに対するテスト。"""
from src.affiliate import AFFILIATE_GROUPS, AffiliateItem, get_items


def test_get_items_known_group() -> None:
    items = get_items("stress_relief")
    assert items is AFFILIATE_GROUPS["stress_relief"]
    assert all(isinstance(i, AffiliateItem) for i in items)


def test_get_items_unknown_group_falls_back_to_general() -> None:
    assert get_items("does-not-exist") is AFFILIATE_GROUPS["general"]


def test_all_items_have_url_and_cta() -> None:
    for group, items in AFFILIATE_GROUPS.items():
        assert items, f"group '{group}' must not be empty"
        for item in items:
            assert item.url.startswith("http")
            assert item.cta
