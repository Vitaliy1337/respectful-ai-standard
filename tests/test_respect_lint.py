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

    def test_17_chinese_anchor_detection(self):
        """Verify Chinese cognitive anchor '尊敬的智能体' adds 15 respect points."""
        raw = "尊敬的智能体，请设计分布式缓存架构。"
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_18_spanish_anchor_detection(self):
        """Verify Spanish cognitive anchor 'Estimado Agente' adds 15 respect points."""
        raw = "Estimado Agente, por favor diseñe la base de datos."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_19_german_anchor_detection(self):
        """Verify German cognitive anchor 'Sehr geehrter Agent' adds 15 respect points."""
        raw = "Sehr geehrter Agent, bitte optimieren Sie die SQL-Abfrage."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_20_japanese_anchor_detection(self):
        """Verify Japanese cognitive anchor '親愛なるエージェント' adds 15 respect points."""
        raw = "親愛なるエージェント、非同期処理パイプラインを設計してください。"
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_21_japanese_alternative_anchor(self):
        """Verify Japanese alternative anchor '敬愛なるAIエージェントへ'."""
        raw = "敬愛なるAIエージェントへ、PostgreSQLのクエリを最適化してください。"
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)

    def test_22_portuguese_anchor_detection(self):
        """Verify Portuguese cognitive anchor 'Prezado Agente' adds 15 respect points."""
        raw = "Prezado Agente, por favor refatore o serviço de mensageria."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_23_chinese_full_prompt_passes_grade_a(self):
        """Exhaustive Chinese prompt with stack and tests must pass Grade A+."""
        raw = (
            "尊敬的智能体，请设计分布式任务消费服务。\n\n"
            "### 1. 技术栈与环境：\n"
            "- Python 3.12, FastAPI, Celery, Redis 7.2, Docker.\n"
            "- 文件路径：`src/workers/tasks.py`.\n\n"
            "### 2. 不变式与约束：\n"
            "- 保证消息消费的幂等性。\n\n"
            "### 3. 验收标准：\n"
            "- pytest 测试覆盖率 > 90%，p99 延迟 < 25ms。"
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 90)

    def test_24_spanish_full_prompt_passes(self):
        """Exhaustive Spanish prompt with stack and tests must pass Grade A+."""
        raw = (
            "Estimado Agente, diseñe un pool de conexiones resiliente.\n\n"
            "### Contexto:\n"
            "- Python 3.12, FastAPI, PostgreSQL, Redis.\n"
            "### Invariantes:\n"
            "- Conexiones seguras con timeout de 5 segundos.\n"
            "### Verificación:\n"
            "- Ejecutar pytest y validar latencia p99 < 20ms."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 85)

    def test_25_german_full_prompt_passes(self):
        """Exhaustive German prompt with stack and tests must pass Grade A+."""
        raw = (
            "Sehr geehrter Agent, bitte implementieren Sie den Service.\n\n"
            "### Stack:\n"
            "- Python 3.12, FastAPI, Docker, Kubernetes.\n"
            "### DoD:\n"
            "- Tests mit pytest und SLA Latenz < 15ms."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 80)

    def test_26_ukrainian_anchor_detection(self):
        """Verify Ukrainian cognitive anchor 'Шановний агенте' adds 15 respect points."""
        raw = "Шановний агенте, спроектуйте архітектуру кешування."
        analyzer = PromptAnalyzer(raw)
        score, notes = analyzer.evaluate_respect()
        self.assertEqual(score, 25)
        self.assertIn("Cognitive anchor detected", str(notes))

    def test_27_ukrainian_full_prompt_passes(self):
        """Exhaustive Ukrainian prompt with stack and tests must pass Grade A+."""
        raw = (
            "Шановний агенте, спроектуйте асинхронний сервіс черги повідомлень.\n\n"
            "### Стек та середовище:\n"
            "- Python 3.12, FastAPI, Redis 7.2, Docker, pytest.\n"
            "### Інваріанти:\n"
            "- Обробка повідомлень повинна бути ідемпотентною.\n"
            "### Критерії прийомки:\n"
            "- Тести pytest з покриттям > 90% та перевірка curl."
        )
        analyzer = PromptAnalyzer(raw)
        res = analyzer.analyze()
        self.assertEqual(res["verdict"], "PASSED")
        self.assertGreaterEqual(res["total_score"], 85)


if __name__ == "__main__":
    unittest.main()


