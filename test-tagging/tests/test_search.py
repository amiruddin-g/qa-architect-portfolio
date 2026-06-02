import allure
import pytest


@allure.step
def perform_search(*search_terms):
    pass

@allure.feature("Search")
@allure.story("Successful search check")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_successful_search():
    # Smoke check: A successful search with valid details/criteria
    # verify results are visible for the search.
    perform_search("ABC")

@allure.feature("Search")
@allure.story("Negative validation with special characters")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_invalid_search_with_special_characters():
    # Regression check: search validation with special characters
    # verify graceful failure and clear user messaging.
    perform_search("@B$")

@allure.feature("Search")
@allure.story("Multi parameter Search validation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.slow
def test_multi_parameter_search():
    # Regression check: Search with multiple parameters for a combined result
    # verify the results include all search criteria.
    perform_search("ABC",123)
