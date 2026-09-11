# InteropAtlas Knowledge Model v0 — Schema / Compatibility Design v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft / High-impact Design — NOT IMPLEMENTED**
Document Created At: 2026-09-01T21:03:42+08:00
Document Updated At: 2026-09-01T21:03:42+08:00
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

> 状态：**Draft / High-impact Design — NOT IMPLEMENTED**
>
> Work Item：#61
>
> 上游：#58 / PR #60 已批准的 Minimum Knowledge Representation Contract v0.1
>
> 目的：把已经批准的知识语义翻译成可实现的机器合同、兼容层和自动审核 Gate；本文件本身不修改 Canonical Data、不启用 Schema enforcement、不修改 Ruleset。

## 1. Owner View

这一阶段只做一件事：

> **让机器开始理解我们刚刚批准的知识语言，同时保证旧数据还能继续工作。**

简单路线：

```text
旧数据仍能读
        +
新模型有明确机器规则
        ↓
Engine 同时理解 Legacy + v0
        ↓
先迁移少量代表对象测试
        ↓
确认没有把 Graph / Query / 页面弄坏
        ↓
才考虑分批迁移全部数据
```

GitHub Actions 同时成为第一层自动审核 Gate：格式、Schema、引用、Graph 等确定性问题由机器挡住；语义问题交给 Human / Agent Reviewer；高影响方向继续由 Human Maintainer 批准。

---

# 2. 设计原则

本设计必须同时满足：

1. **Stable ID First** — 现有对象 ID 不因模型升级改变；
2. **No Big-bang Migration** — Legacy 与 v0 必须可以短期共存；
3. **Semantic Model ≠ Schema** — Schema 实现已批准语义，不反向发明新语义；
4. **Physical Storage ≠ Semantic Classification** — 不创建 `concept/`、`artifact/` 等物理目录；
5. **Graph-native, database-agnostic** — 关系语义稳定，不绑定某数据库；
6. **Minimal v0** — 不复制完整 Wikibase / RDF / OWL；
7. **Evidence Before Assertion** — Statement Evidence 能够逐步进入机器合同；
8. **Automation is Gate, not Reviewer Identity** — CI 通过是 Evidence，不是治理批准。

---

# 3. A1 — Core Machine Discriminator

## 3.1 v0 Identity Object

新的 Identity Object 机器合同使用：

```yaml
type: concept | artifact | system | agent
kind: <controlled-term>
```

其中：

- `type` = 极少、稳定的 Core Identity Family；
- `kind` = family 内具体身份；
- Stable Profile = 由 `type + kind` 选择机器约束；
- `roles` / `authority` = 正交语义，不塞进 `type`。

### 关键决定：v0 不新增显式 `profile:` 字段

原因：

```yaml
type: concept
kind: capability
```

本身已经足够选择 Capability Profile。

如果再要求：

```yaml
profile: capability
```

会产生重复信息和漂移风险：

```text
kind = capability
profile = scenario   ← 两个字段可能互相冲突
```

因此 v0 的 **Strong Profile 是 Schema / Validator 概念，不一定是 Canonical Data 字段**。

未来只有出现同一 `type + kind` 需要多个正交 Profile 的真实需求时，再考虑显式 `profiles`。

---

# 4. A2 — `kind` Controlled Vocabulary

## 4.1 不把所有 kind 写死在 Core JSON Schema enum

Core Schema 只验证：

```text
kind 是合法 machine identifier
```

真正的 family ↔ kind ↔ profile 约束由独立受控 Vocabulary Registry + Validator 检查。

原因：

- `type` 改动属于核心模型变化，应该很少；
- 新增合法 `kind` 不应该每次都被伪装成 Core Schema 架构变更；
- Vocabulary 可以拥有 definition / status / aliases / profile / migration mapping；
- GitHub Actions 可以直接验证 vocabulary membership；
- 避免 `other` 成为新垃圾桶。

## 4.2 建议的 Registry 逻辑结构

后续实现可类似：

```yaml
vocabulary: object_kind
version: 0.1
terms:
  capability:
    family: concept
    profile: capability
    status: active

  scenario:
    family: concept
    profile: scenario
    status: active

  framework:
    family: concept
    status: active

  standard:
    family: artifact
    profile: normative_artifact
    status: active

  dataset:
    family: artifact
    status: active

  software:
    family: system
    profile: implementation
    status: active

  organization:
    family: agent
    profile: organization
    status: active
```

注意：这是逻辑示例，本 Design PR 不创建 Registry 文件。

## 4.3 v0 初始 kind 范围

### Concept

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

### Artifact

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

