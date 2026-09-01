# InteropAtlas 自身产生的方法、规范、标准与 Skills（暂定方向）

> 状态：Future Direction / Provisional Note（后续方向 / 暂定记录）。记录项目建设过程中产生可复用方法论与规范的治理需求，不冻结编号、仓库结构或标准化流程。

## 背景

InteropAtlas 在建设过程中很可能不断产生新的可复用成果，例如：

- 数据建模方法；
- Relation vocabulary（关系词汇）设计规则；
- 标准收录规范；
- Evidence / Source 记录规范；
- Renderer / View 生成约定；
- Open Gap 评估方法；
- Coverage 评估方法；
- Atlas ↔ Engine 实践反馈方法；
- Agent 使用流程与 Skills；
- 仓库结构、命名、版本、发布与迁移约定。

这些成果如果只存在于主仓库代码或零散讨论中，会造成两个问题：

1. 项目自身未来重复发明同一套方法；
2. 外部项目即使认可这些方法，也难以独立理解、实现和复用。

因此需要逐步建立“项目自产知识的产品化与标准化路径”。

## 暂不假设“所有东西都是标准”

不同成果应区分其成熟度和性质。暂定可以考虑以下层级：

```text
Experiment / Note
实验与设计记录
      ↓
Methodology / Guide
方法论与指南
      ↓
Specification
明确、可实现的规范
      ↓
Standard / Profile
稳定、版本化、可独立符合的标准或配置文件
```

Skill（技能）不一定处于这条成熟度链上。它更像是某个方法论或规范的可执行实现：

```text
Methodology / Specification
          ↓
        Skill
          ↓
Agent / Tool 实际执行
```

因此“方法论、标准、Skill”不应互相替代。

## 需要进一步研究的问题

### 1. 标识体系

未来每个正式规范/标准需要稳定 ID，但当前不冻结格式。

待研究：
- 是否采用项目缩写 + 序列号；
- 是否包含年份；
- 日期究竟属于 ID、版本还是发布日期；
- 是否需要人类友好 short name；
- 是否需要永久 URI / URL；
- 改名后 ID 是否保持稳定。

例如 `IA-20260831-001` 目前只应视为示意，而不是决定。

### 2. 仓库边界

“每个标准一个 GitHub 仓库”是候选方案，但不能默认适用于所有产物。

待比较：
- monorepo；
- 每个正式规范独立仓库；
- 一个标准族一个仓库；
- 主规范独立仓库 + 实现/测试分离；
- 何时从主仓库孵化并独立出去。

### 3. 规范仓库结构

未来需要研究统一模板，例如：
- README / Overview；
- normative specification；
- examples；
- schemas；
- conformance tests；
- changelog；
- governance；
- security / IPR / licensing；
- versioning / releases；
- machine-readable metadata。

### 4. 生命周期

需要定义从想法到正式规范的阶段，例如：

```text
Idea
 ↓
Experiment
 ↓
Draft
 ↓
Review
 ↓
Candidate
 ↓
Stable
 ↓
Revised / Superseded / Deprecated
```

应优先参考成熟标准组织的流程，而不是自行发明完整治理体系。

### 5. 与 InteropAtlas 主地图的关系

IA 自己产生的规范不应成为“地图外的特殊对象”。

一旦达到可公开引用的程度，也应像其他外部标准一样被主 Atlas 收录：

```text
IA 内部实践产生方法/规范
          ↓
独立、版本化、可引用的公开产物
          ↓
InteropAtlas 将其作为 Standard / Specification / Methodology 重新收录
          ↓
与其他标准建立 alternative_to / inspired_by / profile_of / implements 等关系
```

这样可以避免“我们自己的标准天然高于别人”的特殊待遇。

## 核心原则（暂定）

1. **先复用，后创造。** 建立新规范之前必须做 Prior Art（既有方案）调查。
2. **先记录方法，再决定是否标准化。** 不把每个内部习惯都升级为标准。
3. **标准必须解决独立实现或协作中的真实互操作问题。**
4. **稳定标识与版本必须分开考虑。** ID 不应轻易随版本变化。
5. **规范文本、机器可读定义、测试与实现尽量分层。**
6. **IA 自己产生的标准也接受 IA 自己的收录、比较与批判。**
7. **避免过早成为“标准组织”。** 先建设可复用的开放方法和规范，治理结构随真实协作者和真实需求演进。

## 与当前路线的关系

这实际上可能形成一条独立于“人类可读”和“机器可用”的路线：

**Governance / Standardization Route（治理与标准化路线）**。

它处理的不是“人怎么看”和“机器怎么算”，而是：

> 一个新方法如何提出、验证、评审、编号、版本化、发布、实现、修订和废弃。

是否把它正式提升为 InteropAtlas 的第三条路线，需要在参考 IETF、W3C、开放源码规范项目等成熟实践后再决定。