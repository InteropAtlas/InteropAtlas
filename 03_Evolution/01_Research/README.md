# 01_Research

<!-- InteropAtlas Document Metadata v0
Document Status: research_record
Document Created At: 2026-09-01T15:04:02+08:00
Document Updated At: 2026-11-05T13:26:00+00:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: mixed
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_bw64_adm_boundary
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

- [VC2 验证职责与既有库包装层的有限对照（2026-10-31）](01_Prior_Art/vc2-verification-responsibilities-2026-10-31.zh-CN.md)：对照固定 Recommendation 三顶层算法职责与局部预检、外部委派、状态回调和失败返回；不推完整符合性或验签成功。

- [Syslog 消息组成与既有读写先例的有限覆盖对照（2026-11-05）](01_Prior_Art/syslog-message-composition-coverage-2026-11-05.zh-CN.md)：按原版 HEADER / STRUCTURED-DATA / 可选 MSG 区分格式化、文本解析与组合未知；传输分帧另列，不推无损往返或送达。

- [WoT 描述、表示与 MQTT 交互证据的跨域对照（2026-11-05）](01_Prior_Art/wot-mqtt-crossdomain-evidence-2026-11-05.zh-CN.md)：连接既有工业、语法、语义和元数据入口，保留 TD、绑定、客户端与 broker 的不同角色/版次/条件，不把图中相连当作已测设备链。

- [HLS 文本、媒体读取与定时信令的有限对照（2026-11-05）](01_Prior_Art/hls-playlist-media-signaling-2026-11-05.zh-CN.md)：区分 m3u8 文本载体、FFmpeg 选定媒体读取与可选 SCTE35-CMD 映射，保留零时长、时间绑定和实际拼接的证据边界。

- [六个覆盖维度与跨域组合证据的有限对照（2026-11-05）](03_Tests/coverage-dimension-reconciliation-2026-11-05.zh-CN.md)：将 Issue #276 的既有六维连接到 Syslog、WoT/MQTT、HLS 的机器载体、研究与实验，区分可回答的问题、组合限制与具体未知；不是全域快照或覆盖完成声明。

- [既有领域的证据问题与跨域后续研究（2026-11-05）](02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)：沿所有既有导航领域连接代表问题、接纳链、有限关系和既有证据，提出少量跨域后续研究；不是全库快照、完整率或新维护队列。

- [libbw64 与 libadm 的 AXML／音轨关联责任交接（2026-11-05）](01_Prior_Art/libbw64-libadm-handoff-2026-11-05.zh-CN.md)：固定源码区分块读取、XML／ADM 内部引用与调用方 CHNA／fmt 核对，附机器可读来源及未执行配对见证；不宣称版本配对或完整符合性。

## 与 `docs/` 的边界

- `docs/`：现在应该理解和遵守什么；
- Research：这些判断从哪里来、怎样被验证。

研究记录可以长期保留，但不应因为历史上曾经重要，就继续冒充当前正式规则。
