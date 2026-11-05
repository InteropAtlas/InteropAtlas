# HTTP 与工具调用的失败信号：来源、表示与消费者判断

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Static Evidence Comparison
Document Created At: 2026-11-05T16:09:31+00:00
Document Updated At: 2026-11-05T16:09:31+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / finish_wot_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_failure_signal_comparison
  GitHub Actor: ff6962757
-->

## 共同问题与有限结论

解析得到了 JSON、HTTP 状态是 2xx、响应含有 result、客户端没有抛异常，这些事实分别回答不同问题，不能单独证明用户的任务已经成功。本研究把 services 的问题详情、transport 的 HTTP 客户端、syntax/semantic 的 JSON 与 URI，以及 agents 的 JSON-RPC/MCP 调用放到同一个消费者判断问题下：**现在看见的信号由谁产生，报告哪一层的结果，还有什么证据才能决定后续处理？**

三处容易误判的连接已有直接来源：RFC9457 要求生成端的正文与 HTTP 状态一致，却没有为接收端分歧规定无条件优先级；MCP 工具错误可放在 JSON-RPC result 内；固定 Python SDK 还能把本地超时或断流变成 McpError。这不是一种通用错误分类、状态映射或重试设计。比较只澄清现有合同和固定实现的责任，不把它们拼成一条已运行的网络链。

IA 固定基线为 `845eafa0a63922680b6cafbf80c71ee20c8b6435`。入口沿[既有领域证据问题](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)，选择已经记录的三条问题详情关系和三条 agent 消息/实现关系，另读 HTTP/HTTPX 对象。关系 ID、原文件、基线指纹及原 context 的固定链接见[来源与选择清单](failure-signal-comparison-2026-11-05-sources.json)。没有做关系传递闭包，也没有把共享 JSON、URI、异常名称或数值当作直接互操作关系；HTTPX 仍是对象级比较先例，不补 implements。

### 把证据保留到足以作出判断

| 看到的信号 | 该信号直接支持什么 | 仍须保留的上下文或补充证据 |
|---|---|---|
| HTTPX json() 返回 Python 值 | 正文按该解析调用取得了一个值。 | 实际状态、媒体类型、对象/成员合同、扩展语义；URI 标识还可能需要文档基址。 |
| HTTPX raise_for_status() 在关联 request 后返回 | 实际状态落在该实现的 2xx 分支。 | 请求方法和具体状态语义、领域效果。202 接受处理不表示已经完成。 |
| Problem Details 的 status/type/instance | 正文报告的原状态、问题类型和发生标识。 | 与实际状态的生成关系、可能的中间路径改写、URI 解析基址；不能靠 detail 文本替代机器合同。 |
| JSON-RPC error 或 result | 对应请求的错误或结果分支；result 的内容由方法定义。 | 调用 ID、具体协议/方法约定和所用传输绑定。该信封不规定统一 HTTP 状态。 |
| MCP result.isError=true | 工具结果报告执行错误，即使它位于 JSON-RPC result 内。 | 哪条包装路径生成它，客户端是否读取标志；不证明无副作用或允许自动重试。 |
| Python McpError 或内部 JSONRPCError | 进入了相应客户端异常或内部消息路径。 | 远端错误、本地超时与本地断流合成路径的来源证据。类型/数值本身不足以识别来源。 |
| 通知没有响应，或请求等待超时 | 前者受无 JSON-RPC 响应合同约束；后者是本地等待条件结束。 | 不能仅据沉默判定业务成功/失败、未执行或可安全重复。 |

矩阵是下文固定来源的综合判断，不是新增字段、消费者实现要求或全库的失败信号全集。下面逐段保留条件、规范强度、源码入口和未执行示例。

## HTTP 问题详情：相同 JSON 不等于相同失败信号

### 范围与结论

本小节以 IA 基线 `845eafa0a63922680b6cafbf80c71ee20c8b6435` 的既有对象与关系为入口，固定 rfc9457 0.4.1（`b7bd8868f714ccc808343331c2dd08c8369c753f`）和 HTTPX 0.28.1（`26d48e0634e6ee9cdc0533996db289ce4b430177`），只做源码及正式 RFC 文本的静态组合研究。它不是实际部署架构、已执行的互通链路或新增关系提案。

