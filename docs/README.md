# InteropAtlas 正式文档地图

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-05T15:06:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Owner-authorized consolidation
  GitHub Actor: ff6962757
-->

`docs/` 只保存**今天进入 InteropAtlas 时仍需要理解或遵守的 Living Documents**。它不是研究档案，也不是项目施工日志。

研究、实验和变化过程进入 `03_Evolution/01_Research`、`02_Experiments`、`03_Change`。

## 三个主要入口

```text
docs/
├── README.md
├── 01_Foundation/   项目为什么存在、是什么、长期往哪里走
├── 02_System/       知识系统怎样组成、怎样被人和 Agent 使用
└── 03_Operation/    项目怎样协作、治理和持续维护
```

数字前缀表示主要注意力入口。同级主要类别默认只使用 `01 / 02 / 03`；需要更多概念时继续向下分层。但只有一两个文件的主题不应为了形式分类额外制造目录层级。

完整规则见 [`Repository Structure Profile`](03_Operation/03_Project/repository-structure-profile.zh-CN.md)。

## 01 Foundation

```text
01_Foundation/
├── 01_Definition/   Master Design / Definition & Scope
├── 02_Principles/   Knowledge Philosophy & Principles
└── 03_Direction/    Core Architecture / Long-term Roadmap
```

第一次理解项目优先阅读：[`Master Design`](01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md) → [`Definition & Scope`](01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md) → [`Knowledge Philosophy`](01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md) → [`Architecture`](01_Foundation/03_Direction/architecture.zh-CN.md)。

## 02 System

```text
02_System/
├── 01_Knowledge/
│   ├── 01_Model/
│   ├── 02_Workspace/
│   └── 03_Provenance/
└── 02_Interface/
    ├── 01_Foundation/   Human Interface Package / Primary Baseline
    ├── 02_Profiles/     五个模块化 IA-HI Profile
    └── 03_Contracts/    Compare / Search 等独立功能合同
```

Human Interface 不再维护一份并行 integrated specification；Package + 五个 Profile 是当前唯一主要规范入口。这个收口不等于 Stable Specification promotion。

## 03 Operation

```text
03_Operation/
├── 01_Collaboration/
│   ├── open-collaboration-profile.zh-CN.md
│   ├── agent-onboarding-context-continuity-profile.zh-CN.md
│   └── agent-attribution-contribution-identity-profile.zh-CN.md
├── 02_Governance/
│   └── research-governance.zh-CN.md
└── 03_Project/
    ├── repository-structure-profile.zh-CN.md
    ├── language-policy.zh-CN.md
    ├── terminology-registry.md
    └── project-development-model.zh-CN.md
```

Open Collaboration 已吸收 Task Authority 与 Task Reference Seeding 的长期规则；任务协作、T0–T3 授权、Seed References 与 Freshness 只维护一个 Primary Home。Research Governance 独立负责研究深度、停止条件、证据与管理上浮。

## 第一次进入项目

人类贡献者：

```text
README.md → Master Design → Definition & Scope → 按任务读取 Philosophy / Architecture → PROJECT_STATE.md
```

智能体 / 维护者：

```text
AGENTS.md → PROJECT_STATE.md → README.md → Master Design → 当前 Issue → 相关 Contract / Profile
```

不要为了“保险”一次读取整个 `docs/`。沿目录层级进入最小充分上下文。

## Primary Home 与生命周期

```text
Philosophy          为什么
Master Design       整个系统长期是什么
Definition / Scope  项目边界是什么
Architecture        当前核心系统怎样组成
Roadmap             阶段关系与长期顺序
Specification       可执行规范
Profile             特定场景的规范化约束
PROJECT_STATE       项目现在在哪里
Issue / PR           当前工作项
Evolution           为什么形成、试过什么、怎样改变
```

维护文件前先判断：

```text
CURRENT   今天仍需理解 / 遵守 → docs/
PROCESS   正在研究 / 实验 / 迁移 → 03_Evolution/
HISTORY   已完成 / 被取代但值得保存 → Git history / 必要时 Evolution
```

一个长期概念只维护一个完整 Primary Home。其他文档只保留必要摘要和链接，不复制第二套完整定义。实时状态只进入 `PROJECT_STATE.md` / Issue / PR。

本目录原创说明文档默认采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**，除非文件另有说明。