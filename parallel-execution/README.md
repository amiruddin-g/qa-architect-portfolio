# Parallel Execution

Demonstrates parallel test execution using `pytest-xdist`, including when parallelism helps, when it hurts, and a subtle bug class it can hide.

---

## What this module covers

- Running tests in parallel across multiple CPU cores with `-n`
- Measuring the real-world tradeoff between slow and fast tests
- Understanding worker isolation and how it affects shared state
- Identifying tests that are unsafe to parallelize

---

## Concepts

### Sequential vs parallel execution

By default, pytest runs tests one at a time. Each test waits for the previous one to finish. For a suite of 100 tests that each take 1 second, that is 100 seconds of wall-clock time.

`pytest-xdist` spawns multiple worker processes. Each worker picks up a test independently, so tests run concurrently across CPU cores. The same 100 tests might finish in 15–20 seconds on an 8-core machine.

### Worker overhead

Spawning workers has a fixed startup cost — on Windows, roughly 5–6 seconds for 8 workers. For tests that run in milliseconds, this overhead dominates and parallel execution is slower than sequential. Parallelism pays off only when individual tests are slow enough to offset startup cost.

### Worker isolation

Each worker is a separate Python process with its own memory space. Workers do not share variables, global state, or module-level objects. This isolation is what makes parallel execution safe for well-written tests — but it can silently hide bugs in tests that rely on shared state.

---

## Project structure

```
parallel-execution/
├── src/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_fast.py       # 8 instant tests — demonstrates overhead cost
│   ├── test_slow.py       # 8 tests with 1s sleep — demonstrates time savings
│   └── test_shared.py     # 4 tests with shared state — demonstrates hidden bugs
└── requirements.txt
```

---

## Setup

```bash
pip install -r parallel-execution/requirements.txt
```

---

## Running the tests

All commands run from the repo root.

### Slow tests — sequential

```bash
pytest parallel-execution/tests/test_slow.py -v
```

Expected: ~8 seconds. Each test waits for the previous one.

### Slow tests — parallel with 8 workers

```bash
pytest parallel-execution/tests/test_slow.py -v -n 8
```

Expected: ~7 seconds. All 8 tests run simultaneously.

### Fast tests — sequential

```bash
pytest parallel-execution/tests/test_fast.py -v
```

Expected: ~0.1 seconds.

### Fast tests — parallel with 8 workers

```bash
pytest parallel-execution/tests/test_fast.py -v -n 8
```

Expected: ~5–6 seconds. Worker startup cost exceeds the time saved.

### Shared state — sequential

```bash
pytest parallel-execution/tests/test_shared.py -v
```

Expected: 1 passed, 3 failed. The module-level list accumulates across tests. Each test after the first finds the list longer than expected.

### Shared state — parallel

```bash
pytest parallel-execution/tests/test_shared.py -v -n 4
```

Expected: 4 passed. Each worker imports the module fresh, so each test gets its own empty list. The bug is masked.

---

## Results summary

| Test file     | Sequential | Parallel (-n 8)  | Observation                        |
|---------------|------------|------------------|------------------------------------|
| test_slow.py  | ~8.1s      | ~7s              | 4–8x faster — parallelism pays off |
| test_fast.py  | ~0.1s      | ~5.9s            | 60x slower — overhead dominates    |
| test_shared.py| 1P / 3F    | 4P / 0F          | Bug hidden by worker isolation     |

---

## The shared state pitfall

`test_shared.py` intentionally demonstrates a broken pattern. The tests append to a module-level list and assert its length is always 1. Sequentially this fails immediately — the list grows across tests. In parallel it passes — each worker has its own copy of the list.

This is the danger: a developer runs the suite with `-n 4`, sees green, and ships. The bug is real but invisible under parallel execution.

**The fix** is to use a pytest fixture with `function` scope instead of a module-level variable:

```python
import pytest

@pytest.fixture
def fresh_state():
    return []

def test_example(fresh_state):
    fresh_state.append("item")
    assert len(fresh_state) == 1
```

Each test receives a new list from the fixture regardless of execution order or worker count. The test is now safe to parallelize.

---

## When to use parallel execution

| Scenario                              | Recommendation         |
|---------------------------------------|------------------------|
| Tests with I/O, sleep, or API calls   | Use `-n auto`          |
| Pure unit tests under 100ms each      | Sequential is faster   |
| Tests that write to shared files      | Fix isolation first    |
| CI pipeline taking over 10 minutes    | Strong candidate       |

`-n auto` lets xdist choose the worker count based on available CPU cores. It is a safe default for mixed suites.

---

## Key takeaway

Parallel execution is not a free speedup. It requires tests to be stateless and isolated. Enabling it on a suite with shared state can turn failures into false passes — which is worse than a slow pipeline.