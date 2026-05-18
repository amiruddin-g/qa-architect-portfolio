import pytest

@pytest.mark.smoke
def test_successful_payment():
    pass

@pytest.mark.regression
def test_failed_payment():
    pass

@pytest.mark.critical_path
@pytest.mark.slow
def test_successful_refund():
    pass