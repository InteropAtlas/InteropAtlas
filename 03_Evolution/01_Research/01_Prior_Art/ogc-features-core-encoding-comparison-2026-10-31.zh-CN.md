# OGC API Features Core 四编码类的有限覆盖比较

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-10-31T05:43:00+00:00
Document Updated At: 2026-10-31T07:09:50+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot / independent_encoding_review
  GitHub Actor: ff6962757
-->

## 问题、结论与范围

本研究问：固定 OGC 17-069r4 §8.1–8.5 明列的 HTML、GeoJSON、GML-SF0、GML-SF2 编码要求类（requirements classes），在 IA 已有对象/关系中有哪些精确映射，pygeoapi 0.24.0 的有限静态源码又能证明到哪里？它服务于后续扩充路径判断，不设新的分类或维护规则。

**结论：GeoJSON 已有精确文献级边；HTML 有相关 Living Standard 对象，但不能直接算成整个 HTML 编码类已覆盖；GML-SF0/SF2 未找到精确 canonical 映射，也未从所查实现切片建立支持证据。后者是限定记录未匹配与 unknown，不是现实缺实现。** 没有发现必须修改既有 canonical 的错误，不为数量新增对象/关系。

记录基线为实际读取的 main `975a717e1fe7fb46e484812fe4bd6800d5bc35aa`（2026-10-31，#614），不是承诺当前 main 永不变化。固定规范为 OGC 17-069r4 / 1.0.1；固定 pygeoapi 0.24.0 源码 commit 为 `f765a64fa65350dc93d9df0a1b38755bef6c31b0`。矩阵与指纹都是该时点、该版本的研究证据，不是活目录或持续覆盖指标。

## 四行矩阵

类 URI 前缀 `R = http://www.opengis.net/spec/ogcapi-features-1/1.0/req/`；每一行均以 Core 为依赖、Web API 为 target。`F` 指 Features `/collections/{collectionId}/items` 与 Feature `/collections/{collectionId}/items/{featureId}`；`D` 指 `/`、`/conformance`、`/collections`、`/collections/{collectionId}`。这些是固定文档定义的资源，不是整个软件的所有 API。四类均可选、可共存，§8.1 还允许其他编码；HTML/GeoJSON 是 where-practical 推荐，不是强制或四选一。不得据此计算全域/地理空间完备率或产品排名。

