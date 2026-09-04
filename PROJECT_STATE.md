# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T13:44:00+08:00
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
> Verified At: 2026-09-04T13:44:00+08:00
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

### #145 identity-safety checkpoint landed

Added / wired:

- `01_State/01_Objects/candidate-object.v1.schema.json`
- `01_State/03_Candidates/README.md`
- `02_Runtime/01_Engine/candidate_identity_validator.py`
- `02_Runtime/01_Engine/legacy_identity_adapter.py`
- `03_Evolution/04_Experiments/v1_contract_fixtures/candidate-identity-resolution-cases.fixture.yaml`
- main `machine_review.py` now scans production Candidate carrier separately from Canonical objects and reports Candidate review states.

The Candidate contract distinguishes:

```text
new
duplicate
possible_duplicate
identity_risk
deferred
```

and hard-codes `merge_authorized: false` for ordinary Candidate validation.

Safety behavior:

- known normalized identifier collision cannot silently remain `new`；
- duplicate must name an existing Canonical target；
- collisions against multiple Canonical subjects must defer/escalate；
- identity-risk/deferred states require reasons；
- Candidate review state is not Canonical acceptance；
- Machine Review PASS does not authorize semantic identity, merge or split；
- title/name/version similarity is not used as an automatic merge signal。

### Legacy compatibility

Existing V0 Canonical records often do not expose structured `external_identifiers`. #145 therefore uses a conservative Legacy Identity Adapter that only emits identifiers from deterministic publisher-controlled evidence. Initial supported adapter: RFC Editor official/info URL → `rfc:<number>`.

BCP 47 / RFC 5646 is the first known duplicate control: candidate `rfc:5646` can be matched to existing `bcp47_rfc5646` without guessing from title similarity.

### Validation caveat

The current execution container still cannot resolve `github.com`, so a fresh full checkout Machine Review could not be executed after wiring. No repository-level PASS is claimed. GitHub also reported no workflow run for the direct-main commit. The code/fixtures are landed but still require an executable checkout/CI validation before #145 can move to Review.

**Resume Here:** run/obtain executable validation for the new Candidate identity path, fix any integration errors, then add the minimal acceptance-boundary representation needed for an ordinary batch to reach review without performing automatic Canonical merge/write.

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
