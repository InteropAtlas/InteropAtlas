# InteropAtlas Repository Structure Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification
Document Created At: 2026-09-01T11:34:09+08:00
Document Updated At: 2026-09-05T14:20:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：Draft / Provisional Specification
>
> 本 Profile 是 InteropAtlas 仓库物理结构、注意力层级、Artifact 生命周期与文档去重规则的 Primary Home。

## 1. 三条核心原则

### 1.1 物理存储不等于语义模型

> **物理存储 ≠ 知识分类 ≠ 索引 / 视图。**

文件放在哪里只解决维护与工具访问；对象是什么由机器可读合同、稳定 ID、Relation 与 Graph 表达；用户怎样看由 Index / Map / Query / Workspace 表达。

因此不得为了某种浏览分类复制 Canonical 对象，也不得让路径承担 ontology 身份。

### 1.2 数字前缀表示主要注意力入口

数字不是装饰性排序，而是 Owner / Maintainer 应优先理解的认知入口。

同一物理层级默认遵守：

```text
01_*   第一主要关注域
02_*   第二主要关注域
03_*   第三主要关注域
```

规则：

- 同级编号 **MUST** 唯一，不得出现两个 `02_*`；
- 同级主要编号 **SHOULD** 限于 `01_ / 02_ / 03_`；
- 出现第四个主要关注域时，默认继续向下一层分组，而不是新增 `04_ / 05_`；
- `.github/`、`docs/`、`LICENSES/` 等辅助 / 平台目录可以不编号，但数量和职责仍应克制；
- 三分是认知复杂度默认约束，不是 ontology 的数学硬限制。若强行三分会破坏真实语义、Canonical contract 或关键工程约束，应明确记录例外，而不是为了形式移动语义边界。

### 1.3 一个概念一个 Primary Home

同一长期概念的完整定义 **SHOULD** 只有一个主要维护位置（Primary Home）。其他文件可以保留最小摘要并链接，但不应复制第二套完整论证、规则表或平行定义。

新增文件前首先判断能否修改既有 Primary Home。

## 2. 仓库一级结构

```text
01_State/       当前正式承认的 Canonical State
02_Runtime/     怎样运行、验证和使用 State
03_Evolution/   怎样研究、实验、决策并改变项目

docs/           当前 Living Documents
.github/        GitHub 原生协作 / 自动化
LICENSES/       外部许可证布局
root files      README / CONTRIBUTING / AGENTS / PROJECT_STATE 等入口
```

前三个编号目录是项目本体的三个主要生命周期区域；外围目录不构成第四个主域。

`02_Runtime` 与 `03_Evolution` 的主要结构：

```text
02_Runtime/
├── 01_Engine/
├── 02_Tools/
└── 03_Outputs/

03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

`01_State` 的 Canonical 子结构属于数据合同层。当前存在 Objects、Relations、Candidates 与 Acceptance Events；是否进一步把这些 Canonical 类别压缩为三入口不能仅按文件整理原则决定，必须以 Canonical architecture / intake semantics 为依据。本次物理结构清理不擅自改变其语义边界。

## 3. `docs/` 注意力结构

`docs/` 只保留今天仍需理解或遵守的 Living Documents，并采用三个主要入口：

```text
docs/
├── README.md
├── 01_Foundation/   项目为什么存在、是什么、往哪里走
├── 02_System/       知识系统怎样组成和被使用
└── 03_Operation/    项目怎样协作、治理和维护
```

继续采用递归三分：

```text
01_Foundation/
├── 01_Definition/
├── 02_Principles/
└── 03_Direction/

02_System/
├── 01_Knowledge/
└── 02_Interface/
    ├── 01_Foundation/
    ├── 02_Profiles/
    └── 03_Contracts/

03_Operation/
├── 01_Collaboration/
├── 02_Governance/
└── 03_Project/
```

目录只表达阅读与维护边界。Specification / Profile / Contract 是否独立，仍由其规范职责和演化节奏决定，不因为“文件少”而强制合并。

## 4. Current / Process / History

任何 Artifact 先判断生命周期，再决定位置：

```text
CURRENT   今天仍需理解 / 遵守
          → docs/、01_State/、02_Runtime/ 或平台原生位置

PROCESS   正在研究 / 实验 / 迁移
          → 03_Evolution 对应区域 / Issue / PR

