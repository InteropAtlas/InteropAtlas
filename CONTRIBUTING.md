# 为 InteropAtlas 贡献

InteropAtlas 当前处于 Pre-Alpha 设计阶段。贡献应优先保证：事实可验证、来源明确、对象类型区分清晰、结构机器可读。

## 如何参与一个任务

InteropAtlas 使用 GitHub Issues 作为当前统一的可执行任务入口。人类贡献者与未来的 AI / Agent 原则上使用同一套公开协作流程。

最小流程：

```text
找到 Issue
   ↓
确认目标 / 范围 / 完成条件
   ↓
留言说明希望接手，避免重复劳动
   ↓
工作并保持必要进展可见
   ↓
提交较小、可审查的 Pull Request
   ↓
独立 Review
   ↓
Merge / Done
```

- 默认一个普通任务同一时间只有一个主要执行者；大型任务应优先拆成互不冲突的子任务。
- 如果 Issue 已有人执行，请先讨论，不要无意重复同一份工作。
- 当前无法自行设置 Assignee 的外部贡献者，可以直接在 Issue 留言说明希望接手，由维护者确认。
- Pull Request 应关联对应 Issue，并说明做了什么、依据是什么、还存在哪些已知问题。
- 长期无进展的任务可以在沟通后重新开放给其他贡献者；具体超时 / Lease 机制尚未冻结。
- AI / Agent 参与时仍需遵守与人类贡献相同的 Evidence、Review、许可证和质量要求。

总体优先级见 `docs/roadmap.zh-CN.md`；当前协作机制的实验记录见 `docs/open-collaboration-route-v0-notes.zh-CN.md`。

## 基本原则

- 能使用权威一手来源时，优先使用一手来源。
- 明确区分标准、协议、规范、API、格式、实现、组织、项目和产品。
- 不要把“开放性”压缩成单一布尔值。应分别记录规范可访问性、治理开放度、专利/版税条件、开源实现、认证限制、厂商中立性等事实维度。
- 关系应被视为需要证据支持的、带上下文的事实主张。
- 除非再发布权利清晰，否则不要复制第三方规范全文。
- 优先提交较小、可审查的 Pull Request。

## 语言规则

项目采用“中文优先、英文机器标识、中英双语知识字段”。

- `id`、字段名、枚举值、关系类型、路径、Schema 和 API 标识使用英文。
- 中文是当前主文档和主要解释语言。
- 名称、描述、定义等知识字段尽可能同时提供 `*_zh` 与 `*_en`。
- 对官方名称、标准编号、组织名、协议名等，不应为了中文化而替换其正式原文。
- 翻译存在不确定性时，应保留原文并明确标记译名，而不是把译名当成新的官方名称。

示例：

```yaml
id: device_discovery
name_zh: 设备发现
name_en: Device Discovery
description_zh: 系统发现可用设备、节点或服务的能力。
description_en: The capability to discover available devices, nodes or services.
```

完整规则见 `docs/language-policy.zh-CN.md`。

## 贡献内容的许可证

提交贡献即表示，你同意按照 `LICENSE.md` 中与目标内容对应的许可证提供该贡献：

- 软件及功能性 Schema：Apache-2.0；
- 原创结构化事实数据：CC0-1.0；
- 原创文字文档与研究内容：CC BY 4.0。

不要提交无权再发布的第三方材料；如果第三方材料允许收录，应保留必要的归属和许可证信息。

## 数据工作流

初期计划使用人类可编辑的 YAML 作为事实源，并使用 JSON Schema 校验。未来可从同一事实源生成 JSON、RDF、图数据库、API 与网站表示。

本体与 Schema 目前尚未稳定。v0.1 设计阶段允许破坏性变更。
