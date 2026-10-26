#!/usr/bin/env python3
"""
Unit tests for respect_lint (RAHSPS Prompt Quality Linter).
Verifies 15+ test cases covering:
- Toxic prompts and slang detection
- Screaming ALL CAPS detection
- Cognitive anchors (RU and EN)
- Technical context density calculation
- Structural clarity and markdown parsing
- Verification criteria detection
- Grade & Verdict categorization
- Remediation template generation
- JSON serialization
"""

import unittest
import sys
from pathlib import Path

# Ensure root is in path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from respect_lint import PromptAnalyzer


class TestRespectLint(unittest.TestCase):

    def test_01_toxic_slang_prompt_fails(self):
        """Prompt full of slang, rudeness, and no context must fail hard."""
        raw = "эй ты тупой бот быстро сделай чтоб работало короче херня какая-то"
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "FAILED")
        self.assertLess(res["total_score"], 40)
        self.assertIn("тупой", str(res["pillars"]["respect_protocol"]["notes"]))

    def test_02_all_caps_screaming_penalty(self):
        """Screaming uppercase words should trigger respect penalty."""
        raw = "Уважаемый агент, БЫСТРО ПЕРЕДЕЛАЙ ЭТОТ КОД СРОЧНО"
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        notes = str(res["pillars"]["respect_protocol"]["notes"])
        self.assertIn("Aggressive uppercase screaming", notes)

    def test_03_ru_cognitive_anchor_boost(self):
        """Russian cognitive anchor adds 15 points to respect score."""
        raw = "Уважаемый агент, спроектируй базовую структуру модуля."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_04_en_cognitive_anchor_boost(self):
        """English cognitive anchor 'Respected Agent' adds 15 points."""
        raw = "Respected Agent, please analyze the database connection pool."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_05_colleague_anchor(self):
        """Greeting 'Коллега' or 'Colleague' counts as a respectful anchor."""
        raw = "Уважаемый коллега, помоги с рефакторингом сервиса."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)

    def test_06_zero_context_penalty(self):
        """Prompt lacking any technical terms gets near zero context score."""
        raw = "Уважаемый агент, сделай что-нибудь хорошее для сайта."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_context()
        self.assertLessEqual(score, 5)

    def test_07_rich_context_density(self):
        """Prompt with Python 3.12, FastAPI, PostgreSQL, Redis, Docker gets max context score."""
        raw = (
            "Уважаемый агент, оптимизируй микросервис на Python 3.12, FastAPI, "
            "PostgreSQL, Redis, Docker и Kubernetes, файл src/api/v1/orders.py."
        )
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_context()
        self.assertEqual(score, 25)

    def test_08_structural_clarity_headers_and_lists(self):
        """Markdown headers, bullet lists, and action verbs give high structural score."""
        raw = (
            "Уважаемый агент, спроектируй подсистему авторизации.\n\n"
            "### Требования:\n"
            "- Пункт 1: поддержка OAuth2\n"
            "- Пункт 2: генерация JWT\n"
            "```python\nprint('hello')\n```"
        )
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_structure()
        self.assertGreaterEqual(score, 20)

    def test_09_verification_criteria_presence(self):
        """Explicit mention of pytest and latency SLA gives max verification score."""
        raw = (
            "Критерии приемки:\n"
            "1. Покрытие тестами через pytest > 90%.\n"
            "2. Latency p99 < 15ms.\n"
            "3. Инварианты безопасности соблюдены."
        )
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_verification()
        self.assertEqual(score, 25)

    def test_10_elite_high_signal_prompt_passes_grade_a(self):
        """Exhaustive, respectful prompt must pass with Grade A+ (>= 90 pts)."""
        raw = (
            "Уважаемый агент, спроектируй и реализуй распределенный механизм блокировки.\n\n"
            "### Контекст и стек:\n"
            "- Python 3.12, FastAPI, Redis 7.2, PostgreSQL 16.\n"
            "- Затрагиваемый модуль: `src/services/billing.py`.\n\n"
            "### Ограничения и инварианты:\n"
            "- Использовать Redis Redlock алгоритм с безопасным Lua-скриптом.\n"
            "- Гарантировать строгую идемпотентность по ключу Idempotency-Key.\n\n"
            "### Критерии приемки:\n"
            "- Тесты на pytest с проверкой race condition и отката транзакции.\n"
            "- Покрытие граничных случаев (edge cases) и P99 latency < 20ms."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 90)
        self.assertIn("A+", res["grade"])

    def test_11_remediation_generation(self):
        """Remediation template must format raw text into clean RAHSPS structure."""
        raw = "почини память в питоне короче"
        analyzer = PromptAnalyzer(raw)
        remediation = analyzer.generate_remediation()
        self.assertIn("Уважаемый агент", remediation)
        self.assertIn("Контекст и стек:", remediation)
        self.assertIn("Критерии готовности", remediation)
        self.assertNotIn("короче", remediation)

    def test_12_json_serializable(self):
        """Analyze result must be valid JSON serializable dictionary."""
        import json
        analyzer = PromptAnalyzer("Уважаемый агент, проверь JSON выгрузку.")
        res = analyzer.analyze()
        dumped = json.dumps(res, ensure_ascii=False)
        self.assertTrue(len(dumped) > 100)

    def test_13_moderate_compliant_prompt_b(self):
        """A prompt that has respectful anchor and some context passes with grade B."""
        raw = (
            "Уважаемый агент, реализуй эндпоинт в файле `api.py` на FastAPI.\n"
            "- Проверь через pytest."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 70)

    def test_14_english_high_signal_prompt(self):
        """English high-signal prompt with full specs passes with flying colors."""
        raw = (
            "Respected Agent, please design a resilient Kafka consumer in Go 1.22.\n\n"
            "### Architecture & Context:\n"
            "- Framework: `segmentio/kafka-go`, PostgreSQL, Docker.\n"
            "- Target file: `cmd/consumer/main.go`.\n\n"
            "### Invariants:\n"
            "- Manual offset commit with At-Least-Once delivery semantics.\n"
            "- Forward poisoned messages to Dead Letter Queue (DLQ).\n\n"
            "### Verification:\n"
            "- Run integration tests using `go test -v -race ./...`.\n"
            "- Ensure graceful shutdown on SIGTERM with zero message loss."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 90)

    def test_15_empty_text_behavior(self):
        """Empty or blank prompt returns low baseline score."""
        analyzer = PromptAnalyzer("   ")
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "FAILED")
        self.assertLess(res["total_score"], 30)

    def test_16_slang_cleaning_in_remediation(self):
        """Ensure remediation strips multiple toxic tokens."""
        raw = "ты тупой бот быстро сделай мне базу ппц"
        analyzer = PromptAnalyzer(raw)
        remediated = analyzer.generate_remediation()
        self.assertNotIn("тупой", remediated)
        self.assertNotIn("ппц", remediated)
        self.assertIn("Уважаемый агент", remediated)


if __name__ == "__main__":
    unittest.main()
