# Seed Experiment 01：用真实对象反向测试 InteropAtlas

> 状态：进行中
>
> 目标不是追求数量，而是用 InteropAtlas 自身依赖的技术和外部标准地图项目测试当前数据模型。

## A. InteropAtlas 自身实际使用或明确依赖的首批对象

当前已录入：

- YAML 1.2.2：初期人工编辑的数据序列化格式；
- JSON RFC 8259：JSON 数据模型与交换格式；
- JSON Schema 2020-12：InteropAtlas 当前 Schema 的描述与验证规范；
- HTTP RFC 9110：未来网站/API 和 Web 资源交互相关的核心协议语义；
- URI RFC 3986：Schema `$id`、来源 URL 和资源标识的基础规范；
- Git Wire Protocol v2：版本控制技术体系中的网络协议对象；
- Unicode 17.0：中英双语文本与现代数据格式的字符体系基础；
- BCP 47 / RFC 5646：语言标签与多语言元数据的基础规范。

对应新增能力对象包括：

- `data_serialization`（数据序列化）
- `schema_validation`（数据结构验证）
- `resource_identification`（资源标识）
- `web_resource_transfer`（Web 资源传输）
- `version_control`（版本控制）
- `text_encoding`（文本字符编码）
- `language_identification`（语言标识）

## B. 外部标准地图 / 互操作框架参考对象

当前已录入：

- W3C AI KR：分类法、词汇、标准清单与缺口分析；
- NIST Smart Grid Interoperability Framework：场景、标准、缺口、行动计划、测试与认证；
- Industry 4.0 Standards Knowledge Graph（I40KG）：标准本体、关系图和参考架构映射；
- ETSI STF505：IoT 标准全景与缺口分析；
- IEC SRD 63233：智慧城市标准清单与映射方法；
- INA（德国医疗互操作导航器）：标准/配置/指南/模型/架构/软件组件及治理生命周期；
- ITU-T Y.Sup58：IoT、数字孪生与智慧城市全球标准全景；
- IETF Agent Landscape：快速变化的智能体标准工作项与缺口跟踪；
- EUOS（欧洲 ICT 标准化观察站）：跨 ICT 领域标准库、全景分析、缺口分析和专家协作。

为此新增了 `reference_project`（参考项目）对象类型和对应 Schema。这个变化来自真实数据，而不是预先假设。

## C. 第一轮已经暴露出的模型问题

### 1. “标准”不能成为万能对象

YAML、HTTP、URI 可以放入广义的标准/规范对象族，但 Git 整体不是一个单一标准。Git 至少包含软件实现、数据格式、仓库结构、对象模型和传输协议等多个层面。因此当前只先把 Git Wire Protocol v2 作为 `protocol`（协议）记录。

### 2. “标准地图”本身也应该成为 Atlas 中的对象

EUOS、INA、I40KG 和 NIST Smart Grid 等不能合理塞进 `Standard`。它们需要自己的 `reference_project` 对象，以描述覆盖范围、功能、机器可读性、方法和可借鉴经验。

### 3. “项目使用某技术”与“该技术最好”必须分开

InteropAtlas 使用 YAML、Git 或 JSON Schema 只是事实，不构成最佳性、开放性或长期适用性的结论。未来应通过 Scenario（场景）、Openness Policy（开放性判定规则）和 Assessment（评估结果）分析替代方案。

### 4. 自动验证应尽快进入 Engine（分析引擎）

第一次写 Capability（能力）真实数据时已经出现漏填 Schema 必填字段的问题。人工发现可以修正，但规模扩大后必须由 Validator（验证器）自动执行结构验证和跨文件引用检查。

## 下一轮实验

下一轮不应立即追求大量收录，而应围绕这些真实对象补齐：

1. `Relation`（关系）：例如 JSON Schema `uses` JSON；HTTP `uses` URI；InteropAtlas `uses` YAML；
2. `Organization`（组织）：IETF、W3C、Unicode Consortium、IEC、ETSI 等；
3. 更细的开放性事实：规范获取、治理、专利/许可、开源实现、认证、供应商中立性；
4. 第一个 Scenario（场景）：InteropAtlas 自身的“机器可读事实库”技术选择；
5. 第一个 Openness Policy（开放性判定规则）；
6. 用最小 Engine 原型运行验证和第一轮比较。

如果这一轮发现当前 Schema 无法自然表达真实对象，应优先修改模型，而不是强迫真实世界适应模型。
