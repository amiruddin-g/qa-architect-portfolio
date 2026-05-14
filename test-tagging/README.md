# Test Tagging with pytest Markers

Demonstrates how to organize a test suite for selective execution at scale, using pytest markers as **multi-dimensional metadata** — not single-category labels.

## The problem this solves

In any real codebase with hundreds or thousands of tests, you can't run all of them on every commit. The suite becomes the bottleneck. Teams start ignoring red builds. Releases ship anyway.

The standard fix is "tagging tests" — but most teams tag along a single axis (e.g. "test type") and end up unable to express common selections like *"run everything critical that's also fast enough for PR builds."*

This module demonstrates the alternative: tagging tests along **independent axes**, so test selection becomes a query rather than a category lookup.

## Marker design

Four markers, each defined by a different axis:

| Marker | Axis | Meaning |
|---|---|---|
| `smoke` | Frequency | Runs on every PR. Must complete in seconds. |
| `regression` | Coverage | Full suite, runs nightly or on release branches. |
| `critical_path` | Business impact | Failure blocks release, regardless of speed. |
| `slow` | Resource cost | Excluded from PR builds; runs in nightly/full pipelines. |

Because the axes are independent, a single test can carry multiple markers. For example, a test that exercises post-password-reset login flow is both `critical_path` (blocks release if broken) *and* `slow` (involves email/token timing). The CI config decides which combination to run when.

## How to run

```bash
# All tests
pytest

# PR pipeline: everything except slow tests
pytest -m "not slow"

# Smoke check only
pytest -m smoke

# Release gate: anything critical, regardless of speed
pytest -m critical_path

# Combinations
pytest -m "smoke or critical_path"
pytest -m "regression and not slow"
```

## Files

- `tests/test_login.py` — login flow tests demonstrating marker stacking
- `tests/test_payment.py` — _(coming next)_ payment flow tests
- `tests/test_search.py` — _(coming next)_ search functionality tests
- `pytest.ini` — marker registration (prevents silent typos in marker names)

## Why marker registration matters

The `pytest.ini` file declares each marker name explicitly. Without this, `@pytest.mark.smoek` (typo) silently creates a *new* marker called `smoek` that no CI job ever runs — a classic silent failure. With registered markers and `--strict-markers` (planned), pytest hard-fails on unknown markers, surfacing the typo immediately.

This is a recurring pattern in test infrastructure: catch silent failures early. Most production issues in test suites aren't dramatic — they're quiet drift where the right tests stopped running and nobody noticed.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
pytest
```

---

*Part of [qa-architect-portfolio](../). Next module: containerized test environments.*