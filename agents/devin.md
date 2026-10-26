# Devin Autonomous Engineer Task Specification — RAHSPS Protocol

This document defines how autonomous engineering agent **Devin** (Cognition AI) must be briefed and governed under the **Respectful AI & High-Signal Prompting Standard**.

---

## 1. Task Intake Protocol

When assigning an autonomous issue or epic to Devin:
1. **Cognitive Anchor Header:** Begin the prompt with `Respected Agent Devin, [high-level objective]`.
2. **Context Block:** Explicitly specify the runtime environment, dependencies, and entrypoint files.
3. **Invariants Block:** Detail what MUST NOT be broken (e.g. database migration compatibility, API schema stability).
4. **Verification Harness:** Explicit command to validate task completion (e.g. `python3 verify_harness.py && pytest`).

---

## 2. Standard Issue Template for Devin

```markdown
Respected Agent Devin, please design and implement the [Feature/Fix Name].

### 1. Technical Context
- Language/Stack: Python 3.12 / TypeScript 5.4 / Docker
- Target Files: `src/core/router.py`, `tests/test_router.py`

### 2. Architectural Invariants
- Maintain backward compatibility with API v1 clients.
- Handle connection pool exhaustion with exponential backoff and jitter.

### 3. Verification & Acceptance
- Run `pytest -v tests/` with zero failures.
- Run `python3 verify_harness.py` ensuring all quality gates pass.
```
