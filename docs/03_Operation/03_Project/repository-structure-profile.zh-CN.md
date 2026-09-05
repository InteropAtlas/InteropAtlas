# InteropAtlas Repository Structure Profile v0.2

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification
Document Created At: 2026-09-01T11:34:09+08:00
Document Updated At: 2026-09-05T15:50:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human Owner — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Draft / Provisional Specification
>
> 本 Profile 是 InteropAtlas 仓库物理结构、注意力层级、Artifact 生命周期、文档去重与路径迁移完整性的 Primary Home。

## 1. 核心原则

### 1.1 物理存储不等于语义模型

> **物理存储 ≠ 知识分类 ≠ 索引 / 视图。**

文件放在哪里只解决维护与工具访问；对象是什么由机器可读合同、稳定 ID、Relation 与 Graph 表达；用户怎样看由 Index / Map / Query / Workspace 表达。

不得为了浏览分类复制 Canonical 对象，也不得让路径承担 ontology 身份。

### 1.2 数字前缀表示主要注意力入口

数字不是装饰性排序，而是 Owner / Maintainer 应优先理解的认知入口。

同一物理层级默认：

```text
01_*   第一主要关注域
02_*   第二主要关注域
03_*   第三主要关注域
```

规则：

- 同级编号 **MUST** 唯一；
- 同级主要编号 **SHOULD** 限于 `01_ / 02_ / 03_`；
- 出现第四个主要关注域时，默认继续向下一层分组，而不是新增 `04_ / 05_`；
- 非主要入口、临时入口、辅助入口可以不编号；它们不得仅因“存在”就占用编号注意力位置；
- `.github/`、`docs/`、`LICENSES/` 等辅助 / 平台目录可以不编号，但数量和职责仍应克制；
- 三分是认知复杂度默认约束，不是 ontology 的数学硬限制。若强行三分会破坏真实语义、Canonical contract 或关键工程约束，应明确记录例外。

### 1.3 一个概念一个 Primary Home

同一长期概念的完整定义 **SHOULD** 只有一个主要维护位置（Primary Home）。其他文件可以保留最小摘要并链接，但不应复制第二套完整论证、规则表或平行定义。

新增文件前首先判断能否修改既有 Primary Home。

### 1.4 层级必须有真实收益

目录不是越多越清晰。新增一层目录必须解决真实问题，例如：

- 同层项目已经造成明显注意力负担；
- 有稳定的主题边界；
- 生命周期、所有权或工具链确实不同；
- 需要容纳一组会长期共同演化的 Artifact。

**只有 1–2 个文件的主题，默认 SHOULD NOT 为了形式分类额外制造一层目录。** 文件名已能清楚表达职责时，优先保持扁平。不要创建“一文件一文件夹”的空壳层级。

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

```text
01_State/
├── 01_Objects/
├── 02_Relations/
└── Inbox/
    ├── candidates/
    └── acceptance-events/

02_Runtime/
├── 01_Engine/
├── 02_Tools/
└── 03_Outputs/

03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

`01_State` 当前只有两个编号主入口：`01_Objects/` 与 `02_Relations/`，分别承载正式 Canonical 对象与正式关系。`Inbox/` 是不编号的 intake 辅助工作区，用于尚未正式收入的候选内容和接纳流程证据，因此不占主要注意力入口。不能证明已经满足正式接纳条件的新内容，默认应先进 `Inbox/`，不得直接写入正式 Canonical 目录。

## 3. `docs/` 注意力结构

```text
docs/
├── README.md
├── 01_Foundation/   项目为什么存在、是什么、往哪里走
├── 02_System/       知识系统怎样组成和被使用
└── 03_Operation/    项目怎样协作、治理和维护
```

继续采用递归三分，但不为了凑三而增加无意义目录：

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

目录只表达阅读与维护边界。Specification / Profile / Contract 是否独立，仍由其规范职责和演化节奏决定。

## 4. Current / Process / History

任何 Artifact 先判断生命周期，再决定位置：

```text
CURRENT   今天仍需理解 / 遵守
          → docs/、01_State/、02_Runtime/ 或平台原生位置

PROCESS   正在研究 / 实验 / 迁移
          → 03_Evolution 对应区域 / Issue / PR

HISTORY   已完成 / 被取代但仍有独立价值
          → 03_Evolution / Git history
