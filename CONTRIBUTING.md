# Contributing to Respectful AI & High-Signal Standard (RAHSPS)

We welcome contributions from engineers, researchers, and systems architects who value cognitive hygiene and deterministic AI collaboration.

---

## 1. The Core Philosophy

In this repository, we practice what we preach:
1. **Respectful Communication:** All GitHub Issues, Pull Requests, and discussions MUST adhere to the High-Signal standard.
2. **Zero Toxic Slang:** Whining, unconstructive complaints, or low-signal one-liners will be closed by automated gatekeepers.
3. **Automated Verification:** Every PR must pass the `verify_harness.py` audit and `unittest` suite before merge.

---

## 2. Contribution Workflow

1. **Fork and Clone the Repository:**
   ```bash
   git clone https://github.com/respectful-ai/standard.git
   cd standard
   ```

2. **Install Local Tooling:**
   ```bash
   pip install -e .
   ```

3. **Verify Existing Tests:**
   ```bash
   python3 -m unittest discover tests
   python3 verify_harness.py
   ```

4. **Making Changes:**
   - If adding new prompt examples, follow the exact structure of `examples/before_after.md`.
   - If modifying `respect_lint.py`, add corresponding unit tests in `tests/test_respect_lint.py`.
   - Ensure `bin/respect-lint.py` passes on all sample prompts.

5. **Submitting a Pull Request:**
   - Use the provided Pull Request template ([`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md)).
   - Include the output of `python3 verify_harness.py` in your PR description.

Thank you for elevating software engineering culture!
