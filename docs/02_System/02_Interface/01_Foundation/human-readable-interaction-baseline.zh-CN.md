# InteropAtlas 人类可读交互基线

<!-- InteropAtlas Document Metadata v0
Document Status: Provisional Baseline（暂定交互基线）。
Document Created At: 2026-08-31T22:31:22+08:00
Document Updated At: 2026-08-31T22:34:35+08:00
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

> 状态：Provisional Baseline（暂定交互基线）。
>
> 目的：在继续建设 Human-readable Route 之前，为网站导航、局部地图、筛选与后续图探索建立可解释、可复用、可测试的交互依据。优先采用 Web 标准、成熟 HCI 方法和成熟图谱产品实践；只有真实缺口存在时才创造 IA 自有模式。

## 1. 决策顺序

设计新交互前依次检查：

```text
Web / Accessibility 标准
        ↓
成熟 HCI / 信息可视化方法
        ↓
成熟图谱产品 / 开源库 Prior Art
        ↓
能直接采用则采用
        ↓
能组合 / Profile 则组合
        ↓
仍有真实缺口时才创建 IA 自有交互模式
```

任何重要交互都应能够回答：

1. 用户任务是什么？
2. 采用了什么外部标准、方法或 Prior Art？
3. 为什么它适合 IA？
4. IA 做了哪些必要扩展？
5. 如何验证它没有破坏一致性、可访问性和基础导航？

## 2. Web 语义基线：Link 与 Button 分工

依据：
- WHATWG HTML `<a>` / hyperlink 语义：https://html.spec.whatwg.org/multipage/links.html
- WHATWG HTML `<button>`：https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element
- WAI-ARIA APG Link Pattern：https://www.w3.org/WAI/ARIA/apg/patterns/link/
- WAI-ARIA APG Button Pattern：https://www.w3.org/WAI/ARIA/apg/patterns/button/

采用规则：

### Link（链接）

用于“前往一个资源”。

IA 中：
- 对象名称 / 标题如果可打开对象详情页，应使用原生 `<a href>`；
- 点击对象标题应始终导航到该对象资源；
- 不使用 JavaScript `preventDefault()` 把一个看起来和语义上都是 Link 的元素改造成局部地图动作；
- 保留浏览器原生行为，如复制链接、新标签页打开、键盘 Enter、上下文菜单。

### Button（按钮）

用于“在当前上下文触发动作”。

IA 中：
- `以此为地图中心`；
- 关系筛选；
- 主题切换；
- 后续的展开、收起、重置地图等动作；

都应使用原生 `<button type="button">`。

原则：

> **Navigate with links; act with buttons.**
>
> 导航用链接，动作使用按钮。

## 3. 一致性与可预期性

依据：
- WCAG 2.x / 2.2 Success Criterion 3.2.4 Consistent Identification：https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html
- WCAG Link Purpose：https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html

采用规则：
- 同一种对象标题在不同页面承担相同功能；
- 同一种按钮在不同对象页使用相同名称和行为；
- 不允许“GitHub Actions 标题在 A 页面用于聚焦，在 B 页面却用于跳转”这类语义漂移；
- 用户应能从控件外观和名称预测结果。

## 4. 信息可视化方法：Overview → Filter → Details

依据：Ben Shneiderman 的 Information Visualization Mantra：

> Overview first, zoom and filter, then details-on-demand.

参考：
- https://www.cs.umd.edu/~ben/about.html

对应 IA：

```text
Capability-first 首页 / 全局入口
        ↓
Local Map / 一跳邻居概览
        ↓
按来源 / 关系语义筛选
        ↓
对象详情页 / Explanation / Comparison
```

因此当前的“概览 + 筛选 + 详情”方向有成熟 HCI 方法依据，不应被理解为 IA 自创交互模式。

## 5. Focus + Context（焦点 + 上下文）

依据：G. W. Furnas, *Generalized Fisheye Views*, CHI 1986。
- DOI: https://doi.org/10.1145/22627.22342

核心思想：用户关注的局部对象需要高细节显示，同时保留周围上下文，而不是每次都展示整张巨大网络。

对应 IA 当前 Local Map：

```text
入向邻居 ← 当前地图中心 → 出向邻居
```

这是 IA 当前“只展示一跳邻居、不急着一次画完整图”的理论依据之一。

## 6. 成熟图谱产品 Prior Art：Neo4j Bloom

参考：
- Scene interactions：https://neo4j.com/docs/bloom-user-guide/current/bloom-visual-tour/bloom-scene-interactions/
- Default actions：https://neo4j.com/docs/bloom-user-guide/current/bloom-appendix/bloom-appendix/

Bloom 将图探索中的不同任务显式分开，例如：
- Inspect：查看节点详情；
- Expand：展开邻居；
- Select related nodes；
- Fit to selection；
- 按关系类型和方向选择性扩展。

对 IA 的直接启示：

> **“查看对象详情”和“改变地图焦点 / 展开邻居”应当是两个明确动作。**

因此 IA 不应通过劫持对象标题链接来完成地图聚焦。

## 7. 地图状态与浏览器历史

依据：WHATWG HTML History API：
- https://html.spec.whatwg.org/multipage/nav-history-apis.html

