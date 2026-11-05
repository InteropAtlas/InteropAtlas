# WoT TD 验证资源修订与固定规范身份的有限实验

<!-- InteropAtlas Document Metadata v0
Document Status: bounded_experiment_record
Document Created At: 2026-11-05T14:17:00+00:00
Document Updated At: 2026-11-05T14:17:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_wot_final_evidence
  GitHub Actor: ff6962757
-->

## 问题与有界答案

[既有跨域研究](../../01_Research/02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)指出，工业领域的 TD 可读取，不能自动证明 JSON-LD 处理或设备交互；[#276](https://github.com/InteropAtlas/InteropAtlas/issues/276) 仍保留外部证据时效性问题。本实验进一步回答：**固定为同一个 TD 1.1 Recommendation，是否已经固定用于验证的机器资源及其行为？**

没有。新读取的[官方 TD1.1 errata](https://w3c.github.io/wot-thing-description/errata11.html)明确区分了 HTML 规范与修订的 TD/TM JSON Schema 资源。本次将同一组合成输入交给修订前后的完整官方资源，在它们声明的 Draft 7 下得到不同接受结果。变化不仅涉及 context 映射值类型，也涉及数组顺序和该方言实际识别的关键字。**规范身份、资源字节、验证器/方言和调用入口是不同证据，不能以同一个“1.1”标签代替。** 这是对本次来源和输入的判断，不新增项目维护要求。

结果不等于 node-wot 行为或 JSON-LD 符合性；没有运行 Ajv、node-wot、JSON-LD 展开、设备或 MQTT。历史 node-wot 示例已经记录 March-2025 依赖版本，本次不把它们判为使用旧资源或已失效。

## 来源身份与时间不混同

仓库背景固定为 `f29d41bc26d10b53acdadb5aa128ea8f40365938`，本轮不修改任何 Canonical 事实或核验日期。

- [官方 PR2080](https://github.com/w3c/wot-thing-description/pull/2080) 的前资源取自 `c3a03057dfa7d8b1dc0c7c25298b9908287c87e0`，后资源取自合并提交 `5af0fb099830d36fbe925256a0e81c60527623fb`。TD 与 TM 均声明 `http://json-schema.org/draft-07/schema#`；资源 version 从 `1.1-09-November-2023` 变为 `1.1-12-March-2025`。
- PR 实际于 **2025-04-01T11:10:12Z** 合并。资源版本字符串和 errata 条目的 2025-03-12 不是该合并时刻，也不自动证明 npm 包发布时刻。
- PR head 的两份 schema 与合并提交字节相同；合并父提交的两份 schema 与上述前资源字节相同。只按 PR/合并提交自身的改动核对，不把包含其他提交的宽泛 base→merge 差异全部归给 PR2080。
- 本轮读取的官方 errata 页显示最近更新 2026-08-27，仍列 Recommendation 日期 2023-12-05。本文只研究其中 2025 schema 修订，不声称复核全部 errata 或当前发布端点与选定提交字节相同。
- schema 内的 `$id` 含 main URL，但本实验只消费已核哈希的提交文件，未据此读取 main 或自动替换输入。

前后 TD/TM 原文件、PR 身份、逐文件 Git blob/SHA256、捕获方式和时间见[来源清单](../03_Evidence/wot-td-resource-probe-20261105-manifest.json)。第三方 schema 全文不镜像进仓库；固定提交与指纹用于恢复输入，不把源码读取或单次验证升级为上游完整审计。

## 相同输入下的观察

每类 schema 使用同一组 24 个 context 夹具，TD/TM 各自保留所需的最小根字段；前后资源分别运行。数目只是实验矩阵，不是领域分母或通过率。完整输入在[清单](../03_Evidence/wot-td-resource-probe-20261105-manifest.json)中；接受/拒绝及错误实例路径、原始资源 pointer 与沿引用求值 pointer 分别保留于[结果](../03_Evidence/wot-td-resource-probe-20261105-result.json)。

`old` 为 `https://www.w3.org/2019/wot/td/v1`，`new` 为 `https://www.w3.org/2022/wot/td/v1.1`，`other` 为明确的合成 URI。PR 描述中的 `/2022/wot/td/v1` 不是前后 schema 的旧 context 常量，本实验不采用那个拼写作正面对照。

| 固定输入类别 | 前资源 | 后资源 | 本次能够解释的边界 |
| --- | --- | --- | --- |
| new、old 标量及单元素数组；old→new；new→other | 接受 | 接受 | 基本对照，不证明完整 TD/TM 有效 |
| new/old/old→new 后加字符串值映射 | 接受 | 接受 | 修订没有拒绝这些对照 |
| 上述位置的数值值映射 | 接受 | 拒绝 | context 映射值约束在所选资源中改变 |
| new→old；other→new；other→old | 接受 | 拒绝 | 顺序/位置约束同样改变，不能全部归因于数值类型 |
| new 后加对象、null、布尔、数组值映射；new 或 old 后加数值尾项 | 接受 | 拒绝 | 仅描述 schema 结果；不把所有非字符串 JSON-LD 定义一概判为无效 |
| 空 context 数组；old→other→new | 接受 | 接受 | 后资源通过仍不足以证明全部规范要求 |
| 无关 URI 标量 | 拒绝 | 拒绝 | 负面对照 |

TD 与 TM 在上述 context 矩阵得到同样的接受模式；这不是两种文档在其他字段等价。每种 schema 有 12 个前接受/后拒绝的输入对，没有据此给软件排名。

两版 schema 都通过 Draft7 的 schema 检查，但旧版在两个数组分支使用 `prefixItems`。独立的方言对照确认，当前 Draft7 验证器不识别这个关键字，而识别 tuple-form `items`。PR 又加入 `additionalProperties: {type: string}` 并调整 `contains`。因此不能把所有变化归给单个关键字，也不能把 `check_schema` 成功解释成每个关键字都被执行。

本实验没有配置 format checker；这些 context 分支中的 `anyUri` 只是 string 类型条件，不是 URI 有效性证明。也没有调用 JSON-LD 处理器，尤其不能把 schema 拒绝扩展 term-definition 对象解读为这类 JSON-LD 对象普遍非法。

## 对既有 node-wot 证据意味着什么

固定 node-wot0.9.2 的 [helpers.ts](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/helpers.ts#L32-L52) 从单独的 `wot-thing-description-types` 包导入 schema，使用 `Ajv({strict:false})` 与 ajv-formats。它先深复制并[放宽指定的 required 字段](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/src/helpers.ts#L222-L252)，并不是本实验直接验证的未改动完整资源。`isThingDescription` 复用这个初始化 validator；consume/produce 又有不同调用路径。

[固定 package.json](https://github.com/eclipse-thingweb/node-wot/blob/2fd12ddf95ad9684e89d703bb916bc07e1959c79/packages/core/package.json#L23-L38) 声明 `^1.1.0-12-March-2025`；[#472 的冻结记录](https://github.com/InteropAtlas/InteropAtlas/blob/0cf0806de78ef964728b38c995dde0215dc94eae/01_State/Inbox/review-packets/node-wot-implementation-20261021.yaml#L213-L267) 已记载十五个有限 core 示例及实际解析到的同名 March-2025 TD/TM 包、Ajv8.20.0。它们不是本轮重跑，也没有因为本次发现 errata 就失效。原记录保留的版本标签与 lock 摘要没有给出当时已安装 schema 的内容哈希，因此**实际历史资源字节与 PR2080 文件是否相同仍未在本次证实**。

要对具体 node-wot 入口作新的运行判断，需要先恢复对应包字节、验证器配置与调用路径；本实验没有跨过这个边界。也不新增 implements、修改已有关系条件或把对象日期刷新为实验日期。

## 执行与复现边界

使用已有 CPython3.12.14、jsonschema4.26.0 及清单中的预装依赖，没有安装、构建或导入上游软件。脚本只读取本地经哈希检查的 schema 数据和自有夹具，输出 JSON；外部引用解析被拒绝，socket guard 的合成自测通过，实际验证没有外部检索尝试或 socket 操作。该 Python 保护不是 OS 网络隔离或安全沙箱。

按清单的固定 URL/提交读取九个输入文件，保留原始字节及 `file` 名称到单独的本地目录。四个比较端点外的文件用于核实 base/合并父节点、head/合并结果及 errata 来源；没有自动联网获取步骤。所有 fixture 已嵌入清单，不依赖额外 cases 文件。使用已具备所列依赖的环境：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105.py \
  --sources /path/to/captured-sources \
  --manifest 03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105-manifest.json \
  > /tmp/wot-td-resource-result.json
```

配方核对大小、Git blob SHA-1、SHA256、本地引用闭包和原数据未被修改，并保留所有嵌套错误。执行者重复运行的输出逐字节相同；独立复核另行核对四份比较源文件并复跑。跨环境解释器路径或模块位置可能不同，不能把环境元数据差异当作接受行为变化，也不能忽略版本/输入差异。

| 产物 | SHA256 |
| --- | --- |
| [脚本](../03_Evidence/wot-td-resource-probe-20261105.py) | `4bb70603c81b3b0ad7281104ca1e459c7ca0a95e48462d0dd4ffbf48e46de01a` |
| [清单](../03_Evidence/wot-td-resource-probe-20261105-manifest.json) | `2d193145ab96f811d90e5de6ea09046303208f3608cee8e791b78a6881b819a3` |
| [结果](../03_Evidence/wot-td-resource-probe-20261105-result.json) | `e1c7fe4b7db7c3a4a9cf469a1830636522c105765667d019631cc4ffdf79460b` |


本次缩小的是现有工业↔语法↔语义问题中“同版规范是否足以确定验证证据”的未知，不建立全域目录、实时快照、schema API、持续检查规则或新的分类。旧快照、不确定发布操作及全部既有 holds 保持不变。
