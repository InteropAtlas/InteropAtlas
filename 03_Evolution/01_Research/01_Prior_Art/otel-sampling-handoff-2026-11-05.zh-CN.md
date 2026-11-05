# OpenTelemetry Python 1.45.1：从已提取父上下文到采样与 on_end 的条件衔接

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-source Conditional Handoff
Document Created At: 2026-11-05T20:47:00+00:00
Document Updated At: 2026-11-05T20:47:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot
  GitHub Actor: ff6962757
-->

检视日期：2026-11-05。InteropAtlas 基线：`cb25cf9677c94acd8b8b00e2c3720107836e7d96`。上游固定 commit：`14971cef9c84c2354cbaf6871090896fad0f9a1a`。本研究不修改 Canonical 对象、能力、技术关系、查询或项目级维护规则。

## 1. 新回答及实际用途

**对于明确选择的有效远程父上下文，传播成功不是记录，更不是导出。** 在启用的 SDK tracer、默认 `ParentBased(ALWAYS_ON)` 及正常调用条件下：

- sampled 远程父上下文选择 `remote_parent_sampled=ALWAYS_ON`，得到 `RECORD_AND_SAMPLE`；创建中的 SDK 子 span 处于 recording 状态且 sampled=true。正常首次结束时，已注册的 `BatchSpanProcessor.on_end` 会经过 sampled 筛选而调用内部 `emit`。
- unsampled 远程父上下文选择 `remote_parent_not_sampled=ALWAYS_OFF`，得到 `DROP`；仍构造可用于上下文传播的本地子 `SpanContext`，但返回 `NonRecordingSpan`，其 `end()` 不调用 SDK 处理器。
- **仅增加一个对照配置**：显式传入 `AlwaysRecordSampler(DEFAULT_ON)`。它不更改 sampled 决定，而将上述 `DROP` 改为 `RECORD_ONLY`。同一个 unsampled 父输入因此得到 recording=true、sampled=false 的 SDK 子 span；正常首次结束会到达已注册的 `on_end`，但 `BatchSpanProcessor.on_end` 立即返回，不调用内部 `emit`。

这给 services/transport 请求可观测性带来具体判断：**“能关联 trace ID”“处理器能观察结束的 span”“通过批处理器 sampled 筛选”是三个不同条件。** 看到远程上下文或记录型 span，不能据此认定它进入导出队列；没看到批处理导出的 span，也不能反推没有上下文或没有发生记录。上述对照让已有传播证据与批处理证据之间的采样责任可被定位，不宣称已运行一条跨包、跨服务或网络互通管道。

`emit` 是本研究的下游停止点：它不代表成功入队、保留、导出回调成功、网络送达或 Collector 确认。此前 SDK 队列、丢弃、flush 与 shutdown 的结论仍是历史证据，本轮没有重做。

## 2. 证据等级和范围

本轮执行的是公开固定源码的读取、UTF-8 字节保存、SHA-256/Git blob 重算、定位及人工条件推导。**没有安装、导入、构建、执行上游代码或测试，没有实例化 SDK、线程、处理器、exporter，没有遥测网络活动或真实业务数据。** 读取公开 GitHub 源码本身不等于执行遥测。

[机器可读证据附件](otel-sampling-handoff-2026-11-05.json)分开保存：

- `source_verification`：九份源码的固定 URL、commit、blob、字节数、SHA-256、行段及 IA 编写的导航注释；六份与既有研究使用相同源码文件，三份是本次衔接的最小补充（sampling、span-context helper、ID generator）。
- `illustrative_cases`：九个新定义的假设输入及条件推导，不是历史22例的重建。全部 `execution_status=UNEXECUTED`、`actual_result=null`。
- `existing_evidence`：两个原接纳 packet、两个既有对象及本次所续接审计的固定身份。原 API packet 只有22例汇总及范围，不能据此捏造逐例输入输出。
- `verification_boundary`：源码与仓库记录的身份核对，以及没有上游执行、遥测或历史重跑的边界。身份核对通过不等于行为测试；人工源码推导也不是外部来源直接作出的整体结论。

### 历史证据不合并为本轮运行

