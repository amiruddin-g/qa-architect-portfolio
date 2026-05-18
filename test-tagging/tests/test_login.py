import pytest

@pytest.mark.smoke
def test_valid_login_smoke():
    # Smoke check: valid credentials log in successfully and a session is established
    pass

@pytest.mark.regression
def test_login_with_special_characters():
    # Regression check: login validation with special characters in credentials
    pass

@pytest.mark.critical_path
@pytest.mark.slow
def test_login_after_password_reset():
    # Critical path: login works correctly after a password reset flow
    pass