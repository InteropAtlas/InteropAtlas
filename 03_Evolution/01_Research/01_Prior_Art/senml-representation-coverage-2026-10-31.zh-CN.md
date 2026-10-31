# SenML 原版四表示族与流媒体的有限覆盖比较

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-10-31T07:18:00+00:00
Document Updated At: 2026-10-31T07:18:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / publish_senml_coverage_comparison
  Reviewer: Independent Agent — OpenAI / dot / senml_independent_review
  GitHub Actor: ff6962757
-->

## 问题与有限结论

面对简单测量数据，采用有限记录包还是持续记录流、选择哪种表示、已有通用编码库是否足够，是三个不同问题。本研究将 RFC 8428 原文明确列出的四个表示族，与 IA 的精确文献记录、既有技术关系及实现证据分开对照，便于用户和 AI 判断已知与未知，不建立新的分类或维护制度。

**结论：SenML 原始规范对象已经存在；其 JSON 引用有精确 RFC 8259 对象，CBOR 与 XML 只有不同文献身份的相关对象；未匹配 EXI 的精确对象。所查 canonical 没有 SenML 专门实现证据，通用 JSON/CBOR 库及其既有关系不能填补这一 unknown。** 这里的“未匹配”是固定记录快照的查询结果，不是世界上缺少标准或实现，也不是已有对象必须修正的结论。