**核心判断：** Python 问题字典、JSON 字节、HTTP 状态与媒体类型、问题类型/发生实例的 URI 标识，是相关但不同的合同。rfc9457 的 `marshal()` 只覆盖其中的字典构造；HTTPX 的 `json()` 与 `raise_for_status()` 分别读取内容和实际响应状态，不自动把这些合同合成一个“API 成功/失败”判断。固定源码足以指出责任缺口，不能证明某个框架填补了缺口或某条网络链路能够互通。[HTTP-S01 L32–101；HTTP-S03 L794–832]

这里的新增价值是共同合同及失配归因，而非重新发现旧行为。IA 已有 `python_rfc9457 → problem_details_rfc9457` 的有限实现关系，以及 RFC 9457 对 JSON、URI 的使用关系；这些不需要重建。HTTPX 原有17项可信内存/默认值观察中的返回404与显式 `raise_for_status()` 仍属历史，本次未重跑、未算作新增测试；没有新增 HTTPX `implements` 边，也没有推导 IA 采用或完整 RFC 符合性。

### 生产端、HTTP 表示与消费端分别承担什么

1. **生产问题字典。** `Problem` 保存 `status`、`status_code` 和 `headers`；`marshal()` 返回含 `type`、`title`、`status`、扩展及真值 `detail` 的 Python dict。`headers` 不进入该 dict。`instance` 可作为扩展传入，但这段代码没有为它执行 URI 校验或解析。`uri` 使用 Python `str.format`；`strict=True` 不是完整 RFC 验证，且先格式替换、再按显式 `type_` 的假值情况选择 `about:blank`。因此不能把输出dict、URI格式化或strict开关当作已生成正确HTTP响应的证据。[固定生产源码](https://github.com/NRWLDev/rfc9457/blob/b7bd8868f714ccc808343331c2dd08c8369c753f/src/rfc9457/__init__.py#L32-L101)（HTTP-S01 L32–101）

2. **组成实际响应。** 在本研究覆盖的边界之外，调用方/框架仍须选择响应状态、序列化方式、内容字节和响应头。RFC 9457 §3规定JSON问题详情表示的媒体类型为 `application/problem+json`；RFC 9110 §8.3把媒体类型同时联系到数据格式和接收者的处理方式，不能仅凭可解析JSON判定格式合同相同。RFC 8259 §8.1要求在非封闭生态系统间交换的JSON文本使用UTF-8。[RFC 9457 §3](https://www.rfc-editor.org/rfc/rfc9457.html#section-3)（HTTP-S08 L152–156）；[RFC 9110 §8.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.3)（HTTP-S09 L2928–2962）；[RFC 8259 §8.1](https://www.rfc-editor.org/rfc/rfc8259.html#section-8.1)（HTTP-S10 L483–498）

   固定HTTPX中，若调用者**自行构造** `Response(status_code=..., json=...)`，且 stream is None、json is not None、输入可 JSON 序列化，并未同时选择优先级更高的content/text/html路径，编码辅助函数会生成UTF-8 JSON字节，并给出默认 `application/json`；显式响应头通过 `setdefault` 保留优先权。这只揭示一个本地响应构造API的默认行为，不能把HTTPX当作已核验的服务器框架，或把“传入json参数”等同于已经声明问题详情媒体类型。[HTTP-S03 L515–576；HTTP-S04 L176–183、221–240]

3. **读取内容不等于判断失败。** HTTPX `Response.json()` 直接调用标准库 `json.loads(self.content, **kwargs)`，不在该方法内检查Content-Type、实际状态、body.status、成员类型、问题类型定义或URI。它使用的是 `.content` 字节，不是 `.text`；未读取的流式内容可先触发 `ResponseNotRead`。因此它返回Python值不证明这是问题详情对象，更不证明领域语义有效。RFC 8259允许JSON文本表示一般值，而RFC 9457要求的问题模型是对象。[HTTP-S03 L6、636–650、831–832；HTTP-S10 L246–257；HTTP-S08 L152–156]

4. **显式状态检查不读取问题对象。** 固定 `raise_for_status()` 先要求关联request，再按实际 `status_code` 判断：200–299返回原Response，其他状态走 `HTTPStatusError` 路径；它并非只处理4xx/5xx，也不读取body.status。异常保留原request与response，但不会自动替应用解释问题类型。若调用顺序在此抛出异常且未处理，后续JSON处理不会自然继续；怎样保留或解释错误内容仍是调用方控制流。[HTTP-S03 L732–736、794–829；HTTP-S06 L52–57；HTTP-S07 L258–268]

此外，HTTPX的2xx分支不能充当最终业务完成判据：RFC9110 §15.3.3明确说明202 Accepted仅表示已接受处理、处理尚未完成，后续也不保证最终执行。这里仅补充该状态的规范含义，没有新增异步任务运行案例。[RFC 9110 §15.3.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.3)（HTTP-S09 L6982–6998；HTTP-S03 L805–806；HTTP-S06 L52–57）

### `status` 分歧：生成约束与接收端归因不能混写

RFC 9457 §3.1.2把body.status定义为来源服务器为该次问题生成的HTTP状态，仅作参考；生成者**必须**使其与实际生成的HTTP响应状态相同。这一约束使不理解问题详情的通用HTTP软件仍可正确处理。[RFC 9457 §3.1.2](https://www.rfc-editor.org/rfc/rfc9457.html#section-3.1.2)（HTTP-S08 L292–309）

但接收端看见二者不同，**不能直接断言生成者出错，也不能把任一值无条件提升为所有软件的唯一真值**。同节允许body.status帮助保留被中间件或缓存改写前的状态；§5明确指出发生分歧时二者相对优先级并不清楚，通用HTTP软件通常不认识body.status。已知“来源直接生成且没有后续改写”的情况下，分歧才直接触及上述生成约束；否则需要来源响应、中间路径和保存上下文才能归因。HTTPX按实际状态进行的方法行为是一条具体实现事实，不是在替RFC规定全局冲突解决策略。[RFC 9457 §5](https://www.rfc-editor.org/rfc/rfc9457.html#section-5)（HTTP-S08 L538–545；HTTP-S03 L794–829）

HTTP状态本身仍描述请求结果和响应语义；2xx、4xx、5xx等类别不是从问题字典推导出来的。响应内容的用途还取决于请求方法和响应字段；例如HEAD、1xx、204及304并不能被统一套入“都有JSON错误正文”的模式。[RFC 9110 §15](https://www.rfc-editor.org/rfc/rfc9110.html#section-15)（HTTP-S09 L6789–6813）；[§6.4.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-6.4.1)（HTTP-S09 L2118–2149）

### 责任矩阵：本切片已经连接什么，仍缺什么

| 接合处 | 规范或固定实现已提供的合同 | 尚需明确的责任/证据 | 不能推出的结论 |
| --- | --- | --- | --- |
| 问题构造→Python值 | rfc9457保存成员并构造dict；headers单独保存。[HTTP-S01 L32–101] | 调用方提供符合成员语义、扩展定义和JSON序列化条件的值。 | 得到dict即已得到合法RFC9457/HTTP响应。 |
| Python值→JSON表示 | RFC9457的JSON表示使用 `application/problem+json`；JSON生成及字节编码另有合同。[HTTP-S08 L152–156；HTTP-S10 L483–498、553–556] | 序列化、字节编码、实际Content-Type及协商由选定调用方/框架落实。 | 一切JSON编码器会自动选择问题媒体类型。 |
| body.status→实际HTTP状态 | 生成者须一致；中间件/缓存可能改写接收端状态。[HTTP-S08 L292–309、538–545] | 生成阶段的对应关系；分歧时的来源证据和应用处理策略。 | 接收端有分歧就一定是生产者错误，或body.status覆盖HTTP状态。 |
| 字节→Python值 | HTTPX `json()`只把content传给JSON解析器；未读内容可能先失败。[HTTP-S03 L636–639、831–832] | 完整内容的读取、解析错误处理、对象/成员/扩展语义处理。 | JSON解析成功即问题详情有效、请求成功或失败已被识别。 |
| HTTP状态→Python异常 | 有request时，`raise_for_status()`按实际状态判定；2xx不抛此状态异常。[HTTP-S03 L794–829；HTTP-S06 L52–57] | 是否调用、调用顺序、异常捕获及如何读取保留的response。 | 不抛异常即领域成功，或异常内容自动变成问题详情。 |
| type/instance→URI身份 | 相对引用以文档基URI解析；解析后type为问题类型主标识。[HTTP-S08 L249–277、338–363] | 保留/确定文档基URI，选择遵守该合同的解析步骤。 | 字符串相等即身份相同，或`json()`已经解析URI。 |
| URI身份→取回/安全 | type一般不应被自动解引用；instance可只是不可解引用的发生标识。[HTTP-S08 L257–262、279–290、341–348] | 另行决定取回用途、目标及安全控制；审查错误详情泄露风险。 | 标识合法就可安全取回，或每个问题都必须请求链接。 |

RFC9457消费者还必须忽略类型不符的标准成员，并忽略不认识的扩展；这不同于“所有错误输入一律拒绝”，也不是普通JSON解析器自动实现的行为。`title`和`detail`的人类说明文本不能代替类型标识及扩展合同。[HTTP-S08 L240–255、311–334、365–380]

### 相对 URI：缺少基址就缺少可比较的身份

RFC 9457 §3.1.1/§3.1.5要求 `type` 和 `instance` 中的相对引用按RFC3986 §5解析到文档基URI。解析后的type是问题类型主标识，instance标识本次发生；两者不能互换，也不能把instance当然当成type的基址。缺失type默认 `about:blank`，该类型没有HTTP状态之外的额外语义。[HTTP-S08 L249–277、338–363、508–520]

RFC3986 §5.1按内容嵌入、封装上下文、取回URI及应用默认上下文的顺序讨论基URI来源；若适用取回URI规则，重定向后使用实际取回表示的最后URI。不能不看上下文就把任意请求地址、日志文件路径或其他JSON对象的基址套进来。仅保留解析后的dict而遗漏其来源上下文，会使相对URI失去可稳定解释的依据；这不表示调用 `json()` 会删除HTTPX原Response或其request URL。[HTTP-S11 L1547–1659；HTTP-S03 L595–608、628–639、831–832]

引用解析是形成URI标识；解引用是另一个可能触发取回的动作。RFC9457允许不可解引用的type，且消费者通常不应自动解引用type，向开发者提供信息的工具是其说明的例外。instance也可能只是对客户端不透明的唯一标识。RFC9457 §5提醒审查问题正文与发生详情链接，避免泄露实现细节或用户信息；RFC3986 §7.2指出看似无害的URI取回可能触发有害远端操作。因此本研究没有将“识别/比较type”变成自动网络访问规则，更不把URI语法或可解析性当作安全认证。[HTTP-S08 L257–290、341–348、522–536；HTTP-S11 L2382–2403]

### 未执行示例：可分离的失配信号

以下全部是**未执行的、由固定源码与规范推导的说明**，不是测试结果、真实HTTP消息、生产故障或互通保证。状态方法示例假设已有合法关联request；JSON示例假设正文已读取且是普通、完整的UTF-8 JSON，未配置自定义JSON解析参数。每一行分别描述独立调用的预期，不假设异常后程序仍会继续执行。

| 假设输入/上下文 | 源码或规范导出的结果 | 仍不能得出的结论 |
| --- | --- | --- |
| 实际HTTP200，正文为含数字 `status:400` 的问题形状对象 | `json()`可把该普通JSON解析为dict；`raise_for_status()`按200返回原Response。[HTTP-S03 L794–832；HTTP-S06 L52–57] | 不能把“不抛状态异常”当作问题语义通过；也不能仅凭接收端分歧认定来源生成者违规。 |
| 实际HTTP400，正文含数字 `status:200` | 单独调用 `json()`仍可取得该dict；显式 `raise_for_status()`按400抛 `HTTPStatusError`，body.status不使它改判成功。[HTTP-S03 L794–832] | 不能认为JSON解析成功撤销HTTP错误；分歧来源仍需追踪。 |
| 完全相同的JSON对象字节，一次标记 `application/json`，一次标记 `application/problem+json` | `json()`自身不会因该头部差异改变调用分支；媒体类型合同仍不同，问题表示由RFC9457标识为后者。[HTTP-S03 L831–832；HTTP-S08 L152–156；HTTP-S09 L2930–2936] | 不能用相同解析值证明两种媒体类型语义等价，也不能证明调用方协商正确。 |
| 标记 `application/problem+json`，正文是 `[]` | 这是可解析的JSON数组，但不是RFC9457的对象模型；头部并不把数组转换为对象。[HTTP-S10 L246–257；HTTP-S08 L152–156；HTTP-S03 L831–832] | 不能把媒体类型声明或JSON解析通过当作问题详情验证通过。 |
| 两个已确定的文档基URI分别为 `https://api.example.org/foo/bar/123` 与 `https://api.example.org/widget/456`，正文type均为 `example-problem` | RFC9457自己的例子解析为不同类型URI：`https://api.example.org/foo/bar/example-problem` 与 `https://api.example.org/widget/example-problem`。相对instance有同类差异。[HTTP-S08 L264–277、350–363] | 原始字符串相同不证明同一类型/发生实例；不得据此自动取回任一URI。 |

### 尚未闭合的条件与证据边界

- 没有选定、安装或检查Web服务器框架适配器，因此不知道哪个实际组件将Problem.headers、status与dict组成响应，以及它是否校验或覆盖媒体类型。HTTPX本地Response构造源码不是这项部署证据。
- 没有真实请求、listener、代理、缓存、网络传输、TLS、框架集成或上游测试执行证据；“来源生成状态一致”与“接收状态是否被改写”均未观测。
- 没有完整问题类型注册/业务扩展合同、错误重试/恢复策略或消费者应用代码；不能从这些通用库判定领域操作最终成功与否。
- 没有为具体离线保存、重定向或封装场景选择基URI算法实现，也没有开展URI取回或安全验证。这里只指出其必要上下文及标准边界。
- 正式RFC原始文本与固定Git源码保留字节指纹；没有把草案当作正式RFC，也未整合这些规范全部勘误、后续更新或依赖运行时差异。RFC9457附录A本身明确为非规范性JSON Schema，不能替代正文的成员和语义合同。[HTTP-S08 L651–655]


## JSON-RPC 与 MCP：响应信封成功，不等于工具任务成功

本节沿用既有 `mcp_2025_11_25 → json_rpc_2.0` 的消息层使用关系，以及固定 MCP Python SDK 1.26.0 / `3d9d34552a9ab8988acf8d06e4a705bd799fc32b` 的有限实现证据。JSON-RPC2.0 对 JSON 的明确引用仍是 RFC4627，不升级成 RFC8259，也不经 uses 链推导 MCP 的直接 JSON 版本或批处理支持。问题不是把所有失败归并成一种状态，而是判定观察到的字段究竟报告了哪件事，以及谁仍需解释它。以下规范阅读和源码追踪均为静态；示例为人工构造、未执行的说明性消息，不是网络抓包或 SDK 实测结果。

### 1. JSON-RPC 2.0 规定响应对象，不规定统一 HTTP 状态映射

[官方规范第 1、4、4.1、5、5.1 节](https://www.jsonrpc.org/specification)给出以下边界：

- 协议不绑定传输，可以用于进程内、socket 或 HTTP。它的错误码不能直接当作 HTTP 状态码，也不能由该规范推导某种 JSON-RPC 消息一定使用 HTTP 200、400 或 500。
- 对非通知调用，服务端 MUST 返回响应。响应必须包含 `result` 或 `error` 之一，二者 MUST NOT 同时出现。`result` 在成功时必需，方法调用出错时 MUST NOT 出现；`error` 在出错时必需，无调用错误时 MUST NOT 出现。`result` 的具体值由被调用方法定义，因此读到这个成员仍须解释方法自身的返回约定。
- 响应的 `id` 必需且 MUST 与请求相同；若解析或无效请求导致无法识别请求 ID，则 MUST 为 `null`。基础 JSON-RPC 允许显式 `null` 请求 ID，但 SHOULD 通常不使用它。省略 `id` 才是通知，不能把二者混同。
- 对通知，服务端 MUST NOT 返回 JSON-RPC 响应；通知本身不可确认，调用方不能据沉默判定成功或失败。这不是对每一种承载传输的确认机制作结论。
- `error.code` MUST 为整数；`message` 是短描述字符串，SHOULD 限为简洁单句；`data` 可以省略，内容由服务端定义。预定义错误码区分解析、请求结构、方法缺失、参数和内部错误；规范还留有应用自定义错误空间。不要把 `error` 一律理解为底层网络失败，或把文本消息当稳定的机器分类键。

这里使用的是 `https://www.jsonrpc.org/specification` 于 **2026-11-05T15:55:44Z** 捕获的官方 HTML，共 24,512 字节，SHA256 `8fe1edfdca511d309e712e47447457ea5159b728ec02071a84593aed692aefeb`。页内标明 Origin Date 为2010-03-26、Updated 为2013-01-04；本次抓取时间、页面声明的更新时间和 HTTP Last-Modified 各自保留，不能互换为规范发布日。定位为 HTML L109–113、145–146、182–193、206–247、250–293；没有拿 GitHub 镜像冒充官方最终规范。

### 2. MCP 的工具失败可以位于 `result` 内

MCP 2025-11-25 的 [basic 消息规则](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/basic/index.mdx#L25-L108)要求所有双方消息 MUST 遵循 JSON-RPC 2.0，并增加请求 ID 必须为字符串或整数、MUST NOT 为 `null`、同一请求方在同一会话中 MUST NOT 重用等限制。结果响应 MUST 使用对应请求 ID；错误响应也有同 ID 要求，但保留畸形请求无法读出 ID 的例外。通知 MUST NOT 带 ID，接收方 MUST NOT 回复。

[tools 的错误处理段落](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/server/tools.mdx#L460-L507)把未知工具、不满足 CallToolRequest 结构的请求和服务端错误列为协议错误示例；API 失败、输入值验证失败和业务逻辑错误则列为 `result.isError: true` 的工具执行错误示例。这里的输入值验证失败不能与请求信封/CallToolRequest 结构错误混写成同一个无条件映射。

更精确的强度见官方 [TypeScript `CallToolResult` 定义](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/schema/2025-11-25/schema.ts#L1104-L1129)：工具自身产生的错误 **SHOULD** 放在结果对象内并设 `isError=true`，而非协议级错误；这不是 MUST。查找工具失败、不支持工具调用及其他异常条件另有应走 MCP error 的指导，原文该句使用小写 `should`，本节不擅自升级为大写 MUST/SHOULD。省略 `isError` 时按 false 解释，但这只是字段约定，不是业务效果已经得到独立验证。

客户端对工具执行错误提供给语言模型是 **SHOULD**，对协议错误提供给模型是 **MAY**。因此 `isError=true` 可以在 JSON-RPC `result` 信封中成为模型可见的失败反馈；这既不是工具成功，也不保证模型实际看见、纠正或安全重试了它。相关 dated 文档和 schema 字节均来自官方仓库提交 `3c4d91b7e832d9b74338d56eed03403ccc662123` 的本次捕获，不声称是2025-11-25当天原始发布字节。

### 3. 同一固定 SDK 中，实际出口取决于已到达的路径

下表接续 [MCP 模式责任研究 #698](https://github.com/InteropAtlas/InteropAtlas/pull/698)，不重做方言实验。源码中的普通 Python 异常、`CallToolResult`、JSON-RPC 错误响应和客户端本地异常仍是不同证据。

| 到达条件 | 固定 1.26.0 源码的处理 | 可以与不可以推断的内容 |
| --- | --- | --- |
| 已进入低层 `call_tool` handler；`validate_input=True` 且取得工具定义；输入实例校验抛 `jsonschema.ValidationError` | `_make_error_result` 构造文本内容与 `isError=True`，包装成 `ServerResult` | 这是工具错误结果路径，不是天然的 JSON-RPC `error`。没有工具定义或关闭该输入开关时，不走这一输入验证分支 |
| 同一低层 handler 中，普通异常到达外层 `except Exception` | 同样转为 `_make_error_result(str(e))` | 不能写成“所有异常都转工具结果”：`UrlElicitationRequiredError` 被显式重新抛出；取消、外部包装和其他未检查路径不在这种概括内 |
| FastMCP 已按 `_setup_handlers` 注册低层 handler，ToolManager 查找不到指定工具，且无自定义拦截改写 | ToolManager 抛 `ToolError`，经低层普通异常分支形成 `isError=True` 结果 | 这条静态路径与 dated tools 页面“未知工具→协议错误”的示例不同；不能仅照搬规范示例预测该版实际出口，也不能据此给整个 SDK 作完整符合/不符合裁决。直接调用 ToolManager 而未经过低层包装时则是 Python 异常 |
| `UrlElicitationRequiredError` 穿过 FastMCP/低层工具包装，到达低层 `_handle_request` | 它是 `McpError` 子类；`_handle_request` 取其 `error`，作为 `ErrorData` 交给 `respond` | 这是被明确保留的协议错误出口，不等于普通 ToolError 分支；本节不运行 elicitation、授权或浏览器流程 |
| `BaseSession._send_response` 得到 `ErrorData` 或普通 `ServerResult` | 前者构造 `JSONRPCError(error=...)`，后者构造 `JSONRPCResponse(result=...)`，都使用传入请求 ID，发到会话写流 | 证明代码如何选择信封，并非已观察到某种传输的状态行或真实对端已收到 |
| 客户端 `send_request` 从内部响应流取到 `JSONRPCError`，或取到普通 result | 前者抛 `McpError`；后者先用指定结果类型 `model_validate`。随后 `ClientSession.call_tool` 只对 `not result.isError` 调用输出验证，最终返回结果 | 实际从对端读到的错误消息可到达这个分支，但内部类型本身不能证明消息来自线缆，另见下方断流路径。工具错误结果通常不是异常；非错误结果仍可能因模型/输出验证在客户端本地抛异常。不能用“API 未抛异常”替代读取 `isError` |
| 接收循环结束，进入 `_receive_loop` 的 finally，仍存在待响应请求 | 以 `CONNECTION_CLOSED` 和 `Connection closed` 在本地构造 `JSONRPCError`，发送到这些请求的内部响应流，随后清理 | 内部 `JSONRPCError` 也可能是本地合成；不能把 Python 类型或后续 `McpError` 当成已收到对端错误信封的证明。此处不是向网络对端发一个错误响应 |
| 客户端 `send_request` 在 `anyio.fail_after(timeout)` 中等待 `response_stream_reader.receive()` 抛 `TimeoutError`；非空请求级 timeout 优先于会话级 timeout | 在本地构造带 `code=httpx.codes.REQUEST_TIMEOUT` 的 `McpError(ErrorData(...))` | 仅看异常类或这个数值，不能断言收到过对端 JSON-RPC 错误，更不能把它当作捕获到 HTTP 响应状态；本地超时也没有证明操作未产生效果 |

逐项定位：[低层工具包装 L467–589](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/lowlevel/server.py#L467-L589)、[低层分派 L763–788](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/lowlevel/server.py#L763-L788)；[FastMCP 注册/转发 L302–346](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/server.py#L302-L346)、[ToolManager L81–93](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/tools/tool_manager.py#L81-L93)、[Tool.run L93–117](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/tools/base.py#L93-L117)、[ToolError 继承 L4–17](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/exceptions.py#L4-L17)；[UrlElicitationRequiredError L8–55](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/shared/exceptions.py#L8-L55)；[会话超时/接收 L283–308](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/shared/session.py#L283-L308)、[会话发送 L337–349](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/shared/session.py#L337-L349)、[断流本地合成 L445–456](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/shared/session.py#L445-L456)、[客户端工具结果 L368–423](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/client/session.py#L368-L423)。

### 4. 注释示例：只展示含义，不伪装成实测

以下每段均为未执行的人工示例；没有假设 HTTP 状态、网络到达、重试或业务副作用。

**A. 能识别调用 ID 的 JSON-RPC 方法错误。** 假设调用 `missing_method` 的请求 ID 为字符串 `req-7`，响应中同一 ID 用于关联；`error` 与 `result` 不并存。这个错误没有声称底层连接失败。

```json
{"jsonrpc":"2.0","id":"req-7","error":{"code":-32601,"message":"Method not found"}}
```

**B. 无法识别 ID 的基础 JSON-RPC 解析错误。** 这里的 `null` 是错误响应的关联边界，不是成功的“空结果”，也不是一个通知。此例只说明基础 JSON-RPC，不用来展示 MCP 的合法请求 ID。

```json
{"jsonrpc":"2.0","id":null,"error":{"code":-32700,"message":"Parse error"}}
```

**C. 基础 JSON-RPC 通知。** 假设 `update` 是已定义方法；以下对象省略 `id`，接收者不得给这个通知返回 JSON-RPC 响应。不附一个“成功响应”或“失败响应”，正是这个例子的含义；观察不到响应不能区分方法是否执行成功。这里没有把该通用方法名移植为 MCP 方法。

```json
{"jsonrpc":"2.0","method":"update","params":{"value":1}}
```

**D. MCP `tools/call` 的工具错误结果。** 假设某工具的业务要求数量至少为1，本例展示一个值检查失败的结果约定；具体服务是否按此返回，仍需单独证据。

请求：

```json
{"jsonrpc":"2.0","id":41,"method":"tools/call","params":{"name":"reserve_items","arguments":{"quantity":0}}}
```

响应：

```json
{"jsonrpc":"2.0","id":41,"result":{"content":[{"type":"text","text":"quantity must be at least 1"}],"isError":true}}
```

这里是 JSON-RPC 结果信封，但工具调用已报告错误。只读取 `result` 是否存在会错判；客户端还需识别 `isError`，并按应用策略处理内容。这不声明库存已预留、毫无副作用或必然可安全重试。

**E. MCP 文档所展示的另一种未知工具出口。** 参照 dated tools 示例构造，`tools/call` 方法本身与工具名查找不是同一件事，因此不要机械改成 JSON-RPC 的 `Method not found`。这也不是固定 FastMCP 路径的实测输出，后者的条件差异见上表。

```json
{"jsonrpc":"2.0","id":42,"error":{"code":-32602,"message":"Unknown tool: missing_tool"}}
```

### 5. 与 HTTP Problem Details 并读时，保留什么问题

- 先问证据来自实际 HTTP 响应、JSON-RPC 信封、工具结果还是客户端本地异常。不同来源不能仅因都出现“error”、同一个数字或“成功”用语而互相替代；这不是新增一套分类或转换映射。
- JSON-RPC `id` 回答“这个响应对应哪次调用”，不回答业务是否成功。`result` 回答的是方法返回路径；MCP 又用 `isError` 在结果内容内表达工具错误。HTTP 状态或响应体的相关判断需由 HTTP 规范和具体绑定另行支持。
- 通知本来就无 JSON-RPC 响应，超时则是调用方没有在所设期限内获得响应；两者都不能独自证明业务失败、没有副作用或允许自动重试。规范推荐提供可纠错反馈也不是自动执行重试的授权或幂等保证。
- 符合消息形状、返回结构化错误和解决用户的任务不是同一个完成条件。通用客户端需要保留响应来源、关联 ID、错误/结果分支及工具错误标志，再按实际协议和方法约定处理，而非依单个“成功”信号收敛判断。

本次未安装、导入或执行 SDK，没有启动工具、服务或传输，没有网络监听、凭据、授权/安全配置或上游写操作；公共来源下载不是 SDK 运行。原十三项纯内存观察仍是历史证据，#698 的十二项验证器探针也保留原身份，均未在本节重跑。没有穷尽消息解析、取消、Tasks、自定义包装器、所有传输、依赖版本或第三方实现；不作完整符合性、安全或生产适用结论，不扩展现有对象/关系、分类、Runtime、UI、视角、治理或未来维护规则。


## 已闭合与仍未闭合的组合问题

本次已能回答“这些固定信号各自意味着什么、哪个包装层会改变出口”：HTTP 问题字典不负责组成 HTTP 响应，HTTPX 的解析/状态检查不负责问题语义；MCP 的工具包装可把普通 Python 异常转成工具错误结果，客户端本地失败也可能使用同一异常类型。来源清单和条件化路径使这些结论不再只是图中缺少注释或查询未显示。

尚缺的是选定应用中的真实交接证据，而非泛泛的“错误支持”标签：

1. 对某一问题详情生产端，固定实际框架适配器及其状态、headers、序列化和媒体类型输出，再比对接收前后的值，才能判断某次 status 分歧发生在哪一步。本研究未选定该组件，不能宣布它不存在或不支持。
2. 对某一工具调用，固定入口、包装器、传输和客户端控制流，保留请求 ID、所收消息与本地异常来源，才能判断工具错误是否被消费者正确呈现。固定 FastMCP 的静态未知工具路径不是网络抓包，也没有填补真实调用观察。
3. 对重试或最终业务完成，需要方法自身的完成、幂等和副作用合同，以及对应操作的实际证据。202、isError、超时和异常文本都不能独自提供这项依据。

以上是基于来源提出的具体下一证据条件，不是安装、联网、部署、授权或自动重试许可。没有统一映射 HTTP 状态、JSON-RPC 错误码和业务状态，也没有增加 taxonomy、Canonical 边、Runtime、页面、视角转换或未来维护规则。所有旧 hold 保持；其他领域问题仍分别取证，不据本切片宣告底图覆盖完成。

## 来源与可复核性

[机器可读来源清单](failure-signal-comparison-2026-11-05-sources.json)保存23份外部材料的官方 URL、固定提交/出版身份、SHA256、字节数、可得的 Git blob 和行段。HTTP-S01–S11 对应 HTTP 小节；RPC-S01–S12 对应 JSON-RPC/MCP 小节中的固定链接。行号是捕获原始文件从1起计数，不是渲染页行号。完整第三方源码/规范不在本仓库镜像。

HTTP 原先准备的11份捕获与7份 MCP 既有捕获按原始字节复验后复用；JSON-RPC 官方 HTML 与4份 MCP 源文件为此比较新取。获取时间不替代出版日期：MCP 的2025-11-25页面来自所列官方仓库当前固定提交，不声称是当天首发字节；JSON-RPC 页内更新日与 HTTP Last-Modified 分列。指纹标识本次材料，不证明最新性、完整性或发行者签名。

本轮没有安装、导入或执行上游库，也没有真实 HTTP/MCP 响应实验。HTTP 表格与6个 JSON 对象全是人工未执行示例；对象仅经本地标准库 JSON 语法解析，不代表协议或语义验证。历史 HTTPX17项、MCP13项及前次验证器12项各自保留原证据身份，均未重跑或计为新增观察。适用仓库检查及独立复核另在交付 PR 记录，不等同上游符合性测试。
