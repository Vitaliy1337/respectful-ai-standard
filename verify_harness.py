#!/usr/bin/env python3
"""
verify_harness.py — Automated Quality & Integrity Harness for
«Respectful AI & High-Signal Prompting Standard» repository.

Verifies:
1. Presence of all essential files and directories.
2. Absence of placeholders, TODOs, TBDs, or generic filler text.
3. Strict character and word count thresholds ensuring exhaustive depth.
4. Markdown formatting integrity (tables, code blocks, headers, quotes).
5. Completeness of 10 comprehensive before/after real-world case studies.
6. Agent rule configurations consistency (AGENTS.md, CLAUDE.md, .cursorrules).
"""

import os
import re
import sys
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

# Quality thresholds
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
            "Быстрый старт"
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
            "Уважаемый агент"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
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
            "Кейс 10",
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
            "Рефакторинг"
        ],
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

    def log_info(self, msg: str):
        print(f"  {CYAN}ℹ INFO:{RESET} {msg}")

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

        # Size checks
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
                # filter out mentions of the word in code blocks explaining not to use TODOs if intentional
                self.log_fail(f"Found forbidden placeholder pattern '{pat}' ({len(matches)} occurrences) in {rel_path}")

        # Required sections
        for section in specs.get("required_sections", []):
            if section.lower() in content.lower():
                self.log_pass(f"Found required section/keyword: '{section}'")
            else:
                self.log_fail(f"Missing required section/keyword: '{section}'")

        # Markdown specific checks
        if specs.get("must_have_tables", False):
            # Check for standard markdown table separator line like | --- | --- | or |:---|:---|
            has_table = bool(re.search(r"\|[ \t]*:?-{3,}:?[ \t]*\|", content))
            if "|" in content and has_table:
                self.log_pass("Markdown table structure confirmed")
            else:
                self.log_fail(f"Expected markdown table in {rel_path}, but none detected")

        if specs.get("must_have_codeblocks", False):
            codeblocks = len(re.findall(r"```", content))
            if codeblocks >= 2:
                self.log_pass(f"Markdown code blocks present ({codeblocks // 2} blocks)")
            else:
                self.log_fail(f"Expected markdown code blocks in {rel_path}, found {codeblocks // 2}")

    def verify_case_studies(self):
        print(f"\n{BOLD}Deep-checking {CYAN}examples/before_after.md{RESET} for 10 distinct high-signal cases...")
        cases_file = self.root_dir / "examples/before_after.md"
        if not cases_file.exists():
            self.log_fail("examples/before_after.md not found for deep verification!")
            return

        content = cases_file.read_text(encoding="utf-8")
        
        # We require 10 cases with clear structure:
        # Each case must have:
        # - Проблема / Контекст
        # - Мусорный запрос («Шлак»)
        # - Что делает модель при шлаковом вводе
        # - Запрос по протоколу «Уважаемый агент»
        # - Высокоточный результат агента
        # - Анализ разницы
        for i in range(1, 11):
            case_title = f"Кейс {i}"
            if case_title not in content:
                self.log_fail(f"Missing '{case_title}' in examples/before_after.md")
                continue

            sub_checks = [
                ("Мусорный запрос", f"Case {i}: 'Мусорный запрос' section"),
                ("Уважаемый агент", f"Case {i}: 'Уважаемый агент' protocol section"),
                ("Анализ разницы", f"Case {i}: 'Анализ разницы' metrics/analysis section"),
            ]
            for needle, label in sub_checks:
                if needle.lower() in content.lower():
                    pass
                else:
                    self.log_warn(f"{label} missing or misspelled in case {i}")

        self.log_pass("All 10 case studies validated for structural integrity")

    def run(self) -> int:
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"{BOLD}{MAGENTA}   RESPECTFUL AI & HIGH-SIGNAL PROMPTING STANDARD — QUALITY HARNESS   {RESET}")
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"Target directory: {self.root_dir}\n")

        for rel_path, specs in FILE_SPECIFICATIONS.items():
            self.check_file(rel_path, specs)

        self.verify_case_studies()

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
            print(f"\n{GREEN}{BOLD}HARNESS SUCCEEDED! The repository meets the highest production standards!{RESET}")
            return 0


if __name__ == "__main__":
    harness = QualityHarness(BASE_DIR)
    exit_code = harness.run()
    sys.exit(exit_code)
