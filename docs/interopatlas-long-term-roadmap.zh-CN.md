# InteropAtlas 长期路线图 v1.0（Long-term Roadmap）

<!-- InteropAtlas Document Metadata v0
Document Status: active long-term roadmap
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T23:38:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文是长期方向图，不是当前任务队列。实时施工状态以 `PROJECT_STATE.md` 和 GitHub Issue / PR 为准。

## 1. 为什么需要长期路线图

InteropAtlas 过去曾把某一轮基础建设（Foundation）工作、五路线运行模型或某组页面功能误读成整个项目路线图（Roadmap）。

本路线图明确区分：

- **长期使命和产品形态**；
- **持续成长循环**；
- **有边界的基础建设 / 架构周期（Foundation / Architecture Cycles）**；
- **具体工作项（Work Items）**。

## 2. 长期目标（Long-term Destination）

长期 InteropAtlas 应逐步成为：

> **一个面向全人类的开放互操作方案空间（Interoperability Solution Space）公共知识基础设施，并允许人（Human）与智能体（Agent）在同一知识世界上，通过公共或个人视角（Perspective），把知识投影为适合当前任务和认知方式的可操作工作空间（Workspace）。**

它同时具有：

```text
公共知识共同体（Public Knowledge Commons）
        +
机器可读的规范知识（Machine-readable Canonical Knowledge）
        +
人 / 智能体共享访问（Human / Agent Shared Access）
        +
视角 / 选择（Perspective / Selection）
        +
投影 / 表达 / 工作空间（Projection / Representation / Workspace）
        +
个人知识空间（Personal Knowledge Space）
        +
持续收录 / 证据 / 来源追踪（Continuous Intake / Evidence / Provenance）
        +
由真实实践驱动的反馈（Practice-driven Feedback）
```

## 3. 路线图不是一条线性的终点线

IA 长期更像一个不断扩张和校正的循环：

```text
知晓（KNOW）──→ 使用（USE）──→ 发现（DISCOVER）──→ 贡献（CONTRIBUTE）
   ↑                                                    │
   └────────────────────────────────────────────────────┘

                         +
                    匹配（MATCH）
```

因此不存在“把所有标准收完”这样的终点。

## 4. 第一轮基础建设周期——V1 架构重新验证（Foundation Cycle 1）

2026-09-02 开始的新方向先通过一轮完整的验证和重构周期落地：

```text
P1  设计原则（Design Principles）                         ✅
P2  既有先例 / 标准研究（Prior-Art / Standards Research） ✅
P3  当前状态审计（Current-State Audit）                   ✅
P4  V1 架构 / 路线图重置（Architecture / Roadmap Reset）   ✅
P5  真实数据实验 / 收录压力测试（Real-data Experiments / Intake Stress） ✅ 主线完成
P6  V1 实现 + 迁移 + 收录（Implementation + Migration + Intake） ← 当前周期
```

这轮工作的目的不是“完成 IA”，而是把旧的参考实现（Reference Implementation）导向一个可信的 **V1 可运行基础（Operating Foundation）**。

## 5. 第一轮基础建设周期之后

P6 之后的长期演化不预先锁成固定的 P7 / P8 / P9 编号。未来阶段应由真实运行、研究、贡献规模和用户 / 智能体使用暴露的问题决定。

但当前已经明确需要长期推进的能力域包括：

### A. 知识地图覆盖与持续收录（Atlas Coverage & Continuous Intake）

- 扩大标准 / 成熟先例 / 方法 / 实现 / 组织 / 能力 / 场景（Standards / Prior Art / Methods / Implementations / Organizations / Capabilities / Scenarios）覆盖；
- 候选池 + 有边界的收录（Candidate Pool + Bounded Intake）；
- 覆盖率 / 方案空间覆盖率（Coverage / Solution-space Coverage）测量；
- 新鲜度 / 陈旧度（Freshness / Staleness）；
- 证据 / 来源追踪（Evidence / Provenance）；
- 身份 / 去重 / 合并-拆分治理（Identity / Dedup / Merge-split Governance）；
- 开放缺口发现（Open Gap Discovery）。

### B. 知识建模演化（Knowledge Modeling Evolution）

- 用真实数据检验对象 / 关系 / 事件 / 范围 / 上下文（Object / Relation / Event / Scope / Context）；
- 多元 / 带角色关系（N-ary / Role-bearing Relations）只在证据支持时演化；
- 语句级证据 / 来源追踪（Statement-level Evidence / Provenance）；
- 生命周期 / 历史知识（Lifecycle / Historical Knowledge）；
- 不因理论漂亮而提前重构规范模式（Canonical Schema）。

### C. 知识操作空间（Knowledge Operation Spaces）

- 百科式浏览（Wiki / Browse）；
- 对象 / 文章（Object / Article）；
- 时间线（Timeline）；
- 关系图 / 生态图（Graph / Ecosystem）；
- 比较（Compare）；
- 证据 / 验证（Evidence / Verification）；
- 后续矩阵 / 地图 / 模拟 / 交互 / 音视频 / 游戏式形式（Matrix / Map / Simulation / Interactive / Audiovisual / Game-like Forms）；
- 协调的工作空间状态（Coordinated Workspace State）；
- 表达转换 / 可恢复性（Representation Transformation / Recoverability）。

