# AGENTS.md — InteropAtlas Repository Instructions

This file contains repository-specific instructions for AI / Agent contributors. It does **not** replace `README.md`, `CONTRIBUTING.md`, project governance, Issues, or Specifications.

## Read first

Before starting repository work, read in this order:

1. the assigned GitHub Issue / Work Item;
2. `CONTRIBUTING.md`;
3. `docs/collaboration-task-system-v0.1.zh-CN.md`;
4. the Issue's `Read First / Upstream Contracts`;
5. relevant Schema / Specification files for the area being changed.

For repository-structure work also read:
- `docs/repository-structure-profile-v0.1.zh-CN.md`

For collaboration / task-system work also read:
- `docs/open-collaboration-profile-v0.1.zh-CN.md`

## Source of truth

- GitHub Issue = default Work Item identity.
- Canonical YAML objects and relations = knowledge facts.
- Schema / Specifications = contracts, not fact instances.
- Generated website / Markdown / exports are views and MUST NOT become a second source of truth.
- Private chat memory is not project state. Durable context belongs in Issue / PR / repository artifacts.

## Task protocol

Do not autonomously start a `Draft` task as if it were `Ready`.

For `Ready` tasks follow:

`Ready → Claimed → In Progress → Review → Done`

with `Blocked / Handoff / Released` when needed.

Claims must be public and time-limited. During the Pilot, the default initial lease review window is 72 hours unless the Work Item specifies otherwise.

Use the Claim and Handoff formats in `CONTRIBUTING.md`.

## Scope discipline

- Follow the Work Item's Scope and Non-goals.
- Do not expand a task merely because adjacent cleanup is convenient.
- If a new modeling problem, broken assumption, or unrelated defect is found, record it in the current Issue and create / request a follow-up Work Item when appropriate.
- Do not invent facts to satisfy a Schema. If the current model cannot represent reality accurately, record a Model / Intake Gap.

## Research and evidence

- Prefer authoritative first-party sources.
- Preserve the identity and publication status of standards accurately.
- Keep Fact and Assessment separate.
- `Seed References` are starting points, not a closed whitelist.
- Perform the Work Item's `Freshness / Completeness Check`.
- Do not copy protected standards text beyond what redistribution rights allow; store identity, official source, concise original summaries, and IA assessments instead.

## Repository editing

- Preserve stable object IDs unless the Work Item explicitly authorizes an identity migration.
- Avoid large directory moves unless the task explicitly covers migration and its invariants.
- Do not create Agent-only project state directories.
- Do not edit generated outputs as canonical inputs.
- Prefer small, reviewable changes and a Pull Request for completed Work Items.

## Validation

For changes affecting Canonical data, relations, schemas, or the engine, run the relevant deterministic checks when the environment permits:

```bash
pip install -r engine/requirements.txt
python engine/graph_index.py
python engine/bootstrap_query.py --capability automated_build_deployment
```

For renderer-related changes, also exercise representative rendering, for example:

```bash
python engine/render_markdown.py yaml_1.2.2 --output build/standards/yaml-1.2.2.md
```

Record what was run and the result in the PR. CI output is evidence, not an independent reviewer.

## Review and authorization

Executor self-check is not independent review.

`normal` tasks SHOULD receive review from a different Human or Agent.

`high-impact` changes require Human Maintainer final authorization, including project scope, governance / collaboration rules, destructive Schema changes, license / security policy, stable Specification promotion, main-branch protection / rulesets, large Canonical Data deletion, and formal releases.

## Agent transparency

Record execution mode as `human`, `agent`, or `mixed` in the Work Item / PR. Specific tool or model identity may be recorded but is not required for protocol compatibility.

These instructions are vendor-neutral. Do not assume ChatGPT, Codex, Claude, Copilot, or any other product is the only supported execution environment.
