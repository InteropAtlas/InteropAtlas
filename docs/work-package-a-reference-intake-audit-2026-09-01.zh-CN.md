# Work Package A Reference Intake Audit — 2026-09-01

> 状态：Point-in-time Audit / Intake Record
>
> 目的：检查 Foundation Work Package A 中实际用于 Repository Structure Profile 与 Open Collaboration Profile 的 Existing Standards & Prior Art，确认它们是否已经进入 InteropAtlas Canonical Atlas；可准确建模的立即纳入，当前模型无法准确表达的进入 #15 Non-normative Knowledge Object Model 的 intake queue。

## 1. 原则

本次审计遵守：

> **Used as a design basis → SHOULD become discoverable in the Atlas, when it is inside the interoperability problem boundary.**

但同时遵守：

> **Correct identity before convenient ingestion.**
>
> 宁可暂时进入 Intake Queue，也不把 Method / Guideline / Platform Convention 错标成 Standard 或 Reference Project。

因此“没有立即生成 YAML”不等于“没有收录意识”，而是明确区分：

1. **Canonicalized now** — 当前 Schema 能准确表达；
2. **Already present** — A 使用前已在 Atlas 中；
3. **Queued for #15** — 值得收录，但当前对象模型语义不准确；
4. **Platform mechanism / implementation modeling pending** — 需要与 Implementation / Method / Governance 对象模型一起决定。

---

# 2. 已存在于 Atlas

## BCP 14 / RFC 2119 + RFC 8174

状态：**Already present**

Canonical ID：`bcp14_rfc2119_rfc8174`

路径：`standards/bcp14-rfc2119-rfc8174.yaml`

用途：Repository / Collaboration / Knowledge Object 等 IA 自产规范中的 MUST / SHOULD / MAY 语义。

---

# 3. 本次立即 Canonicalized

## 3.1 REUSE Specification 3.3

状态：**Canonicalized now**

Canonical ID：`reuse_specification_3.3`

对象身份：Normative Artifact / Specification

路径：`standards/reuse-specification-3.3.yaml`

A 中用途：
- Repository licensing layout；
- root `LICENSES/`；
- machine-readable copyright / licensing information。

官方来源：https://reuse.software/spec/

注意：REUSE 3.3 本身明确采用 RFC 2119 Requirement Keywords。

## 3.2 ISO/IEC 5339:2024

状态：**Canonicalized now**

Canonical ID：`iso_iec_5339_2024`

对象身份：Published International Standard

路径：`standards/iso-iec-5339-2024.yaml`

Capability：`ai_application_lifecycle_governance`

A 中用途：AI application lifecycle、stakeholder engagement、governance 的上位参考。

官方来源：https://www.iso.org/standard/81120.html

## 3.3 ISO/IEC CD 25589

状态：**Canonicalized now**

Canonical ID：`iso_iec_25589_cd`

对象身份：Committee Draft / Normative Artifact under development

路径：`standards/iso-iec-25589-cd.yaml`

Capability：`human_machine_teaming`

A 中用途：Human-Machine Teaming 的概念、术语、技术特征和设计原则。

官方来源：https://www.iso.org/standard/90831.html

重要：该对象必须保持 `committee_draft / under development` 身份，不能描述为已经发布的 International Standard。

## 3.4 W3C browser-specs

状态：**Canonicalized now**

Canonical ID：`w3c_browser_specs`

当前对象身份：Mature Precedent / Standards Catalog Project

路径：`reference-projects/w3c-browser-specs.yaml`

A 中用途：Data + Schema + Tooling + Tests 在同一机器可读知识仓库共同演化的成熟先例。

## 3.5 MDN Browser Compat Data

状态：**Canonicalized now**

Canonical ID：`mdn_browser_compat_data`

当前对象身份：Mature Precedent / Machine-readable Knowledge Project

路径：`reference-projects/mdn-browser-compat-data.yaml`

A 中用途：Schema-governed facts、one source / many consumers、机器可读知识发布。

## 3.6 CNCF Landscape

状态：**Canonicalized now**

