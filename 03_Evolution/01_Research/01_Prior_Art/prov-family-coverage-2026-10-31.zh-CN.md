# PROV 固定文献家族与有限实现证据覆盖对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-10-31T08:26:00+00:00
Document Updated At: 2026-10-31T09:07:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / publish_prov_family_coverage
  Reviewer: Independent Agent — OpenAI / dot / prov_independent_review
  GitHub Actor: ff6962757
-->

## 问题与有限结论

表达和交换来源记录、验证记录一致性、访问来源信息，以及证明现实事件为真，是不同问题。本研究对照固定 PROV 家族的文献职责、IA 已有对象/关系和已接纳的 `python_prov` 3.2.3 有限证据，帮助用户与 AI 看清已知与 unknown；不另建知识模型或分类。

**已有 DM、Constraints、AQ 文献记录和一个选定记录构建/JSON 内存读写的库先例，不等于已覆盖整个 PROV 家族。PROV-O 两个既有身份仍处于 hold，精确映射 unknown；其他“未匹配”只是所查记录中的观察，不是真实世界空白或后续待补清单。**

本研究只固定 [PROV-Overview，Working Group Note 2013-04-30](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/) 的 Status 与 §2 所列 **12 份文献，包含 Overview 自身：4 份 Recommendation、8 份 Working Group Note**。§2 roadmap 表只有另外 11 份，不能数成 11 项家族；这些也不是 12 种可互换格式。它不是当前全部 W3C 成果、全部溯源标准或实现全集，不计算领域完备率。各行核对原始日期版本的标题、状态、摘要/职责相关段落，不声称完整符合性审计或已整合后续勘误。

本研究与[既有轻量留痕先例研究](provenance-traceability-prior-art-2026-09-02.zh-CN.md)不同：旧研究回答 IA 的 Adopt / Profile / Defer，本研究回答固定家族与现有证据的对应，不重开其设计决策或开放式收集。既有[知识表示决策压力测试](../03_Tests/knowledge-representation-decision-stress-test-v0.1.zh-CN.md)的模型、验证、序列化、查询解耦原则保持。

