# JSON-LD → RDF → SHACL：字段与选图边界实验（2026-10-21）

<!-- InteropAtlas Document Metadata v0
Document Status: experiment_record
Document Created At: 2026-10-21T05:47:56.900151+00:00
Document Updated At: 2026-10-21T05:47:56.900151+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot / main-session experimental review
  GitHub Actor: ff6962757
-->

## 结论先行

在固定软件版本和 7 个可信合成输入上，12 个预期观察全部复现，**不是 12 个数据都符合形状**。这项一次性实验说明：

1. 未映射的原始 JSON 字段可以在转换到 RDF 之前丢弃，后续 SHACL `conforms=true` 不代表原文所有字段已验证。
2. 显式只选默认图与显式合并全部图，会对同一数据集得到不同验证结果。
3. 仅在命名图中的数据，对默认图的 `targetClass` 验证可能因没有焦点节点而通过；使用 `targetNode` 仍可检出缺失属性。
4. 普通数据不符合、返回 `ValidationFailure` 和抛出异常，是不同结果，不能只看布尔值或把异常当普通报告。

这保留可复现的失败边界，不建立一般兼容关系、完整转换/验证管道、符合性认证、安全或生产推荐，也不是 IA 采用决定、实时底图或未来回归维护约定。

## 为什么与底图有关

