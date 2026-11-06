# aioquic 请求完成与连接关闭：固定源码的责任交接

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-source Analysis
Document Created At: 2026-11-06T12:36:06.566923+00:00
Document Updated At: 2026-11-06T12:36:06.566923+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_transport_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_aioquic_handoff
  GitHub Actor: ff6962757
-->

## 问题与结论

承接[既有 transport 问题](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md#transporthttp3quictls-的图路径是否已经证明一个可用且安全的连接)：一个请求从 HEADERS/DATA 到完成或失败，哪些责任属于 HTTP/3 核心、QUIC 核心、asyncio 适配层和应用调用方？

固定 aioquic 1.7.0 源码支持三个不同结论：

1. HTTP/3 核心把请求写入 QUIC 流，并从 QUIC 事件生成 HTTP 事件。实际发包、逐数据报目的地址、定时器重设和事件排空由集成层承担；固定 asyncio 适配层已有这些调用，不应笼统写成“库没有驱动”。
2. 上游示例 `HttpClient` 已在响应的终止 HTTP 事件上完成请求 future，也已在 `ConnectionTerminated` 上让未完成请求以 `ConnectionError` 结束并清理记录。该行为属于示例应用，不是 `H3Connection` 自动提供的请求管理。
3. 连接关闭与单流重置须分别观察。所选普通响应流 `StreamReset` 在 H3 内部有处理，但不返回完成/失败的 H3 事件；示例没有对应的逐请求重置分支。若没有后续连接终止、终止 HTTP 事件或外部处理，所选调用路径不会仅因该 reset 结束请求 future。这是有条件的静态控制流判断，**不是已复现的挂起、漏洞或整个库不符合性的裁决**。

本研究仅读取固定文件并核对指纹，所有观察配方均 **UNEXECUTED**。没有安装、导入、构建、运行上游代码或测试，没有打开网络连接、握手、使用凭证或更改信任配置。IA 自身文档检查与这些未执行的上游配方分开。

## 固定输入与新增价值

- IA 基线：`2c944c7226fabf37be109b45deca7c139b3f520a`。既有 [`aioquic` 对象](https://github.com/InteropAtlas/InteropAtlas/blob/2c944c7226fabf37be109b45deca7c139b3f520a/01_State/01_Objects/aioquic.yaml)、[两条有界 implements](https://github.com/InteropAtlas/InteropAtlas/blob/2c944c7226fabf37be109b45deca7c139b3f520a/01_State/02_Relations/p0-http-quic-relations.yaml)及[接纳回执](https://github.com/InteropAtlas/InteropAtlas/blob/2c944c7226fabf37be109b45deca7c139b3f520a/01_State/Inbox/review-packets/aioquic-implementation-20261024.yaml)均保持不变。
- 上游：`aiortc/aioquic`，历史固定版本 1.7.0、提交 `8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0`。本次重读版本文件及选定源码，不重新认证 tag、PyPI、发行包、签名或最新版本。
- [机器可读记录](aioquic-request-closure-handoff-2026-11-06.json)保存 13 份选定完整文件的字节数、Git blob、SHA256、行范围与配方状态。文件完整获取不等于每行已经语义审计；本文只分析引用路径，不复制第三方源码进仓库。
- 既有记录已说明 Sans-I/O、逐目的地址发送、GOAWAY 与 TLS 配置边界，也已读取请求测试定义。本次新增的是从这些片段到**请求 future 的完成/失败条件**的跨层追踪，以及测试夹具不能证明什么。不重复接纳实例，不改 Canonical、关系、分类、UI、治理或维护要求。

## 1. 请求完成：排队、事件与应用判断分层

[示例初始化与 GET/POST](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/examples/http3_client.py#L135-L167)在非 `hq-` 配置分支构造 `H3Connection`。本文只取 H3 分支及普通请求，排除 H0、WebSocket、server push、WebTransport、0-RTT、重试与迁移策略。

[_request](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/examples/http3_client.py#L248-L272)取得流 ID，排入 HEADERS；无非空 content 时把 HEADERS 标为 end_stream，否则再排入终止 DATA。随后建立每流事件队列和 future，调用 `transmit()`，最后 `await asyncio.shield(waiter)`。这里的发送 API 返回不能作为远端送达或请求完成记录。

[send_headers / send_data](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/h3/connection.py#L605-L684)最终调用 QUIC 的 `send_stream_data`；[handle_event](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/h3/connection.py#L509-L532)消费 QUIC 事件。[示例事件处理](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/examples/http3_client.py#L202-L246)将 `HeadersReceived` / `DataReceived` 放入相同 stream_id 的队列，**仅当该 HTTP 事件的 `stream_ended` 为真**才 pop 对应 waiter 并 `set_result`。因此只有响应头不一定完成；只有头的终止响应也可能完成，不必等待非空 DATA。future 返回的是事件集合，不是 HTTP 状态成功或业务接纳裁决；代码在此没有按 `:status` 判定成功。

完成一个响应流并不结束整个 QUIC 连接。[未执行的流生命周期测试](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L3361-L3438)的断言把请求流结束后仍存活的 control/QPACK 流分别保留。这是上游测试设计证据，不是本次实测。

## 2. 发包与定时器：适配层已经提供的责任

[transmit 与接收入口](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/asyncio/protocol.py#L109-L159)逐个取出 `(data, addr)` 并调用 `transport.sendto(data, addr)`，随后重新查询 `get_timer()`。deadline 变化会取消旧 timer；新值非 None 时用事件循环 `call_at` 安排回调。直接操作底层 QUIC/H3 的调用方仍须让待发数据进入此发送路径，不能只调用 `send_headers` 就停止驱动。

接收路径的顺序是 `receive_datagram → _process_events → transmit`；[定时器与事件排空](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/asyncio/protocol.py#L194-L235)的顺序是 `handle_timer → _process_events → transmit`，回调时间取已安排时间与当前 loop time 的较大值。`_process_events` 持续读取 `next_event()` 直到 None，再把每项事件交给可重写的 `quic_event_received`。这些是固定实现的正常返回路径，不保证操作系统传输、回调异常或任意自定义子类也正确。

[QUIC timer 选择与处理](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L675-L737)还涉及 ACK、丢包检测、pacing、路径验证及关闭/空闲 deadline。收到数据、发送 API 返回、暂时没有待发数据，均不能独自证明定时器已无后续工作。本文没有审完拥塞控制或丢包恢复算法，也没有测时延。

## 3. 连接关闭：通知到达后，谁让请求失败？

[低层 close](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L488-L510)先保存关闭事件并设置待发送标志，不在此处直接向事件队列发布终止。[关闭帧发送路径](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L563-L588)启动关闭阶段；[_close_begin / _close_end](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L1454-L1472)将 deadline 设置为当前时间加三倍 probe timeout，分别进入 CLOSING 或 DRAINING，最终 `_close_end` 才把事件入队。[收到 CONNECTION_CLOSE](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L1939-L1975)保存远端理由并开始 draining；这条路径也不是一收到关闭帧就立即完成所有请求。

[handle_timer](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/connection.py#L710-L727)在关闭/空闲 deadline 到达时结束连接；没有既有 close event 的空闲情形构造带 `Idle timeout` 理由的 `ConnectionTerminated`。该具体错误码与理由只是固定实现行为，不代替所有关闭原因或规范结论。

通知到达 asyncio 层后，`_process_events` 处理连接等待者、ping 等待者，设置 `_closed`，并调用子类事件方法。**普通 QUIC StreamReader 的 EOF、连接 wait_closed、HTTP 请求 future 是三种不同状态。**默认事件方法可为流 reader 喂 EOF，但 HTTP 示例重写了方法并自行管理请求。

示例的 `ConnectionTerminated` 分支对当前未完成 request waiter 调用 `set_exception(ConnectionError)`，清空事件/等待者字典。这个分支已经存在，不能把“关闭时忘记处理请求”当作本次发现的问题。它也没有将 `error_code / frame_type / reason_phrase` 携入这个通用异常；需要原因的应用须保留原 QUIC 事件。已完成、已从字典移除的请求不在该分支的 pending 集合内。

[asyncio connect 清理](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/asyncio/client.py#L90-L98)按 `protocol.close() → await protocol.wait_closed() → transport.close()` 收尾。若另写集成只请求 close 就停止时钟/事件处理，不能借这段实现宣称已完成相同收尾。上面三倍 probe timeout 也不是实测 wall-clock 上限。

## 4. 单流重置与取消：本次定位的剩余交接

对已有普通客户端请求流，[_receive_stream_reset](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/h3/connection.py#L1521-L1568)取消相关 QPACK 解码、清空该流缓冲并标记接收结束，满足流结束条件时移除 H3 流；`handle_event` 对该分支最终返回空列表。critical stream reset 会触发不同的关闭路径，不在这个普通流判断中。

示例 `quic_event_received` 转交 H3 事件后，只额外处理连接终止；`http_event_received` 的请求完成条件则是终止的 HeadersReceived/DataReceived。两者没有普通 `StreamReset` 到 request waiter 的直接失败映射。所选 reset 路径因此可以完成 H3 内部清理而没有完成示例应用的请求 future；仍须单列后续连接终止、外部 deadline/取消及应用自定义处理。

`asyncio.shield(waiter)` 与请求记录同样需要区分：`_request` 本身没有每请求 timeout 或 `finally` 清理分支。本文仅记录这些源码事实，不测试 task cancellation，不宣称取消永不清理，也不规定新的 IA 调用规范。

[blocked response reset 测试](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L2541-L2596)使用 FakeQuicConnection，断言 reset 返回空 H3 事件、移除流并生成 QPACK cancellation；[未完成请求 reset 测试](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L2598-L2633)对服务端尚未可见的请求断言 H3_REQUEST_INCOMPLETE。两者均未执行，也没有检查示例 `HttpClient` 的 future；不能把内部流断言当作应用等待者验证。

## 5. 上游请求测试能支持多大范围？

- [_make_request](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L147-L220)定义 GET 头和空终止 DATA、同流 200 响应头与 HTML DATA、对应事件序列。[test_request / headers_only](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L1746-L1824)还定义重复请求与仅头的 HEAD 响应。原接纳已读取这些定义，本次沿其调用的夹具继续核边界。
- [h3_client_and_server / h3_transfer](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_h3.py#L42-L83)的正常请求路径使用真实 QuicConnection 配对并排空 QUIC 事件；另有 FakeQuicConnection 分支，不能混称所有 H3 测试都是假核心或都是真实网络。
- [配对夹具](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_connection.py#L192-L249)会加载测试 CA、证书/私钥路径，在内存中安排三轮握手交换，同时把 ACK delay 设为零并替换 pacing。本文没有获取或使用那些证书/私钥，也没有调用夹具。
- [transfer](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/tests/test_connection.py#L300-L309)把字节直接交给给定 receiver，source address 按 sender 角色选定；它迭代返回的 addr，却没有用这个目的地址选择 receiver。此固定二端内存测试不验证多目的地址路由。也没有在该 helper 中驱动 `get_timer/handle_timer`；夹具退出只调用两端 close，不能据此证明完整关闭等待。其他上游测试可能覆盖不同 timer 行为，本文不作全套缺失断言。
- [版本配置](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/quic/configuration.py#L110-L120)缺省列出 v1/v2；本文不把测试定义的 ALPN 配置当作每次协商结果证明。若未来观察要针对既有 RFC9000 关系，应显式固定 v1 并记录实际结果，不把版本选择当作本次已经执行。

## 6. 可检验配方，全部未执行

以下是研究观察设计，既不是通过记录，也不是立即运行、联网或部署授权。具体 Python/依赖、时间模型、版本、端点与信任材料仍需在获准的后续任务中固定。观察者应分别记录调用、QUIC 事件、H3 事件和应用 waiter，不以单个 API 返回代替整链。

| 配方 | 前提与触发 | 要观察的边界 |
| --- | --- | --- |
| R1 普通响应 | 固定 v1/H3；非空响应 DATA 在最后标终止 | HEADERS 与中间 DATA 不提前完成；最终事件与相同 stream_id 的 waiter 对应；业务状态另判 |
| R2 仅头响应 | 有效 HEAD 请求与终止 HEADERS 响应 | 无非空 DATA 也能到终止事件；不能以“收到响应头”无条件判完成 |
| R3 连接关闭 | 保留一个未完成请求；分别请求本地 close 或处理远端关闭 | close/draining deadline、终止事件、request ConnectionError、字典清理逐层区分；不能跳过 timer |
| R4 空闲结束 | 未完成请求且到达核心提供的空闲 deadline | 核心 Idle timeout 事件、适配层排空、示例通用 ConnectionError；不把 idle timeout 当每请求 SLA |
| R5 普通流 reset | 已有请求流，收到 StreamReset；连接继续且没有终止 HTTP 事件 | H3 内部清理与无 H3 完成事件、示例 pending waiter 分开检查；预期是静态推导而非本次结果 |
| R6 目的地址与计时 | 在受控适配器中记录每个返回 addr 与每次 timer 变化 | 每个 datagram 按对应地址转交；重设/取消 timer；现有 transfer 不能充当路由正确性的证据 |
| R7 调用 task 取消 | 应用等待 _request 时取消外层 task | shield 后 waiter、每流记录及后续终止事件的处理分别记录；实际结果未定 |

GOAWAY 仍保留既有边界：[控制流解析](https://github.com/aiortc/aioquic/blob/8c5c6b49ee8c0d19b310c9b9e6a3b6301360dbb0/src/aioquic/h3/connection.py#L1395-L1419)丢弃未使用载荷，不能从本研究的 connection close 推导完整 GOAWAY、重试许可或优雅关闭。TLS 名称/链验证、可信端点、跨实现互通、安全性、性能和部署适用性均未由此补证。HTTP/3→QUIC→TLS 图路径仍只保持既有关系的版本与范围，不生成传递性保证。
