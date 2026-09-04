# AGENTS.md — InteropAtlas Repository Instructions

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T12:43:20+08:00
Document Updated At: 2026-09-04T23:50:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

This file is the repository-level Bootstrap / Router for AI / Agent contributors. It does **not** replace `README.md`, `PROJECT_STATE.md`, the Master Design, `CONTRIBUTING.md`, GitHub Issues / PRs, governance, or domain Specifications.

The goal:

> A new Agent should be able to enter this repository with no private chat history, understand both the long-term project and the current construction phase, and continue without asking a Human to reconstruct previous conversations.

## 1. Do not confuse project layers

InteropAtlas has multiple design scales:

```text
L0  Mission / Philosophy
L1  Master Design
L2  Architecture / Long-term Directions
L3  Operating & Evolution Model
L4  Foundation / Phase Roadmap
L5  Contracts / Specifications / Profiles
L6  Issues / PRs / Implementation
```

**P1–P6 is the first V1 Foundation / Architecture Revalidation Cycle, not the whole project lifecycle.**

The long-term project is Atlas-first: a public interoperability knowledge commons with multiple Human / Agent access modes, evolving Perspective / Projection / Workspace forms, and a long-term Personal Knowledge Space direction. Do not reduce the project to the current website, current P6 work, the historical five-route model, or one Workspace.

## 2. Start mode

Choose the smallest reading path sufficient for the job.

### First visit / project understanding

Read in this order:

1. `PROJECT_STATE.md` — current phase, main line, resume point and gates;
2. `README.md` — concise project entry;
3. `docs/interopatlas-master-design-v1.0.zh-CN.md` — long-term Master Design and layer model;
4. `docs/interopatlas-definition-and-scope-v0.2.zh-CN.md` — definition / scope;
5. the current Phase Plan / Issue referenced by `PROJECT_STATE.md`;
6. `CONTRIBUTING.md` — collaboration / review rules;
7. relevant Architecture / Specification / Research artifacts.

For product philosophy, Personal Knowledge Space, Perspective / Projection / Workspace, Human+Agent shared knowledge or long-term roadmap questions, also read as relevant:

- `docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md`;
- `docs/public-commons-and-personal-knowledge-space-v0.1.zh-CN.md`;
- `docs/knowledge-workspace-design-principles-v1.0.zh-CN.md`;
- `docs/interopatlas-long-term-roadmap-v1.0.zh-CN.md`.

You should then be able to explain:
- why InteropAtlas exists and whom it serves;
- why the project is Atlas-first rather than Human-first or Agent-first;
- the difference between Public Canonical Knowledge, Personal Perspective and Representation / Workspace;
- what the current Foundation / Phase state is;
- why P1–P6 is only one bounded reconstruction cycle;
- the major invariants that must not be broken casually;
- what requires explicit Human authorization.

### Assigned Issue / Work Item

Read in this order:

1. `PROJECT_STATE.md` to understand how the task fits the current main line;
2. the assigned GitHub Issue / Work Item;
3. latest Handoff / active PR, if any;
4. `CONTRIBUTING.md`;
5. `docs/collaboration-task-system-v0.1.zh-CN.md`;
6. the Issue's `Read First / Upstream Contracts`;
7. relevant Schema / Specification / Research files.

If the task may change project philosophy, public/personal boundary, Canonical truth model, long-term product direction or major architecture, move back up the ladder and read the Master Design before acting.

### User says only “continue” / “继续”

Do **not** guess from private chat memory.

1. Read `PROJECT_STATE.md`;
2. check its `Verified At` and inspect newer main commits / merged PRs / Issue state if they may have changed the main direction;
3. verify the first unfinished item under `Resume Here`;
4. resume existing In Progress / Review work before starting a parallel replacement;
5. update `PROJECT_STATE.md` if the real project state has moved on.

### Review / Audit

Do not review only the local Diff. Also read:

1. `PROJECT_STATE.md`;
2. Master Design / Definition when direction matters;
3. relevant Decision / Specification;
4. Work Item Scope / Non-goals / Acceptance Criteria;
5. known gates and unresolved risks.

