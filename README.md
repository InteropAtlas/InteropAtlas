# InteropAtlas

**开放、机器可读、可持续计算的互操作性地图。**

InteropAtlas 是一个开放基础设施项目，用于描述彼此独立设计的系统如何交换信息、能力、控制、身份、资源与语义，并通过规则与分析程序持续评估互操作路径、开放覆盖与开放缺口。

项目遵循两个基本原则：

- **架构上通用，维护上聚焦。**
- **当前架构是可演化的设计，而不是不可修改的最终规范。**

InteropAtlas 不按某个行业划定最终边界，而是把 **互操作性（interoperability）** 作为问题边界。

> English summary: InteropAtlas is an open, machine-readable and continuously analyzable map of interoperability.

## 核心架构

当前 v0.1 采用三层架构：

### 1. Facts（事实层）

记录可以查证、引用来源并进行版本控制的事实，例如：

- Standard（标准）、Specification（规范）、Protocol（协议）；
- Capability（能力）；
- Organization（组织）；
- Implementation（实现）；
- Relation（关系）；
- Evidence（证据）。

事实层是 InteropAtlas 的知识底座。GitHub 中的 YAML 数据将作为初期的 Source of Truth（事实源）。

### 2. Rules & Engine（规则与分析引擎层）

记录判断规则，并由 InteropAtlas Engine（InteropAtlas 分析引擎）读取事实数据进行计算，例如：

- 数据验证；
- 关系图构建；
- 互操作路径搜索；
- 场景约束匹配；
- Openness Policy（开放性判定规则）；
- Open Gap（开放缺口）检测。

### 3. Assessments（动态评估结果层）

保存或生成某个时间点、某套规则和某个场景下得到的分析结果，例如：

- Gap Assessment（缺口评估）；
- Path Assessment（路径评估）；
- Coverage Assessment（覆盖度评估）；
- Compatibility Assessment（兼容性评估）。

Open Gap（开放缺口）原则上不被视为永久事实，而是基于事实、场景、约束、开放性规则和时间得到的动态评估结果。经人工确认的重要缺口可以进一步形成长期跟踪的 Gap Case（缺口案例）。

核心数据流为：

```text
Facts（事实）
    ↓
Rules & Engine（规则与分析引擎）
    ↓
Assessments（动态评估结果）
```

这套架构目前用于指导 v0.1，但允许随着真实数据实验和程序实现继续调整。

## 先用项目自身做实验

InteropAtlas 将优先收录**项目自身实际依赖或使用的标准、规范、协议和技术**，作为第一批小范围实验数据。

这样可以同时验证两件事：

1. InteropAtlas 的数据模型、关系模型和分析程序能否真实工作；
2. InteropAtlas 自身采用的技术是否存在更开放、更合适或更可持续的替代方案。

这意味着项目将尝试对自己的技术栈进行“自我描述”和“自我检查”。例如 YAML、JSON、JSON Schema、Git、HTTP、URI、Unicode、语言标签等实际使用到的标准或规范，都可以成为首批候选对象。

收录某项技术不等于认定它是开放标准，也不等于认定它是最佳方案。InteropAtlas 应记录事实、比较替代方案，并让具体结论来自明确场景和规则下的评估。

## 语言策略

InteropAtlas 采用 **中文优先、英文机器标识、中英双语知识字段** 的策略。

- 人类可读的主文档：中文优先。
- 稳定 ID、目录名、字段名、Schema、API、关系类型：使用英文。
- 名称、描述、定义等知识字段：设计为中英双语。
- 标准、组织、协议等专有名称保留官方原文，并可附中文名称或译名。

详见 [`docs/language-policy.zh-CN.md`](docs/language-policy.zh-CN.md)。

## 仓库结构

当前结构仍在演化。主要目录包括：

```text
standards/       标准、协议、规范及相关技术的结构化事实
capabilities/    互操作能力
scenarios/       互操作场景及约束
organizations/   标准组织、项目、基金会及相关机构
schemas/         数据结构与验证规则
docs/            架构、方法论、治理和研究文档
tools/           InteropAtlas Engine 及其他验证、分析、转换工具
gaps/            早期缺口数据；将逐步迁移到动态评估/缺口案例模型
```

初期计划使用 YAML 作为适合人类编辑的源数据格式，并通过 JSON Schema 进行验证。未来可以从同一事实源生成 JSON、RDF、图数据库、API、网站视图与动态评估结果。

## 范围

如果一个规范或技术定义、实现、约束，或直接影响两个及以上实体如何交换信息、能力、控制、身份、资源、语义、协调或行为，就可以进入候选范围。

当前主动维护的核心范围聚焦于：感知、通信、数据表达、计算、存储、时间同步、身份、安全、发现、语义、Agent（智能体）、协调、控制、执行与反馈。

## 许可证

InteropAtlas 使用多许可证：

- **软件代码：** Apache License 2.0
- **结构化事实数据：** CC0 1.0 Universal
- **原创文档与研究内容：** Creative Commons Attribution 4.0 International（CC BY 4.0）
- **名称、Logo 与商标：** 不包含在上述授权中，后续单独维护商标政策。

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准全文、规范文本、商标、Logo 以及其他第三方材料仍受各自权利与许可证约束。

## 项目状态

**Pre-Alpha / v0.1 设计阶段。**

本体、Schema、规则、分析引擎和初始数据集仍在设计中，当前允许破坏性变更。真实标准的早期收录首先服务于架构验证，而不是追求目录数量。

## 网站

计划使用 **interopatlas.org** 作为主要公共域名。
