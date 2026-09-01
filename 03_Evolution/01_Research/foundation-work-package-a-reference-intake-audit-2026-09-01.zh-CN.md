# Foundation Work Package A — Reference Intake Audit — 2026-09-01

> 状态：Point-in-time Intake Audit（阶段性收录审计）
>
> 目的：检查 Repository Structure Profile v0.1 与 Open Collaboration Profile v0.1 实际使用过的 Existing Standards & Prior Art 是否已经进入 InteropAtlas Canonical Atlas；能正确建模的立即纳入，不能正确建模的明确进入模型待办，而不是继续只留在研究文档中。

## 1. 审计结论

审计开始时，Work Package A 的多数依据**只存在于 Research / Specification 文档中，没有成为 Canonical Atlas Object**。

本轮已把当前模型能够较准确表达的核心依据纳入对象层，并建立显式 Graph relations。

当前结果：

- 正式标准 / Specification：已补入；
- 成熟机器可读知识项目 / Landscape /平台协作先例：已补入或以明确 provisional modeling 状态补入；
- 相关治理组织：已补入；
- 纯 Method / Framework（例如 Diátaxis、Docs as Code）：**暂不强塞现有 `reference_project`**，留给 #15 Non-normative Knowledge Object Model 的真实 Fit Test。

核心规则：

> **Use it → check Atlas → reuse / ingest / create modeling intake.**
>
> 任何被 IA 自身实际用于重要设计决策的外部标准或成熟先例，都不应该长期只存在于自然语言参考列表中。

---

## 2. 审计前已经存在

### BCP 14 / RFC 2119 + RFC 8174

Canonical Object：`bcp14_rfc2119_rfc8174`

路径：`standards/bcp14-rfc2119-rfc8174.yaml`

用途：IA 自产 Specification 中 MUST / SHOULD / MAY 等规范性关键词。

状态：**已有，无需重复创建。**

### ISO、W3C 等组织

`iso`、`w3c` 等基础组织对象已经存在。

本轮因 ISO/IEC 联合标准真实需求新增 `iec`。

---

## 3. 本轮新增：Normative Artifacts

### REUSE Specification 3.3

ID：`reuse_specification_3.3`

路径：`standards/reuse-specification-3.3.yaml`

身份：Specification；不是一般“最佳实践文章”。

A 中用途：
- Repository licensing layout；
- root `LICENSES/`；
- machine-readable licensing information。

官方来源：
- https://reuse.software/spec/
- https://reuse.software/specifications/

### ISO/IEC 5339:2024

ID：`iso_iec_5339_2024`

路径：`standards/iso-iec-5339-2024.yaml`

身份：已发布 International Standard。

A 中用途：AI application lifecycle、stakeholder communication、Human–AI governance 的上位依据之一。

官方来源：
- https://www.iso.org/standard/81120.html

### ISO/IEC CD 25589

ID：`iso_iec_25589_cd`

路径：`standards/iso-iec-25589-cd.yaml`

身份：**Committee Draft / under development**。

A 中用途：Human–Machine Teaming 的概念、术语、技术特征与设计原则参考。

重要：Atlas 明确保留其 Draft 状态，**没有把它误标成已发布 International Standard**。

官方来源：
- https://www.iso.org/standard/90831.html

---

## 4. 本轮新增：Mature Precedents / Reference Projects

### W3C browser-specs

ID：`w3c_browser_specs`

路径：`reference-projects/w3c-browser-specs.yaml`

用途：机器可读 specification catalog；Data + provenance + version series + tests；支持 IA 的 Layered Monorepo 结构判断。

### MDN Browser Compat Data

ID：`mdn_browser_compat_data`

路径：`reference-projects/mdn-browser-compat-data.yaml`

用途：高频更新的 Canonical Data + Schema + 多消费者发布模式。

### CNCF Landscape

ID：`cncf_landscape`

路径：`reference-projects/cncf-landscape.yaml`

用途：Landscape data 与 generator 可在合同稳定后拆分，支持“当前单仓、未来可抽离”的判断。

### SPDX License List

ID：`spdx_license_list`

路径：`reference-projects/spdx-license-list.yaml`

用途：Authoritative Source 与 Generated JSON / RDF / HTML / Text 等投影分离。

### OpenSSF Best Practices Badge

ID：`openssf_best_practices_badge`

路径：`reference-projects/openssf-best-practices-badge.yaml`

用途：把开放项目最佳实践转化为公开、分级、可检查的符合性标准。

### OpenSSF Scorecard

ID：`openssf_scorecard`

路径：`reference-projects/openssf-scorecard.yaml`

用途：把部分 repository security / project health 要求转成自动化、持续性检查；自动结果作为 Review Evidence，而不是 Reviewer。

### GitHub Community Health

ID：`github_community_health`

路径：`reference-projects/github-community-health.yaml`

用途：README / CONTRIBUTING / CODE_OF_CONDUCT / SECURITY / SUPPORT / Issue & PR templates 等平台级约定与发现机制。

建模状态：`provisional_reference_project_until_non_normative_object_model`。

原因：它更接近平台约定 / governance practice，不是传统“project”；当前以临时 Reference Project 进入事实图，待 #15 模型成熟后迁移身份。

### GitHub Collaboration Primitives

ID：`github_collaboration_primitives`

