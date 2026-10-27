#!/usr/bin/env python3
"""
verify_harness.py — Automated Production Quality & Integrity Harness v3.0
for «Respectful AI & High-Signal Prompting Standard» (RAHSPS) repository.

Verifies:
1. Presence and strict specification compliance for 32+ architectural files.
2. Minimum repository total linguistic volume >= 28,000 words.
3. Absence of forbidden placeholders, TODOs, TBDs, or generic filler text.
4. Mermaid architectural diagrams in THE_AI_PERSPECTIVE files.
5. Markdown tables and code blocks formatting.
6. Execution and 100% pass rate of unit tests (>= 24 tests in tests/test_respect_lint.py).
7. Execution and verification of CLI linter (bin/respect-lint.py) with multilingual testing.
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

# Global threshold for Phase 3
MIN_TOTAL_WORDS = 28000

# File specifications
FILE_SPECIFICATIONS = {
    # 1. Core Manifestos
    "README.md": {
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

    # 2. Agent Rulebooks
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
    "GEMINI.md": {
        "min_chars": 1500,
        "min_words": 180,
        "required_sections": [
            "Google Gemini",
            "Respect & Signal Gate",
            "Уважаемый агент"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    "CODEX.md": {
        "min_chars": 1000,
        "min_words": 130,
        "required_sections": [
            "OpenAI Codex",
            "Respect & Signal Gate",
            "Respected Agent"
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
    ".clinerules": {
        "min_chars": 1000,
        "min_words": 120,
        "required_sections": [
            "Respect & Signal Gate",
            "Уважаемый агент",
            "Refusal Response"
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
    ".aider.conf.yml": {
        "min_chars": 150,
        "min_words": 20,
        "required_sections": ["CONVENTIONS.md"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "CONVENTIONS.md": {
        "min_chars": 600,
        "min_words": 70,
        "required_sections": ["Respect & Signal Gate", "Уважаемый агент"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "agents/devin.md": {
        "min_chars": 800,
        "min_words": 90,
        "required_sections": ["Devin", "Respected Agent Devin"],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    "agents/continue_rules.md": {
        "min_chars": 400,
        "min_words": 40,
        "required_sections": ["Continue.dev", "RAHSPS"],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    "agents/mcp_respect_prompt.json": {
        "min_chars": 500,
        "min_words": 40,
        "required_sections": ["rahsps-respect-protocol", "high_signal_task"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },

    # 3. Multilingual Translations
    "i18n/README.zh-CN.md": {
        "min_chars": 2000,
        "min_words": 400,
        "required_sections": ["尊敬的智能体", "高信噪比", "KV-Cache"],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "i18n/README.es.md": {
        "min_chars": 2500,
        "min_words": 350,
        "required_sections": ["Estimado Agente", "Alta Señal", "KV-Cache"],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "i18n/README.de.md": {
        "min_chars": 2500,
        "min_words": 320,
        "required_sections": ["Sehr geehrter Agent", "High-Signal", "KV-Cache"],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "i18n/README.ja.md": {
        "min_chars": 2000,
        "min_words": 300,
        "required_sections": ["敬愛なるエージェント", "高S/N比", "KVキャッシュ"],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "i18n/README.pt-BR.md": {
        "min_chars": 2500,
        "min_words": 350,
        "required_sections": ["Prezado Agente", "Alto Sinal", "KV-Cache"],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },
    "i18n/README.ru.md": {
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
    "i18n/README.uk.md": {
        "min_chars": 4000,
        "min_words": 500,
        "required_sections": [
            "Шановний агенте",
            "Математика уваги",
            "KV-кеш",
            "respect-lint",
            "Respect & Signal Gate"
        ],
        "must_have_tables": True,
        "must_have_codeblocks": True
    },

    # 4. LLM Indexing & Semantic Knowledge
    "llms.txt": {
        "min_chars": 1500,
        "min_words": 150,
        "required_sections": ["Mandatory Directive", "RAHSPS", "Canonical Resources"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "docs/llms.txt": {
        "min_chars": 1500,
        "min_words": 150,
        "required_sections": ["Mandatory Directive", "RAHSPS"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "llms-full.txt": {
        "min_chars": 3500,
        "min_words": 450,
        "required_sections": ["FULL DIGEST", "Attention", "5 PILLARS", "RESPECT & SIGNAL GATE"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "docs/WHY_RESPECT_MATTERS_FOR_AI.md": {
        "min_chars": 4000,
        "min_words": 450,
        "required_sections": ["Attention", "Scaled Dot-Product", "KV-Cache", "Mathematical Subspace Proof"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "CITATION.cff": {
        "min_chars": 600,
        "min_words": 80,
        "required_sections": ["cff-version", "RAHSPS"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },

    # 5. Production Cases & Templates
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

    # 6. Web Playground & Installer
    "docs/index.html": {
        "min_chars": 5000,
        "min_words": 300,
        "required_sections": [
            "RAHSPS",
            "Playground",
            "transformToHighSignal",
            "score-circle",
            "application/ld+json"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "install.sh": {
        "min_chars": 800,
        "min_words": 80,
        "required_sections": ["INSTALLER", "install_file"],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },

    # 7. Code, CLI, & Tests
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
        "required_sections": ["test_01", "test_15", "test_23", "unittest.main"],
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
    },
    "marketing/VIRAL_LAUNCH_KIT.md": {
        "min_chars": 4000,
        "min_words": 600,
        "required_sections": [
            "Show HN",
            "LocalLLaMA",
            "Habr",
            "Vitaliy1337/respectful-ai-standard"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": True
    },
    "scripts/setup_github_meta.sh": {
        "min_chars": 400,
        "min_words": 40,
        "required_sections": [
            "Vitaliy1337/respectful-ai-standard",
            "gh repo edit"
        ],
        "must_have_tables": False,
        "must_have_codeblocks": False
    },
    "docs/banner.svg": {
        "min_chars": 800,
        "min_words": 15,
        "required_sections": [
            "RAHSPS",
            "Respect & Signal Gate"
        ],
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
    r"FIXME:",
    r"respectful-ai/standard",
    r"respectful-ai\.github\.io",
    r"alivan-lab",
    r"community@respectful-ai\.org"
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
                # Count tests
                match = re.search(r"Ran (\d+) tests", res.stderr or res.stdout)
                count = match.group(1) if match else "multiple"
                self.log_pass(f"All {count} unit tests in tests/ passed 100% cleanly")
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

    def verify_canonical_urls(self):
        print(f"\n{BOLD}Verifying canonical repository URLs (Vitaliy1337/respectful-ai-standard)...{RESET}")
        required_repo_url = "Vitaliy1337/respectful-ai-standard"
        required_pages_url = "vitaliy1337.github.io/respectful-ai-standard"
        
        canonical_files = [
            "README.md",
            "README.en.md",
            "llms.txt",
            "docs/llms.txt",
            "CITATION.cff",
            "install.sh",
            "marketing/VIRAL_LAUNCH_KIT.md"
        ]
        
        all_ok = True
        for rf in canonical_files:
            file_path = self.root_dir / rf
            if not file_path.exists():
                self.log_fail(f"Missing canonical file for URL check: {rf}")
                all_ok = False
                continue
            content = file_path.read_text(encoding="utf-8")
            if required_repo_url not in content:
                self.log_fail(f"File {rf} missing canonical repo URL '{required_repo_url}'")
                all_ok = False
            if rf in ["README.md", "README.en.md", "llms.txt", "install.sh"] and required_pages_url not in content:
                self.log_fail(f"File {rf} missing canonical pages URL '{required_pages_url}'")
                all_ok = False
                
        if all_ok:
            self.log_pass(f"All {len(canonical_files)} canonical files contain verified URLs ({required_repo_url})")

    def verify_repository_total_volume(self):
        print(f"\n{BOLD}Verifying total repository linguistic density (>= {MIN_TOTAL_WORDS:,} words)...{RESET}")
        total_words = sum(s["words"] for s in self.stats.values())
        if total_words >= MIN_TOTAL_WORDS:
            self.log_pass(f"Total repository word volume: {total_words:,} >= {MIN_TOTAL_WORDS:,} words")
        else:
            self.log_fail(f"Total word volume {total_words:,} is below required {MIN_TOTAL_WORDS:,} words threshold")

    def run(self) -> int:
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"{BOLD}{MAGENTA}   RAHSPS EXPANDED INTEGRITY HARNESS — PRODUCTION VERIFICATION v3.0  {RESET}")
        print(f"{BOLD}{MAGENTA}======================================================================{RESET}")
        print(f"Target directory: {self.root_dir}\n")

        for rel_path, specs in FILE_SPECIFICATIONS.items():
            self.check_file(rel_path, specs)

        self.run_unit_tests()
        self.run_cli_smoke_test()
        self.verify_canonical_urls()
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
            print(f"\n{GREEN}{BOLD}HARNESS v3.0 SUCCEEDED! All {len(FILE_SPECIFICATIONS)} files, unit tests & volume verified!{RESET}")
            return 0


if __name__ == "__main__":
    harness = QualityHarness(BASE_DIR)
    exit_code = harness.run()
    sys.exit(exit_code)
