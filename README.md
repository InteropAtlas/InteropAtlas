# InteropAtlas

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:49:18+08:00
Document Updated At: 2026-09-01T16:44:53+08:00
Metadata Backfilled At: 2026-09-02T10:49:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

**开放、机器可读、可持续分析的互操作知识地图。**

InteropAtlas 是一个开放基础设施项目，用于描述彼此独立设计的系统如何交换信息、能力、控制、身份、资源与语义，并连接现实世界中与互操作有关的**既有标准、成熟先例、方法与指南、实现、组织、能力、场景、关系、证据与开放缺口**。

它的目标不是只建立一个 Standards Catalog（标准目录），而是逐步映射真实的 **Interoperability Solution Space（互操作方案空间）**，帮助人和机器发现、理解、比较、组合和改进互操作方案。

项目遵循几个基本原则：

- **架构上通用，维护上聚焦。**
- **互操作性是问题边界，而不是某个固定行业。**
- **扩大方案空间覆盖，但严格区分对象身份与权威性。**
- **当前架构是可演化的设计，而不是不可修改的最终规范。**

> English summary: InteropAtlas is an open, machine-readable and continuously analyzable knowledge map of interoperability, connecting normative standards, mature precedents, methods, implementations and open gaps.

项目定义与收录范围见 [`docs/interopatlas-definition-and-scope-v0.2.zh-CN.md`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md)。

## 收录的不是只有“标准”

现实中的互操作建设不仅依赖正式标准，还依赖经过实践验证的项目、方法、实现和治理机制。

InteropAtlas 因此区分并连接多类知识对象：

- **Normative Artifacts（规范性产物）**：Standard、Specification、Protocol、Profile、API / Interface、Format 等；
- **Mature Precedents / Prior Art（成熟先例 / 既有方案）**：成熟知识项目、Landscape、Design System、协作机制、Reference Architecture、长期实践模式等；
- **Methods / Guidelines / Frameworks（方法 / 指南 / 框架）**：设计、分析、文档、治理、验证等方法；
- **Implementations / Tools / Services（实现 / 工具 / 服务）**；
- **Organizations（组织与治理主体）**；
- **Capabilities / Needs / Scenarios（能力、需求与场景）**；
- **Evidence / Sources（证据与来源）**；
- **Relations（关系）**；
- **Assessments / Open Gaps（评估与开放缺口）**。

这些对象可以同时进入 Atlas，但不能混为一谈。一个成熟 Design System 不会因为值得参考就被描述成国际标准；一个正式标准也不会因为缺乏成熟实现就失去其规范身份。

核心原则：

> **Map the solution space, preserve the authority distinction.**
>
> **扩大方案空间覆盖，但保持权威性与对象身份的严格区分。**

## 核心架构

概念上，InteropAtlas 仍以事实、确定性处理与动态评估之间的关系理解系统：

```text
Facts / Current State
        ↓
Rules & Engine / Runtime
        ↓
Assessments / Generated Views
```

仓库物理结构不直接复制这些知识类别，而采用更稳定的生命周期结构：

```text
01_State      当前正式承认什么
02_Runtime    当前如何运行和使用这些状态
03_Evolution  项目如何研究、验证和改变自己
```

物理目录、知识分类和索引 / View 是三个不同层面。对象属于 Standard、Capability、Organization、Method、Implementation 等类别，由其数据字段和关系表达，而不是由文件夹名决定。

## Prior Art / 既有方案调查

在设计新的数据模型、仓库结构、交互方式、治理流程或协作机制前，InteropAtlas 优先执行：

> **Existing Standards & Prior Art Check（既有标准与成熟先例调查）**

基本顺序是：

```text
问题
 ↓
已有标准或成熟先例是否已经解决？
 ↓
能否直接 Adopt？
 ↓
能否 Profile / 组合？
 ↓
能否 Extend？
 ↓
只有真实缺口仍存在时才 Invent
```

`Prior Art` 是调查活动的上位概念，不会成为 Canonical Atlas 中所有对象的统一类型；调查发现的对象仍应分别建模为 Standard、Method、Precedent、Implementation、Organization 等准确身份。

## 先用项目自身做实验

InteropAtlas 将优先收录**项目自身实际依赖或参考的标准、规范、成熟先例、方法、实现与基础技术**，作为第一批小范围实验数据。

这样可以同时验证：