1. [API 原接纳 packet](https://github.com/InteropAtlas/InteropAtlas/blob/d453849f9510a2c575642a33ec50b77bf031f36d/01_State/Inbox/review-packets/opentelemetry-api-implementation-20261021.yaml) 记录22个可信内存 carrier/context 示例；这不是 SDK 测试，本轮没有重跑。
2. [当前 API 对象，固定 IA 基线](https://github.com/InteropAtlas/InteropAtlas/blob/cb25cf9677c94acd8b8b00e2c3720107836e7d96/01_State/01_Objects/opentelemetry_python_api.yaml) 保留10月30日的静态澄清：指定拒绝分支保留传入 Context，inject 不自动清旧字段。这里引用其父上下文后果，不另作载体研究。
3. [SDK 原接纳 packet](https://github.com/InteropAtlas/InteropAtlas/blob/6eeb4f53dd270878f405ad5f97824b058e03ef01/01_State/Inbox/review-packets/otel-sdk-batchspan-20261101.yaml) 固定七份文件，未包含 `sampling.py`；批处理、flush、shutdown 只做过静态检视。[当前 SDK 对象](https://github.com/InteropAtlas/InteropAtlas/blob/cb25cf9677c94acd8b8b00e2c3720107836e7d96/01_State/01_Objects/opentelemetry_python_sdk.yaml) 继续作为这些下游限制的入口。

## 3. 输入和配置须先明确

以下值只是假设性的测试设计，未执行：

- trace ID：`4bf92f3577b34da6a3ce929d0e0e4736`；远程父 span ID：`00f067aa0ba902b7`。
- sampled 输入：`traceparent=00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`。
- unsampled 输入：同上，仅末尾为 `00`。
- 二者的 `tracestate=vendor=value`；下文把解析后的这个有效 TraceState 记为 S。
- 载体为可信、正确取值的内存文本映射；extract 的 base 为明确的空 `Context()`。以上输入会走源码中有效提取分支，不借此声明任意 HTTP 适配或输入均安全。
- **将 extract 返回的 Context 直接作为 SDK `tracer.start_span(..., context=returned_context)` 的参数。** 这既排除未受控 ambient parent，也不要求全局 provider 或上下文更改。若实际使用 attach，则须保证调用时 current context 正是该返回值；本轮没有执行 attach。
- 选定 SDK provider/tracer 均启用，构造/调用参数有效。默认配置例中未提供 sampler，`OTEL_TRACES_SAMPLER` 未设置，因此 `_get_from_env_or_default` 选 `parentbased_always_on`。不能把任何未显式给 sampler 的环境都称为这个默认值。
- 对照是 `TracerProvider(sampler=AlwaysRecordSampler(DEFAULT_ON))` 的源码路径。该对象为 truthy，跳过 provider 的 `if not sampler` 环境回退。它不是环境变量中另一个已验证的名字，也未审自定义 entry-point 配置器。
- 若要谈到 BSP：该 provider 的默认同步 multi-processor 已注册该 BSP，且未换用自定义 processor 链。记录型 span 已成功 start，并发生正常首次 end；结束指标回调、`_on_ending`、之前注册的处理器回调都正常返回，没有异常或中断阻断到达目标。只是取得 span 或重复调用 end 不满足这项前提。

“启用”不可省略：`OTEL_SDK_DISABLED` 的处理可令 provider 返回 `NoOpTracer`；per-tracer 配置的 `is_enabled=false` 则在 `start_span` 调用 sampler 之前返回 `NonRecordingSpan(parent_context)`。这两条旁路不适用下文的正常采样表。

## 4. 精确调用链和责任位置

### A. extract 产生上下文，不选择 SDK，也不自动设为 current

[tracecontext.py L37–86](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/propagation/tracecontext.py#L37-L86) 将有效头部解析为 `SpanContext(is_remote=True)`，包在 `NonRecordingSpan` 中，通过 `set_span_in_context` 返回 Context。**父 span wrapper 不 recording，不妨碍其有效 SpanContext 的 sampled 标志参与子 span 采样。**

[span helper L12–37](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/propagation/__init__.py#L12-L37) 与 [context L59–116](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/context/__init__.py#L59-L116) 表明：set 返回复制后的 Context，attach 才关联当前执行上下文；显式空 Context 与 `None` 不等价。SDK 若省略 `context`，查的是当时的 current span，不会自己寻找刚刚 extract 的返回值。

API provider/proxy/no-op 路径也不等同 SDK。没有已配置 provider 且未指定 provider 环境变量时取得 proxy；尚无真实 provider 的 proxy 用 no-op tracer。选定的有效 SDK provider 是本报告前提，不由 extract 激活。[API trace L404–473](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/__init__.py#L404-L473)、[L520–575](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/__init__.py#L520-L575)。

### B. provider 选 sampler；start_span 选父上下文和 trace ID，再问 sampler

[SDK trace L1253–1279](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L1253-L1279) 中的判断是 `if not sampler`，不仅是 `sampler is None`。其环境选择见 [sampling L455–479](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L455-L479)。provider 把该 sampler、ID generator 和 processor 传入 tracer，[L1374–1398](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L1374-L1398)。`start_span` 本身没有单次 sampler 参数。

[start_span L1150–1171](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L1150-L1171) 先取所选 Context 的 span context，检查类型和 tracer enablement。父 SpanContext 有效则沿用 trace ID；无效或不存在则把 SDK parent 设为 None 并调用生成器取得 trace ID。传给 sampler 的仍是原 `context` 参数，而非改写成 None 的本地 parent 变量。

### C. ParentBased 先看有效性，再区分 remote/local 和 sampled

[sampling L300–364](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L300-L364) 的精确委托是：

| 所选父 SpanContext | 委托 | 本报告默认委托的决定 |
| --- | --- | --- |
| 不存在或无效 | root | `ALWAYS_ON` → RECORD_AND_SAMPLE |
| 有效、remote=true、sampled=true | remote_parent_sampled | `ALWAYS_ON` → RECORD_AND_SAMPLE |
| 有效、remote=true、sampled=false | remote_parent_not_sampled | `ALWAYS_OFF` → DROP |
| 有效、remote=false、sampled=true | local_parent_sampled | `ALWAYS_ON` → RECORD_AND_SAMPLE |
| 有效、remote=false、sampled=false | local_parent_not_sampled | `ALWAYS_OFF` → DROP |

默认四个 parent 委托成对相同，但它们是四个独立配置槽，不可删去 remote/local 分支只写“跟随父 sampled”。改变 root sampler 也不会自动改掉四个有效父委托。由 SDK 创建的子 SpanContext 固定 `is_remote=False`；如果之后**实际把该子 span 放入下一次调用所选 Context**，下一跳走 local 分支。`start_span` 不自动设为 current，[API trace L286–295](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/__init__.py#L286-L295)。

### D. 唯一对照把 DROP 变为 RECORD_ONLY，不增加 sampled

[sampling L370–420](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L370-L420) 中 `AlwaysRecordSampler` 先执行包装的 root（本报告为 DEFAULT_ON，亦即 ParentBased(ALWAYS_ON)）。只有返回 DROP 时才产生 RECORD_ONLY，沿用该 result 的 attributes 和 trace_state。

这不是“总采样”，也不是“恢复被丢掉的原始 attributes”：默认 unsampled 分支已由 `StaticSampler(DROP)` 把 attributes 置为 None，`SamplingResult` 将其变为空映射；wrapper 只是保留这个结果。[sampling L176–187](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L176-L187)、[L215–243](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L215-L243)。本报告的示例不带业务 attributes，不扩展到完整属性、事件或指标审计。

### E. child 状态、标志和 tracestate 不是 carrier 的盲目复制

[SDK trace L1173–1220](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L1173-L1220) 与 [Decision L147–159](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L147-L159) 支持以下**未执行推导**：

| 明确远程输入 / sampler | decision | start 成功后且 end 前 recording | child sampled / flags | 正常首次结束到 BSP.on_end | BSP 调用 emit |
| --- | --- | --- | --- | --- | --- |
| 01 / DEFAULT_ON | RECORD_AND_SAMPLE | true | true / 01 | 是，若已注册并到达 | 是 |
| 00 / DEFAULT_ON | DROP | false | false / 00 | 否，NonRecordingSpan.end 为 no-op | 否 |
| 01 / AlwaysRecordSampler(DEFAULT_ON) | RECORD_AND_SAMPLE | true | true / 01 | 是，若已注册并到达 | 是 |
| 00 / AlwaysRecordSampler(DEFAULT_ON) | RECORD_ONLY | true | false / 00 | 是，若已注册并到达 | 否，在 sampled 筛选返回 |

四者都沿用有效父 trace ID，都调用 `generate_span_id()` 取得 child span ID，child `is_remote=False`，选定的默认委托保留有效父 S。这里的“生成”是一次生成器调用，不保证 ID 与父 ID 一定不同，也不证明无碰撞。

- sampled 位 0x01 来自 **sampling_result.decision**，不是直接照抄父标志；有效父的 random-trace-id 位 0x02 另行继承。未保留任意其他父 flags 位。
- 因此上述 01/00 两输入的结果分别是01/00；若同样有效父另带 random 位，03/02 对应分支将生成03/02。此为同一源码表达式推导，不是新增 flags03 运行例或2021规范验证。
- trace_state 来自 **SamplingResult.trace_state**。本报告所选 StaticSampler 经 `_get_parent_trace_state` 返回有效父 S，wrapper 不改它；任意自定义 sampler 可能修改 trace_state，不能推广为所有配置均保留。[sampling L482–488](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/sampling.py#L482-L488)。
- recording 是生命周期状态。记录型 SDK span 的 `is_recording()` 在结束后为 false，不应把表中 end 前状态当作结束后仍为 true。[SDK trace L956–978](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L956-L978)。

### F. on_end 与 batch admission 的最后一段是既有下游事实的连接

记录型 `_Span` 的 `start()` 调用 processor.on_start；首次正常 `end()` 设置结束时间后，依次执行结束指标回调（如有）、`_on_ending`、转换 ReadableSpan、`on_end`。[SDK trace L943–971](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L943-L971)。同步 multi-processor 按注册顺序调用各处理器，[L163–189](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/__init__.py#L163-L189)。

`NonRecordingSpan.end()` 只有 pass；[API span L523–539](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/span.py#L523-L539)。反之 RECORD_ONLY 确有 SDK end 路径，但 [BSP L212–215](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/export/__init__.py#L212-L215) 只在 context 存在且其 sampled 为真时 emit。这是新采样推导与**已审** sampled 门的连接，不将后者包装成新发现。

## 5. 无效父边界必须与解析失败分开

`SpanContext.is_valid` 检查两个 ID 的非零及位宽范围，[API span L453–473](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/span.py#L453-L473)。SDK 对无效或不存在父不继承其 trace ID；ParentBased 也以 root sampler 决定，而不是相信这个无效对象上的 remote/sampled 标志。非 None 但不属于 SpanContext 的父返回值则触发 TypeError，不是自动 root。

对于明确空 Context（或者只包含无效 SpanContext 的 Context），DEFAULT_ON 的 root 是 ALWAYS_ON，因此源码推导为新的 root、RECORD_AND_SAMPLE。父 tracestate helper 返回 None，SpanContext 构造将其换成默认空 TraceState。默认 RandomIdGenerator 的 `is_trace_id_random()` 为 true，所以此 root 的 flags 为03；这不由先前无效父的 flags 决定。[ID generator L54–72](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-sdk/src/opentelemetry/sdk/trace/id_generator.py#L54-L72)。新 root 的 trace/span ID 实际数值未知，未生成。

**无效 traceparent 不等于上述空/无效父条件。** 既有提取规则对指定拒绝分支返回传入 Context；如果传入 base 已含有效的 sampled local span，返回值仍选它，SDK 会继承它的 trace ID 并走 `local_parent_sampled`，而不是重新生成 root。反之，使用明确空 base 才能在该拒绝分支得到无有效父的上下文。此处只是把历史澄清用于 sampler 的父选择，不声称重新验证了旧22例。

## 6. 保留的边界与未回答问题

- 现有 `trace_context_1.0` 固定2021端点不变。API `TraceFlags` 明确链接 Trace Context 2，并含 random 位0x02，[API span L199–228](https://github.com/open-telemetry/opentelemetry-python/blob/14971cef9c84c2354cbaf6871090896fad0f9a1a/opentelemetry-api/src/opentelemetry/trace/span.py#L199-L228)。不新增到2021端点的 implements，也不据此判定完整符合或不符合。
- 同一 monorepo commit 的跨文件阅读不是包安装兼容性、wheel/sdist 身份、依赖部署、全规范、安全、性能、生产适用性或跨实现互通证明。没有新增 API→SDK dependency、composed-protocol 或 adoption 关系。
- 未全面审计 ratio samplers、自定义 sampler、自动 instrumentation、异步任务上下文传播、processor 扩展、metrics、logs、exporter、并发或网络；没有实际 child 状态或回调计数。