### System

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

### Agent

```text
person
organization
project_team
community
software_agent
```

这不是永远封闭的 taxonomy。新增 term 需要定义和 Review，但不需要新增 Core Family。

### 禁止通用 `other`

v0 Vocabulary **SHOULD NOT** 提供 `other`。

当现实对象无法表达时，应产生：

```text
unknown_kind / vocabulary_gap
```

作为 Curation / Governance 工作项，而不是把对象永久塞进 `other`。

---

# 5. A3 — Strong Profiles

Strong Profile = 某些 `type + kind` 组合需要额外机器合同。

## 5.1 Capability Profile

选择条件：

```yaml
type: concept
kind: capability
```

保留现有成熟结构：

```text
category
layers
domains
parent_capabilities
constraints
```

现有 `capability.schema.json` 的主体结构可以复用，不需要重新发明。

## 5.2 Scenario Profile

选择条件：

```yaml
type: concept
kind: scenario
```

保留：

```text
actors
requires
environment
success_criteria_zh/en
```

`requires[].capability` 将继续引用 Capability identity。

## 5.3 Normative Artifact Profile

适用于：

```text
standard
specification
protocol
profile
interface_specification
```

从当前 Standard Schema 复用：

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

但必须拆债：

- `maturity` 不再默认视为普通 identity property；
- `vendor_neutrality` 不再默认视为普通 factual property；
- `organization` 长期改为 role-aware Agent relation / reference；
- authority / normative status 单独表达。

## 5.4 Implementation / System Profile

适用于工程实现类 System：

```text
software
library
tool
service
platform
hardware
firmware
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

注意：

`reference_implementation` 长期更像 **role**，不推荐继续作为 System kind。

Legacy `kind: reference_implementation` 需要 Pilot 中逐对象决定其现实 System kind，再增加 `reference_implementation` role。

## 5.5 Organization Profile

选择：

```yaml
type: agent
kind: organization
```

保留：

```text
organization_kind
jurisdiction
domains
official_url
governance_notes
```

`organization_kind: open_source_project` 必须审计，因为它可能实际指：

```text
治理社区 / 团队 → Agent
软件工程项目 → System
```

不得机械迁移。

---

# 6. A4 — Legacy Compatibility Matrix

迁移期不要求现有 121 个对象立即改写。

Engine 先产生一个**Normalized Semantic View**。

| Legacy record | v0 normalized semantic view | 自动映射？ |
|---|---|---|
| `standard` | `artifact` + existing `kind` + Normative Artifact Profile | 是，少量 kind alias 后续审计 |
| `implementation` | `system` + existing `kind` + Implementation Profile | 是，`reference_implementation` 除外 |
| `organization` | `agent` + `kind: organization` + Organization Profile | 是，但 `open_source_project` 要审计 |
| `capability` | `concept` + `kind: capability` + Capability Profile | 是 |
| `scenario` | `concept` + `kind: scenario` + Scenario Profile | 是 |
| `reference_project` | unresolved identity target | **否** |
| `map` | View / Projection record | 不属于 Core Identity Object |
| `open_gap` | Finding / Assessment / workflow debt | 本阶段不强制映射 |
| `relation` | Relationship Statement | 保持并演进 |

## 6.1 `reference_project` 的特殊规则

禁止：

```text
reference_project → system
```

统一批量迁移。

每一个对象必须先做 Identity Target Audit：

```text
它是 Concept？
Artifact？
System？
还是需要拆成多个 identity？
```

Apple HIG、AGENTS.md、Design System 等边界案例已证明这个步骤必要。

## 6.2 Runtime Normalization 不修改源 YAML

建议 Engine 增加逻辑函数：

```text
normalize_identity(document)
```

返回类似：

```text
record_class
family
kind
profiles
legacy_type
migration_status
```

这些可以是 runtime dataclass / internal descriptor，**不应为了方便直接写回 Canonical YAML 隐藏字段**。

这样：

```text
Legacy source
        ↓
Normalization
        ↓
Unified semantic query
```

等 Pilot 证明新模型可用以后，再迁移源数据。

---

# 7. Engine Dual-read Design

现有 Engine 有几处直接依赖 Legacy type，必须先解除。

## 7.1 Capability reference validation

当前 `GraphIndex`：

```text
capabilities → expected_type = capability
```

迁移以后对象将变成：

```yaml
type: concept
kind: capability
```

所以 Validator / Graph 不应继续检查原始：

```text
target.type == capability
```

而应检查 normalized semantic predicate：

```text
is_capability(target) == true
```

Legacy 与 v0 都能通过同一个 predicate。

## 7.2 Implementation query

当前 bootstrap query：

```python
obj.get("type") == "implementation"
```

长期应改成：

```text
is_implementation_system(obj)
```

在 compatibility period 内：

```text
legacy implementation
OR
v0 system with Implementation Profile
```

都返回 true。

这能保证迁移 1 个、10 个或全部对象时，同一个 Query 都不需要改写。

## 7.3 Relation refs 不再把对象 `type` 当身份真相

当前 Relation：

```yaml
source:
  type: implementation
  id: forgejo_actions
