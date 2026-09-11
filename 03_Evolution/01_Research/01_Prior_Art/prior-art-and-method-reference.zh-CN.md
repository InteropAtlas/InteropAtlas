# InteropAtlas 参考项目与方法索引

<!-- InteropAtlas Document Metadata v0
Document Status: Living Reference（持续维护参考）。目的不是把 InteropAtlas 绑定到这些项目，而是在设计每一层能力时优先参考成熟实践，减少重复造轮子。
Document Created At: 2026-08-31T19:35:31+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

> 状态：Living Reference（持续维护参考）。目的不是把 InteropAtlas 绑定到这些项目，而是在设计每一层能力时优先参考成熟实践，减少重复造轮子。

## 使用原则

在设计新的数据模型、标识体系、验证规则、文档结构、治理流程、交互方式或标准化机制之前，优先执行 Prior Art Check（既有方案调查）：

```text
我们遇到了什么问题？
        ↓
已有成熟方案是否解决？
        ↓
能否直接采用？
        ↓
不能直接采用，能否 Profile / 组合 / 扩展？
        ↓
只有真实缺口仍存在时，才创建 IA 自有方法或规范
```

参考不是照抄。InteropAtlas 最终需要统一完整的模型与体验，但应尽量建立在成熟概念和长期实践上。

## 1. Wikidata

**重点参考：知识图谱数据模型、Statement、Qualifier、Reference、Rank、人机双重访问。**

可借鉴：
- Item / Property / Statement 的清晰分工；
- Statement 不止是简单关系，可以附加 qualifier、reference 和 rank；
- 时间、地域、适用范围等上下文不必塞进 predicate 名称；
- 人类实体页和机器 API / 查询服务共享同一事实基础；
- 多个冲突或不同时间点的事实可以共存，并附加来源和上下文。

重点页面：
- Data model: https://www.wikidata.org/wiki/Wikidata:Data_model
- Statements: https://www.wikidata.org/wiki/Help:Statements/en
- Qualifiers: https://www.wikidata.org/wiki/Help:Qualifiers/en

对应 IA：Relation context、Evidence / Provenance、Graph、Human Route、Machine Route。

## 2. OpenStreetMap（OSM）

**重点参考：简单底层元素 + 开放标签 + 多种渲染 / 地图视图 + 社区词汇治理。**

可借鉴：
- 底层保持简单，复杂地图由上层 Renderer / View 产生；
- Node / Way / Relation 与 Tag 组合成丰富世界模型；
- Relation 是一等结构，不依赖目录层级表达所有关系；
- 同一数据可以产生不同地图样式和用途；
- 开放词汇具有强扩展性，但长期必须依靠社区约定、文档、统计和治理避免失控；
- “Relations are not categories” 对 IA 很重要：关系不应被错误用作唯一分类树。

重点页面：
- Data model / Elements: https://wiki.openstreetmap.org/wiki/Data_model
- Relation: https://wiki.openstreetmap.org/wiki/Relation
- Tag: https://wiki.openstreetmap.org/wiki/Tag

对应 IA：Flat Objects + Rich Relations + Dynamic Maps、Relation vocabulary、Map/View、Governance。

## 3. FAIR Principles

**重点参考：机器可行动数据、持久标识、丰富 metadata、qualified references、provenance、license。**

FAIR = Findable、Accessible、Interoperable、Reusable。

可借鉴：
- globally unique and persistent identifier；
- rich metadata；
- searchable / indexed resources；
- standardized communication protocol；
- qualified references；
- clear license；
- detailed provenance；
- machine-actionability 应作为目标，而不是附带效果。

重点页面：
- FAIR Principles: https://www.go-fair.org/fair-principles/
- Practical FAIRification framework: https://www.go-fair.org/how-to-go-fair/

对应 IA：Machine Route、Trust Route、ID、Metadata、Interoperability、Curation。

## 4. W3C DCAT 3

**重点参考：Catalog、Resource、Version、Qualified Relation、Federation。**

可借鉴：
- Catalog 本身也可以拥有结构化描述；
- resource / dataset / service 等资源可被统一目录化；
- version / previous version / current version 等版本关系；
- qualified relation；
- 多目录之间可以聚合和 federation，而不一定要求所有数据进入唯一仓库；
- Latest version 与特定日期版本 URL 分离。

重点页面：
- DCAT 3: https://www.w3.org/TR/vocab-dcat-3/

对应 IA：Map of Maps、Federation、Versioning、Relation context、未来多 Atlas 互联。

## 5. W3C SHACL

**重点参考：结构化约束、验证报告、验证规则复用于 UI / 数据集成。**

