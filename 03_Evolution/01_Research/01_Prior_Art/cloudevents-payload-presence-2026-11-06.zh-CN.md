# CloudEvents 载荷存在性取决于实际入口

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed Source Evidence
Document Created At: 2026-11-06T06:41:37+00:00
Document Updated At: 2026-11-06T06:41:37+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_independent_ia_work
  Reviewer: Independent Agent — OpenAI / dot / review_payload_presence_evidence
  GitHub Actor: ff6962757
-->

## 问题与新结论

[已有领域研究](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)指出，两份 SDK 记录没有同输入的缺失 `data` / 显式 `data:null` 运行对照。JavaScript 的旧16项检查名称不能补造这些输入输出，Kotlin 的固定源码则已区分缺失与显式 null。本研究不重复宽泛字段比较，而是追查一个更具体的问题：**同一个 JSON 载荷值，直接构造事件与从 structured 消息接收，是否走同一条保留路径？**

JavaScript 10.0.0 的固定源码给出不同分支：直接构造器按“不是 undefined”保留 `data`；HTTP structured 接收器却先按 truthy 判断映射字段，再无条件从剩余输入删除该字段。因此，在下述条件内，`null`、`false`、`0`、空字符串会在 structured 接收入口被丢弃，后续 structured 输出不再含 `data` 成员；直接构造入口保留这些值。Kotlin 0.2.0 的 JSON decoder/encoder 则以成员存在性、显式 null 和 JSON carrier 分路。

这是有界的**源码推导**，不是本轮 SDK 实测、跨 SDK 交换成功或完整符合性裁决。它说明“库能构造 null 数据”不能替代“接收入口保留 null 数据”，也不能从使用同一事件格式推出值被保留。

## 固定材料与共同输入

- IA 基线为 `6a76609fd995836f96aa6357b094b3d117343783`。原两 SDK 对象、来源访问日期、验证时间、接纳记录、既有关系及能力注释均不改变。
- JavaScript 固定 `cloudevents/sdk-javascript` 10.0.0 / commit `c23895145a2f055e8e90714401fc67252a0edf21`；Kotlin 固定源码0.2.0 / commit `27b718156fd9410a926e08f087ee67c7ba421c1a`。18份选定完整文件逐份核 Git blob、字节数及 SHA256，并核对应官方 tree 条目。完整清单与十组精确 JSON 输入见[机器可读附件](cloudevents-payload-presence-2026-11-06.json)。这不是完整树、发布包、Maven/npm 产物、签名或可复现构建核验。
- 每组固定非空 id/source/type、`specversion="1.0"`、有效显式 time、`datacontenttype="application/json"`；structured 外层 header 固定 `content-type: application/cloudevents+json`。不含扩展、`data_base64`、旧版编码属性或重复键。除 `data` 成员外输入完全一致。
- JavaScript 假定模块初始化及版本读取时为正常原生 JSON 绑定，`CE_USE_BIG_INT` 不等于字符串 `true`；不含 getters、proxies、原型污染或并发宿主改写。已知 JSONParser 赋值行为仍保留为范围限制，未改环境变量或执行该路径。Kotlin 不在解码后修改 carrier 或 content type。
- 比较的是解析输出 JSON 后的 **data 成员是否存在、存在时的 JSON 值**，不是字符串逐字节、字段顺序、全部属性或网络消息相等。JS 构造器会赋值 `this.data`，所以不能用事件对象的 `hasOwnProperty("data")` 代替输出成员观察；undefined 与显式 JSON null 也不能共用一个无标签的 null 结果。

所有例子标记 `UNEXECUTED_SOURCE_DERIVATION`，`actual_result=null`。本轮只读取源码、核对文件身份并检查手写输入/预期的内部一致性；没有安装、导入、构建或运行 SDK、依赖、上游测试，也没有模拟器结果冒充库输出。以下预测以正常宿主及周围解析、时间、构造和验证步骤成功为条件，不保证实际运行成功。

## JavaScript：值在构造之前已被过滤

