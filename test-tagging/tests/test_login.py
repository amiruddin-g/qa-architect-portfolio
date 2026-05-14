import pytest

@pytest.mark.smoke
def test_valid_login_smoke():
    pass

@pytest.mark.regression
def test_login_wth_special_characters():
    pass

@pytest.mark.critical_path
@pytest.mark.slow
def test_login_after_password_reset():
    pass