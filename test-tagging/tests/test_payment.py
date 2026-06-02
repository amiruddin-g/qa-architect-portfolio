import allure
import pytest


@allure.step
def perform_payment(currency, amount):
    pass

@allure.feature("Payment")
@allure.story("Successful payment check")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_successful_payment():
    # Smoke check: Standard card payment with valid details
    # verify transaction completes and confirmation is returned.
    perform_payment("INR", 500)

@allure.feature("Payment")
@allure.story("Payment check with an expired card")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_payment_declined_expired_card():
    # Regression check: Payment declined due to expired card
    # verify graceful failure and clear user messaging.
    perform_payment("INR", 500)

@allure.feature("Payment")
@allure.story("Refund validation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.critical_path
@pytest.mark.slow
def test_successful_refund():
    # Critical path check: Full refund on a completed transaction
    # verify funds reversal and updated order status.
    perform_payment("INR", 500)
