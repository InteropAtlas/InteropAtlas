# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-05T03:51:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-05T03:51:00+08:00
>
> Purpose: 给新的 Human / Agent 一个短小的“现在在哪、为什么、从哪里继续”入口。它不替代 Master Design、Issue、PR、Git history 或完整 Roadmap。

## 1. Project in one sentence

InteropAtlas 是一个面向全人类的、开放、机器可读、可持续分析与演化的 **Interoperability Solution Space（互操作方案空间）公共知识基础设施**，连接标准、成熟先例、方法、实现、组织、能力、场景、关系、证据与开放缺口，并服务 Human 与 Agent 的发现、比较、组合、验证、使用和持续改进。

长期方向以 [`docs/interopatlas-master-design.zh-CN.md`](/docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md) 为上位设计基线。

## 2. Long-term orientation — do not reduce IA to the current phase

InteropAtlas is **Atlas-first**, not Human-first or Agent-first.

核心产品哲学压缩为一个相互依存的命题：

> **Knowledge belongs to the commons. Perspective belongs to the individual.**

其动态展开是知识流动模型（Knowledge Flow Model）：

```text
Discover → Connect → Transmit → Transform → Reuse → Create → Commons ↺
```

发现与连接偏向公共知识世界的形成；传递与转化承担跨主体、系统、时间、媒介与认知边界的桥接；复用与创造让知识进入具体任务，并把新的成果重新送回 Commons。

长期形态区分 Public Knowledge Commons、Personal Knowledge Space 与 Experience / Workspace。Personalization 可以改变注意力、选择、排序和表达，但不能静默改变公共 Canonical facts；个性化必须保持透明、可控、可逆。

这些长期方向不等于已授权的当前 Work Item。实时施工仍遵守下面的 P6 状态和 Issue Gate。

## 3. Core invariants

- Evidence Before Assertion；
- Stable Identity 不能依赖文件路径、显示名称或单个 URL；
- Canonical State ≠ Generated View；
- Readable Projection ≠ Updatable Projection；
- Agent Output ≠ Canonical Fact；
- Public Canonical Knowledge ≠ Personal State / Perspective；
- Human 与 Agent 共享同一 Canonical knowledge world；
- Personalization 应透明、可控、可逆，并允许回到公共 Atlas；
- Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission；
- Identity Merge/Split、破坏性迁移、稳定规范升级和项目方向/权限边界变化需要更高 Gate；
- **Ordinary intake MUST NOT silently merge Canonical subjects.**
- Owner 管项目方向、重大边界和不可逆决策；可由确定性测试/Validator/CI充分验证且不改变这些边界的普通技术实现，不要求 Owner 做形式化技术签字。
- Living Document 路径保持稳定，内容版本历史由 Git / tag / release / provenance 承担；只有协议、Schema、标准身份、兼容契约或历史制品需要把版本号保留在文件名中。

## 4. P1–P6 meaning and status

P1–P6 是 2026-09-02 总体设计升级后，把早期 InteropAtlas 转向新 V1 方向的第一轮 **Foundation / Architecture Revalidation Cycle**，不是整个项目生命周期。

```text
旧 InteropAtlas / Reference Implementation model
    ↓
P1  Design Principles                         ✅ Completed
P2  Prior-art / standards research            ✅ Completed / #124
P3  Current-state audit                       ✅ Completed / #126
P4  V1 Architecture / Roadmap reset           ✅ Completed / #127
P5  Real-data experiments / intake stress     ✅ Mainline completed
#134 Contribution-Ready Gate                  ✅ PASS WITH BOUNDARIES
P6  V1 Implementation + Migration + Intake    ← NOW / #129
    ↓
V1 becomes an operating foundation
    ↓
Long-term Atlas growth / Workspace / Personalization / Human+Agent evolution
```

P1–P5 已经确定并压力测试新方向；**P6 的职责是把仓库实际改造成 V1，同时迁移旧资产并启动长期运行。P6 完成不等于 InteropAtlas 完成。**

长期 Roadmap：`docs/interopatlas-long-term-roadmap.zh-CN.md`。

## 5. P6 current mainline

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

Repository event continuation infrastructure is active via `.github/workflows/agent-continuation-bridge.yml`. It is task-continuation infrastructure, not Reviewer or Canonical acceptance authority.

## 6. #146 Continuous Intake

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

## 7. Resume Here — current construction work

The Master Design restoration does **not** automatically promote future product directions into P6 work.

Do not reopen #147 or #148 merely to accumulate more work; both completed their bounded first-slice objectives.

Continue **#146** as a live parallel intake lane.

For the next ChatGPT / GPT-5.6 Sol mainline:

1. inspect #149 `P6 Agent Access Slice 1` against its now-satisfied technical prerequisites；
2. **do not autonomously treat it as Ready while the Issue remains `Draft / Future` and `Review Class: high-impact`**；
3. once explicitly promoted/authorized, implement only Structured Read / Query / Traverse + Candidate Write, preserving least privilege and Candidate→Validation→Acceptance；
4. do not grant unrestricted Canonical acceptance, Agent self-approval of M2/M3, or identity merge/split authority；
5. Personal Knowledge Space, recommendation, dynamic personalization, Simulation/Game and MATCH are long-term directions, **not implicitly authorized by this document**；
6. later Relation / Evidence / Lifecycle migration belongs to dedicated P6 Work Items rather than expanding #147 indefinitely。

## 8. Owner escalation boundary

Escalate to Owner when execution materially changes:

- InteropAtlas project definition / Master Design / V1 direction / scope；
- Public Canonical ↔ Personal State / privacy boundary；
- identity merge/split policy or irreversible identity decision；
- destructive migration / major deletion / Legacy retirement gate；
- material security or repository permission boundary；
- stable specification/governance promotion；
- formal release or other materially irreversible project decision；
- promotion of a still-`Draft / Future` high-impact task when AGENTS.md prohibits silently starting it as Ready。

Ordinary technical choices, implementation details and mechanically verifiable migrations should proceed without ceremonial Owner review.

## 9. Read next

### Understand the project

```text
README.md
→ docs/interopatlas-master-design.zh-CN.md
→ docs/knowledge-philosophy-and-principles.zh-CN.md
→ docs/public-commons-and-personal-knowledge-space.zh-CN.md
→ docs/interopatlas-long-term-roadmap.zh-CN.md
```

### Resume current P6 construction

```text
AGENTS.md
→ PROJECT_STATE.md
→ #146 for live intake
→ #149 for the next Agent Access slice after explicit Ready/promotion
→ docs/canonical-write-intake-contract-architecture-draft.zh-CN.md
```
