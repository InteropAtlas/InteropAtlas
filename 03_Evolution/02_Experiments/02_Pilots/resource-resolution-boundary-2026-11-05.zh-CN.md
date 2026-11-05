# 引用何时成为被使用的资源：JSON Schema、JSON-LD 与事件标识的跨域边界

<!-- InteropAtlas Document Metadata v0
Document Status: bounded_experiment_record
Document Created At: 2026-11-05T17:21:00+00:00
Document Updated At: 2026-11-05T17:35:40+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / finish_wot_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_resource_resolution
  GitHub Actor: ff6962757
-->

## 问题与主要发现

本记录承接[既有领域研究](../../01_Research/02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)，回答一个跨 agents、industrial、语法/语义表示和服务事件的问题：出现 URI 或引用后，哪个环节选择资源、取得内容，最终结果又受什么影响？基线固定为 `7f58751be3be669159036df039a208f2d1e9ec30`，不是当前全域快照。

**标识相同不保证资源内容相同，引用解析成功也不等于实例或业务有效。** 本次九个受控离线 JSON Schema 案例实际区分了标识、base、显式资源供应与实例判定：完全相同的根 schema 和实例，换一份独立 registry 供应的资源即可改变判定；相同双资源 registry 中，只改根 base 则选中另一资源。缺资源产生解析异常，取得资源后的类型不符产生普通实例拒绝。

JSON-LD 的对应证据是固定规范与 PyLD 静态源码，不是同级运行结果：上下文内容、最终 documentUrl、缓存和 loader 共同限定映射处理。CloudEvents `source` 则提供必要反例：URI-reference 在那里标识事件上下文，不是自动加载 schema/context 的指令。不能把三者画成共同执行管道或推出新技术关系。

## 同一个比较问题，不同责任与证据层级

| 问题 | JSON Schema | JSON-LD / PyLD | CloudEvents source |
| --- | --- | --- | --- |
| 字符串承担什么作用 | `$id` 标识资源并提供 base；`$ref` 选定应应用的 schema | `@context` 字符串进入上下文解析；普通节点/属性 IRI 不都需要取得资源 | URI-reference 标识事件发生的上下文，source+id 有事件唯一性要求 |
| 相对值依赖什么 | 当前 base 与 `$ref` 合成目标 URI；本轮 A/B 已执行 | 上下文 base URL、活动 base IRI、API base 不可混同；嵌套上下文用取得文档的 URL，静态核对 | 允许相对 URI-reference，绝对 URI 为 RECOMMENDED；没有因此建立自动 dereference 责任 |
| 资源从哪里来 | 本轮显式 registry 或纯内存/拒绝 callback；两者均无外部读取 | ContextResolver 缓存、选择的 documentLoader、RemoteDocument；仅源码证据 | 本条款不要求通过 source 取得文档；应用可另定义行为 |
| 成功说明什么 | 在被选资源与指定 validator 下，实例未产生 errors | 若执行，还须区分已取得、已解析、已处理与展开结果；本轮无运行结果 | 合法标识不是生产者真实、事件送达或内容可信的证明 |
| 本轮证据 | 规范 + 安装源码 + 9 个实际离线案例 | 日期版规范 + commit 固定源码 + 1 组明确未执行说明例 | 版次固定规范的角色对照，没有 SDK 实验 |

RFC3986 [§1.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.2)明确区分 identification 与 interaction：URI 的存在不保证也不暗示可访问；关联操作由所在协议元素或数据格式定义。它描述 retrieval 可以涉及缓存和取得时的表示，不把标识符当资源字节锁定值。此处“相对引用合成绝对 URI”与“实际取得表示”分别说明，避免把 resolution 一词的不同上下文含义混用。

[机器可读来源与既有关系上下文](../03_Evidence/resource-resolution-20261105-sources.json)绑定规范、固定源码、九个既有对象的身份/来源及七条原关系的完整 context/evidence。它沿用现有 loader/normalizer 做显式对象选择，不以 capability 字段筛选，也不把省略或未注释解释成不支持。选择器没有创造关系闭包；第三方全文不镜像进仓库。