后续方向：
- 地图中心变化、筛选条件等重要探索状态，应研究是否通过 URL query / fragment + `history.pushState()` 表达；
- 浏览器 Back / Forward 应能够恢复探索状态；
- 用户应能够复制 / 分享某个有意义的地图状态；
- 不应长期依赖“只有当前 JavaScript 内存知道用户走到哪里”的不可恢复状态。

这一项尚未完成，属于下一阶段设计要求。

## 8. Progressive Enhancement（渐进增强）

参考：
- MDN Progressive Enhancement：https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement

采用规则：
- 基础 HTML 页面和对象链接在没有 JavaScript 时仍应可用；
- JavaScript 用于增强 Local Map、筛选和连续探索；
- 增强失败不应破坏基础对象导航；
- 不应为了一个高级交互功能牺牲普通超文本链接的稳定性。

## 9. 图形库 / 渲染器 Prior Art Check

在 IA 从当前简单 HTML/CSS Local Map 升级为真正大型交互式图谱前，必须先评估成熟方案，而不是直接自写完整图渲染引擎。

至少包括：
- Cytoscape.js — 图模型、分析和交互式网络可视化：https://js.cytoscape.org/
- Sigma.js — 面向大规模图的 WebGL 渲染：https://www.sigmajs.org/
- Graphviz — 成熟自动图布局与 DOT：https://graphviz.org/
- D3 / d3-force — 可组合图形与 force-directed layout：https://d3js.org/d3-force

当前结论：
- 现阶段一跳 Local Map 规模很小，纯静态 HTML/CSS 足以验证信息架构；
- 当需求进入自由拖拽、缩放、上千节点、自动布局、多层展开等阶段时，必须重新执行 Prior Art Check；
- 若成熟库能满足需求，应优先集成，而不是重复实现图渲染、布局和交互基础设施。

## 10. IA Local Map Interaction Contract v0.1

当前暂定合同：

### 对象标题
- 语义：Link；
- 动作：打开对象详情页；
- 必须保持原生 `<a href>` 行为。

### `以此为地图中心`
- 语义：Button；
- 动作：只改变当前 Local Map 的焦点；
- 不改变正文对象页；
- 如果增强失败，标题链接仍然可正常访问详情页。

### Filters
- 语义：Toggle Buttons；
- 使用 `aria-pressed` 表达状态；
- 筛选只改变 View，不改变底层 Graph / Facts。

### Page Object 与 Map Center

必须明确区分：

```text
Page Object = 当前正在阅读的对象页面
Map Center  = 当前局部地图正在观察的中心节点
```

两者可以不同，UI 文案不能混淆。

## 11. 最小验收规则

每次修改 Local Map 交互至少验证：

1. 点击对象标题是否始终打开对象详情页；
2. 点击 `以此为地图中心` 是否留在当前页面并只更新地图；
3. 同一种控件在 Capability / Standard / Implementation 页面行为是否一致；
4. 不运行 JavaScript 时，对象详情导航是否仍可用；
5. 键盘 Enter / Space 行为是否符合 Link / Button 语义；
6. 筛选是否只改变显示而不改变 Graph 数据；
7. 新交互是否已有 Prior Art / 标准依据，若没有则记录 IA 为什么必须扩展。

## 12. 当前已确认的反例

2026-08-31 的 Local Map 实验曾将对象名称 `<a href>` 的默认跳转通过 JavaScript `preventDefault()` 拦截，并改造成“设为地图中心”动作。

该方案造成：
- 同样外观的标题在不同区域行为不一致；
- 用户无法仅凭 Link 语义预测结果；
- 失去部分原生超文本行为；
- 与 WAI-ARIA Link / Button 分工不一致。

结论：**废弃该交互模式，不作为 IA 后续模式参考。**

## 13. 浏览器级交互验收

仅仅做到：

```text
Python 运行成功
→ HTML 能生成
→ GitHub Pages 部署成功
```

不能证明真实用户交互正确。

依据：
- W3C WebDriver：https://www.w3.org/TR/webdriver/
- W3C Browser Testing and Tools Working Group：https://www.w3.org/groups/wg/browser-tools-testing/
- Playwright Test：https://playwright.dev/docs/intro

后续交互功能的最低交付要求应逐步升级为：

```text
Static / Unit checks
        ↓
Site build
        ↓
Real browser E2E
        ↓
Pages deployment
```

至少覆盖：
- 点击对象标题，浏览器是否真实导航到目标对象页；
- 点击 `以此为地图中心`，URL / 正文是否保持符合设计，地图中心是否真实变化；
- 筛选按钮是否真实改变可见节点和统计；
- 深色模式切换是否真实生效；
- 浏览器 Back / Forward 在引入地图 History 状态后是否正确恢复；
- Capability / Standard / Implementation 三类页面是否行为一致。

工具层面优先采用现成浏览器自动化实现，例如 Playwright；不自行发明浏览器测试协议。

原则：

> **构建成功 ≠ 交互验收成功。**

---

本文件本身不是最终 IA Standard；它是用于约束当前 Human-readable Route 的 Provisional Baseline，并应随真实使用反馈和外部标准研究持续修订。
