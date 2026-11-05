# Syslog 消息组成与既有读写先例的有限覆盖对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-11-05T04:57:40.804766+00:00
Document Updated At: 2026-11-05T05:00:49.952462+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Agent — OpenAI / dot / review_syslog_composition (independent)
  GitHub Actor: ff6962757
-->

## 问题与结论

IA 已记录 Syslog 消息文献、TLS 传输映射、一个日志格式化库和一个文本解析库。把这些名字连在一起，能否据此得到可靠的消息往返或送达链？**现有证据不足以支持这一结论：格式化返回 bytes，解析接收 str；中间的分帧、字节解码和 BOM 处理没有由这两个已审切片共同建立。解析结果还可能丢失重复参数或 PROCID 的字面形式。** 这些限制帮助定位下一次验证的问题，不表示现实中没有实现，也不判定某个部署一定失败。

本研究只对照 [RFC 5424 原始正文 §6](https://www.rfc-editor.org/rfc/rfc5424.html#section-6) 的三个消息组成部分：`HEADER`、`STRUCTURED-DATA`、可选 `MSG`。依据是原文 `SYSLOG-MSG = HEADER SP STRUCTURED-DATA [SP MSG]`；HEADER 子字段保留在同一行。这是文献给出的局部组成，不是新分类法、能力模型或观测性领域的完整分母，不计算覆盖百分比。[RFC 5425 §4.3](https://www.rfc-editor.org/rfc/rfc5425.html#section-4.3) 的传输分帧另行讨论，不计作第四个消息组成部分。

Canonical 基线固定为 [`7c267fad8db959051a10ef7564715ebf08fd5c51`](https://github.com/InteropAtlas/InteropAtlas/tree/7c267fad8db959051a10ef7564715ebf08fd5c51)。规范使用 RFC 5424 / RFC 5425 的 2009 年 3 月原版及 RFC 3339 的 2002 年 7 月原版，不合并勘误或后续修订。RFC 5425 的 RFC 9662 更新边界继续保留；本文不是当前完整 TLS 安全或部署指南，不推荐原版密码套件。

## 已有机器记录与证据范围

- [`syslog_rfc5424`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/syslog_rfc5424.yaml)：独立于传输的消息格式文献，不是存储格式或完整日志平台。
- [`syslog_tls_rfc5425`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/syslog_tls_rfc5425.yaml)：原版 TLS 映射及其限制。
- [`python_rfc5424_logging_handler`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/python_rfc5424_logging_handler.yaml)：整体 rfc5424-logging-handler 1.4.3 库，源码固定 `8426fd9d143accbfccd1db43553729a53b3f08e9`；已审范围为 `build_msg(LogRecord)` 单向格式化，未执行上游。
- [`python_syslog_rfc5424_parser`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/python_syslog_rfc5424_parser.yaml)：整体 syslog-rfc5424-parser 0.3.2 库，源码固定 `578bf58922a8cb90c3340f072a307721642cb8ff`；已审范围为单条文本 `SyslogMessage.parse(str)`、文法变换和 `as_dict()`，未执行上游。
- [`rfc3339`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/rfc3339.yaml)：时间戳文献，不是时钟准确性或任意 Syslog TIMESTAMP 的验证证明。

固定基线里，以前四个对象为任一端点的显式技术关系只有：

1. [`syslog_rfc5424_uses_rfc3339`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/02_Relations/protocol-data-representation.yaml)：原版消息规范使用受限 RFC 3339 时间戳语法，必须读取该记录的 `context`。
2. [`syslog_tls_rfc5425_uses_syslog_rfc5424`](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/02_Relations/syslog-tls-message.yaml)：原版传输映射纳入 SYSLOG-MSG，并保留逐跳保护及无应用层确认的限制。

两个库已有 observability 编辑导航，但没有 `implements` 技术边；既有接纳有意保留 object-only 范围。本文不将缺边当作缺少知识，不新增或推导两库之间的关系，也不改写其原接纳决定。Trace Context 与 OpenTelemetry 不属于本次三部分问题，不据此判定其覆盖状况。

## 三个消息组成部分的对照

下表规范列来自原文；库列来自固定源码及已接纳对象；最后一列是本研究对证据组合能力的判断，不写回 Canonical。

| RFC 5424 消息组成 | 原版要求与相关边界 | 格式化先例 1.4.3 | 解析先例 0.3.2 | 组合后仍不能据此声称什么 |
|---|---|---|---|---|
| HEADER，§6、§6.2 | PRI、VERSION、TIMESTAMP、HOSTNAME、APP-NAME、PROCID、MSGID。PRI 值为 0..191；时间戳使用受限 RFC 3339：大写 T/Z、必须有 T、无闰秒，小数秒若出现为 1..6 位；无法获取系统时间时用 NILVALUE。头部字符串有 ASCII 与长度约束。 | `build_msg` 从 facility/level 构造 PRI，写版本1，从 `record.created` 构造日期时间；默认本地时区，选项可转 UTC。头部字符经过滤和截长；过滤可能产生空字段，不能将其当严格验证或无损复制。 | 文法匹配字段；PRI 接受 1..3 位数字，但没有把 0..191 作为文法范围；时间戳匹配形状而不验证年月日/时分秒范围。PROCID 全为数字时转成整数。 | 格式化时间与校验收到的时间是不同职责。没有证明所有输入有效、时钟准确、输入文本原样保留或任意头部往返。 |
| STRUCTURED-DATA，§6.3 | 无元素时用 NILVALUE；SD-ID 在同一消息内必须唯一，名称有受限 ASCII 规则。PARAM-VALUE 使用 UTF-8；反斜杠、双引号、右方括号须转义。§6.3.3 允许同一 SD-ELEMENT 中重复 SD-PARAM。 | 值按反斜杠、双引号、右方括号顺序转义并编码；名称经过滤/截长。入参用映射组织，不能由此证明任意原始参数序列保真；既有记录的空名称及 enterprise_id 失败路径限制保留。 | 变换器剥去参数值外层引号，未显式执行 RFC5424 特定反转义；历史 Lark `ESCAPED_STRING` 的全部接受范围未另外核验。`parse` 将参数存入字典，同名参数后值覆盖前值；重复 SD-ID 也未由该路径拒绝。 | 写端的转义不自动等于读端还原；成功产生字典不证明重复参数、词法形式或所有合法 SD 输入保真。不能把未审的依赖行为补成肯定或否定结论。 |
| 可选 MSG，§6.4 | MSG 可以是非 BOM 开头的任意字节，或 BOM 开头的 UTF-8；原文对 UTF-8 最短形式及非法序列有额外规则。可选消息体与传输帧是不同层次。 | `None`/空消息省略 MSG；非空消息默认 UTF-8 加 BOM，`msg_as_utf8=False` 仍编码 UTF-8 但不加 BOM。输出为 bytes，不是接收端的字符流。 | `parse` 接受 str，MSG 规则取剩余文本；所查路径没有输入字节解码、UTF-8/BOM 识别或完整字节合法性验证。 | 无法据此推断任意 MSG-ANY 字节的可逆解码、BOM 策略正确、消息体字节保真或双方真实互通。 |

## 为什么不能直接拼成无损往返

**输入输出类型之间还有工作。** 格式化函数返回整个消息的 bytes，解析入口的已审接口是 str。调用者仍须确定收到的是完整消息还是传输片段、如何按字节边界提取消息、怎样处理允许的消息体编码，以及是否保留 BOM。不能把一次普通 `decode` 设想当作已验证的通用连接器；本文没有新增适配器或执行连接测试。

**字段映射可以保留含义的一部分，却丢失原样表达。** 源码显示，成功解析后数字 PROCID 的 `0012` 会经整数转换表示为 `12`，因此不能保证原字符序列不变。对于成功进入变换路径的同一 SD-ID 下重复 PARAM-NAME，字典赋值只留下后一个值；原版 §6.3.3 允许重复 SD-PARAM，所以“字典里有此字段”不足以证明原参数序列保留。这是源码推导，不是本次运行或跨库测试结果。

**转义与语法接受需要分别验证。** 写端明确增加转义，读端已查源码只去掉外层引号，不能据此声称所有 RFC5424 转义都已还原。未检查历史依赖完整词法行为，也没有执行一组转义输入；因此本文只指出组合证据缺口，不发布未经运行的互通失败测试结果。

这三点是跨记录阅读得到的有限判断。两库的整体身份不变，未审能力不当作不存在；也不把它们称为可互相替代的完整 Syslog 实现。

## 分帧和送达在消息组成之外

RFC 5425 §4.3 定义 `SYSLOG-FRAME = MSG-LEN SP SYSLOG-MSG`，§4.3.1 明确 MSG-LEN 是 SYSLOG-MSG 的**字节数**，不是字符数；TLS record 与 Syslog message 边界不必一一对应。仅能构造或解析 §6 消息文本，不足以证明这个帧层。

固定 handler 的传输代码确实存在，不能写成“库没有传输能力”。构造器初始化传输；默认 UDP localhost:514，选择 TLS 还需要流式 socket。已读源码的 TCP/TLS 传输路径支持两种 framing 分支，默认非透明分帧会替换消息内 LF 并追加 LF，另一分支写字节长度前缀。这里仅确认分支存在及其静态操作，不将选项存在升级为 RFC5425 符合性、TLS 配置正确或部署成功。RFC6587 整体文献、上游网络行为与接收端互通未纳入本次审查。

RFC 5425 原版的保护是逐跳的；经认证的传输对端不一定就是 HEADER 中 HOSTNAME 指称的实体。原版 §6.3 没有应用层确认，连接断开时发送方可能无法知道远端应用收到哪些消息。即使两库未来通过某个有限文本往返测试，也不能据此推出安全身份或送达保证；RFC9662 后续更新及当前配置另需对应证据。

## 用现有机器入口复查

事实源仍是固定提交的 YAML，不另设 Syslog 对象体系、JSON API 或自动维护任务。用同一提交的 `bootstrap_query.load_atlas` / `index_objects` 和 `relation_model.normalize_relation` 读取即可复查：

```python
from pathlib import Path
import sys
root = Path('/path/to/checkout-at-7c267fad').resolve()
sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
from bootstrap_query import load_atlas, index_objects
from relation_model import normalize_relation
objects, relations = load_atlas(root)
index = index_objects(objects)
subjects = {'syslog_rfc5424', 'syslog_tls_rfc5425',
            'python_rfc5424_logging_handler', 'python_syslog_rfc5424_parser'}
selected_objects = [index[key] for key in sorted(subjects | {'rfc3339'})]
selected_relations = [row for row in relations
    if normalize_relation(row).source_id in subjects
    or normalize_relation(row).target_id in subjects]
```

本次实际读取上述五个对象及两条关系全文，保留原始 `context`、来源和限制；没有仅凭标签或对象数判断覆盖。代码片段只是固定研究的读取方法，不成为新 Engine、公共接口合同或 CI 维护要求。先确认 checkout 的 HEAD 为上述完整 SHA，并使用该提交现有 Engine 依赖；该片段本身不自动切换版本。

读取结果证明这组已记录对象和显式边存在；对象的自然语言范围与本次源码对照支持表内判断。没有技术边不等于没有事实或实现，两个 object-only 库也不能被计作已完整实现协议。原有全域日期快照不在本次改写范围。

## 有限后续问题

若以后要评价这两个具体版本能否组成指定用途的链路，应先确定允许的消息输入子集、字节到文本边界、重复参数/PROCID 是否需要字面保真、转义期望和失败行为，再设计明确的测试观察。网络分帧、TLS 和应用接收则需要各自证据。这是从当前记录导出的研究问题，不是已安排测试、部署建议、新维护标准或自动批准上游执行。

现阶段可用结论是：已有单向格式化和文本解析先例，以及文献级时间戳和传输关系；对任意消息的无损组合、严格验证、真实网络互通、当前依赖兼容性与安全/送达保证仍未建立。本文不填造这些 unknown，不解除任何已有身份或操作 hold。

## 来源与字节指纹

2026-11-05 重新读取下列完整固定文件。RFC 文本由官方出版物 URL 取回；GitHub 文件按固定提交读取，并核对 Git blob 身份。下面仅保存指纹和链接，不镜像第三方全文。读取的源码没有被安装、导入、构建或运行；没有发送日志，没有执行上游测试或网络客户端。

| 固定来源 | SHA256 |
|---|---|
| [rfc5424.txt](https://www.rfc-editor.org/rfc/rfc5424.txt) | `24d91f90a05d2536730ada929c296f45ae9cd72226e22b6775ad8c04cae37a53` |
| [rfc5425.txt](https://www.rfc-editor.org/rfc/rfc5425.txt) | `a807ec7024fb200e9cf91590cfe41ac06029fb48bf9ddba088862bc134647639` |
| [rfc3339.txt](https://www.rfc-editor.org/rfc/rfc3339.txt) | `9ab2b8864a85dca73a88f49b0927bc7bc85f596926e4fd1890905777924e700a` |
| [formatter-handler.py](https://github.com/jobec/rfc5424-logging-handler/blob/8426fd9d143accbfccd1db43553729a53b3f08e9/rfc5424logging/handler.py) | `a3809353f5bc2cf738ba5ca70cd4ba29fd3bc7938e5715d7c85621d348f4e449` |
| [parser-requirements.txt](https://github.com/EasyPost/syslog-rfc5424-parser/blob/578bf58922a8cb90c3340f072a307721642cb8ff/requirements.txt) | `6b4ce119efad0ea8231aea5c7f2f2f8d67629f07507cf623793bb0960ed1fcd5` |
| [formatter-transport.py](https://github.com/jobec/rfc5424-logging-handler/blob/8426fd9d143accbfccd1db43553729a53b3f08e9/rfc5424logging/transport.py) | `ae2bea481285b9c04702ebe165e4c939f743321775e0b4b80f05f2f2f1e0454a` |
| [parser-grammar.py](https://github.com/EasyPost/syslog-rfc5424-parser/blob/578bf58922a8cb90c3340f072a307721642cb8ff/syslog_rfc5424_parser/parser.py) | `c3f6cc627b0003114b2e266334b455bac818ed87f48bf46f2183d9b2e9b758fa` |
| [parser-message.py](https://github.com/EasyPost/syslog-rfc5424-parser/blob/578bf58922a8cb90c3340f072a307721642cb8ff/syslog_rfc5424_parser/message.py) | `2750cfaa60dfa9a9e901d6b6af8c85feb42b9be7b8a72d05cf238c5334b19c38` |

Canonical 文件均使用上述基线；本次读取指纹如下，不改变各对象原有 last_verified_at 或接纳时间：

| 基线文件 | SHA256 |
|---|---|
| [01_State/01_Objects/syslog_rfc5424.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/syslog_rfc5424.yaml) | `7223e252d1f7337d943bce79f7c95420a43f653a5a68054c9bd8bad520a0569f` |
| [01_State/01_Objects/syslog_tls_rfc5425.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/syslog_tls_rfc5425.yaml) | `fc7fb64d76b0957ce729692c052b488d897d0fae6fa8f06c2c436284042ee85d` |
| [01_State/01_Objects/python_rfc5424_logging_handler.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/python_rfc5424_logging_handler.yaml) | `e6d9bd2063ad29bc49090965515f0182f16feb985742e7eb7ef9d658491d9362` |
| [01_State/01_Objects/python_syslog_rfc5424_parser.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/python_syslog_rfc5424_parser.yaml) | `84456c69d71467ed785ef193ba041e96753fc5e76556da7f179a276149d5de05` |
| [01_State/01_Objects/rfc3339.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/01_Objects/rfc3339.yaml) | `b9fe7d7b4cf4ea824655b68fb5c7584ff68ad8df64633a436b7c7d4722701000` |
| [01_State/02_Relations/protocol-data-representation.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/02_Relations/protocol-data-representation.yaml) | `480c477ce97168cb6589c62fbca0ed005196c7af8397291ff820b513dc07417f` |
| [01_State/02_Relations/syslog-tls-message.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/7c267fad8db959051a10ef7564715ebf08fd5c51/01_State/02_Relations/syslog-tls-message.yaml) | `d3f09b563e1149595a99a12f08e0aeada1a6ae512b12d0f47253941ae42c3d8b` |

两份关系文件的指纹覆盖完整文件，判断只使用前述精确关系 ID，不将其他关系自动纳入本研究。规范要求、原有记录、本次静态推导与未建立证据分别保留；本文是有限研究，不是 Canonical 接纳或完整协议符合性审查。
