# InteropAtlas Human Interface Standards Baseline

> 状态：Provisional Baseline（暂定标准基线）
>
> 目的：在继续设计 InteropAtlas Human-readable Route 之前，先建立可追溯的外部标准与成熟方法基础。IA 不把 ISO、W3C Recommendation、Authoring Pattern、Design System、产品实践混为一类，而是按依据强度分层采用。

## 1. 采用层级

### A. Normative Standards（规范性标准）

优先级最高。包括 ISO / IEC International Standard、W3C Recommendation、WHATWG Living Standard 等具有正式规范地位的文件。

当前第一批核心：
- ISO 9241-210:2019 — Human-centred design for interactive systems
- ISO 9241-110:2020 — Interaction principles
- ISO 9241-112:2025 — Principles for the presentation of information
- ISO 9241-125:2017 — Guidance on visual presentation of information
- ISO/IEC 40500:2025 / WCAG 2.2 — Web Content Accessibility Guidelines

后续重点：
- ISO 9241-11:2018 — Usability: Definitions and concepts
- ISO 9241-20:2021 — Accessibility within ISO 9241
- ISO 9241-161:2025 — Visual user-interface elements
- ISO 9241-171:2025 — Software accessibility
- ISO 9241-220:2019 — Organizational HCD processes
- ISO 9241-221:2023 — HCD process assessment model
- ISO/TR 25060:2023 及 25060 系列 — usability-related information / CIF
- WAI-ARIA 1.2
- ACT Rules Format 1.1
- HTML Living Standard / CSS / URL 等 Web 基础规范

### B. Authoring Patterns / Methods（实现模式与方法）

这些通常不是国际标准，但用于把上层原则落实为可执行交互。

重点参考：
- WAI-ARIA Authoring Practices Guide (APG)
- Shneiderman: Overview first, zoom and filter, then details-on-demand
- Furnas: Focus + Context / Generalized Fisheye Views
- Information Architecture（信息架构）成熟方法
- Progressive Enhancement（渐进增强）

### C. Reference Implementations（参考实现）

用于研究成熟系统如何将原则转化为组件、布局和交互；不能因为某产品这样做就自动升级为 IA 规范。

重点参考：
- USWDS
- GOV.UK Design System
- IBM Carbon Design System
- Material Design
- Apple Human Interface Guidelines
- Neo4j Bloom

### D. IA Profile / Specification（IA 自身配置与规范）

仅当外部标准不足以直接回答 IA 的具体问题时建立。每条重要 IA 规则必须记录：
1. 用户任务；
2. 上游标准 / Prior Art；
3. 直接采用、Profile、组合还是扩展；
4. 为什么需要 IA 特定约束；
5. 如何测试符合性。

原则：

> Adopt → Profile → Extend → Invent.
>
> 能采用就采用；不能直接采用时优先 Profile / 组合；只有真实缺口存在时才创造。

## 2. 第一版 Human Interface 骨架

### ISO 9241-210：设计过程

作用：规定 IA 不应从“先画页面”开始，而应先理解用户、任务、使用场景、需求，再迭代设计并进行以用户为中心的评价。

对应 IA：
- Human-readable Route；
- 用户任务与 Entry Point；
- 原型与真实使用反馈；
- 设计迭代和评价。

### ISO 9241-110：交互原则

作用：提供与具体技术无关的交互原则，约束 IA 的链接、按钮、筛选、导航、地图探索等交互。

对应 IA：
- self-descriptiveness；
- conformity with user expectations；
- controllability；
- learnability；
- robustness against use error；
- suitability for user tasks；
- user engagement。

### ISO 9241-112：信息呈现原则

作用：约束信息如何被察觉、区分、理解和组织，覆盖视觉、听觉、触觉/触感等呈现模态。

对应 IA：
- 对象页面信息层级；
- Relation / Capability / Evidence 的可区分表达；
- 页面摘要与渐进披露；
- 地图信息密度；
- 表格、文本及未来导出视图。

### ISO 9241-125：视觉信息呈现

作用：进一步指导软件控制的视觉信息组织、编码方式，以及如何考虑人的感知和记忆能力。

对应 IA：
- typography / hierarchy；
- grouping；
- visual coding；
- relation labels；
- 状态、类别和证据强度的视觉编码。

注意：该标准本身不负责具体 chart / graph visualization 细节，因此关系图仍需结合信息可视化研究与成熟图库 Prior Art。

### ISO/IEC 40500:2025 / WCAG 2.2：Web 无障碍基线

作用：为网页内容建立可测试的 accessibility 要求。

IA 暂定目标：

> Human-readable Web SHOULD target WCAG 2.2 Level AA unless a documented exception exists.

对应：
- 颜色对比；
- 键盘操作；
- focus；
- link purpose；
- consistent identification；
- target size；
- heading / landmark 结构；
- 辅助技术兼容。

## 3. IA 建设流程

```text
External Standards
        ↓
Standards / Prior Art Study
        ↓
Human Interface Requirements
        ↓
IA Human Interface Profile
   ↙         ↓          ↘
Interaction  Information  Visual
        ↓
Components / Navigation / Graph Views
        ↓
Conformance Rules
        ↓
Browser E2E + Accessibility + Human Evaluation
        ↓
Human-readable Website
```

网页不是标准化过程的起点，而是规范的一个实现与验证场。

## 4. 需要保持的边界

- ISO 的受版权保护全文不复制进入 IA；IA 记录标准身份、范围、官方来源和自己的摘要 / applicability assessment。
- W3C Recommendation 与 Community Group Report 必须区分状态。
- APG / Design System / 产品行为是实现参考，不应自动描述成国际标准。
- IA 自身形成的 Design Profile 不能冒充上游标准的原文要求。
- 视觉美学并非 ISO 9241-110 的主要范围；品牌与审美仍需单独建立 IA Visual Language，但必须满足可用性、信息呈现和 accessibility 约束。

## 5. 第一批官方来源

- ISO 9241-210:2019: https://www.iso.org/standard/77520.html
- ISO 9241-110:2020: https://www.iso.org/standard/75258.html
- ISO 9241-112:2025: https://www.iso.org/standard/87518.html
- ISO 9241-125:2017: https://www.iso.org/standard/64839.html
- WCAG 2.2 / ISO/IEC 40500:2025: https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/
- WAI-ARIA 1.2: https://www.w3.org/TR/wai-aria-1.2/
- ACT Rules Format: https://www.w3.org/WAI/standards-guidelines/act/
- Design Tokens Format 2025.10: https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/

## 6. 下一阶段

第一阶段只建立标准骨架，不继续修改网页视觉。

顺序：
1. 将第一批核心标准正式收录到 Atlas；
2. 建立 Human Interface capability vocabulary；
3. 建立标准之间以及标准 → capability 的关系；
4. 研究 APG / Design Systems / IA methods，形成组件级 Profile；
5. 再设计 IA 网站信息架构和视觉语言；
6. 使用 #13 的真实浏览器 E2E 与 accessibility evaluation 验收。
