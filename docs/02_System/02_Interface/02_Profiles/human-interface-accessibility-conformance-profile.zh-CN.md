# InteropAtlas Accessibility / Conformance Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft / Gate B Module**
Document Created At: 2026-09-02T07:39:56+08:00
Document Updated At: 2026-09-05T03:51:00+08:00
Metadata Backfilled At: 2026-09-02T11:06:28+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> 状态：**Draft / Gate B Module**
>
> Package: [`human-interface-profiles.zh-CN.md`](human-interface-profiles.zh-CN.md)

## 1. 目标

本 Profile 是 Human Interface Package 的横向验收层：

> **不同用户是否能够完成核心任务，以及项目怎样用可重复的证据证明实现符合 Requirements。**

Accessibility 不是 Visual Profile 的附录，Conformance 也不等于“CI 绿了”。

---

## 2. 上游依据

### Normative / high-authority

- WCAG 2.2 / ISO/IEC 40500:2025；
- ISO 9241-20:2021；
- ISO 9241-171:2025；
- ISO 9241-11:2018 — usability in context；
- ISO 9241-110:2020；
- HTML Living Standard；
- WAI-ARIA 1.2；
- ACT Rules Format 1.1。

### Implementation / testing references

- WAI-ARIA APG；
- Playwright 等成熟 Browser E2E implementation；
- W3C WebDriver 作为浏览器自动化上游协议参考；
- USWDS / GOV.UK 的 component accessibility guidance。

使用成熟 accessible component 不自动证明整个 IA View 或用户任务符合 WCAG。

---

## 3. Accessibility Requirements

### `IA-HI-A11Y-001` — WCAG Target

Human-readable Web SHOULD 以 WCAG 2.2 Level AA 作为最低目标；例外 SHOULD 被显式记录。

- 采用方式：**Adopt + Profile**
- Conformance：`Accessibility + Review`

### `IA-HI-A11Y-002` — Semantic Structure

页面 MUST 使用合理的 heading、landmark、link、button 等语义结构。

- 上游：HTML / WCAG / WAI-ARIA
- 采用方式：**Adopt**
- Conformance：`Static + Accessibility`

### `IA-HI-A11Y-003` — Keyboard Accessibility

所有核心任务 MUST 可通过键盘完成。

- 上游：WCAG 2.2
- Conformance：`Browser + Accessibility`

### `IA-HI-A11Y-004` — Contrast and Non-text Contrast

文本、关键状态与必要非文本 UI MUST 满足适用的 WCAG 对比度要求。

- Conformance：`Automated + Browser + Manual`

### `IA-HI-A11Y-005` — Target Size and Input Diversity

交互目标 SHOULD 满足 WCAG 2.2 适用 Target Size 要求，并不得只假设精确鼠标输入。

- Conformance：`Browser + Accessibility`

### `IA-HI-A11Y-006` — Component Accessibility Is Not Site Conformance

采用 APG / USWDS / GOV.UK 等成熟组件 MUST NOT 被当作整站 Conformance 的替代证据。

- 采用方式：**Profile**
- Conformance：`Review + Human`

---

## 4. Conformance Requirements

### `IA-HI-CONF-001` — Requirement Traceability

重要页面 / 组件 / View SHOULD 能追溯到 IA Requirement ID 或直接上游要求。

- Conformance：`Static + Review`

### `IA-HI-CONF-002` — Static Build Is Insufficient

代码运行、HTML 生成和部署成功 MUST NOT 单独等价于交互验收。

- Conformance：`CI policy + Review`

### `IA-HI-CONF-003` — Browser E2E

核心真实交互 SHOULD 用真实浏览器 E2E 验证；优先复用成熟工具。

- Conformance：`Browser`

### `IA-HI-CONF-004` — Accessibility Testing

Accessibility SHOULD 组合：
- automated checks；
- keyboard / focus checks；
- 必要人工检查；
- 后续逐步映射 ACT Rules。

- Conformance：`Automated + Browser + Manual`

### `IA-HI-CONF-005` — Multi-page Consistency Test

共享组件跨不同对象 / View 时 SHOULD 验证行为一致性。

- Conformance：`Browser + Static`

### `IA-HI-CONF-006` — Progressive Enhancement Test

核心 Resource reading / navigation SHOULD 验证 JavaScript 禁用后仍然成立。

- Conformance：`Browser`

### `IA-HI-CONF-007` — Human Evaluation

自动化不能替代真实用户任务评价；重大 IA / Interaction 变化 SHOULD 有真实任务 evidence。

Gate B minimum 使用统一任务记录结构：

```text
Task
Starting point
Expected destination / outcome
Observed path
Friction / ambiguity
Requirement affected
Result: Conform / Partial / Non-conform / Unknown
```

代表任务至少覆盖 Identify、Find、Relate / Return、Verify、Compare，以及当前真实可触达的 Explore / Recenter path。Browser-observable 行为 SHOULD 由真实 Browser E2E 补强；没有 UI 的 Gate B minimum contract（例如当前 Minimal Compare）可以使用 deterministic semantic walkthrough，但必须明确它不是已实现的完整 UI。

- Conformance：`Human + Browser + Evidence Artifact`
- Gate B evidence：[`../03_Evolution/02_Experiments/gate-b-minimal-human-task-walkthrough-2026-09-02.zh-CN.md`](../03_Evolution/02_Experiments/gate-b-minimal-human-task-walkthrough-2026-09-02.zh-CN.md)

