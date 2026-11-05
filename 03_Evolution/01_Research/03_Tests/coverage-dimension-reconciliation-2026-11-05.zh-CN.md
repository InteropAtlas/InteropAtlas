# 六个覆盖维度与跨域组合证据的有限对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Evidence Reconciliation
Document Created At: 2026-11-05T11:50:00+00:00
Document Updated At: 2026-11-05T11:54:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / develop_coverage_dimension_reconciliation
  Reviewer: Independent Agent — OpenAI / dot / review_coverage_dimension_reconciliation
  GitHub Actor: ff6962757
-->

## 研究问题与结论

[Issue #276](https://github.com/InteropAtlas/InteropAtlas/issues/276) 已将覆盖问题分为候选发现、正式对象、关系、证据、验证时效性和有界方案替代六个维度。本研究检验一个具体假设：**把已完成的 Syslog、WoT/MQTT 和 HLS 研究接回现有机器载体，是否已经足以回答实际组合和替代问题？**

结论是：现有载体可以连接所选对象的身份、接纳记录、显式关系及其条件，定位支持判断的来源；研究与实验还揭示了图本身没有表达的组合限制。但三个区域都不能仅凭对象齐全、存在共同标准端点或图中可达，就被称为经过验证的完整方案。Syslog 的若干组合问题已有有限执行答案；WoT 的角色与配置边界、HLS 的文本承载与媒体处理边界主要仍由静态证据支持。三者不能合并成一个“实现覆盖”数。

这是一份针对既有材料的假设检验，放在既有 `03_Tests` 研究入口。它为整体底图提供可追溯的解释和下一处证据问题，不是全库盘点、全域快照更新、全局分母、分类方案或新的维护合同。没有新增 Candidate、Canonical、关系、Runtime、页面或 CI gate，也不改变任何既有身份、治理或发布 hold。

## 固定输入与问题范围

仓库读取固定到 [`75978b953182541cf3c5a2b96e749ae547fa474e`](https://github.com/InteropAtlas/InteropAtlas/tree/75978b953182541cf3c5a2b96e749ae547fa474e)。本次重新读取的是该提交中的记录与研究材料；没有再次获取其全部外部来源，没有安装、构建或执行上游，也没有重跑历史实验。下列研究各自原有的 Canonical 基线、上游提交、版次、指纹和执行边界继续有效，不被统一改成本文日期。

| 已有材料 | 本文取用的问题与证据 | 原材料的边界 |
| --- | --- | --- |
| [Syslog 消息组成研究](../01_Prior_Art/syslog-message-composition-coverage-2026-11-05.zh-CN.md) | RFC5424 的 HEADER、STRUCTURED-DATA、可选 MSG，以及读写两端的表示变化 | 消息三部分来自固定文献，不是观测性领域的完整分母；RFC5425 分帧另列 |
| [Syslog 内存实验](../../02_Experiments/02_Pilots/syslog-composition-runtime-2026-11-05.zh-CN.md)及[结果 JSON](../../02_Experiments/03_Evidence/syslog-composition-probe-20261105-result.json) | 固定发行包、依赖、CPython3.12.14 和12个输入下的真实观察 | 明确 UTF-8 解码、无网络、无再序列化测试；不是完整符合性或现代环境普遍兼容性 |
| [WoT/MQTT 跨域研究](../01_Prior_Art/wot-mqtt-crossdomain-evidence-2026-11-05.zh-CN.md) | 描述、表示、可选 MQTT 绑定、客户端和 broker 的不同职责 | 新读取的源码为静态证据；历史15个 core 示例没有重跑，也不是 MQTT 端到端实验 |
| [HLS 文本、媒体与信令研究](../01_Prior_Art/hls-playlist-media-signaling-2026-11-05.zh-CN.md) | 播放列表文本、受限媒体读取和可选 SCTE35-CMD 的衔接 | 固定 RFC8216 与源码；未执行播放列表处理、媒体读取、解码或拼接 |

本文的机器选择为三个研究明确使用的14条关系，以及相应端点和两个 Syslog object-only 库，共19个对象。它是输入选择，不是领域应有对象数或全邻接图。比如 FFmpeg 的 DPX/FFV1 边、端点间已有的 `json_ld_uses_json` 都没有因此被纳入本次14条证据分析；原记录仍可另行读取。

## 六个维度分别能回答什么

下表沿用 #276 原有六维，不增加状态分类。每行中的“未知”指特定问题缺少所需证据，不等于现实中没有技术或没有解决办法。

| 既有维度 | 现有机器载体与读取方式 | 本次可回答的问题 | 仍不能回答的问题或分母 |
| --- | --- | --- | --- |
| 候选发现覆盖（Candidate discovery coverage） | [Candidate YAML](../../../01_State/Inbox/candidates/)、[编辑导航](../../../01_State/Inbox/relations/intake-coverage-20260913.yaml)、[接纳事件](../../../01_State/Inbox/acceptance-events/) | 某个导航引用指向候选还是正式对象，候选如何对应已接纳主体。例如 MQTT/TD 保留 candidate surface，但 accepted 事件指向同 ID 的 Canonical | 这不是待发现技术全集。导航成员与候选身份状态不能给出世界范围的发现率，也不能仅据 `duplicate` 判定已经接纳或尚未接纳 |
| 正式对象覆盖（Canonical object coverage） | [Object YAML](../../../01_State/01_Objects/)；现有 `load_atlas` / `index_objects` 按稳定 ID 读取 | 能定位所选文献、库和软件身份，保留版本及 description 限制；两个 Syslog 库已经收录，尽管没有技术边 | 对象存在不回答协议全部功能、指定部署或端到端链是否成立。19个选中对象没有外部完备分母 |
| 关系覆盖（relation coverage） | [Relation YAML](../../../01_State/02_Relations/)；`normalize_relation` 读取端点、谓词、context/evidence | 能区分 TD 的文献 uses、node-wot 的有限 implements、Paho 客户端路径和 Mosquitto SUBSCRIBE 路径，解释各自条件 | 没有把所有现实关系列成封闭集合。不能以路径连通推导组合成功，也不能把 object-only 自动补成 implements |
| 证据覆盖（evidence coverage） | 对象 `sources`、关系 `evidence/context`、研究固定来源指纹、Syslog 实验清单/结果 | 可以追到具体文献条款、静态路径或实际输入观察；能指出相同命题已有哪一种支持 | URL 数量、文件哈希和字段非空不说明证据充分。完整运行路径、未审上游和未知输入行为不能由来源数量替代 |
| 验证时效性（verification freshness） | `last_verified_at/by`、来源 `accessed`、记录更新时间与研究/实验自身时间 | 能分别报告“记录声明何时核验”和“哪次研究观察了什么”；缺字段保留未知 | 未取得当前外部状态，不知道所有规范、发行物、依赖或配置是否仍适用；本文日期不是全体重新验证日期 |
| 有界方案替代覆盖（solution-space alternative coverage） | 现有 `alternative_to`、其 context 与 `bootstrap_query.alternative_relations` | 系统已能按明确 capability 返回既有替代关系，并保留条件；下文 URI 例子可解释替代边为何不能直接进入 TD 链 | 本次三个组合问题没有建立各自的候选方案全集、共同任务约束及充分比较。共享标准端点既不证明可互换，也不证明没有替代方案 |

[现有 intake audit](../../../02_Runtime/01_Engine/intake_coverage_audit.py) 的成功结果明确限于结构和引用检查；它会用冻结 Git Candidate 和底库复算 accepted 事件，不替代独立语义复核。本文的局部查询仅连接已有记录，不冒充完整 audit 或历史接纳复算。Candidate 的 ID 不必等于它指向的 Canonical ID：`p6-slice0-bcp47-rfc5646` 的 duplicate 状态指向 `bcp47_rfc5646`，却没有对应 accepted 事件，不能把它当成一次接纳。反过来，旧 Canonical 没有对应 Candidate/事件也不自动成为无效对象。

## 从三个组合问题检验六维之间的推断

### Syslog 的执行证据补上了什么

所选正式图只有消息规范使用 RFC3339、TLS 映射使用 Syslog 消息两条文献关系。格式化库与解析库的既有接纳保留 object-only；单看关系边，会漏掉它们已经存在的详细对象证据和后来的实验。

源码研究原先把转义接受、BOM、重复参数、PROCID 的组合行为列为待验证问题。[实验结果](../../02_Experiments/03_Evidence/syslog-composition-probe-20261105-result.json) 已给这些问题增加了有界答案：

- `sd_backslash`、`sd_quote`、`sd_bracket`、`sd_combined` 在所选依赖环境中被接受，但公开参数值仍保留协议转义；不能继续把“这些具体输入能否接受”一概写成未知，也不能把接受扩大为原应用值还原。
- `unicode_bom` 的 MSG 保留 U+FEFF。它说明所用 UTF-8 衔接的实际结果，不说明所有消费者都要求移除 BOM。
- 手写 `duplicate_param` 在文法结果中保留两个参数，公开字典只剩末值；它不是格式化器能够从 Python dict 生成重复键的证据。
- 格式化输入的 `0012` 被公开解析为整数12；`procid_nonnumeric` 的 `worker-12` 仍为字符串。应用若关心原字面形式，就不能把这些结果称为保真。

因此，对“在这组输入下，格式化结果经明确解码后能否解析、是否保持应用值”已有部分肯定和具体不保持的观察。对“任意 RFC5424 消息是否无损往返、可靠送达”仍无充分证据：实验没有测试解析对象再序列化、任意 MSG-ANY 字节、分帧、TLS 或远端接收。RFC5425 的字节长度前缀、逐跳身份和无应用确认限制继续存在，RFC9662 更新也未被消化为当前部署结论。

这一区域说明证据可以进步而技术边数量不变；不应为了让图看起来连通而改变既有 object-only 决定，也不应因未修改 Canonical 的历史核验日期而丢掉后续实验的有限价值。

### WoT 和 MQTT 的连通路径缺少共同运行条件

这里的图跨过工业、语法、语义和元数据等既有导航入口。`node_wot_implements_wot_td_1_1` 加上 TD 的五条 uses，回答了描述处理与表示文献的关联；`node_wot_uses_mqtt_5_0`、Paho 和 Mosquitto 的边则回答特定网络角色和路径。它们并未给出同一次运行。

关键的组合限制不是“缺一个名字”。`MqttBrokerServer` 是暴露 Thing 的绑定路径，所审配置为 `protocolVersion=5`、`selfHost=false`，连接外部 broker；不能按类名把它当作 Mosquitto 的替代 broker。Paho 的边要求显式 MQTTv5 和网络循环；Mosquitto 的所审段从 active MQTT5 session 开始，到 SUBACK 构造并入队结束。前者并不证明已建立该会话，后者也没有证明响应已到达该客户端。

因此，描述可读、MQTT5 路径存在、broker 有 SUBSCRIBE 处理，能够回答不同的局部问题；要回答“某个 TD form 能驱动一次约定的交互”，仍缺实际 form、绑定角色、主题/负载、认证/ACL和两端成功/失败观察的对应。JSON-LD 的语义处理同样不能由 MQTT 传输成功补证。这里引用的是 [WoT 研究](../01_Prior_Art/wot-mqtt-crossdomain-evidence-2026-11-05.zh-CN.md)及其固定来源，没有运行新的设备链。

### HLS 的文本可保留不等于信令被消费

三条所选边分别支持 m3u8 的选定文本读写、FFmpeg 的选定未加密 MPEG-TS 片段读取，以及 RFC8216 对 SCTE35-CMD 的可选文献映射。它们的共同 HLS 端点提供比较入口，但工作职责不相同。

[HLS 研究](../01_Prior_Art/hls-playlist-media-signaling-2026-11-05.zh-CN.md)的新静态观察进一步缩小了问题：m3u8 6.0.0 的特定 DateRange 路径把非空 SCTE35-CMD 作为字符串承载，不解码完整 splice_info_section，也不对齐命令时间；`duration` / `planned_duration` 为数值 `0.0` 时，对应属性在 dumps 的 truthiness 分支被省略。固定 FFmpeg HLS `parse_playlist` 则没有 DATERANGE 分支，未匹配注释走跳过路径。这些是所查源码路径的事实，不能写成已经运行的互通失败，也不评价 FFmpeg 其他组件是否能处理媒体内 SCTE 数据。

对“文本载体是否有这项属性”已有静态答案；对“显式零时长是否保留、信令是否被指定消费者解释并与媒体时间对应”则有明确的验证入口。即使片段 URI 能被读取，也没有建立命令解释、节目时间绑定或拼接成功。RFC8216 的 MAY/SHOULD、必需日期成员和 PROGRAM-DATE-TIME 前提不能在组合中省略。m3u8 与 FFmpeg 因而不能仅凭两条 implements 边被当作可互换的完整 HLS 实现。

### 已有替代关系为何也不能直接填补组合缺口

本次三个区域没有证明完整替代方案，不意味着载体无法表示替代。现有 [`url_standard_alternative_context_uri`](https://github.com/InteropAtlas/InteropAtlas/blob/75978b953182541cf3c5a2b96e749ae547fa474e/01_State/02_Relations/engine-v0.1-bootstrap.yaml) 就在 `resource_identification` 下记录 WHATWG URL 与 RFC3986 的条件性比较。[现有查询函数](../../../02_Runtime/01_Engine/bootstrap_query.py) 只有在 `context.capabilities` 明确匹配时才返回一条 capability-specific alternative；即使返回，也不是充分替代的判决。

把这条边与 [`wot_td_1.1_uses_uri_rfc3986`](https://github.com/InteropAtlas/InteropAtlas/blob/75978b953182541cf3c5a2b96e749ae547fa474e/01_State/02_Relations/protocol-data-representation.yaml) 一起读，能得到一个具体约束：TD1.1 的可选 base 按 RFC3986 解析相对 URI，且不作用于 @context URI 或语义处理中的 Linked Data 图 IRI；而既有 alternative 条件明确排除对要求 RFC3986 的协议/数据格式自动改用 WHATWG 行为。故“底图已有 URL/URI 替代边”不能推出“node-wot 可在这个位置无条件替换解析路线”。本文只对照两条既有条件，没有新做 URL 算法或实现比较。

这也解释六维为何需要分开：发现替代候选、记录其身份、保存比较关系、取得任务相符的证据、核验当前状态和证明指定任务下可替代，是不同问题；前一维的存在不能自动回答后一维。

## 验证时间需要跟着具体主张读取

固定输入里，`wot_td_1.1`、`mqtt_5.0`、`hls_rfc8216` 没有 `last_verified_at/by`。这是字段所能报告的未知，不等于从未有人阅读这些规范。对应关系仍可有自己的核验日期，例如 TD→URI 与 HLS→SCTE35；关系日期不能自动填给整个端点对象。

Syslog 解析库对象的核验时间仍为 `2026-10-31T21:23:43+00:00`，范围是固定源码阅读；11月5日的实验有自己的版本、环境、夹具和结果。本文可以同时报告这两项事实，不能把旧对象改述为已经通过完整运行验证，也不能把实验时间推成整个库的当前状态认证。WoT 研究保留的 pending reviewer 元数据亦不由本文补签或改写。

依据[既有来源追踪规范 §5–7](../../../docs/02_System/01_Knowledge/03_Provenance/provenance-traceability-profile.zh-CN.md)，`accessed`、Git 时间、记录更新时间和实质核验时间各有含义，当前也没有统一过期天数。固定源文件和哈希解决“读了哪份材料”，不会自行回答“是否最新、后续修订是否影响此用途、当前环境是否仍兼容”。这些外部 freshness 问题在本研究中保持未验证，不做批量日期刷新。

## 可复查的局部机器读取

在固定提交的 checkout 根目录、使用其已有 Engine 依赖运行下方一次性查询。它只读并向标准输出打印；不执行上游、改写记录或生成持久快照。集合断言固定本次输入选择，不是以后必须满足的新测试合同。首先核对 HEAD；历史研究自身的基线另见原文。

```python
from pathlib import Path
import json, subprocess, sys, yaml

root = Path('.').resolve()
baseline = '75978b953182541cf3c5a2b96e749ae547fa474e'
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == baseline
sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
from bootstrap_query import load_atlas, index_objects, alternative_relations
from relation_model import normalize_relation
from intake_coverage_audit import records, unique

objects, relations = load_atlas(root)
index = index_objects(objects)
relation_ids = {
    'syslog_rfc5424_uses_rfc3339', 'syslog_tls_rfc5425_uses_syslog_rfc5424',
    'node_wot_implements_wot_td_1_1', 'node_wot_uses_mqtt_5_0',
    'wot_td_1.1_uses_json', 'wot_td_1.1_uses_json_ld',
    'wot_td_1.1_uses_uri_rfc3986', 'wot_td_1.1_uses_json_pointer_rfc6901',
    'wot_td_1.1_uses_bcp47_rfc5646',
    'paho_mqtt_python_implements_mqtt_5.0',
    'eclipse_mosquitto_implements_mqtt5_subscribe_path',
    'python_m3u8_implements_hls_rfc8216', 'ffmpeg_implements_hls_rfc8216',
    'hls_rfc8216_uses_scte35',
}
selected = [r for r in relations if r['id'] in relation_ids]
assert len(selected) == 14 and {r['id'] for r in selected} == relation_ids
descriptors = [normalize_relation(r) for r in selected]
ids = {d.source_id for d in descriptors} | {d.target_id for d in descriptors}
ids |= {'python_rfc5424_logging_handler', 'python_syslog_rfc5424_parser'}
assert len(ids) == 19 and ids <= index.keys()

nav = yaml.safe_load((root / '01_State/Inbox/relations/intake-coverage-20260913.yaml').read_text())
memberships = [m for m in nav['memberships'] if m['ref']['id'] in ids]
candidates = unique(records(root / '01_State/Inbox/candidates'), 'candidate_id')
events = unique(records(root / '01_State/Inbox/acceptance-events'), 'event_id')
selected_events = [e for e in events.values() if e.get('accepted_canonical_id') in ids]
candidate_ids = {e['candidate_id'] for e in selected_events}
candidate_ids |= {m['ref']['id'] for m in memberships if m['ref']['surface'] == 'candidate'}
candidate_ids |= {cid for cid, c in candidates.items()
                  if ids.intersection(c.get('identity_resolution', {}).get('matched_canonical_ids', []))}
comparison = [r for r in alternative_relations(relations, 'resource_identification')
              if r['id'] == 'url_standard_alternative_context_uri']
assert len(comparison) == 1
print(json.dumps({
    'objects': [index[i] for i in sorted(ids)],
    'relations': selected,
    'navigation_memberships': memberships,
    'candidates': [candidates[i] for i in sorted(candidate_ids)],
    'acceptance_events': selected_events,
    'separate_conditional_alternative_example': comparison,
}, ensure_ascii=False, indent=2, default=str))
```

输出保留原始 description、context、sources/evidence 与 provenance。单独的替代例子不计入14条研究关系或19个工作流对象；它只用于检验已有条件如何限制跨边推论。本次实际读取并核对该选择，没有输出或承诺全库覆盖数量。`surface: candidate` 的 MQTT/TD 仍通过原事件连接正式对象，没有改写导航或重复计作两个现实技术；BCP47 的 duplicate-only 候选仍只是一条身份指向，查询不会为它制造接纳事件。

## 可以继续缩小的具体证据问题

以下是由已有材料产生的研究选择，不是新的任务分级、排期、部署批准或持续维护义务。每项都可以先在相应既有材料上澄清问题，不需要新增孤立条目来制造覆盖增长。

| 已知依据 | 有限下一问与所需证据 | 何时能回答该问及仍保留什么未知 |
| --- | --- | --- |
| Syslog 已有明确 UTF-8 衔接和12个输入观察 | 若用途要求保留应用值，先明确哪些 SD 参数、BOM 和 PROCID 表示需要保留，再对照已有结果；若要求重新输出原消息，另需固定再序列化入口、输入子集和逐字节或逐值比较 | 可以对该子集说明保持/变化/失败；仍不推出任意输入、传输分帧、TLS或应用送达。已有12个结果无需被当成尚未执行再做一遍 |
| WoT 已有描述、绑定、客户端和 broker 的不同路径 | 先选定一个 TD form 与同一业务交互，逐项追踪配置如何传入绑定、主题/负载如何对应；实际端到端主张还需要授权的参与实例和两端观察 | 才能评价这个 form 的约定行为，不能借此补证全部 JSON-LD、所有 MQTT 角色、QoS、安全或设备兼容 |
| HLS 已有 DateRange 静态路径和消费者跳过路径 | 先固定一个含显式零 DURATION 的 DateRange 放置位置与输出期待；若继续测试，观察模型值、输出属性及指定消费者的处理。命令解码和节目时间一致性需要另外的输入/观察 | 可把特定静态推导收窄为执行结果；即使文本保留，也不证明完整 SCTE命令、媒体时钟或无缝拼接 |

这些问题把“还需研究什么”落到既有对象之间的实际衔接。外部发现全集、跨域完备分母和三个工作流各自充分的替代方案仍未建立；这不是停止整体底图工作的理由，也不是声称本轮已经完成 #276。

## 输入指纹

下列 SHA256 识别本次读取的仓库材料。上游来源指纹在各原研究/实验中；本文没有把它们冒充新获取或新执行的证据。

| 输入 | SHA256 |
| --- | --- |
| Syslog 消息组成研究 | `cb43b686a25ffc2f7e2272659326f4c53a1e4f9f6dcc79e476c74d16ce0361dc` |
| Syslog 内存实验 | `55601675036fa2f9901f295f7ac333b600f65bfdcca59dd203184ba6ad9396f1` |
| Syslog 结果 JSON | `976d0151c67be6e33810e048061941b0e081cf50f1c4d588a0a5514abf5b024e` |
| WoT/MQTT 跨域研究 | `8a4f9a467fac737d3a6b8d92818add56957b96f1b6b2d2d64abe24eae41d9d03` |
| HLS 文本、媒体与信令研究 | `44ce342d6986b24f00bed8385ccad79d33ce12175185fbc563a630c3e0199ae4` |

本研究只形成这一有限对照及 Research 导航入口。原日期快照、既有接纳和关系条件、候选身份争议及独立授权边界均未改变。
