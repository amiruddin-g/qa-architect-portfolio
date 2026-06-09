# Allure Reporting

Demonstrates how to produce stakeholder-readable test reports from a pytest suite — reports that communicate test intent, failure context, and business impact without requiring access to CI logs.

## The problem this solves

A passing CI pipeline is not the same as a trustworthy one. Most test output — pytest's terminal output, raw JUnit XML — is written for developers debugging a failure, not for stakeholders deciding whether to ship.

Allure bridges that gap. By annotating tests with feature, story, severity, and step metadata, the report communicates *what was tested and why it matters*, not just *which file failed on which line*.

## Annotation design

Four annotations, each adding a distinct layer of context to the report:

| Annotation | What it communicates |
|---|---|
| `@allure.feature` | Which functional area of the product this test covers |
| `@allure.story` | The specific user scenario being validated |
| `@allure.severity` | Business impact of a failure — CRITICAL, NORMAL, MINOR |
| `@allure.step` | Internal test actions exposed in the report without adding logging code |

The hierarchy in the Behaviors section of the report follows: `Feature → Story → Test`. A stakeholder can navigate directly to "Payment → Refund validation" without reading test code.

## How to run

### Local

```bash
pytest test-tagging/ --alluredir=allure-results
allure serve allure-results
```

This generates raw result files in `allure-results/` and opens the report in your default browser.

### Docker

Make sure Docker Desktop is running, then:

```bash
# Build the image
docker build -f docker-test-env/Dockerfile -t qa-test-tagging:latest .

# Run with volume mount to extract results
docker run --rm -v <your-repo-root>\allure-results:/app/allure-results qa-test-tagging:latest

# Serve the report locally
allure serve allure-results
```

The `--alluredir=allure-results` flag is baked into the Dockerfile. The volume mount extracts results from the container to your local machine so `allure serve` can read them.

## Files

- `test-tagging/tests/test_login.py` — login flow tests with feature, story, severity, and step annotations
- `test-tagging/tests/test_payment.py` — payment flow tests including refund and declined card scenarios
- `test-tagging/tests/test_search.py` — search tests including special character and multi-parameter scenarios
- `docker-test-env/Dockerfile` — container with `--alluredir` baked into CMD

## Tradeoffs

Allure annotations are test-framework-specific. A test annotated with `@allure.feature` is coupled to Allure — switching reporting tools means revisiting every annotation. For a portfolio demonstrating infrastructure decisions, that tradeoff is acceptable. In a production codebase, the annotation overhead should be weighed against the reporting value for your specific stakeholders.

---

*Part of [qa-architect-portfolio](../). Next module: quality gates.*