A technically correct change can still be wrong for the current project direction.

## 3. Context ladder

```text
L0  AGENTS.md
        ↓
L1  PROJECT_STATE.md
        ↓
L2  README + Master Design + Definition / Scope
        ↓
L3  current Phase / Issue + PR + Handoff
        ↓
L4  relevant Specification / Schema / Research
        ↓
L5  Decision Artifacts + Git history
```

Use progressive context loading. Move upward for architecture, governance, Knowledge Model, Personalization, Human Interface, migration, security, licensing, major review or project-direction work.

Full contract: `docs/agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`.

## 4. Source of truth

- Master Design = current long-term project direction and layer relationships, not live task status.
- `PROJECT_STATE.md` = project-level current checkpoint / resume index, not task details.
- GitHub Issue = default Work Item identity and task state.
- PR / Handoff = active delivery and task-continuation state.
- Canonical YAML objects and relations = knowledge facts.
- Schema / Specifications = contracts, not fact instances.
- Decision Artifacts = durable rationale for important choices.
- Git history = authoritative change/event history.
- Generated website / Markdown / exports are views and MUST NOT become a second source of truth.
- Personal Perspective / user state MUST NOT silently become Public Canonical Knowledge.
- Private chat memory, hidden Agent memory and transient Messages are **not** project state.

If current-status artifacts conflict, inspect newer Git / merged PR / Issue evidence and repair the stale artifact before making a high-level direction decision.

## 5. Project invariants

Preserve these unless an explicitly authorized change is about changing them:

- `Adopt → Profile → Extend → Invent`;
- Evidence Before Assertion;
- Fact ≠ Assessment;
- Physical Storage ≠ Semantic Classification ≠ Index / View;
- stable identity must not depend on display name or physical path;
- Canonical State ≠ generated view;
- **Knowledge belongs to the commons; Perspective belongs to the individual**;
- personalization changes selection / emphasis / representation, not Public Canonical facts;
- personalization should remain transparent and reversible;
- Human and Agent share one Canonical knowledge world;
- Agent-only hidden project state is not allowed;
- real use should be allowed to expose model gaps before ontology expansion;
- high-impact governance / destructive migration / project-direction decisions require Human Maintainer authorization.

For repository structure read `docs/repository-structure-profile-v0.1.zh-CN.md`.
For collaboration read `docs/open-collaboration-profile-v0.1.zh-CN.md`.
For provenance read `docs/provenance-traceability-profile-v0.1.zh-CN.md` and `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`.

## 6. Task protocol

Do not autonomously start a `Draft` task as if it were `Ready`.

For `Ready` tasks follow:

`Ready → Claimed → In Progress → Review → Done`

with `Blocked / Handoff / Released` when needed.

Claims must be public and time-limited. During the Pilot, the default initial lease review window is 72 hours unless the Work Item specifies otherwise.

Use Claim / Handoff formats in `CONTRIBUTING.md`.

## 7. Scope discipline

- Follow Work Item Scope and Non-goals.
- Do not implement a long-term Master Design direction merely because it appears in the roadmap; it must enter an authorized Work Item.
- Do not expand a task merely because adjacent cleanup is convenient.
- Record newly discovered modeling problems / broken assumptions / unrelated defects as follow-up work.
- Do not invent facts to satisfy a Schema. Record a Model / Intake Gap when reality cannot be represented accurately.
- Do not silently cross a Human decision gate listed in `PROJECT_STATE.md`.

## 8. Research and evidence

- Prefer authoritative first-party sources.
- Preserve standards identity and publication status accurately.
- Keep Fact and Assessment separate.
- `Seed References` are starting points, not a whitelist.
- Perform the Work Item's Freshness / Completeness Check.
- Useful standards / prior art discovered during work should enter the Atlas or an explicit Intake follow-up when the model is not ready.
- Do not copy protected standards text beyond redistribution rights.
- Research should seek validation, correction and cognitive gain; do not select evidence merely to prove current IA ideas.

## 9. Repository editing

