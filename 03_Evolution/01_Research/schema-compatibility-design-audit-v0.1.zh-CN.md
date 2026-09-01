# Schema / Compatibility Design Audit v0.1

> 状态：Research / Design Audit
>
> 审计对象：#61 / PR #63
>
> 目的：在批准 Phase A 设计前，反向检查当前 Schema、Engine、Relation 数据和 GitHub Actions，确认设计不会重新制造新的模型耦合。

## 1. 总结

PR #63 的主路线 **PASS with revisions**。

推荐继续保留：

- Semantic Normalization / dual-read 先于数据迁移；
- Strong Profile 不在 Canonical Data 冗余写 `profile:`；
- `kind` 使用受控 Vocabulary Registry；
- Relation 引用迁向 ID-only；
- Relation 演进为 relationship Statement；
- GitHub Actions 作为 deterministic machine gate；
- Human / Agent Semantic Review 与 Human Maintainer Authorization 分层。

需要在实现前补清楚 4 个边界。

---

# 2. Audit A — Strong Profile：PASS

当前 Capability / Scenario 已经有明显专用字段，因此 Strong Profile 是真实机器需求。

但不需要每条数据重复：

```yaml
kind: capability
profile: capability
```

推荐继续：

```yaml
type: concept
kind: capability
```

Validator 根据 Vocabulary Registry 选择 Capability Profile。

## 小修正

Registry 内部 SHOULD 支持：

```yaml
profiles:
  - capability
```

而不是假设永远只有一个 `profile`。

这只是 Registry metadata；**Canonical Object 本身仍不写 `profiles:`**。

理由：未来某个 kind 可能同时应用基础 Profile + 一个正交附加 Profile，但不应该因此重新设计对象格式。

---

# 3. Audit B — Kind Vocabulary Registry：PASS with gate condition

把全部 kind 写死到 Core Schema enum 会让任何术语扩展都变成 Core Schema 修改，不符合稳定 Core / 可扩展 Profile 的目标。

因此独立 Registry 方向正确。

但有一个必要条件：

> **在真正接受 v0 Canonical Data 之前，Vocabulary Validator 必须已经进入 Machine Gate。**

否则 Core Schema 只检查 identifier pattern，会暂时允许任意新 kind。

## 推荐物理实现

Registry SHOULD 使用 JSON 等不会被当前 YAML Loader 当成 Canonical Object 的格式。

例如逻辑候选：

```text
01_State/01_Objects/object-kind.vocabulary.json
```

这只是机器合同资源的共置建议，不是语义分类目录。

是否最终采用该文件名 / 路径属于 Implementation 细节。

---

# 4. Audit C — Legacy `standard` 不能完全自动映射

PR #63 原 Compatibility Matrix 写：

```text
standard → artifact + existing kind
```

大方向正确，但当前 `standard.schema.json` 的 legacy `kind` 包含：

```text
standard
protocol
specification
api
format
profile
interface
device_class
```

其中：

```text
standard / protocol / specification / format / profile
```

通常很自然指向 Artifact。

但：

```text
api
interface
device_class
```

可能指：

- 一份发布的规范 Artifact；
- 一个抽象接口 / API Concept；
- 一个 Device Class Concept。

因此 Legacy Standard normalization 应改为：

```text
kind ∈ clearly-artifact set
→ automatic artifact mapping

kind ∈ api / interface / device_class
→ Identity Target audit required
```

不能为了方便再次用历史 Schema 名称决定 reality identity。

---

# 5. Audit D — Document Class 与 Core Identity Family 必须区分

批准模型只有 4 个 Core Identity Families：

```text
concept
artifact
system
agent
```

但仓库里仍存在：

```text
type: relation
type: map
type: open_gap
```

这些不能被误读成第 5 / 6 / 7 个 Core Family。

## 推荐 Runtime Descriptor

Normalization Layer SHOULD 明确产生：

```text
record_class
```

例如：

```text
identity
statement
view
finding
```

再在 `record_class = identity` 时拥有：

```text
family = concept | artifact | system | agent
kind = ...
```

逻辑示例：

```text
Capability
record_class: identity
family: concept
kind: capability

Relation
record_class: statement
statement_profile: relation

Map
record_class: view

Open Gap
record_class: finding   # 暂定，后续 Trust/Curation 再 Profile
```

### 关键边界

`record_class` 先作为 Runtime normalized descriptor，**v0 不要求在全部 Canonical YAML 中新增一个 `record_class:` 字段**。

这可以保持源数据最小化，同时让 Engine 不再混淆“文档种类”和“对象现实身份”。

---

# 6. Audit E — Relation ID-only：PASS

当前 Relation 把引用写成：

```yaml
source:
  type: implementation
  id: forgejo_actions
```

GraphIndex 还会要求这里的 type 与目标 raw type 相同。

这与 stable identity 原则直接冲突：一旦对象从 `implementation` 迁为 `system`，关系本身其实没有变，但引用会 stale。

