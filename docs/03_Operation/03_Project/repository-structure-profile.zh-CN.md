# InteropAtlas Repository Structure Profile v0.4

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification
Document Created At: 2026-09-01T11:34:09+08:00
Document Updated At: 2026-09-05T17:35:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
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

### 1.2 注意力层级（Attention Hierarchy）

数字前缀不是装饰性排序，而是 Owner / Maintainer 应优先理解的主要注意力入口（Primary Attention Target）。

同一物理层级默认：

```text
01_*   第一主要关注域
02_*   第二主要关注域
03_*   第三主要关注域
```

规则：

- 同级编号 **MUST** 唯一；
- 同级主要编号 **SHOULD** 限于 `01_ / 02_ / 03_`；
- 默认只暴露 1–2 个主要入口，最多 3 个；三不是目标，而是上限；
- 出现第四个主要关注域时，默认继续向下一层分组，而不是新增 `04_ / 05_`；
- 非主要入口、临时入口、辅助入口可以不编号；它们不得仅因“存在”就占用编号注意力位置；
- `.github/`、`docs/`、`LICENSES/` 等辅助 / 平台目录可以不编号，但数量和职责仍应克制；
- 三分是认知复杂度默认约束，不是 ontology 的数学硬限制。若强行三分会破坏真实语义、Canonical contract 或关键工程约束，应明确记录例外。

注意力层级限制的是**同时暴露给人的主要认知选择数量**，不是仓库可以拥有多少 Canonical Object、Relation、Issue、Project 或历史 Artifact。

### 1.3 一个概念一个 Primary Home

同一长期概念的完整定义 **SHOULD** 只有一个主要维护位置（Primary Home）。其他文件可以保留最小摘要并链接，但不应复制第二套完整论证、规则表或平行定义。

新增文件前首先判断能否修改既有 Primary Home。

### 1.4 层级必须有真实收益

目录不是越多越清晰。新增一层目录必须解决真实问题，例如：

- 同层内容已经造成明显注意力负担；
- 有稳定的主题边界；
- 生命周期、所有权或工具链确实不同；
- 需要容纳一组会长期共同演化的 Artifact。

**只有 1–2 个文件的主题，默认 SHOULD NOT 为了形式分类额外制造一层目录。** 文件名已能清楚表达职责时，优先保持扁平。不要创建“一文件一文件夹”的空壳层级。

### 1.5 Repository 不是工作空间

InteropAtlas Repository 保存**长期有效的状态、实现、规范和演化依据**，不承担普通任务管理或完整项目过程记录。

```text
正在发生的工作
→ GitHub Issue / Project / Branch / PR

工作完成后仍值得长期存在的结果
→ Repository 对应 Primary Home
```

小活动、研究项目、整改任务、迁移施工等不会仅因为持续时间或参与人数而自动获得 Repository 项目文件夹。

> **GitHub 管正在怎样工作；Repository 管工作之后值得长期存在什么。**

## 2. 仓库一级结构与变化梯度

```text
01_State/       当前正式知识状态
02_Runtime/     当前运行实现
03_Evolution/   长期演化依据

docs/           当前正式定义、原则、规范与治理
.github/        GitHub 原生协作 / 自动化
LICENSES/       外部许可证布局
root files      README / CONTRIBUTING / AGENTS / PROJECT_STATE 等入口
```

前三个编号目录是项目本体的三个主要内容入口；`docs/` 是约束和解释这些内容的规则层，不构成第四个编号主域。

### 2.1 变化梯度（Change Gradient）

```text
变化频率：
01_State  >  02_Runtime  >  03_Evolution  >  docs
```

这是设计倾向，不是机械 SLA：

- `01_State` 持续吸收 Canonical Object、Relation 与 Evidence，集合变化最快；
- `02_Runtime` 随 State、Schema、查询、验证和界面实现演化；
- `03_Evolution` 只保存经过筛选的长期研究、实验和决策依据，变化更少；
- `docs/` 承担当前项目正式定义、原则、规范与治理，实质变化最谨慎。

### 2.2 变更权限梯度（Change Authority Gradient）

```text
既有内容的改写门槛：
01_State  <  02_Runtime  <  03_Evolution  <  docs
```

这不表示 State 可以绕过 intake / validation，也不表示 docs 永远不可修改。它表达的是：越接近长期依据和正式规范，对既有内容做实质改写时，需要越强的理由、证据、review 与适用 authority gate。

特别是 Evolution 中的历史依据，默认更适合补充、勘误或追加 successor，而不是为了配合当前结论任意重写过去。