```

`draft` 是状态，不是位置。仍是当前入口的 Draft 可以留在 `docs/`；已经完成或被取代的 Draft 不得因为文件名而永久留在 Living Documents。

## 5. Artifact 职责

| Artifact | Primary Home |
|---|---|
| Canonical Data / Relation / State Contract | `01_State/` |
| Intake Candidate / Acceptance Evidence | `01_State/Inbox/` |
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
Research / Experiment / Change 被接受后，更新对应 Living Document；被替代的 Living Document 按 Current / Process / History 重新归位，历史由 Evolution / Git history 恢复。

### IA-RS-DOC-006 — 文档数量不是安全性
连续性来自稳定 Primary Home、Git history、Evolution、PROJECT_STATE、Issue / PR，而不是复制更多文件。

### IA-RS-DOC-007 — 文件夹不能掩盖重复
建立子目录只能降低同级注意力负担，不能替代去重。若两个文件实际拥有同一完整定义，应先决定 Primary Home，再合并 / 吸收 / 历史化。

### IA-RS-DOC-008 — 单文件主题默认不建目录
只有一个文件，或仅少量文件且没有稳定独立演化需求时，**SHOULD** 直接放在现有语义父目录中。只有文档密度或职责边界真实形成后再增加下一层。

## 7. 路径与迁移不变量

- Stable object identity **MUST NOT** 依赖物理文件路径；
- Generated view **MUST NOT** 成为第二事实源；
- Canonical migration 必须保持 object / relation identity、resolved graph 与 reference integrity；
- Living Document 路径 **SHOULD** 稳定；只有当现有路径违反已接受结构原则，或明显增加维护成本时才迁移；
- 路径迁移不能只验证“新文件存在”，还必须验证所有已知消费者已更新；
- 内容版本通常不进入 Living Document 文件名；Git commit / tag / release / provenance 负责版本历史；
- GitHub 原生识别的 Issue / PR / Workflow / Community Health 文件继续放在平台原生位置。

### IA-RS-MIG-001 — Path move 必须带引用修复

移动、重命名或删除被引用的文件 / 文件夹时，执行者 **MUST** 同步修复仓库内已知的显式引用。不得把“路径移动成功”当作迁移完成。

### IA-RS-MIG-002 — 迁移后必须做引用完整性审计

路径迁移完成前 **MUST** 至少执行：

1. 全仓 Markdown / repository-local link validation；
2. 搜索旧完整路径；
3. 搜索旧文件名 / 被删除文件名；
4. 对已知代码、workflow、validator、fixture、脚本中的硬编码路径进行检查；
5. 如果涉及 Canonical / Runtime，再执行对应 schema / compatibility / graph validation。

只有这些检查没有发现未处理引用，迁移才可视为完成。

### IA-RS-MIG-003 — 搜索不到不等于绝对不存在

Code search、索引或第三方工具可能有范围 / 时效限制。因此重要路径迁移应同时依赖 repository-local validator / CI，而不是只依赖搜索结果。若某类引用无法被自动覆盖，应在 PR 中明确记录残余风险或人工检查范围。

### IA-RS-MIG-004 — 删除前先吸收长期语义

删除重复 / 过渡 Living Document 前，必须先确认：

- 仍有效的独有规则已经迁入目标 Primary Home；
- 下游引用已经指向 successor；
- 删除不会静默改变规范状态、Requirement ID、Canonical semantics 或授权边界；
- 历史可由 Git history / Evolution 恢复。

如果不能满足，应该先合并内容或保留文件，而不是为了减少数量直接删除。

## 8. 清理 / 重构方法

执行仓库结构清理时，按以下顺序：

```text
1. 盘点真实结构与职责
   ↓
2. 找出明显错层 / 重复编号 / 平行 Primary Home
   ↓
3. 区分“纯物理问题”与“会改变语义的问题”
   ↓
4. 先处理无歧义的物理整理
   ↓
5. 对重复文档做内容级比较
   ↓
6. 把独有长期规则吸收到 Primary Home
   ↓
7. 删除 / 历史化被吸收 Artifact
   ↓
8. 修复所有引用与入口文档
   ↓
9. 运行 Markdown links + 相关兼容性 / Graph / Provenance 检查
   ↓
10. 搜索旧路径与旧文件名做迁移后审计
```

遇到以下情况不得仅凭结构美观自行处理：

- 会改变项目 Definition / Scope；
- 会改变 Canonical semantic model；
- 会执行 stable Specification / Governance promotion；
- 会改变重大 authority / security / identity policy；
- 为满足“三分”必须扭曲真实语义。

这些属于上层设计 / Owner Gate，而不是普通结构整理。

## 9. 新增文件 / 文件夹检查表

创建之前依次问：

1. 这是 Current、Process 还是 History？
2. 它属于哪一个 `01 / 02 / 03` 主要注意力域？
3. 同层是否已经有三个主要入口？如果有，能否继续向下分层？
4. 是否已有 Primary Home？
5. 它是新概念，还是旧概念的补充 / 操作化 / 临时过程？
6. 是否能修改已有文件而不是新增？
7. 新目录是否解决真实的规模、生命周期、所有权、工具或认知负担问题？
8. 目录下预计是否只有 1–2 个文件？若是，为什么不能保持扁平？
9. 是否会制造重复编号、第四主要入口或第二事实源？
10. 新路径将影响哪些链接、脚本、workflow 或消费者？

默认选择：**少建一级、少建一份、优先归位、必要时继续向下三分；任何路径变化都要把引用完整性当作迁移的一部分。**

## 10. 当前已知边界

`01_State` 的编号入口只用于正式 Canonical State。候选对象与接纳决策证据已经归入不编号的 `Inbox/`；它们参与 intake 流程，但不因此获得主要注意力编号。后续如果再出现类似“流程辅助物 / 临时物 / 未正式收入内容”，应优先判断是否属于不编号辅助入口，而不是机械增加新的编号目录。