所以推荐：

```yaml
source: forgejo_actions
target: github_actions
```

ID-only 是更稳定的 canonical v0 ref。

## 额外限制

当前 GraphIndex 只把 Identity Objects 放进 `objects` index；Relation 本身不在同一个 resolver 中。

因此 Phase B Pilot 暂时 SHOULD 限制：

> Relation source / target 指向 Identity Object IDs。

不要在这次顺便扩张到 Statement → Statement、Finding → Statement 等任意 record reference。

如果未来真实需求出现，再设计 generic reference resolver。

---

# 7. Audit F — Engine dual-read：PASS and required first

当前 Engine 存在明确 Legacy coupling：

```text
GraphIndex:
capabilities field expects raw type == capability

bootstrap_query:
implementation query expects raw type == implementation
```

因此 PR #63 的实施顺序是正确的：

```text
先 Semantic Normalization / predicates
再迁移数据
```

否则迁移第一条 Capability / Implementation 就会改变 Query / Reference behavior。

## 推荐 semantic predicates

初期最少需要：

```text
is_identity(record)
is_capability(record)
is_scenario(record)
is_implementation_system(record)
is_organization_agent(record)
semantic_family(record)
semantic_kind(record)
```

这些 predicate 消费 Normalized Descriptor，不要求每个调用者自己理解 legacy mapping。

---

# 8. Audit G — JSON Schema enforcement 当前确实不存在

当前 Runtime dependencies 只有：

```text
PyYAML
Markdown
```

当前 GitHub Action 运行：

- repository layout test；
- graph health；
- deterministic query；
- site / renderer build；
- Markdown links。

没有 JSON Schema Validator dependency，也没有 Schema validation job。

因此：

> **“Schema 已经存在” ≠ “Schema 已经是 Machine Gate”。**

#61 Implementation 必须显式增加 Validator dependency / command / CI step，不能把 Schema enforcement 当成已经存在的能力。

具体使用 Python `jsonschema`、check-jsonschema 或其他实现，可在 I2 Implementation Task 中决定。

---

# 9. Audit H — Automated Review：PASS

三层模型与现有 Open Collaboration Profile 相容：

```text
Machine Gate
≠ Reviewer identity
≠ Maintainer authorization
```

## v0 推荐合并策略

Canonical Data：

```text
Machine PASS
→ 仍进入 Semantic Review
```

High-impact：

```text
Machine PASS
→ Semantic Review
→ Human Maintainer Authorization
```

v0 暂时不要让 Canonical Data 因 CI PASS 就直接 auto-merge。

未来只有在长期运行证明某类变更完全 deterministic 后，再给那一小类工作开放 auto-merge。

---

# 10. Audit I — High-impact Detection：PASS with separation

Actions 可以自动判断：

```text
这个 PR 是否需要高影响审核
```

但不能自动判断：

```text
这个高影响改动是否应该被批准
```

所以 risk classifier 的输出应类似：

```text
HIGH_IMPACT_REVIEW_REQUIRED
```

而不是：

```text
FAIL because high impact
```

除非缺少 required human authorization 时由 Ruleset 阻止 merge。

Ruleset 配置本身仍是独立 high-impact 治理变更，不在 #61 Design / Pilot 自动修改。

---

# 11. Revised Legacy Mapping

| Legacy type | Normalized result | Audit requirement |
|---|---|---|
| `capability` | identity / concept / capability | automatic |
| `scenario` | identity / concept / scenario | automatic |
| `implementation` | identity / system / legacy kind | automatic except `reference_implementation` |
| `organization` | identity / agent / organization | `open_source_project` needs audit |
| `standard` | identity / artifact for clearly-artifact kinds | `api/interface/device_class` need audit |
| `reference_project` | unresolved | every object needs Identity Target Audit |
| `relation` | statement / relation | automatic record-class mapping |
| `map` | view | automatic record-class mapping |
| `open_gap` | finding (provisional) | no forced semantic migration in #61 |

---

# 12. Revised Implementation Gate

在第一条 v0 Canonical Object 被允许 merge 前，至少必须有：

```text
Semantic Normalization             ✅
Kind Registry                       ✅
Kind/family Validator               ✅
Legacy + v0 Graph resolution        ✅
Machine Review CI check             ✅
Representative regression tests     ✅
```

否则继续只把 v0 Schema 当 Draft，不接收混合数据。

---

# 13. Audit Outcome

结论：

> **PR #63 主设计可以继续，建议吸收以上修订后进入 Maintainer Design Approval。**

不需要更多大规模 Prior Art，也不需要再开新的真实对象 Fit Test。

真正下一步是把 Design Draft 修订为：

```text
Document Class
+ Core Identity Family
+ Kind Registry / Strong Profiles
+ Semantic Normalization
+ ID-only Relation refs
+ Machine Review Gate
```

然后再决定是否批准进入 I1 Semantic Normalization Layer 实现。