## JSON Schema：标识、基址、资源供应与实例判定不能合并

**观察结论。** 在本次已安装的 `jsonschema 4.26.0` 与 `referencing 0.37.0` 中，相同根 schema、`$ref` 字符串及实例，因显式注册表供应不同 schema 字节而改变判定。URI 字符串相同不保证输入资源相同。缺少资源导致引用解析异常，与已经取得 schema 后的普通实例拒绝是两条不同路径。

这不是 IA `python_jsonschema 4.25.1` 对象版本更新，也不证明两版等价；基线为 `7f58751be3be669159036df039a208f2d1e9ec30`。没有运行 MCP SDK、node-wot、完整符合性测试，也没有重做 #698 的 12 个 dialect-only 案例。

### 规范依据与证据层级

官方 [2020-12 Core](https://json-schema.org/draft/2020-12/json-schema-core) 为 2022-06-16 的 `draft-bhutton-json-schema-01`，不能称为 RFC。精确短引文及锚点保存在 来源清单的 `json_schema_normative`：

- §8.2.1：`$id` 标识 schema resource；绝对 URI 还为内部相对引用提供 base，不能由网络形式的标识推导下载。
- §8.2.3.1：`$ref` 按当前 base 解析为被应用 schema 的 URI，并应用其结果。
- §9.1.2：实现可提前关联 URI 与 schema。这里 A/B 是两个独立配置，不测试同一注册表内同 URI 冲突。
- §9.2：解析后的 URI 若指向已经提供的 schema，应自动使用该 schema。

Core 全文的直接原始读取返回 HTTP 403，本轮没有重试或绕行；保存的是连接器提取文本，不宣称完整原始 HTML。来源清单分别标明提取字节的 hash、条款锚和核对短引文，不能把提取 hash 当官方响应 hash。

这些是规范事实；以下是固定本地实现和显式配置的观察，不把规范措辞改写为跨实现运行保证。

### 固定输入与方法

[离线脚本](../03_Evidence/resource-resolution-20261105-probe.py) 为可直接执行的有限离线脚本。[原始 JSON 输入](../03_Evidence/resource-resolution-20261105-cases.json) 保留实际解析的 UTF-8 JSON 文本：根 schema、instance、registry URI→资源文本及 callback URI→资源文本。根引用固定 `target.json`，根 base 为 `https://example.invalid/a/root.json` 或 `/b/root.json`；资源分别是 `{"type":"integer"}` 与 `{"type":"string"}`。用于资源标识和引用目标的 URL 均为 example.invalid 合成标识；`$schema` 保留官方方言 URI。本次没有网络访问。

逐例使用新的 `Registry(retrieve=retrieve)`，通过 `with_resources` 预供资源，再明确调用 `Draft202012Validator(..., registry=registry).iter_errors(instance)`。未调用 `check_schema`，不将此结果当成 schema 自身合法性证明。callback 只记录 URI，返回既有内存资源或抛 `NoSuchResource`；无 HTTP、文件或其他外部加载。进程 audit guard 在第三方导入前生效，拒绝 socket、HTTP/urllib、子进程等事件；探测阶段同时拒绝 `open`。

### 完整结果

| case | 关键控制 | 实际结果 | callback URL |
|---|---|---|---|
| id_only_accept | 只有 `$id` 与 integer 约束；7 | accepted | 无 |
| id_only_reject_instance | 同 schema；`"seven"` | ValidationError | 无 |
| same_root_registry_A | root A；7；目标供应 integer | accepted | 无 |
| same_root_registry_B | 完全相同 root 与 7；目标改供应 string | ValidationError | 无 |
| relative_base_a | 同一双资源 registry；base A；7 | accepted | 无 |
| relative_base_b | 同 registry、相同 `$ref` 与 7；仅 base 改 B | ValidationError | 无 |
| missing_resource_rejected_callback | root A；7；空 registry；拒绝回调 | 引用解析异常 | `https://example.invalid/a/target.json` |
| explicit_memory_callback | root A；7；空 registry；回调供应 integer | accepted | `https://example.invalid/a/target.json` |
| registered_resource_bad_instance | root A；供应 integer；`"seven"` | ValidationError | 无 |

[完整结果](../03_Evidence/resource-resolution-20261105-result.json)（与原 stdout 字节相同） 保存逐例实际消息、完整错误类、路径、异常 cause 链、callback URL 和审计记录。实例错误为 `jsonschema.exceptions.ValidationError`；缺资源则抛 `jsonschema.exceptions._WrappedReferencingError`，其显式 cause 为 `referencing.exceptions.Unresolvable`，消息 `Unresolvable: target.json`。callback 明确抛的 `NoSuchResource` 在该实现中被 `raise ... from None` 屏蔽，不在展示的 cause 链中伪造一层。

9 个分类及 callback 列表断言全部通过，最终运行 guard 事件数为 0。回调被调用证明实现请求该 URI 的资源，不证明发起网络请求；成功的内存回调则证明回调不等于下载。`$id` 单独出现的两例均未触发回调。

### 实现路径和界限

重放输出的 `api-inspection.json` 包含实际安装 API 的签名和源代码，`sources/` 保存六个实际安装模块；仓库内[环境清单](../03_Evidence/resource-resolution-20261105-environment.json)绑定其版本、依赖声明、包内相对路径、字节数和 SHA-256。环境清单中的 snapshot 路径是重放输出目录内的名称，不是仓库内文件链接。观察路径为 `$ref` keyword → `_validate_reference` → `Resolver.lookup`（base 与 ref 合成 URI）→ `Registry.get_or_retrieve`（先查询/爬取已有资源，未命中才调用 retrieve）→ 应用解析结果。API 源码与运行结果分别保留，不用源码推断替代运行。

未知项保持未知：默认 registry、默认远程行为、HTTP 下载、缓存、认证、恶意 URI、并发、跨进程、`$dynamicRef`、anchor/fragment、schema 自身校验及其他版本均未探测。audit guard 是本进程的防护和观察，不宣称通用安全沙箱。开发阶段的失败记录独立于本次最终成功运行，不纳入最终结果集。

**用于跨域比较的限定。** 此处能够比较的是“引用文本/基址 → URI → 显式供应资源 → 实例判定”的证据链及缺资源分支，不等同于其他标准的 endpoint、operation、链接目标或协议传输，也不能由依赖声明推导 SDK 使用同一版本或同一 registry 配置。


## JSON-LD：上下文引用、资源取得与映射处理是不同责任

### 范围与证据身份

本节只读核对 [JSON-LD 1.1 Syntax Recommendation（2020-07-16）](https://www.w3.org/TR/2020/REC-json-ld11-20200716/)、[Processing Algorithms and API 同日 Recommendation](https://www.w3.org/TR/2020/REC-json-ld11-api-20200716/)，以及 PyLD 3.3.0 固定 commit `3ac1987d9be3648c09b7c7e34865ce82d637e742` 的源文件。原字节的 SHA-256、大小和捕获行锚在来源清单的 `jsonld_static_sources`。不是网络行为观测、安装或运行，也不重新执行、认可或扩大历史 18 例；这些历史例仍排除真实远程上下文。PyLD 未安装，本次未导入、运行或变更全局 loader。

### 规范责任：识别符解析不等于资源取得

- 上下文中的术语映射把属性名展开为 IRI；普通节点 `@id` 或属性 IRI 不是“凡出现就下载”的指令。需要取得的是算法指定的文档/上下文引用。API §5.2 的 IRI Expansion 与 §4.1 的 Context Processing 是不同算法。固定 PyLD `_expand_iri`（`jsonld.py` L6053–6140）进行映射、拼接和基址解析；`ContextResolver`（L64–78、120–131）才处理字符串上下文并在缓存未命中时进入取得路径。
- 字符串 `@context` 先相对 **base URL** 解析；该值不能与活动上下文的 **base IRI** 或 API `base` 选项混为一谈。规范明确提示三者可能不同。在该算法处理过程中，已取得的上下文应复用，不重复 dereference；递归处理使用所得 `RemoteDocument.documentUrl` 作为上下文 base URL，并保留它供嵌套引用解析。来源：[API §4.1](https://www.w3.org/TR/2020/REC-json-ld11-api-20200716/#alg-context-string)，HTML L2509–2577。
- 规范的 `RemoteDocument.document` 可以是原始 payload，也可以是已解析文档；`documentUrl` 是加载文档的最终 URL，用于正确处理重定向；`contextUrl` 是响应中 JSON-LD context Link 关系的上下文 URL，不是“本次下载的最终地址”。`application/ld+json` 的 context Link header 被忽略。来源：[API §9.4.3](https://www.w3.org/TR/2020/REC-json-ld11-api-20200716/#remotedocument)，HTML L7630–7670。资源字节到内部表示、内部表示到展开结果，仍是后续步骤，不是 URL 本身的保证。
- 规范允许自定义 `documentLoader` 使用本地上下文缓存或应用专用协议，并不要求每次上下文引用都上网。Syntax §4.10 是非规范性说明；API §9.4.1 才定义 callback 要求。[API callback](https://www.w3.org/TR/2020/REC-json-ld11-api-20200716/#loaddocumentcallback)，HTML L7520–7605；[Syntax 加载说明](https://www.w3.org/TR/2020/REC-json-ld11-20200716/#loading-documents)，HTML L9855–9890。

### 固定实现责任：调用选项、解析器、缓存与 loader 分层

- `expand` 在未提供选项时选择默认 loader，并构造使用共享缓存的 `ContextResolver`；若输入是字符串，先加载输入文档，若为内存对象则不为输入本身加载。默认 base 来自返回的 `documentUrl`（`jsonld.py` L598–657）。内存对象中若有远程 `@context`，仍可能进入上下文取得路径。
- `ContextResolver.resolve` 先查缓存。`_get` 先查本次操作缓存，再查共享缓存中 `static` 项；`_cache_resolved_context` 总写操作缓存，有 tag 才写共享缓存。不能把这说成“每个上下文总加载一次”或持久网络缓存保证（`context_resolver.py` L64–118）。`ResolvedContext` 还按 active-context UUID 缓存已处理上下文（`resolved_context.py` L16–40），这是又一层缓存。
- 未命中时，resolver 先解析相对 URL，再调用 `jsonld.load_document`，后者调用选定 loader，并在收到字符串 document 时解析 JSON 或走对应 HTML 提取分支（`context_resolver.py` L120–171；`jsonld.py` L6580–6655）。这里的源码分支不等于已验证这些格式的运行结果。
- 固定 Requests loader 的 `session.get` 负责 HTTP 请求；用 `response.url` 填 `documentUrl`、按 Link header 填 `contextUrl`，用 `response.json()` 填 `document`；相关 alternate 分支可能再次调用 loader（`documentloader/requests.py` L67–102）。这是所检源码的责任分工，不是本轮实际联网加载上下文记录。
- resolver 从 `remote_doc.documentUrl`（缺键时回退请求 URL）取得嵌套上下文基址，把字符串/数组以及术语定义内的 `@context` 相对 URL 转为绝对 URL，然后递归解析（`context_resolver.py` L120–131、209–241）。此结论只针对源码明确遍历的 `@context`，不扩写成“所有 URI 都按这个基址加载”。
- 选定 loader 的允许名单、拒绝策略、离线存储及资源可用性是调用者/部署条件，不是 JSON-LD 的自动保证；缓存还可能绕过此次 loader 调用。源码的 `set_document_loader` 改进程默认值（`jsonld.py` L306–313），本轮未调用。历史有限例的拒绝 loader 不能泛化为所有 API 的通用离线或安全保护。

### 必须保留的规范/实现边界

规范要求远程上下文忽略 `@base`：API §4.1 的条件是 `remote contexts` 为空才处理该项（HTML L2634–2655；Syntax 非规范性说明 L3828–3835）。不能据此直接断言固定 PyLD 分支已实现同样效果：`context_resolver.py` L195–199 保留取得文档的 `@context`，`jsonld.py` L3250–3315 接收解析结果，而 L3413–3433 的 `@base` 分支未显式区分远程上下文。本次把它标为**实现条件待核验点**，不宣称已执行不符合性测试，更不替历史 18 例补远程覆盖。同样，规范对缺少顶层 `@context` 的远程文档要求报错（API HTML L2554–2557），固定 resolver L195–197 则替换为空上下文；不要将规范要求自动写成该实现的已证能力。

### 同输入、同上下文标识符而不同映射：未执行说明例

来源清单的 `jsonld_unexecuted_illustration`（`actual_result: null`） 精确保存输入、两种假设的内存 loader 返回值及源码推导结果，明确标记 `UNEXECUTED_SOURCE_DERIVED_ILLUSTRATION`。输入均为 `{"@context":"https://example.invalid/context.jsonld","@id":"urn:example:item","label":"A"}`。若两个独立、空缓存的假设操作分别取得 `label → https://example.invalid/vocab/name` 与 `label → https://example.invalid/vocab/title`，按映射展开后的属性 IRI 就不同。全部标识符均未访问；这不是同一在线 URL 的变化观测，也不是新的 PyLD 实验。该例只说明输出依赖取得并采用的上下文内容，不说明 HTTP 内容协商、服务器行为、可用性或安全保证。

### 既有对象连接范围

仅作为 `pyld`、`json_ld_1.1`、`rdf_1.1_concepts`、`wot_td_1.1` 既有上下文的比较材料；可与已有 `03_Evolution/02_Experiments/02_Pilots/wot-td-resource-runtime-2026-11-05.zh-CN.md` 对照资源引用责任。不新增执行管道、对象映射或关系语义，不改变 RDF 1.2 / PROV-O hold，不触及 UI、项目规范或治理。

### 固定源码直达锚

- [ContextResolver：缓存、取得与嵌套基址 L64–241](https://github.com/digitalbazaar/pyld/blob/3ac1987d9be3648c09b7c7e34865ce82d637e742/lib/pyld/context_resolver.py#L64-L241)。
- [expand：loader/resolver 与 documentUrl L598–657](https://github.com/digitalbazaar/pyld/blob/3ac1987d9be3648c09b7c7e34865ce82d637e742/lib/pyld/jsonld.py#L598-L657)。
- [固定 @base 分支 L3413–3433](https://github.com/digitalbazaar/pyld/blob/3ac1987d9be3648c09b7c7e34865ce82d637e742/lib/pyld/jsonld.py#L3413-L3433)。
- [Requests loader L67–102](https://github.com/digitalbazaar/pyld/blob/3ac1987d9be3648c09b7c7e34865ce82d637e742/lib/pyld/documentloader/requests.py#L67-L102)。

## CloudEvents：标识用途不能自动提升为资源加载要求

固定 [1.0.2 source 条款](https://github.com/cloudevents/spec/blob/fc1f6f31f5f011a72183f1bcea20c987cb683ade/cloudevents/spec.md#L263-L295)要求非空 URI-reference，绝对 URI 只是 RECOMMENDED。它标识事件发生的上下文，具体编码语义由 producer 定义；source+id 必须区分事件，source 可以覆盖多个 producer。条款同时列出 HTTPS、mailto、URN 和应用相对标识示例。因此不能由 source 外形像 URL 就套用 JSON-LD loader 或 JSON Schema registry。该结论不是禁止应用访问 source，也不是证明其真实性或安全性。

已有 `cloudevents_1.0.2_uses_uri` 保留的正是这个字段级语法用途；`wot_td_1.1_uses_uri_rfc3986`、`wot_td_1.1_uses_json_ld` 和 `mcp_uses_json_schema_2020_12` 各有自己的 context/evidence，不能通过共同端点互相继承运行保证。

## 与已完成证据的接合，以及仍未闭合的段落

- [WoT 资源比较](wot-td-resource-runtime-2026-11-05.zh-CN.md)已经证明同一 Recommendation 名下固定前后 TD/TM schema 资源改变部分合成输入的判定。本轮新增的是另一控制：固定根输入而改变供应资源，或保持资源集合而改变 base。前者不是 node-wot 依赖字节证明，后者也没有运行 node-wot。版本标签、资源 hash、实际调用入口仍需分别确定。
- [MCP 验证责任](mcp-schema-responsibility-2026-11-05.zh-CN.md)已经区分 SDK 调用分支和独立 validator 方言案例。本轮重读固定 SDK1.26.0 [低层输入/输出](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/lowlevel/server.py#L520-L571)与[客户端输出](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/client/session.py#L398-L423)的 validate 调用，选定语句没有显式传 registry。这只是参数层面的源码事实；不能把本轮显式内存 registry 的结果赋给 SDK 默认配置，更不能据此断言它会联网、禁止联网或使用本轮安装版本。
- JSON-LD 远程上下文的 base、缺少顶层 @context、缓存命中及重定向仍是具体待核验条件。固定源码能说明该看哪些分支，但不能用源码推导的 A/B 说明例冒充观察结果。既有实现边没有因此增加“所有远程上下文正确”的承诺。
- 这些证据足以排除“只保存引用字符串即可固定解释”的宽泛假设。它们尚不回答具体部署实际取到了哪些字节、缓存是否覆盖 loader 策略、离线拒绝是否覆盖所有入口、取得失败如何呈现给协议调用方。要闭合某一选定应用链，需获得其确切配置/资源/结果，而不是由三类标准共同使用 URI 推断互通。

以上是有来源的研究判断和剩余问题，不是新增系统设计、统一 resolver API、安全策略、持续维护义务或自动研究队列。没有更新 Canonical、Runtime、UI、全域快照或任何 hold。

## 一次性离线复核

使用已经安装依赖的环境，不为本配方安装或下载任何东西。环境身份见前述清单；这份结果属于 jsonschema4.26.0/referencing0.37.0，IA 的 python_jsonschema4.25.1 对象保持不变。选择尚不存在、不同于脚本目录的仓库外临时输出目录：

```sh
python 03_Evolution/02_Experiments/03_Evidence/resource-resolution-20261105-probe.py \
  --output-dir /tmp/resource-resolution-replay
```

预期退出 0，9 个分类及 callback 列表断言通过，4 个 accepted、4 个 instance_rejected、1 个 resolution_exception，最终运行无被 guard 拦截事件。七例不调用 retrieve，缺资源和纯内存 callback 两例各调用一次同一目标 URI。输出目录保留 cases、results、环境、API 源码及安装模块快照；stdout 等于 results.json。脚本只写显式新目录，不自动创建项目文件。

最终作者运行与独立复核运行的 cases、results、environment 字节完全相同；各自源 hash 在来源清单中。需复核的三个输出 SHA256：

- cases.json：`f25b2703acfb794a73f7dee603f67ad2f06497dc9511e7a23d4c33978d095641`。
- results.json：`e506597d0dc4e08e95637b9d30fba128ce67c312683ec15b6912d8bf80252ace`。
- environment-manifest.json：`9349b90542658667625478aa54077afc75560e3a428433c7c5b03bd994f69e6d`。

环境清单含精确 Python build 和依赖元数据，其他环境不保证同 hash；不得用改写 expected 结果掩盖差异。审计 guard 是本进程有限防护，不是任意代码/系统调用的通用沙箱。开发过程的包装失败不纳入上述最终成功结果，也不意味着所有尝试从未触发 guard。
