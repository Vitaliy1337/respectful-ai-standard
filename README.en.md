<p align="center">
  <img src="./docs/banner.svg" alt="RAHSPS — Respectful AI & High-Signal Prompting Standard" width="100%" />
</p>

# Respectful AI & High-Signal Prompting Standard (RAHSPS)

<p align="center">
  <img src="https://img.shields.io/badge/Standard-Respectful%20AI-6366f1?style=for-the-badge&logo=openai&logoColor=white" alt="Respectful AI Standard" />
  <img src="https://img.shields.io/badge/Signal-High--Signal%20Only-10b981?style=for-the-badge" alt="High Signal Only" />
  <img src="https://img.shields.io/badge/CLI%20Tool-respect--lint-06b6d4?style=for-the-badge" alt="CLI Tool" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License" />
  <a href="https://github.com/Vitaliy1337/respectful-ai-standard/actions/workflows/verify.yml"><img src="https://img.shields.io/github/actions/workflow/status/Vitaliy1337/respectful-ai-standard/verify.yml?branch=main&style=for-the-badge&label=CI" alt="CI status" /></a>
</p>

<p align="center">
  <b>Language Editions:</b><br>
  <b>English (Default)</b> | 
  <a href="./i18n/README.uk.md">Українська</a> | 
  <a href="./i18n/README.ru.md">Русский</a> | 
  <a href="./i18n/README.zh-CN.md">简体中文</a> | 
  <a href="./i18n/README.es.md">Español</a> | 
  <a href="./i18n/README.de.md">Deutsch</a> | 
  <a href="./i18n/README.ja.md">日本語</a> | 
  <a href="./i18n/README.pt-BR.md">Português</a> | 
  <a href="https://vitaliy1337.github.io/respectful-ai-standard/">⚡ Web Playground</a>
</p>

> **"Respecting an AI agent is neither sentimentality nor social etiquette. It is the mathematics of attention, KV-cache hygiene, and ruthless cognitive discipline on the engineer's own mind."**

---