记录基线为 2026-10-31 实际核对的 main [`bdeefaa5eeffd2cf152f9096747bbb89324819fe`](https://github.com/InteropAtlas/InteropAtlas/tree/bdeefaa5eeffd2cf152f9096747bbb89324819fe)。以下 canonical 链接固定到该提交；本研究是时点快照，不是实时目录，不刷新原记录验证日期。

## 固定家族逐项对照

下表各文献均为 2013-04-30 原始出版物；Recommendation 与 Working Group Note 是出版身份，不能被仓库通用 `type: standard` / `kind: specification` 抹平。每行只报告当前映射与已接纳证据，不新建关系。

| 原始文献与状态 | 职责 | 固定 canonical 映射 | python_prov 3.2.3 证据与 unknown |
|---|---|---|---|
| [PROV-OVERVIEW](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/)；Working Group Note | 家族导航；说明模型、表示与配套机制。 | 未匹配独立对象；仅作为本研究来源。 | 不是实现规范；不以库方法覆盖导航文献。 |
| [PROV-PRIMER](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/)；Working Group Note | 概念与示例入门，帮助创建或使用 PROV 数据。 | 未匹配独立对象。 | 不是另一个数据模型；未对入门示例作执行核验。 |
| [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/)；Recommendation | 以 OWL 2 表达的本体，支持 RDF 中表示与交换来源记录。 | [`prov_o`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/prov-o.yaml) 与 [`w3c_prov_o`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-o.yaml) 两身份处于既有 hold；精确映射 **unknown**。 | 既有正面范围排除该表示；上游声明不是已验证行为，不作“不支持”判断。 |
| [PROV-DM](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)；Recommendation | 概念数据模型，描述实体、活动、参与者及其关系；独立于具体表示。 | [`w3c_prov_dm`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-dm.yaml) 已录；文献身份对应，原对象仍用通用 URL。 | 既有 [`python_prov_implements_prov_dm_records`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/02_Relations/prov-implementations.yaml) 只覆盖选定记录构建和查询；完整模型符合性 unknown。 |
| [PROV-N](https://www.w3.org/TR/2013/REC-prov-n-20130430/)；Recommendation | 面向人的文本记法，用于写下 PROV 模型实例。 | 未匹配独立文献对象。 | 上游声明支持；既有九项 smoke 未调用该 codec，符合性 unknown。 |
| [PROV-CONSTRAINTS](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/)；Recommendation | 有效性、一致性约束、规范化与等价性定义。 | [`w3c_prov_constraints`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-constraints.yaml) 已录；既有 [`w3c_prov_constraints_uses_prov_dm`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/02_Relations/linked-data-and-hypertext.yaml) 是文献级 uses。 | 文献关系不是软件执行结果；没有验证约束、时序、因果一致性或 unified()。 |
| [PROV-XML](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/)；Working Group Note | PROV 的 XML 表示及 XML schema。 | 未匹配独立文献对象。 | 上游文档/registry 有相关设施；未安装可选依赖或调用该 codec，符合性 unknown。 |
| [PROV-AQ](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/)；Working Group Note | Web 上定位、取得与查询来源信息的机制。 | [`w3c_prov_aq`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-aq.yaml) 已录；是 Working Group Note，不因 kind=specification 变为 Recommendation。 | 内存查询与 JSON 读写不证明网络访问/查询协议、服务托管或远端互通；unknown。 |
| [PROV-DICTIONARY](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/)；Working Group Note | 键—实体对集合的 Dictionary 结构及其相关构造。 | 未匹配独立文献对象。 | 既有正面范围明确排除；本研究不把上游表格转成验证结论。 |
| [PROV-DC](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/)；Working Group Note | Dublin Core Terms 到 PROV-O 的部分映射。 | 未匹配独立文献对象；不借映射绕过 PROV-O hold。 | 不是完整双向转换保证；没有转换执行证据，unknown。 |
| [PROV-SEM](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430/)；Working Group Note | 以一阶逻辑提供声明式语义；未被提出作为 PROV 的规范性或必需语义，也不限制 PROV 使用。 | 未匹配独立文献对象。 | 记录生成和回读不证明完整推理或语义有效性，unknown。 |
| [PROV-LINKS](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/)；Working Group Note | 跨 bundle 链接来源描述的机制。 | 未匹配独立文献对象。 | 既有正面范围排除 nested bundle/Bundle-as-entity；不能由方法名推出跨 bundle 互通，unknown。 |

模型定义“表达什么”，记法/编码决定“怎样写出”，约束定义“一致性意义上何为有效”，访问/查询机制处理“从哪里取得、如何请求”。这些职责相关但不可互相替代；Overview 图 1 只是粗略依赖图，不据它生成技术边。即使记录内部一致，也不能证明现实事件、归因或责任真实。

PROV-O hold 的具体边界是保留两个原对象和原字段，不挑选其中一个作为精确唯一映射、不合并、不修正、不恢复身份处理或新增边。对其他条目的“未匹配独立文献对象”，不等于未有文字提及、库不支持，亦不要求补齐。

## 表外对照：PROV-JSON 不是第十三项

[PROV-JSON，2013-04-24](https://www.w3.org/submissions/2013/SUBM-prov-json-20130424/) 的原始页面明确标为 **W3C Member Submission**。它不在上述 12 份文献中，不是 W3C Recommendation；W3C 发布 Submission 不代表认可该内容。不能把“非 Recommendation”误写成“从未由 W3C 发布”，也不把它加为家族第十三项。

库的 JSON 路径是已接纳软件的有限交换设施，并无额外 JSON/PROV-JSON 格式符合性关系。本研究不据一次内存回读声称满足整份 Submission，也不新增格式对象。

## 已接纳运行证据：仅回读旧九项，不重新执行

[`python_prov`](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/python_prov.yaml) 的身份是 PyPI `prov` 独立 Python 库，固定 **3.2.3**、源码 commit `f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf`。既有记录已记载官方 wheel SHA-256 `bc392921d2cc7e02e03312b2d00da6c7cfdaaee261f76a56f7c57d01f988164e`；本研究未重新下载/执行 wheel 或复验全部源文件，亦不延伸到其他版本、sdist、完整构建或安全保证。

旧作者于 2026-10-29 以 Python 3.12.14 `-I -S` 直接导入该 wheel，未安装依赖。公共[冻结证据 packet 的 runtime_evidence](https://github.com/InteropAtlas/InteropAtlas/blob/be0d200239f8c7f5330384c5a99ab96fdfae9849/01_State/Inbox/review-packets/prov-dm-records-20261029.yaml#L394-L521)嵌入九项结果；其准备稿保留 pending 状态，**不把该稿本身当批准**。独立接纳决定见[既有 acceptance event](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/Inbox/acceptance-events/prov-dm-records-20261029.yaml)，当前有界范围见上述对象与 implements 关系。

| 旧案例（均记为 PASS） | 实际支持的有限事实 |
|---|---|
| exact-wheel-import | 导入版本为 3.2.3。 |
| entity-activity-agent-and-five-relations | 一个九记录图：Entity、Activity、Agent，以及 generation、usage、derivation、attribution、association 五种关系及正式参与者引用。 |
| lookup-and-IRI | 该图按类型/标识查找；不是 Web 查询协议。 |
| explicit-json-dispatch-encode | 显式 `format="json"` 内存编码；不是其他 serializer 执行。 |
| own-output-memory-roundtrip-selected-values | 限定 string/int/bool/QualifiedName 值回读，不是全部类型/任意输入往返。 |
| independently-authored-json-fixture-decode | 另一手写 JSON fixture 回读；不是跨实现测试。 |
| missing-required-entity-accepted-characterization | 缺必需实体参数仍接受，是宽松行为观察而非有效 PROV 证明。 |
| multiple-prov-value-accepted-characterization | 多个 `prov:value` 仍接受，不强制完整断言时结构约束。 |
| duplicate-json-key-warning-last-value-characterization | 重复键警告且最后值保留，不是严格解析保证。 |

调用方仍须提供角色正确的限定名、namespace 与适当属性；Agent 子类型需实际 `QualifiedName` 的 `prov:type`，不是任意同拼写字符串。独立 Plan 工厂、完整 datatype/时间语法、非法输入、nested bundle、Bundle-as-entity、PROV-Dictionary、所有其他 codec、图像、NetworkX、服务托管、自动工作流采集、密码验证及 IA 采用均不在正面范围。没有运行上游全套测试，没有验证 `unified()`、完整 PROV-CONSTRAINTS、时序/因果有效性、权限、真实性或跨实现互通。旧 Python audit guard 未观察到网络/写文件/子进程尝试，只描述旧执行路径，不是 OS 隔离或安全认证。

## 上游声明、代码存在与执行证据分层

固定 [3.2.3 conformance 文档](https://github.com/trungdong/prov/blob/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/docs/reference/conformance.md)声明五种序列化及测试覆盖；[serializer registry](https://github.com/trungdong/prov/blob/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/src/prov/serializers/__init__.py)有注册与可选依赖机制；[PROV-JSON codec](https://github.com/trungdong/prov/blob/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/src/prov/serializers/provjson.py)有具体 JSON 处理设施。这三者不能使其余四种格式自动成为 IA 已验证能力。

固定 [PROV-JSON 使用说明](https://github.com/trungdong/prov/blob/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/docs/howto/provjson.md)还讲文件、流和自动探测；本研究只读取文档，不执行示例，不扩大原来的显式内存 JSON 范围。旧 registry 初始化导入其他无依赖模块，也不表示调用了它们的 codec。上游自述、代码存在、旧作者运行与独立接受决定，是不同证据层。

## 机器读取与有限检索

沿用 `01_State/01_Objects/*.yaml` 和 `01_State/02_Relations/*.yaml`，上表固定 blob 链接即现有机器可读 YAML，不另建矩阵 schema 或第二事实源。关系文件可含多份 YAML 文档，须按明确 relation ID 选取，连同 `source`、`relation`、`target`、`context` 和 `evidence` 阅读，不能把一个 `implements` 或 `uses` 词解释为全面符合性。

在固定基线检索对象 `id`、中英文名称、`official_name`、`official_url`、`sources` 的 PROV 身份/链接，并逐项核对 12 个名称及其官方文献标识；直接对应的对象是上表五条文献记录（含双 PROV-O）及 `python_prov`。关系按这些稳定 ID 检索端点，命中上述两个既有技术关系。通用描述/元数据中的 provenance 字样不是独立 PROV 文献身份；检索结果只反映此快照，不代表所有候选、现实实现或未来状态。

DM、Constraints、AQ 的原对象 URL 是不带日期的官方入口；本研究没有把它们全部改写为精确日期字段。DM 与 Constraints 的原始 2013 版边界由既有关系 `version_context` 与固定来源支持，AQ 的本次身份核对只用于研究，不能冒称原记录已作同等全文验证。

## 固定来源与文件指纹

以下 SHA-256 为本次实际读取的完整原文件字节，不是网页解析视图/HTTP 头散列，也不升级为实现符合性证明。官方原始页均于 2026-10-31 读取；这里只给固定来源与指纹，不镜像第三方全文。canonical 与接受记录固定到基线提交；历史 packet 固定到原冻结提交。

| 来源 | 字节数 | SHA-256 |
|---|---:|---|
| [PROV-OVERVIEW](https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/) | 34025 | `fc45beed479aef763da4dd6e11d1f92e0e7b91e9c19c30a0ed9ba279de36b556` |
| [PROV-PRIMER](https://www.w3.org/TR/2013/NOTE-prov-primer-20130430/) | 109524 | `4db54135a6f06bbee1983e079c6d9bd3d54e5b45eb6ed0f5686e922c665b8c4a` |
| [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) | 464179 | `6b96671ab84faf12ce3f041aca12c3f93a6df2ed242348810743179a68e69555` |
| [PROV-DM](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) | 271572 | `5c925c21bc96c285b25017c3b90d82cf74251d07713b71fcb81ca60f873c9e88` |
| [PROV-N](https://www.w3.org/TR/2013/REC-prov-n-20130430/) | 205708 | `c7320ed45cc643eca0819b0616835529dfb35dc819eaf50deaf209ee1e974e49` |
| [PROV-CONSTRAINTS](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/) | 285333 | `0e65d02339347af6f6e5744cb69a99cf56430e8fd9dd904ac476541634361287` |
| [PROV-XML](https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/) | 156639 | `a9407d19fe83ee7f2f24c53cf2e89d579225a67393986d56baa18a62126adaa7` |
| [PROV-AQ](https://www.w3.org/TR/2013/NOTE-prov-aq-20130430/) | 132659 | `00ac5c1455da2e04ad3d94f4dad6969c78b11e0062c154faab70b680d24c0fc7` |
| [PROV-DICTIONARY](https://www.w3.org/TR/2013/NOTE-prov-dictionary-20130430/) | 183287 | `37503d84b6ef24c9083567feaf55932c56b9005fe3a8f533122283e4e1041497` |
| [PROV-DC](https://www.w3.org/TR/2013/NOTE-prov-dc-20130430/) | 116838 | `2e35c0a5eec557d3919317b269c0834980b10ec59519c90f3529ab40ade871d8` |
| [PROV-SEM](https://www.w3.org/TR/2013/NOTE-prov-sem-20130430/) | 1104908 | `b142a11142e15b6d8504a5dd7e7156c1cba6c237b810f62265f3bc104e12297c` |
| [PROV-LINKS](https://www.w3.org/TR/2013/NOTE-prov-links-20130430/) | 67066 | `7e9b204973b20dad5fe7e205a060be9d20fa6dd5679347d4106fd79d07a9412a` |
| [PROV-JSON](https://www.w3.org/submissions/2013/SUBM-prov-json-20130424/) | 78243 | `a478e4c400538f3555f0901780d9ae52e6a9adea9c8510509bf6a15f95bc04c1` |
| [上游 __init__.py](https://raw.githubusercontent.com/trungdong/prov/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/src/prov/serializers/__init__.py) | 6822 | `4ceaf0c2f6a9b0367c259266c4b958cc8f2ca3ff36645d109936a6ec9065b9e1` |
| [上游 conformance.md](https://raw.githubusercontent.com/trungdong/prov/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/docs/reference/conformance.md) | 18164 | `28c2c048ee6215e078a3979b44c45d5f71956a8e4f72554a520761a954ab3c73` |
| [上游 provjson.md](https://raw.githubusercontent.com/trungdong/prov/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/docs/howto/provjson.md) | 2618 | `12d8f737ef3d54484ce5ace0dc6da7fd702ec5d17dc1d13134c53ef758ad767c` |
| [上游 provjson.py](https://raw.githubusercontent.com/trungdong/prov/f9fe0198f8ec5d06ea2e7aac20a1fcb85f8769cf/src/prov/serializers/provjson.py) | 44920 | `464747e9bd1a48a97cd15ec8c6ceca76d306e09af507d61d710e43c262a863e9` |
| [01_State/01_Objects/w3c-prov-dm.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-dm.yaml) | 1902 | `28a00f3f7dde4b301fc08ff9d36c4a3bd435d18521a7d4c71426895036c7e25e` |
| [01_State/01_Objects/w3c-prov-constraints.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-constraints.yaml) | 1789 | `886a01d2968a6e3f0c4bf38fbf108c3386d8ea86979483c2c2932517da02bcf8` |
| [01_State/01_Objects/w3c-prov-aq.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-aq.yaml) | 1699 | `2d03e819eac35c8de2c081585e77eef7e1792dac5ec21fbada219e15c882a1fb` |
| [01_State/01_Objects/prov-o.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/prov-o.yaml) | 1412 | `b1a253ba30fb07271f477b3f0a4991d004e3a159a3a9ab354b0ea8af6479f2f2` |
| [01_State/01_Objects/w3c-prov-o.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/w3c-prov-o.yaml) | 1842 | `63a0453efe7de2e677f6129501e9e21ba524ee47722aa9a6e717063de4a61a1c` |
| [01_State/01_Objects/python_prov.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/01_Objects/python_prov.yaml) | 14503 | `5d54235ffad005250c2a74e6013728e195f723dd98aeffa2d7dc0c688fa8d62d` |
| [01_State/02_Relations/prov-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/02_Relations/prov-implementations.yaml) | 8525 | `56418677f6352cbb564da5befc5930d4f06238ce3c6a362e9135d195fd77ade7` |
| [01_State/02_Relations/linked-data-and-hypertext.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/02_Relations/linked-data-and-hypertext.yaml) | 61903 | `24eb50722e6599878daeffc431ffbab154b5d39362e8cd49f30d874e64b4b018` |
| [01_State/Inbox/acceptance-events/prov-dm-records-20261029.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/bdeefaa5eeffd2cf152f9096747bbb89324819fe/01_State/Inbox/acceptance-events/prov-dm-records-20261029.yaml) | 4695 | `a91a6350dd4497db433d6b96a0ce14367fbe7fd5f68886d6903a641599b4b434` |
| [冻结证据 packet](https://github.com/InteropAtlas/InteropAtlas/blob/be0d200239f8c7f5330384c5a99ab96fdfae9849/01_State/Inbox/review-packets/prov-dm-records-20261029.yaml) | 52769 | `1982afd24251eec57b8e9b42647dd7bc494c9803b9c97e6846dac4716d9e56d9` |

## 研究边界与停止条件

本次交付止于固定 12 文献、表外 Submission 的身份说明、当前记录/有限证据对照及独立最终逐行复核；适用仓库检查与确切交付版本见交付 PR。仓库 CI、自检与独立复核分别记录，不互相替代，也不把文档检查当上游程序验证。

没有新增或修改 canonical、关系、候选、模型、分类、schema、UI、renderer 或未来维护制度；没有解除 PROV-O hold 或展开依赖闭包/实现候选收集。入口是现有 Research README 与 GitHub 文档；本次两个 Markdown 路径不匹配 Pages 的 push 路径过滤，不宣称新增网站对象页或部署。所有未证实项保留 unknown，不能由条目数推导溯源领域完备。

## 后续交付附记：PROV-N 原始记法文献（2026-10-31）

本附记记录原研究之后的限定增量，不改写上文 `bdeefaa5eeffd2cf152f9096747bbb89324819fe` 历史基线、12 行矩阵、来源指纹或旧九项 smoke 范围。原 PROV-N 行“当时未匹配独立文献对象”保留为历史观察；新增文献记录不能自动填补实现符合性的 unknown。

[PR #625](https://github.com/InteropAtlas/InteropAtlas/pull/625) 交付于固定 M `b77308b5f5aac776d8ac446003ad0b9cd7100076`：原始 W3C Recommendation 2013-04-30 对象 [`w3c_prov_n_20130430`](https://github.com/InteropAtlas/InteropAtlas/blob/b77308b5f5aac776d8ac446003ad0b9cd7100076/01_State/01_Objects/w3c_prov_n_20130430.yaml)，以及 [`w3c_prov_n_20130430_uses_prov_dm`](https://github.com/InteropAtlas/InteropAtlas/blob/b77308b5f5aac776d8ac446003ad0b9cd7100076/01_State/02_Relations/prov-n.yaml) 到既有 [`w3c_prov_dm`](https://github.com/InteropAtlas/InteropAtlas/blob/b77308b5f5aac776d8ac446003ad0b9cd7100076/01_State/01_Objects/w3c-prov-dm.yaml) 的文献级 `uses`。这提供了人可读、紧凑函数式记法这一具体表示选择，不是解析器或验证器已可用的证明。

PROV-N 原文提供正式语法和附加语义规则，不能说“只有语法、没有语义”；语法正确的表达式仍可能不被模型接受。正文产生式/表格为规范性内容，示例和单独汇总的便利语法文件是资料性内容。新关系限定该原始记法文献使用同日 PROV-DM 概念并将其映射到表示，不能推出完整 PROV-CONSTRAINTS 有效性、推理、现实事件/归因真实性或 IA 采用。勘误未审阅或整合，不称最新纠错版。

本次仅回读已交付 canonical 与来源范围，不安装、构建、运行上游或验证任何 PROV-N parser。没有新增 Python 实现边，也未将 `python_prov` 的上游 PROV-N 声明升级为旧九项 smoke 的已验行为。PROV-O 两身份 hold、其余家族项的历史未匹配与实现 unknown 保持；不为补齐 12 项继续新增对象、关系或维护制度。
