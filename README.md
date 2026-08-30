# InteropAtlas

**开放、机器可读的互操作标准、能力、关系与开放缺口地图。**

InteropAtlas 是一个开放基础设施项目，用于描述彼此独立设计的系统如何交换信息、能力、控制、身份、资源与语义，并进一步形成可查询、可组合、可验证的互操作关系网络。

项目遵循一个基本原则：**架构上通用，维护上聚焦。** InteropAtlas 不按某个行业划定最终边界，而是把 **互操作性（interoperability）** 作为问题边界。

> English summary: InteropAtlas is an open, machine-readable map of interoperability standards, capabilities, relationships, and gaps.

## InteropAtlas 映射什么

InteropAtlas 不把标准视为一张平面的清单，而是把互操作性建模为一张图。

核心对象包括：

- **Standard / Specification / Protocol（标准 / 规范 / 协议）**：定义技术规则、接口或交换方式的对象。
- **Capability（能力）**：系统需要具备的互操作能力，例如设备发现、实时媒体传输、身份、时间同步、Agent 通信。
- **Scenario（场景）**：具体的互操作需求与约束条件。
- **Relation（关系）**：带上下文的类型化关系，例如 `depends_on`、`implements`、`alternative_to`、`compatible_with`、`bridges_to`。
- **OpenGap（开放缺口）**：某项互操作需求尚不存在充分开放解决方案的位置。

长期目标并不是消灭专有技术，而是尽可能消灭：

> **没有可行开放替代方案的位置。**

## 语言策略

InteropAtlas 采用 **中文优先、英文机器标识、中英双语知识字段** 的策略。

- 人类可读的主文档：中文优先。
- 稳定 ID、目录名、字段名、Schema、API、关系类型：使用英文。
- 名称、描述、定义等知识字段：设计为中英双语。
- 标准、组织、协议等专有名称保留官方原文，并可附中文名称或译名。

例如：

```yaml
id: device_discovery
name_zh: 设备发现
name_en: Device Discovery
description_zh: 系统发现可用设备、节点或服务的能力。
description_en: The capability to discover available devices, nodes, or services.
```

机器标识使用英文不是为了规定项目的思考语言，而是为了提高 API、Schema、代码、RDF、CLI、URL 和第三方工具链中的可移植性与国际协作能力。

详见 [`docs/language-policy.zh-CN.md`](docs/language-policy.zh-CN.md)。

## 仓库结构

```text
standards/       标准、协议、规范及相关技术的结构化记录
capabilities/    互操作能力
scenarios/       具体互操作场景及约束
gaps/            Open Gap（开放缺口）及其生命周期数据
organizations/   标准组织、项目、基金会及相关机构
schemas/         用于验证项目数据的机器可读 Schema
docs/            架构、方法论、治理和研究文档
tools/           验证、转换、查询或发布 Atlas 的软件工具
```

初期计划使用 YAML 作为适合人类编辑的源数据格式，并通过 JSON Schema 进行验证。未来可以从同一事实源生成 JSON、RDF、图数据库、API 与网站视图。

## 范围

如果一个规范或技术定义、实现、约束，或直接影响两个及以上实体如何交换以下内容，就可以进入候选范围：

- 信息或数据；
- 能力或服务；
- 控制；
- 身份或信任；
- 资源；
- 语义；
- 协调或行为。

当前主动维护的核心范围聚焦于：感知、通信、数据表达、计算、存储、时间同步、身份、安全、发现、语义、Agent、协调、控制、执行与反馈。

## 许可证

InteropAtlas 使用多许可证，因为软件、事实型结构化数据和文档具有不同的再利用需求。

- **软件代码：** Apache License 2.0
- **结构化事实数据：** CC0 1.0 Universal
- **原创文档与研究内容：** Creative Commons Attribution 4.0 International（CC BY 4.0）
- **名称、Logo 与商标：** 不包含在上述授权中，后续单独维护商标政策。

完整边界见 [`LICENSE.md`](LICENSE.md)。

第三方标准全文、规范文本、商标、Logo 以及其他第三方材料仍受各自权利与许可证约束。InteropAtlas 对某个第三方对象的收录，不构成对该材料的重新授权。

## 项目状态

**Pre-Alpha / v0.1 设计阶段。**

本体、Schema、贡献流程和初始数据集仍在设计中，当前允许破坏性变更。

## 网站

计划使用 **interopatlas.org** 作为主要公共域名。
