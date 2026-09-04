# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T14:43:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-04T14:43:00+08:00
>
> Purpose: 给新的 Human / Agent 一个短小的“现在在哪、为什么、从哪里继续”入口。它不替代 Issue、PR、Git history 或完整 Roadmap。

## 1. Project in one sentence

InteropAtlas 是一个开放、机器可读、可持续分析的 **Interoperability Solution Space（互操作方案空间）** 知识基础设施，用来连接标准、成熟先例、方法、实现、组织、能力、场景、关系、证据与开放缺口，并服务 Human 与 Agent 的发现、比较、组合、验证和改进。

## 2. Core invariants

- Evidence Before Assertion；
- Stable Identity 不能依赖文件路径、显示名称或单个 URL；
- Canonical State ≠ Generated View；
- Readable Projection ≠ Updatable Projection；
- Agent Output ≠ Canonical Fact；
- Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission；
- 高影响治理、Identity Merge/Split、破坏性迁移和稳定规范升级需要更高授权 / Review Gate；
- **Ordinary intake MUST NOT silently merge Canonical subjects.**

## 3. Phase status

```text
P1  Design Principles                    ✅ Completed
P2  Prior-art / standards research       ✅ Completed / #124 closed
P3  Current-state audit                  ✅ Completed / #126 closed
P4  Architecture / Roadmap reset         ✅ Completed / #127 closed
P5  Real-data experiments / intake stress test ✅ representative mainline complete
#134 Contribution-Ready Gate              ✅ PASS WITH BOUNDARIES / Owner confirmed
P6  Implementation + continuous intake   ← NOW / #129
```

P4 architecture drafts remain drafts; #134 did not implicitly stable-promote all of them or authorize destructive migration.

## 4. P5 gate result

#159 synthesized evidence from #137/#130/#132/#133/#136.

Owner decision at #134: **PASS WITH BOUNDARIES**.

Meaning:

- architecture survived representative real-data pressure without reversal；
- Candidate/preflight work can scale immediately；
- ordinary M0/M1 continuous intake may open in P6 once the minimum production safety path is operational；
- mass direct Canonical writes on P5 experiment fixtures remain prohibited；
- M2/M3, identity merge/split, destructive migration and stable/governance changes remain separately gated。

## 5. NOW — P6 Slice 0 / #145

Primary next task: **#145 — V1 Serialization / Validator minimal production loop**.

First production chain:

```text
#145 V1 Serialization / Validator minimal production loop ← NOW
├→ #146 Continuous Intake
├→ #147 Migration Cohort 1
├→ #148 Compare + Evidence Workspace
└→ #149 Agent structured read/query + Candidate Write
```

### #145 production safety path landed

Added / wired:

- `01_State/01_Objects/candidate-object.v1.schema.json`
- `01_State/03_Candidates/README.md`
- `02_Runtime/01_Engine/candidate_identity_validator.py`
- `02_Runtime/01_Engine/legacy_identity_adapter.py`
- `02_Runtime/01_Engine/test_candidate_identity_validator.py`
- `01_State/04_Acceptance_Events/acceptance-event.v1.schema.json`
- `01_State/04_Acceptance_Events/README.md`
- `02_Runtime/01_Engine/acceptance_event_validator.py`
- `02_Runtime/01_Engine/test_acceptance_event_validator.py`
- `.github/workflows/p6-v1-intake-validation.yml`
- main `machine_review.py` scans production Candidate carrier separately from Canonical objects and emits deterministic Candidate intake routes.

The Candidate contract distinguishes `new / duplicate / possible_duplicate / identity_risk / deferred` and hard-codes `merge_authorized: false` for ordinary Candidate validation.

Deterministic routes distinguish:

```text
review_required
        = unique/new Candidate may proceed to independent semantic review;
duplicate_existing
        = known duplicate routes to the existing Canonical subject, without merge;
identity_review_required
        = possible duplicate / identity risk must stop for identity review;
deferred
        = unresolved semantic/identity case remains deferred;
blocked_invalid_identity_state
        = declared identity state contradicts deterministic evidence.
```

**No machine route means Canonical acceptance.** The strongest ordinary machine result is `review_required`.

Acceptance Event minimally records `accepted / duplicate / deferred / rejected`, Candidate reference, machine route, independent reviewer, evidence basis, mutation impact/authority, decision time, and Canonical target when applicable. Identity-review/deferred routes cannot become ordinary-path acceptance; M2/M3 require non-ordinary authority and explicit approver.

### Full repository validation now exists

GitHub Actions workflow `P6 V1 Intake Validation` runs on the real repository and passed on commit `fee09adbe5b22af0381853b0a088186aabbe7dfb`.

Passed steps:

- Candidate identity safety tests — 6 tests / PASS；
- Acceptance boundary safety tests — 5 tests / PASS；
- Machine Review — `PASS + SEMANTIC REVIEW REQUIRED` with 0 deterministic errors；
- Graph validation — 0 reference issues；
- bootstrap compatibility query — PASS / expected deterministic output。

The previous local-container DNS limitation is no longer a blocker for full-repository evidence because GitHub Actions now provides the executable repository validation path.

### Real production Candidate batch

Three production Candidate records now exercise the key routes:

```text
p6-slice0-rfc9114
→ review_required

p6-slice0-bcp47-rfc5646
→ duplicate_existing

p6-slice0-iso27001-2022
→ identity_review_required
```

Machine Review observed exactly these three routes with 0 deterministic errors. The ISO item remains held for identity review; no merge/split was guessed.

**Resume Here:** complete independent semantic review / acceptance-event evidence for the ordinary RFC 9114 path and the duplicate disposition, keep ISO/IEC 27001:2022 held for identity review, then move #145 to Review and prepare #146 Continuous Intake. Do not count Agent self-check or CI as the independent reviewer.

## 6. When Agent intake can scale

Already safe to scale now:

- Candidate discovery；
- first-party source confirmation；
- identifier capture/normalization；
- evidence-gap discovery；
- preflight generation；
- possible-duplicate / identity-risk routing。

Broad production Canonical acceptance starts through **#146**, after #145 provides the minimum production serialization/validator + dedup/identity-risk + review/acceptance boundary.

## 7. Owner / higher gates that remain

Explicit Owner/Governance decision is still required for:

- identity merge/split where authority requires；
- destructive migration / Legacy retirement；
- material security/permission governance changes；
- stable specification/governance promotion；
- V1-only writer / Legacy retirement gates；
- material project definition/scope changes。

## 8. Where to read next

```text
AGENTS.md
→ PROJECT_STATE.md
→ #145
→ #134 decision
→ docs/p5-gate-evidence-synthesis-v1-draft.zh-CN.md
→ docs/p5-ordinary-intake-minimal-checklist-v1-draft.zh-CN.md
→ #146 after #145 minimum safety loop is usable
```