### `IA-HI-CONF-008` — Evidence of Conformance

未来稳定版本 SHOULD 保存可追踪的测试 / 审计结果，作为 Conformance Evidence。

- Conformance：`Artifact + Review`

---

## 5. Requirement → Test → Evidence 模型

目标链：

```text
IA Requirement
      ↓
Conformance Rule
      ↓
Automated / Browser / Manual / Human Test
      ↓
Result
      ↓
Evidence / Conformance Report
```

ACT Rules Format 可用于 Accessibility rule 的机器可共享表达，但 IA 不应假装所有 Human Interface Requirement 都适合自动化。

---

## 6. 第一版 Gate B 测试分层

### Layer 1 — Static Checks

适合：
- heading / landmark；
- Link / Button 语义；
- stable href；
- duplicate IDs；
-明显 label leakage；
- required semantic states。

### Layer 2 — Browser E2E

至少覆盖：
- normal resource navigation；
- Back / Forward；
- Filter；
- Recenter / Explore；
- keyboard；
- focus；
- JS disabled；
- small viewport / zoom / reflow；
- light / dark / reduced-motion preference（触发时）。

### Layer 3 — Accessibility Evaluation

组合：
- automated accessibility scanner；
- keyboard walkthrough；
- semantic / accessible-name review；
- 对复杂组件进行必要辅助技术人工检查。

### Layer 4 — Human Task Evaluation

代表任务至少包括：
- Identify an object；
- Find implementations for a capability；
- Understand a relation；
- Compare alternatives；
- Verify evidence；
- Explore and return。

Gate B 的最小执行证据见 [`../03_Evolution/02_Experiments/gate-b-minimal-human-task-walkthrough-2026-09-02.zh-CN.md`](../03_Evolution/02_Experiments/gate-b-minimal-human-task-walkthrough-2026-09-02.zh-CN.md)。更大规模 usability research 不是 v0.1 Foundation 的毕业前置条件，除非后续 P0 evidence 证明当前核心任务仍存在结构性阻塞。

---

## 7. Conformance 状态词

Profile Audit SHOULD 使用：

- `Conform`
- `Partial`
- `Non-conform`
- `Not applicable`
- `Unknown / Needs test`

`Unknown` 不应为了提高 PASS 率被自动视为 Conform。

机器 PASS 同样不等于 Human / Semantic / Governance PASS。

---

## 8. 当前证据

第一次网站 Audit 已提供一个重要基线：

- heading level 基础总体正确；
- 早期缺 `<main>` / semantic breadcrumb；
- Link / Button 基础较正确；
- contrast 静态检查没有发现明显主文字问题；
- keyboard / focus / target size / reflow 等仍需要真实 Browser evaluation；
- 当时还没有正式 Browser E2E / accessibility conformance pipeline。

此后 Gate B 已补充真实 Browser E2E，并覆盖 stable navigation、Back / Forward、keyboard / focus、JS disabled、narrow viewport / reflow、reduced-motion preference、Local Map loading / success / failure，以及四个 Core Identity Family 的代表 Resource Page。

#96 进一步执行代表 Human Task Walkthrough：Chromium suite 在该切片上共执行 19 tests，全部通过；其中 5 个测试直接覆盖 Identify / Find / Relate / Verify / Local Map representative path。Compare 使用已合并的 Minimal Compare deterministic fixture，以明确任务上下文完成最小语义走查，而不是虚构一个尚不存在的完整 Compare UI。

Knowledge Model 机器线的 deterministic Machine Review 仍然只是另一类证据，**不能替代 Human Interface 的 Browser / Accessibility / Human evaluation**。

---

## 9. 当前 Gap

### `HI-CONF-GAP-001` — Browser test harness

**Gate B minimum：closed。**

真实 Chromium E2E 已成为可重复 workflow，并覆盖当前代表 Human Route 核心行为。扩大所有页面 / 所有组件覆盖继续作为后续工程质量工作。

### `HI-CONF-GAP-002` — Requirement registry / report format

当前 `IA-HI-*` ID 已稳定到足以审计，但尚没有机器可读 requirement → test mapping。Gate B 可先用 Markdown matrix；后续再判断是否值得结构化。

### `HI-CONF-GAP-003` — Accessibility target exceptions

WCAG 2.2 AA 目前是 SHOULD target。后续需要明确：哪些类型的例外允许、谁批准、如何记录，以及何时升级为更强项目合同。

### `HI-CONF-GAP-004` — Human evaluation protocol

**Gate B minimum：closed by #96。**

最小任务评价模板已经形成，并对代表切片实际执行；Browser-observable tasks 有真实 Chromium evidence，Compare 有明确 semantic fixture。更大规模用户研究、tree testing sample size 与长期 usability measurement 继续作为 Gate B 后工作，除非新的 P0 evidence 证明存在结构性问题。

### `HI-CONF-GAP-005` — Broader accessibility capability modeling

现有 Atlas `web_accessibility` 对 ISO 9241-20 / 171 的范围只是部分投影。该知识建模 Gap 已记录，Human Interface 不应把这些标准错误缩窄成仅 Web。

---

## 10. 与其他 Profile 的关系

Accessibility / Conformance 横向验证：

- Information Architecture：任务是否能找到；
- Information Presentation：结构、reading order、labels 是否可理解；
- Interaction：keyboard、state、feedback、recoverability；
- Visual Presentation：contrast、focus、reflow、motion、非颜色编码。

**Gate B PASS 必须有 Conformance Evidence；仅有五份文档不够。**
