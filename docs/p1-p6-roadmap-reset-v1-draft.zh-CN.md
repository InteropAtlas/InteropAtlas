# InteropAtlas P1–P6 Roadmap Reset v1 — Draft

<!-- InteropAtlas Document Metadata v0
Document Status: Architecture / Roadmap Draft
Document Created At: 2026-09-04T09:35:00+08:00
Metadata Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> Status: P4.6 Roadmap Draft. This document resets execution order after P1–P4. It does not stable-promote the P4 architecture drafts and does not authorize destructive migration or broad Canonical write access.

## 1. Why reset the roadmap

InteropAtlas 已完成从“Reference Implementation 功能建设”向“Canonical Contract + Intake + Migration + Workspace + Human/Agent Access”架构的转向。旧 `knowledge-workspace-phase-plan-v1.0` 中的 `NOW:P2` 属于历史执行断点，不再是当前路线 authority。

本 Roadmap 的目标不是增加另一套永久规划，而是把 P4.1–P4.5 的架构结论转换成可执行的 P5 真实数据实验、Contribution-Ready Gate 与 P6 渐进式生产实施。

核心原则：

> **Candidate discovery 可以现在规模化；bounded Canonical intake 在 P5 小批启动；broad ordinary Canonical intake 只在真实实验通过 Gate 后规模化。**

因此，项目不需要等到所有架构、迁移和前端全部完成才开始“收入标准”，也不能在 Contract 尚未经真实数据验证时直接 mass ingest。

## 2. Phase map

```text
P1 Design Principles                         ✅ Completed
        ↓
P2 Prior-art / Standards Research            ✅ Completed
        ↓
P3 Current-State Audit                       ✅ Completed
        ↓
P4 Architecture / Roadmap Reset              🟡 Closing
        ↓
P5 Real-data Experiments / Intake Stress     NEXT
        ↓              ↘
Contribution-Ready Gate   Candidate Discovery / Evidence / Inventory fast lanes
        ↓
P6 V1 Implementation + Continuous Intake
        ↓
Long-running operating loops: intake / migration / quality / workspace / governance
```

P6 不是“项目完成”。InteropAtlas 的知识空间会持续变化，因此最终状态是持续运营，而不是把所有标准一次性收完。

## 3. P4 exit

P4 已形成五个架构 draft：

1. Canonical Contract V1；
2. Canonical Write / Intake Contract；
3. Migration Architecture；
4. Selection / Projection / Workspace Architecture；
5. Human + Agent Access Architecture。

P4.6 的退出条件是：
- 有明确 P5 主实验链；
- 有可立即并行的 Candidate / research / inventory fast lane；
- 有 Contribution-Ready Gate；
- 有 P6 implementation order；
- 旧 backlog 已有 reclassification 入口；
- PROJECT_STATE 指向 P5，而不是旧页面功能路线。

P4 exit **不要求**：final field-level Schema、全量 migration、frontend rewrite、stable spec promotion、复杂 permission automation。

## 4. P5 — Real-data Experiments / Intake Stress Test

Primary umbrella: **#128**。

### 4.1 Critical path

```text
#137 Experiment Harness / V1-shaped fixtures
        ↓
#130 Identity / Version / Family-Kind Fit Test
        ↓
#132 Relation + Evidence/Assertion/Conflict + Lifecycle Fit Test
        ↓
#133 Migration + Workspace + Human/Agent Write-back E2E
        ├──────────────┐
        ↓              ↓
#136 Candidate→Canonical bounded Intake Stress Test
        ↓
#159 Gate Evidence Synthesis
        ↓
#134 Contribution-Ready Owner/Governance Gate
```

这不是要求所有 P5 Issue 串行完成。只有足以回答 Gate 的 representative evidence 位于 critical path。

Supporting experiments按发现触发，包括：#154 non-normative family/kind、#155 workspace 2×3、#156 review independence、#157 machine gate adequacy、#158 identity merge/split dry-run、#153 Architecture Decision Log。

### 4.2 Fast lanes — 现在即可并行

Fast Lane index: **#192**。

无需等待 #134 的安全工作包括：
- Candidate discovery / source confirmation / dedup；
- Evidence gap discovery；
- relation complexity inventory；
- lifecycle ambiguity inventory；
- identity/version ambiguity inventory；
- migration mapping inventory；
- Workspace current-asset audit；
- validator / graph baseline；
- Agent continuity / task readability validation；
- bounded non-destructive research / fixtures。

这些工作不允许越界到 mass Canonical write、identity merge/split、production Schema migration、stable governance promotion 或 destructive deletion。

### 4.3 Candidate Pool accelerator

#125 保留为历史入口，#131 是 P5 expansion umbrella。#140–#165 提供多个可并行 Candidate Discovery batches，按 publisher/domain/version/profile 等方向扩充。

Candidate Pool 的作用：
1. 让“收入标准”的发现阶段现在就开始扩张；
2. 为 P5 Fit Tests 提供真实样本；
3. 为 #136 首批 bounded Canonical intake 提供 backlog；
4. Gate 通过后直接转成 continuous intake queue。

**Candidate ≠ Canonical**。数量增长不代表 IA 已接受这些对象为 Canonical Fact。

### 4.4 Contribution-Ready Gate

Gate: **#134**，evidence synthesis: **#159**。

Gate 关注 ordinary M0/M1 intake 是否可重复、安全、可并行，而不是要求所有 M2/M3 问题都解决。