### 2.3 当前主要结构

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
└── 03_Decisions/
```

`01_State` 当前只有两个编号主入口：`01_Objects/` 与 `02_Relations/`。`Inbox/` 是不编号的 intake 辅助工作区，不能证明已经满足正式接纳条件的新内容默认应先进 `Inbox/`。

`02_Runtime/03_Outputs/` 只有在生成结果确实需要版本控制时才使用；可重建输出默认优先 CI artifact / deployment，而不是为了三分长期提交空洞或重复输出。

`03_Evolution` 已按 Research / Experiments / Decisions 三个长期职责落实。旧 `03_Change/` 中真正具有独立长期解释价值的方向与架构依据已进入 `03_Decisions/`；阶段计划、旧 roadmap、迁移预检、施工审计与其他只有过程价值的材料不再保留在当前树，由 Git / GitHub history 继续提供历史恢复能力。

## 3. `docs/` 注意力结构

```text
docs/
├── README.md
├── 01_Foundation/   项目为什么存在、是什么、往哪里走
├── 02_System/       知识系统怎样组成和被使用
└── 03_Operation/    项目怎样协作、治理和维护
```

继续采用递归注意力层级，但不为了凑三而增加无意义目录：

```text
01_Foundation/
├── 01_Definition/
├── 02_Principles/
└── 03_Direction/

02_System/
├── 01_Knowledge/
└── 02_Interface/

03_Operation/
├── 01_Collaboration/
├── 02_Governance/
└── 03_Project/
```

目录只表达阅读与维护边界。Specification / Profile / Contract 是否独立，仍由其规范职责和演化节奏决定。

`docs/` 不因未编号而重要性较低。相反，它是前三个系统内容域的正式规则层，因此其长期职责更重，实质修改应更谨慎。

## 4. Artifact 生命周期：Current / Work / Durable History

任何 Artifact 先判断生命周期，再决定是否进入 Repository：

```text
CURRENT
今天仍需理解 / 遵守 / 运行
→ docs/、01_State/、02_Runtime/ 或平台原生位置

WORK
正在研究 / 实验 / 迁移 / 整改 / 协作
→ GitHub Issue / Project / Branch / PR
→ 默认不是 Repository Artifact

DURABLE HISTORY / RATIONALE
工作完成后仍具有独立阅读、引用、复用或解释价值
→ 03_Evolution/ 或 Git history
```

`draft` 是状态，不是位置。仍是当前入口的 Draft 可以留在 `docs/`；已经完成或被取代的 Draft 不得因为文件名而永久留在 Living Documents。

### 4.1 工作成果吸收顺序

一个任务 / 项目完成后，按以下顺序处理：

```text
1. 当前正式知识
   → 01_State/

2. 当前仍运行的实现
   → 02_Runtime/

3. 当前正式定义 / 原则 / 规范 / 治理
   → docs/

4. 不属于前三者，但仍有独立长期研究 / 实验 / 决策价值
   → 03_Evolution/

5. 只有过程价值
   → Issue / PR / Git history；不新增 Repository 文件