| requirements class / 精确依赖身份 | 适用资源、媒体类型和条件 | 可选性 / 用途边界 | 既有记录映射（固定 main） | pygeoapi 固定源码静态证据 | 未知 / 不得推断 |
|---|---|---|---|---|---|
| **HTML**，`Rhtml` (§8.2)。依赖表写 HTML5、Schema.org；§3 的 `#HTML5` 实际指 WHATWG HTML Living Standard（viewed 2020-03-16），而 req/content 的 “HTML 5 document” 链接是 `https://www.w3.org/TR/html5/`。Schema.org 参考未给版本，只给 viewed 2020-03-16。保留两种原始指向，不裁决为一个固定 HTML5 版次。 | 每个操作的 200 响应应支持 `text/html`；含 F、D。实际 HTML 响应 body 应含 Response Object schema 所识别全部信息及 `<a>` 链接；Schema.org 注释是 SHOULD。 | 可选；实践可行时推荐。浏览/发现用途可与机器编码互补，不是 GeoJSON 的等价替代。 | [`ogc_api_features_17_069r4`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/ogc_api_features_17_069r4.yaml) 是容纳该类的规范对象；[`html_living_standard`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/html-living-standard.yaml) 是相关文献对象（living，无固定 2020 快照），**不是该 requirements class，也未证明覆盖 HTML5 内容要求**。未找到此 Core→HTML/Schema.org 编码类专门关系。已有 [`pygeoapi_implements_ogc_api_features_core`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/02_Relations/ogc-api-features-implementations.yaml) 不认证可选类。 | `formats.py:35–54`、`api/__init__.py:301–333,477–485,757–793,903–910,988–1015` 有 HTML 选择、header、入口/符合性/集合模板分支；`api/itemtypes.py:665–687,1009–1025` 有 F 模板输出路径；`templates/_base.html:1,50` 是 doctype/body，模板中有 anchors。`util.py:462–517` 允许自定义模板。 | 未运行或验证所有配置响应，不证明所有 schema 信息/链接完整出现在 HTML body、HTML5 合规或 Schema.org 注释完整。静态 `/conf/html` 声明不解决这些问题；当前 living 对象不能替代所有历史/内容身份。 |
| **GeoJSON**，`Rgeojson` (§8.3)；GeoJSON RFC 7946（2016；对象固定 August 2016）。 | F 支持 `application/geo+json`；其余资源 `application/json`。F 对应 FeatureCollection / Feature，单项 id 与请求 featureId 相同，links 外来成员；其他 JSON 响应须满足 Core 指定资源 schema。 | 可选；数据适于 GeoJSON 的预期用途时推荐。并不要求所有 Core 实现使用它。 | 精确对象 [`geojson_rfc7946`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/geojson_rfc7946.yaml)；已有 [`ogc_features_core_1_0_1_uses_geojson_rfc7946`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/02_Relations/geospatial-representation.yaml) 精确限定可选 §8.3。[`geojson_rfc7946_uses_json_rfc7159`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/02_Relations/geospatial-representation.yaml) 是历史 JSON 定义依赖，非编码符合性。[`python_geojson`](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/python_geojson.yaml) 是另一个库先例，不证明 pygeoapi。 | `api/itemtypes.py:555–564,576–650,728,933–940,951–989,1033` 获取 provider 结果、添 links/GeoJSON media-type 链接并 JSON 序列化；`api/__init__.py:793,910,1015` 为发现资源 JSON 路径。`formats.py:35–54`、`api/__init__.py:77–78,477–485` 默认/`f=json` 为 `application/json`，不能把链接里 `application/geo+json` 当实测响应 header；`api.api_headers`、分支/部署亦影响实际输出。 | 未证明 RFC7946 几何/坐标语义、全部 JSON schema、id 一致、完整 content negotiation 或实际 `application/geo+json` 响应。provider 输入格式、静态 `/conf/geojson` 不是输出合规证明；此观察也未被升级成软件缺陷判定。 |
| **GML-SF0**，`Rgmlsf0` (§8.4)；OGC 10-100r3 *GML Simple Features Profile*（2012）Level 0；媒体参数固定 GML 3.2 / profile OGC 2.0 gml-sf0。 | F：`application/gml+xml; version=3.2; profile="http://www.opengis.net/def/profile/ogc/2.0/gml-sf0"`；其余 `application/xml`。§8.4 Table 4：D 为 core:LandingPage / core:ConformsTo / core:Collections（单集合仍为单 entry core:Collections）；F 为 sf:FeatureCollection / 可替代 gml:AbstractFeature 元素。单项 gml:id 匹配 featureId；core root 需 Core XML Schema 验证；存在时间/计数/links 时有 Date、OGC-NumberMatched、OGC-NumberReturned、Link header 要求。 | 可选；2D 线性/平面插值几何，SF0 限制可表格化要素。不由 GeoJSON/HTML 支持自动推出。 | 规范容器对象已有；对 canonical 对象/关系检索 `gmlsf`, `10-100r3`, `Geography Markup`, GML 未找到精确 profile 对象或对应编码关系。没有据此新增对象。 | 所捕获 `formats.py` 和 `plugin.py:75–77` 未列 GML media/formatter（内置 formatter 项为 CSV）；所读核心/要素输出路径未建立该 profile 输出证据。`util.py:759–782` 可配置额外 formatter，`plugin.py:121–133` 可用 dotted-path 加载，故不能用内置清单排除扩展。 | 未检查所有可选 provider/第三方 formatter/部署，更未执行 XML/profile/header 验证。结论为 **固定阅读切片未建立支持证据**，不是“不支持”或实际空白。 |
| **GML-SF2**，`Rgmlsf2` (§8.5)；同一 OGC 10-100r3（2012）Level 2；媒体参数 GML 3.2 / profile OGC 2.0 gml-sf2。 | F：`application/gml+xml; version=3.2; profile="http://www.opengis.net/def/profile/ogc/2.0/gml-sf2"`；其余 `application/xml`。复用 §8.4 内容/root/id/schema 要求但替换 profile 为 Level 2；复用 SF0 headers 要求。 | 可选；非空间属性不再限于原子值；不是以 SF0 命名替代 SF2，也不将放宽属性误写为任意三维/曲面支持。 | 同上：规范对象已有，所查 canonical 未找到精确 SF2/profile 对象或编码关系；不是世界无方案。 | 同一有限静态路径/formatter 可扩展机制；未定位出能独立证明 SF2 profile 输出的代码。没有从 SF0 文献复用条文推导实现已支持 SF2。 | SF2 输出/复杂属性/XML/schema/header 符合性均未建立；unknown 独立保留，不借 SF0 或一般 XML 能力补齐。 |

## 原始记录与证据边界

