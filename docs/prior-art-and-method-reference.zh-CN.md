# InteropAtlas 参考项目与方法索引

> 状态：Living Reference（持续维护参考）。目的不是把 InteropAtlas 绑定到这些项目，而是在设计每一层能力时优先参考成熟实践，减少重复造轮子。

## 使用原则

在设计新的数据模型、标识体系、验证规则、文档结构、治理流程或标准化机制之前，优先执行 Prior Art Check（既有方案调查）：

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
