# 共享 RFC 3339 引用之后：时间字段的跨领域可迁移性

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Static Evidence Comparison
Document Created At: 2026-11-05T15:35:19+00:00
Document Updated At: 2026-11-05T15:36:18+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / finish_wot_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_timestamp_portability_evidence
  GitHub Actor: ff6962757
-->

## 问题与结论

共同引用 RFC 3339，首先建立的是**表示一个 UTC 参考瞬时值的共同基础**，并不把四个字段变成同一命题。CloudEvents `time` 说明事件发生时间或按同一来源规则选择的替代时间；Syslog `TIMESTAMP` 是与发送方系统时间及其可信程度相联系的消息头时间；OASF `created_at` 说明记录创建时间；OGC `datetime` 是请求方施加的时间相交筛选条件。把同一数值放入另一字段，可能保住瞬时值，却新增了来源材料并未证明的字段含义。

因此，一次转换至少有三个可分别回答的问题：目标字段是否允许此表示；解析后是否仍是同一瞬时值；原来的字段含义、偏移知识、表达分辨率和时钟质量有没有被保留。以下是这四个已有外部使用的局部比较，不是新分类法、第五种外部使用、Canonical 新关系或实现符合性结论。

## 固定材料与观察边界

IA 基线为 `InteropAtlas/InteropAtlas@3d19b47a79034e9a26c2fd06b81a41e4e66ebc0d`。读取了 AGENTS、PROJECT_STATE、四个对象、相应 `uses` 关系、RFC 3339/9557 对象，以及既有 Syslog 组成研究。源规范固定为：

- CloudEvents Core 1.0.2，`cloudevents/spec@fc1f6f31f5f011a72183f1bcea20c987cb683ade`，本次从既有 `v1.0.2` 引用解析得到的 commit。
- Syslog RFC 5424，2009 年 3 月原始出版物。
- OGC API Features Part 1 Core corrigendum 1.0.1，17-069r4，2022-05-11 发布的文档。
- OASF 1.0.0 record/schema，沿用既有记录的 `agntcy/oasf@1d2eed1089e39a37678c4a1d9773ff618279d897`。
- RFC 3339 的 2002 年 7 月原文，与更新它的最终 RFC 9557（2024 年 4 月）分开读取；不是 Internet-Draft，也不把勘误或后续更新悄悄并入旧出版物。

[来源及固定选择清单](timestamp-portability-2026-11-05-sources.json)分开保存规范文献、实现源码和历史证据的官方 URL、固定 ref、可得的 Git blob、SHA256、字节数、获取方法与行号/章节锚；第三方完整源文件不在仓库镜像。字节指纹定位此次所读材料，不证明它覆盖全部上游、是最新版或具备发行者签名。没有安装、导入或执行上游实现，没有开启服务或改变时区；pyRFC3339 的40项、CloudEvents JavaScript 的16项及 Syslog 的12项继续是各自固定环境中的历史观察，未重跑或归属为本轮新测试。