1. InteropAtlas 的数据模型、关系模型和分析程序能否表达真实方案空间；
2. 项目自身采用的技术、方法和协作机制是否存在更开放、更成熟或更可持续的替代方案；
3. Atlas 是否能够区分“正式标准”“成熟先例”“方法”“实现”和“评估”；
4. 实践中暴露出的模型缺口能否反向推动 Atlas 演化。

收录某项对象不等于认定它是开放标准，也不等于认定它是最佳方案。InteropAtlas 应记录事实、证据和身份差异，并让具体结论来自明确场景和规则下的评估。

## 语言策略

InteropAtlas 采用 **中文优先、英文机器标识、中英双语知识字段** 的策略。

- 人类可读的主文档：中文优先。
- 稳定 ID、目录名、字段名、Schema、API、关系类型：使用英文。
- 名称、描述、定义等知识字段：设计为中英双语。
- 标准、组织、协议、项目、方法等专有名称保留官方原文，并可附中文名称或译名。

详见 [`docs/language-policy.zh-CN.md`](docs/language-policy.zh-CN.md)。

## 仓库结构

当前核心结构为：

```text
01_State/
├── 01_Objects/       Canonical Objects + Object Schemas
└── 02_Relations/     Canonical Relations + Relation Schema

02_Runtime/
├── 01_Engine/        Loader / Graph / Query / Renderer 等核心运行代码
├── 02_Tools/         Human / Agent / CI 使用的辅助工具
└── 03_Outputs/       生成物的逻辑区域；并非所有产物都提交 Git

03_Evolution/
├── 01_Research/      Prior Art、研究、Audit、方案比较
├── 02_Experiments/   原型、实验、Dry Run
└── 03_Change/        Proposal、Migration、Transition 等变更材料
```

根目录继续保留 GitHub / 开源项目接口：

```text
.github/
docs/
LICENSES/
README.md
CONTRIBUTING.md
LICENSE.md
AGENTS.md
```

关键规则：

- `01_Objects/` 内不同对象类型平级存放，不再通过 Standard / Capability / Organization 等语义文件夹分类；
- Properties 是 Object / Relation 自身字段，不建立独立目录；
- Schema 与其约束的数据共置，README 给 Human / Agent 看，`*.schema.json` 给机器验证；
- 公共对象地址使用稳定 ID：`/objects/<stable-id>.html`，不依赖 YAML 的物理文件位置；
- 如果未来文件数量过大，需要分片时，应优先采用 ID / 哈希等非语义分片，而不是重新用对象类别建目录。

初期使用 YAML 作为适合人类编辑的事实源格式，并逐步通过 JSON Schema 与 Validator 进行验证。未来可以从同一事实源生成 JSON、RDF、图数据库、API、网站视图与动态评估结果。

## 范围

如果一个对象满足以下至少一项，就可以成为候选：

- 直接定义实体如何交换信息、能力、控制、身份、资源、语义、协调或行为；
- 为这种互操作提供实现；
- 为互操作系统的设计、治理、验证、发现、选择、组合或维护提供成熟方法；
- 是具有可复用价值的成熟互操作案例 / 先例；
- 为相关事实或 Assessment 提供必要证据；
- 揭示现有方案空间中的 Open Gap。

当前主动维护的核心范围聚焦于：感知、通信、数据表达、计算、存储、时间同步、身份、安全、发现、语义、Agent（智能体）、协调、控制、执行与反馈，以及支撑这些系统互操作的 Human Interface、协作、治理和知识组织方法。

范围扩大并不意味着收录泛知识。与互操作没有明确关系、缺乏可靠来源、只有营销表述或无法提取可复用价值的对象，默认不进入核心维护范围。

## 许可证

InteropAtlas 使用多许可证：

- **软件代码：** Apache License 2.0
- **结构化事实数据：** CC0 1.0 Universal
- **原创文档与研究内容：** Creative Commons Attribution 4.0 International（CC BY 4.0）
- **名称、Logo 与商标：** 不包含在上述授权中，后续单独维护商标政策。

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准全文、规范文本、商标、Logo 以及其他第三方材料仍受各自权利与许可证约束。

## 项目状态

**Pre-Alpha / v0.1 设计阶段。**

本体、Schema、规则、分析引擎、收录对象分类和初始数据集仍在设计中，当前允许破坏性变更。真实对象的早期收录首先服务于架构验证，而不是追求目录数量。

## 网站

计划使用 **interopatlas.org** 作为主要公共域名。当前 GitHub Pages 仅作为 Reference Implementation / Test Bed，不是事实源，也不负责反向定义项目规范。