HISTORY   已完成 / 被取代但仍有独立价值
          → 03_Evolution + lifecycle marker / Git history
```

`draft` 是状态，不是位置。仍是当前入口的 Draft 可以留在 `docs/`；已经完成或被取代的 Draft 不得因为文件名而永久留在 Living Documents。

## 5. Artifact 职责

| Artifact | Primary Home |
|---|---|
| Canonical Data / Relation / State Contract | `01_State/` |
| Engine / Validator / Renderer / Tool | `02_Runtime/` |
| Generated View / Export / Report | `02_Runtime/03_Outputs/` 或 CI artifact |
| Philosophy / Definition / Master Design / Architecture | `docs/01_Foundation/` |
| Knowledge / Human Interface Specification / Profile / Contract | `docs/02_System/` |
| Collaboration / Governance / Repository Policy | `docs/03_Operation/` |
| Research / Prior Art / Audit | `03_Evolution/01_Research/` |
| Experiment / Fixture / Prototype / Result | `03_Evolution/02_Experiments/` |
| Proposal / Phase Plan / Migration / Superseded Design | `03_Evolution/03_Change/` |
| Current project checkpoint | `PROJECT_STATE.md` |
| Work Item / Delivery | GitHub Issue / PR |

## 6. 文档去重与层级规则

### IA-RS-DOC-001 — 一个概念一个主要维护位置
当前正式文档 **MUST** 能指出概念的 Primary Home。

### IA-RS-DOC-002 — 上位不承担下位细节
Philosophy 不维护具体架构；Master Design 不维护专项字段；Roadmap 不维护实时施工；PROJECT_STATE 不承担完整 Roadmap。

### IA-RS-DOC-003 — 下位不重新定义上位
若上位定义不足，应回到 Primary Home 修改，不在下位文件创建更完整但不同的版本。

### IA-RS-DOC-004 — 摘要指回 Primary Home
因上下文必须重复概念时，只保留最小摘要和明确链接。

### IA-RS-DOC-005 — Promotion / Supersession 闭环
Research / Experiment / Change 被接受后，更新对应 Living Document；被替代的 Living Document 明确 successor，并按 Current / Process / History 重新归位。

### IA-RS-DOC-006 — 文档数量不是安全性
连续性来自稳定 Primary Home、Git history、Evolution、PROJECT_STATE、Issue / PR，而不是复制更多文件。

### IA-RS-DOC-007 — 文件夹不能掩盖重复
建立子目录只能降低同级注意力负担，不能替代去重。若两个文件实际拥有同一完整定义，应先决定 Primary Home，再合并 / 吸收 / 历史化。

## 7. 路径与迁移不变量

- Stable object identity **MUST NOT** 依赖物理文件路径；
- Generated view **MUST NOT** 成为第二事实源；
- Canonical migration 必须保持 object / relation identity、resolved graph 与 reference integrity；
- Living Document 路径 **SHOULD** 稳定，但当现有路径本身违反已接受的结构原则时，可以通过一次有验证、有引用修复的迁移建立新的稳定路径；
- 内容版本通常不进入 Living Document 文件名；Git commit / tag / release / provenance 负责版本历史；
- GitHub 原生识别的 Issue / PR / Workflow / Community Health 文件继续放在平台原生位置。

## 8. 新增文件 / 文件夹检查表

创建之前依次问：

1. 这是 Current、Process 还是 History？
2. 它属于哪一个 `01 / 02 / 03` 主要注意力域？
3. 同层是否已经有三个主要入口？如果有，能否继续向下分层？
4. 是否已有 Primary Home？
5. 它是新概念，还是旧概念的补充 / 操作化 / 临时过程？
6. 是否能修改已有文件而不是新增？
7. 新目录是否解决真实的规模、生命周期、所有权、工具或认知负担问题？
8. 是否会制造重复编号、第四主要入口或第二事实源？

默认选择：**少建一级、少建一份、优先归位、必要时继续向下三分。**

## 9. 本次结构迁移边界

本轮整理依据 Human Owner 明确授权，处理明显重复编号、明显错层和 Living Documents 平铺问题；不借整理之名改变项目 Definition / Scope、长期路线、Canonical semantics、stable Specification 状态或 Agent authority。

其中 `01_State` 的四类 Canonical 入口属于上层语义结构问题，保留现状，等待以 Canonical architecture 为依据单独判断。