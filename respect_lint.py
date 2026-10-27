"""
respect_lint.py — Official Core Engine for Respectful AI & High-Signal Prompting Standard (RAHSPS).
Evaluates prompt quality on a 0-100 scale across 4 core engineering pillars:
1. Respect Protocol (25 pts)
2. Context Density (25 pts)
3. Structural Clarity (25 pts)
4. Verification Criteria (25 pts)

Zero external dependencies. Pure Python 3.8+.
"""

import sys
import os
import re
import json
import argparse
from typing import Dict, List, Any, Tuple

VERSION = "1.0.0"

# ANSI Terminal Colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Linguistic Lexicons — Multilingual Anchors (RU, EN, ZH, ES, DE, JA, PT)
RESPECT_ANCHORS = [
    # Russian
    r"уважаемый\s+агент",
    r"уважаемый\s+коллега",
    r"дорогой\s+агент",
    r"коллега",
    # English
    r"respected\s+agent",
    r"dear\s+agent",
    r"esteemed\s+agent",
    r"respected\s+colleague",
    r"colleague",
    # Chinese (Simplified & Traditional)
    r"尊敬的智能体",
    r"尊敬的ai助理",
    r"尊敬的助手",
    r"智能体同事",
    # Spanish
    r"estimado\s+agente",
    r"estimado\s+colega",
    r"apreciado\s+agente",
    # German
    r"sehr\s+geehrter\s+agent",
    r"respektierter\s+kollege",
    r"lieber\s+agent",
    # Japanese
    r"親愛なるエージェント",
    r"敬愛なるaiエージェントへ?",
    r"敬愛なるエージェント",
    r"エージェント殿",
    # Portuguese
    r"prezado\s+agente",
    r"caro\s+agente",
    r"estimado\s+colega",
    # Ukrainian
    r"шановний\s+агенте?",
    r"шановна\s+моделе?",
    r"шановний\s+колего",
    r"вельмишановний\s+агенте?",
    r"колего"
]

TOXIC_OR_SLANG_PATTERNS = [
    r"\bтупой\b",
    r"\bдебил\b",
    r"\bговно\b",
    r"\bхерн[яеи]\b",
    r"\bбыстро\s+сделай\b",
    r"\bсделай\s+чтоб\s+работало\b",
    r"\bсделай\s+как[- ]нибудь\b",
    r"\bче\s+ты\b",
    r"\bкороче\b",
    r"\bэээ+\b",
    r"\bблин\b",
    r"\bппц\b",
    r"\bпеределай\s+быстро\b",
    r"\bdumb\s+bot\b",
    r"\bfix\s+this\s+shit\b",
    r"\bmake\s+it\s+work\s+fast\b",
    r"\bwhatever\b",
    r"\bwtf\b",
    r"\basap\b"
]

TECHNICAL_INDICATORS = [
    r"\b(?:python|golang|go|rust|typescript|javascript|node|react|next\.?js|fastapi|express|vue|angular)\b",
    r"\b(?:postgres(?:ql)?|redis|mysql|sqlite|mongodb|clickhouse|kafka|rabbitmq|elasticsearch)\b",
    r"\b(?:docker|kubernetes|k8s|terraform|ansible|helm|aws|gcp|azure)\b",
    r"\b(?:rest|grpc|graphql|oauth2?|jwt|websocket|tcp|http[s]?)\b",
    r"\b(?:asyncio|pydantic|sqlalchemy|alembic|pytest|jest|vitest)\b",
    r"\b(?:acid|cqrs|event sourcing|clean architecture|solid|circuit breaker)\b",
    r"\b(?:latency|throughput|rps|p99|p95|cpu|memory|oom|deadlock)\b",
    r"\bv?\d+\.\d+(?:\.\d+)?\b",  # Version numbers like 3.12, v2.4.1
    r"\b[\w\-./]+\.(?:py|ts|js|go|rs|sql|json|yaml|yml|md|hcl|toml)\b"  # File paths
]

