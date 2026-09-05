# 03_Evolution

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T14:31:59+08:00
Document Updated At: 2026-09-05T16:30:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

`03_Evolution` 是 InteropAtlas 三个核心一级目录之一，但它**不是项目工作空间，也不是所有历史过程的归档区**。

它保存那些已经脱离具体 Issue / Project / PR 生命周期、但仍具有独立长期价值的**演化依据（Evolution Rationale）**：研究成果、实验成果，以及解释重大方向或架构为何形成的决策记录。

目标结构：

```text
03_Evolution/
├── 01_Research/      通过研究，我们长期知道了什么
├── 02_Experiments/   通过实验，我们长期验证了什么
├── 03_Decisions/     为什么 IA 演化成今天这样
└── README.md
```

## 1. Repository 不是工作空间

InteropAtlas 的进行中工作优先使用 GitHub 原生协作层：

```text
Activity / Task          → Issue
Multi-task coordination  → GitHub Project
Implementation delivery  → Branch / PR
Discussion / review      → Issue / PR
Work history             → GitHub history
```

一个研究、实验、迁移或整改任务不会仅因为持续多天、参与多人或被称为“Project”，就在 Repository 中获得项目文件夹。

核心原则：

> **GitHub 管正在怎样工作；Repository 管工作之后值得长期存在什么。**

## 2. Evolution 的三个长期入口

### `01_Research/` — 研究成果

回答：**我们通过研究长期知道了什么？**

适合保留：

- 具有独立阅读价值的 Prior Art / standards research；
- 多方案系统比较；
- 对项目哲学、知识模型、信息架构或重要设计判断形成长期依据的研究；
- 即使原 Issue / PR 已结束，未来仍值得引用、复用或重新审视的研究成果。

普通搜索过程、临时笔记、阶段性任务记录、一次性 audit checklist 不因“属于研究”就自动进入这里。

### `02_Experiments/` — 实验成果

回答：**我们通过实际验证长期知道了什么？**

适合保留：

- 对重要技术或模型选择有长期解释价值的可复现实验；
- 仍值得未来重复验证的实验设计、关键 fixture 与结果；
- 有知识价值的失败路径或压力测试结果。

普通 CI 测试、当前 Runtime 单元测试、临时 dry-run 和施工 smoke test 不属于这里；当前运行验证应留在 `02_Runtime/` 或 CI。

### `03_Decisions/` — 决策与演化依据

回答：**为什么 InteropAtlas 演化成今天这样？**

适合保留：

- 重大架构选择及其 rationale；
- 长期项目方向发生实质变化时的决策依据；
- 认真评估后被放弃、且未来仍值得理解的重大路线；
- 对当前 `docs/` 中正式原则或规范具有重要 provenance 价值的决策记录。

普通施工计划、Phase checklist、文件迁移清单、任务进度和已经由 Issue / PR / Git history 充分记录的机械变更不属于这里。

## 3. 与 `01_State`、`02_Runtime`、`docs/` 的边界

项目或任务结束时，不先问“应该归档到 Evolution 哪个文件夹”，而先问长期成果属于哪个 Primary Home：

```text
当前正式知识 / 对象 / 关系 / Evidence
→ 01_State/

当前仍在运行的实现、Validator、Renderer、Tool
→ 02_Runtime/

当前项目定义、原则、规范、治理与长期规则
→ docs/

不属于以上三者，但仍具有独立长期研究 / 实验 / 决策价值
→ 03_Evolution/

只有工作过程价值
→ Issue / PR / Git history，不进入 Repository
```

Evolution 不应成为 `State / Runtime / docs` 无法归类内容的兜底垃圾桶。

## 4. 研究成果与研究过程

研究结果可以被吸收到 Canonical State：标准、组织、方法、实现等成为 Object；主题内部的连接、比较、来源和其他结构化知识可以由 Relation / Evidence / Assessment 表达。

因此一个研究任务完成以后，Repository 中可能几乎不剩“项目文件”。这是正常且理想的。

研究过程只有在**理解结论所必需，或本身具有独立长期知识价值**时才进入 Evolution。不要为了保存完整过程而把所有搜索顺序、临时假设、讨论事件和任务日志转换成 Canonical Relation，也不要复制 GitHub 已经完整保存的协作历史。

## 5. 变化梯度与变更权限梯度

根目录形成一个有意的变化梯度：

```text
变化频率：
01_State  >  02_Runtime  >  03_Evolution  >  docs

既有内容的改写门槛：
01_State  <  02_Runtime  <  03_Evolution  <  docs
```

这里的比较是设计倾向，不表示 State 可以绕过验证，也不表示 docs 永远不可修改。

- `01_State` 持续吸收新的 Canonical knowledge，因此集合变化最快；
- `02_Runtime` 随数据合同、查询、验证和产品实现演化；
- `03_Evolution` 只保存筛选后的长期依据，新增较少，已有历史更偏向补充 / 勘误而非任意重写；
- `docs/` 承担当前正式定义、原则和规范，因此实质修改应最谨慎。

## 6. 准入门槛

一份材料只有同时满足以下判断，才应长期进入 Evolution：

1. 它不是当前 Canonical State、Runtime 实现或 Living Specification 的 Primary Home 内容；
2. 原 Issue / PR / Project 完成以后，它仍具有独立阅读、引用、复用或解释价值；
3. 仅依赖 Git history 会明显损失未来理解某项重要研究、实验或决策的能力。

三个条件不能成立时，默认不新增 Evolution Artifact。

## 7. 层级与增长规则

Evolution 默认保持扁平：`Research / Experiments / Decisions` 下直接放 Durable Artifact。

只有当真实积累已经形成稳定主题边界、共同生命周期或明显检索负担时，才新增下一层目录。不得为了预判未来而提前建立 `Shared/`、`Resources/`、`Archive/`、`Projects/`、`Activities/`、`Misc/` 等宽泛容器。

Evolution 本身已经是筛选后的长期记录层，因此默认不再设置 `Active / Archive` 双层生命周期。

## 8. 当前结构迁移

仓库现有 `03_Evolution` 是在旧模型下形成的，仍包含 Prior Art、Audit、Test、Pilot、Evidence、Direction、Architecture、Migration 等混合材料。

后续迁移必须逐件按本 README 的准入门槛判断：

- 应进入 `01_State / 02_Runtime / docs` 的先吸收到对应 Primary Home；
- 仍具长期独立研究 / 实验 / 决策价值的保留并归入新三类；
- 只有工作过程价值的依赖 Issue / PR / Git history，不因“历史”身份永久留在 Repository；
- 删除或移动前必须遵守 Repository Structure Profile 的语义吸收与引用完整性规则。

在完成内容级审计前，不对现有 Artifact 做机械批量删除或仅按文件名重分类。