决策：
- `PASS` — broad ordinary intake 开放；
- `PASS WITH BOUNDARIES` — 只开放已验证 family/mutation types；
- `HOLD` — 存在会造成系统性返工/知识损坏的 blocker。

Gate 是 Human Owner / Governance decision。普通 P5 research/discovery 不需要 Owner 逐项批准。

## 5. “什么时候可以快速收入标准”

路线明确分三层：

### Level A — Candidate discovery：**现在**

可多 Human/Agent 并行发现、确认官方源、known identifier、粗分类、基础去重，进入 Candidate Pool。

### Level B — bounded Canonical intake：**P5**

#136 用 5–10 个真实候选跑完整 Intake；稳定后可扩大到 20–50 的实验 batch，但仍受 P5 validated scope 限制。

### Level C — broad continuous Canonical intake：**#134 Gate 通过后 / early P6**

#145 先落最小 production V1 serialization/validator，随后 #146 启动 Candidate Pool → bounded Intake Tasks。#167 用 4 个并行 Human/Agent batch 验证并发，再逐步扩张。

因此，“标准收录”与“架构建设”从 P5 开始并行，而不是等 P6 全部完成。

## 6. P6 — V1 Implementation + Continuous Intake

Primary umbrella: **#129**；navigation: **#194**。

第一轮生产链：

```text
#145 V1 Serialization / Validator minimal production loop
      ├→ #146 Continuous Intake
      ├→ #147 Migration Cohort 1
      ├→ #148 Compare + Evidence Workspace
      └→ #149 Agent structured read/query + Candidate Write
```

之后按真实压力扩张，而不是 monolithic rewrite。

### 6.1 Intake scaling

- #152 ordinary intake task template；
- #167 four-batch parallelism pilot；
- #229 first ~100 canonical intake review；
- #230 100→1,000 scale gate；
- #231 1,000+ operating model。

自动 task generator / queue / dedup index / source monitor 只有在手工流程出现重复摩擦后再做，避免 premature automation。

### 6.2 Migration

- low-ambiguity object cohorts first；
- binary relations remain binary when sufficient；
- explicit Assertion only where evidence/conflict/provenance needs justify it；
- lifecycle dimensions split progressively；
- semantic diff / loss report required；
- V1-only writer cutover before full Legacy reader retirement；
- final retirement needs #151 Human/Governance gate。

### 6.3 Workspaces

优先验证/实现 Compare + Evidence，再扩 Search/Browse/Object、Graph/Timeline。Workspace 消费 Selection/Projection contract；renderer 不建立第二份 truth。View 中发现的 correction 进入 Candidate Intake，而不是直接反写 projection。

### 6.4 Agent access

Agent 与 Human 使用同一 Canonical facts/evidence/identity/relation semantics，但 capability / authority / platform permission 分离。第一轮只要求 structured read/query + Candidate Write；unrestricted Canonical acceptance 不属于 Agent 默认能力。

### 6.5 Quality / coverage

Coverage、staleness、evidence debt、review capacity、migration debt 成为持续运营环。标准数量 ≠ solution-space coverage；Candidate coverage ≠ Canonical coverage；freshness ≠ truth。

## 7. Legacy work reclassification

#135 / #195 负责旧 backlog mapping / cleanup proposal。

原则：
- 保留有用代码、research、stable IDs、Git history；
- 旧 Engine/Validator/Graph 作为 implementation assets 复用；
- 旧 Compare/Explanation/Human Route 保留 product intent / interaction evidence；
- 旧 schema/curation/evidence research 作为 P5 inputs，不直接恢复旧模型；
- 旧 fixed page roadmap 不再决定优先级；
- #86 continuity、#122 Owner anchor、#125 Candidate Pool 继续保留；
- 不 mass-close，只有明确 completed/superseded 后再逐项处理。

## 8. Authority and stop conditions

### P5 autonomous

执行者可以自主进行 bounded research、Candidate discovery、fixtures、inventory、machine audits、普通 fit tests，并公开留痕。

### Must escalate

以下情况停止自动推进并请求适当 authority：
- identity merge/split/destructive mutation；
- stable specification/governance promotion；
- broad intake policy activation (#134)；
- permission/security model material change；
- Legacy writer/reader retirement；
- material project scope/definition change。

### Architecture mismatch

若 P5 发现 V1 draft 无法表达真实对象，不在单个 intake task 临时加字段。进入 #153 Decision Log / bounded Research Question，遵循 `Adopt → Profile → Extend → Invent`。

## 9. Public continuity

新的 Agent 不应依赖私人聊天历史。最低恢复路径：

```text
AGENTS.md
→ PROJECT_STATE.md
→ this roadmap
→ #128 P5 umbrella / #193 mainline index
→ #192 fast-lane index if parallel work is desired
```

#138 / #190 用 fresh takeover 验证这条路径。

## 10. Roadmap status semantics

- `Ready`：依赖满足，可认领；
- `Draft / Queued`：已有定义，但等待上游 evidence；
- `Draft / Future`：P6 backlog，不应现在执行；
- `Conditional Future`：只有出现明确 friction/need 才激活；
- `Gate`：需要明确 authority decision。

大量 Future Issues 的存在不是当前待办数量，也不代表应同时实施。它们用于让长期方向公开、可分工、可被 Agent 接手，同时由 Index / Blocked By 保持执行顺序。

## 11. Roadmap invariant

> **先把“可安全并行的工作”开放出来，再用真实反馈扩大 Canonical intake；不要把所有工作串行压在 Owner 或单一 Agent 上，也不要为了速度跳过 identity/evidence/review boundaries。**