Canonical ID：`cncf_landscape`

当前对象身份：Mature Precedent / Landscape Project

路径：`reference-projects/cncf-landscape.yaml`

A 中用途：data repository 与 generator 在合同稳定后分离的成熟先例。

## 3.7 SPDX License List

状态：**Canonicalized now**

Canonical ID：`spdx_license_list`

当前对象身份：Mature Precedent / Standards Catalog Data Project

路径：`reference-projects/spdx-license-list.yaml`

A 中用途：Authoritative Source 与 Generated Multi-format Outputs 分离。

## 3.8 OpenSSF Best Practices Badge

状态：**Canonicalized now**

Canonical ID：`openssf_best_practices_badge`

当前对象身份：Mature Precedent / Conformance-oriented Open Project Practice

路径：`reference-projects/openssf-best-practices-badge.yaml`

A 中用途：把开放项目最佳实践转化成可检查、可分级、可公开验证的项目健康 / conformance criteria。

---

# 4. 本次新增 supporting capabilities

## `human_machine_teaming`

用于表达 Human + Machine Intelligence 的协作、角色、共享上下文、任务完成与监督能力。

## `ai_application_lifecycle_governance`

用于表达 AI application lifecycle、stakeholder engagement、责任和持续治理能力。

`license_expression` 已在仓库中存在，因此 REUSE 直接复用现有 capability，没有创建重复对象。

---

# 5. 应收录但当前不应强塞进 `reference_project`

以下对象在 A 中具有真实设计依据价值，但当前 `reference_project` 语义不准确。

它们进入 #15 intake queue。

## 5.1 NIST AI Risk Management Framework 1.0 + Playbook

建议身份：Framework / Guideline / Governance Method

为什么不直接建 `reference_project`：
- 它首先是一套 Framework / Guidance，而不是“参考项目”；
- `reference_project.project_kind=interoperability_framework` 虽技术上能塞进去，但会让“project”和“framework artifact”混淆。

当前权威状态：
- AI RMF 1.0 发布于 2023-01-26；
- NIST 当前明确说明 AI RMF 1.0 正在修订；
- 因此未来 Canonical Object 需要同时表达 `published v1.0` 与 `revision in progress`。

官方来源：
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- https://www.nist.gov/itl/ai-risk-management-framework
- https://airc.nist.gov/airmf-resources/

## 5.2 AGENTS.md

建议身份：Repository Agent Instruction Convention / Specification-like Practice

为什么不直接建 Standard：
- Linux Foundation / AAIF 将其描述为 simple universal standard / convention，并已成为 AAIF founding project；
- 但当前 Atlas 应先研究其正式治理、规范文档和 conformance status，再决定 Normative Artifact 还是 Mature Practice；
- 不应因为新闻稿使用 `standard` 一词就自动映射到 IA `standard` object family。

当前成熟证据：Linux Foundation 2025-12-09 公告称 AGENTS.md 已被超过 60,000 个开源项目采用，并由 AAIF 提供开放治理。

来源：https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

## 5.3 Agentic AI Foundation（AAIF）

建议身份：Organization / Foundation + Governance Precedent

需要进一步判断：
- 是否创建 Organization `aaif`；
- AGENTS.md 与 AAIF 的 governed_by 关系怎样表达；
- Linux Foundation 与 AAIF 的组织层级关系。

当前 Organization schema 可以表达 foundation，但应在实际 AGENTS.md 模型一起进入，避免只有组织没有对应知识对象。

## 5.4 GitHub Community Health Files

建议身份：Platform Convention / Contribution Governance Practice

包括：README、CONTRIBUTING、CODE_OF_CONDUCT、SECURITY、SUPPORT、Issue / PR templates 等 GitHub 原生识别机制。

为什么不直接建 `reference_project`：这不是一个 project，而是一组平台约定 / mechanisms。

需要 #15 判断应该使用：
- Practice；
- Guideline / Convention；
- Platform Mechanism；
- 或少量顶层类型 + facets / relations。

