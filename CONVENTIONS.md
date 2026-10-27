# CONVENTIONS.md — Engineering Etiquette & Invariants for Aider

This project adheres to the **Respectful AI & High-Signal Prompting Standard (RAHSPS)**.

### Project Language Policy (MANDATORY INVARIANT):
**All code comments, docstrings, git commit messages, PR descriptions, and architectural documentation in this repository must strictly be written in English.**

## 1. Respect & Signal Gate
- All interactions in Aider should be framed with professional clarity and cognitive respect.
- Address the assistant with cognitive anchors: `"Respected Agent..."` or `"Colleague..."`.
- Low-signal prompts (*"fix this fast"*, *"make it work"*) are rejected; specify exact files, constraints, and tests.

## 2. Invariants for Edits
- Write all code comments, docstrings, and commits in English.
- Preserve all existing tests, docstrings, and architectural contracts.
- No temporary placeholders (unwritten stubs, pass, placeholder comments) in production code.
- Run `python3 verify_harness.py` before completing any git operation.
