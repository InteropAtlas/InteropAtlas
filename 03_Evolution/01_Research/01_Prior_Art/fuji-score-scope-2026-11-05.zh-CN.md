# F-UJI 的汇总分数覆盖了哪些指标

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-source scope analysis
Document Created At: 2026-11-05T22:10:00+00:00
Document Updated At: 2026-11-05T22:10:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot / review_fuji_score_scope
  GitHub Actor: ff6962757
-->

## 研究问题与结论

现有 [research 领域问题](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md#researchfair-来源分数可以证明何种可复用性证据逐项测试与汇总分数是否相同)已经区分 R1.2 来源评估组件的七项历史观察与未执行的汇总层。本次进一步回答一个读取结果时必须分清的问题：**F-UJI 的百分比、通过数量与成熟度，是否使用同一个覆盖分母？**

固定源码给出的答案是不同。默认 0.8 配置含 17 个指标、26 个配置分值、14 个按标识推导的原则键；A2 项被注释。汇总百分比的分母来自实际传入汇总函数的结果行，并不重新检查它们是否覆盖全部配置。总体成熟度则单独对 F/A/I/R 四类平均。因此，即使某个结果报告 100%，也必须一起读取指标清单及分值分母，才能理解它覆盖的范围；不同指标集合的 100% 不能直接当成同一覆盖程度。

这是对已有研究问题的固定源码分析，**没有执行 F-UJI、pandas 汇总、采集器或服务**。下文算例是明确输入假设下的人工算术推导，实际汇总结果仍为未知。没有新增 Canonical、关系、能力、UI、Runtime、工作流或维护规则，也不改原七例及其历史结论。

## 固定来源与实际核验

IA 输入固定于 [`5931e84d3827`](https://github.com/InteropAtlas/InteropAtlas/tree/5931e84d38279f2369d4fc9a2c438e0175b04e68)，对象入口为 [`fuji`](https://github.com/InteropAtlas/InteropAtlas/blob/5931e84d38279f2369d4fc9a2c438e0175b04e68/01_State/01_Objects/fuji.yaml)。上游仍是已记录的 F-UJI 4.0.1 源码提交 `7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a`，不是线上部署状态或最新版本声明。

本次通过 GitHub 连接器重新取得六份固定完整文件，逐份核对返回 blob、原始 UTF-8 字节数、Git blob SHA-1 与 SHA256：[证据清单与配置计数](fuji-score-scope-2026-11-05.json)。仅将 YAML 当数据安全解析，并运行本研究自己编写的计数程序；没有导入、安装、构建或执行 F-UJI，也没有安装上游依赖或运行上游测试；仅使用 IA 已有的 PyYAML 解析数据。六文件核验不是完整源码树、发行包、签名或部署核验。

## 配置、执行结果与汇总之间的边界

1. [`FAIRCheck` 初始化](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/controllers/fair_check.py#L198-L208)在没有指定版本时选 `metrics_v0.8`。[`MetricHelper`](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/helper/metric_helper.py#L44-L116)读取 YAML，记录配置条目数，并按标识筛选可用指标；它不是本次运行完成情况的清单。
2. [`FAIREvaluator.set_metric/getResult`](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/evaluators/fair_evaluator.py#L69-L117)从配置读取 `total_score`，只在指标存在时调用其 `evaluate`；若没有 `self.result`，返回空字典。这里没有追查全部 evaluator 的可达输入和所有返回路径，不能据此保证默认服务恰好返回 17 行。
3. [`assess_by_id`](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/controllers/fair_object_controller.py#L127-L252)的有效 `results.append` 均由相应结果的 truthiness 守卫，然后调用 `get_assessment_summary(results)`。响应的 `total_metrics` 是 `len(results)`，不是 `MetricHelper.total_metrics`。
4. [`get_assessment_summary`](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/controllers/fair_check.py#L638-L730)从非空 `metric_identifier` 用正则提取类别和原则，读取该行的 `score`、`maturity` 与 `test_status`。它没有把传入 ID 集合与配置清单比较，也不按原则全集补零。不能把少行的结果自动当成少行都通过，亦不能把配置条目数冒充已完成数量。

上述是函数之间的静态连接，不是端到端请求成功证据。无效标识可能导致正则匹配失败，未知状态、空集合、零分母和异常数值也需要另行分析；本文的有限算例均避开这些输入，不宣称函数对任意数据具有完整验证或容错能力。

## 默认 0.8 的配置清单

下表是对固定 YAML 的实际数据解析，不是评估某个数据集的结果。

| 类别 | 配置指标数 | 配置总分 | 按标识提取的原则键 |
| --- | ---: | ---: | --- |
| F | 5 | 7 | F1、F2、F3、F4 |
| A | 4 | 7 | A1、A1.1、A1.2 |
| I | 3 | 6 | I1、I2、I3 |
| R | 5 | 6 | R1、R1.1、R1.2、R1.3 |
| 合计 | 17 | 26 | 14 个不同键 |

17 项中有 16 个显式 `fair_principle` 字段；F4 的该字段缺失，但其 `FsF-F4-01M` 标识仍可被汇总正则归到 F4。因此字段缺失不能直接当成汇总没有 F4。[A2 配置行](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/fuji_server/yaml/metrics_v0.8.yaml#L327-L344)全部被注释，未进入本次解析清单。14 只是这份配置的标识分组数，不是“已验证 14 项原则”或 FAIR 完备度分母。

[`metrics_configuration.md`](https://github.com/pangaea-data-publisher/fuji/blob/7bc65525efdca9aaaaef3bc9f96dd27a5101bb0a/metrics_configuration.md#L7-L23)说明可以删减指标/测试来限制配置，但该说明仍引用 0.6 模板。本文不据它证明任意自定义 0.8 配置在服务中可运行，也不把元数据中的指标规范 DOI 当成已重新审核其完整正文。

## 三种汇总值不能混用

- **分数百分比**：按传入的有效结果行求 `earned` 总和与 `total` 总和，再算比例；原则、类别和 FAIR 总体分别聚合。总分不是固定 26。只有传入行确实覆盖该配置、分值也匹配时，26 才能用于解释这份配置的结果。
- **成熟度**：先求每个原则/类别的行均值，正值小于 1 时置为 1，其余使用源码中的 `round`。总体只取四个类别成熟度相加再除以 4，同样把 0 与 1 之间的正值置为 1，并保留两位小数。缺类别不会缩小这个 4；这不同于按返回行数平均，也不同于按配置分值加权。
- **通过数量**：`pass/fail` 映射成 1/0，再分别 `count/sum`；未知状态映射为 `None`，`count` 统计非空值而非直接取结果列表长度。本文算例只使用这两个已知状态。通过数量不是分数比例，亦不是全配置测试或全部原则的执行数量。

### 用小算例理解分母

以下均为**人工构造的汇总输入及源码算术推导，未调用上游函数，未观察服务返回**。假定标识有效、有限非负数值、正总分、已知 pass/fail 状态，且 `input_id` 不命中旧记录中的两个特殊分支。它们不证明采集器或任一真实数据集能产生这些完整输入。

| 假设传入结果 | 分数算术 | FAIR 成熟度算术 | 通过数量算术 |
| --- | --- | --- | --- |
| 只有 R1.2 一行：1/1、成熟度 2、pass | 1/1 = 100% | R=2，其余类缺失；2/4=0.5，经分支置为 1 | 1/1 |
| 按上述 17 个配置 ID 构造行，均 earned=total、成熟度 2、pass | 26/26 = 100% | F=A=I=R=2；8/4=2 | 17/17 |
| R1.2 为 1/1、成熟度 2、pass；F1 的一项为 0/1、成熟度 0、fail | 1/2 = 50% | R=2、F=0；2/4=0.5，经分支置为 1 | 1/2 |

第一行数值与旧来源组件某些观察相同，但这里把它作为假设输入，不声称已经把历史结果传进汇总器。第二行并未验证每个 evaluator 能达到设定值；其用途仅是显示两个不同分母都能得到 100%。这些不是三项新增运行测试，也不把完整响应空间简化为这三行。

已有 Canonical 记录还说明了两个特定 `input_id` 的汇总分支。该分支只在汇总用的列表里替换 earned/maturity/status，并没有在这段函数中把 `results` 原行改为通过。因而读取者也不能用特殊汇总值覆盖逐指标证据；本次没有访问这些 URL、运行该分支或据此评价线上服务。

## 如何使用这项发现

比较两次评估前，先保留各自的 `metric_version`、`metric_specification`、实际返回的指标 ID、各项 `score.total`、`total_metrics` 及逐项结果，再分别解释百分比、成熟度和通过数量。配置清单可以用于提出完整性问题，但不能单独证明本次运行已完成它。对于 R1.2，旧七例仍只支持所选来源存在性启发式，既不代表全部 FAIR 原则，也不能凭汇总 100% 扩成元数据真实、完整或可复用的证明。

这是本研究的读取建议，不增加默认排序、通用符合性判断、新 validator、CI gate 或后续维护义务。服务是否实际返回预期结构、各配置和错误输入的行为，以及部署状态仍未验证。

## 复查方式

[只读复算脚本](fuji-score-scope-2026-11-05-reproduce.py)只校验六份固定源文件的字节并解析 YAML，不执行其中的 Python。先通过授权的只读渠道按 JSON 清单的固定 URL 取得完整文件，按脚本说明把路径中的 `/` 换成 `__` 保存到本地来源目录，然后使用 IA 已有的 PyYAML 依赖执行：

```bash
python 03_Evolution/01_Research/01_Prior_Art/fuji-score-scope-2026-11-05-reproduce.py /path/to/pinned-sources > /tmp/fuji-score-scope.json
cmp /tmp/fuji-score-scope.json 03_Evolution/01_Research/01_Prior_Art/fuji-score-scope-2026-11-05.json
```

脚本不下载、安装、导入或运行 F-UJI；这里只复算配置清单与来源身份，不把静态推论包装成已观察的汇总输出。
