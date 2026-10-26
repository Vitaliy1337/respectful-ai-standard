## Pull Request: High-Signal Engineering Contribution

### 1. Respected Colleague Greeting & Objective
<!-- Example: Respected Reviewer, this PR introduces a new resilient Kafka consumer case study... -->
**Respected Reviewers,** [Summarize your technical objective cleanly here]

---

### 2. Context & Affected Modules
- **Files Modified / Added:**
  - `...`
- **Area of Impact:** [Core Linter / Documentation / Agent Rulebooks / Web Playground]

---

### 3. Invariants & Safety Verification
- [ ] Preserved backward compatibility of all prompt templates.
- [ ] No unformatted raw logs or forbidden placeholder stubs introduced.
- [ ] Added or updated unit tests in `tests/test_respect_lint.py` (if modifying linter).

---

### 4. Verification Evidence
Please paste the output of the automated quality harness:
```bash
python3 verify_harness.py
python3 -m unittest discover tests
```
- [ ] `verify_harness.py` exited with code 0 (100% PASS).
- [ ] All unit tests pass cleanly.