## 5.5 GitHub Issues / Assignees / Sub-issues / Dependencies / Issue Fields / Projects

建议身份：Platform Collaboration Mechanisms / Implementations

A 中用途：Task identity、Task Graph、Lifecycle metadata、Lease-style Claim 的 GitHub-native implementation basis。

当前 `implementation` schema 可能部分适用，但需要先决定“GitHub platform”与“GitHub Issues capability / mechanism”是否拆对象，避免把每个 UI feature 都建成一个独立 implementation。

## 5.6 GitHub PR / Reviews / CODEOWNERS / Rulesets

建议身份：Platform Collaboration / Governance Mechanisms

A 中用途：Artifact delivery、independent review、ownership routing、merge authorization。

同样进入 implementation / practice modeling review，而不是直接建立一堆 feature objects。

## 5.7 Diátaxis

建议身份：Documentation Method / Framework

A 中用途：说明真正用户文档可按 Tutorial / How-to / Reference / Explanation 组织，但不能用 Diátaxis 替代 Specification / Research / Governance 等 Artifact identity。

当前不适合 `reference_project`。

## 5.8 Docs as Code

建议身份：Documentation Method / Practice

A 中用途：Documentation 与 code 一样接受 version control、review、issue tracking、automated testing。

当前不适合 `reference_project`。

---

# 6. 一个额外模型缺口：joint publisher / governance

ISO/IEC 5339 和 ISO/IEC 25589 暴露当前 `standard.schema.json` 的已知限制：

```text
organization: string
```

只能引用一个 Organization。

但 ISO/IEC 标准具有 joint ISO/IEC publication / governance 语义。

因此本次对象没有强行把 `organization: iso` 当成完整事实，也没有把 ISO 与 IEC 合并成虚构组织。

后续应研究：
- `organizations: []`；
- publisher / developer / adopter role relations；
- `governed_by` / `published_by` / `developed_by` 等关系是否分离。

这属于真实数据驱动的模型反馈。

---

# 7. Work Package A Reference Coverage

按“实际引用的上游依据族”计算：

### 已有 / 本次已结构化
- BCP 14；
- REUSE 3.3；
- ISO/IEC 5339:2024；
- ISO/IEC CD 25589；
- W3C browser-specs；
- MDN BCD；
- CNCF Landscape；
- SPDX License List；
- OpenSSF Best Practices Badge。

### 已确认应收录、等待正确模型
- NIST AI RMF / Playbook；
- AGENTS.md；
- AAIF；
- GitHub Community Health；
- GitHub Issues / Projects collaboration mechanisms；
- GitHub PR / Review / CODEOWNERS / Rulesets；
- Diátaxis；
- Docs as Code。

所以本次审计不以“所有 A 参考都强行变成 YAML”作为成功标准，而以：

> **每一项都有 Canonical Object 或明确 Intake / Model Gap 去向。**

为成功标准。

---

# 8. 新协作原则：Reference Seeding

本次讨论形成一个新的协作原则：

> **发布任务时，如果 Atlas 已收录明显相关的标准 / 成熟先例 / 方法，Task Author SHOULD 把它们作为 Seed References 提供给协作者。**

目的：
- 避免每个 Human / Agent 从零重复发现相同基础材料；
- 复用 Atlas 自己的知识资产；
- 缩短任务启动时间；
- 让任务依据更可追踪。

但 Seed References **MUST NOT** 被视为完整答案或封闭参考集合。

执行者仍 SHOULD 做 Freshness / Completeness Check：
- 是否出现新版本；
- 是否有新的标准；
- 是否有更成熟先例；
- 当前 Seed 是否已 superseded / deprecated；
- 是否存在任务作者遗漏的重要替代方案。

因此未来任务推荐区分：

```text
Read First / Upstream Contracts
- 必须遵守的 IA 定义与规范

Seed References
- Atlas 中已经知道的相关 Standard / Method / Precedent / Implementation

Freshness Check
- 是否需要检查新增 / 更新 / superseded references
```

这使 InteropAtlas 开始真正“用自己的地图建设自己”。