```

因此 Research Project 可以在完成后被“拆空”；这不是信息损失，而是成果已经进入正确的长期 Primary Home。

### 4.2 延迟分类

无法归入 State / Runtime / docs，但仍可能有长期价值的材料，不应立即催生新的 `Shared/`、`Resources/`、`Misc/` 等宽泛类别。

如果它已经形成独立长期研究 / 实验 / 决策价值，可以先随对应 Evolution Durable Artifact 保留；只有真实积累反复暴露同一种稳定新职责时，才设计新的 Primary Home。

## 5. Artifact 职责

| Artifact | Primary Home |
|---|---|
| Canonical Data / Relation / State Contract | `01_State/` |
| Intake Candidate / Acceptance Evidence | `01_State/Inbox/` |
| Engine / Validator / Renderer / current operational Tool | `02_Runtime/` |
| Necessary versioned Generated View / Export / Report | `02_Runtime/03_Outputs/` 或 CI artifact |
| Philosophy / Definition / Master Design / Architecture | `docs/01_Foundation/` |
| Knowledge / Human Interface Specification / Profile / Contract | `docs/02_System/` |
| Collaboration / Governance / Repository Policy | `docs/03_Operation/` |
| Durable Research / Prior-art comparison | `03_Evolution/01_Research/` |
| Durable Experiment / reproducible result | `03_Evolution/02_Experiments/` |
| Durable architectural / directional Decision rationale | `03_Evolution/03_Decisions/` |
| Current project checkpoint | `PROJECT_STATE.md` |
| Work Item / Activity / Project coordination / Delivery | GitHub Issue / Project / PR |
| Ordinary work history | Git / Issue / PR history |

## 6. Evolution 准入规则

Evolution 不是过程归档区，也不是 Primary Home 缺失时的兜底目录。

一份材料只有同时满足以下条件，才应长期进入 `03_Evolution/`：

1. 它不属于当前 `01_State / 02_Runtime / docs` 的 Primary Home；
2. 原 Issue / PR / Project 完成以后，它仍具有独立阅读、引用、复用或解释价值；
3. 仅依赖 Git / GitHub history 会明显损失未来理解某项重要研究、实验或决策的能力。

默认三类：

```text
01_Research/      我们通过研究长期知道了什么
02_Experiments/   我们通过实验长期验证了什么
03_Decisions/     为什么 IA 演化成今天这样
```

默认不建立 `Projects/`、`Activities/`、`Archive/`、`Shared/`、`Resources/`、`Misc/` 等宽泛容器。

`01_Research/` 与 `02_Experiments/` 当前保留已有下一层分组，是因为真实积累量和实验可复现性已经构成实际收益；后续仍应按内容价值审计，而不是为了“绝对扁平”机械移动。

## 7. 文档去重与层级规则

### IA-RS-DOC-001 — 一个概念一个主要维护位置
当前正式文档 **MUST** 能指出概念的 Primary Home。

### IA-RS-DOC-002 — 上位不承担下位细节
Philosophy 不维护具体架构；Master Design 不维护专项字段；Roadmap 不维护实时施工；PROJECT_STATE 不承担完整 Roadmap。

### IA-RS-DOC-003 — 下位不重新定义上位
若上位定义不足，应回到 Primary Home 修改，不在下位文件创建更完整但不同的版本。

### IA-RS-DOC-004 — 摘要指回 Primary Home
因上下文必须重复概念时，只保留最小摘要和明确链接。

### IA-RS-DOC-005 — Promotion / Supersession 闭环
Research / Experiment / Decision 被接受并形成当前规则或实现后，更新对应 State / Runtime / Living Document；Evolution 只继续保存仍有独立长期价值的 rationale。

### IA-RS-DOC-006 — 文档数量不是安全性
连续性来自稳定 Primary Home、Git history、Evolution、PROJECT_STATE、Issue / PR，而不是复制更多文件。

### IA-RS-DOC-007 — 文件夹不能掩盖重复
建立子目录只能降低同级注意力负担，不能替代去重。若两个文件实际拥有同一完整定义，应先决定 Primary Home，再合并 / 吸收 / 历史化。

### IA-RS-DOC-008 — 单文件主题默认不建目录
只有一个文件，或仅少量文件且没有稳定独立演化需求时，**SHOULD** 直接放在现有语义父目录中。只有文档密度或职责边界真实形成后再增加下一层。

### IA-RS-DOC-009 — 工作对象默认不实体化为 Repository 文件夹
Issue、活动、研究项目、整改项目、迁移项目等工作对象 **SHOULD NOT** 仅因为其存在就在 Repository 中建立一一对应的目录。需要长期保存的是其 Durable Output，而不是工作容器本身。

## 8. 路径与迁移不变量

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

删除重复 / 过渡 Living Document 或 Evolution Artifact 前，必须先确认：

- 仍有效的独有规则 / 知识已经迁入目标 Primary Home；
- 下游引用已经指向 successor；
- 删除不会静默改变规范状态、Requirement ID、Canonical semantics 或授权边界；
- 需要保留的独立长期 rationale 已经进入 Evolution；
- 普通过程历史可由 Git / GitHub history 恢复。

如果不能满足，应该先合并内容或保留文件，而不是为了减少数量直接删除。

## 9. 清理 / 重构方法

执行仓库结构清理时，按以下顺序：

```text
1. 盘点真实结构与职责
   ↓
2. 找出明显错层 / 重复编号 / 平行 Primary Home
   ↓
3. 区分 Current、Work、Durable History
   ↓
4. 判断成果是否应吸收到 State / Runtime / docs
   ↓
5. 判断剩余材料是否达到 Evolution 准入门槛
   ↓
6. 把独有长期规则 / 知识吸收到 Primary Home
   ↓
7. 删除 / 历史化没有独立长期价值的过程 Artifact
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

## 10. 新增文件 / 文件夹检查表

创建之前依次问：

1. 这是 Current、Work 还是 Durable History？
2. 如果是 Work，为什么不能只存在于 Issue / Project / PR？
3. 如果是 Current，它属于 State、Runtime 还是 docs？
4. 如果是 Durable History，它是否达到 Evolution 三项准入门槛？
5. 是否已有 Primary Home？
6. 是否能修改已有文件而不是新增？
7. 新目录是否解决真实的规模、生命周期、所有权、工具或认知负担问题？
8. 同层是否已经暴露三个主要注意力入口？
9. 目录下预计是否只有 1–2 个文件？若是，为什么不能保持扁平？
10. 新路径将影响哪些链接、脚本、workflow 或消费者？

默认选择：**先减少有资格成为 Repository Artifact 的东西，再讨论如何分类；少建一级、少建一份、优先归位，路径变化同时保证引用完整性。**

## 11. 当前实施状态

当前一级结构已经按本 Profile 落实：`01_State / 02_Runtime / 03_Evolution` 为三个编号内容域，`docs/` 为规则层；`01_State` 使用 `01_Objects / 02_Relations + Inbox`；`03_Evolution` 使用 `01_Research / 02_Experiments / 03_Decisions`。

本轮没有为了形式一致而重排已经合理的 Root、State、Runtime 与 docs，也没有机械扁平化 Research / Experiments。后续结构变化应由真实职责、规模或工具摩擦触发，而不是继续进行无目标的目录整理。