import allure
import pytest


@allure.step
def perform_login(username, password):
    pass


@allure.feature("Authentication")
@allure.story("Login check with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_valid_login_smoke():
    # Smoke check: valid credentials log in successfully and a session is established
    perform_login("user", "pass")


@allure.feature("Authentication")
@allure.story("Login check with special characters")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_login_with_special_characters():
    # Regression check: login validation with special characters in credentials
    perform_login("user", "pass")


@allure.feature("Authentication")
@allure.story("Login check after a password reset")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical_path
@pytest.mark.slow
def test_login_after_password_reset():
    # Critical path check: login works correctly after a password reset flow
    perform_login("user", "pass")