可借鉴：
- Data Graph 与 Shapes / Constraints 分离；
- Validation 应生成结构化 Validation Report，而不仅是 CI PASS / FAIL；
- 相同约束信息可以同时服务数据验证、UI、代码生成和数据集成；
- 验证规则本身也是可版本化资产。

重点页面：
- SHACL Recommendation: https://www.w3.org/TR/shacl/

对应 IA：Validator、Atlas Health、编辑器提示、Agent 自动修复、Schema evolution。

## 6. Diátaxis

**重点参考：人类文档不能只靠一种页面解决所有需求。**

四类文档：
- Tutorial；
- How-to Guide；
- Reference；
- Explanation。

可借鉴：
- Standard/Object 页面更接近 Reference；
- “为什么存在、如何理解方案空间”属于 Explanation；
- “如何选择 / 如何完成任务”属于 How-to；
- 不应把所有说明都塞进一个无限增长的对象详情页；
- 文档结构应反映被描述系统的结构，但不同阅读目的需要不同 View。

重点页面：
- Overview: https://diataxis.fr/start-here/
- Reference: https://diataxis.fr/reference/

对应 IA：Human Route、Readable、Understandable、Actionable、Standard Family Guide。

## 7. IETF / RFC 工作方式

**重点参考：草案命名、版本、成熟过程、稳定编号与草案迭代分离。**

可借鉴：
- Internet-Draft 名称具有明确格式；
- 草案 revision 使用独立递增编号；
- 工作组采纳和正式 RFC 身份不等于原草案文件名；
- 名称、版本、状态、正式标准编号应被分开考虑；
- 不应让一个临时文件名承担全部身份语义。

重点页面：
- Naming your Internet-Draft: https://authors.ietf.org/naming-your-internet-draft

对应 IA：自产 Specification / Standard 的命名、Draft 生命周期、ID 与版本分离。

## 8. W3C Process

**重点参考：标准不是写完一份文档就结束，而是治理、review、实现经验和长期 revision 的结果。**

可借鉴：
- charter / group / review / candidate / recommendation 等阶段背后的职责分工；
- Candidate 阶段重视实现经验；
- comments、objections、consensus、revision 都需要正式处理；
- 标准生命周期和组织治理需要分离设计。

重点页面：
- W3C Process Document: https://www.w3.org/policies/process/

对应 IA：Governance / Standardization Route、自产规范生命周期。

## 9. Software Heritage / SWHID

**重点参考：Persistent Identifier（持久标识）与资源 URL / 显示名称分离。**

可借鉴：
- identifier 需要长期稳定；
- identifier scheme 本身可以有版本；
- identifier 可通过 resolver 访问，但 identifier 不等于网页 URL；
- qualifier 可以对持久标识增加上下文。

重点页面：
- SWHID specification: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html

对应 IA：自产标准 ID、对象 Persistent ID、Resolver、版本与 URL 分离。

## 10. WHATWG HTML + WAI-ARIA APG + WCAG

**重点参考：网站交互语义、Link / Button 分工、键盘行为、一致性与可预期性。**

可借鉴：
- `<a href>` 是前往资源的 Hyperlink，不应被随意劫持成局部动作；
- `<button>` 用于当前上下文中的动作；
- 同一功能的组件在不同页面应被一致识别和操作；
- Link 文本应让用户能够理解点击后会发生什么；
- 优先使用原生 HTML 语义，而不是自造相似控件。

重点页面：
- HTML links: https://html.spec.whatwg.org/multipage/links.html
- HTML button: https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element
- WAI-ARIA Link Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/link/
- WAI-ARIA Button Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/button/
- WCAG Consistent Identification: https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html

对应 IA：Human Route、Local Map、导航、筛选、可访问性、交互规范。

## 11. Shneiderman Information Visualization Mantra

**重点参考：信息可视化任务顺序。**

经典原则：

> Overview first, zoom and filter, then details-on-demand.

可借鉴：
- 先提供结构概览；
- 再让用户缩小范围、筛选关系；
- 最后按需进入对象详情；
- 不应一开始就把全部图数据和全部细节同时压给用户。

重点页面：
- Ben Shneiderman: https://www.cs.umd.edu/~ben/about.html

对应 IA：Capability-first 首页、Local Map、关系筛选、对象详情、后续全局地图。

## 12. Furnas — Focus + Context / Fisheye Views

**重点参考：大型信息结构中的焦点 + 周边上下文。**

可借鉴：
- 用户当前关注对象显示更详细；
- 周边邻居作为上下文保留；
- 不必为了理解一个局部对象而一次显示完整巨大网络。

重点页面：
- G. W. Furnas, Generalized Fisheye Views, CHI 1986: https://doi.org/10.1145/22627.22342

对应 IA：一跳 Local Map、局部探索、未来 semantic zoom / focus+context 视图。

## 13. Neo4j Bloom

