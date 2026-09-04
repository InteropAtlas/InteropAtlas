# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T14:55:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: verification-evidence / Owner direction
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-04T14:55:00+08:00
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
- Identity Merge/Split、破坏性迁移、稳定规范升级和项目方向/权限边界变化需要更高 Gate；
- **Ordinary intake MUST NOT silently merge Canonical subjects.**
- Owner 管项目方向、重大边界和不可逆决策；可由确定性测试/Validator/CI充分验证且不改变这些边界的普通技术实现，不要求 Owner 做形式化技术签字。

## 3. P1–P6 meaning and status

P1–P6 是把早期 InteropAtlas 转向新 V1 方向的第一轮 Foundation 重构工程，不是整个项目生命周期，也不是只写计划。

```text
旧 InteropAtlas
    ↓
P1  Design Principles                         ✅ Completed
P2  Prior-art / standards research            ✅ Completed / #124
P3  Current-state audit                       ✅ Completed / #126
P4  V1 Architecture / Roadmap reset           ✅ Completed / #127
P5  Real-data experiments / intake stress     ✅ Mainline completed
#134 Contribution-Ready Gate                  ✅ PASS WITH BOUNDARIES
P6  V1 Implementation + Migration + Intake    ← NOW / #129
    ↓
V1 becomes the actual operating InteropAtlas
```

P1–P5 已经确定并压力测试新方向；**P6 的职责是把仓库实际改造成 V1，同时迁移旧资产并启动长期运行。**

## 4. P6 current mainline

#145 V1 Serialization / Validator minimal production loop is **Done / closed**.

It delivered production Candidate serialization, identity-safe validation, Acceptance Event boundary, conservative Legacy identity compatibility, executable GitHub Actions validation, and a representative production batch covering unique / duplicate / identity-risk routes.

Current P6 work now runs in parallel where safe:

```text
#146 Continuous Intake                         ← In Progress
#147 Migration Cohort 1                       ← NEXT / may start now
#148 Compare + Evidence Workspace             ← Ready after production substrate
#149 Agent structured access + Candidate Write← Ready after production substrate
```

The active zero-context video-industry intake Agent is a real #146 stress test. Experiment/audit baseline remains **2026-09-04 14:26 +08:00**; do not interrupt it merely for review work.

## 5. #146 Continuous Intake

Production ordinary intake safety lane is open:

```text
Candidate discovery / first-party evidence
→ production Candidate carrier
→ identifier + identity/dedup preflight
→ deterministic machine route
→ semantic decision / Acceptance Event
→ bounded Canonical mutation where authorized
```

Key rules:

- Candidate Pool is the queue; do not create one Issue per standard；
- bounded batches, public provenance, official/publisher-controlled sources preferred；
- duplicate points to existing Canonical subject; no silent merge；
- identity-risk / work-vs-edition / merge/split / equivalence / composite identity stop/escalate；
- M2/M3 and genuinely high-impact mutations do not enter ordinary fast lane；
- Candidate state does not enter Canonical graph/index；
- GitHub Actions `P6 V1 Intake Validation` is the executable production validation path。

## 6. Resume Here — P6 migration starts now

Continue **#146** as a live parallel intake lane, but do not wait for intake to finish.

Start **#147 Migration Cohort 1** now:

1. inventory Legacy Canonical objects；
2. select only low-ambiguity P5-proven lossless/normalization mappings；
3. preserve stable IA IDs by default；
4. dry-run first；
5. run schema / relation / graph / semantic-diff checks；
6. exclude and escalate any identity merge/split, work-vs-edition ambiguity, semantic promotion or hidden-loss case；
7. migrate a small first cohort and prove rollback/correction path；
8. record provenance and post-migration verification。

Do not redesign P1–P5 unless execution reveals a genuine contradiction with the Owner's V1 direction. Prefer implementation/migration over further planning.

## 7. Owner escalation boundary

Escalate to Owner only when execution materially changes:

- InteropAtlas project definition / V1 direction / scope；
- identity merge/split policy or a concrete irreversible identity decision；
- destructive migration / major deletion / Legacy retirement gate；
- material security or repository permission boundary；
- stable specification/governance promotion；
- formal release or other materially irreversible project decision。

Ordinary technical choices, implementation details and mechanically verifiable migrations should proceed without ceremonial Owner review.

## 8. Read next

```text
AGENTS.md
→ PROJECT_STATE.md
→ #146 for live intake
→ #147 for current migration work
→ docs/canonical-migration-architecture-v1-draft.zh-CN.md
→ #148 / #149 as parallel P6 lanes open
```