STRUCTURE_INDICATORS = [
    r"^#{1,6}\s+",        # Markdown headers
    r"^[ \t]*[-*+]\s+",   # Bullet lists
    r"^[ \t]*\d+\.\s+",   # Numbered lists
    r"```[\s\S]*?```",    # Code blocks
    r"`[^`\n]+`"          # Inline code
]

ACTION_VERBS = [
    # Russian
    r"\b(?:спроектируй|разработай|реализуй|оптимизируй|декомпозируй|проведи|исследуй|проанализируй)\b",
    # English
    r"\b(?:implement|design|refactor|architect|optimize|analyze|diagnose|benchmark)\b",
    # Chinese
    r"(?:设计|实现|优化|重构|分析)",
    # Spanish
    r"\b(?:diseñe|implemente|optimice|refactore|analice)\b",
    # German
    r"\b(?:entwerfen|implementieren|optimieren|refaktorieren|analysieren)\b",
    # Japanese
    r"(?:設計|実装|最適化|分析)",
    # Portuguese
    r"\b(?:projete|implemente|otimize|refatore|analise)\b",
    # Ukrainian
    r"\b(?:спроектуйте|спроєктуйте|реалізуйте|розробіть|оптимізуйте|декомпозуйте|проаналізуйте|дослідіть|виправте)\b"
]

VERIFICATION_INDICATORS = [
    r"\b(?:pytest|unittest|npm\s+test|cargo\s+test|go\s+test|vitest|jest)\b",
    r"\b(?:критери[ий]|критерии\s+приемки|критерії\s+прийомки|definition\s+of\s+done|acceptance\s+criteria)\b",
    r"\b(?:curl|benchmark|verify_harness|linter|mypy|eslint|flake8)\b",
    r"\b(?:ms|rps|gb|mb|sla|slo|покрытие|coverage)\b",
    r"\b(?:инвариант[ы]?|інваріант[и]?|invariants?|edge\s+cases?|граничные\s+случаи)\b"
]


