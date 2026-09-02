# AGENTS.md — InteropAtlas Repository Instructions

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T12:43:20+08:00
Document Updated At: 2026-09-02T10:43:23+08:00
Metadata Backfilled At: 2026-09-02T10:49:00+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

This file is the repository-level Bootstrap / Router for AI / Agent contributors. It does **not** replace `README.md`, `PROJECT_STATE.md`, `CONTRIBUTING.md`, GitHub Issues / PRs, project governance, or domain Specifications.

The goal is simple:

> A new Agent should be able to enter this repository with no private chat history, understand where the project is, find the correct task context, and continue without asking a Human to reconstruct previous conversations.

## 1. Start mode

Choose the smallest reading path that is sufficient for the job.

### First visit / project understanding

Read in this order:

1. `PROJECT_STATE.md` — current phase, current main line, resume point and decision gates;
2. `README.md` — project purpose, architecture and scope summary;
3. `docs/interopatlas-definition-and-scope-v0.2.zh-CN.md` — project definition / scope;
4. the current Phase Plan referenced by `PROJECT_STATE.md`;
5. `CONTRIBUTING.md` — collaboration / review rules;
6. relevant Decision / Specification artifacts for the area being discussed.

You should then be able to explain:
- why InteropAtlas exists;
- what the current Foundation / Phase state is;
- the major invariants that must not be broken casually;
- what the current main work is;
- what requires explicit Human authorization.

### Assigned Issue / Work Item

Read in this order:

1. `PROJECT_STATE.md` to understand how the task fits the project main line;
2. the assigned GitHub Issue / Work Item;
3. latest Handoff / active PR for that Work Item, if any;
4. `CONTRIBUTING.md`;
5. `docs/collaboration-task-system-v0.1.zh-CN.md`;
6. the Issue's `Read First / Upstream Contracts`;
7. relevant Schema / Specification / Research files for the area being changed.

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
2. project Definition / Scope when direction matters;
3. the relevant Decision / Specification;
4. Work Item Scope / Non-goals / Acceptance Criteria;
5. known decision gates and unresolved risks.

A technically correct change can still be wrong for the current project direction.

## 2. Context ladder

Use progressive context loading instead of reading the entire repository into one context window:

```text
L0  AGENTS.md
        ↓
L1  PROJECT_STATE.md
        ↓
L2  README + Definition / Scope + current Phase Plan
        ↓
L3  Issue + PR + Handoff
        ↓
L4  relevant Specification / Schema / Research
        ↓
L5  Decision Artifacts + Git history
```

Read only the minimum sufficient context for a local task, but move upward for architecture, governance, Knowledge Model, Human Interface, migration, security, licensing, major review or project-direction work.

Full contract: `docs/agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`.

## 3. Source of truth

- `PROJECT_STATE.md` = project-level current checkpoint / resume index, not task details.
- GitHub Issue = default Work Item identity and task state.
- PR / Handoff = active delivery and task-continuation state.
- Canonical YAML objects and relations = knowledge facts.
- Schema / Specifications = contracts, not fact instances.
- Decision Artifacts = durable rationale for important project choices.
- Git history = authoritative change/event history.
- Generated website / Markdown / exports are views and MUST NOT become a second source of truth.
- Private chat memory, hidden Agent memory and transient Messages are **not** project state.

If two current-status artifacts conflict, inspect newer Git / merged PR / Issue evidence and repair the stale artifact before making a high-level direction decision.

## 4. Project invariants

Preserve these unless an explicitly authorized change is about changing them:

- `Adopt → Profile → Extend → Invent`;
- Evidence Before Assertion;
- Fact ≠ Assessment;
- Physical Storage ≠ Semantic Classification ≠ Index / View;
- stable identity must not depend on display name or physical path;
- Canonical State ≠ generated view;
- Agent-only hidden project state is not allowed;
- high-impact governance / destructive migration decisions require Human Maintainer authorization.

For repository-structure work also read:
- `docs/repository-structure-profile-v0.1.zh-CN.md`

For collaboration / task-system work also read:
- `docs/open-collaboration-profile-v0.1.zh-CN.md`