本次沿[既有领域导航](https://github.com/InteropAtlas/InteropAtlas/blob/3d19b47a79034e9a26c2fd06b81a41e4e66ebc0d/01_State/Inbox/relations/intake-coverage-20260913.yaml)连接 services、observability、geospatial、agents 的四个外部使用，并以 measurement 入口的 pyRFC3339 作转换对照。它延续[领域证据问题](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)，没有重复[全导航/实现关系审计](../02_Audits/domain-selection-audit-2026-11-05/README.zh-CN.md)，也没有把注释缺失当知识缺口。

按固定基线既有 loader/normalizer，目标为 rfc3339 的直接关系共六条：本次选择四条外部规范 uses（CloudEvents、Syslog、OGC、OASF），另将 RFC9557 extends 与 IA 自用 engine scenario uses 分开。没有做图路径闭包或把这些计数当现实使用全集。精确 ID、原文件和文件指纹见来源清单；主张范围仍以各边的原 context 为准。

## 共同基础不是共同应用合同

RFC 3339 原版以 Gregorian calendar、四位年份和相对于 UTC 的偏移表示瞬时值，不定义区间。日期必须与月份/闰年相符；小时为 00–23、分钟为 00–59，秒受实际闰秒规则约束。可选秒小数由一位或更多数字组成，规范没有给出统一位数上限；偏移为 `Z` 或带符号的小时、分钟，数值语法不等于证明某个真实地点采用该时区。小写 `t/z` 在基本语法中有效，生成端 SHOULD 用大写；应用可进一步限制大写，也可明确选择空格分隔符。不能从一个应用的空格示例推出所有应用都应接受空格。区间、时区名称、时钟校准、业务字段含义均需要各自证据。[RFC 3339 §§1、4.2、5.6–5.7](https://www.rfc-editor.org/rfc/rfc3339.html)

| 外部使用及固定来源 | 字段承载的命题 | 必需性与缺失 | 表示、精度、范围及应用限制 | 不随裸值自动迁移的内容 |
|---|---|---|---|---|
| CloudEvents 1.0.2 `time` | 事件发生的时间；若不能确定，生产者 MAY 用其他时间。同一 `source` 的所有生产者必须一致，均使用真实发生时间或同一确定算法。 | OPTIONAL；不提供该属性是允许的，不能据缺失补造发生时刻。 | 类型为 `Timestamp`，canonical string 编码引用 RFC 3339；可用可转换的原生运行时/协议类型，不要求每一跳都出现文本。核心 `time` 条文没有额外规定统一秒小数上限、禁止闰秒或大写专用配置。 | 是否真实发生时间、替代算法及 `source` 一致性；转换为原生类型后是否仍保存原文偏移/小数位数，需实现证据，不能由“可转字符串”推出字节往返。 |
| RFC 5424 `TIMESTAMP` | Syslog 头部时间，与 originator 的系统时间认识相联系。§6.2.3 要求在不能获取系统时间时使用 NILVALUE；§7.1 可说明对该时间的信任程度。文本没有把所有消息的时间都认证成所描述事件的真实发生时刻。 | 头部该位置存在，但可以是 `-`；无法获取系统时间时 MUST 为 NILVALUE。`-` 不是 RFC 3339 时间戳，也不是某个 UTC 瞬时值。 | 大写 `T/Z`，必须使用 `T`，不得用闰秒；小数秒若出现为 1–6 位，秒为 00–59。其他日期、小时、分钟及偏移限制由 §6 的 ABNF 明列。§6.2.3.1 明示 9 位小数的例子无效。 | `timeQuality`、发送方时区知识、同步状态、误差上界；以及系统时间与应用事件发生时间的关系。 |
| OGC API Features Core 1.0.1 查询 `datetime` | 时间相交筛选谓词，不是声明新事件或记录何时发生。匹配要素的 temporal geometry；多个时间属性采用哪个由服务端决定。 | 服务端 SHALL 支持此参数，但请求的 `required:false`，客户端可以省略。省略参数不等于某个时间未知的记录。 | query string；单个 RFC 3339 §5.6 `date-time`，或 OGC 另行组合的区间。支持两端有界及单侧开放端，`..` 或空端点的半有界形式；端点纳入相交。本文未找到该参数另设小数位上限、禁止闰秒或大写专用条文。固定 ABNF 存在下述命名差异，不能称为已验证的完备形式文法。 | 另一端点、开放/未知端点表达、谓词身份、服务端选取的时间属性、集合上下文。返回匹配本身不证明该时间是所有结果的事件发生时间。无 temporal geometry 的要素也必须匹配。 |
| OASF 1.0.0 `record.created_at` | 记录的创建时间戳；dictionary 的通用说明为对象创建时间，并要求参看具体用法。不能替换成被描述 agent 的所有活动时间。 | `requirement:required`；文字 MUST conform to RFC-3339。没有从被查条文得到 NILVALUE 或缺省时间的许可。 | 映射到字符串 `datetime_t`。文字引用 RFC 3339；正则只检查较弱形状，允许缺少时区后缀、未限制日期/时分秒数值范围，小数位无上限。正则仅列 `T/t`，但说明中有空格示例。两种示例的小数位数不是“仅限 3/6 位”规则。 | 创建行为的主体及依据、记录版本/身份、时间准确性；正则匹配也不能迁移成“完整 RFC 3339 验证通过”或“服务器已接纳”的事实。 |

表格来源：[CloudEvents Type System 与 time，固定 commit](https://github.com/cloudevents/spec/blob/fc1f6f31f5f011a72183f1bcea20c987cb683ade/cloudevents/spec.md#type-system)；[RFC 5424 §§6、6.2.3、7.1](https://www.rfc-editor.org/rfc/rfc5424.html#section-6.2.3)；[OGC §7.15.4](https://docs.ogc.org/is/17-069r4/17-069r4.html#_parameter_datetime)；[OASF record L37–40](https://github.com/agntcy/oasf/blob/1d2eed1089e39a37678c4a1d9773ff618279d897/schema/objects/record.json#L37-L40) 与 [dictionary L385–389、L807–813](https://github.com/agntcy/oasf/blob/1d2eed1089e39a37678c4a1d9773ff618279d897/schema/dictionary.json#L807-L813)。表内“没有额外条文”仅指所查固定字段合同，不声称所有绑定、部署或实现没有附加限制。

## 用同一个值逐步检查迁移

以下均为规范推导示例，不是本次执行结果。

### 同一个数值可以合语法，却不能自动改变用途

`2024-09-10T23:20:50.520789+08:00` 具有合法日历、六位小数、非闰秒、大写 `T` 和明确偏移，满足本次四个字段的共同日期时间表示条件。它与 `2024-09-10T15:20:50.520789+00:00` 表示同一瞬时值。这只是字符串层面的规范推导，不是完整事件、Syslog 消息、HTTP 请求或 OASF 记录的符合性判断，也不是任何运行时的接纳/往返结果；实际请求还受该通道的编码规则约束。

- 写入 CloudEvents `time`，须有“此刻是该事件的发生时间，或合乎该 source 的替代算法”这一应用依据。
- 写入 OASF `created_at`，须有“此刻是该记录创建时间”这一依据。仅仅因为 agent 曾在此刻产生事件，不足以证明记录也在此刻创建。
- 放入 Syslog 头部，需要保留它与 originator 系统时间的关系。仅复制另一领域时间而不说明来源，并不能获得时钟质量或真实发生时间证明。
- 放入 OGC `datetime`，它成为一次筛选条件。返回结果可以是这个瞬时值落在其区间内的要素，也可以是没有 temporal geometry 的要素；不能把响应全部解释成“在这个精确时刻发生的事件”。

这是本次跨记录研究最主要的新增判断：**瞬时值相等不足以证明字段命题相等**。若真实业务确认四种角色恰好对应同一时刻，则可以映射；RFC 3339 引用本身没有完成这项确认。

### 表示精度不是可用任意目标格式保留的，也不是时钟误差

`.1234567` 是基本 RFC 3339 可表达的秒小数，但不符合 Syslog 的最多六位限制。直接复制失败；截断为 `.123456` 或舍入为 `.123457` 会改变所表示的瞬时值。若多出的位全为零，例如 `.1234560`，去掉末尾零可保住数值，但不再保留原始小数位数。这里的“数值保留”与“词法/表达分辨率保留”必须分开。CloudEvents 核心的原生类型转换要求也不单独证明任意精度或原始字符序列被实现保留。

RFC 3339 允许真实已宣布闰秒的相应表示，RFC 5424 明文禁止它。RFC 3339 §5.8 自身给出的 `1990-12-31T23:59:60Z` 不能原样作为 Syslog TIMESTAMP。改写为下一秒不是无损的语法修正，也不能凭标准引用推定某实现采用闰秒平滑。应把不能保留的表示能力报告出来，而不是伪造同一瞬时值。

有效小写 `t/z` 可转大写而保留 RFC 3339 日期时间数值，满足 Syslog 的大小写限制；这仍改变原文。空格选择则必须查应用合同：OASF 的示例不能授权 Syslog 接受空格，后者明确要求 `T`。[RFC 3339 §§5.6–5.7](https://www.rfc-editor.org/rfc/rfc3339.html#section-5.6)、[RFC 5424 §6.2.3](https://www.rfc-editor.org/rfc/rfc5424.html#section-6.2.3)

### 裸时间戳不携带 Syslog 的全部时间质量知识

RFC 5424 §7 把这些 SD-ID 定为 OPTIONAL；`timeQuality` 可以存在，也可以缺失，其所有参数也 OPTIONAL。§7.1 建议在未可靠同步或不知道时区信息是否正确时写它，不是要求每条消息都有。

- `tzKnown=1` 表示 originator 知道自己的时区；即使选择输出 UTC，仍必须使用 1。信息有疑问则为 0。它不是“文本包含非零偏移”的同义词。
- `isSynced=1` 表示同步到可靠外部时间源；未同步则为 0。RFC 3339 解析成功、出现 `Z` 或小数位很多，都不能推出 1。
- `syncAccuracy` 是发送方认为两次同步之间其时钟最多可能偏差的微秒整数，不是秒小数位数。`isSynced=0` 时 MUST NOT 给出；`isSynced=1` 而未给出时，规范允许 collector/relay 假定时间足够准确可视作正确，但未提供具体数值界限。只有确实知道外部时间源可靠性时才可给出该参数。

因此，从带 timeQuality 的 Syslog 消息只取 TIMESTAMP 写入另一个普通时间字段，会丢掉这些显式质量断言。反过来，只有一个合法 RFC 3339 数值，也不能填造这些参数。即便保留该结构，得到的仍是发送方对其系统时间的说明，不是独立测量或认证结果。[RFC 5424 §§7–7.1.3](https://www.rfc-editor.org/rfc/rfc5424.html#section-7.1)

### 单点、区间、缺失与未知不是同一种“空”

OGC 的 `start/end` 保留两个端点，且时间相交包括边界；取其中一个端点写入 `time`、`TIMESTAMP` 或 `created_at`，只留下一个瞬时值，丢掉整个筛选区间。`start/..`、`start/` 及镜像的开放起点在查询上由 OGC 定义；不是 RFC 3339 本身的语法。该原文说明查询中未知端点与无界端点效果相同，但这不使其他领域的未知发生时间、缺失字段或 Syslog NILVALUE 获得同样含义。也不能从单侧开放形式推导任意 ISO 8601 区间均受支持。

此外，OGC §7.11 对要素本身时间属性仅为 SHOULD，允许其他格式或时间参考系；`datetime` 的 RFC 3339 要求不能自动证明所有被查询属性都原生使用相同表示。[OGC §§7.11、7.15.4](https://docs.ogc.org/is/17-069r4/17-069r4.html#_coordinate_reference_systems)

## `Z`、`+00:00`、`-00:00`：保住瞬时值仍可能改变偏移知识

| 阅读层次 | `Z` | `+00:00` | `-00:00` |
|---|---|---|---|
| RFC 3339 原版（2002）§4.3 | 与 +00:00 一样，隐含 UTC 是首选参考点。 | UTC 是首选参考点。 | UTC 时间已知，但本地偏移未知；不是“UTC 瞬时值未知”。 |
| RFC 3339 经最终 RFC 9557（2024）§2.2–2.3 更新后 | 与 -00:00 同义，UTC 时间已知但本地偏移未知；不再隐含 UTC 是首选参考点。 | 语义不变，仍隐含 UTC 是首选参考点。 | 未被正式弃用；该更新建议现在用 Z 表达此意。 |

在两种阅读中，这三种零偏移形式都可以给出已知的 UTC 瞬时值，但所表达的本地偏移/参考点知识不完全相同。因此，原版语义下把 `-00:00` 统一成 `Z`，或更新语义下把 `Z` 统一成 `+00:00`，不能声称所有语义信息无损。数值规范化成 UTC 还会丢掉原来 `+08:00` 一类局部偏移表示；偏移又不等于 IANA 时区名或未来夏令时规则。

这里必须保留版本边界：IA 既有多个关系把目标限定为原始 RFC 3339，四个固定来源也没有因本研究而被改写。RFC 9557 是真实生效的 RFC 3339 语义更新，不应被忽略；但仅凭旧对象或一条 uses 关系，不能证明具体生产者、消费者及字段合同已经一致采用更新后的解释。本研究分别报告原版与更新后的语义，不把后来对 `Z` 的解释追溯说成 2002 年原文，也不把某实现的行为推断成整个标准的含义。[RFC 3339 §4.3](https://www.rfc-editor.org/rfc/rfc3339.html#section-4.3)、[RFC 9557 §§2.2–2.3](https://www.rfc-editor.org/rfc/rfc9557.html#section-2.2)

RFC 9557 另有一项**不同的变化**：IXDTF 为日期时间增加可选的时区/其他注释后缀。旧 RFC 3339 字符串可不带后缀进入该格式，不代表旧字段或旧解析器会接受带后缀的字符串。若一个 IXDTF 字符串承载 `[Europe/Paris]` 或 critical 注释，去掉后缀也不能称为所有元数据保留；遇到不识别或矛盾的 critical 信息须拒绝或做其他错误处理，不能默默当普通时间使用。四个外部字段共同引用 RFC 3339，不会自动授权这些后缀。IA 引擎自用时间戳与已有 `rfc9557_extends_rfc3339` 关系均不算第五个外部应用实例。[RFC 9557 §§1.1、3.3–3.4、4.1](https://www.rfc-editor.org/rfc/rfc9557.html#section-4.1)

## 保留来源中的差异，不制造统一合同

**OASF 的文字、正则与示例分工不同。** `record.created_at` 的 MUST 和 required 是字段要求；dictionary 指定 `datetime_t` 及其正则；示例展示三位和六位小数及 T/空格两种分隔。正则后缀整体可选，所以匹配并不证明明确 UTC 偏移；它也会匹配不少数值/日历无效的形状。相反，空格示例未被这个正则接纳。RFC 3339 本身允许应用选择空格，不能把空格一概判为违反 RFC；也不能用示例修补正则、推定整个服务端的验证逻辑或把示例位数升级为精度上限。

**OGC 固定原文有局部文法命名差异。** §7.15.4 `/req/core/fc-time-response` D 在原始 HTML L3891 定义 `interval-bounded`，L3894 的 `interval` 却引用 `interval-closed`。本研究保留原始字节，不替来源改名、不称这一形式文法已经执行验证。两端区间、单侧开放和相交语义的比较依据是同节正文、F 与示例；这个差异不抹除正文事实。本次没有查询或整合该差异的后续勘误状态。

## 实现选择如何改变时间信息

这里比较的不是几个库谁“支持 RFC 3339 更多”，而是同一时间信息沿不同入口经过什么处理。pyRFC3339 2.1.1 是独立比较先例，**没有证据把它写成下列产品的依赖**。版本固定为 pyRFC3339 `cc6ffe260f63c4e37c2789813894516c089e5cb6`、CloudEvents JavaScript 10.0.0 `c23895145a2f055e8e90714401fc67252a0edf21`、CloudEvents Kotlin 源码发布 0.2.0 `27b718156fd9410a926e08f087ee67c7ba421c1a`、pygeoapi 0.24.0 `f765a64fa65350dc93d9df0a1b38755bef6c31b0`，以及既有 Syslog 两库固定版本。下表除明确标为“旧观察”的部分外，均为源码推导，不是本次执行结果。

| 比较入口 | 语法接受与转换路径 | 瞬时值、偏移信息与小数秒 | 字段含义与应用边界 |
|---|---|---|---|
| pyRFC3339 `parse` → `generate` | parser 将末尾 Z/z 换为 +00:00，再委托 `datetime.fromisoformat`；这不是严格 RFC 3339 验证器。generator 默认要求 aware datetime，默认转 UTC，以秒输出；`microseconds=True` 才选微秒。 | 旧 Python 3.12.14 观察中，带 +08:00 的值转 UTC；九位小数变为六位；默认生成又去掉全部小数而不四舍五入。Z、+00:00、-00:00 的三个特定输入再生成都成为 Z。数值结果不能恢复原拼写，也不能据此恢复来源对本地偏移的知识。 | 它转换调用者给定的值，不知道值指发生、创建、接收还是查询时间；无时区输入的解释还受入口选项影响，见下文。[P1][P2][H1] |
| CloudEvents JavaScript 10.0.0 core `time` | 构造器的 `strict` 默认 true，末尾调用 `validate()`；`strict=false` 跳过该调用及若干扩展拒绝分支，不等于全部分支不检查。`time` 先取 truthy 输入字符串，否则用当前 `new Date().toISOString()`。 | 初始对象属性与 JSON 输出不能混同：`toJSON()` 对该属性再次执行 `new Date(time).toISOString()`。因此不能把构造时尚在对象中的原字符串当作 JSON 原样往返证明。此处只确认转换调用，没有本轮偏移/小数秒输出例，也不把旧16项扩大为这类测试。 | 默认补齐时间只证明 SDK 填了值，不证明实际发生时间；版本验证只进入 wire `1.0` 路径，不能据此推出 1.0.2 patch 符合性。[J1][J2][H2] |
| CloudEvents Kotlin 0.2.0 JSON core `time` 与 Timestamp 扩展 | JSON core `time` 必须为字符串或 unset（缺失/null）；`readTimestamp` → `TimestampValue.fromCanonicalString` → `Instant.parse`。编码 core time 调 `Instant.toString`。JSON decoder 构造后调用 STRICT。 | 中间值是 `Instant`，不是用于保留原 offset 拼写的字符串。具体接受集合、闰秒或小数位数往返没有新增执行证据，不能只凭类型名称承诺。Timestamp 扩展编码成字符串，普通 JSON 扩展读取又重建成 `StringValue`，不会按字符串外形自动还原 Timestamp 包装类型。 | core 字段与任意扩展的解释入口不同；“JSON 中都是字符串”不能保证原类型或相同含义。仍限原 v1.0、有效且不与 core 重名的扩展；本轮不重试被拒绝的 settings.gradle.kts，也不声称构建输入齐全。[K1]–[K5] |
| pygeoapi 0.24.0 Features `datetime` 参数 | `get_collection_items` 将请求参数和该集合 `extents` 交给 `validate_datetime`；只有参数非 None 且 extents 含 `temporal` 才进入 dateutil 解析及集合时间范围比较。否则 helper 原样返回。 | 进入检查时，无 tzinfo 的临时比较值被赋 UTC；区间空端会改写为 `..`。helper 返回字符串，而不是统一解析后的 datetime。此行为不是 pyRFC3339 的解析，也不是原值精度/偏移保真证明。 | 字符串被检查/传给 `p.query` 不等于过滤已应用。固定 CSV/GeoJSON query 接收却不向 `_load` 传 `datetime_`，文档矩阵也标不支持。若集合 extents 无 temporal，helper 不做这项解析检查；在这两个 provider 的所查 query 路径也没有应用 datetime 过滤。不是所有 provider 都无效，更不是整次 HTTP 请求一定成功。[G1]–[G4][G6][G7] |
| Syslog 格式化库 1.4.3 与解析库 0.3.2 | handler 从 `record.created` 经本地时区 `datetime.fromtimestamp` 生成时间；选项可转 UTC，再 `isoformat`。parser 的 TIMESTAMP 文法约束形状与1–6位小数，并把匹配片段拼回文本；没有转成 datetime。 | parser 保留匹配到的时间文本，并不因保留字符串就获得日历/闰秒/偏移范围验证或一个已验证瞬时值。旧12项只使用固定整秒时间或 NILVALUE，没有小数秒、非法日期、零偏移知识或时区变化的覆盖。 | handler 选取日志记录的 `created`，不是对任意业务事件的独立测时；parser 从收到的文本提取 timestamp，也不证明其真实性。两库的 object-only 与原组合实验边界保持不变。[S1]–[S3][H3] |

### 不是同一个“时间没丢”问题

1. **能读入，不等于符合目标语法。** pyRFC3339 历史输入包含无偏移、仅日期等非严格 RFC 3339 形状；Syslog parser 则在字符串形状层处理时间，没有日历转换。前者和后者都不能单靠“成功”证明目标格式有效。[P1][H1][S2]
2. **同一瞬时值，不等于相同时间知识。** 旧 pyRFC3339 的三个零偏移输入合并案例足以说明原始词法区别不可恢复；如何解释这些形式的规范语义，应回到相应 RFC 版次，不能由 Python datetime 的相等关系裁决。相反，即使 parser 原样保留某个 offset 文本，也没有证明该 offset 是真实已知的。[H1][S2]
3. **统一成 UTC，也可能先引入了未经业务确认的假设。** 同一旧无偏移输入 `2026-10-22T12:34:56` 配 `parse(utc=True)`，在受控 TZ=UTC0 与 TZ=UTC-8（POSIX 写法，对应 UTC+8）环境分别得到 `12:34:56+00:00` 与 `04:34:56+00:00`；`generate(naive, accept_naive=True)` 在两环境都当 UTC 生成 `12:34:56Z`。这些是原40项中的历史观察，不是本次更改时区或新测试。pygeoapi helper 对无 tzinfo 比较值赋 UTC 又是第三种显式源码选择，不能把三者当通用缺失偏移规则。[P1][P2][G1][H1]
4. **字段有更多小数位，不等于测量更准确。** 旧 pyRFC3339 已展示转换层的微秒截取和默认秒级输出；固定 pygeoapi 响应的 `timeStamp` 则取 `datetime.now(UTC)` 并格式化六位小数。后者是这次响应形成时获取的当前时间，与请求的 `datetime` 条件、要素自己的时间和事件发生时间不是同一来源。本文不把位数、当前时钟或字段名升级为准确度证明。[P2][G5][H1]
5. **字段存在，不等于领域动作发生。** SDK 可以补 time，JSON 可以重建不同类型，API 可以接受并传递 datetime 而选定 provider 不应用过滤。每一步都有局部证据，却没有自动建立跨域业务含义或真实事件的证据。[J1][K4][K5][G1]–[G4][G6][G7]

因此，这些先例支持一个有限的组合结论：语法接受、瞬时值保存、来源偏移知识、小数精度、字段指称与操作效果，需要分别找证据；本次没有验证任意两实现间的互通，也没有提出新的分类、Canonical 技术边或维护义务。

### 历史观察只用于其原范围

- [H1] 是冻结提交 `30d548b6…` 中 Python 3.12.14 的原40项源码/结果。本文实际引用：`parse_fraction_9`、`parse_normalize_utc`、`generate_default` / `generate_local` / `generate_microseconds`、`zero_offset_roundtrip`、两组 host TZ 观察及相关非严格输入；未重跑。
- [H2] 是冻结提交 `640c41f7…` 的 Node v24.19.0 / npm cloudevents 10.0.0 原16项摘要。它明确记录默认 id/time populated，但不提供上述 timestamp 精度/偏移输入输出，不能把 structured/binary round trip 摘要当作任意时间词法往返证据。
- [H3] 是既有 Syslog 原12项结果及实验文档。十项 formatter 输入的 timestamp 为 `2024-01-01T00:00:00+00:00`，两项手写消息使用 NILVALUE `-`。它证明该固定输入的组合结果，不新增时间有效性或时区覆盖。

## 对共同引用能支持的最窄结论

一条 `uses RFC3339` 足以引导读者寻找共同日期时间表示及该字段的专用限制。要说明两个字段之间可无损迁移，还须在给定用途上确认：

1. 源值确实满足日历、偏移及目标字段限制，而不仅匹配形状；转换没有减少必要的数值精度或改变瞬时值。
2. 新字段的角色确实成立，且源属性中的 fallback、区间、缺失等语义没有被偷换。
3. 需要保留的局部偏移、未知偏移语义版本、时区注释、小数位表达、时钟质量及来源依据没有在转换中消失或被补造。
4. 实现是否接受、转换、保存和回传这些内容，有独立于规范引用的具体证据。

这些是对本次四种字段迁移问题的有限分析，不是新增的项目治理、维护门槛、通用模型、自动测试要求或上游执行授权。既有 held PR、身份与谓词决定均不受本稿影响。


## 本次补上的证据与仍未回答的问题

本次补上的不是另一个“支持 RFC3339”的数量，而是可回到既有标准与先例的迁移判断：四个字段指称不同事实；OGC 时间命中不等于结果含有同一时刻；Syslog 的时间质量断言不在裸字符串里；固定实现的原生类型、缺省值和后端选择又会改变实际保留的信息。pygeoapi 的参数入口、provider 接口与响应生成时间现有明确源码衔接，不能继续把它们当作同一层结果。

仍没有某两个部署之间的真实时间字段交换，也没有本轮 SDK 时间输入输出、完整上游测试或全格式符合性结论。要判断具体迁移能否满足用途，下一份所需证据是明确的源字段/目标字段、输入值与必要保留的信息，以及实际调用入口/版本下的输出；若输入角色本来不同，增加解析测试也不能补足业务依据。该判断不启动自动测试或新的维护队列。

本研究只增加 Evolution 研究及其入口，Canonical、Runtime、标准身份、关系语义、原核验日期、页面/显示/视角转换及所有既有 hold 均保持。局部来源差异没有被升级为新的治理决定或全项目阻塞。


[P1]: https://github.com/kurtraschke/pyRFC3339/blob/cc6ffe260f63c4e37c2789813894516c089e5cb6/pyrfc3339/parser.py#L30-L68
[P2]: https://github.com/kurtraschke/pyRFC3339/blob/cc6ffe260f63c4e37c2789813894516c089e5cb6/pyrfc3339/generator.py#L53-L79
[J1]: https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/event/cloudevent.ts#L45-L151
[J2]: https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/event/spec.ts#L13-L29
[K1]: https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/core/src/commonMain/kotlin/io/cloudevents/kotlin/core/CloudEventAttributeValue.kt#L68-L75
[K2]: https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/EventDecoder.kt#L64-L107
[K3]: https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/JsonFieldReader.kt#L23-L40
[K4]: https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/EventEncoder.kt#L28-L74
[K5]: https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/JsonExtensionReader.kt#L19-L89
[G1]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/__init__.py#L1161-L1245
[G2]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/itemtypes.py#L318-L327
[G3]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/provider/csv_.py#L232-L256
[G4]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/provider/geojson.py#L165-L200
[G6]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/itemtypes.py#L556-L563
[G7]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/docs/source/publishing/ogcapi-features.rst#L14-L35
[G5]: https://github.com/geopython/pygeoapi/blob/f765a64fa65350dc93d9df0a1b38755bef6c31b0/pygeoapi/api/itemtypes.py#L657-L658
[S1]: https://github.com/jobec/rfc5424-logging-handler/blob/8426fd9d143accbfccd1db43553729a53b3f08e9/rfc5424logging/handler.py#L366-L380
[S2]: https://github.com/EasyPost/syslog-rfc5424-parser/blob/578bf58922a8cb90c3340f072a307721642cb8ff/syslog_rfc5424_parser/parser.py#L6-L65
[S3]: https://github.com/EasyPost/syslog-rfc5424-parser/blob/578bf58922a8cb90c3340f072a307721642cb8ff/syslog_rfc5424_parser/message.py#L74-L121
[H1]: https://github.com/InteropAtlas/InteropAtlas/blob/30d548b66cb6860cad92cd82ce15edc248b45fc7/01_State/Inbox/review-packets/timestamp-implementation-20261022.yaml#L177-L335
[H2]: https://github.com/InteropAtlas/InteropAtlas/blob/640c41f7d0e2cadff1c9e6f2d7c156a85214b7ab/01_State/Inbox/review-packets/cloudevents-javascript-sdk-20261021.yaml#L171-L196
[H3]: https://github.com/InteropAtlas/InteropAtlas/blob/3d19b47a79034e9a26c2fd06b81a41e4e66ebc0d/03_Evolution/02_Experiments/03_Evidence/syslog-composition-probe-20261105-result.json
