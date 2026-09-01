# InteropAtlas Knowledge Model v0 — Schema / Compatibility Design v0.2

> 状态：**Consolidated Draft / High-impact Design — NOT IMPLEMENTED**
>
> Work Item：#61
>
> 上游：#58 / PR #60；本版吸收 `schema-compatibility-design-audit-v0.1.zh-CN.md`
>
> 本文件取代同分支 v0.1 Draft 作为当前待审核设计。

## 1. Owner View

现在要解决的不是“重新写 121 个对象”，而是：

> **先让机器同时听懂旧语言和新语言。**

顺序：

```text
Semantic Normalization
机器理解 Legacy + v0
        ↓
Vocabulary / Schema / Validator
机器知道什么写法合法
        ↓
GitHub Actions Machine Gate
不合格 PR 自动挡住
        ↓
少量 Migration Pilot
        ↓
确认 Graph / Query / 页面都没坏
        ↓
才考虑全量迁移
```

---

# 2. 核心机器模型

## 2.1 Runtime `record_class`

机器先区分“这条记录是什么类型的记录”：

```text
identity
statement
view
finding
```

这是 **Runtime Normalized Descriptor**，v0 不要求所有 YAML 增加 `record_class:` 字段。

### Identity

才拥有批准的 Core Identity Family：

```text
concept
artifact
system
agent
```

### Statement

当前最重要 Profile：

```text
relation
```

### View

当前 `map`。

### Finding

当前 `open_gap` 暂时归入 provisional finding；后续 #10 / Curation 再决定 Assessment / workflow 的精确拆分。

因此：

> `relation / map / open_gap` **不是第五、第六、第七个 Core Identity Family**。

---

# 3. v0 Identity Object Contract

新模型的最小身份字段：

```yaml
id: stable_id
type: concept | artifact | system | agent
kind: controlled_term
name_zh: ...
name_en: ...
```

其中：

- `id` = 稳定机器身份；
- `type` = Core Identity Family；
- `kind` = family 内具体身份；
- Strong Profiles = Validator 根据 `type + kind` 自动选择；
- roles / authority = 正交语义。

## Decision A — Canonical Data 不写冗余 `profile:`

推荐：

```yaml
type: concept
kind: capability
```

而不是：

```yaml
type: concept
kind: capability
profile: capability
```

原因：Profile 是机器合同，不需要重复成为事实字段。

---

# 4. Kind Vocabulary Registry

## Decision B — Core Schema 不写死全部 kind enum

Core JSON Schema 只检查：

```text
kind 是合法 machine identifier
```

独立 Vocabulary Registry 管理：

```text
term
family
definition
status
aliases
profiles[]
```

逻辑示例：

```json
{
  "capability": {
    "family": "concept",
    "status": "active",
    "profiles": ["capability"]
  },
  "standard": {
    "family": "artifact",
    "status": "active",
    "profiles": ["normative_artifact"]
  },
  "software": {
    "family": "system",
    "status": "active",
    "profiles": ["implementation"]
  },
  "organization": {
    "family": "agent",
    "status": "active",
    "profiles": ["organization"]
  }
}
```

Registry 内部允许 `profiles[]`，但对象本身不写 profiles。

## 4.1 为什么 Registry 独立

这样：

```text
新增一个正常 kind
≠
修改 Core ontology
```

同时又不会放任自由标签。

## 4.2 `other` 禁止作为长期通用 term

如果对象无法归类：

```text
→ vocabulary_gap
→ Semantic Review
→ 决定复用 / 新增 term / 拆 identity
```

而不是：

```text
kind: other
```

## 4.3 Gate 条件

在第一条 v0 Canonical Object 被允许 merge 前：

> **Kind Registry Validator 必须已经进入 Machine Gate。**

否则 Core Schema 只有 pattern check，不足以约束语义。

---

# 5. 初始 Kind Space

## Concept

```text
capability
scenario
need
constraint
method
methodology
framework
conceptual_model
guideline
principle
heuristic_set
practice
approach
convention
workflow_pattern
architecture_pattern
```

## Artifact

```text
standard
specification
protocol
profile
interface_specification
publication
guidance_document
dataset
distribution
schema
format
report
release
reference_architecture
```

## System