机器读取沿用已有 canonical YAML，不建立另一套编码类数据模型。上表的 ID 链接固定到记录基线；多文档 YAML 还应按明确 relation ID 选取，不把整文件视为一条边。共同实现主体为 [pygeoapi 对象](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/pygeoapi.yaml)，共同规范主体为 [Core 规范对象](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/ogc_api_features_17_069r4.yaml)。GML 两行没有虚构的对象路径。可将同一固定 GitHub blob URL 换为对应 `raw.githubusercontent.com/InteropAtlas/InteropAtlas/<commit>/<path>` 读取原始 YAML。

canonical 检索限于基线的 `01_State/01_Objects/*.yaml` 和 `01_State/02_Relations/*.yaml`，包括 `gmlsf`、`10-100r3`、`Geography Markup`、完整 GML 词及 Schema.org 身份查询，再核对对象身份与 source/target；未匹配不能外推到世界。HTML现有living对象与§3有文献关联，但不等于要求类内容要求、历史时点及Schema.org依赖都已覆盖。

表内源码路径均相对固定源码树的 [pygeoapi/ 包目录](https://github.com/geopython/pygeoapi/tree/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi)。`api/itemtypes.py:78–91` 的 URI 列表与 `api/__init__.py:875–900` 的配置组合仅是声明；`flask_app.py:275–326` 只确认路由到相关函数，不是运行证据。原文 [OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §3、§8.1–8.5 是依赖身份/编码要求的直接来源；本次未完整审查各依赖规范，不为文档未提供的版本补造版次。

没有安装、导入、执行、构建、部署上游或运行 CITE/测试。只做文本读取、静态路径检查、Git 快照读取和散列验证。没有验证全部配置、第三方插件、实际HTTP响应或跨系统互通；源码注释、provider输入、链接媒体类型及conformance URI都不能替代输出符合性。

## 独立复核

原研究矩阵于 2026-10-31 由独立执行者 `independent_encoding_review` 逐行复核，结论 PASS，无阻断修正；被审矩阵 SHA-256 为 `f76eeec227d15d8c6b95839705db39ca021ad727f3410612ae499d6a1f350644`。此值标识原研究矩阵，不是本出版文档的文件散列。

复核者独立重算下表21个来源的SHA-256，14个上游源码/模板另重算Git blob SHA-1并比对固定commit官方tree，6个canonical文件与固定Git字节一致。复核基于已捕获原文与源码，不宣称重新联网下载或执行上游。其判断明确保留HTML双重引用、可选共存、声明非认证及GML unknown，并同意“无必要canonical补丁”的有限结论，不证明所有既有记录正确。出版排版及链接改动的最终等义复核见本次交付PR记录。

## 来源与捕获指纹

以下URL指向官方原文或固定Git内容；SHA-256是本次保存的响应正文/文件字节，不是HTTP头、元数据序列化或整库归档散列。上游文件另有固定tree匹配的Git blob SHA-1。这里不镜像第三方全文，也不声称可变OGC URL将永远返回同一字节；指纹差异需要另行解释，不能自动判为标准语义改变。

| 来源（点击读取） | SHA-256 | Git blob SHA-1（上游固定tree比对） |
|---|---|---|
| [pygeoapi/api/__init__.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/__init__.py) | `e7c16aa087a760b146dcf7a8cb873a62dd0770f35f3b5a924d4dc3e3177d5582` | `e54b90e6a97fbe81ecd50fac900fae26ed6fece7` |
| [pygeoapi/api/collection.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/collection.py) | `db9fd3e67593d19d9dedb6fa5a15f91760df6bfcb0bf93ceb0f9240836636221` | `2cd8b3ea62d737848f68ad5dd135bc44c25592dd` |
| [pygeoapi/api/itemtypes.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/itemtypes.py) | `aa1a36975801ced3c92700d4b96fe897562e2ca55c041aa694bc760812347ea7` | `65c93aa0a7366b99692c87c3c34509ec2b479a6d` |
| [pygeoapi/flask_app.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/flask_app.py) | `c952b7bef53235ebe00a4120243793695ea84ba4564f880e1c9dd7f23f41a864` | `6a272e4d25bddd09aae61e692da853551f231889` |
| [pygeoapi/formats.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/formats.py) | `4ee1a032a778b1d707b881027a2d3a54d8e1892a2a650b3c36b028632f64c3f6` | `3ad1f481e8f7f1399dd87b8e3f92ea33335be7c1` |
| [pygeoapi/plugin.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/plugin.py) | `e740aec75d613ea32551146f3ecc51b0276095223e20e0f80f344d4cb65e8c44` | `32292c895234a0e8ce10abef11c36cd2fde5172f` |
| [pygeoapi/templates/_base.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/_base.html) | `b91b7d6472fc317cca72969714839c6856483486970f155590a58c75bb45cc3f` | `0aed269e38a1ccc54dbd948c664b6c647f7ea260` |
| [pygeoapi/templates/collections/collection.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/collections/collection.html) | `245c96b34b0b4f0c8c74ff70787f5a0f3bb4947331f25e2a42ebc6caa2dbbf15` | `4cfbfca0b868134cc5debfb9ffa7a19e92865277` |
| [pygeoapi/templates/collections/index.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/collections/index.html) | `f4b97558f27730ad1c46729f7a35b379b8dcb5032c37ed5a37339e844a4b86cc` | `ccd9aa5c7092c116f89907a9cdb66bad3e796c9e` |
| [pygeoapi/templates/collections/items/index.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/collections/items/index.html) | `b9f63e39f71e613f9332ef1ff86f13b0b6a7741ffc50a75c58a74bfb335158be` | `88fa36b51080df17973393c2653d4fe5843de2e4` |
| [pygeoapi/templates/collections/items/item.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/collections/items/item.html) | `5506c736a70f36eecbd544ae731495127ba56206df7e23abac587c8de847a19d` | `705f9057ccecec3d4d2810cad717c835c8f406a1` |
| [pygeoapi/templates/conformance.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/conformance.html) | `aeca705a16fe432d062a6a783ab1f532dbeff1f7356c2a24f59b1c3d8a4d0e07` | `59fe356016d072881408566402b63a7a18ba8740` |
| [pygeoapi/templates/landing_page.html](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/templates/landing_page.html) | `3985a6d640347ab92a8f471d160ac45b0747567aff82b1927dc103c2125b4cc7` | `11e8d7dfb2fd5bcf45c684c56ba938bb9f5c8d17` |
| [pygeoapi/util.py](https://raw.githubusercontent.com/geopython/pygeoapi/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/util.py) | `1962299e1fa4a3e26d2d7951e6f7b9fc5f1f04cd36f5510398c5f3ed04d7eb74` | `b60e187a085763ae3fa1bbd8d5e2e19f5334aca3` |
| [01_State/01_Objects/ogc_api_features_17_069r4.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/ogc_api_features_17_069r4.yaml) | `3f12176f3ee82193c3192297c9f2d635b9796b370c027bebed49e0c9534e19f9` | `—` |
| [01_State/01_Objects/pygeoapi.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/pygeoapi.yaml) | `f760e457ea23e61555be4ed26193662a402c5bf139c6381a35fcccb3f158d8b1` | `—` |
| [01_State/01_Objects/geojson_rfc7946.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/geojson_rfc7946.yaml) | `144288ca04eaf4d83e2f13e8937e295a9afd31210590ad2ba26e816eb788cf23` | `—` |
| [01_State/01_Objects/html-living-standard.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/01_Objects/html-living-standard.yaml) | `0eef20e5f72a1c5aae75b27ec68814b9f70dd33e46badd454765198e1688d04a` | `—` |
| [01_State/02_Relations/geospatial-representation.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/02_Relations/geospatial-representation.yaml) | `0e53347a80e1fa0af93723c80e0f7c29ecf20130e4f288e3848ca378fe145920` | `—` |
| [01_State/02_Relations/ogc-api-features-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/975a717e1fe7fb46e484812fe4bd6800d5bc35aa/01_State/02_Relations/ogc-api-features-implementations.yaml) | `2a93930793601887537bad4d8f459882b37ce8978999eb8c92ad7f6205091e8a` | `—` |
| [ogc-17-069r4.html](https://docs.ogc.org/is/17-069r4/17-069r4.html) | `6a88db75970a327e6dcfbf823d6c56b6edcec0d8347425385b08534546b4c310` | `—` |

## 本次停止条件

四行问题、既有记录绑定、固定静态证据和未知项已完成独立核对。本研究不升级为GML intake、符合性测试、全球分母或持续维护合同；未来如有具体新问题，可沿用现有研究机制另行评估。该文档经研究入口提供GitHub阅读，不宣称自动生成网站对象页。

## 后续交付附记（2026-10-31）

本附记记录原研究之后已经交付的增量，不回写上文 `975a717e1fe7fb46e484812fe4bd6800d5bc35aa` 历史四行、原来源指纹或原验证范围。**记录映射的新增不等于编码实现符合性的未知已经解决。** 下列路径仍是已有 canonical YAML，不另造机器读取模型。

### GML Profile：精确文献映射已补录，编码实现未知保留

[PR #617](https://github.com/InteropAtlas/InteropAtlas/pull/617) 已交付于固定 M `09f55a8fc6a4d4cdf9d2131add523faabb0862f6`：

- 新增规范对象 [`ogc_gml_simple_features_10_100r3`](https://github.com/InteropAtlas/InteropAtlas/blob/09f55a8fc6a4d4cdf9d2131add523faabb0862f6/01_State/01_Objects/ogc_gml_simple_features_10_100r3.yaml)。精确身份为 OGC 10-100r3、2012-04-05 corrigendum；封面 Version 2.0 与外部标识 URI `/spec/gmlsf/2.0.1` 分别保留，不混成另一个版次。
- 新增**一条文献级关系** [`ogc_features_core_1_0_1_uses_gml_simple_features_10_100r3`](https://github.com/InteropAtlas/InteropAtlas/blob/09f55a8fc6a4d4cdf9d2131add523faabb0862f6/01_State/02_Relations/ogc-gml-simple-features.yaml)：仅 Core §8.4/SF0、§8.5/SF2 两个可选类分别使用 Level 0、Level 2；不是所有 Core 部署必须使用 GML。Profile 本身涉及 SF0/SF1/SF2，Core 两个编码类的二维线性几何限制不能反投为整个 Profile 的限制。不拆分虚构 SF0/SF2 对象，不推导传递关系。

所以，原矩阵两行的“固定基线未找到精确 profile 对象/编码关系”是正确历史观察；后续已补**规范对象及一条限定文献边**。pygeoapi 或其他实现是否输出符合 GML-SF0/SF2 的 HTTP 表示，仍未由此建立；不能将这次收录说成实现未知已解决。

交付验证范围：#617 的固定 M 已完成仓库适用验证、独立语义/结构复核、P6 冻结接受链核对以及 Pages/实际页面字节读回；这是记录、仓库与页面交付验证，不是执行上游或 GML 编码认证。该 PR 已公开保留未解决 P1 review thread 与其未知来源说明，本附记不把交付完成改称 bot-clean，不改变任何 review 状态。

### GDAL：有限文件转换先例，不是 Web 编码类实现证明

[PR #618](https://github.com/InteropAtlas/InteropAtlas/pull/618) 已交付于固定 M `40e7d2358b72afe2b820ae4fdc3b934f3d8eed89`，新增完整软件对象 [`gdal`](https://github.com/InteropAtlas/InteropAtlas/blob/40e7d2358b72afe2b820ae4fdc3b934f3d8eed89/01_State/01_Objects/gdal.yaml)，以及既有 geospatial 编辑归属；没有新增技术关系或能力。

记录边界：GDAL 是完整地理空间数据转换软件，固定 v3.10.3 / `ed29baf16d20bccbe331d809e0bafd7afde03360`；不是新造的 GML 转换器、独立驱动对象或 OGC Web 编码类。官方固定文档共同描述 GML 驱动读取可映射为简单要素模型的数据、ogr2ogr 文件转换、GeoJSON writer 的局部路径；这是文献组合并辅以局部源码检查，不是官方原样给出的 GML→GeoJSON 命令实例，也未运行验证。

GeoJSON 写出默认 `RFC7946=NO`（GeoJSON 2008）；需显式 `RFC7946=YES` 才选择该输出模式，仍不代表全部选项组合均已证明符合 RFC 7946。GML 读入的 schema 推断、字段/几何映射、CRS/轴序及输出重投影、精度/日期线处理均有边界，不能保证无损保留源语义或任意 CRS 正确。`DOWNLOAD_SCHEMA` 默认 YES（当前针对看似 WFS response 的文档），所以“本地文件转换”不是保证离线；可禁用下载并本地供给所需资源，但未验证完整无网络行为。不把独立 GMLAS 驱动混入此切片。

交付验证范围：#618 固定 M 已完成适用仓库验证、独立语义/结构复核、完整 P6 冻结接受链核对、Pages 与对象/索引/搜索实际字节读回，并核验完整双语正文可见性。它验证记录接受、渲染与交付，不验证上游转换执行结果或规范符合性。未安装、构建或运行上游命令/测试，未审完整 ogr2ogr 调用链；不声称第三方互通、安全、性能、部署适用性或 IA 采用。

该先例不新增 GDAL→Core/Profile/GeoJSON 技术关系或能力断言，既有 geospatial 成员关系只是编辑导航；不从一般 GML 文件转换推导 GML-SF0/SF2、OGC 10-100r3 或 Core 符合性。上文 HTML/GeoJSON 的既有边界和两 GML 编码类的实现 unknown 均保留。
