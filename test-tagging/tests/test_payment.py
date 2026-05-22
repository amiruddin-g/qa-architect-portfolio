import pytest


@pytest.mark.smoke
def test_successful_payment():
    # Smoke check: Standard card payment with valid details
    # verify transaction completes and confirmation is returned.
    pass


@pytest.mark.regression
def test_payment_declined_expired_card():
    # Regression check: Payment declined due to expired card
    # verify graceful failure and clear user messaging.
    pass


@pytest.mark.critical_path
@pytest.mark.slow
def test_successful_refund():
    # Critical path: Full refund on a completed transaction
    # verify funds reversal and updated order status.
    pass