```text
software
library
tool
service
platform
hardware
firmware
design_system
data_project
knowledge_base
registry
catalog_system
platform_mechanism
```

## Agent

```text
person
organization
project_team
community
software_agent
```

这是 v0 seed vocabulary，不是封闭世界。

---

# 6. Strong Profiles

## Capability

```yaml
type: concept
kind: capability
```

复用现有：

```text
category
layers
domains
parent_capabilities
constraints
```

## Scenario

```yaml
type: concept
kind: scenario
```

复用：

```text
actors
requires
environment
success_criteria
```

## Normative Artifact

适用于明确的标准 / 规范发布物。

可复用：

```text
domains
layers
system_roles
capabilities
communication_models
transports
official_url
versions
```

但当前：

```text
maturity
vendor_neutrality
```

必须进入 Fact / Assessment 审计，不能原样当永恒 identity property。

## Implementation System

适用于：

```text
software / library / tool / service / platform / hardware / firmware
```

复用：

```text
capabilities
provider
open_source
self_hostable
license_expression
deployment_models
```

`reference_implementation` 长期改为 role，不作为稳定 System kind。

## Organization Agent

```yaml
type: agent
kind: organization
```

复用：

```text
organization_kind
jurisdiction
domains
official_url
governance_notes
```

`open_source_project` 必须做 identity audit。

---

# 7. Semantic Normalization / Dual-read

这是第一项实现工作。

Engine 对每个 source record 生成内部 descriptor：

```text
record_class
family
kind
profiles[]
legacy_type
migration_status
```

它是 runtime 数据，不写回 Canonical YAML。

所有 Graph / Query / Renderer 逐步改为依赖 normalized predicates，而不是 raw legacy type。

## 最少 predicates

```text
is_identity(record)
is_capability(record)
is_scenario(record)
is_implementation_system(record)
is_organization_agent(record)
semantic_family(record)
semantic_kind(record)
```

---

# 8. Revised Legacy Compatibility Matrix

| Legacy | Normalized semantic result | 自动？ |
|---|---|---:|
| `capability` | identity / concept / capability | ✅ |
| `scenario` | identity / concept / scenario | ✅ |
| `implementation` | identity / system / existing kind | ✅ 大部分 |
| `organization` | identity / agent / organization | ✅ 大部分 |
| `standard` | identity / artifact for clearly-artifact kinds | ⚠ 部分 |
| `reference_project` | unresolved Identity Target | ❌ |
| `relation` | statement / relation | ✅ |
| `map` | view | ✅ |
| `open_gap` | provisional finding | ⚠ 后续 Profile |

## 8.1 Implementation exceptions

```text
kind = reference_implementation
```

不能自动映为新 System kind。

需要：

```text
现实 System kind
+
role = reference_implementation
```

## 8.2 Organization exceptions

```text
organization_kind = open_source_project
```

需要判断 stable ID 指：

```text
community / governance actor → Agent
engineering project → System
```

## 8.3 Standard exceptions

Legacy `standard.kind`：

```text
standard / protocol / specification / format / profile
```

通常可以自动映 Artifact。

但：

```text
api / interface / device_class
```

必须 Identity Target Audit。

因为它们可能是：

```text
发布的规范 Artifact
OR
抽象 API / Interface / Device Class Concept
```

## 8.4 Reference Project

全部逐对象审核，不做 bulk mapping。

---

# 9. Engine Compatibility

## 9.1 当前问题

现在 Graph / Query 直接判断 Legacy type：

```text
capabilities ref expects target.type == capability
implementation query expects object.type == implementation
```

这意味着直接改第一条数据就可能破 Query。

## 9.2 新规则

调用者不自己判断 Legacy/v0。

统一用 semantic predicates：

```text
is_capability(target)
is_implementation_system(object)
```

迁移 0%、10%、100% 时查询语义保持一致。

---

# 10. Relation References

## Decision C — v0 Canonical Relation refs 使用 ID-only

当前：

```yaml
source:
  type: implementation
  id: forgejo_actions
```

推荐迁向：

```yaml
source: forgejo_actions
```

原因：

> Stable identity 是 ID，不是对象当前 family。

对象从 `implementation` 迁为 `system` 不应迫使所有 Relation 重写。

## Compatibility

Legacy `{type,id}` 继续读取。

