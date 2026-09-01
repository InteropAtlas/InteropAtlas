# Human Interface — Reference Intake Audit — 2026-09-01

> 状态：Point-in-time Intake Audit
>
> 目的：把 #14 Human Interface Standards Package 实际依赖的上游标准与成熟先例，从研究文档中的参考列表推进到 Canonical Atlas；能准确建模的直接入库，不能准确建模的明确记录为 Intake / Model Gap。

## 1. 本轮范围

本轮只做一个小步：**补齐 #14 第一批核心中已经明确、且现有 `standard` 模型可以准确表达的 ISO 9241 缺口。**

不在本轮：
- 不开始网页视觉重构；
- 不开始 Human Interface 五个 Profile 的大规模写作；
- 不提前拍板 #15 的 Method / Guideline / Design System 模型；
- 不把非规范性参考强塞进 `standard`。

## 2. 审计前已经进入 Atlas 的核心依据

已有 Canonical Objects：

- `iso_9241_210_2019` — Human-centred design；
- `iso_9241_110_2020` — Interaction principles；
- `iso_9241_112_2025` — Presentation of information；
- `iso_9241_125_2017` — Visual presentation of information；
- `wcag_2.2` — WCAG 2.2；
- `wai_aria_1.2` — WAI-ARIA 1.2；
- `act_rules_format_1.1` — ACT Rules Format 1.1；
- `html_living_standard` — HTML Living Standard；
- `design_tokens_format_2025.10` — Design Tokens Format；
- `aria_apg`、`uswds`、`govuk_design_system` — 当前以 Reference Project / Guidance Collection 表达的成熟参考。

## 3. 本轮新增的正式标准

### ISO 9241-11:2018

ID：`iso_9241_11_2018`

路径：`standards/iso-9241-11-2018.yaml`

作用：为 usability、user / goal / context of use 与评价提供概念基线。

官方状态：Published International Standard。

### ISO 9241-20:2021

ID：`iso_9241_20_2021`

路径：`standards/iso-9241-20-2021.yaml`

作用：把 accessibility 与 ISO 9241 系列、尤其 Human-centred Design process 连接起来。

官方状态：Published International Standard。

### ISO 9241-161:2025

ID：`iso_9241_161_2025`

路径：`standards/iso-9241-161-2025.yaml`

作用：视觉用户界面元素的选择、使用与依赖关系；用于组件级 Visual / Interaction Profile，不把它扩大成品牌审美标准。

官方状态：Published International Standard。

### ISO 9241-171:2025

ID：`iso_9241_171_2025`

路径：`standards/iso-9241-171-2025.yaml`

作用：软件无障碍要求与指南；用于补充 WCAG 的 Web 内容无障碍基线。

官方状态：Published International Standard。

## 4. 新增 Graph relations

新增：

`relations/human-interface-iso-accessibility-and-ui.yaml`

表达：
- ISO 9241-11 → Human-system Interaction / usability conceptual basis；
- ISO 9241-20 → Accessibility，并与 ISO 9241-210 关联；
- ISO 9241-161 → Visual Information Presentation；
- ISO 9241-171 → Software Accessibility，并与 ISO 9241-11 关联。

## 5. 本轮实际发现的模型缺口

### Gap HI-CAP-001 — Accessibility Capability 过度 Web-specific

当前 Canonical Capability 中已有：

`web_accessibility`

但 ISO 9241-20 和 ISO 9241-171 的真实范围明显大于 Web：它们覆盖更广的人机交互 / software accessibility。

因此当前关系只能把它们投影到 `web_accessibility`，并在 relation condition 中明确：**这只是现有 Capability 模型中的部分投影，不代表标准范围仅限 Web。**

这说明 Atlas 需要后续验证是否应存在更上位的：

- `accessibility`；或
- `software_accessibility`；或
- 通过 capability hierarchy / broader-narrower relation 表达。

本轮不拍板，只记录为 Capability Model Gap。

这正是 Practice-driven Feedback Loop 的目标：不是为了让字段“看起来完整”而把现实对象压扁到旧模型里。

## 6. 明确进入 #15 的非规范性对象

以下对象真实参与 #14，但当前不应作为 `standard` 入库：

- Shneiderman Visual Information-Seeking Mantra；
- Furnas Focus + Context / Generalized Fisheye Views；
- Nielsen 10 Usability Heuristics；
- Card Sorting；
- Tree Testing；
- Gestalt principles；
- Bertin visual variables；
- Cleveland & McGill graphical perception；
- Munzner Nested Model；
- Grammar of Graphics / Vega-Lite；
- Diátaxis；
- Progressive Enhancement；
- Apple HIG / Material Design 等多角色 Design System / Guideline 对象。

处理：进入 #15 Real-object Fit Test，不先创造错误顶层类型。

## 7. 仍待核验 / 收录的正式标准

下一批正式标准候选：

- ISO 9241-220:2019；
- ISO 9241-221:2023；
- ISO/TR 25060:2023 与相关 CIF 系列；
- W3C WebDriver；
- ISO/IEC 40500:2025 与 WCAG 2.2 的 identity / adoption / equivalence 建模关系。

这些都应先检查 Atlas 是否已有，再决定 reuse / ingest / modeling gap。

## 8. 对 Foundation Gate B 的影响

本轮没有让 Gate B 直接 PASS，但消除了 #14 中四个明确的 formal-standard intake 缺口。

现在 Gate B 的主要瓶颈进一步收敛为两类：

1. **Non-normative Knowledge Object Model（#15）**：Method / Guideline / Heuristic / Framework / Design System；
2. **Human Interface Profiles（#14）**：把上游依据转成带 Requirement IDs 与 conformance 方法的五个 Draft Profile。

因此下一小步不应回到网页实现，而应优先做 #15 的第一组真实对象 Fit Test，使 Human Interface 的非标准依据能够被正确建模。

## 9. Intake Invariant

继续沿用：

```text
Use it
  ↓
Check Atlas
  ↓
已有 → 引用 stable ID
没有 → 现有模型能正确表达？
            ↓            ↓
           Yes           No
            ↓            ↓
          Ingest     Intake / Model Gap
```

Human Interface 现在正式进入这套 Atlas ↔ Practice Feedback Loop。
