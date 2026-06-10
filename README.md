# QA Architect Portfolio

Test infrastructure, CI/CD pipelines, and quality engineering work — building toward Principal/Staff QA Engineer roles at product companies.

## About

I'm Amiruddin (Amir) — a QA Automation Architect with 13 years of experience in test automation across Selenium, Java, Python, and pytest. I currently work at [Indium](https://www.indium.tech/), a digital engineering firm with a recognized Quality Engineering practice, where I focus on AI-driven test automation strategy.

My focus is shifting from writing tests to **building the systems that run them** — self-triggering pipelines, parallel execution, release-gating quality checks, and reporting infrastructure that engineering teams actually trust. This repo is where that work lives, in public, as I build it.

## What's in this repo

> This portfolio is actively under construction. Each module is added as I complete it — not as a plan, but as working, runnable code.

| Module | Status | What it demonstrates |
|---|---|---|
| `test-tagging/`       | ✅ Done | pytest markers as multi-dimensional metadata, selective execution via CI marker filters |
| `docker-test-env/` | ✅ Done | Containerized Python+pytest environment, sibling-module composition, deliberate layer caching |
| `github-actions-ci/` | ✅ Done | CI pipeline using GitHub Actions with Docker build and pytest execution |
| `allure-reporting/` | ✅ Done | Allure annotations (feature, story, severity, step), local and Docker-integrated report generation |
| `quality-gates/` | ✅ Done | Coverage threshold enforcement, pytest-cov integration, CI-blocking quality gate |
| `parallel-execution/` | ✅ Done | Worker-based parallelism, execution overhead tradeoffs, shared state isolation pitfalls |

Each module includes runnable code, a focused README explaining the pattern, and notes on tradeoffs I encountered.

## Why this portfolio exists

After 13 years in QA, I've seen the same gap repeatedly: organizations have tests but don't have **test infrastructure**. Tests live in someone's local IDE. CI runs are flaky. Reports get ignored. Releases ship despite red builds because nobody trusts the signal.

The work I want to do — and the work this repo demonstrates — is closing that gap. Pipelines that block releases when they should. Reports that engineers read. Test environments that match production. Quality signals leadership can actually use.

## Tech stack

- **Languages:** Python (primary), Java
- **Test frameworks:** pytest, Selenium
- **CI/CD:** GitHub Actions
- **Containers:** Docker
- **Reporting:** Allure
- **Parallel execution:** pytest-xdist

## Background

13 years in QA and test automation since December 2012. Currently QA Automation Architect at Indium, working on AI-driven test automation strategy. Previously worked across multiple service-domain teams on automation framework design, CI integration, and quality engineering practice.

Actively transitioning to Principal/Staff QA Engineer roles at product companies.

## Contact

- **LinkedIn:** _(coming soon)_
- **Location:** Chennai, India

---

*This README will evolve as the work does.*
