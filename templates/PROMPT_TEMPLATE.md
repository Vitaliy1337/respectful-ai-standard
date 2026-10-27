# High-Signal Prompt Templates

> **"Copy these templates, supply your variables, and achieve deterministic first-pass execution."**

These templates are engineered under the **Respectful AI & High-Signal Prompting Standard (RAHSPS)**. They eliminate cognitive fatigue, prevent KV-cache pollution, and ensure sharp attention beam convergence across frontier models.

---

## 1. Universal High-Signal Template (Basic Engineering Tasks)

Use for daily implementation tasks (adding endpoints, data validation, API integration, CLI utilities).

```markdown
Respected Agent, please design and implement [task / component name].

### Context & Stack:
- Runtime & Environment: [e.g. Python 3.12 / Node.js 20 LTS / Go 1.22]
- Framework & Core Dependencies: [FastAPI, Pydantic v2, SQLAlchemy 2.0]
- Target Files: [src/api/v1/users.py, src/models/user.py]

### Primary Technical Objective:
1. [Precise requirement #1]
2. [Precise requirement #2]

### Invariants & Constraints:
- Do not modify existing public method signatures.
- Do not introduce new external third-party dependencies.
- Ensure strict static typing and defensive edge case handling.

### Definition of Done & Verification:
- Code compiles without linter warnings.
- Unit test suite provided covering both successful paths and edge case failures.
```

---

## 2. System Architecture & RFC Template (Distributed Systems & Core Engines)

Use for designing sub-systems, distributed databases, message queues, and microservices.

```markdown
Respected Agent, acting as Principal Systems Architect, design the architectural RFC for [subsystem name].

### Business Context & Target Workload:
- Problem Domain: [brief description of domain requirements]
- Workload Profile: [DAU, peak RPS, expected dataset volume]
- Availability Requirements (SLA/SLO): [99.95%, permissible RPO/RTO]

### Architectural Alternatives Under Review:
- Option A: [e.g. Synchronous gRPC with distributed sharded database]
- Option B: [e.g. Asynchronous Event-Driven pipeline via Apache Kafka]

### Required Report Sections:
1. Trade-off Analysis evaluating: latency, operational cost, maintenance complexity.
2. Architecture Diagram in Mermaid format (C4 Container / Sequence).
3. Data Consistency Model & Failure Handling Strategy (Circuit Breaker, Dead Letter Queue).
4. Phased Zero-Downtime Rollout Migration Plan.
```

---

## 3. Debugging & Incident Investigation Template (Root Cause Analysis)

Use for diagnosing race conditions, memory leaks, distributed deadlocks, and production anomalies.

```markdown
Respected Agent, localize and eliminate the critical defect in module [module name].

### Incident Symptoms:
- Actual Behavior: [e.g. Memory leak of 300MB/hour under load / thread deadlock]
- Expected Behavior: [Stable resource usage and responsive execution]
- Trigger Conditions: [Occurs only when concurrent websocket connections exceed 1,000]

### Attached Artifacts:
- Error Stack Trace (filtered):
  ```
  [attach 10-15 lines of relevant stack trace, stripping noise]
  ```
- Affected Code Segment:
  ```
  [function or class code segment]
  ```

### Task for Agent:
1. Perform Root Cause Analysis and identify the underlying physical reason for failure.
2. Provide a minimal, safe diff that fixes the root cause without masking side-effects.
3. Write a regression test that fails before the fix and passes cleanly after it.
```

---

## 4. Refactoring & Technical Debt Template (Clean Architecture & Performance)

Use for modularizing monoliths, decoupling spaghetti code, and optimizing critical execution paths.

```markdown
Respected Agent, perform a rigorous engineering refactoring of file [path/to/file].

### Current State:
- Problem: [high coupling / Single Responsibility violation / duplicate logic]
- Size: [e.g. 1,500 lines in a single class]
- Existing Test Coverage: [existing test suite details or noted absence]

### Refactoring Objectives:
1. Decouple domain business logic from infrastructure details (Ports & Adapters).
2. Replace hardcoded dependencies with interfaces and Dependency Injection.
3. Maintain 100% backward compatibility of all public API contracts.
4. Optimize critical execution paths for CPU and memory allocations.

### Output Format:
- Step-by-step migration plan.
- New interface definitions and decoupled component code.
- Verification demonstrating that public contracts remain unbroken.
```

