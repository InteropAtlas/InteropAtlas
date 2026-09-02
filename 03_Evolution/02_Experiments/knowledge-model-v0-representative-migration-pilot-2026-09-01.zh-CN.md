# Knowledge Model v0 Representative Migration Pilot

<!-- InteropAtlas Document Metadata v0
Document Status: experiment_record
Document Created At: 2026-09-01T23:32:42+08:00
Document Updated At: 2026-09-01T23:32:42+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

Date: 2026-09-01  
Parent: #61  
Pilot issue: #75

## 1. 目的

本 Pilot 不尝试全量迁移，而是回答一个更小但更关键的问题：

> 已批准的 Knowledge Model v0、Kind Registry、Schema、Relation compatibility、Machine Review 和 Human Route dual-read，能否一起承载一组真实 Canonical Data，而不破坏稳定 ID、Graph、Query 和网站页面？

因此，本次只迁移一个具有代表性的最小切片，并把“不应迁移的对象”也作为测试结果保留下来。

## 2. 迁移切片

### Identity Objects

| Stable ID | Legacy | v0 | 目的 |
| --- | --- | --- | --- |
| `automated_build_deployment` | `capability` | `concept / capability` | 验证 Capability Strong Profile |
| `engine_v0_1_bootstrap` | `scenario` | `concept / scenario` | 验证 Scenario Strong Profile 与结构化 `requires` |
| `forgejo_actions` | `implementation / platform_service` | `system / platform_service` | 验证 System + Implementation Profile |
| `github_actions` | `implementation / platform_service` | `system / platform_service` | 验证同一 kind 的多对象查询与比较 |
| `apple` | `organization` | `agent / organization` | 验证 Agent + Organization Profile |

所有 Stable ID 保持不变。

### Controlled Vocabulary

现有真实数据中的 `platform_service` 明确标识一个持续维护的平台服务，不等同于纯软件包，也不需要为了迁移压扁为较宽泛的 `service` 或 `platform`。

因此将其注册为：

```text
platform_service
family = system
profiles = [implementation]
status = active
```

这属于受控词汇补充，不改变四个 Core Identity Families。

### Relation

`engine_v0_1_uses_semver` 从 Legacy `{type,id}` endpoint 迁移到：

```yaml
source: engine_v0_1_bootstrap
relation: uses
target: semantic_versioning_2_0_0
```

用于验证稳定 ID 是 Relation endpoint 的唯一身份来源。

## 3. 明确不迁移的负样本

### 3.1 Normative Artifact + `maturity`

`semantic_versioning_2_0_0` 等 Legacy Standard 的 Reality Identity 可以较安全地判断为 Artifact，但当前对象仍把 `maturity` 作为对象内字段。

已批准模型要求：成熟度、推荐度、适用性、置信度等评价属于 Assessment，而不是对象的固有身份属性。

因此本 Pilot **不为了覆盖 Artifact family 而把这些记录直接宣布为完整 v0 对象**。这不是失败，而是在真实数据中验证了 Fact / Assessment 边界确实需要后续显式迁移路径。

### 3.2 Relation + bare `confidence`

`forgejo_actions_alternative_to_github_actions` 仍保留 Legacy `confidence: 0.95`。当前记录没有显式 assessor / basis，无法把这一数值安全提升为已批准的 Assessment 语义。

因此本 Pilot 不迁移该 Relation，只把它作为后续 Statement / Assessment 工作的真实样本。

## 4. Pilot 实际发现的问题

真实数据迁移比 synthetic test 多暴露了两类问题。

### 4.1 YAML 日期类型被 Schema 正确拦截

`apple` 的旧数据写成：

```yaml
accessed: 2026-09-01
```

PyYAML 会把这一值解析成日期对象，而 v0 Base Object Schema 要求来源日期是字符串。第一次 Machine Review 因此产生 2 条 `IA-MR-003` 并 FAIL。

修正为：

```yaml
accessed: "2026-09-01"
```

这说明 Machine Gate 已经能在“旧数据进入 v0 合同”的真实迁移时发现过去没有暴露的序列化差异。

### 4.2 Capability Query 暴露了上下文泄漏

Pilot 首次通过后，`automated_build_deployment` 的能力查询虽然正确找到 Forgejo Actions 与 GitHub Actions，却同时返回了两个与该能力无关、且没有 capability context 的 `alternative_to` Relation。

根因是旧查询逻辑把“没有 capability context”解释成“适用于任意 capability”。这会产生假阳性。

修正规则：

> capability-specific query 只接收**显式声明匹配 capability context** 的 Relation；没有上下文的全局 Relation 不能被自动推断为适用于任意能力。

因此该查询现在应只返回：

```text
forgejo_actions --alternative_to--> github_actions
```

这不是为了让迁移测试“看起来通过”而修改结果，而是 Pilot 发现并修复了一个原有 Query 语义错误。

## 5. 必须通过的 Gate

1. Stable ID 不变；
2. v0 Identity records 通过 Registry + Schema；
3. Graph reference issues = 0；
4. `automated_build_deployment` supportability query 只返回该能力明确记录的 Implementations 与 capability-scoped alternatives；
5. Forgejo Actions 仍被识别为 open-source + self-hostable；
6. Human Route 能继续生成 Capability / Implementation / Standard 页面；
7. 原有 public object route 不因 `type` 迁移而变化；
8. Machine Review deterministic errors = 0；
9. Legacy compatibility warnings / semantic-review records 可以存在，但不能伪装成 deterministic error；
10. 不修改 Ruleset，不启用全库 Schema enforcement，不进行全量 Canonical migration。

## 6. 解释边界

本 Pilot 验证的是：

> **v0 机器合同可以在真实 Canonical Data 中开始工作。**

它不意味着：

- 所有 Legacy 对象已经可自动迁移；
- `reference_project` 已完成逐对象 Identity Target audit；
- Assessment / generic Statement 已有完整 Canonical Schema；
- 可以立刻开启 repository-wide enforcement；
- 可以跳过 Human Interface 阶段。

## 7. Pilot 后的决策规则

如果所有 Gate PASS：

- #61 的 Schema / Compatibility Design + Representative Migration Pilot 可以视为完成；
- 后续大规模迁移必须另开工作项，并继续保留 Semantic Review；
- Foundation 主路线应从“机器怎么执行这些规则”转向“人怎么理解、浏览和使用这些知识”；
- Artifact Assessment、Legacy `reference_project`、边界 Standard kinds 与 open-source-project Identity Target 作为显式 migration debt 进入后续队列，而不是阻塞 Human Interface 主路线。

如果 Gate FAIL：

- 先修复模型/Engine/Schema，不扩大迁移范围。
