# InteropAtlas 正式文档地图

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-05T14:45:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

`docs/` 只保存**今天进入 InteropAtlas 时仍需要理解或遵守的 Living Documents**。它不是研究档案，也不是项目施工日志。

研究、实验和变化过程分别进入：

```text
03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

## 三个主要入口

数字前缀表示主要注意力入口。`docs/` 只暴露三个编号主域：

```text
docs/
├── README.md
├── 01_Foundation/   项目为什么存在、是什么、长期往哪里走
├── 02_System/       知识系统怎样组成、怎样被人和 Agent 使用
└── 03_Operation/    项目怎样协作、治理和持续维护
```

如果一个层级需要超过三个主要类别，默认继续向下一层拆分，而不是横向增加 `04_ / 05_`。但**只有一个或两个文件的主题，不应为了形式上的分类额外制造一层目录**；文件名本身已经足够表达职责时，应优先保持扁平。

完整结构规则见 [`Repository Structure Profile`](03_Operation/03_Project/repository-structure-profile.zh-CN.md)。

## 01 Foundation

```text
01_Foundation/
├── 01_Definition/
│   ├── Master Design
│   └── Definition & Scope
├── 02_Principles/
│   └── Knowledge Philosophy & Principles
└── 03_Direction/
    ├── Core Architecture
    └── Long-term Roadmap
```

第一次理解项目，优先阅读：

1. [`总体设计（Master Design）`](01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)
2. [`项目定义与范围`](01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)
3. [`知识哲学与原则`](01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md)
4. [`当前核心架构`](01_Foundation/03_Direction/architecture.zh-CN.md)

长期路线见 [`Long-term Roadmap`](01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md)。

## 02 System

```text
02_System/
├── 01_Knowledge/
│   ├── Knowledge Object Classification
│   ├── Knowledge Workspace Design
│   ├── Public Commons & Personal Knowledge Space
│   └── Provenance / Traceability
└── 02_Interface/
    ├── 01_Foundation/
    ├── 02_Profiles/
    └── 03_Contracts/
```

`01_Knowledge` 保存知识模型、Workspace 与来源追踪等当前系统规则。

`02_Interface` 继续保留 Human Interface 已有的 Specification / Profile / Contract 边界；这次整理只改变物理层级，不借结构清理擅自改变其规范状态或 Requirement IDs。

## 03 Operation

```text
03_Operation/
├── 01_Collaboration/
│   ├── open-collaboration-profile.zh-CN.md
│   ├── agent-onboarding-context-continuity-profile.zh-CN.md
│   └── agent-attribution-contribution-identity-profile.zh-CN.md
├── 02_Governance/
│   ├── research-governance.zh-CN.md
│   ├── task-authority-governance-draft.zh-CN.md
│   └── task-reference-seeding-profile.zh-CN.md
└── 03_Project/
    ├── repository-structure-profile.zh-CN.md
    ├── language-policy.zh-CN.md
    ├── terminology-registry.md
    └── project-development-model.zh-CN.md
```

这里保存仍然有效的协作模型、任务治理、Agent 续接、贡献身份、研究治理、仓库结构、语言与项目建设规则。`01_Collaboration` 和 `03_Project` 不再为单个文件额外制造子目录；真正需要新的目录层级时，应先出现足够的长期文档密度和清晰主题边界。

## 第一次进入项目

### 人类贡献者 / 项目理解

```text
README.md
→ Master Design
→ Definition & Scope
→ Philosophy / Architecture（按任务需要）
→ PROJECT_STATE.md
```

### 智能体 / 维护者

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ Master Design
→ 当前 Issue
→ 相关 Contract / Profile
```

不要为了“保险”一次读取整个 `docs/`。按任务沿目录层级进入最小充分上下文。

## Primary Home 与生命周期

```text
Philosophy          为什么
Master Design       整个系统长期是什么
Definition / Scope  项目边界是什么
Architecture        当前核心系统怎样组成
Long-term Direction 长期子系统或方向
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
HISTORY   已完成 / 被取代但值得保存 → 03_Evolution/ + lifecycle marker
```

一个长期概念只维护一个完整 Primary Home。其他文档只保留必要摘要和链接，不复制第二套完整定义。实时状态只进入 `PROJECT_STATE.md` / Issue / PR；Git history 与 Evolution 负责历史恢复。

本目录原创说明文档默认采用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**，除非文件另有说明。