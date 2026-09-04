# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T17:58:00+08:00
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
> Verified At: 2026-09-04T17:58:00+08:00
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

#147 Migration Cohort 1 is **Done / closed**. It proved executable dry-run planning, rollback/correction, stable-ID preservation and multiple real low-ambiguity Class B Legacy→V1 additive migrations without hidden loss, identity merge/split or semantic promotion.

#148 Compare + Evidence Workspace Slice 1 is **Done / closed**. Production Human Compare and Evidence now consume an explicit shared Selection / Projection contract with recoverability, `not_recorded` semantics and read-only Projection boundaries.

Continuous P6 work now runs in parallel where safe:

```text
#146 Continuous Intake                         ← In Progress / parallel lane
#147 Migration Cohort 1                       ✅ Done
#148 Compare + Evidence Workspace             ✅ Done
#149 Agent structured access + Candidate Write← Draft / Future; prerequisites now materially satisfied, but not yet promoted to Ready
```

Repository event continuation infrastructure is also active via `.github/workflows/agent-continuation-bridge.yml`: required PR checks emit an idempotent continuation/repair signal and can optionally notify an external Agent/Harness webhook. This is task-continuation infrastructure, not Reviewer or Canonical acceptance authority.

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

## 6. Resume Here — close completed slices, then promote the next authorized lane

Do not reopen #147 or #148 merely to accumulate more work; both completed their bounded first-slice objectives.

Continue **#146** as a live parallel intake lane.

For the next ChatGPT / GPT-5.6 Sol mainline:

1. inspect #149 `P6 Agent Access Slice 1` against its now-satisfied technical prerequisites；
2. **do not autonomously treat it as Ready while the Issue itself remains `Draft / Future` and `Review Class: high-impact`**；
3. once the task is explicitly promoted/authorized, implement only Structured Read / Query / Traverse + Candidate Write, preserving least privilege and the existing Candidate→Validation→Acceptance boundary；
4. do not grant unrestricted Canonical acceptance, Agent self-approval of M2/M3, or identity merge/split authority；
5. later Relation / Evidence / Lifecycle migration belongs to their dedicated P6 Work Items rather than expanding #147 indefinitely。

## 7. Owner escalation boundary

Escalate to Owner only when execution materially changes:

- InteropAtlas project definition / V1 direction / scope；
- identity merge/split policy or a concrete irreversible identity decision；
- destructive migration / major deletion / Legacy retirement gate；
- material security or repository permission boundary；
- stable specification/governance promotion；
- formal release or other materially irreversible project decision；
- promotion of a still-`Draft / Future` high-impact task when AGENTS.md prohibits silently starting it as Ready。

Ordinary technical choices, implementation details and mechanically verifiable migrations should proceed without ceremonial Owner review.

## 8. Read next

```text
AGENTS.md
→ PROJECT_STATE.md
→ #146 for live intake
→ #149 for the next Agent Access slice after explicit Ready/promotion
→ docs/canonical-write-intake-contract-v1-architecture-draft.zh-CN.md
→ docs/canonical-human-agent-access-v1-architecture-draft.zh-CN.md
```
