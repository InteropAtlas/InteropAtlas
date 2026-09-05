# InteropAtlas 长期路线图（Long-term Roadmap）

<!-- InteropAtlas Document Metadata v0
Document Status: active long-term roadmap
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T18:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文描述长期方向，不是当前任务队列。当前主线只看 `PROJECT_STATE.md`；具体执行只看 GitHub 中真实处于 Ready / In Progress 的 Work Item。

## 1. 长期目标

InteropAtlas 要逐步成为：

> **一个面向全人类的开放互操作方案空间公共知识基础设施，让 Human 与 Agent 在同一知识世界上，通过公共或个人视角，把知识转化为适合当前任务和认知方式的可操作工作空间。**

核心结构：

```text
公共知识共同体
        +
机器可读 Canonical Knowledge
        +
持续收录 / Evidence / Provenance
        +
Human / Agent 共享访问
        +
Perspective / Selection
        +
Projection / Representation / Workspace
        +
Personal Knowledge Space
        +
真实使用驱动的持续反馈
```

## 2. 路线不是阶段流水线

InteropAtlas 不再用固定的项目版本号或 `P1 / P2 / P3 ...` 阶段编号描述长期路线。

历史建设周期只保留在 Git history、closed Issues 和 Evolution 中；现行路线按照“长期能力域 → 当前主线 → Work Item”推进。

项目长期运行更接近持续循环：

```text
知晓（KNOW）→ 使用（USE）→ 发现（DISCOVER）→ 贡献（CONTRIBUTE）
     ↑                                                   │
     └───────────────────────────────────────────────────┘

                         +
                    匹配（MATCH）
```

不存在“全部收录完成”这样的终点。

## 3. 长期能力域

### A. 知识地图覆盖与持续收录

持续扩大标准、成熟先例、方法、实现、组织、能力、场景和关系覆盖；维护 Candidate Pool、Evidence / Provenance、Freshness / Staleness、Identity / Dedup、Open Gap 和 Solution-space Coverage。

### B. 知识建模演化

用真实数据持续检验对象、关系、事件、范围、上下文、声明级证据与生命周期表达。只有现实证据证明有缺口时才扩展 Canonical Model。

### C. 知识操作空间

逐步发展 Browse、Object / Article、Timeline、Graph / Ecosystem、Compare、Evidence / Verification，以及未来可能出现的 Matrix、Map、Simulation、Interactive、Audiovisual、Game-like 等表达与工作空间。

### D. Human + Agent 共享操作

让 Human 与 Agent 在同一知识世界上进行结构化查询、遍历、证据检索、Candidate Write、Perspective / Workspace 操作和有边界的协作，不建立隐藏的 Agent-only truth。

### E. 个人知识空间

在公共知识之上形成 Personal State / Intent / Context、Personal Perspective、Attention / Representation Personalization、Privacy / Portability 和反信息茧房控制。

### F. 知识生命周期 / 知识代谢

区分 Validity、Freshness、Usage、Relevance、Historical Value、Authority 与 Lifecycle，形成归档、压缩、重新激活、Revalidation 和 Knowledge-maintenance Debt 管理能力。

### G. 匹配 / 发现 / 推荐

在公共知识和个人视角足够可靠之后，逐步研究 Problem ↔ Solution、Need ↔ Capability、Standard ↔ Implementation、Person ↔ Knowledge、互补方案、替代方案和 Gap。MATCH 必须可解释，不能把 Engagement 最大化当成目标。

### H. 开放生态与联邦化

长期支持第三方客户端、多 Agent、多种实现、可导出的个人视角 / Workspace State，以及在真实需求出现时支持 Federation / Alternative Backends。只有重复实践证明存在真实互操作缺口时，IA 才考虑自产新的 Specification。

## 4. 当前方向

当前不再以“完成某个阶段编号”为目标，而是同时推进三件事：

```text
知识地图持续成长
    +
可运行的知识基础设施
    +
Human / Agent 真实使用与反馈
```

这三条线互相校验：真实收录暴露模型缺口，真实 Workspace 暴露表达与交互缺口，真实 Agent / Human 使用暴露访问和治理缺口；修正后的能力再回流 Atlas。

当前状态和具体入口只由 `PROJECT_STATE.md` 与 GitHub Work Item 维护。

## 5. 能力进入施工的条件

长期方向不因为写在 Roadmap 上就自动成为任务。进入当前施工前至少回答：

1. 真实问题是什么？
2. 当前系统为什么解决不了？
3. 是否存在成熟 Prior Art / Standard？
4. 是否有真实数据或使用证据？
5. 问题属于 Canonical Knowledge，还是只属于 Projection / Workspace？
6. 对公共事实、个人隐私和 Agent Authority 有什么风险？
7. 如何验证成功、失败和可回滚性？

## 6. 产品演化原则

不要用固定页面列表、阶段编号或项目版本号定义长期产品。

```text
稳定、可追溯的知识
        ↓
持续演化的 Selection / Perspective
        ↓
持续演化的 Projection
        ↓
持续演化的 Workspace
        ↓
Human / Agent 真实使用
        ↓
反馈重新进入 Atlas
        ↺
```

## 7. 规划与版本边界

项目级 Roadmap、Living Documents 和当前主线采用持续演化模式，不使用 `V1 / V2` 作为规划框架。

版本身份只保留给真正需要版本边界的现实对象或技术制品，例如外部标准的特定版本、兼容契约、协议、Schema、发布制品或历史快照。Git / Issue / PR / provenance 负责记录项目自身演化。

## 8. Agent 阅读规则

Agent 必须区分：

- **长期方向**：本文的能力域，不代表已授权施工；
- **当前主线**：`PROJECT_STATE.md`；
- **可执行工作**：GitHub 中真实处于 Ready / Claimed / In Progress 的 Issue。

不得从历史阶段标题、旧版本号或 Roadmap 中的长期能力自动推断当前授权。