路径：`reference-projects/github-collaboration-primitives.yaml`

覆盖：Issue、Assignee、Sub-issues、Dependencies、PR、Review、CODEOWNERS、Rulesets。

用途：Open Collaboration Profile 的 GitHub-native implementation primitives。

建模状态：provisional。

### AGENTS.md

ID：`agents_md`

路径：`reference-projects/agents-md.yaml`

用途：跨 Coding Agent 的 repository-specific instruction entry point；支持 nested instruction scope。

建模状态：provisional。

另建立：
- Organization `agentic_ai_foundation`；
- Relation `agents_md governed_by agentic_ai_foundation`。

### NIST AI RMF 1.0

ID：`nist_ai_rmf_1.0`

路径：`reference-projects/nist-ai-rmf-1.0.yaml`

用途：Human–AI role differentiation、responsibilities、oversight 与 risk governance。

建模状态：provisional。

重要：保持其 NIST Framework / guidance 身份，不误标为 ISO/IEC International Standard。

---

## 5. 本轮新增：Supporting Objects

### Capabilities

- `human_machine_teaming`
- `ai_application_lifecycle_governance`

### Organizations

- `iec`
- `nist`
- `agentic_ai_foundation`

这些对象让新增标准 / 先例不只是孤立记录，而能进入 Capability / Governance Graph。

---

## 6. Graph relations

新增：

`relations/foundation-work-package-a-prior-art.yaml`

显式表达 InteropAtlas 对以下依据的使用 / inspired_by：
- REUSE 3.3；
- W3C browser-specs；
- MDN BCD；
- CNCF Landscape；
- SPDX License List；
- OpenSSF Best Practices Badge；
- OpenSSF Scorecard；
- GitHub Community Health；
- GitHub Collaboration Primitives；
- AGENTS.md；
- NIST AI RMF 1.0；
- ISO/IEC 5339:2024；
- ISO/IEC CD 25589。

同时表达：
- ISO/IEC CD 25589 `uses` ISO/IEC 5339；
- ISO/IEC 5339 / 25589 分别 `governed_by` ISO 与 IEC。

另有：

`relations/agents-md-governance.yaml`

表达 AGENTS.md 与 AAIF 的治理关系。

---

## 7. Validation

第一轮入库后 CI 实际发现一个 YAML 语法问题：

```text
official_name: @mdn/browser-compat-data
```

YAML 解析器不能接受未加引号的 `@` 开头 plain scalar。

修正为：

```text
official_name: "@mdn/browser-compat-data"
```

之后 Bootstrap Engine Experiment 成功。

阶段性 Graph health：

```text
108 objects
101 explicit relations
148 resolved edges
reference_issues: []
```

这说明本轮新增对象与关系均可被当前 Loader / GraphIndex 解析，并没有产生悬空引用。

已知 #7 `alternative_to` Query scope bug 仍然存在，与本次 intake 无关。

---

## 8. 明确暂缓：纯 Method / Framework

### Diátaxis

A 中用途：文档按 Tutorial / How-to / Reference / Explanation 的用户任务区分。

当前判断：Method / Framework。

**不进入现有 `reference_project`**。

原因：Knowledge Object Classification Specification 已明确 Method 与 Mature Precedent 应区分；当前 Schema 没有合适 Method object family。

进入 #15 Fit Test / intake queue。

### Docs as Code

A 中用途：documentation 使用 version control、review、issue tracking、automated tests 等软件工程工作流。

当前判断：Method / Practice。

**同样暂缓进入旧 `reference_project`**，等待 #15。

这不是遗漏，而是有意避免坏建模。

---

## 9. Reference Seeding：把 Atlas 反哺任务发布

本轮同时形成：

`docs/work-item-reference-seeding-v0.1.zh-CN.md`

新协作原则：Ready Work Item SHOULD 分三层提供参考依据。

### Must Read

必须理解的上位 Definition / Specification / Schema / Issue。

### Seed References

Task Author 已知的高价值 Atlas 对象，优先使用 stable object ID：

```text
standard: reuse_specification_3.3
reference_project: w3c_browser_specs
reference_project: github_collaboration_primitives
```

### Freshness Check Required

Executor 仍应检查：
- 新版本；
- 新标准；
- 新替代方案；
- 新成熟先例；
- 既有依据状态变化。

因此 Seed References 是**共享起点**，不是阻止新搜索的白名单。

---

## 10. Intake Invariant（后续建设规则）

以后对重要 Foundation / Specification 工作，Task Author 与 Reviewer SHOULD 检查：

```text
本任务实际使用了哪些外部依据？
             ↓
Atlas 已有？ ── Yes → 直接引用 stable ID
     │
     No
     ↓
现有模型能准确表达？
   │          │
 Yes         No
   ↓          ↓
立即入库    创建 modeling / intake 任务
              ↓
          不强塞错误类型
```

这使项目自身建设持续推动 Atlas 扩充：

```text
IA 实践
  ↓
发现标准 / 先例 / 方法
  ↓
Atlas intake
  ↓
未来任务 Reference Seeding
  ↓
减少重复研究
  ↓
Freshness Check 发现新知识
  ↓
再次反哺 Atlas
```

这是 Practice-driven Feedback 与 Open Collaboration / Curation Route 的一个直接闭环。