迁移期：

```text
unknown ID
→ ERROR

legacy type hint stale
→ compatibility warning

ID-only
→ canonical v0 PASS
```

## v0 scope

Pilot 阶段 Relation source / target 只引用 Identity Object ID。

暂不顺带设计任意 Statement→Statement 引用。

---

# 11. Relation = Relationship Statement

Relation 继续演进，不建第二套关系系统。

逻辑目标：

```yaml
id: ...
type: relation
source: object_a
relation: compatible_with
target: object_b
context:
  capabilities: [...]
  scenarios: [...]
  version_context: ...
  valid_from: ...
  valid_to: ...
  conditions_zh: ...
  conditions_en: ...
evidence:
  - url: ...
    title: ...
    accessed: ...
assertor: agent_id
```

字段名在 Implementation PR 最终冻结。

## Legacy context

```text
capability_context
scenario_context
conditions_zh/en
```

由 normalization 映射到统一 context。

## Legacy `confidence`

继续读取，但 v0 暂不新增裸 `confidence`。

其未来语义由 #10 Evidence / Trust Profile 明确为 Assessment。

---

# 12. Evidence

## Object `sources`

继续作为：

> Identity / basic object metadata source

## Statement `evidence`

每条 Relation / explicit Statement 可以拥有独立 Evidence。

因此：

```text
对象官网
≠
对象所有 Claim 的统一证据
```

v0 Evidence item 先复用现有 source 的：

```text
url
title
language
accessed
```

以后再按真实需求扩展 source artifact ID / fragment / archive 等。

---

# 13. Missing Semantics

机器合同明确：

```text
missing field = not recorded
```

而：

```yaml
open_source: false
```

= known false。

需要明确 unknown / none 时使用 explicit Value State：

```yaml
state: unknown
```

或：

```yaml
state: none
```

普通 `null` 不作为万能语义。

---

# 14. Schema / Registry Physical Strategy

现有 Engine 只递归读取 YAML Canonical Data；JSON Schema 文件不会进入 Object Loader。

因此后续机器合同资源建议继续使用 JSON，并与现有 Schema 共置，例如逻辑候选：

```text
01_State/01_Objects/object-kind.vocabulary.json
01_State/01_Objects/identity-object-v0.schema.json
01_State/01_Objects/capability-profile-v0.schema.json
...
```

这不是按语义分类建目录。

继续遵守：

> Schema logical `$id` ≠ Git physical path.

---

# 15. Automated Review Model

## Decision D — Actions 是 Machine Gate，不是 Reviewer identity

```text
Layer 1
GitHub Actions / Validator
确定性检查
        ↓
Layer 2
Human / Agent Semantic Reviewer
语义判断
        ↓
Layer 3
Human Maintainer
High-impact authorization
```

## Machine FAIL

适合确定性拒绝：

```text
YAML parse error
Schema violation
duplicate ID
invalid family/kind
unknown reference
Graph reference issue
broken local link
public route regression
kind not registered
forbidden semantic null
Schema $id/$ref failure
regression test failure
```

## Semantic Review

机器不决定：

```text
Identity Target 是否正确
Evidence 是否真的支持 Claim
是否新增 kind
是否拆对象
是否重复造概念 / 标准
Fact / Assessment 语义判断
```

## High-impact

继续 Human Maintainer：

```text
Core family
breaking Schema
adopted Decision / Governance
License / Security
Ruleset / branch protection
large migration / deletion
stable Specification promotion
Release
```

---

# 16. Machine Review Report

Validator 输出稳定 finding codes。

初始建议：

```text
IA-MR-001 YAML_PARSE_ERROR
IA-MR-002 DUPLICATE_ID
IA-MR-003 SCHEMA_VIOLATION
IA-MR-004 UNKNOWN_REFERENCE
IA-MR-005 INVALID_KIND_FOR_FAMILY
IA-MR-006 GRAPH_REFERENCE_ISSUE
IA-MR-007 FORBIDDEN_NULL_STATE
IA-MR-008 SCHEMA_REFERENCE_ERROR
IA-MR-009 PUBLIC_ROUTE_REGRESSION
IA-MR-010 HIGH_IMPACT_REVIEW_REQUIRED
```

输出：