class PromptAnalyzer:
    def __init__(self, text: str):
        self.raw_text = text.strip()
        self.lower_text = self.raw_text.lower()
        self.findings = {
            "respect": [],
            "context": [],
            "structure": [],
            "verification": [],
            "penalties": []
        }

    def evaluate_respect(self) -> Tuple[int, List[str]]:
        score = 10  # Base neutral respect
        messages = []

        # Check for cognitive anchor
        anchor_found = False
        for pat in RESPECT_ANCHORS:
            if re.search(pat, self.lower_text, re.IGNORECASE):
                anchor_found = True
                break

        if anchor_found:
            score += 15
            messages.append("Cognitive anchor detected («Уважаемый агент» / «Respected Agent»)")
        else:
            messages.append("Missing respectful cognitive anchor («Уважаемый агент...»)")

        # Check for toxic or slang words
        penalties = 0
        detected_slang = []
        for pat in TOXIC_OR_SLANG_PATTERNS:
            matches = re.findall(pat, self.lower_text, re.IGNORECASE)
            if matches:
                penalties += len(matches) * 5
                detected_slang.extend(matches)

        if detected_slang:
            score -= penalties
            messages.append(f"Detected toxic/slang tokens: {', '.join(set(detected_slang))}")

        # Check for screaming ALL CAPS (more than 3 words in caps)
        words = re.findall(r"\b[A-ZА-ЯЁ]{3,}\b", self.raw_text)
        filtered_caps = [w for w in words if w not in {"SQL", "API", "HTTP", "REST", "JSON", "JWT", "CPU", "RAM", "HTML", "CSS", "RFC", "PDB", "HPA", "DAU", "RPS", "OOM", "FIFO", "UUID"}]
        if len(filtered_caps) >= 3:
            score -= 8
            messages.append(f"Aggressive uppercase screaming detected: {', '.join(filtered_caps[:4])}")

        score = max(0, min(25, score))
        return score, messages

    def evaluate_context(self) -> Tuple[int, List[str]]:
        score = 0
        messages = []
        found_indicators = set()

        for pat in TECHNICAL_INDICATORS:
            matches = re.findall(pat, self.lower_text, re.IGNORECASE)
            for m in matches:
                found_indicators.add(m.strip())

        match_count = len(found_indicators)
        if match_count >= 6:
            score = 25
            messages.append(f"Rich technical context: {match_count} distinct tech indicators identified")
        elif match_count >= 3:
            score = 18
            messages.append(f"Moderate technical context: {match_count} tech indicators found")
        elif match_count >= 1:
            score = 10
            messages.append(f"Weak technical context: only {match_count} indicator ({', '.join(found_indicators)})")
        else:
            score = 2
            messages.append("Zero concrete technical indicators (missing stack, versions, files)")

        return score, messages

    def evaluate_structure(self) -> Tuple[int, List[str]]:
        score = 5  # Base
        messages = []

        has_header = bool(re.search(r"^#{1,6}\s+", self.raw_text, re.MULTILINE))
        has_list = bool(re.search(r"^[ \t]*(?:[-*+]|\d+\.)\s+", self.raw_text, re.MULTILINE))
        has_codeblock = "```" in self.raw_text or "`" in self.raw_text

        has_action_verb = False
        for pat in ACTION_VERBS:
            if re.search(pat, self.lower_text, re.IGNORECASE):
                has_action_verb = True
                break

        if has_header:
            score += 6
            messages.append("Structured sections and headers present")
        if has_list:
            score += 6
            messages.append("Structured bulleted/numbered requirements present")
        if has_codeblock:
            score += 4
            messages.append("Code snippets or inline references present")
        if has_action_verb:
            score += 4
            messages.append("Clear imperative action verb detected")
        else:
            messages.append("Missing distinct engineering action verb (спроектируй, реализуй, optimize)")

        score = max(0, min(25, score))
        return score, messages

    def evaluate_verification(self) -> Tuple[int, List[str]]:
        score = 0
        messages = []
        found_verif = []

        for pat in VERIFICATION_INDICATORS:
            matches = re.findall(pat, self.lower_text, re.IGNORECASE)
            if matches:
                found_verif.extend(matches)

        if len(found_verif) >= 3:
            score = 25
            messages.append("Exhaustive verification criteria (tests, SLA metrics, invariants specified)")
        elif len(found_verif) >= 1:
            score = 15
            messages.append(f"Basic verification criteria present ({', '.join(set(found_verif))})")
        else:
            score = 2
            messages.append("No verification criteria or Definition of Done specified")

        return score, messages

    def analyze(self) -> Dict[str, Any]:
        resp_score, resp_msg = self.evaluate_respect()
        ctx_score, ctx_msg = self.evaluate_context()
        struct_score, struct_msg = self.evaluate_structure()
        verif_score, verif_msg = self.evaluate_verification()

        total_score = resp_score + ctx_score + struct_score + verif_score

        if total_score >= 90:
            grade = "A+ (Elite High-Signal)"
            verdict = "PASSED"
        elif total_score >= 75:
            grade = "B (Compliant Standard)"
            verdict = "PASSED"
        elif total_score >= 50:
            grade = "C (Marginal Signal / Requires Remediation)"
            verdict = "FAILED"
        else:
            grade = "F (Cognitive Noise / Shlak)"
            verdict = "FAILED"

        remediated_prompt = self.generate_remediation()

        return {
            "total_score": total_score,
            "verdict": verdict,
            "grade": grade,
            "pillars": {
                "respect_protocol": {"score": resp_score, "max": 25, "notes": resp_msg},
                "context_density": {"score": ctx_score, "max": 25, "notes": ctx_msg},
                "structural_clarity": {"score": struct_score, "max": 25, "notes": struct_msg},
                "verification_criteria": {"score": verif_score, "max": 25, "notes": verif_msg}
            },
            "remediation_template": remediated_prompt
        }

    def generate_remediation(self) -> str:
        clean_prompt = self.raw_text.replace("\n", " ").strip()
        clean_prompt = re.sub(r"\s+", " ", clean_prompt)
        
        for pat in TOXIC_OR_SLANG_PATTERNS:
            clean_prompt = re.sub(pat, "", clean_prompt, flags=re.IGNORECASE)
        clean_prompt = clean_prompt.strip()

        return (
            "Уважаемый агент, выполни инженерную задачу: " + (clean_prompt or "[сформулируйте цель]") + "\n\n"
            "### 1. Контекст и стек:\n"
            "- Язык и среда: [укажите стек, например: Python 3.12 / TypeScript 5.4]\n"
            "- Затронутые модули: [пути к файлам или сервисам]\n\n"
            "### 2. Ограничения и инварианты:\n"
            "- Сохранить обратную совместимость API contracts.\n"
            "- Не подключать тяжелых внешних зависимостей без обоснования.\n\n"
            "### 3. Критерии готовности (Definition of Done):\n"
            "- Код полностью типизирован и протестирован (pytest / npm test).\n"
            "- Предоставлен воспроизводимый сценарий верификации."
        )