```

一旦 `forgejo_actions` 迁为：

```yaml
type: system
```

旧 Relation 中的 `type: implementation` 会立刻 stale。

因此 v0 Relation Reference 应采用：

> **ID 是身份；type 只是 Legacy hint，不能成为引用正确性的必要条件。**

### 推荐 canonical v0 ref

最简单形式：

```yaml
source: forgejo_actions
target: github_actions
```

或者在未来必须挂 ref metadata 时：

```yaml
source:
  id: forgejo_actions
```

但 **不再复制对象当前 Core Family**。

Engine 当前 `ref_id()` 已经同时支持字符串和 `{id: ...}`，因此这条迁移路径天然可兼容。

### Compatibility period

旧 Relation 中的：

```yaml
type: implementation
```

可以继续读取，但 Graph 不再以它与目标 raw `type` 是否相等作为 blocking truth。

处理策略：

```text
ID 不存在
→ ERROR

Legacy type hint 与 raw source 不同
→ compatibility warning（迁移期）

v0 ID-only ref
→ PASS
```

等全量 migration 完成后再决定是否完全删除 legacy type hint。

---

# 8. A5 — Relation → Relationship Statement

Relation 不另起炉灶，直接演进为 Statement 的关系 Profile。

当前已经有：

```text
source
relation
target
capability_context
scenario_context
conditions
confidence
```

这本身已经接近：

```text
subject
predicate
object
context
assessment
```

## 8.1 v0 新 Relation 逻辑结构

```yaml
id: ...
type: relation
source: object_a
relation: compatible_with
target: object_b
context:
  capabilities: [...]
  scenarios: [...]
  versions: [...]
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

实际字段名在 Implementation PR 最终确认。

## 8.2 Legacy context aliases

现有：

```text
capability_context
scenario_context
conditions_zh/en
```

在 dual-read 时 normalization 成：

```text
context.capabilities
context.scenarios
context.conditions_zh/en
```

不要求第一批就改 107 个 Relation。

## 8.3 `confidence` 暂不进入 v0 新合同

当前裸：

```yaml
confidence: 0.95
```

语义不够明确：

- 谁的 confidence？
- 基于什么 criteria？
- 是来源自己给的，还是 IA Assessment？

因此：

- Legacy `confidence` 继续读取；
- v0 新 Relation 暂不鼓励新增裸 `confidence`；
- 后续 #10 Evidence / Trust Profile 把它设计成明确 Assessment。

---

# 9. A6 — Evidence Contract

## 9.1 Identity Source

当前 Base Object：

```yaml
sources:
  - url: ...
    title: ...
    language: ...
    accessed: ...
```

v0 继续保留这个 compact 结构，明确语义为：

> **Identity / basic object metadata source**

不把它自动当成对象全部 Claim 的证据。

## 9.2 Statement Evidence

Relation / explicit Statement 可以拥有自己的：

```yaml
evidence:
  - url: ...
    title: ...
    accessed: ...
```

初始 Evidence item 可复用 Base Source 的字段结构。

未来再扩展：

```text
source artifact ID
quoted/located fragment
retrieval method
archived copy
verification status
```

v0 不一次做完。

---

# 10. A6 — Missing / Unknown / Explicit None

## 10.1 核心规则

```text
字段不存在
= not recorded
```

绝不自动等于：

```text
unknown
none
false
```

## 10.2 Boolean false

```yaml
open_source: false
```

= 已知值 false。

与字段缺失完全不同。

## 10.3 explicit unknown / none

v0 不要求所有普通字段都变成 wrapper。

只有现实需求需要明确表达时，使用可复用 Value State 模型：

```yaml
state: known
value: ...
```

```yaml
state: unknown
```

```yaml
state: none
```

`missing` 不需要写成一个值；缺少 Statement / field 本身就表示 Atlas 没有记录。

### 禁止把普通 `null` 当万能语义

对 governed fields：

```yaml
field: null
```

SHOULD 被 Validator 警告或拒绝，除非该 Schema 明确定义 null 的语义。

---

# 11. A7 — Schema Logical Identity

继续采用现有规则：