```text
Human-readable GitHub Job Summary
+
Machine-readable JSON report
```

逻辑结果分为：

```text
FAIL

PASS + SEMANTIC REVIEW REQUIRED

PASS + HIGH-IMPACT REVIEW REQUIRED

PASS / ELIGIBLE
```

`HIGH_IMPACT` 本身不是技术失败。

真正阻止未批准 High-impact Merge，要由后续 Ruleset / required review 实现。

#61 不直接改 Ruleset。

---

# 17. 当前 Actions 基线

仓库目前已经自动做：

```text
repository layout test
graph health
deterministic bootstrap query
site build / renderer smoke test
Markdown local link validation
```

但当前 Runtime dependencies 只有：

```text
PyYAML
Markdown
```

也就是说：

> **JSON Schema 文件存在，但 Schema Validation 还没有真正成为 CI Gate。**

后续 Validator implementation 必须显式增加验证依赖和命令。

---

# 18. v0 Merge Policy

Pilot 期间：

```text
Canonical Object / Relation
Machine PASS
→ 仍需 Semantic Review
```

High-impact：

```text
Machine PASS
→ Semantic Review
→ Human Maintainer Authorization
```

暂不让 Canonical Data 因 CI PASS 直接 auto-merge。

以后如果长期证明某一类变更完全 deterministic，再单独开放低风险 auto-merge。

---

# 19. Representative Migration Pilot

Pilot 只选少量高信息量对象。

## Concept

- 1–2 Capability；
- 1 Scenario；
- 1 Method / Framework（若已进入 Canonical）。

## Artifact

- `yaml_1.2.2`；
- 1 个新收录 Standard；
- Apple HIG boundary case。

## System

- `forgejo_actions`；
- `github_actions`。

## Agent

- 1 个明确 Organization；
- 1 个 `open_source_project` boundary case。

## Relation

- `forgejo_actions_alternative_to_github_actions`；
- 1 个 context-rich Relation；
- 1 个 legacy confidence debt Relation。

## Reference Project

- Apple HIG；
- AGENTS.md。

---

# 20. Pilot Acceptance

必须保持：

```text
Stable IDs unchanged
Public /objects/<id>.html unchanged
Legacy + v0 load together
Graph reference_issues = 0
Edge changes fully explainable
Capability query works
Implementation/System query works
Backlinks work
Relation contexts preserved
Renderer works
Machine Review report works
No folder-derived semantics
```

关键一项 FAIL：

> 不进入全量 migration。

---

# 21. Implementation Order After Approval

```text
I1 Semantic Normalization Layer
        ↓
I2 Kind Registry + Validator skeleton
        ↓
I3 v0 Identity / Strong Profile Schemas
        ↓
I4 Relation ID-only + Context compatibility
        ↓
I5 GitHub Actions Machine Review report
        ↓
I6 Representative Migration Pilot
        ↓
Pilot Audit
        ↓
再决定 Canonical Migration / Enforcement
```

这套顺序故意让：

> **Engine 先学会两种语言，再让数据逐步换语言。**

---

# 22. Approval Decisions

进入 I1 前需要 Maintainer 对以下 4 点批准：

### A
Strong Profile 由 `type + kind` / Registry 推导，不在对象中重复写 `profile:`。

### B
`kind` 使用独立受控 Registry + Validator，不把全部 terms 写死在 Core Schema enum。

### C
Relation canonical refs 逐步迁为 ID-only；Legacy `{type,id}` 只做兼容输入。

### D
GitHub Actions 作为确定性 Machine Gate；Canonical semantic review 和 high-impact authorization 保持独立。

---

# 23. Non-goals

本 Design Approval 不等于批准：

- 全量数据迁移；
- Schema enforcement rollout；
- Ruleset 修改；
- 自动合并 Canonical Data；
- RDF / OWL canonicalization；
- 数据库选型；
- IA Query Language；
- 语义物理目录；
- #10 全部 Trust / Assessment 设计。

---

# 24. Recommendation

当前推荐批准 v0.2 Design，并只进入 **I1 Semantic Normalization Layer**。

I1 本身不修改 Canonical Data；它只是让 Runtime 有统一的：

```text
record_class
family
kind
profiles
semantic predicates
```

因此它是下一步风险最低、杠杆最高的实现工作。
