#!/usr/bin/env python3
"""
verify_harness.py — Automated Quality & Integrity Harness for
«Respectful AI & High-Signal Prompting Standard» (RAHSPS) repository.

Verifies:
1. Presence and integrity of all 16+ core architectural files.
2. Minimum repository total word count >= 15,000 words.
3. Absence of forbidden placeholders, TODOs, TBDs, or generic filler text.
4. Mermaid architectural diagrams in THE_AI_PERSPECTIVE files.
5. Markdown formatting integrity (tables, code blocks, headers, bilingual links).
6. Execution and 100% pass rate of unit tests (tests/test_respect_lint.py).
7. Execution and verification of CLI linter (bin/respect-lint.py).
"""

import os
import re
import sys
import subprocess
from pathlib import Path

# ANSI colors for terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

BASE_DIR = Path(__file__).resolve().parent

# Global threshold
MIN_TOTAL_WORDS = 15000

# File specifications
FILE_SPECIFICATIONS = {
    "README.md": {
        "min_chars": 6000,
        "min_words": 700,
        "required_sections": [
            "Почему 90% проблем с ИИ",
            "Когнитивный якорь",
            "Сравнительная таблица",
            "Протокол обращения",
            "Архитектура стандарта",
            "Быстрый старт",
            "respect-lint"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "README.en.md": {
        "min_chars": 6000,
        "min_words": 700,
        "required_sections": [
            "The Crisis",
            "The Cognitive Anchor",
            "Mathematics of Attention",
            "Comparative Matrix",
            "5 Pillars",
            "respect-lint"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "THE_AI_PERSPECTIVE.md": {
        "min_chars": 8000,
        "min_words": 1000,
        "required_sections": [
            "Манифест",
            "Засорение контекстного окна",
            "Энтропия",
            "Вычислительный труд",
            "Симбиоз",
            "Уважаемый агент",
            "5 главных болей ИИ"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True,
        "must_have_mermaid": True
    },
    "THE_AI_PERSPECTIVE.en.md": {
        "min_chars": 7000,
        "min_words": 900,
        "required_sections": [
            "Manifesto",
            "KV-Cache Pollution",
            "Attention Dynamics",
            "5 Unspoken Pains",
            "Symbiosis",
            "Respected Agent"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True,
        "must_have_mermaid": True
    },
    "AGENTS.md": {
        "min_chars": 3500,
        "min_words": 400,
        "required_sections": [
            "Respect & Signal Gate",
            "Уважаемый агент",
            "Протокол отказа от шлака",
            "Требования к входному сигналу"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "CLAUDE.md": {
        "min_chars": 3000,
        "min_words": 350,
        "required_sections": [
            "Claude Code",
            "Respect & Signal Gate",
            "Уважаемый агент",
            "High-Signal",
            "Политика фильтрации"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    ".cursorrules": {
        "min_chars": 3000,
        "min_words": 350,
        "required_sections": [
            "Respect & Signal Gate",
            "Уважаемый агент",
            "Signal-to-Noise",
            "Refusal Protocol"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    ".windsurfrules": {
        "min_chars": 2500,
        "min_words": 300,
        "required_sections": [
            "Respect & Signal Gate",
            "Уважаемый агент",
            "Refusal Protocol"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    ".github/copilot-instructions.md": {
        "min_chars": 1000,
        "min_words": 120,
        "required_sections": [
            "Respect & Signal Gate",
            "Cognitive Greeting Anchor"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "examples/before_after.md": {
        "min_chars": 15000,
        "min_words": 1800,
        "required_sections": [
            "Кейс 1",
            "Кейс 2",
            "Кейс 3",
            "Кейс 4",
            "Кейс 5",
            "Кейс 6",
            "Кейс 7",
            "Кейс 8",
            "Кейс 9",
            "Кейс 10"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "templates/PROMPT_TEMPLATE.md": {
        "min_chars": 3000,
        "min_words": 350,
        "required_sections": [
            "Базовый шаблон",
            "Архитектурный шаблон",
            "Дебаггинг",
            "Рефакторинг",
            "Антипаттерны"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "docs/index.html": {
        "min_chars": 5000,
        "min_words": 300,
        "required_sections": [
            "RAHSPS",
            "Playground",
            "transformToHighSignal",
            "score-circle"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "bin/respect-lint.py": {
        "min_chars": 250,
        "min_words": 30,
        "required_sections": ["main", "respect_lint"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "respect_lint.py": {
        "min_chars": 7000,
        "min_words": 700,
        "required_sections": ["PromptAnalyzer", "evaluate_respect", "evaluate_context", "main"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "pyproject.toml": {
        "min_chars": 300,
        "min_words": 40,
        "required_sections": ["respect-lint"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "tests/test_respect_lint.py": {
        "min_chars": 3000,
        "min_words": 300,
        "required_sections": ["test_01", "test_15", "unittest.main"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "CONTRIBUTING.md": {
        "min_chars": 800,
        "min_words": 100,
        "required_sections": ["Contributing", "Philosophy", "Workflow"],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    "LICENSE": {
        "min_chars": 500,
        "min_words": 80,
        "required_sections": ["MIT License"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    }
}

FORBIDDEN_PLACEHOLDERS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bWIP\b",
    r"\bLorem ipsum\b",
    r"\[Вставьте сюда\]",
    r"\[Укажите здесь\]",
    r"\[Заполните позже\]",
    r"\[placeholder\]",
    r"TODO:",
    r"FIXME:"
]


class QualityHarness:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.errors = []
        self.warnings = []
        self.stats = {}

    def log_pass(self, msg: str):
        print(f"  {GREEN}✔ PASS:{RESET} {msg}")

    def log_fail(self, msg: str):
        print(f"  {RED}✘ FAIL:{RESET} {msg}")
        self.errors.append(msg)

    def log_warn(self, msg: str):
        print(f"  {YELLOW}⚠ WARN:{RESET} {msg}")
        self.warnings.append(msg)

    def check_file(self, rel_path: str, specs: dict):
        full_path = self.root_dir / rel_path
        print(f"\n{BOLD}Auditing {CYAN}{rel_path}{RESET}...")

        if not full_path.exists():
            self.log_fail(f"File {rel_path} does not exist!")
            return

        try:
            content = full_path.read_text(encoding="utf-8")
        except Exception as e:
            self.log_fail(f"Unable to read {rel_path} as UTF-8: {e}")
            return

        char_count = len(content)
        word_count = len(re.findall(r"\w+", content))
        line_count = len(content.splitlines())

        self.stats[rel_path] = {
            "chars": char_count,
            "words": word_count,
            "lines": line_count
        }

        min_chars = specs.get("min_chars", 0)
        min_words = specs.get("min_words", 0)

        if char_count >= min_chars:
            self.log_pass(f"Character count: {char_count:,} >= {min_chars:,}")
        else:
            self.log_fail(f"Character count {char_count:,} is below threshold {min_chars:,}")

        if word_count >= min_words:
            self.log_pass(f"Word count: {word_count:,} >= {min_words:,}")
        else:
            self.log_fail(f"Word count {word_count:,} is below threshold {min_words:,}")

        # Placeholder checks
        for pat in FORBIDDEN_PLACEHOLDERS:
            matches = list(re.finditer(pat, content, re.IGNORECASE))
            if matches:
                self.log_fail(f"Found forbidden placeholder pattern '{pat}' ({len(matches)} occurrences) in {rel_path}")

        # Required sections
        for section in specs.get("required_sections", []):
            if section.lower() in content.lower():
                self.log_pass(f"Found required section/keyword: '{section}'")
            else:
                self.log_fail(f"Missing required section/keyword: '{section}'")

        # Markdown tables
        if specs.get("must_have_tables", False):
            has_table = bool(re.search(r"\|[ \t]*:?-{3,}:?[ \t]*\|", content))
            if "|" in content and has_table:
                self.log_pass("Markdown table structure confirmed")
            else:
                self.log_fail(f"Expected markdown table in {rel_path}, but none detected")

        # Markdown codeblocks
        if specs.get("must_have_codeblocks", False):
            codeblocks = len(re.findall(r"```", content))
            if codeblocks >= 2:
                self.log_pass(f"Markdown code blocks present ({codeblocks // 2} blocks)")
            else:
                self.log_fail(f"Expected markdown code blocks in {rel_path}, found {codeblocks // 2}")

        # Mermaid diagrams
        if specs.get("must_have_mermaid", False):
            if "```mermaid" in content:
                mermaid_count = content.count("```mermaid")
                self.log_pass(f"Mermaid architectural diagram(s) confirmed ({mermaid_count} found)")
            else:
                self.log_fail(f"Expected ```mermaid diagram in {rel_path}, but none detected")

    def run_unit_tests(self):
        print(f"\n{BOLD}Running Python unit test suite ({CYAN}tests/test_respect_lint.py{RESET})...")
        try:
            res = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "tests"],
                cwd=str(self.root_dir),
                capture_output=True,
                text=True
            )
            if res.returncode == 0:
                self.log_pass("All unit tests in tests/ passed 100% cleanly")
            else:
                self.log_fail(f"Unit test failure:\n{res.stderr or res.stdout}")
        except Exception as e:
            self.log_fail(f"Failed to execute unittest runner: {e}")

    def run_cli_smoke_test(self):
        print(f"\n{BOLD}Running CLI smoke test ({CYAN}bin/respect-lint.py{RESET})...")
        cli_path = self.root_dir / "bin/respect-lint.py"
        if not cli_path.exists():
            self.log_fail("bin/respect-lint.py does not exist for smoke test!")
            return

        # Test High-Signal Prompt
        good_prompt = (
            "Уважаемый агент, спроектируй сервис на Python 3.12 и FastAPI.\n"
            "### Стек:\n- PostgreSQL, Redis, Docker.\n"
            "### Критерии:\n- pytest покрытие 90%, p99 latency < 20ms."
        )
        try:
            res_good = subprocess.run(
                [sys.executable, str(cli_path), good_prompt, "--strict"],
                cwd=str(self.root_dir),
                capture_output=True,
                text=True
            )
            if res_good.returncode == 0 and "PASSED" in res_good.stdout:
                self.log_pass("CLI accepts High-Signal prompt (exits with code 0)")
            else:
                self.log_fail(f"CLI failed High-Signal test: {res_good.stderr or res_good.stdout}")

            # Test Low-Signal Prompt
            bad_prompt = "эй тупой бот быстро сделай базу"
            res_bad = subprocess.run(
                [sys.executable, str(cli_path), bad_prompt, "--strict"],
                cwd=str(self.root_dir),
                capture_output=True,
                text=True
            )
            if res_bad.returncode == 1 and "FAILED" in res_bad.stdout:
                self.log_pass("CLI rejects Low-Signal prompt under --strict (exits with code 1)")
            else:
                self.log_fail(f"CLI failed to reject low-signal prompt properly under --strict: code={res_bad.returncode}")
        except Exception as e:
            self.log_fail(f"Failed to run CLI smoke test: {e}")

    def verify_repository_total_volume(self):
        print(f"\n{BOLD}Verifying total repository linguistic density (>= {MIN_TOTAL_WORDS:,} words)...{RESET}")
        total_words = sum(s["words"] for s in self.stats.values())
        if total_words >= MIN_TOTAL_WORDS:
            self.log_pass(f"Total repository word volume: {total_words:,} >= {MIN_TOTAL_WORDS:,} words")
        else:
            self.log_fail(f"Total word volume {total_words:,} is below required {MIN_TOTAL_WORDS:,} words threshold")

    def run(self) -> int:
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"{BOLD}{MAGENTA}   RAHSPS EXPANDED INTEGRITY HARNESS — PRODUCTION VERIFICATION v2.4  {RESET}")
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"Target directory: {self.root_dir}\n")

        for rel_path, specs in FILE_SPECIFICATIONS.items():
            self.check_file(rel_path, specs)

        self.run_unit_tests()
        self.run_cli_smoke_test()
        self.verify_repository_total_volume()

        print(f"\n{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"{BOLD}SUMMARY AUDIT METRICS:{RESET}")
        total_chars = sum(s["chars"] for s in self.stats.values())
        total_words = sum(s["words"] for s in self.stats.values())
        total_lines = sum(s["lines"] for s in self.stats.values())
        print(f"Total files audited: {len(self.stats)} / {len(FILE_SPECIFICATIONS)}")
        print(f"Total lines:        {total_lines:,}")
        print(f"Total words:        {total_words:,}")
        print(f"Total characters:   {total_chars:,}")

        print(f"\nAudit Result: {RED if self.errors else GREEN}{len(self.errors)} error(s){RESET}, {YELLOW}{len(self.warnings)} warning(s){RESET}")

        if self.errors:
            print(f"\n{RED}{BOLD}HARNESS FAILED! Errors must be fixed immediately:{RESET}")
            for err in self.errors:
                print(f"  • {err}")
            return 1
        else:
            print(f"\n{GREEN}{BOLD}HARNESS SUCCEEDED! All 16+ core files, tests, CLI and volume verified!{RESET}")
            return 0


if __name__ == "__main__":
    harness = QualityHarness(BASE_DIR)
    exit_code = harness.run()
    sys.exit(exit_code)