### D. 人与智能体共享操作（Human + Agent Shared Operation）

- 结构化查询 / 遍历 / 证据检索（Structured Query / Traverse / Evidence Retrieval）；
- 候选写入（Candidate Write）；
- 智能体操作视角 / 工作空间状态（Agent Operates Perspective / Workspace State）；
- 人与智能体共享上下文（Human + Agent Shared Context）；
- 可解释的智能体操作（Explainable Agent Actions）；
- 有边界的权威（Bounded Authority）；
- 不建立隐藏的智能体事实世界（No Hidden Agent Truth）。

### E. 个人知识空间（Personal Knowledge Space）

- 个人状态 / 意图 / 上下文（Personal State / Intent / Context）；
- 个人视角（Personal Perspective）；
- 内容 / 注意力个性化（Content / Attention Personalization）；
- 表达个性化（Representation Personalization）；
- 隐私与可携带性（Privacy and Portability）；
- 反信息茧房控制（Anti-filter-bubble Controls）；
- 公共 ↔ 个人反馈循环（Public ↔ Personal Feedback Loop）。

### F. 知识生命周期 / 知识代谢（Knowledge Lifecycle / Metabolism）

- 区分有效性 / 新鲜度 / 使用情况 / 相关性 / 历史价值 / 权威性 / 生命周期（Validity / Freshness / Usage / Relevance / Historical Value / Authority / Lifecycle）；
- 活跃 / 温热 / 冷却注意力模型（Active / Warm / Cold Attention Models）；
- 归档 / 压缩 / 重新激活（Archive / Compaction / Reactivation）；
- 公共知识生命周期与个人注意力生命周期分离；
- 知识维护债务（Knowledge-maintenance Debt）。

### G. 匹配 / 发现 / 推荐（Match / Discovery / Recommendation）

在公共知识和个人视角足够可靠之后，逐步研究：

- 问题 ↔ 方案（Problem ↔ Solution）；
- 需求 ↔ 能力（Need ↔ Capability）；
- 标准 ↔ 实现（Standard ↔ Implementation）；
- 人 ↔ 知识（Person ↔ Knowledge）；
- 人 ↔ 人 / 组织（Person ↔ Person / Organization）；
- 互补方案（Complementary Solutions）；
- 替代方案 / 缺口（Alternatives / Gaps）。

匹配（MATCH）必须保持可解释，并避免把参与度（Engagement）最大化变成项目目标。

### H. 开放生态与联邦化（Open Ecosystem & Federation）

长期允许：

- 第三方客户端；
- 新工作空间 / 表达（Workspace / Representation）；
- 多智能体（Multi-Agent）；
- 多种实现；
- 可导出的个人视角 / 工作空间状态；
- 当真实需求出现时支持联邦化 / 替代后端（Federation / Alternative Backends）；
- 只有在重复实践证明存在真实互操作缺口时，才由 IA 产出新的规范（Specification）。

## 6. 阶段晋级规则（Phase Promotion Rule）

未来新阶段不应因为“路线图上写了”就自动开始。

一个长期方向进入正式实现阶段前至少应回答：

1. 真实用户 / 智能体问题是什么？
2. 当前 V1 为什么解决不了？
3. 是否已经有成熟先例 / 标准（Prior Art / Standard）？
4. 是否有真实数据或使用证据？
5. 是否需要改变规范知识（Canonical Knowledge），还是只需要改变投影 / 工作空间（Projection / Workspace）？
6. 对公共事实、个人隐私、智能体权威（Agent Authority）有什么风险？
7. 成功和失败如何验证？

## 7. 产品演化原则（Product Evolution Principle）

不要用固定页面列表定义长期产品。

正确方向是：

```text
稳定的规范知识（Stable Canonical Knowledge）
        ↓
持续演化的选择 / 视角（Evolving Selection / Perspective）
        ↓
持续演化的投影（Evolving Projection）
        ↓
持续演化的工作空间（Evolving Workspaces）
        ↓
人 / 智能体真实使用（Human / Agent Real Use）
        ↓
反馈重新进入知识地图（Feedback into Atlas）
```

## 8. 智能体阅读路线图的规则（Roadmap Reading Rule for Agents）

智能体必须区分三种“下一步”：

- **长期方向（Long-term Direction）**：本文描述的能力域，不代表已授权施工；
- **当前项目阶段（Current Project Phase）**：以 `PROJECT_STATE.md` 为准；
- **可执行工作（Executable Work）**：GitHub 中处于 Ready / Claimed / In Progress 状态的 Issue。

不得因为本文提到个性化（Personalization）、模拟（Simulation）、匹配（MATCH）、联邦化（Federation）等，就绕过当前阶段和授权门（Authorization Gate）直接实现。

## 9. 当前恢复点（Current Resume Point）

截至本文本次更新时，第一轮基础建设周期仍位于 P6。实时状态、已完成切片（Slice）和下一授权入口以 `PROJECT_STATE.md` 为准。

P6 结束后，应根据实际运行结果重新进行一次路线图审查（Roadmap Review），而不是机械创建“P7”。