固定知识基线为 [`b8f87ab89bc5cf463d25ed0f1a1c6df0217f689a`](https://github.com/InteropAtlas/InteropAtlas/commit/b8f87ab89bc5cf463d25ed0f1a1c6df0217f689a)。[pySHACL 先例](https://github.com/InteropAtlas/InteropAtlas/pull/478)、[PyLD 先例](https://github.com/InteropAtlas/InteropAtlas/pull/481) 和 [RDF 1.1 精确引用](https://github.com/InteropAtlas/InteropAtlas/pull/482) 使现有导航/能力查询能够找到规范、实现与条件。本实验检验这些已录资料能否支持一个有边界的具体问题，而不把共享能力或两条关系当作互通证明。

它与[旧 JSON-LD 适配探索](../01_Foundations/json-ld-fit-experiment.zh-CN.md)目标不同：这里只处理合成数据，不运行 IA Canonical 数据导出，不复核旧 RDF 1.2 映射，也不修改旧实验或其结论。实验资产不进入 Canonical loader，不依赖新页面、API、Schema 或 CI。

## 冻结输入、程序与输出

- [生成脚本](../json-ld/jsonld-shacl-produce-20261021.py)：内联上下文 → 展开 → N-Quads；显式拒绝外部文档加载，不调用进程默认 loader setter。
- [验证脚本](../json-ld/jsonld-shacl-validate-20261021.py)：N-Quads → RDFLib Dataset → 显式选图复制到 Graph → pySHACL；数据和形状均由可信内存内容解析，`do_owl_imports=False`，不提供远程文档。
- [冻结输入/中间结果](../json-ld/jsonld-shacl-produced-20261021.json)：7 个原始 JSON-LD、展开数据、N-Quads、被丢弃字段与被拒加载地址。另有一个外部上下文拒绝断言，不包含实际远程内容。
- [冻结验证结果](../json-ld/jsonld-shacl-result-20261021.json)：10 个普通验证断言、1 个返回 failure 断言、1 个异常断言，及实际依赖版本。

原始生成执行为 `2026-10-21T05:40:12.529001+00:00` 至 `05:40:12.531970+00:00`，验证为 `05:40:13.046981+00:00` 至 `05:40:13.132389+00:00`。这些是该次实验时间，不是发布、审核或软件标准核查时间。

### 具体设置与结果

普通形状针对 `ex:Person`，要求 `ex:name` 恰好一个 `xsd:string`，关闭形状且仅忽略 `rdf:type`。普通运行固定 `inference=none`、`advanced=False`、`meta_shacl=False`、`js=False`、`do_owl_imports=False`。只有最后异常例设置 `meta_shacl=True`。`targetNode` 例把目标改为固定 `ex:a`。

默认图策略仅复制 `Dataset.default_graph`；命名图不参与。union 策略显式复制 `Dataset.graphs()` 中全部三元组，Graph 以集合方式去重。这是用于对照的应用选择，不是本实验为 IA 或所有使用者制定的处理规则。

| 输入/条件 | 选图/目标 | 观察结果 |
|---|---|---|
| 有效姓名 | 默认图 / class | 符合，0 条结果 |
| 姓名为数字 | 默认图 / class | 不符合，1 条结果 |
| 缺少必需姓名 | 默认图 / class | 不符合，1 条结果 |
| 有效姓名 + 未映射额外字段 | 默认图 / class | 额外字段先丢弃，仍符合 |
| 带语言标签姓名 | 默认图 / class | 不符合 `xsd:string`，1 条结果 |
| 默认图有效、命名图有同节点无效姓名 | 默认图 / class | 符合 |
| 同一混合数据集 | 显式 union / class | 不符合，2 条结果 |
| 仅命名图有数据 | 默认图 / class | 图为空且无焦点，符合 |
| 同一仅命名图数据 | 默认图 / node | 缺少必需属性，不符合 |
| 同一仅命名图数据 | 显式 union / class | 不符合，1 条结果 |
| 约束查询含禁止的 VALUES | 默认图 | 返回 `ValidationFailure`，不是普通结果图 |
| 非法形状 + `meta_shacl=True` | 默认图 | 抛出 `ReportableRuntimeError`，无普通 conforms 结果 |

没有测试真实网络、外部上下文/导入、不可信文档、全部 W3C 测试集、任意应用图选择或 RDF 1.2。失败例也不是对上游缺陷的指控。库的进程内副作用与宿主应用影响未在本实验评估；两个阶段使用分开的进程/环境。

## 复现这一固定实验

原环境均为 Python **3.12.14**，两阶段使用不同虚拟环境。不要把下列版本清单当作生产推荐或当前最新版：

- PyLD 环境：PyLD 3.3.0、cachetools 7.2.4、frozendict 2.4.7、lxml 6.1.3。
- pySHACL 环境：pyshacl 0.40.1、rdflib 7.6.0、owlrl 7.6.2、pyparsing 3.3.3、packaging 26.3、prettytable 3.18.0、html5rdf 1.2.1、wcwidth 0.9.3。

按需要在两个隔离环境准备这些固定依赖；脚本不会安装软件或下载标准。令 `PYLD_PY` 和 `SHACL_PY` 分别指向这两个环境的 Python，仓库根目录下运行：

```bash
OUT=$(mktemp -d)
"$PYLD_PY" 03_Evolution/02_Experiments/json-ld/jsonld-shacl-produce-20261021.py "$OUT"
"$SHACL_PY" 03_Evolution/02_Experiments/json-ld/jsonld-shacl-validate-20261021.py "$OUT"
```

**必须显式给输出目录**；结果写入该目录的 `produced.json` / `result.json`，不改仓库冻结文件。缺少参数时脚本退出并显示用法。复跑会有新的真实时间；比较时仅排除两个顶层 `started_at` / `completed_at`，其余字段（包括所有输入、中间值、12 个结果与版本）应与上述冻结 JSON 相同。环境或结果不同时，应保留差异，不把它当成本次已核结果。

独立审核者在另一输出目录阅读代码后亲自重跑，输入、展开、N-Quads、全部 12 结果及依赖版本完全一致，仅真实执行时间不同。发布副本仅把私有默认输出路径改成必需的显式输出参数，未改变输入、算法、断言；该副本也已另行重跑比较。

### 四个资产的 SHA256

- `jsonld-shacl-produce-20261021.py`: `f9264c2492c66663647aa353ef8b369a518322170a92d165965f8eea22e8a306`
- `jsonld-shacl-validate-20261021.py`: `33f488ce4154de5ca97939ba2562592e25f0e9c3a380d0b1fd7c9a17d389fab0`
- `jsonld-shacl-produced-20261021.json`: `88b4bc11f9bac5d6610cf615a953addb426d3e3cbd4c12d2b6fc906d2f911ebc`
- `jsonld-shacl-result-20261021.json`: `6479ee89c69697f781344d7a0e296c7f8f8f551818f4de0e0ff780a688cbf1d3`

## 解释边界

规范背景可查 [JSON-LD 1.1 §10](https://www.w3.org/TR/2020/REC-json-ld11-20200716/#relationship-to-rdf)、[RDF 1.1 数据集](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-dataset) 与 [SHACL 验证](https://www.w3.org/TR/2017/REC-shacl-20170720/#validation)。实际结果的直接依据是上述代码、固定输入与输出，而不是仅引用规范。

本实验只支持所列条件下的观察。它不把模型引用变成传递性兼容，不决定 IA 的存储/导出/验证路线，不增加未来更新或自动执行义务，不声称底图或该领域覆盖完成。