**重点参考：成熟知识图谱产品中的节点探索、Expand、Inspect、按关系类型 / 方向展开。**

可借鉴：
- Inspect（查看详情）与 Expand（展开邻居）是不同动作；
- 可以从一个节点逐步扩展其 immediate neighbors；
- 可以按关系类型和方向选择性扩展；
- 图探索不等于对象详情页导航。

重点页面：
- Scene interactions: https://neo4j.com/docs/bloom-user-guide/current/bloom-visual-tour/bloom-scene-interactions/
- Default actions: https://neo4j.com/docs/bloom-user-guide/current/bloom-appendix/bloom-appendix/

对应 IA：Local Map、连续探索、关系筛选、对象详情与地图聚焦分工。

## 14. Graph visualization libraries

在进入复杂交互图之前需要重点评估：

### Cytoscape.js
- 图理论模型 + 分析 + 交互式可视化；
- 支持 pan、zoom、selection 等成熟交互；
- https://js.cytoscape.org/

### Sigma.js
- 面向大规模图的 WebGL 浏览器渲染；
- 与 graphology 配合；
- https://www.sigmajs.org/

### Graphviz
- 成熟自动图布局；
- DOT 图描述语言；
- 可输出 SVG 等格式；
- https://graphviz.org/

### D3 / d3-force
- 可组合数据可视化与 force-directed layout；
- https://d3js.org/d3-force

对应 IA：未来 Mappable / Explorable 阶段的图渲染与布局选型。

原则：现阶段小规模一跳视图可以继续使用简单 HTML/CSS 验证信息架构；一旦需求进入自由拖拽、缩放、复杂自动布局、上千节点等，应先评估成熟库，不自行重写完整图渲染基础设施。

## 15. Human-Machine Teaming / Human-AI Collaboration

**重点参考：人类与 AI / Agent 作为同一协作系统中的不同参与者时，如何定义角色、责任、监督、交接与组织实施。**

当前最直接的标准化工作仍很新：
- ISO/IEC CD 25589 — Framework for human-machine teaming：定义人机团队关系、技术特征和设计原则，目前仍在 Committee Draft 阶段；
- ISO/IEC AWI 25880 — Requirements and guidance for the organizational implementation of human-machine teaming：面向组织实际部署人机团队，目前仍处于早期工作项目阶段；
- ISO/IEC CD TR 42109 — Use cases of human-machine teaming：收集人机团队实际用例，目前仍在制定中；
- ISO/IEC 5339:2024 — Guidance for AI applications：已发布，强调 AI 应用全生命周期中的 stakeholder engagement；
- NIST AI RMF：要求明确区分 human-AI configuration 中的角色、责任、沟通与 human oversight，并持续记录和评估；
- GitHub Coding Agents / Agentic Workflows：不是标准，但已形成可直接观察的开源协作实现，例如把 Issue 分配给 Agent、Agent 创建 PR、再进入人工 Review。

对 IA 的初步启示：
- AI / Agent 应被建模为协作参与者，而不是项目主题或独立“自动化层”；
- 人与 Agent 应尽量共享同一任务、Review 和贡献流程，只在权限、时限、监督强度等方面按参与者类型 Profile；
- 任务执行者、Reviewer / Overseer 和项目治理者应明确区分，不能把执行、审核和最终授权全部交给同一 Agent；
- 任务分配、交接、超时释放等仓库级机制目前没有可直接照搬的国际标准，IA 应在上述上位原则基础上形成最小 Open Collaboration Profile，并继续观察 ISO/IEC 25589 / 25880 的演进。

重点页面：
- ISO/IEC 25589: https://www.iso.org/standard/90831.html
- ISO/IEC 25880: https://www.iso.org/standard/91833.html
- ISO/IEC TR 42109: https://www.iso.org/standard/88243.html
- ISO/IEC 5339: https://www.iso.org/standard/81120.html
- NIST AI RMF Core / Human-AI Interaction: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- GitHub coding agents: https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents

对应 IA：Curation / Contribution Route、Open Collaboration、Agent participation、任务分配、Review / Oversight、未来多 Agent 协作。

## 后续可继续扩展的参考池

已知还值得按需要逐步深入：
- RDF / JSON-LD：图语义与交换；
- SKOS：知识组织、broader / narrower / related；
- OWL：正式 ontology；
- ISO / IEC Directives：更重型标准治理；
- OASIS、Khronos、IETF Datatracker、W3C TR：标准发布与版本管理；
- GitHub / Rust RFC / Python PEP：开源社区中的轻量提案流程；
- Schema.org：开放词汇演进；
- SPDX：机器可读规范与生态协作；
- NIST interoperability frameworks：跨领域互操作规划。

原则：需要解决具体问题时再深入对应参考，不为“研究完整”而提前研究所有体系。