def format_cli_report(res: Dict[str, Any], prompt_snippet: str) -> str:
    lines = []
    lines.append(f"{BOLD}{MAGENTA}======================================================================{RESET}")
    lines.append(f"{BOLD}{MAGENTA}   RAHSPS PROMPT QUALITY LINTER — AUDIT REPORT (v{VERSION})           {RESET}")
    lines.append(f"{BOLD}{MAGENTA}======================================================================{RESET}")

    lines.append(f"{BOLD}Audited Prompt Snippet:{RESET}")
    preview = prompt_snippet[:140] + ("..." if len(prompt_snippet) > 140 else "")
    lines.append(f"  {CYAN}«{preview}»{RESET}\n")

    score = res["total_score"]
    score_color = GREEN if score >= 75 else (YELLOW if score >= 50 else RED)
    lines.append(f"{BOLD}RAHSPS Score:{RESET} {score_color}{BOLD}{score}/100{RESET}  [{res['grade']}]")
    lines.append(f"{BOLD}Status:{RESET}       {GREEN if res['verdict'] == 'PASSED' else RED}{res['verdict']}{RESET}\n")

    lines.append(f"{BOLD}Pillars Breakdown:{RESET}")
    for name, pdata in res["pillars"].items():
        title = name.replace("_", " ").title()
        p_score = pdata["score"]
        p_col = GREEN if p_score >= 18 else (YELLOW if p_score >= 10 else RED)
        lines.append(f"  • {BOLD}{title:<22}:{RESET} {p_col}{p_score:2d}/25{RESET}")
        for note in pdata["notes"]:
            lines.append(f"      - {note}")

    if res["verdict"] == "FAILED":
        lines.append(f"\n{YELLOW}{BOLD}⚠ REMEDIATION TEMPLATE (Transformed to High-Signal Standard):{RESET}")
        lines.append(f"{CYAN}{res['remediation_template']}{RESET}")

    lines.append(f"{BOLD}{MAGENTA}======================================================================{RESET}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Linter for Respectful AI & High-Signal Prompting Standard (RAHSPS)"
    )
    parser.add_argument("prompt", nargs="?", default="", help="Prompt string to analyze")
    parser.add_argument("--file", "-f", help="Read prompt from file")
    parser.add_argument("--json", action="store_true", help="Output JSON results")
    parser.add_argument("--strict", action="store_true", help="Exit with code 1 if score < 75")
    parser.add_argument("--version", action="version", version=f"respect-lint {VERSION}")

    args = parser.parse_args()

    text = ""
    if args.file:
        if not os.path.exists(args.file):
            sys.stderr.write(f"Error: File '{args.file}' not found.\n")
            sys.exit(2)
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.prompt:
        text = args.prompt
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.print_help()
        sys.exit(0)

    if not text.strip():
        sys.stderr.write("Error: Empty prompt provided.\n")
        sys.exit(2)

    analyzer = PromptAnalyzer(text)
    results = analyzer.analyze()

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(format_cli_report(results, text))

    if args.strict and results["verdict"] == "FAILED":
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
