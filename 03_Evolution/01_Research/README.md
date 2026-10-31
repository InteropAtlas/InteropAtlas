# 01_Research

<!-- InteropAtlas Document Metadata v0
Document Status: research_record
Document Created At: 2026-09-01T15:04:02+08:00
Document Updated At: 2026-10-31T09:29:00+00:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / publish_fhir_exchange_coverage
  Reviewer: Independent Agent — OpenAI / dot / health_exchange_review
  GitHub Actor: ff6962757
-->

这里保存推动 InteropAtlas 演化所需的研究与分析。Research 不是当前规则本身；已经被正式采用的结论，应由 `docs/`、`01_State` 或 `02_Runtime` 中的 Primary Home 承担当前角色。

## 三个主要入口

1. [`01_Prior_Art/`](01_Prior_Art/) — 外部标准、成熟先例、Reference Map、方案比较与思想来源。
2. [`02_Audits/`](02_Audits/) — Gap、Conformance、Verification、Reference Intake、Work Package / Pilot Audit。
3. [`03_Tests/`](03_Tests/) — Fit Test、Stress Test 与非规范性对象适配测试。

它们分别回答：**我们依据什么？当前判断经得起什么审计？关键假设经过了什么测试？**

## 有限比较记录

- [OGC API Features Core 四编码类的有限覆盖比较（2026-10-31）](01_Prior_Art/ogc-features-core-encoding-comparison-2026-10-31.zh-CN.md)：对照固定规范、既有记录与 pygeoapi 静态证据，区分精确映射、相关记录和未知；不是全域完备率。

- [SenML 原版四表示族与流媒体的有限覆盖比较（2026-10-31）](01_Prior_Art/senml-representation-coverage-2026-10-31.zh-CN.md)：区分原版八媒体的协商/处理、精确引用版次、既有通用实现与专门证据 unknown；不是当前注册全集。

- [PROV 固定文献家族与有限实现证据覆盖对照（2026-10-31）](01_Prior_Art/prov-family-coverage-2026-10-31.zh-CN.md)：以 2013-04-30 的 12 文献为有界分母，区分职责、已录对象、双 PROV-O 身份 hold 与 python_prov 3.2.3 旧证据范围；不推全域完备。

- [FHIR R4 五种交换方法与既有模型库证据的有限对照（2026-10-31）](01_Prior_Art/fhir-r4-exchange-evidence-2026-10-31.zh-CN.md)：分开标准身份、INA 导航、旧内存模型观察与新只读 GET 静态路径；不推真实交换或完整符合性。

## 与 `docs/` 的边界

- `docs/`：现在应该理解和遵守什么；
- Research：这些判断从哪里来、怎样被验证。

研究记录可以长期保留，但不应因为历史上曾经重要，就继续冒充当前正式规则。
