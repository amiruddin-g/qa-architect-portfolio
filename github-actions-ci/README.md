# GitHub Actions CI

Demonstrates a CI pipeline that builds and runs the containerized test suite on a GitHub-hosted runner — verifying that the Docker image builds cleanly and all tests pass in a completely fresh environment.

## The problem this solves

Local Docker removes "works on my machine" for individual developers. CI removes it for the team. A test suite that only runs on someone's laptop is not a quality signal — it's a personal check. GitHub Actions makes the pipeline the source of truth: the same image, built from scratch on a clean Ubuntu runner, with no dependency on any local setup.

## What the workflow does

Three steps, in order:

1. **Checkout** — clones the repo onto the GitHub-hosted Ubuntu runner via `actions/checkout@v4`
2. **Build** — builds the Docker image from `docker-test-env/Dockerfile` using the repo root as build context
3. **Run** — executes all 9 pytest tests inside the container; a non-zero exit code fails the workflow

The entire run happens on GitHub's infrastructure. Local Docker is never touched.

## Design decisions

**`workflow_dispatch` trigger.** Manual trigger only — intentional for a portfolio. A push or PR trigger would fire on every commit while the module is under active development, generating noise. `workflow_dispatch` keeps the signal clean: the pipeline runs when explicitly invoked, not on every work-in-progress commit.

**No separate test environment setup.** The workflow does not install Python, create a venv, or manage dependencies directly. All of that lives inside the Dockerfile. The CI job is three lines because the container encapsulates the environment — this is the payoff of the `docker-test-env/` module.

**`ubuntu-latest` runner.** GitHub-hosted, no self-hosted runner configuration required. Matches the Linux environment inside the container, so there are no OS-level surprises between the runner and the container.

**Exit code as the quality signal.** `docker run --rm` returns pytest's exit code directly to the runner. If any test fails, the container exits non-zero, the workflow step fails, and the run is marked failed. No parsing, no post-processing — the signal is clean by construction.

## Workflow file

`.github/workflows/ci.yml` — the complete pipeline definition. Three steps, no matrix, no artifacts. Deliberately minimal: the complexity lives in the container, not the workflow.

## How to trigger

Navigate to **Actions → CI → Run workflow** in the GitHub UI.

## Connection to other modules

This pipeline is the integration point for the entire portfolio:
- Builds the image defined in `docker-test-env/`
- Runs the tests and markers defined in `test-tagging/`
- Allure reporting can be extracted via volume mount if added to the run step

---

*Part of [qa-architect-portfolio](../). Previous module: [docker-test-env](../docker-test-env/). Next module: quality-gates.*