# MCP 工具模式的验证责任：固定 SDK 路径与跨域边界

<!-- InteropAtlas Document Metadata v0
Document Status: bounded_experiment_record
Document Created At: 2026-11-05T14:58:07+00:00
Document Updated At: 2026-11-05T14:58:07+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / finish_wot_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_mcp_schema_evidence
  GitHub Actor: ff6962757
-->

## 问题与结论

本研究接续 [agents 领域问题](https://github.com/InteropAtlas/InteropAtlas/blob/564142bc6eef4a0cf27cff60fad017b7aa52a0ab/03_Evolution/01_Research/02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)：工具声明了输入/输出模式（inputSchema/outputSchema）后，实际由谁、在什么条件下检查方言、实例与错误？仓库背景固定为 `564142bc6eef4a0cf27cff60fad017b7aa52a0ab`；SDK 固定为 MCP Python SDK 1.26.0、提交 `3d9d34552a9ab8988acf8d06e4a705bd799fc32b`，不是最新版本或生产推荐。

答案不能只写成“SDK 使用 JSON Schema”。低层服务端、FastMCP 和客户端有不同的条件分支：低层入口委派 jsonschema；FastMCP 输入先转换再经 Pydantic；客户端只在非错误工具结果上检查输出。声明、验证器版本、真正到达的调用分支和最终响应不是同一种证据。本次源码核对没有安装、导入或运行 SDK，没有工具执行或网络监听。下文另有已安装 jsonschema4.26.0 的验证器实验，其结果不冒充这些 SDK 路径的运行。十二份来源的固定提交、Git blob、SHA256、字节数和定位见[来源清单](../03_Evidence/mcp-schema-source-manifest-20261105.json)，第三方源码全文不镜像进仓库。

## 规范要求与证据层级

本次读取 MCP 2025-11-25 的 [basic](https://modelcontextprotocol.io/specification/2025-11-25/basic#json-schema-usage) 与 [tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) 日期版页面；另外捕获其官方仓库在 `3c4d91b7e832d9b74338d56eed03403ccc662123` 的文本字节。此提交是本次捕获位置，不是声称 2025-11-25 当日的原始发布快照。

- basic 的 Schema Dialect / Implementation Requirements：缺少 `$schema` 默认 2020-12；双方 MUST 支持它，并 MUST 按声明或默认方言校验 schema，对不支持的方言 MUST 返回说明不支持的适当错误；支持方言的文档化是 SHOULD。Schema Validation 另要求 schema 本身在其方言下有效。
- tools 的 Security Considerations 将服务端验证全部工具输入列为 MUST。Output Schema 在声明输出模式时要求服务端 MUST 提供符合模式的结构化结果，而客户端验证结构化结果是 SHOULD，不应改写成两端同等的 MUST。
- tools 区分协议错误与 `isError: true` 的工具执行错误，输入值验证失败属于后一类示例。Python 异常、日志 warning、工具错误结果与 JSON-RPC error 不能互换称谓。

固定文本定位：[basic L136–186](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/basic/index.mdx#L136-L186)；[tools L335–341](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/server/tools.mdx#L335-L341)、[L460–476](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/server/tools.mdx#L460-L476)、[L510–523](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/3c4d91b7e832d9b74338d56eed03403ccc662123/docs/specification/2025-11-25/server/tools.mdx#L510-L523)。

## 固定源码责任矩阵（静态）

| 入口与到达条件 | 实际验证/转换 | 返回或仍需调用方承担的边界 |
| --- | --- | --- |
| 低层 `Server.call_tool(validate_input=True)`，且缓存/刷新列表后存在工具定义 | `jsonschema.validate(instance=arguments, schema=tool.inputSchema)`，未显式传 `cls`、format checker 或方言允许表 | ValidationError 变成带 `Input validation error` 文本的 `isError=True` 工具结果。其他普通异常落入外层捕获，同样形成工具错误。无工具定义时日志警告，并不会在此验证输入；`validate_input=False` 也跳过此步 |
| 同一低层入口，普通 dict/二元 tuple/可迭代返回值，且工具定义有 outputSchema | 先规范化；结构化输出缺失则工具错误，否则调用同形 `jsonschema.validate` | 输入开关不关闭此输出分支。返回有效只说明实际调用的模式验证成功，不证明业务成功或全部协议符合性 |
| 同一低层入口，handler 直接返回 `CallToolResult` | 立即封装 `ServerResult` 返回 | 跳过其后 outputSchema 分支；不能据函数 docstring 推断所有返回类型均经过低层输出检查。`CreateTaskResult` 也提前返回，但 Tasks 不在本研究展开 |
| FastMCP 注册及输入 | 注册低层 `validate_input=False`；`call_tool`→ToolManager→Tool.run→FuncMetadata，先 `pre_parse_json`，再 `arg_model.model_validate`，再将解析后参数交给函数 | 不是“完全不验证”，也不是直接以公布的 JSON Schema 验证原始参数。字符串预解析是有条件的，不能概括为所有 JSON 字符串都被解析；Pydantic 实际接受/强制转换行为未在本轮运行 |
| FastMCP 输出转换，`convert_result=True` | 有 output_schema 时由 output_model 校验；普通值按需要包装成 result，再 model_dump 成结构化内容并返回二元 tuple；随后可到达低层输出检查 | 直接 `CallToolResult` 若有 output_schema，FastMCP 先对 structuredContent 作 Pydantic model_validate，再原样返回，低层的提前返回仍存在。若无 output_schema 则无这步输出模型校验。不能将低层提前返回概括为 FastMCP 一概不校验 |
| 客户端 `ClientSession.call_tool` 返回 `isError=False` | 调用 `_validate_tool_result`；必要时 list_tools 刷新输出模式缓存。存在 output_schema 时要求 structuredContent，再委派 `jsonschema.validate` | 缺结构化内容抛 RuntimeError；ValidationError/SchemaError 各包装成 RuntimeError。错误工具结果跳过该方法；未列出的工具只有 warning，无模式则不作此输出验证。此方法不是发送前的 inputSchema 验证器 |

源码位置：[低层 L476–589](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/lowlevel/server.py#L476-L589)；[FastMCP 注册和转发 L302–346](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/server.py#L302-L346)；[ToolManager L81–94](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/tools/tool_manager.py#L81-L94)；[Tool 构造/执行 L72–120](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/tools/base.py#L72-L120)；[FuncMetadata L74–170](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/utilities/func_metadata.py#L74-L170)；[客户端 L368–423](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/client/session.py#L368-L423)。

FastMCP 的输出模式也不是无条件存在：`structured_output=False` 提前返回无输出模型的元数据；裸 `CallToolResult` 返回注解也走无输出模式分支，Annotated 元数据可用于提供输出类型。详见 [FuncMetadata L263–327](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/src/mcp/server/fastmcp/utilities/func_metadata.py#L263-L327)。本表只追所列代码，没有穷尽自定义配置、包装器、缓存时效性、分页或实验 Tasks。

## 历史 13 项与依赖版本不可合并

[历史被审 packet L206–233](https://github.com/InteropAtlas/InteropAtlas/blob/af265ff5fad43332bdcea22483b9486d45cb68b3/01_State/Inbox/review-packets/mcp-python-sdk-implementation-20261021.yaml#L206-L233) 的 13 项包含版本、初始化、能力、ping、工具列表/结构化结果/非法参数/未知工具、资源和提示。它明确记录纯内存执行及 jsonschema4.26.0、Pydantic2.13.4，并说明使用当时环境依赖而非历史 lockfile。该清单没有分别记录省略、显式支持或未知 `$schema` 的方言对照，不能将“非法工具参数已报告”扩大为这些分支已测，也不能把历史13项抹成未运行。

本次新增可核的区分：固定 SDK [pyproject L24–39](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/pyproject.toml#L24-L39) 声明 `jsonschema>=4.20.0`、`pydantic>=2.11.0,<3.0.0`，固定 [uv.lock L660–673](https://github.com/modelcontextprotocol/python-sdk/blob/3d9d34552a9ab8988acf8d06e4a705bd799fc32b/uv.lock#L660-L673) 的 jsonschema 是 **4.25.1**。IA 既有 `python_jsonschema` 对象也固定 **4.25.1**。历史及本轮验证器观察的 **4.26.0** 不是该 lockfile 的复现，也不自动更新 Canonical 软件身份或关系。

## 验证器层的方言选择实验（实际执行）

为区分“有调用”与“按哪种方言调用”，本轮使用已有 CPython3.12.14、jsonschema4.26.0，实际执行 `jsonschema.validate(instance=..., schema=...)`，没有传入 cls、registry 或 format_checker，也没有替换其注册表。完整夹具嵌入[自包含配方](../03_Evidence/mcp-schema-dialect-probe-20261105.py)，并随[结果](../03_Evidence/mcp-schema-dialect-probe-20261105-result.json)保留；结果同时记录依赖、validators.py 指纹、异常及 warning，而不是只有通过/失败计数。

基本模式为含 `values` 数组的对象，用 `prefixItems` 要求首项为 integer。正面对照为 `values: [7]`，非整数输入为 `values: ["not-an-integer"]`；非法模式对照把根 type 设为不合法的类型名。只改变 `$schema` 的声明或上述单一控制项，比较四种情况：

| `$schema` | 非整数首项 | 整数正面对照 | 非法模式 type | 本次解释 |
| --- | --- | --- | --- | --- |
| 省略 | ValidationError | 接受 | SchemaError | 所选库默认选择 Draft202012Validator |
| 显式 2020-12 | ValidationError | 接受 | SchemaError | 与本组省略声明结果一致 |
| 显式 Draft7 | 接受 | 接受 | SchemaError | Draft7 不执行这个 `prefixItems` 约束；接受不表示该字段已被按2020-12检查 |
| 合成未知 URN | ValidationError，并有 DeprecationWarning | 接受，并有 DeprecationWarning | SchemaError，并有 DeprecationWarning | 该依赖版本 warning 后回退到最新支持方言；不是“不支持方言”专门拒绝，也不是一律接受 |

这是 12 个实例/模式输入对上的 12 次 validate 调用，不是覆盖率；另有 12 次 `validator_for` 诊断，用于记录所选类，不能算成额外端点验证。省略声明在这个固定依赖中得到2020-12，不证明所有未来版本的“最新方言”都等于MCP日期版默认。warning 捕获设置为 always 以便完整观察，应用若将其提升为异常，传播可能不同。

预检拒绝夹具中的 `$ref`、`$dynamicRef`、`$recursiveRef`、`$id`。Python audit hook 禁止 socket/urllib 检索，profile hook 在默认外部资源检索函数入口阻止执行；两个合成保护自测与实际矩阵分开记录。自测后恢复 profile、清空事件，实际矩阵没有检索入口或 socket/urllib 事件。它们不是 OS 网络隔离，也不构成不可信 SDK 或任意外部 schema 的安全保证。

复现只需要结果记录的已有验证器依赖，不需要上述 SDK 源码或任何 MCP 服务；不要用本机其他版本 MCP 代替1.26.0：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  03_Evolution/02_Experiments/03_Evidence/mcp-schema-dialect-probe-20261105.py \
  > /tmp/mcp-schema-dialect-result.json
```

执行者和独立审核分别复跑本配方，本环境输出逐字节一致。跨环境须区分语义结果与解释器/依赖路径、哈希及 warning 定位的差异，不能隐去版本改变；配方只断言所测 jsonschema4.26.0，不自动安装依赖。该实验没有执行固定 SDK 的 client/server、FastMCP/Pydantic 或任何工具函数，不能据此将表格结果直接写成真实协议响应。

| 工件 | SHA256 |
| --- | --- |
| 来源清单 | `55a08647fd9dde95e31febff514064ff8410003ab853dbd711fbb8504d2e08a3` |
| 配方 | `31f47ae2ed52ddac2dc37b1e8815886a96f8e14d151e2a80757b6f2785143076` |
| 结果 | `5015b85d9e2d53931275efe4d1eaf8ca34911474863003ec416a3a59e5ee364f` |

## 与 WoT、UBL 的有限综合

- [WoT #697](https://github.com/InteropAtlas/InteropAtlas/pull/697) 比较同一 TD1.1 规范身份下前后资源字节及 Draft7 对关键字的解释，证明规范版本标签不能代替资源修订；它没有运行 node-wot。MCP 本次追的是 schema 是否实际进入验证以及进入哪种验证器，不是重复 WoT 的资源修订实验。
- [UBL #488](https://github.com/InteropAtlas/InteropAtlas/pull/488) 已用 xmlschema4.3.2 证明 XSD 有效仍可违反 IND5；[ph-ubl23 被审记录 L463–475](https://github.com/InteropAtlas/InteropAtlas/blob/ecbe9e495cd7dbab3e0cf31b816d7f60868b30aa/01_State/Inbox/review-packets/ph-ubl23-implementation-20261024.yaml#L463-L475) 又区分默认启用 schema、可变调用开关及无 schema 时 validate 只警告并序列化的路径。这里复用其已审证据，没有重新运行 Java/Maven，也没有把该函数名当验证发生的证明。
- 三者的共同研究判断是：规范身份、资源/方言、验证调用与领域完整符合性需要分别举证。差异不能抹平为一条通用验证流水线：WoT 的资源变化、UBL 的额外文档约束、MCP 的入口条件各有其本地证据。本次仅沿既有 MCP→JSON Schema2020-12、MCP→JSON-RPC2.0 的 agents↔syntax 连接解释边界；没有发明 MCP↔WoT↔UBL 技术边或传递实现符合性。

## 本次缩小与仍未回答的范围

已缩小的是“由谁检查”的源码未知和历史覆盖/锁文件身份未知。单独的验证器探针已观察到省略、显式和未知 `$schema` 的选择行为，但只能说明该固定 jsonschema 版本及该调用形状的行为；尤其 warning 后继续不等于 MCP 所要求的“不支持方言”错误。探针为可观察性强制捕获 warning；应用的 warnings-as-errors 等配置可能改变传播，所以也不能写成 SDK 遇到未知方言永不报错。必须实际到达所列委派路径且没有上层拦截/改写，才能讨论其对某个部署的含义。

仍未执行的是固定 SDK 端到端方言用例、FastMCP 转换后的运行输入/输出、各分支真实协议消息、不同已解析依赖的差异、第三方互通及授权/安全行为。因此不作 SDK 全局符合或不符合裁决，不把客户端的 SHOULD 改成 MUST，不把静态异常包装说成已观察的网络响应。后续若需要端点结论，需先固定具体入口、依赖、schema、返回类型和既有验证配置；这不是新的长期检查规则或自动运行许可。

本次只补既有证据链的具体责任与未知，不修改 Canonical、Runtime、对象/关系条件、历史核验日期、分类、UI/页面、视角转换或未来维护方式。旧快照、结果不确定的历史发布和全部既有 holds 保持不变。
