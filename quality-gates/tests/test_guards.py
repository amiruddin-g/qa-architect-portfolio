from src.guards import has_required_keys, is_above_threshold, is_within_range


def test_is_above_threshold():
    assert is_above_threshold(95, 90) is True
    assert is_above_threshold(80, 90) is False


def test_is_within_range():
    assert is_within_range(50, 0, 100) is True
    assert is_within_range(150, 0, 100) is False


def test_has_required_keys():
    assert has_required_keys({"name": "login", "status": "pass"}, ["name", "status"]) is True
    assert has_required_keys({"name": "login"}, ["name", "status"]) is False