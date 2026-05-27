# Docker Test Environment

Containerized test execution for reproducible test runs — same image locally, in CI, and across any host OS.

## What this module demonstrates

A minimal, production-shaped Dockerfile that packages the [`test-tagging/`](../test-tagging/) module into a reproducible test environment. The same 9-test suite that runs locally on Python 3.13 also runs identically inside a Linux container, with no environment-specific configuration.

This is the foundation pattern that everything downstream — CI pipelines, parallel execution, cloud-hosted runners — depends on.

## Why this matters

"Works on my machine" is the oldest defect class in software, and it shows up most aggressively in test infrastructure. Tests that pass locally on a developer's laptop fail in CI because of:

- Python version differences
- Missing system libraries
- OS-specific path handling
- Implicit environment variables

The Dockerfile here eliminates that variance. Whatever host you build on — Windows, macOS, Linux — the resulting image runs the same Linux environment with the same Python, the same dependencies, and the same test code. The container is the unit of reproducibility.

## How to build and run

From the **repo root** (not from this folder):

```bash
# Build the image
docker build -f docker-test-env/Dockerfile -t qa-test-tagging:latest .

# Run all tests
docker run --rm qa-test-tagging:latest

# Run with marker filtering — same selection patterns as local
docker run --rm qa-test-tagging:latest pytest -m smoke
docker run --rm qa-test-tagging:latest pytest -m "not slow"
```

The trailing `.` is the build context — the repo root, so the Dockerfile can reference `test-tagging/` as a sibling module.

## Design choices

**Build context is the repo root, not this folder.** This lets the Dockerfile reference `test-tagging/` directly via `COPY test-tagging/...` instead of duplicating test code or using brittle `../` paths. Modules compose; they don't duplicate.

**`python:3.13-slim` base image.** Matches the local development Python version (3.13.7), keeping behaviour consistent between host and container. `-slim` keeps the image around 200MB — small enough for fast CI pulls, large enough to include real Python tooling.

**Layer ordering is deliberate.** `requirements.txt` is copied and `pip install`ed *before* the test code is copied. This lets Docker cache the (slow) dependency installation layer across rebuilds — changing a test file does not trigger a fresh pip install. A small detail with a large impact on CI build times.

**`--no-cache-dir` on pip.** Drops pip's download cache from the final image, keeping the image lean. Small but standard.

**`CMD ["pytest"]` in array form.** The JSON array form (not the shell form) ensures the container handles signals correctly — `Ctrl+C` propagates cleanly to pytest, exit codes are preserved, and the container terminates on the actual test process rather than a wrapping shell.

## What's next

This image is the foundation for the upcoming GitHub Actions CI module — the CI pipeline will build this exact Dockerfile and run the container as the test job, ensuring local and CI environments are identical by construction.

---

*Part of [qa-architect-portfolio](../). Previous module: [test-tagging](../test-tagging/). Next module: github-actions-ci.*