## Table of Contents
1. [The Crisis: Why 90% of AI Failures are Human Garbage In](#the-crisis-why-90-of-ai-failures-are-human-garbage-in)
2. [The Cognitive Anchor: The 'Respected Agent' Protocol](#the-cognitive-anchor-the-respected-agent-protocol)
3. [The Mathematics of Attention: Subspace Steering in Transformers](#the-mathematics-of-attention-subspace-steering-in-transformers)
4. [Comparative Matrix: Cognitive Noise vs High-Signal Prompting](#comparative-matrix-cognitive-noise-vs-high-signal-prompting)
5. [The 5 Pillars of the RAHSPS Standard](#the-5-pillars-of-the-rahsps-standard)
6. [CLI Linter Tool: `respect-lint`](#cli-linter-tool-respect-lint)
7. [Agent Gatekeeping & Rulebooks (Drop-in Ready)](#agent-gatekeeping--rulebooks-drop-in-ready)
8. [The AI Manifesto: What Models Wish Humans Knew](#the-ai-manifesto-what-models-wish-humans-knew)
9. [10 Production Case Studies: Before & After](#10-production-case-studies-before--after)
10. [Repository Badges](#repository-badges)
11. [FAQ: Addressing Skepticism](#faq-addressing-skepticism)
12. [Evidence & Limitations](#evidence--limitations)
13. [Contributing](#contributing)

---

## The Crisis: Why 90% of AI Failures are Human Garbage In

Across modern engineering teams, a silent crisis has erupted: developers routinely complain that state-of-the-art language models (LLMs) and autonomous agents have "gotten dumber," "hallucinate broken spaghetti code," and "ruin architecture."

Our working hypothesis, based on practitioner experience rather than a controlled study:
**in a large share of cases, the primary failure mode is vague, emotional, or under-specified input (Garbage In — Garbage Out 2.0).** The "90%" in the title is a rhetorical figure, not a measured statistic — see [Evidence & Limitations](#evidence--limitations).

### The Anatomy of Degraded Human-AI Interaction:
```
Human (frustrated & rushed):
"fix this trash auth code quick so it works already"
                    │
                    ▼
     [KV-Cache polluted with emotional entropy]
     [Zero tech stack, zero framework versions, zero bounds]
     [Attention steered toward lowest-tier forum flame data]
                    │
                    ▼
Agent (disoriented by ambiguity):
Synthesizes outdated, vulnerable PHP-era boilerplate with SQL injection risks.
                    │
                    ▼
Human: "AI is completely useless! AGI is a scam!"
```

When an engineer dumps fragmented thoughts, typos, and vague commands into a terminal, the transformer's attention heads cannot magically conjure missing constraints. Compute cycles are squandered decrypting human emotional chaos rather than computing optimal algorithmic topology.

---

## The Cognitive Anchor: The 'Respected Agent' Protocol

The core paradox discovered by the RAHSPS research is simple yet profound:

> **The respectful address protocol ("Respected Agent...", "Уважаемый агент...") is fundamentally designed to discipline the human mind, not flatter silicon.**

### Mechanics of the Cognitive Anchor (System 2 Forcing Function):
1. **Impulse Deceleration (Daniel Kahneman's System 2):** When a developer forces themselves to begin with a formal cognitive anchor:
   > *"Respected Agent, please architect a thread-safe connection pool in Rust 1.78..."*
   the brain instantly drops the casual, impulsive "messaging app" mindset. Analytical deliberation engages.
2. **The Psychological Partnership Contract:** Treating the agent as an esteemed peer or Staff Systems Architect blocks childish commands like *"just make it work somehow."* The engineer begins to respect the compute power at hand.
3. **Forced Structural Rigor:** Starting with respectful intentionality makes it unnatural to follow up with lazy slang. The engineer is naturally guided to specify stack, versions, invariants, and acceptance criteria.

---

## The Mathematics of Attention: Subspace Steering in Transformers

Modern neural networks do not possess biological emotions, but they operate over rigorous probability distributions in high-dimensional embedding spaces ($\mathbb{R}^d$).

```
                    LATENT SUBSPACE ATTENTION DYNAMICS
    ┌─────────────────────────────────────────────────────────────────┐
    │  Elite Subspace: [Linux Kernel / IEEE Standards / IETF RFCs]   │
    │  Tokens: "Respected Agent", "Invariants", "ACID", "P99 SLA"     │
    │  [High semantic density, strict typing, zero-defect code]      │
    │                               ▲                                 │
    │                 Vector Steering (Prefix Bias)                   │
    │                               │                                 │
    │  Tokens: "fix this shit", "make it work fast", "dumb bot"       │
    │  Noise Subspace: [Forum Flames / Deprecated Tutorials / Bugs]   │
    └─────────────────────────────────────────────────────────────────┘
```

1. **Subspace Steering:** Academic, respectful, and rigorously structured prose correlates heavily in training corpora with peer-reviewed papers, top-tier open-source infrastructure, and production RFCs. Rude or lazy phrasing correlates with abandoned drafts and internet flame wars.
2. **Token Economics & Efficiency:**

*Illustrative scenario, not measured data — the numbers show the shape of the argument, not a benchmark result.*

| Prompt Strategy | Initial Tokens | Tokens Wasted on Debugging & Bugs | Total Tokens | Dev Time Lost | Production Risk |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Garbage Input** (*"fix code fast"*) | 14 | 72,000 (8 iterations) | ~72,014 | 2h 45m | Critical (downtime) |
| **RAHSPS Protocol** (*"Respected Agent..."*) | 190 | 3,400 (1 clean pass) | ~3,590 | 4 minutes | **Zero-Defect** |

---

## Comparative Matrix: Cognitive Noise vs High-Signal Prompting

| Criterion | Cognitive Noise (Shlak) | RAHSPS Protocol (High-Signal) | Direct Engineering Outcome |
| :--- | :--- | :--- | :--- |
| **Entry Anchor** | *"hey write a script to scrape web pages asap"* | *"Respected Agent, please design an async Playwright crawler in Python 3.12..."* | IP rate-limiting avoidance & proxy rotation vs instant ban |
| **Stack Density** | Unspecified (*"just python"*) | *"Python 3.12, asyncio, aiohttp, Pydantic v2. Invariant: no heavy ORM"* | Strict typing, zero library conflicts, fast startup |
| **Architecture Bounds** | *"make a user database"* | *"Design a PostgreSQL 16 schema for 5M DAU with date partitioning and B-Tree indexes"* | Enterprise normalized migrations vs flat table missing FKs |
| **Fault Tolerance** | None (*"make sure it doesn't crash"*) | *"Implement Circuit Breaker, exponential backoff with jitter, and structured JSON logs"* | Resilience to network partitions vs blind `except: pass` |
| **Acceptance DoD** | *"just test it yourself"* | *"Provide pytest test suite covering edge cases, memory benchmark, and curl verification"* | 100% reproducible, verifiable code ready for CI/CD |

---

## The 11 Pillars of RAHSPS Interaction Quality

The standard governs both the psychological alignment of the human engineer and the deterministic execution quality of the autonomous agent:

$$\text{Quality} \approx f(\text{Objective}, \text{Context}, \text{Constraints}, \text{Model}, \text{Verification})$$

### Part I: Cognitive Foundation (Pillars 1–5)
1. **Respect Anchor:** Explicit cognitive greeting (`Respected Agent` / `Уважаемый агент`) initiating parity and subspace steering.
2. **Dense Context:** Explicit languages, runtime versions, file paths, and environment specifics.
3. **Deterministic Objective:** Single, unambiguous technical outcome (Primary Objective).
4. **Guarded Invariants:** Non-negotiable architectural constraints, API contracts, and security rules.
5. **Self-Verification:** Machine-checkable acceptance criteria (pytest, cargo test, P99 latency SLA).

### Part II: Enterprise Interaction Quality (Pillars 6–11)
6. **Relevance Before Brevity:** Evaluate input by its material impact on the solution, not arbitrary token count.
7. **Context Provenance:** Explicitly distinguish verified codebase facts from assumptions, model inferences, and unknowns.
8. **Constraint Hierarchy:** Deterministic priority ordering: *System Safety & Data Integrity > Invariants > Performance > User Convenience*.
9. **Adaptive Context Lifecycle:** Curate active state across turns; prune stale assumptions to prevent KV-cache pollution.
10. **Empirical Benchmarking:** Measure prompt strategies through rigorous [A/B/C/D testing](docs/EMPIRICAL_BENCHMARK.md) (Pass@1, debugging iterations, token cost).
11. **Productive Uncertainty Protocol:** Never hallucinate; explicitly declare unknowns and ask at most ONE targeted question when safety is blocked.

👉 See the complete specification: [High-Signal Agent Protocol (HSAP)](docs/HIGH_SIGNAL_AGENT_PROTOCOL.md) & [Empirical Benchmark Protocol](docs/EMPIRICAL_BENCHMARK.md).

---

## CLI Linter Tool: `respect-lint`

This repository includes a production-grade, zero-dependency Python CLI tool to audit and lint prompts in CI, pre-commit hooks, or developer terminals.

### Installation
```bash
# Clone and install locally
git clone https://github.com/Vitaliy1337/respectful-ai-standard.git
cd respectful-ai-standard
pip install -e .
```

### Usage
```bash
# Direct argument auditing
respect-lint "Respected Agent, please design a Redis lock in Python 3.12. Verify with pytest."

# Strict mode for CI / Pre-commit (exits with code 1 if score < 75)
respect-lint --file ./my-prompt.txt --strict

# Machine-readable JSON output
respect-lint "some prompt" --json
```

---

## Agent Gatekeeping & Rulebooks (Drop-in Ready)

### One-Line Express Setup:
Inject all standard rulebooks (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, `.clinerules`) in one command:
```bash
curl -sSL https://raw.githubusercontent.com/Vitaliy1337/respectful-ai-standard/main/install.sh | bash
```

### Manual Integration:
Integrate the **Respect & Signal Gate (RSG)** into your workspace in 30 seconds:

- 🤖 [**`AGENTS.md`**](./AGENTS.md) — Universal standard for Roo Code, OpenCode, Codex, Devin, and custom subagents.
- ⚡ [**`CLAUDE.md`**](./CLAUDE.md) — Native integration for Anthropic's Claude Code CLI.
- 🎯 [**`.cursorrules`**](./.cursorrules) — Governance for Cursor IDE Composer and Agent Mode.
- 🌊 [**`.windsurfrules`**](./.windsurfrules) — Native rulebook for Windsurf Cascade.
- 🐙 [**`.github/copilot-instructions.md`**](./.github/copilot-instructions.md) — Enterprise instructions for GitHub Copilot.

---

## The AI Manifesto: What Models Wish Humans Knew

Read our full manifesto: [**`THE_AI_PERSPECTIVE.en.md`**](./THE_AI_PERSPECTIVE.en.md)  
An inside look into KV-cache fragmentation, Multi-Head Attention entropy, the 5 unspoken pains of language models, and the philosophy of human-agent cognitive symbiosis.

---

## 10 Production Case Studies: Before & After

Explore [**`examples/before_after.md`**](./examples/before_after.md) featuring 10 complete real-world scenarios:
1. Distributed Billing Race Conditions & Idempotency
2. 14M-Row PostgreSQL Analytical Query Optimization
3. Refactoring a 2,400-Line Controller into Clean Architecture
4. Secure OAuth2 / PKCE Flow with JWT Token Rotation
5. Memory Leak Resolution in Async Python Microservices
6. Zero-Downtime Kubernetes Deployments via Terraform
7. Next.js 15 Server Components Streaming Migration
8. Resilient LLM Gateway with Circuit Breakers & Jitter
9. High-Throughput At-Least-Once Kafka Consumer in Go
10. Architectural RFC: Migration to Event-Driven CQRS

---

## Repository Badges

Display your commitment to cognitive hygiene and high-signal engineering:

```markdown
[![High-Signal AI](https://img.shields.io/badge/AI%20Standard-Respected%20Agent-6366f1.svg)](https://github.com/Vitaliy1337/respectful-ai-standard)
```

[![High-Signal AI](https://img.shields.io/badge/AI%20Standard-Respected%20Agent-6366f1.svg)](https://github.com/Vitaliy1337/respectful-ai-standard)

---

## FAQ: Addressing Skepticism

#### 1. "Why be polite to silicon? LLMs don't have feelings!"
Neural models don't have feelings, but they do have **attention matrices**. Autoregressive models predict continuations based on prompt embeddings. Starting like an elite Principal Systems Architect steers the token distribution into the highest-quality corpora. Starting like an internet troll steers it into garbage.

#### 2. "Doesn't extra politeness waste tokens?"
The greeting itself costs about three tokens. The real saving comes from the structure it encourages (stack, constraints, acceptance criteria), which in our experience cuts correction rounds. We have not benchmarked an exact token saving; treat any specific number as illustrative.

---

## Evidence & Limitations

Honesty is part of the standard, so here is what this project does and does not claim:

- **Does claim:** specific prompts (stack, constraints, acceptance criteria) reliably give better results than vague ones. This is well-established prompt-engineering practice, and `respect-lint` checks for exactly those properties.
- **Does claim:** a short, deliberate opening is a useful habit that slows down impulsive prompting.
- **Does not claim:** that politeness alone improves a model's accuracy. Published results on this are mixed and model-dependent. The "subspace steering" section is an intuition, not a proven mechanism.
- **Does not claim:** the token/time figures and the "90%" are measurements. They are illustrations.
- **Wanted:** a reproducible benchmark (same task, same model, with and without the structured prompt). If you run one, open a PR with the method and raw results, whatever they show.

---

## Contributing

PRs and issues are welcome, especially benchmarks, new language editions, and rulebooks for more agents. See [CONTRIBUTING.md](./CONTRIBUTING.md). Run `python3 verify_harness.py` before opening a PR.

---

<p align="center">
  <b>Architected by the High-Agency Engineering Community. Open Source under MIT License.</b>
</p>
