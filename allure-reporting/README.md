# Allure Reporting

Allure is a reporting framework built on java. Provides a pre-built structured report of the execution based on the annotations provided in the code.

## Purpose

To provide stakeholder-readable test reports without requiring access to CI logs.

## What This Module Demonstrates

Integration of Allure reporting with various annotations along with docker integration.

## Annotations Used

@allure.feature     - Maps tests to a functional area of the product 
@allure.story       - Maps tests to a specific user scenario within that feature
@allure.severity    - Signals business impact of a failure
@allure.step        - Exposes internal test actions in the report without adding logging code

## How to Run

### Local

Once the allure is installed and all annotations are provided to the test, proceed as follows
1. Run `pytest test-tagging/ --alluredir=allure-results` in the terminal
    This will create an 'allure-results' folder under your project
2. Run `allure serve allure-results` in the terminal.
    This will open the report in your default browser.

### Docker

Note: Make sure Docker Desktop is running in the background before the execution

To integrate with Docker, we have to make few changes before the run,
1. In Dockerfile, add "--alluredir=allure-results" under CMD as below and save
    `CMD ["pytest", "--alluredir=allure-results"]`
2. Then run `docker build -f docker-test-env/Dockerfile -t qa-test-tagging:latest .` in the terminal to build the image. (the dot at the end is must)
3. Finally, run `docker run --rm -v <your-repo-root>\allure-results:/app/allure-results qa-test-tagging:latest` to run it in docker.
    Example : `docker run --rm -v F:\QA_Architect\qa-architect-portfolio\allure-results:/app/allure-results qa-test-tagging:latest`


## Report Structure
Report has 7 sections on the left side 
1. Overview
    This will have over all execution details with pass/fail counts
2. Categories
    Groups failed and broken tests by failure type — distinguishing product defects from test infrastructure issues
3. Suites
    This section will the test suites, since we don't have any specialized suite, it'll only have tests as a section
4. Behaviors
    This section will categorize based on the annotations we have passed which discussed above. Hierarchy of the section is Feature -> Story -> Test
5. Packages
    This section organizes the test by packages. Since we have only one package, we'll see only 'tests' section
6. Graphs
    Visualizes test distribution by severity, status, and duration — useful for identifying flaky or slow tests
7. Timeline
    Show the execution time of each case.