- Preserve stable object IDs unless explicitly authorized otherwise.
- Avoid large directory moves unless the task covers migration and invariants.
- Do not create Agent-only project state directories.
- Do not edit generated outputs as canonical inputs.
- Prefer small, reviewable changes and a Pull Request for completed Work Items.
- Do not update `PROJECT_STATE.md` for every small change; update only project-level phase, main line, resume point, decision gate or major milestone changes.
- Durable design belongs in a small number of clearly layered documents. Do not recreate design fragmentation through redundant checkpoint files.
- Historical design documents with independent value should normally be marked historical/superseded rather than deleted merely for tidiness.

## 10. Language and terminology

InteropAtlas separates **reading language** from **concept identity**. Agents editing documentation MUST follow `docs/language-policy.zh-CN.md` and `docs/terminology-registry-v0.1.md`.

For Chinese documents:

- write natural Simplified Chinese as the primary reading language;
- when a core IA concept first appears, prefer `中文首选术语（Canonical English Term）`;
- after the concept is established, use natural Chinese without mechanically repeating English;
- put the Chinese preferred term first — do **not** write `English Term（中文翻译）` as the default Chinese prose pattern;
- preserve official names, protocol names, standard identifiers, trademarks, licenses, API names, code identifiers and other established technical identities when translation would reduce precision;
- do not translate machine identifiers merely for visual consistency;
- do not create a new concept simply because a different translation sounds better; register aliases or update the terminology registry explicitly;
- use the terminology registry's preferred Chinese term by default, while allowing registered context-sensitive aliases where their distinction matters.

Current examples include:

```text
规范知识（Canonical Knowledge）
视角（Perspective）
投影（Projection）
表达（Representation）
工作空间（Workspace）
公共知识共同体（Public Knowledge Commons）
个人知识空间（Personal Knowledge Space）
互操作方案空间（Interoperability Solution Space）
成熟先例（Prior Art）
来源追踪（Provenance）
地图优先（Atlas-first）
```

English parallel documents should read as natural English, not as sentence-by-sentence mirrors of Chinese. Translation MUST preserve concept identity, design status, uncertainty, normative strength and source meaning. Missing translation is a visible localization backlog; it is not by itself a reason to block valid knowledge intake.

If a Chinese source document changes substantively, check whether an English parallel document exists and whether its translation provenance / semantic synchronization has become stale. Do not silently claim that translations are synchronized when they are not.

## 11. Validation

For changes affecting Canonical data, relations, schemas or engine, run relevant deterministic checks when environment permits. Current Runtime paths are under `02_Runtime/01_Engine/`.

Typical checks:

```bash
pip install -r 02_Runtime/01_Engine/requirements.txt
python 02_Runtime/01_Engine/graph_index.py
python 02_Runtime/01_Engine/bootstrap_query.py --capability automated_build_deployment
python 02_Runtime/01_Engine/machine_review.py
```

For renderer changes, exercise representative semantic renderer pages and browser E2E when applicable.

Record validation in the PR. CI is evidence, not an independent reviewer.

## 12. Context exhaustion / handoff

If a session ends while work is incomplete, do not leave recoverable state only in chat.

At task level record:

```text
Status:
Completed:
Artifacts / commits / PRs:
Validated:
Remaining:
Blockers / open questions:
Recommended next action:
Current branch / PR / commit:
```

If work changed project-level main line, Gate, resume point or major decision, update `PROJECT_STATE.md`.

## 13. Review and authorization

Executor self-check is not independent review.

`normal` tasks SHOULD receive review from a different Human or Agent.

`high-impact` changes require Human Maintainer final authorization, including project scope / philosophy, governance / collaboration rules, destructive Schema changes, license / security policy, stable Specification promotion, major Personal/Public data boundary changes, main-branch protection, large Canonical deletion, formal releases and other explicit gates.

## 14. Agent transparency

Record execution mode as `human`, `agent`, or `mixed` and follow `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`.

Core contribution roles are Initiator / Executor / Reviewer. GitHub Actor is platform provenance and must be recorded separately when it differs from actual Executor. Governance Approver is recorded only when high-impact authorization is required.

These instructions are vendor-neutral. Do not assume ChatGPT, Codex, Claude, Copilot, Gemini or another product is the only supported environment.