1. [HTTP.toEvent 的入口及模式选择](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/message/http/index.ts#L88-L153)从 header 识别 structured，再从 body 取得版本。所选完整 JSON 对象字符串以 `{` 开头；[JSONParser](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/parsers.ts#L25-L50)据条件解析它，而不是单独把 `data` 的字符串当 JSON 文本重新解析。
2. [v1structuredParsers](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/message/http/headers.ts#L102-L113)把 `data` 列入已知成员，使用 pass-through parser。随后 [parseStructured](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/message/http/index.ts#L224-L255)取 `property=incoming[key]`，仅在 `if(property)` 为真时赋到 eventObj；不论真假均 `delete incoming[key]`。因此假值不是作为扩展再被补回。
3. 在无 `data_base64` / 旧编码属性的选定输入中，二进制分支不介入；函数把 eventObj 传给 `new CloudEvent(..., false)`。`data` 已被删掉时，[构造器](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/event/cloudevent.ts#L85-L101)只能留下 undefined，不能恢复原值。JSON 的 false、零和空字符串在这一步都不等同“没有数据”，但该入口的判断使输出无法区分它们。
4. [HTTP.structured](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/message/http/index.ts#L51-L62)调用事件的 toString；[toJSON/toString](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/src/event/cloudevent.ts#L143-L155)随后走 JSON.stringify。在这里，undefined 对象属性被省略，显式 null/false/零/空字符串则可保留。两段相接，过滤入口而非 JSON 本身是这些选定值丢失的来源。

入口对照使用同一输入 JSON 解析得到的对象，直接 `new CloudEvent(input, false)`，再调用 HTTP.structured；false 与接收路径内部显式传入的标志一致，仅用于控制变量，不是生产环境关闭验证的建议。此时构造器 `typeof properties.data !== "undefined"` 的判断保留全部选定显式值。构造器末尾是否 validate 不会倒流恢复接收器已经删掉的字段。

固定上游[测试定义](https://github.com/cloudevents/sdk-javascript/blob/c23895145a2f055e8e90714401fc67252a0edf21/test/integration/cloud_event_test.ts#L227-L235)含“can be constructed with null data”，检查直接构造后 `.data===null`，没有经过本研究的 structured 接收入口。本轮未运行此测试；单个测试定义不证明该接收链路，也不据此断言整个上游测试集没有覆盖它。

## Kotlin：缺失、null 与其他 JSON 值有不同 carrier

[公共 JSON 入口](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/JsonEventFormat.kt#L22-L36)分别转入 decoder/encoder。[decoder](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/EventDecoder.kt#L64-L107)在读取上下文后调用 readData，将 carrier 交给 builder，最后调用 STRICT 校验；不是所有入口都无验证。

[readData](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/JsonDataReader.kt#L18-L59)先检查 `data` 与 `data_base64` 的冲突，再检查显式 null。无 data 且无 data_base64 返回 core null；`data:null` 返回内部 NullData；所选 application/json 下，false、0、空字符串、true、1、字符串 "null"、空对象和空数组均沿 JsonData(element)。这里的判断不是 JavaScript truthiness。固定[content-type helper](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/JsonContentType.kt#L9-L13)负责选择 JSON 路线，不是完整 MIME 有效性验证。

[encoder 的 putData](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/EventEncoder.kt#L77-L86)对 core null 不写成员，对 NullData 写 JsonNull，对 JsonData 写原 element。这些是[内部来源 carrier](https://github.com/cloudevents/sdk-kotlin/blob/27b718156fd9410a926e08f087ee67c7ba421c1a/json/src/commonMain/kotlin/io/cloudevents/kotlin/json/EventDataCarrier.kt#L8-L77)，不是新公共构造 API，不宜改述为任意 bytes 或任意类型都无损。此处连接原已知源码路径与本次同输入问题，不把 Kotlin 已有静态结论包装为新实测。

## 十组未执行的条件预测

| 输入 data | JS structured 接收再输出 | JS 直接构造再输出 | Kotlin JSON 解码再编码 |
| --- | --- | --- | --- |
| 成员缺失 | 成员缺失 | 成员缺失 | 成员缺失 |
| null | 成员缺失 | null | null |
| false | 成员缺失 | false | false |
| 0 | 成员缺失 | 0 | 0 |
| 空字符串 | 成员缺失 | 空字符串 | 空字符串 |
| true | true | true | true |
| 1 | 1 | 1 | 1 |
| 字符串 "null" | 字符串 "null" | 字符串 "null" | 字符串 "null" |
| 空对象 | 空对象 | 空对象 | 空对象 |
| 空数组 | 空数组 | 空数组 | 空数组 |

表格每格都是输出 data 的存在/值预测，不是整个事件输出或已完成测试。空对象和空数组在 JavaScript 中为 truthy，不能照 Python 的容器真假规则推断；字符串 "null" 也不等于 JSON null。附件将存在性和字面值分开记录，避免缺失与 null 混淆。

## 对互操作问题的实际意义与剩余证据

若调用方把 null、false、零或空字符串当作有意义的业务载荷，仅知道两端都能处理 CloudEvents JSON 不够。发送端保存值，接收端却在已知字段映射时丢掉它，后续 Kotlin decoder 也不能从已经缺失的成员恢复原值。这里的“后续不能恢复”是对所示转换的信息损失推论，不声称实际运行过 Kotlin→JavaScript→Kotlin 链路，也不推断所有消费者、最新版或其他绑定都有同样行为。

可继续验证的对象现在是附件里具体输入与具体 API 路径，而不是旧16项命名检查、笼统“structured roundtrip”或新增能力标签。若以后获准执行，需分别保存每个入口的实际输出、异常与版本/依赖，并对解析后的成员存在性和值逐项比较，不能把本表直接转为 actual_result。此研究没有授权上游执行，也没有修改维护流程。

原 Kotlin `settings.gradle.kts` 的固定 raw GET proxy tunnel403 保持，未重试、换通道或重建该文件，完整构建输入仍缺失。JavaScript 的旧 npm 安装记录与本次源码不是自动等价。wire specversion=1.0 不证明 patch 版1.0.2符合性，原 JavaScript implements 缺边也没有被本研究补上。本文不覆盖批量、HTTP binary、v0.3、data_base64、任意数值精度、扩展类型、真实网络投递、安全性或全事件字节保真。

研究只增加服务事件领域的一个有来源、有反例和正面对照的入口差异。没有改 Canonical、技术关系、UI、分类、治理、总体设计或维护机制，也不重做或替代全域快照及任何保留中的工作。