For provenance / contribution identity work also read:
- `docs/provenance-traceability-profile-v0.1.zh-CN.md`
- `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`

## 5. Task protocol

Do not autonomously start a `Draft` task as if it were `Ready`.

For `Ready` tasks follow:

`Ready → Claimed → In Progress → Review → Done`

with `Blocked / Handoff / Released` when needed.

Claims must be public and time-limited. During the Pilot, the default initial lease review window is 72 hours unless the Work Item specifies otherwise.

Use the Claim and Handoff formats in `CONTRIBUTING.md`.

## 6. Scope discipline

- Follow the Work Item's Scope and Non-goals.
- Do not expand a task merely because adjacent cleanup is convenient.
- If a new modeling problem, broken assumption, or unrelated defect is found, record it in the current Issue and create / request a follow-up Work Item when appropriate.
- Do not invent facts to satisfy a Schema. If the current model cannot represent reality accurately, record a Model / Intake Gap.
- Do not silently cross a Human decision gate listed in `PROJECT_STATE.md`.

## 7. Research and evidence

- Prefer authoritative first-party sources.
- Preserve the identity and publication status of standards accurately.
- Keep Fact and Assessment separate.
- `Seed References` are starting points, not a closed whitelist.
- Perform the Work Item's `Freshness / Completeness Check`.
- New useful standards / mature prior art discovered during project work should enter the Atlas or become an explicit Intake follow-up when the model is not ready.
- Do not copy protected standards text beyond redistribution rights; store identity, official source, concise original summaries, and IA assessments instead.

## 8. Repository editing

- Preserve stable object IDs unless the Work Item explicitly authorizes an identity migration.
- Avoid large directory moves unless the task explicitly covers migration and its invariants.
- Do not create Agent-only project state directories.
- Do not edit generated outputs as canonical inputs.
- Prefer small, reviewable changes and a Pull Request for completed Work Items.
- Do not update `PROJECT_STATE.md` for every small change. Update it only when project-level phase, main line, resume point, decision gate or major milestone changes.

## 9. Validation

For changes affecting Canonical data, relations, schemas or the engine, run the relevant deterministic checks when the environment permits. Current Runtime paths are under `02_Runtime/01_Engine/`.

Typical checks include:

```bash
pip install -r 02_Runtime/01_Engine/requirements.txt
python 02_Runtime/01_Engine/graph_index.py
python 02_Runtime/01_Engine/bootstrap_query.py --capability automated_build_deployment
python 02_Runtime/01_Engine/machine_review.py
```

For renderer-related changes, exercise the relevant semantic renderer / representative pages and the browser E2E suite when applicable.

Do not copy old `engine/...` commands from pre-migration artifacts without checking current paths.

Record what was run and the result in the PR. CI output is evidence, not an independent reviewer.

## 10. Context exhaustion / handoff

If the current Agent session is ending while work is incomplete, do not leave the recoverable state only in the chat response.

At task level, write / update the public Handoff with:

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

If the work changed the project-level main line, Gate state, next resume point or a major decision gate, also update `PROJECT_STATE.md`.

A new Agent should be able to continue from repository state alone.

## 11. Review and authorization

Executor self-check is not independent review.

`normal` tasks SHOULD receive review from a different Human or Agent.

`high-impact` changes require Human Maintainer final authorization, including project scope, governance / collaboration rules, destructive Schema changes, license / security policy, stable Specification promotion, main-branch protection / rulesets, large Canonical Data deletion, formal releases and other explicitly marked decision gates.

## 12. Agent transparency

Record execution mode as `human`, `agent`, or `mixed` and follow `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`.

The core contribution roles are Initiator / Executor / Reviewer. GitHub Actor is platform provenance and must be recorded separately when it differs from the actual Executor. Governance Approver is recorded only when a high-impact authorization is required.

These instructions are vendor-neutral. Do not assume ChatGPT, Codex, Claude, Copilot, Gemini or any other product is the only supported execution environment.

Do not create multiple vendor-specific copies of project state. If a vendor-specific bootstrap file is added later, it should be a thin adapter to these repository sources of truth.