> **Schema logical `$id` ≠ Git physical path.**

v0 新 Schema 在设计时应使用稳定 logical URI。

不因为未来：

```text
文件移动
Schema 共置方式变化
```

就改变其逻辑身份。

现有 `$ref` 解析原则继续保留。

---

# 12. A8 — Automated Review / Review Routing

这是 #61 新增的正式设计维度。

目标：

> **尽可能把确定性检查交给机器，把人的注意力留给真正需要判断的问题。**

## 12.1 三层审核

```text
PR
↓
Layer 1 — Deterministic Machine Gate
GitHub Actions / Validator
↓
Layer 2 — Semantic Review
Human / Agent Reviewer
↓
Layer 3 — Governance Authorization
Human Maintainer（仅 high-impact）
```

### Layer 1：Machine Gate

机器可以阻止：

- YAML / JSON parse error；
- JSON Schema violation；
- duplicate ID；
- invalid family / kind；
- unknown reference；
- Relation 缺 source / target / predicate；
- Graph reference issue；
- broken local docs link；
- public route build failure；
- Engine regression；
- vocabulary term 未注册；
- governed `null` misuse；
- Schema `$id/$ref` resolution failure。

这些是 deterministic failures。

### Layer 2：Semantic Review

机器不能可靠决定：

- Apple HIG 当前 ID 应该指 Concept 还是 Artifact；
- 某 Evidence 是否真的支持某 Claim；
- 是否应该新增一个新的 `kind`；
- 某条关系是不是过度概括；
- Fact 与 Assessment 是否在语义上混淆；
- 是否已经存在更成熟 Prior Art；
- 某个 identity 是否应该拆分成多个对象。

这些交给 Human / Agent Reviewer。

### Layer 3：Maintainer Authorization

以下继续要求 Human Maintainer：

- Core Identity Family 改动；
- breaking Schema changes；
- adopted Model Decision / Governance 修改；
- License / Security policy；
- main Ruleset / branch protection；
- 大规模 Canonical migration / deletion；
- stable Specification 状态升级；
- 正式 Release。

## 12.2 Machine Review Result

Validator 不应该只输出“失败”。

建议产生稳定 failure codes，例如：

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

输出两种格式：

### Human-readable Job Summary

让贡献者直接知道：

```text
哪里错
为什么错
怎么修
```

### Machine-readable report

例如逻辑上：

```json
{
  "status": "fail",
  "findings": [
    {
      "code": "IA-MR-005",
      "severity": "error",
      "path": "...",
      "object_id": "...",
      "message": "kind is not registered for family"
    }
  ]
}
```

以后 Agent / Bot 可以直接消费，而不用重新解析 CI log。

## 12.3 PASS / REVIEW / FAIL

自动审核不应只有二元状态。

逻辑结果：

```text
FAIL
确定性规则不合格，不可合并

PASS + REVIEW REQUIRED
机器规则合格，但需要语义审核

PASS + HIGH-IMPACT REVIEW REQUIRED
机器规则合格，但必须 Maintainer 授权

PASS / ELIGIBLE
所有自动 Gate 合格；是否自动 merge 由 repository policy 决定
```

## 12.4 v0 不立即自动合并 Canonical Data

在 Validator 与 Review routing 经过 Pilot 前：

- Canonical Object / Relation PR 即使 Machine PASS，也至少进入 Layer 2；
- high-impact 必须 Layer 3；
- 暂不把“CI PASS”直接等同于自动 merge。

未来可以对足够窄、低风险的维护工作开启 auto-merge，例如确定性的生成物更新或格式修复，但必须基于实际运行证据。

## 12.5 GitHub 实现方向

未来 Implementation 可使用：

```text
GitHub Actions
+ required status checks
+ Rulesets / branch protection
+ path-based risk classification
+ PR labels / Check summaries（可选）
```

重要：

> #61 Design / Pilot **不直接修改 main Ruleset**。

Ruleset 是 Open Collaboration Profile 定义的 high-impact 治理项，必须独立批准。

---

# 13. High-impact Change Detection

Actions 可以确定性识别“需要额外审核”，但不自行批准。

v0 建议以下路径至少触发 High-impact Review Required：

```text
01_State/**.schema.json
03_Evolution/03_Change/knowledge-representation-model-decision-*.md
docs/knowledge-object-classification-specification-*.md
docs/open-collaboration-profile-*.md
.github/workflows/*validator*
```

以及语义事件：

```text
Core family vocabulary 改动
已有 stable ID 修改 / 删除
大量 Canonical files 删除
kind term 删除 / 重定义
Relation predicate 删除 / 重定义
```