---

## 5. Zero-Human-In-The-Loop Autonomous Harness Template (Never Stop Protocol)

Use for launching autonomous agents in continuous development loops without human intervention.

```markdown
Respected Agent, launch Zero-Human-In-The-Loop Autonomous Development Harness.

### Objective & Target Deliverable:
Architect, implement, test, and polish to production perfection [system/module name].

### Never Stop Protocol Rules:
- Do not ask for permissions between steps. Act as author, architect, code reviewer, and QA.
- Operate in an autonomous loop: Creation -> Automated Validation -> Self-Criticism -> Refinement -> Final Verification.
- Terminate only when all files and tests are verified and ready for git push.

### Required Artifacts:
1. Complete implementation source code with strict typing and error handling.
2. Automated test suite and validation script (`verify_harness.py` / `test_suite.py`).
3. Documentation and deployment instructions.

### Quality Invariants:
- 100% pass rate on all automated test suites.
- Zero stub placeholders, unfinished TODOs, or empty mocks.
```

---

## 6. Enterprise High-Signal Agent Protocol (HSAP Template & Semantic Anchor)

The canonical production template for software engineering, analytics, research, and multi-agent coordination.

```markdown
### HIGH-SIGNAL AGENT PROTOCOL (HSAP-v3.1)

**Communication Standard:** Maintain a respectful, direct, high-signal professional tone. Prioritize solution quality and invariant preservation over empty formalities.

**PRIMARY OBJECTIVE:**
[Formulate the single primary technical outcome and acceptance criteria.]

**CONTEXT & SOURCES OF TRUTH:**
- Current Environment: [Stack, files, paths, runtime version, reproducible context]
- Verified Facts: [Facts confirmed by repository state, test runs, or logs]
- Assumptions & Hypotheses: [Explicitly declared working hypotheses]
- Unknowns: [Parameters not yet present in context]

**NON-NEGOTIABLE INVARIANTS & CONSTRAINTS:**
- Priority Hierarchy: Security & Data Integrity > Architecture Invariants > Performance > Convenience
- Invariants: [Backwards compatibility, public API contracts, data models]
- Prohibited Actions: [No unapproved third-party packages, do not remove existing tests]

**EXECUTION STRATEGY:**
1. Inspect relevant code and verified facts before formulating hypotheses.
2. Localize root cause and key architectural risks.
3. Select the smallest reliable solution that satisfies the objective.
4. Verify results through automated test suite execution.

**PRODUCTIVE UNCERTAINTY PROTOCOL:**
- Never fabricate facts, non-existent library calls, or command outputs.
- If a missing detail critically blocks safe execution: ask exactly ONE targeted question.
- Otherwise: proceed with explicitly declared safe assumptions.

**DEFINITION OF DONE (DoD):**
- [Functional completion criteria]
- Verification Command: [pytest / cargo test / npm test / verify_harness.py]
```

---

## 7. Antipatterns: What Never to Write

| Low-Signal / Toxic Input (Shlak) | Why It Degrades Results | High-Signal Reformulation |
| :--- | :--- | :--- |
| *"make it run fast"* | Lacks measurable SLA / latency targets | *"Respected Agent, optimize the endpoint's P99 latency to < 25ms under 1,000 concurrent requests."* |
| *"everything broke fix it"* | Forces the model to guess failure branches | *"Respected Agent, investigate the `ConnectionResetError` stack trace in client.py..."* |
| *"whip up something quick"* | Activates shallow, unverified boilerplate | *"Respected Agent, create a minimal proof-of-concept (PoC) focusing on resilience and concurrency safety..."* |
| *"you are dumb why does it not work"* | Injects emotional entropy into the KV-cache | *"Respected Agent, a race condition was detected at line 42 in the auth handler. Let us trace the lock acquisition..."* |
