# Human Evidence / Assessment Presentation v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Working Product Contract
Document Created At: 2026-09-02T12:55:00+08:00
Document Updated At: 2026-09-02T12:55:00+08:00
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> Status: Working Product Contract
>
> Parent: #16 / Work Item: #110

## 1. 目标

第一批 Human Evidence / Assessment presentation 只解决一个信息职责问题：用户应能看出 **Canonical Fact、Canonical `sources`、以及 InteropAtlas 自己的说明 / 边界 / assessment-like notes 不是同一类内容**。

本轮不修改 Knowledge Model，也不建立完整 Evidence ontology。

## 2. Presentation contract

### Canonical facts

对象的基本字段、版本、开放性、能力和关系继续由 Canonical State 决定。Renderer 只投影视图，不创建新的事实。

### Sources / supporting material

`来源与依据` 区块只从对象当前的 Canonical `sources` 字段读取。

Renderer MUST NOT：

- 维护第二份来源列表；
- 因为页面需要来源而自行补造 URL；
- 把 IA notes 当作第三方权威来源。

### InteropAtlas notes / assessment-like content

`notes_zh` 在本 slice 中显示为 `InteropAtlas 说明与评估`，并明确声明它是 IA 的说明、边界或评估性记录，不等同于第三方权威来源。

这只是 Human View 的角色区分；本轮不宣称所有 `notes_zh` 都已经完成正式 Fact / Assessment ontology 分类。

### Missing evidence

如果当前对象没有 `sources`，Human View 应明确显示：`当前记录未提供来源 / Evidence 链接`。

该状态表示 **not recorded / unknown at this layer**，不得渲染或推导为 false、none、事实不存在或事实已被否定。

## 3. Representative slice

第一批只验证：

- `forgejo_actions` — Implementation，已有多个 `notes_zh` 与多个 `sources`，用于验证角色分离；
- `yaml_1.2.2` — Standard，已有 `sources`、无同类 IA notes，用于验证不会凭空生成 assessment 区块。

其他 Resource family 暂不强制迁移，避免把产品 slice 扩成全站重构。

## 4. Regression boundary

本变化不得改变：

- stable Resource URLs；
- Canonical object / relation data；
- Search index semantics；
- Compare semantics；
- Breadcrumb；
- Local Map；
- JS-disabled core reading；
- narrow-screen reflow。

Machine Review / Schema / Relation compatibility / Graph / Compare deterministic regression 与 Browser E2E 继续作为验证证据。

## 5. 后续问题

本 slice 完成后，再根据真实使用决定是否需要：

- field / claim level evidence binding；
- Source 与 Evidence 独立 Canonical object；
- Assessment 的正式结构化模型；
- authority / confidence / freshness presentation；
- Evidence 在 Compare 中的逐维展开。

这些都不是 v0.1 的隐含承诺。