注意：检测到 high-impact **不是失败**，而是：

```text
Machine checks PASS
+ Maintainer Review Required
```

---

# 14. Representative Migration Pilot

Phase A 设计通过后，Phase B 只迁移一小组对象。

建议 Pilot Set：

## Artifact

- `yaml_1.2.2`：成熟 Standard；
- 1 个本轮新收录 Standard；
- Apple HIG：边界 Artifact / Concept 判断案例。

## System

- `forgejo_actions`；
- `github_actions`。

## Agent

- `agentic_ai_foundation` 或其他明确 Organization；
- 1 个 `open_source_project` legacy organization_kind 边界案例。

## Concept

- `automated_build_deployment` Capability；
- 1 个 Scenario；
- 1 个 Method / Framework Fit Test 对象（若已进入 Canonical State）。

## Relation

- `forgejo_actions_alternative_to_github_actions`；
- 1 个带 capability/scenario context 的 Relation；
- 1 个带 `confidence` legacy debt 的 Relation。

## Reference Project boundary

- `apple_human_interface_guidelines`；
- `agents_md`。

这些对象不是为了“迁移得多”，而是覆盖最危险的边界。

---

# 15. Pilot Acceptance

Pilot 必须同时证明：

```text
Stable IDs unchanged                     PASS
Public /objects/<id>.html unchanged      PASS
Objects load                             PASS
Legacy + v0 coexist                      PASS
Graph reference_issues = 0               PASS
Representative edge count explainable   PASS
Capability query still works             PASS
Implementation/System query still works  PASS
Backlinks still work                     PASS
Relation contexts preserved              PASS
Renderer still works                     PASS
Machine review report works              PASS
No semantic folder dependency            PASS
```

任何一个关键条件 FAIL：

> 不进入全量迁移，先回到 #61 设计修正。

---

# 16. Implementation Sequence

如果本 Design Draft 获批准，后续推荐拆成独立小任务：

```text
I1 Semantic Normalization Layer
   只加 dual-read / semantic predicates
        ↓
I2 Vocabulary Registry + Validator skeleton
        ↓
I3 v0 Schema drafts / Strong Profiles
        ↓
I4 Relation ref + context compatibility
        ↓
I5 Automated Machine Review report
        ↓
I6 Representative Migration Pilot
        ↓
Pilot Audit
        ↓
再决定 Canonical Migration / Enforcement
```

优先做 Normalization，而不是先改所有 Schema。

原因：

> **Engine 先学会同时理解两种语言，数据才能安全逐步换语言。**

---

# 17. Explicit Decisions Requiring Maintainer Review

本 Draft 中有 4 个真正需要负责人确认的设计选择：

### Decision A — Strong Profile 不存显式字段

推荐：

```text
Profile 由 type + kind 选择
```

而不是每个对象再写 `profile:`。

### Decision B — kind 使用独立 Vocabulary Registry

推荐 Core JSON Schema 不把全部 kind 写死 enum；Validator 检查 Registry。

### Decision C — v0 Relation reference 逐步改成 ID-only

推荐：

```yaml
source: forgejo_actions
```

而不是复制：

```yaml
source:
  type: implementation
  id: forgejo_actions
```

这样对象 family 迁移不会让 Relation 引用全部 stale。

### Decision D — GitHub Actions 是 Machine Gate，不是 Reviewer identity

Machine PASS 证明 deterministic contract 满足；Canonical semantic review / high-impact approval 继续分层。

---

# 18. Non-goals

本 Design Draft 明确不做：

- 不修改现有 Object / Relation Schema；
- 不迁移任何 Canonical object；
- 不启用全量 Schema validation；
- 不修改 Ruleset / branch protection；
- 不发明 IA Query Language；
- 不选择数据库；
- 不创建 `concept/artifact/system/agent` 文件夹；
- 不把全部字段 Statement 化；
- 不解决 #10 全部 Trust / Assessment vocabulary；
- 不合并 PR #26 / #30 等无关任务。

---

# 19. Current Recommendation

Phase A 当前推荐方案：

```text
Canonical source
Legacy + future v0 YAML
        ↓
Semantic Normalization Layer
        ↓
Unified Identity / Profile predicates
        ↓
Graph / Query / Renderer

同时：

Schema + Vocabulary Registry + Validator
        ↓
GitHub Actions Machine Gate
        ↓
Semantic Review
        ↓
Maintainer authorization when high-impact
```

这条路线的核心优势是：

> **不要求先重写整个 Atlas，先把机器的理解方式升级，然后用少量真实对象证明新旧模型能安全共存。**