范围固定为 [RFC 8428，2018 年 8 月原始正文](https://www.rfc-editor.org/rfc/rfc8428.txt) §1、§4.8、§5–8、§12.3.1–12.3.8、§15.1。局部分母只有原版的 **四表示族、八个 SenML/SenSML 媒体类型**；不是当前 IANA 注册全集、设备领域或实现全集，也不计算完备率。RFC 9100 后续更新和勘误内容/处理状态不纳入本次研究，不宣称当前合并修订语义；不以原版替代现行实现的独立核验。

记录基线为 2026-10-31 实际核对的 main [`7b7964e156edeb5012f9fa3cdba84015f4838655`](https://github.com/InteropAtlas/InteropAtlas/tree/7b7964e156edeb5012f9fa3cdba84015f4838655)。以下 canonical 链接全部固定到该提交；研究是时点快照，不是实时目录。

## 先分清流协商与流处理

[§4.8](https://www.rfc-editor.org/rfc/rfc8428.html#section-4.8) 的流模式是可选的；系统或协议采用此模式时必须说明。单条记录接收后即可处理，不必等待整条流完成；使用相对“现在”的时间时，“现在”按该记录在流中发送的时刻解释。

[§12.3](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3) 则要求将 SenML 与 SenSML 作为不同数据格式分别协商。非流格式有包结束语法，许多接收实现等待结束才处理；SenSML 的结束标记可能永不发送，因此接收者不能等它才开始处理记录。**声明或协商某个媒体类型，不等于已经证明实现能逐记录消费；一次普通解析成功也不能代替流处理证据。**

这种区分不是 HTTP/CoAP 可靠传输保证，不等同 JSON Text Sequences/RFC 7464，也不是要求每个实现支持八个媒体类型。四族仍共享 SenML 数据模型，名称、base 字段、单位、时间和值的解释不能只交给通用语法解码器；本研究不是完整符合性审计。

## 四表示族对照

每行第一列把原版两个媒体项分别绑定到注册小节；“现有记录”描述固定 YAML，不将研究推断写成新增技术关系。

| 表示族与原版媒体项 | RFC 8428 引用的精确身份 | 原文中与选择有关的约束 | 固定 canonical 对照 | 实现证据与 unknown |
|---|---|---|---|---|
| JSON，§5；[`application/senml+json`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.1)、[`application/sensml+json`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.2) | RFC 8259，December 2017（§15.1） | 外层数组包含记录对象；仅 UTF-8；Data Value 使用无 padding 的 base64url。接收者须处理 IEEE 双精度范围；指数 `e` 必须小写，尾数/指数长度另有 SHOULD 限制。 | [`senml_rfc8428`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/senml_rfc8428.yaml) 记录该表示；[`json_rfc8259`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/json-rfc8259.yaml) 与被引用的文献身份匹配。未匹配以 SenML 为端点的技术关系。 | [`nlohmann_json`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/nlohmann_json.yaml) 及 [`nlohmann_json_implements_json_rfc8259`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/02_Relations/data-serialization-implementations.yaml) 是有限通用 JSON 先例，不证明 SenML 字段/base 语义或 SenSML 增量处理；SenML 专门支持 unknown。 |
| CBOR，§6；[`application/senml+cbor`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.3)、[`application/sensml+cbor`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.4) | RFC 7049，October 2013（§15.1） | 使用表 4 的整数键，扩展使用字符串键；String Value 与 Data Value 分别为定长文本串/字节串。流记录数组不定长为 SHOULD；非流记录数组定长为 MUST，不能写成对称强制。版本号只允许无符号整数；数值转双精度保真是 SHOULD。 | [`cbor_rfc8949`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/cbor_rfc8949.yaml) 是 RFC 8949，不是原文引用的 RFC 7049。其记录说明 8949 不创建新格式版本，但这不使两个文献身份相同。未匹配 RFC 7049 对象或 SenML 技术关系。 | [`python_cbor2`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/python_cbor2.yaml) 及 [`python_cbor2_implements_cbor_rfc8949`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/02_Relations/data-serialization-implementations.yaml) 限于既有 RFC 8949 通用编解码范围；不能自动证明 RFC 8428 映射、旧文献符合性或流语义；SenML 专门支持 unknown。 |
| XML，§7；[`application/senml+xml`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.5)、[`application/sensml+xml`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.6) | XML 1.0 Fifth Edition，`REC-xml-20081126`（§15.1） | 仅 UTF-8；Data Value 使用无 padding 的 base64url。`sensml` 根包含 `senml` 记录，字段为属性；§7 给出命名空间、类型限制和 Relax NG schema。 | [`xml_1.0_second_edition`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/xml_1.0_second_edition.yaml) 是 `REC-xml-20001006` 第二版，不能算作 2008 第五版的精确文献覆盖。未匹配第五版对象或 SenML 技术关系；共同规范对象仍为 [`senml_rfc8428`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/senml_rfc8428.yaml)。 | 未从所查 canonical 建立 SenML XML 专门实现证据。XML 良构或其他领域的 XML 能力不足以证明该表示，保持 unknown。 |
| EXI，§8；[`application/senml-exi`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.7)、[`application/sensml-exi`](https://www.rfc-editor.org/rfc/rfc8428.html#section-12.3.8) | EXI Format 1.0 Second Edition，`REC-exi-20140211`（§15.1）；§8 另引 XML Schema Part 1: Structures Second Edition，`REC-xmlschema-1-20041028` | strict schema mode 为 SHOULD，但会丢失扩展；需保留扩展时 non-strict 为 MAY。header 必须含 EXI Options 且 `schemaId=a` 指原版 schema。经 HTTP/CoAP 传输时 cookie 为 SHOULD NOT。 | [`senml_rfc8428`](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/senml_rfc8428.yaml) 记录该表示；未匹配 EXI 精确对象或 SenML 技术关系。附加 XSD 引用不是第五个表示族或新增媒体项；本研究不展开依赖闭包。 | 未从所查 canonical 建立 SenML EXI 专门实现证据；不推断现实中无工具或不支持，保持 unknown。 |

## 记录检索与证据层次

机器读取沿用既有 `01_State/01_Objects/*.yaml` 与 `01_State/02_Relations/*.yaml`，不建立第二套四族/八媒体对象。复查时按上述稳定 ID 定位；多文档关系 YAML 必须选择明确的 relation ID，并读取 `source`、`relation`、`target` 与 `context`，不能把整个文件或一个 `implements` 词当完整符合性声明。固定 GitHub blob 链接对应同提交的 raw YAML，读者可直接使用现有机器读取入口。

在固定基线中，检索 `SenML`、`SenSML`、`8428`、`7049`、`REC-xml-20081126`、`REC-exi-20140211` 并核对对象身份字段、官方 URL 和关系端点：相关对象命中集中于既有 SenML 记录；关系中没有 SenML 端点。另分别读取表内六个对象和两条通用实现关系。RFC 7049/XML 第五版/EXI 的未匹配指精确文献对象，不否定文字提及或相关基础技术存在；未标注与真实空白不等同。

规范身份与表示规则来自 RFC 8428 原文；“已有何种对象/关系”来自固定 canonical；“未建立专门实现证据”是上述有限检索和记录阅读的结果。没有安装、执行、构建或测试上游编码库，没有进行设备互通、八媒体收发、性能、安全或完整规范符合性测试；没有重新验证通用库记录中的历史实验。EXI/XML 等依赖的版次身份按 RFC 8428 §15.1 核对，不冒称通读这些依赖规范。

## 来源与文件指纹

下表 SHA-256 标识本次实际读取的完整文件字节。RFC 原文来自官方固定出版物 URL；指纹不是 HTTP 头、网页解析视图或 current registry 散列。canonical 文件同时绑定上述固定 Git 提交；散列不会将历史观察升级为当前状态或实现证明。这里只提供来源链接及指纹，不镜像第三方全文。

| 来源 | SHA-256 |
|---|---|
| [RFC 8428 原始文本](https://www.rfc-editor.org/rfc/rfc8428.txt) | `643195be834507be9e5a8e4c8c506b8c4523159fcdd09b822963971b34faffa9` |
| [01_State/01_Objects/senml_rfc8428.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/senml_rfc8428.yaml) | `a644af23ef763ebde9f8983fd210902d9f8091141b3998b90003756fdc91befe` |
| [01_State/01_Objects/json-rfc8259.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/json-rfc8259.yaml) | `f041691cf772e981f98811709a8f50246023c6d808611d04ecf977f2b8dd1383` |
| [01_State/01_Objects/cbor_rfc8949.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/cbor_rfc8949.yaml) | `b534b36928c3a0715121404fe57c5be49133ebe9247650cf1cf4ce5baacaa7b8` |
| [01_State/01_Objects/xml_1.0_second_edition.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/xml_1.0_second_edition.yaml) | `e950d1f2739f65cc563f9ff5f5555d44913d73a2d7c09f68ea03ee4ae84f2399` |
| [01_State/01_Objects/nlohmann_json.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/nlohmann_json.yaml) | `0f48674b2948ccddabc1db54e318b2af89a3ec16df8218b4a37b721dabd19947` |
| [01_State/01_Objects/python_cbor2.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/01_Objects/python_cbor2.yaml) | `cfab347693a77673b3a84d8ddaa89a9c74e9391cd91521007bf4e873d1cc2169` |
| [01_State/02_Relations/data-serialization-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7b7964e156edeb5012f9fa3cdba84015f4838655/01_State/02_Relations/data-serialization-implementations.yaml) | `e77691f027d70cea6fb926620fcb22215492d3a04b7455db1123801385942ca8` |

## 研究边界与停止条件

本次交付止于四行比较、八媒体的原文定位、固定 canonical 绑定和独立最终逐行复核，具体版本与适用仓库检查见交付 PR。作者自检、自动检查和独立复核分别提供不同证据，不相互冒充。

没有新增 canonical 对象、技术关系、候选、UI、renderer、schema、分类或未来维护合同；也不从上述未匹配项制造后续补库清单。该研究通过既有 Research README 提供 GitHub 阅读，不宣称新增网站对象页或已触发 Pages 部署。未知保留，有限底图不能被表格行数解释为设备领域已经完备。
