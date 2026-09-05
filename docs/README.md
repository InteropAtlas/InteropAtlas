# InteropAtlas 正式文档地图

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:51:02+08:00
Document Updated At: 2026-09-05T05:05:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

`docs/` 只保存**今天进入 InteropAtlas 时仍需要理解或遵守的 Living Documents**。研究、实验、阶段计划、架构形成过程和已被取代但仍有价值的历史材料分别进入 `03_Evolution/01_Research`、`03_Evolution/02_Experiments`、`03_Evolution/03_Change`。

文档生命周期与 Primary Home 规则见 [`repository-structure-profile.zh-CN.md`](repository-structure-profile.zh-CN.md)。中文文档以自然中文为主阅读语言；语言与翻译规则见 [`language-policy.zh-CN.md`](language-policy.zh-CN.md)，跨语言概念绑定见 [`terminology-registry.md`](terminology-registry.md)。

## 0. 第一次进入项目

### 人类贡献者 / 项目理解

```text
README.md
→ interopatlas-master-design.zh-CN.md
→ knowledge-philosophy-and-principles.zh-CN.md
→ architecture.zh-CN.md
→ PROJECT_STATE.md
```

### 智能体 / 维护者

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ interopatlas-master-design.zh-CN.md
→ architecture.zh-CN.md
→ 当前 Issue / Contract / Profile
```

不要把阶段计划、历史 Draft、某个 Workspace、某个 Issue 或某一条旧运行路线当成整个 InteropAtlas。

## 1. L0–L1：使命、哲学与总体设计

- [`interopatlas-master-design.zh-CN.md`](interopatlas-master-design.zh-CN.md) — **当前总体设计（Master Design）**：项目长期是什么、主要系统边界如何组合。
- [`knowledge-philosophy-and-principles.zh-CN.md`](knowledge-philosophy-and-principles.zh-CN.md) — **哲学 Primary Home**：核心哲学、知识流动 / 创造与派生建设原则。
- [`interopatlas-definition-and-scope.zh-CN.md`](interopatlas-definition-and-scope.zh-CN.md) — 项目定义、互操作问题边界和收录范围。

核心哲学：

> **知识属于公共共同体。视角属于个人。**  
> *Knowledge belongs to the commons. Perspective belongs to the individual.*

动态命题：

> **知识流动，创造不息。**  
> *Knowledge travels. Creation continues.*

发现、连接、传递、转化和复用是 Flow 的典型机制，不再作为必须并列的六阶段顶层模型。

## 2. L2：当前核心架构与长期子系统

- [`architecture.zh-CN.md`](architecture.zh-CN.md) — **V1 Core Architecture Primary Home**：Canonical Contract、Evidence / Assertion、Lifecycle、Intake、Selection / Projection、Human + Agent Access 与 Runtime 边界。
- [`public-commons-and-personal-knowledge-space.zh-CN.md`](public-commons-and-personal-knowledge-space.zh-CN.md) — 公共知识共同体 + 个人知识空间专项长期设计。
- [`knowledge-workspace-design-principles.zh-CN.md`](knowledge-workspace-design-principles.zh-CN.md) — Perspective / Selection / Projection / Representation / Workspace 专项设计原则。

P4 Canonical Contract、Write / Intake、Migration、Selection / Projection / Workspace、Human + Agent Access 等阶段 Architecture Draft 已归入 `03_Evolution/03_Change/`；其仍有效的核心架构由 `architecture.zh-CN.md` 承接。

早期 `Flat Objects + Rich Relations + Dynamic Maps` 原则也已吸收到 V1 Core Architecture 与 Repository Structure Profile，不再维护第二份独立架构定义。

## 3. L3：运行、反馈与项目演化

- [`practice-feedback-loop.zh-CN.md`](practice-feedback-loop.zh-CN.md) — Atlas ↔ Runtime / Practice 的反馈机制。
- [`project-development-principles.zh-CN.md`](project-development-principles.zh-CN.md) — 项目建设原则与最小治理规则。

早期五路线协同模型已移入 Evolution。Human / Machine / Curation / Trust / Governance 中仍有效的职责现在分别由 Master Design、Core Architecture、Intake、Provenance 和 Governance Profiles 承接。

## 4. L4：长期路线图与当前施工状态

- [`interopatlas-long-term-roadmap.zh-CN.md`](interopatlas-long-term-roadmap.zh-CN.md) — **长期路线图 Primary Home**；P1–P6 只是第一轮 V1 Foundation / Architecture Revalidation Cycle。
- [`../PROJECT_STATE.md`](../PROJECT_STATE.md) — **唯一项目级实时施工断点**：当前阶段、Resume Here、Gate 与最新验证状态。
- 当前 GitHub Issue / PR — 具体工作项、依赖、交付与协作状态。

P4.6 Roadmap Reset、旧 Phase Plan、迁移计划与其他过渡材料属于 Change history，位于 [`../03_Evolution/03_Change/`](../03_Evolution/03_Change/)。

## 5. L5：契约 / 规范 / 配置规范

### 规范知识 / 收录

- [`knowledge-object-classification-specification.zh-CN.md`](knowledge-object-classification-specification.zh-CN.md)

Canonical Schema、Relation、Candidate / Intake 等机器可执行契约同时存在于 `01_State` 和对应 Profile / Runtime 中；不要从 Historical P4 Draft 推断当前字段级规则。

### 人类界面

- [`human-interface-profiles.zh-CN.md`](human-interface-profiles.zh-CN.md) — Human Interface Profiles 总入口。
- [`human-interface-information-architecture-profile.zh-CN.md`](human-interface-information-architecture-profile.zh-CN.md)
- [`human-interface-information-presentation-profile.zh-CN.md`](human-interface-information-presentation-profile.zh-CN.md)
- [`human-interface-interaction-profile.zh-CN.md`](human-interface-interaction-profile.zh-CN.md)
- [`human-interface-visual-presentation-profile.zh-CN.md`](human-interface-visual-presentation-profile.zh-CN.md)
- [`human-interface-accessibility-conformance-profile.zh-CN.md`](human-interface-accessibility-conformance-profile.zh-CN.md)
- [`human-interface-specification.zh-CN.md`](human-interface-specification.zh-CN.md)
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md)
- [`human-interface-minimal-compare-contract.zh-CN.md`](human-interface-minimal-compare-contract.zh-CN.md)

### 开放协作 / 人机协作

- [`open-collaboration-profile.zh-CN.md`](open-collaboration-profile.zh-CN.md)
- [`collaboration-task-system.zh-CN.md`](collaboration-task-system.zh-CN.md)
- [`task-reference-seeding-profile.zh-CN.md`](task-reference-seeding-profile.zh-CN.md)
- [`agent-onboarding-context-continuity-profile.zh-CN.md`](agent-onboarding-context-continuity-profile.zh-CN.md)
- [`agent-attribution-contribution-identity-profile.zh-CN.md`](agent-attribution-contribution-identity-profile.zh-CN.md)
- [`agent-continuation-bridge.zh-CN.md`](agent-continuation-bridge.zh-CN.md) — 当前 workflow 的运行契约 / 说明，不是阶段路线文档。

### 来源追踪 / 研究 / 治理

- [`provenance-traceability-profile.zh-CN.md`](provenance-traceability-profile.zh-CN.md)
- [`research-governance.zh-CN.md`](research-governance.zh-CN.md)
- [`task-authority-governance-draft.zh-CN.md`](task-authority-governance-draft.zh-CN.md) — 当前仍在形成中的治理入口；`draft` 是状态，不自动意味着历史。

### 仓库 / 政策

- [`repository-structure-profile.zh-CN.md`](repository-structure-profile.zh-CN.md) — 仓库职责、Artifact taxonomy、文档生命周期、Primary Home 与去重规则。
- [`language-policy.zh-CN.md`](language-policy.zh-CN.md)
- [`terminology-registry.md`](terminology-registry.md)

## 6. Evolution：过程和历史放在哪里

```text
03_Evolution/
├── 01_Research/      Prior Art / Research / Audit / Verification
├── 02_Experiments/   Prototype / Experiment / Dry Run / Result
└── 03_Change/        Proposal / Roadmap History / Phase Plan / Migration / Superseded Design
```

Research / Experiment / Change 中的文件存在于仓库，并不表示它仍是当前设计。研究结论被接受后，应更新对应 Living Document；过程文件保留为证据和设计历史。

## 7. Primary Home 与生命周期规则

```text
Philosophy          为什么
Master Design       整个系统长期是什么
Core Architecture   当前核心系统结构
Long-term Direction 某一长期子系统
Roadmap             长期阶段关系
Specification       可执行规范
Profile             特定场景的规范化选择
PROJECT_STATE       现在在哪里
Issue / PR           当前工作项
Evolution           为什么这样形成、试过什么、怎样改变
```

维护文档时先判断 `CURRENT / PROCESS / HISTORY`，再决定 `docs/`、Evolution 或删除。一个长期概念只维护一个完整 Primary Home；其他文件只保留必要摘要并链接，不复制第二套完整定义。

Living Document 的路径保持稳定，内容版本由 Git / tag / release / provenance 留痕。`draft` 是状态，不是位置；已经完成或被取代的 Draft 必须离开 `docs/`。

## 8. 清理原则

- 不为聊天或阶段断点创建新的 checkpoint 文档；
- 不用重复文本保护设计历史；
- 有独立历史价值的 superseded 文件进入 Evolution；
- 真正临时、重复且没有独立价值的文件可以删除；
- 高层设计的 Primary Home 被替代时必须明确 successor；
- 实时状态只进入 `PROJECT_STATE.md` / Issue / PR；
- Git history + Evolution 承担历史恢复，而不是让旧 Draft 长期留在 `docs/`。

本目录原创说明文档默认采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**，除非文件另有说明。
