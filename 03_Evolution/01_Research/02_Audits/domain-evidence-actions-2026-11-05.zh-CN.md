# 既有领域的证据问题与跨域后续研究

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Evidence Reconciliation
Document Created At: 2026-11-05T12:42:00+00:00
Document Updated At: 2026-11-05T14:20:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_wot_final_evidence
  GitHub Actor: ff6962757
-->

## 问题、范围与结论

底图不只需要知道“有什么”，还需要知道现有材料能回答什么、不能回答什么，以及下一步应补哪一种证据。本研究沿既有领域导航逐项选择一个有明确来源的问题，连接代表对象、接纳记录、有限关系和已有研究。它把前一份[六维对照](../03_Tests/coverage-dimension-reconciliation-2026-11-05.zh-CN.md)的提问扩展到所有现有导航领域，而不是再增加一个孤立标准或实验。

结论是：现有入口已有可追溯的标准、实现或方法证据，许多剩余问题发生在已记录部件之间的责任交接处。机械连接不等于电气互通；有效表示不等于业务正确；局部 API 行为不等于交换完成；记录关联也不等于验证组合。部分看似空缺的关系其实保留了版次或证据边界，例如 OpenTelemetry 的传播观察已经存在，但不能因此补一条针对不同 Trace Context 版次的 implements。

本文是固定基线上的代表问题研究，不是全库清单、全域当前快照或覆盖完成声明。每个领域只选一个入口，领域内其他对象和未知仍然存在；20 个领域是导航范围，不是互操作方案空间的分母，案例数也不是完整率。没有新增分类、页面、Canonical 数据、关系、维护要求、CI gate 或自动研究队列。

## 输入与阅读方法

- 仓库基线：`1539ad70b34fd06dc9b18b9e781bf16bde269b59`。当前记录链接固定于此提交，历史执行证据则保留其原冻结提交；原研究自身的取样日期、版本和限制仍适用，不声称重新验证了所有上游现状。

- 领域与成员沿用 [intake-coverage 导航](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/relations/intake-coverage-20260913.yaml) 的 draft / editorial_navigation_only 语义。candidate 表面的成员可能已经接纳；本文逐项对上当前候选、accepted event 与 Canonical 身份，不能把 candidate 导航当作尚未收录。

- 各行的“已有证据”复述所列来源；“未回答与下一步”是本次研究判断，不是已经执行的结果，也不是未来运行、联网或部署许可。静态阅读、有限内存执行、文件实验与规范声明分别保留。

- 关系链接只证明该条边的版次、条件和范围。共同导航、共同端点或本文提出的比较，不生成新的技术边；implements、uses、recommended_with 等关系不作传递闭包。

- 本次核对代表对象的导航成员、接纳链及所选关系端点；阅读当前对象和关联 packet / 研究 / 实验后再提出剩余问题。没有替代或重试任何结果不确定的历史发布，也没有解除既有 hold。

## 逐领域证据问题

### physical：同为 75 Ω BNC、机械可连接，能否据此判断 3G-SDI 链路互通？

- 入口：`canonical:smpte_st424`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/smpte_st424.yaml) → [accept-20261015-sdicore-smpte_st424](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/sdi-core-20261015.yaml) → [smpte_st424](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/smpte_st424.yaml)。

- 已有证据：不能。ST424:2012 §7.3.1–2 对优选 BNC 引用 IEC61169-8:2007 Annex A 的机械依据；超过3 GHz可用性及3 GHz回波损耗来自 ST424 自己。满足电气要求的应用专用替代连接器亦获准，不能称 BNC 必选或跨速率兼容。 已有规范条款与公开 IEC preview 的文献级核对，无设备或线缆运行验证。

- 已录关系：[smpte_st424_uses_iec_61169_8_2007_annex_a](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/sdi-bnc-mechanical.yaml)

- 未回答：在具体一对连接器、线缆长度和载荷下，哪些 ST424 电气与回波损耗条件已有器件证据，哪些只是机械吻合？

- 下一步研究判断：先用现有 ST424/IEC 边的引用范围，把机械尺寸与 ST424 §7.3.1–3 的电气验收证据分列；如要判断具体线缆组合，先取得确切器件/长度及其已有测试依据，不先补一个新标准条目或宣告互通。

- 跨域边界：本行可解释物理连接不能代替媒体交换证据；选中关系未把 ST424 接到 RTP/ST2022-6，不推导一条未记录的媒体链。 同域导航中的 ieee_802_3_family 仍为 identity_risk，需先区分工作级/整合版/修订件/勘误；这不是物理域空白。

- 证据入口：[sdi-bnc-mechanical-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/sdi-bnc-mechanical-20261024.yaml)。


### measurement：测得一个 LUFS 值是否已完成 R128 的归一化与交付判断？

- 入口：`canonical:itur_bs1770`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/itur_bs1770.yaml) → [accept-20261019-bs1770-itur_bs1770](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/bs1770-20261019.yaml) → [itur_bs1770](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/itur_bs1770.yaml)。

- 已有证据：不是。ebu_r128_uses_itur_bs1770 只记录 R128 V5 的测量算法使用，而且其引用未指定 BS1770 版次；-23 LUFS 目标不是 BS1770 自身规定。broadcast_loudness 0.5.0 边仅静态映射 48kHz/stereo/planar f32 的 Annex1 集成响度路径，既不施加增益，也不涵盖真峰值或完整 R128。 Rust 是静态映射；另一既有 C 库 libebur128 v1.2.6 已有核心构建和有限合成运行结果，不能把它再说成未运行。该库仍 object-only，没有到当前 BS1770-5/R128 V5 的 implements 边。

- 已录关系：[ebu_r128_uses_itur_bs1770](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/audio-loudness.yaml)；[broadcast_loudness_implements_bs1770_5_annex1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/loudness-measurement-implementations.yaml)

- 未回答：若要比较两个已有库在同一测量任务的结果，需要怎样对齐 PCM 布局、帧数、声道映射、门控/尾块、返回码与非有限值，才能解释差异而非把 API success 当测量有效？

- 下一步研究判断：先对照已有 Rust 静态条件与 libebur128 的实际命名观察，列明同一可信 48kHz 立体声输入的表示转换、完整400ms块、finish/返回码和预期读数依据；只对还没有共同证据的比较设计后续观察，不重跑已记录探针来制造进度。

- 跨域边界：已记录的 measurement↔editing 连接是 R128→BS1770；测量、施加增益与交付要求必须分开。 libebur128 官方 conformance suite 明确 NOT RUN；libsndfile 获取曾被拒绝/不可用，EBU音频下载涉及接受条款。不得把下载/官方套件执行列为立即授权动作，也不把合成波形等同官方向量。si_brochure_9 仍 identity_risk，具体修订及语言待固定。

- 证据入口：[broadcast-loudness-annex1-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/broadcast-loudness-annex1-20261024.yaml)；[libebur128-1.2.6-20261030.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/libebur128-1.2.6-20261030.yaml)。

- 补充实现来源：[libebur128.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/libebur128.yaml)。


### transport：HTTP/3→QUIC→TLS 的图路径是否已经证明一个可用且安全的连接？

- 入口：`candidate:quic_rfc9000`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-p0-quic_rfc9000](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/p0-core-20260913.yaml) → [quic_rfc9000](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/quic_rfc9000.yaml)。

- 已有证据：没有。http3_quic 是固定 RFC9114 对 QUICv1 的依赖；quic_tls_security 与 quic_tls_version 是文献机制关系。RFC9001 使用 RFC8446 握手/密钥派生，不承载 TLS records。aioquic1.7.0 的两条边有真实 API/源码依据，但调用方仍须驱动 I/O、定时器、事件与逐数据报目的地址；HTTP3 GOAWAY 路径不能称完整优雅关闭。 规范和固定源码/测试定义静态审阅，不是 aioquic 上游测试或远端互通执行。

- 已录关系：[http3_quic](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/p0-http-quic-relations.yaml)；[quic_tls_security](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/p0-http-quic-relations.yaml)；[quic_tls_version](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/p0-http-quic-relations.yaml)；[aioquic_implements_quic_rfc9000](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/p0-http-quic-relations.yaml)；[aioquic_implements_http3_rfc9114](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/p0-http-quic-relations.yaml)

- 未回答：一个明确请求/响应流程是否按返回地址发出每个数据报、驱动所有必需事件/定时器，并在连接关闭时正确报告未完成请求？

- 下一步研究判断：从现有 aioquic 两条 context 及同一版本内存交换测试定义梳理一个请求/响应和一个关闭路径的调用顺序、观察点与失败条件；先建立可检验配方，任何未来运行仍单列版本/依赖/信任配置，不从规范边继承部署安全。

- 跨域边界：显式跨域为 transport 的 QUIC 与 trust 的 TLS13，经 quic_tls_security/quic_tls_version 连接。 RFC9846 已于 PR551 收录；RFC8446 的 superseded 说明已在当前对象，旧 RFC9001→8446 引用保持。不要再创建“补RFC9846/修注记”工作或自动重定向关系。

- 证据入口：[aioquic-implementation-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/aioquic-implementation-20261024.yaml)。

- 补充实现来源：[aioquic.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/aioquic.yaml)；[tls13_rfc8446.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/tls13_rfc8446.yaml)；[tls13_rfc9846.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/tls13_rfc9846.yaml)。


### trust：verifyCredential 返回 verified，究竟支持哪一层验证主张？

- 入口：`candidate:vc_data_model_2.0`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-b-vc_data_model_2.0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-b-20260913.yaml) → [vc_data_model_2.0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/vc_data_model_2.0.yaml)。

- 已有证据：现有 implements 边只支持 numeric version=2.0 的未签名 presentation 构造。10月31日研究及 PR631 已将 verifyCredential 包装层静态控制流补入 digitalbazaar_vc 对象：局部预检、jsigs委派、成功后的条件状态回调和异常包装。函数名/布尔结果均不证明完整 VC2 verifier、验签成功、发行者可信或 claims 为真；规范允许调整检查顺序，不能仅因先预检判违规。 未签名构造与验证 wrapper 两批均静态，不能误称前一批已运行。suite、密钥、loader、purpose、身份/状态网络委派均未被该研究审完或执行。

- 已录关系：[digitalbazaar_vc_implements_vc2_presentation_construction](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/verifiable-credential-implementations.yaml)；[vc_data_model_2.0_uses_json_ld](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)

- 未回答：对一类明确 VC2 输入，在 §7.1 conforming-document 职责中，哪些字段已由 wrapper 检查，哪些留给委派或调用方，哪些还没有证据？

- 下一步研究判断：沿已有 §7.1 三职责矩阵与同一固定 lib/index.js 的 _checkCredential/verifyCredential 分支，选择一个输入形状，逐项标明本地检查、条件委派与未审项；不先运行密钥、身份或网络校验，也不把委派函数调用视为完成。

- 跨域边界：显式连接是 VC2→JSON-LD1.1。JSON-LD→RDF→SHACL 的旧实验至多作为“转换可丢信息”的可选研究类比，不是 VC2 必须走的规范管道，更不是 verification 替代品。 wrapper 回填已完成，下一步不是重复回填或扩大既有 implements。

- 证据入口：[vc2-verification-responsibilities-2026-10-31.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/vc2-verification-responsibilities-2026-10-31.zh-CN.md)。

- 补充实现来源：[digitalbazaar_vc.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/digitalbazaar_vc.yaml)。


### syntax：两个实现都连到 CBOR，是否足以推断字节/值无损交换或确定性编码？

- 入口：`candidate:cbor_rfc8949`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-p0-cbor_rfc8949](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/p0-core-20260913.yaml) → [cbor_rfc8949](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/cbor_rfc8949.yaml)。

- 已有证据：不足。cbor2 6.1.5 已有35项小输入核验（1版本、34行为）：loads 只取首项、Python键相等可能合并CBOR不同键，canonical=True不自动证明完整确定性profile。TinyCBOR7.1 无符号整数编码与 libcbor0.12.0 token解码是静态、有不同缓冲/生命周期约束的边；libcbor FINISHED 仅一次回调，不代表完整文档已消费。 cbor2 有有限执行；另两库选中路径均未构建或运行。三条 implements 不是互通边、替代边或完整RFC认证。

- 已录关系：[python_cbor2_implements_cbor_rfc8949](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/data-serialization-implementations.yaml)；[libcbor_implements_cbor_rfc8949](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/data-serialization-implementations.yaml)；[tinycbor_implements_cbor_uint](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/data-serialization-implementations.yaml)

- 未回答：在共同 major-type0 子集，TinyCBOR 实际写出的前缀能否由 libcbor 按相同 uint64值和精确 consumed length 接收，边界值与截断如何表现？

- 下一步研究判断：先从两条既有 context 对齐0/23/24/255/256等编码分界、实际前缀长度和 decoder read/required 预期；准备安全真缓冲及逐前缀条件，未来有限跨实现观察与已跑 cbor2 探针分开，不声称已运行。

- 跨域边界：本次所选 CBOR 关系只支持序列化实现比较，未记录到某个工业载荷/协议的可执行组合边，不制造 SenML/COSE/CWT 链。

- 证据入口：[python-cbor2-rfc8949-20261029.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/python-cbor2-rfc8949-20261029.yaml)；[tinycbor-v7.1-20261105.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/tinycbor-v7.1-20261105.yaml)；[libcbor-0.12.0-20261104.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/libcbor-0.12.0-20261104.yaml)。

- 补充实现来源：[python_cbor2.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/python_cbor2.yaml)。


### semantics：查询或形状验证成功，是否表示完整原文及全部图都已被正确理解？

- 入口：`candidate:sparql11_query_2013`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-p0-sparql11_query_2013](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/p0-core-20260913.yaml) → [sparql11_query_2013](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/sparql11_query_2013.yaml)。

- 已有证据：SPARQL 对象只指 Query Language，不含 Update/Protocol/结果格式。RDFLib7.6.0 有界边限定可信查询、预加载本地图、内置处理器且 use_store_provided=False；这不是离线/沙箱开关，上游测试定义仍有 xfail/skip。pySHACL→RDFLib 是声明/锁文件依赖，不是实机安装或完整兼容证明。既有 JSON-LD→RDF→SHACL 实验已实际说明丢未映射字段、默认图/union差异及无焦点“通过”。 RDFLib新对象边是静态；旧合成转换/验证实验有固定版本及实际结果，12个预期观察复现不等于12份数据符合。两批证据范围不同。

- 已录关系：[rdflib_implements_sparql11_query_2013](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/linked-data-and-hypertext.yaml)；[pyshacl_depends_on_rdflib](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/linked-data-and-hypertext.yaml)；[json_ld_1_1_maps_to_rdf_1_1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/linked-data-and-hypertext.yaml)；[shacl_2017_uses_rdf_1_1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/linked-data-and-hypertext.yaml)；[shacl_2017_provides_schema_validation](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/linked-data-and-hypertext.yaml)

- 未回答：一个明确应用查询需要哪些原始字段/图作为输入，所选图中是否真的存在预期焦点/结果，且是否经过了未审外部加载或处理器路径？

- 下一步研究判断：复用旧 produced/result 资产做逐字段、逐图的责任对照，再选一个未被现有观察回答的可信查询；先明确默认图/命名图与禁止外部加载边界，不重做旧12观察，也不触发IA RDF导出/验证路线决定。

- 跨域边界：显式语义连接为 JSON-LD→RDF1.1、SHACL→RDF1.1 与 schema_validation 能力，以及 pySHACL→RDFLib；可帮助 syntax 输入保留问题，不推导任意两库兼容。 PROV-O及其他hold不参与本次动作；不改旧RDF1.2映射。

- 证据入口：[rdflib-implementation-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/rdflib-implementation-20261024.yaml)；[jsonld-shacl-boundary-probe-2026-10-21.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/02_Experiments/03_Evidence/jsonld-shacl-boundary-probe-2026-10-21.zh-CN.md)；[jsonld-shacl-result-20261021.json](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/02_Experiments/json-ld/jsonld-shacl-result-20261021.json)。


### services：事件被构造或JSON编解码成功，是否保留载荷、扩展类型与发生时间语义？

- 入口：`candidate:cloudevents_1.0.2`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-service-methods-cloudevents_1.0.2](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/service-methods-20260913.yaml) → [cloudevents_1.0.2](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/cloudevents_1.0.2.yaml)。

- 已有证据：核心要求支持JSON事件格式，不表示所有data必须JSON；二进制可走data_base64。source是非空URI-reference且不可据此断言可抓取或可信；time可省略、存在时RFC3339，不保证时钟/真实发生时刻。Kotlin v0.2.0 的1.0.2边是静态受限内存路径，扩展decode只恢复string/int32/bool；JS10.0.0已有16个本地观察，但官方1.0/源码1.0.1及wire1.0不能自动变成1.0.2 implements。 Kotlin仅静态，缺settings.gradle.kts且曾403，不绕过；JS有历史本地执行，不等于跨SDK或网络投递。

- 已录关系：[cloudevents_1.0.2_uses_json](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[cloudevents_1.0.2_uses_uri](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[cloudevents_1.0.2_uses_rfc3339](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[cloudevents_kotlin_sdk_implements_cloudevents_1_0_2](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/cloudevents-sdk-implementations.yaml)

- 未回答：在一个指定应用事件中，缺省data、JSON null、二进制carrier、超过安全整数范围的数值及扩展类型需要保留什么；两个既有路径的共同子集在哪里？

- 下一步研究判断：先把选中事件的载荷/扩展类型与time需求，对到Kotlin已有encode/decode分支和JS既有16例结果/精度限制；列出可静态判明的变化与仍需独立消费者观察的项，不补JS→1.0.2边、不重试403或据默认time推真实时刻。

- 跨域边界：明确跨域路径是 services→syntax 的 JSON/URI，以及 services→measurement 的 RFC3339；只表达各自文献条件，不等同消息送达、时间同步或生产者可信。 JS版次资料不足以证明1.0.2符合性，但这也不是证明它不符合1.0.2；本次维持既有object-only/无该implements边，不作符合或不符合裁决。

- 证据入口：[cloudevents-kotlin-json-20261029.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/cloudevents-kotlin-json-20261029.yaml)；[cloudevents-javascript-sdk-20261021.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/cloudevents-javascript-sdk-20261021.yaml)。

- 补充实现来源：[cloudevents_javascript_sdk.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/cloudevents_javascript_sdk.yaml)；[cloudevents_kotlin_sdk.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/cloudevents_kotlin_sdk.yaml)。


### agents：支持JSON-RPC或列出MCP协议版本，是否已证明工具调用可互通？

- 入口：`candidate:mcp_2025_11_25`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-a-mcp_2025_11_25](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-a-20260913.yaml) → [mcp_2025_11_25](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/mcp_2025_11_25.yaml)。

- 已有证据：MCP2025-11-25增加请求ID非null及同发起方/会话内不复用等要求；JSON-RPC批处理不能自动变成宿主许可。Schema无$schema时按2020-12，双方须支持默认方言，显式其他方言需按声明处理。SDK1.26.0已有13个纯内存历史观察，但客户端/服务端仍有版本/能力协商；Tasks在固定版文档中为实验API。 历史13例有限执行与之后固定源码边界说明分开；未证明全部传输、第三方互通、授权配置或持久任务。

- 已录关系：[mcp_jsonrpc](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/agent-protocol-messages.yaml)；[jsonrpc_2_0_uses_json_rfc4627](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/agent-protocol-messages.yaml)；[mcp_uses_json_schema_2020_12](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[mcp_python_sdk_implements_mcp_2025_11_25](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/agent-protocol-implementations.yaml)

- 未回答：一个工具的实际inputSchema省略方言、声明支持方言或声明不支持方言时，固定双方会在哪个调用边界验证并报告错误？

- 下一步研究判断：沿现有协议两条uses与SDK固定client/server session源码，先追一个工具schema从声明到验证/错误返回的路径，并核历史13例是否已经覆盖；只补尚无证据的分支，不把JSON-RPC库当MCP端点，不改Agent治理或SDK能力范围。

- 跨域边界：显式 agents↔syntax：MCP→JSON-RPC2.0→历史RFC4627，以及MCP→JSON Schema2020-12；uses不传递为实现符合性。 A2A身份/任务存储与已完成注记不作为待补；不解决持有的身份/范围议题。

- 证据入口：[mcp-python-sdk-implementation-20261021.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/mcp-python-sdk-implementation-20261021.yaml)。

- 补充实现来源：[mcp_python_sdk.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/mcp_python_sdk.yaml)。


### industrial：TD可以读取且图上连到MQTT，是否已有可工作的设备交互链？

- 入口：`candidate:wot_td_1.1`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-b-wot_td_1.1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-b-20260913.yaml) → [wot_td_1.1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/wot_td_1.1.yaml)。

- 已有证据：11月5日研究已回答“尚未”。node-wot0.9.2 core历史15例无网络，不证明JSON-LD或设备交互。MqttBrokerServer选中路径须protocolVersion=5、selfHost=false并连外部broker，不是broker实现；Paho2.1.0需显式MQTTv5和网络循环，Mosquitto2.1.2所选边止于active-session SUBSCRIBE处理与SUBACK入队。 新的研究是静态；历史core示例没有重跑；没有共同端到端MQTT观察。

- 已录关系：[node_wot_implements_wot_td_1_1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/wot-implementations.yaml)；[node_wot_uses_mqtt_5_0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/wot-implementations.yaml)；[paho_mqtt_python_implements_mqtt_5.0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/mqtt-implementations.yaml)；[eclipse_mosquitto_implements_mqtt5_subscribe_path](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/mqtt-implementations.yaml)；[wot_td_1.1_uses_json](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[wot_td_1.1_uses_json_ld](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[wot_td_1.1_uses_uri_rfc3986](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[wot_td_1.1_uses_json_pointer_rfc6901](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[wot_td_1.1_uses_bcp47_rfc5646](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)

- 未回答：一个TD form的href/op、主题/负载与具体MQTT5绑定配置能否一一对应到参与者实际成功/失败观察？

- 下一步研究判断：先在既有fixed-source form/绑定路径中选一条业务交互，追配置进入绑定、主题/负载及SUBACK理由码到调用方的位置；只有需要实际链时再固定已授权broker/参与者及认证ACL，不能现在启动设备/网络或以图可达代替运行。

- 跨域边界：显式 industrial↔syntax/semantics/metadata：TD的JSON、JSON-LD、URI、Pointer和BCP47五条uses；JSON-LD可选处理、URI base不作用于@context、三类Pointer根不同，不能被MQTT成功代验。 MQTT仍是industrial导航，不擅添transport类别。OPC UA身份风险、NMOS等hold不在该动作。

- 证据入口：[wot-mqtt-crossdomain-evidence-2026-11-05.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/wot-mqtt-crossdomain-evidence-2026-11-05.zh-CN.md)；[coverage-dimension-reconciliation-2026-11-05.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/03_Tests/coverage-dimension-reconciliation-2026-11-05.zh-CN.md)。


### observability：追踪上下文已经能提取/注入，是否就意味着一次服务操作会生成并导出对应span？

- 入口：`candidate:trace_context_1.0`；[候选](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-b-trace_context_1.0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-b-20260913.yaml) → [trace_context_1.0](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/trace_context_1.0.yaml)。

- 已有证据：不是，但本域已有实质传播执行证据。opentelemetry_python_api1.45.1原接纳已运行22个可信内存carrier/context示例，含有效回环、无效/未来版本、flags03、tracestate错误/重复/上限、getter大小写/自定义适配、保留context/旧carrier、no-op及手工无效SpanContext。10月30日静态澄清又明确：extract某些拒绝分支返回传入context，inject条件写入且不清旧字段，复用前应清propagator.fields。TraceFlags链接Trace Context2并支持random位0x02，因此未接纳到固定2021 Trace Context端点的implements，缺边是有意版次边界。另一个opentelemetry_python_sdk1.45.1已有独立静态批处理记录：sampled筛选、队列/丢弃、export回调及flush/shutdown限制；不是这22例的SDK运行，也不能把传播成功推成导出或送达。 API22例是已完成的有限内存执行，当前extract/inject补充是之后静态澄清；SDK是独立的固定源码批处理证据，未运行。固定2021规范身份、API采用TraceContext2 flags的版次边界与两包证据分别保留。原22例已涵盖context保留、旧carrier和getter适配，不能把这些泛称为未验证再重做。

- 已录关系：本行不以缺边推断缺少实现或传播证据。

- 未回答：对已提取的一个明确remote SpanContext，在选定SDK sampler与parent上下文配置下，哪一步决定创建的子span是否recording/sampled并进入已审批处理路径？API载体flags保留、SDK采样决策、on_end入队是不同观察，现有22例及SDK批处理静态片段没有共同回答这条衔接。

- 下一步研究判断：先把API原22例和extract/inject澄清接回研究，明确2021规范与TraceContext2/random位0x02不混同。然后只读同一固定1.45.1版本中从提取的parent-context到SDK start_span/sampler选择、再到已审on_end/sample筛选的调用链，选定一个sampled与一个unsampled输入标明责任和未审段；该sampler衔接是新问题，不重复旧22例、不运行SDK线程/导出/网络，也不补到2021端点的implements或推定符合/不符合。

- 跨域边界：Trace Context对象明确HTTP跨服务传播，API对象提供实际文本carrier证据；这可为transport/services的请求上下文提供研究入口。API→SDK的采样/导出衔接目前只是本次提出的组合研究问题，不是现有技术边或已经验证的跨包管道。 Syslog11月5日研究明确排除TraceContext/OpenTelemetry，不能用Syslog结果替代以上独立证据；当前缺TraceContext2021边不等于缺传播实现或传播运行证据。

- 证据入口：[continuous-b-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/continuous-b-20260913.yaml)；[syslog-message-composition-coverage-2026-11-05.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/syslog-message-composition-coverage-2026-11-05.zh-CN.md)；[opentelemetry-api-implementation-20261021.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/opentelemetry-api-implementation-20261021.yaml)；[otel-sdk-batchspan-20261101.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/otel-sdk-batchspan-20261101.yaml)。

- 补充实现来源：[opentelemetry_python_api.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/opentelemetry_python_api.yaml)；[opentelemetry_python_sdk.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/opentelemetry_python_sdk.yaml)；[原执行 packet](https://github.com/InteropAtlas/InteropAtlas/blob/d453849f9510a2c575642a33ec50b77bf031f36d/01_State/Inbox/review-packets/opentelemetry-api-implementation-20261021.yaml)。


### media_network：libSRTP 的包保护合同能证明哪些媒体安全行为？README 的 >65k 与头文件 <32768 重排表述如何区分？

- 入口：`canonical:cisco_libsrtp`；[cisco_libsrtp](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cisco_libsrtp.yaml) → [accept-20261022-libsrtp-cisco-libsrtp](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/libsrtp-implementation-20261022.yaml) → [cisco_libsrtp](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/cisco_libsrtp.yaml)。

- 已有证据：2.8.1 固定源码仅核对文档/API/CMake。protect/unprotect 要求调用方初始化、策略、密钥、对齐缓冲区及尾部容量；成功和认证/重放错误须区分。两处重排表述不一致，尚未运行任何包处理；已完成的可见范围补充不是运行验证。

- 已录关系：[cisco_libsrtp_implements_srtp_rfc3711](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/media-transport-implementations.yaml)；[srtp_rfc3711_secures_rtp_rfc3550](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/media-transport.yaml)

- 未回答：固定版本的序号回卷、包索引估计及 replay-window 代码和上游测试，分别对应哪种乱序情景？现有文档不能选择一个普适阈值。

- 下一步研究判断：先对同一提交追踪 ROC/index estimation 与 replay 检查的实际代码和已有测试，建立两种表述的条件对照。仅在得到精确输入前提后再评估离线合成包实验；不处理真实流、密钥、握手或改安全设置。停止于有限行为解释，不能替上游裁决通用安全阈值。

- 跨域边界：srtp_rfc3711 在 trust 与 media_network 双重导航；cisco_libsrtp_implements_srtp_rfc3711 只到 SRTP 包处理，srtp_rfc3711_secures_rtp_rfc3550 只到固定规范机制。RTP 同时属于 transport/media_network，不能传递成完整 WebRTC/RTSP 实现。

- 证据入口：[libsrtp-implementation-20261022.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/libsrtp-implementation-20261022.yaml)；[关联研究](https://github.com/InteropAtlas/InteropAtlas/pull/514)。


### image_color：同库 Opus 包操作已测到哪里，是否已证明规范解码或跨实现互通？

- 入口：`canonical:libopus`；[libopus](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/libopus.yaml) → [accept-20261030-libopus-1-6-1-libopus](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/libopus-1.6.1-20261030.yaml) → [libopus](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/libopus.yaml)。

- 已有证据：1.6.1 固定 scalar/floating-point 配置中五个启用 CTest 与81个命名探针组已执行；这些集合重叠，不可相加。padding 后包被解码；unpad 后包及 repacketizer 抽取的第二帧只检查了解析时长。RFC8251 外部向量未运行；没有新增 RFC implements 技术边。

- 已录关系：此处保留对象级证据，不补推 implements。

- 未回答：已经抽出的第二帧及 unpad 输出，直接送入独立初始化的同版本 decoder 后，是否返回相应每声道 sample 数及明确状态？现有解析时长不能替代这一步。

- 下一步研究判断：复用固定 1.6.1 源码、配置和已存可信合成输入，设计小型增量探针直接解码上述两个输出并记录结果/失败。只补这个未测阶段，不重跑81组当新覆盖；规范外部向量可作为另一个后续问题，不能用同库结果代替。

- 跨域边界：现有 image_color 导航也收录 opus_rfc6716 和经 accepted 回指的 opus_updates_rfc8251；libopus 记录明确区分 raw Opus、Ogg 文件及 RTP 传输，本对象没有已验收的 Opus→RTP 技术边。 把包边界研究连接媒体传输是研究关联，不是已有 libopus/RTP 互通事实。

- 证据入口：[libopus-1.6.1-20261030.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/libopus-1.6.1-20261030.yaml)。


### editing：音频块写回成功，能否证明 ADM 内容和 CHNA 音轨引用有效？

- 入口：`canonical:ebu_libbw64`；[ebu_libbw64](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/ebu_libbw64.yaml) → [accept-20261020-audio-library-ebu_libbw64](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/audio-library-implementations-20261020.yaml) → [ebu_libbw64](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ebu_libbw64.yaml)。

- 已有证据：0.10.0 的小文件实测已显示：96000→30464 writer 参数窄化、部分 PCM32 相邻值合并、AXML 可保存含 NUL 非 XML 字节、单声道 CHNA trackIndex=99 可被接受。默认构建失败与带单一 Catch 诊断宏的通过须分开。#583 已做这些边界；未验证 libadm 配对。

- 已录关系：[libbw64_recommended_with_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/audio-library-implementations.yaml)；[bw64_uses_adm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/audio-file-metadata.yaml)

- 未回答：当 libbw64 提取的 AXML 交给固定 libadm 0.14.0 时，哪些例在 XML/ADM 层失败，哪些仍需调用方验证 CHNA 与音轨对应？

- 下一步研究判断：先沿已记录 recommended_with 研究两个固定版本的接口和最小支持子集，再准备小型合成音频/AXML/CHNA 配对试验，逐层记录块读取、XML 解析、ADM 结构和音轨关联的结果。新问题是配对边界，不重复 #583 四个已知反例或改变写入实现。

- 跨域边界：libbw64_recommended_with_libadm 是 editing 库到 metadata 库的显式文档建议；未指定 libadm 版次，不是已测0.10.0/0.14.0兼容配对。另有 bw64_uses_adm 文献关系，BS.2088-2 的未注明日期 BS.2076 引用不能升级为专门 BS.2076-3 兼容。

- 证据入口：[audio-library-implementations-20261020.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/audio-library-implementations-20261020.yaml)；[关联研究](https://github.com/InteropAtlas/InteropAtlas/pull/583)。

- 补充实现来源：[ebu_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ebu_libadm.yaml)。


### metadata：ADM XML 处理库支持哪些具体元数据结构，遇到未知或缺失子元素会怎样？

- 入口：`canonical:ebu_libadm`；[ebu_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/ebu_libadm.yaml) → [accept-20261020-audio-library-ebu_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/audio-library-implementations-20261020.yaml) → [ebu_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ebu_libadm.yaml)。

- 已有证据：固定0.14.0只在 README/CHANGELOG 层核实身份和限制：若干 BS.2076-2 功能、修订可能滞后、部分子元素缺失、不支持 S-ADM。现记录没有 libadm 构建、XML实例或配对实验；#456 的接纳审查不是从未验证，#583 的 libbw64 实测不能转嫁给 libadm。

- 已录关系：[libbw64_recommended_with_libadm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/audio-library-implementations.yaml)；[bw64_uses_adm](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/audio-file-metadata.yaml)

- 未回答：针对一个明确、受支持的 ADM 音轨标识子集，parser/write 路径保留、拒绝或省略哪些字段？库级处理和 CHNA 跨文件引用验证的责任边界在哪里？

- 下一步研究判断：沿固定0.14.0源码查一个具体音轨标识/XML读写路径并锚定输入前提，随后与 editing 行共用同一配对实验设计，而不是独立造第二个任务。未知元素与缺失元素必须先从源码找出准确可测问题，不能泛称库能验证全部ADM。

- 跨域边界：显式 libbw64→recommended_with→libadm 连接 editing 与 metadata；itur_bs2088_bw64 同时在 editing/metadata 导航，bw64_uses_adm 则是标准文献层关系。

- 证据入口：[audio-library-implementations-20261020.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/audio-library-implementations-20261020.yaml)；[关联研究](https://github.com/InteropAtlas/InteropAtlas/pull/456#issuecomment-6295510150)。


### research：FAIR 来源分数可以证明何种可复用性证据，逐项测试与汇总分数是否相同？

- 入口：`candidate:fair_principles_2016`；[fair_principles_2016](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-service-methods-fair_principles_2016](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/service-methods-20260913.yaml) → [fair_principles_2016](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/fair_principles_2016.yaml)。

- 已有证据：FAIR 是2016指导原则论文，不是软件符合性规范。F-UJI4.0.1 uses FAIR；固定0.8配置的7个离线 R1.2例已执行：creator:null 或已识别 PROV/PAV namespace 可通过，related-only 未通过。完整采集、控制器和汇总未执行。固定汇总代码对两个指定 input_id URL 有 earned/total、maturity/status 特例；这已记录为源码事实，不是已运行结果。

- 已录关系：[fuji_uses_fair_principles_2016](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/fair-assessment-software.yaml)

- 未回答：同一组原始逐指标结果经过 get_assessment_summary 后，在普通 input_id 与源码中特例 input_id 条件下如何变化？这一未执行层不能由原7个evaluator例推断。

- 下一步研究判断：先把既有固定控制器的输入/输出依赖追清，再设计纯离线、可信合成逐指标结果的汇总探针；input_id 仅作为字面字符串，不访问任何 URL。比较原始结果和汇总字段，保持7例为旧证据，不扩大为完整FAIR测量或验证来源真实性。

- 跨域边界：FAIR同一candidate/accepted/canonical对象同时属于 metadata 与 research；fuji_uses_fair_principles_2016 是实际方法使用边，不是 implements；PROV namespace识别不建立 PROV-O 图符合性关系。

- 证据入口：[fuji-fair-assessment-20261029.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/fuji-fair-assessment-20261029.yaml)；[fair-indexed-evidence-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/fair-indexed-evidence-20260913.yaml)。

- 补充实现来源：[fuji](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/fuji.yaml)。


### design：axe 的零 violations 能证明整个界面可访问吗，选项和呈现状态如何改变结论？

- 入口：`canonical:axe_core`；[axe_core](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/axe_core.yaml) → [accept-20261024-axe-core-accessibility](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/axe-core-accessibility-20261024.yaml) → [axe_core](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/axe_core.yaml)。

- 已有证据：4.14.0 只有固定源码/API阅读。passes、violations、incomplete、inapplicable 分开；未呈现区域需要激活另测，视觉隐藏但呈现的内容并非全排除。target-size 虽有 WCAG2.2 标签但默认 disabled；page-level 规则要求页面上下文，JSDOM不支持color-contrast。provides边只是有界测试能力。

- 已录关系：[axe_core_provides_accessibility_conformance_testing](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/accessibility-implementations.yaml)

- 未回答：固定 target-size 规则在默认、显式rule/tag选择及不同呈现状态下，实际报告的执行/结果分组是什么？标签存在不等于本次执行。

- 下一步研究判断：设计一个离线受控浏览器fixture，固定版本和同一布局，只改变规则选择或状态，一次验证这一分歧并存真实结果。禁止把 JSDOM 的无结果解释为对比度通过，也不改IA页面/CI或宣布网站符合性。

- 跨域边界：axe_core_provides_accessibility_conformance_testing 连到已有能力；其来源明确连接 WCAG2.2 §5.2 的全页面/完整流程要求。没有据标签形成 axe implements WCAG/ACT/WAI-ARIA 边。 与 editing 的字幕呈现可做“已显示/已检查≠完整语义与可访问性”的研究比较，但当前无 axe↔imscJS 技术关系，本行不宣称存在。

- 证据入口：[axe-core-accessibility-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/axe-core-accessibility-20261024.yaml)；[human-interface-standards-baseline.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/human-interface-standards-baseline.zh-CN.md)。


### collaboration：Git 的引用公告是否就是完整仓库清单，ref-prefix 能作为访问权限过滤吗？

- 入口：`canonical:git_software`；[git_software](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/git_software.yaml) → [accept-20261031-git-lsrefs](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/git-lsrefs-20261031.yaml) → [git_software](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/git_software.yaml)。

- 已有证据：Git2.52.0固定源码仅覆盖已选v2的服务端 ls-refs。ref-prefix是优化，65536条及以上清空前缀优化；hideRefs/namespace和unborn配置影响结果；stdout pkt-line/flush不证明对端接收。与Git2.51.0只有ls-refs文档段相同，不是全文或版次等同。未执行该Git源码。

- 已录关系：[git_software_implements_git_v2_ls_refs](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/git-implementations.yaml)

- 未回答：在固定版本的新合成仓库中，unborn配置、symrefs/peel及prefix条件对应的真实stdout响应是什么？现有代码阅读不能替代执行证据。

- 下一步研究判断：先取现有 t/t5701-git-serve.sh 中相关最小配方，评估隔离配置的新合成仓库和stdio输入/输出探针。只验证公告格式/条件，不启网络、fetch/push、真实仓库、身份凭证或安全隔离保证；不把它变成协作规范改革。

- 跨域边界：git_software是collaboration实际导航成员，git_software_implements_git_v2_ls_refs 明确连到 transport 导航中的 git_protocol_v2。只记录有限协议子功能，非完整Git/v2互通。

- 证据入口：[git-lsrefs-20261031.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/git-lsrefs-20261031.yaml)。


### geospatial：OGC Core、可选编码声明和实际HTTP响应分别证明什么？

- 入口：`candidate:ogc_api_features_17_069r4`；[ogc_api_features_17_069r4](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-c-ogc_api_features_17_069r4](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-c-20260913.yaml) → [ogc_api_features_17_069r4](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ogc_api_features_17_069r4.yaml)。

- 已有证据：固定17-069r4/1.0.1 Core仅发现/GET读取；HTML、GeoJSON、GML-SF0/SF2是可选编码。pygeoapi0.24.0只有静态路由/provider证据；CSV/GeoJSON不应用datetime/sortby。#617已补GML profile文献对象及边，#618已补GDAL有限转换记录，不能继续称这两个intake待做。/conformance静态URI与links的媒体类型不能证明真实响应header或全部输出合规。

- 已录关系：[pygeoapi_implements_ogc_api_features_core](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/ogc-api-features-implementations.yaml)；[ogc_features_core_1_0_1_uses_geojson_rfc7946](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/geospatial-representation.yaml)；[ogc_features_core_1_0_1_uses_rfc3339](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/geospatial-representation.yaml)

- 未回答：同一固定pygeoapi配置、同一个合成feature请求下，默认、f=json和Accept协商实际返回的Content-Type、Feature/id和links是什么？既有研究没有执行这一层。

- 下一步研究判断：复用研究列出的formats/API/itemtypes路径，准备一个本地、无网络provider的测试客户端/合成响应矩阵，比较请求选择、response header和body。先只验证有限资源/配置；不宣布GeoJSON类完整符合性、GML支持或CRS/反经线正确。

- 跨域边界：ogc_features_core_1_0_1_uses_geojson_rfc7946（仅可选§8.3）、uses_rfc3339和uses_gml_simple_features均为实际文献边，连接表示/时间；pygeoapi implements只限定GET切片。 与FHIR/UBL的结构与领域语义边界比较是研究关联，不存在三领域之间的互通技术边。

- 证据入口：[ogc-features-core-encoding-comparison-2026-10-31.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/ogc-features-core-encoding-comparison-2026-10-31.zh-CN.md)；[pygeoapi-features-core-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/pygeoapi-features-core-20261024.yaml)。

- 补充实现来源：[pygeoapi](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/pygeoapi.yaml)。


### health：FHIR模型对象能够构造，是否证明read/GET交换路径已经成功？

- 入口：`candidate:fhir_r4_4.0.1`；[fhir_r4_4.0.1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-c-fhir_r4_4.0.1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-c-20260913.yaml) → [fhir_r4_4.0.1](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/fhir_r4_4.0.1.yaml)。

- 已有证据：R4固定4.0.1含不同成熟度内容。python_fhirclient4.4.0已有21项合成内存模型观察；#628已把read→request_json→_get→session.get→res.json→model静态连接写入现有对象，该链仍未经执行。JSON表示、模型合法性、profile/术语及远程交换是不同判断。

- 已录关系：[fhir_r4_4_0_1_uses_json_rfc8259](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/healthcare-representation.yaml)；[python_fhirclient_implements_fhir_r4_models](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/data-serialization-implementations.yaml)

- 未回答：在只用合成响应的受控session下，read怎样处理成功JSON、HTTP错误和JSON解码错误？这条调用链的执行结果不能由旧21项模型观察推断。

- 下一步研究判断：先从固定server.py与fhirabstractresource.py定义最小fake-session协议，再设计完全离线、无凭证/真实健康数据的成功与两类错误观察，标明模拟的是客户端路径而非FHIR服务器互通。不得重跑、编辑或重新包装#672的lenient-model披露；如与该held变更范围相交则停止询问。

- 跨域边界：fhir_r4_4_0_1_uses_json_rfc8259 明确连到syntax；python_fhirclient_implements_fhir_r4_models只限模型映射。研究中的GET链不是新的已验收网络implements边。 与commerce/geospatial比较“解析、模型、交换”证据层是研究者关联，不是领域或实现互通关系。

- 证据入口：[fhir-r4-exchange-evidence-2026-10-31.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/01_Research/01_Prior_Art/fhir-r4-exchange-evidence-2026-10-31.zh-CN.md)；[python-fhirclient-implementation-20261021.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/python-fhirclient-implementation-20261021.yaml)；[关联研究](https://github.com/InteropAtlas/InteropAtlas/pull/628)。

- 补充实现来源：[python_fhirclient](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/python_fhirclient.yaml)。


### commerce：UBL的XML/XSD通过是否等于业务单据有效，模型库的validate调用是否一定实际启用schema？

- 入口：`candidate:ubl_2.3`；[ubl_2.3](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/candidates/cross-domain-intake-20260913.yaml) → [accept-20260913-continuous-c-ubl_2.3](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/acceptance-events/continuous-c-20260913.yaml) → [ubl_2.3](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ubl_2.3.yaml)。

- 已有证据：UBL2.3 uses固定XML1.0第二版和XSD2004两部分；#488的5个合成例已证明空AccountingSupplierParty/Note可XSD有效却违反IND5，非法日期与坏XML产生不同错误。ph-ubl23 10.2.1仅静态核对Java模型/XML及可配置XSD路径；DEFAULT_USE_SCHEMA=true可被全局或实例更改，无 schema 时 validate 警告后仍尝试 wrap/marshal，自定义处理或 JAXB 错误仍可能导致失败。Java/Maven未执行。

- 已录关系：[ubl_2_3_uses_xml_1_0_second_edition](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[ubl_2_3_uses_xml_schema_structures_2004](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[ubl_2_3_uses_xml_schema_datatypes_2004](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/protocol-data-representation.yaml)；[ph_ubl23_implements_ubl_2_3](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/02_Relations/ubl-implementations.yaml)

- 未回答：固定ph-ubl23/ph-jaxb组合在schema开启/关闭时，对相同合成Invoice会产生哪些返回、异常或warning？这是库调用行为，不是尚未证明的“XSD≠IND5”命题。

- 下一步研究判断：在固定Java/JAXB依赖与离线schema闭包可满足后，沿现有Invoice factory和setUseSchema设计小型开/关对照，并单独记录XML生成、XSD执行与结果。复用#488作为已知对照，不重复或改写实验，不创建通用UBL/税务/Peppol验证器。

- 跨域边界：ubl_2_3_uses_xml_1_0_second_edition 与两个XSD关系连接syntax；ph_ubl23_implements_ubl_2_3是有界模型/XML路径，不是全UBL符合性。xmlschema自身不是据此就implements UBL。 与FHIR/OGC的分层保证比较可复用同一研究问题，但不新建跨域技术边。

- 证据入口：[ubl-xsd-boundary-probe-2026-10-21.zh-CN.md](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/02_Experiments/03_Evidence/ubl-xsd-boundary-probe-2026-10-21.zh-CN.md)；[ubl-xsd-result-20261021.json](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/03_Evolution/02_Experiments/03_Evidence/ubl-xsd-result-20261021.json)；[ph-ubl23-implementation-20261024.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/Inbox/review-packets/ph-ubl23-implementation-20261024.yaml)。

- 补充实现来源：[ph_ubl23](https://github.com/InteropAtlas/InteropAtlas/blob/1539ad70b34fd06dc9b18b9e781bf16bde269b59/01_State/01_Objects/ph_ubl23.yaml)。


## 从分散问题收敛到可执行研究

以下是本次对证据收益的判断，不是排期、项目规范或新增维护合同。没有必要为上述每一行创建一个实验；优先复用已完成的观察，先检查部件之间尚未核对的衔接。

1. **CloudEvents 的一个事件如何跨表示保留含义。** services 行已经连接 URI、RFC3339、JSON 和两个实现的不同证据。下一份有限比较可以选择缺省、null、二进制、扩展类型与时间字段，直接对照既有 JavaScript 执行观察和 Kotlin 静态路径，先明确哪些差异已知、哪些需要新输入。收益是回答表示与解释之间的共同问题，不再添加对象。交付边界是一组固定字段的证据对照；不重试已有依赖下载限制，不把 SDK 版本声明升级为完整 1.0.2 符合性，不据此新增 implements。
2. **libbw64 与 libadm 的推荐配合究竟在哪里交接。** editing 与 metadata 是同一个后续问题，不应拆成两个补例任务。已有 recommended_with 是工作级引用，不证明当前固定版本配对；libbw64 已执行的块保存/精度反例与 libadm 静态支持范围不能相加为有效 ADM。先核对固定版本的 XML 读写接口和最小输入，明确原始 AXML 字节、XML 解析、ADM 对象与音频轨道关联各阶段责任。只有这些条件确定后才评估一份合成文件实验；停止于该输入和版本，不重跑旧反例冒充新增覆盖。
3. **FHIR、OGC Features 与 UBL 的结构证据距离实际交换还有多远。** 三者分别已有模型、provider、schema/序列化路径。可以共享一个研究问题：同一输入在哪个接口被接受、修改、拒绝，哪个输出才表示真实交换结果？它们不是互相兼容的协议栈，也没有新增三者之间的关系。先逐段引用已审调用链与已有反例，区分 HTTP 状态/媒体类型、JSON 解码、模型检查、XSD 与业务规则。可选的新证据应是一个严格离线的合成边界用例；不使用健康数据、真实账单或远端服务，不改 held 可见摘要。

其他领域的下一步不因此失效。例如 WoT 的 form→绑定→broker 角色和 OTel 的 parent→sampler→on_end 衔接同样值得研究，但先与已经完成的静态材料和执行案例去重；F-UJI 的 evaluator→summary 也是方法证据问题，不应因为它不是协议实现而视为空白领域。

## 仍然不能据此声称什么

- 这些选择没有列出各领域的所有标准、实现、关系、版本或替代方案。实际覆盖缺口仍需明确定义问题与适用范围，不能从本研究未选某对象推断领域缺失。
- 未注释、object-only、不同版次、有限观察与真实否定证据不是同一种状态。尤其缺 implements 不等于“不实现”，有 implements 也不等于完整符合性。
- HLS DATERANGE 的零值丢失已有 [#692](https://github.com/InteropAtlas/InteropAtlas/pull/692) 有限执行结果；Syslog 已有 [#688](https://github.com/InteropAtlas/InteropAtlas/pull/688) 实验。UBL 五例、OGC 编码/实现澄清、OpenTelemetry 22 例和 F-UJI 七例亦须直接复用，不能再称“尚未检查”。
- 本研究不修改 Unicode、pugixml、Rust semver、fhirclient 可见摘要以及其他既有身份或发布 hold；也不把某处 hold 扩大成所有领域研究停工的理由。若具体后续步骤触及 held 操作、真实服务或新的权限，应单独确认那个动作，独立的来源核对仍可继续。

因此，本研究为整体底图补上的是跨现有领域的“问题—证据—未知—下一步”阅读路径，而不是用代表样本或实验数量替代完整地图。

## 2026-11-05 追加：现有机器读取的有界适配检验

前文提出了 CloudEvents 字段保留问题；本节进一步检验：**直接使用现有 capability 比较与 evidence projection，是否足以找到这两个实现并理解其证据边界？** 新取样基线固定为 `f521367cbf59033b40fee06b491576ce2bc0e3ac`，前文研究及链接仍保留原基线。本节只执行 IA 自身的本地读取/投影代码，没有安装、导入或运行 CloudEvents SDK，也没有修改数据、Runtime 或任何既有选择合同。

结果是否定的，但这不是 Runtime 缺陷。`project_compare` 按明确 capability 成员选择；Kotlin 记录 `data_serialization`，JavaScript 未注释该 capability，因此请求两个 ID 时只返回 Kotlin。JavaScript 已有来源和历史运行记录，不能把被选择器排除解释成没有序列化能力或没有证据，也不为改变查询结果而补标签。JavaScript 未建立到 CloudEvents 1.0.2 的 implements 则是另一个独立的版次证据问题，不等同于缺 capability 注释。

`project_evidence` 的 assessment 专指 `notes_zh`。两个 SDK 的这个字段都未记录，所以该投影返回 `not_recorded`，但其 `description_zh`、`scope_notes_zh` 中有大量条件和限制。不能把这个状态改读成“没有任何评估”，也不能在查询中悄悄把描述升级为外部权威证据。该投影的 sources 仅保留 title/url/accessed 及恢复路径，未输出 language；要查原来源字段及完整限制，应回到同一 Canonical 记录。这里不建议更改现有投影的语义。

因此本次研究显式选择两个 SDK、固定 CloudEvents 标准及 JSON/URI/RFC3339 三个依赖对象，另取四条已有关系，保留原始字段与 context/evidence 后，再观察既有投影。选择是针对本研究问题，不是新增默认视图、通用查询 API、全库快照或替代方案排名。下面的可复现配方检验选择/恢复行为，不自动判断规范符合性、证据质量或字段在 SDK 中的真实运行结果。

### 可复现配方与本次观察

在完整仓库的固定基线 checkout 根目录，使用该版 Engine 的既有 Python 依赖执行下段；工作树的 tracked 文件必须干净。配方只输出本问题的选择结果、字段状态、恢复路径和输入摘要，没有文件写入或网络调用。`load_atlas` 会读取现有本地存储，随后只保留本问题明确选择的记录。不要把本节作为新 Runtime 接口或自动更新任务。

```python
from pathlib import Path
from copy import deepcopy
import hashlib, json, subprocess, sys

root = Path('.').resolve()
baseline = 'f521367cbf59033b40fee06b491576ce2bc0e3ac'
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == baseline
assert not subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], text=True).strip()
sys.dont_write_bytecode = True
sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
from bootstrap_query import load_atlas, index_objects
from relation_model import normalize_relation
from workspace_projection import project_compare, project_evidence, project_field

pair = ['cloudevents_javascript_sdk', 'cloudevents_kotlin_sdk']
ids = {'cloudevents_1.0.2', *pair, 'json_rfc8259', 'uri_rfc3986', 'rfc3339'}
rids = {'cloudevents_1.0.2_uses_json', 'cloudevents_1.0.2_uses_uri',
        'cloudevents_1.0.2_uses_rfc3339', 'cloudevents_kotlin_sdk_implements_cloudevents_1_0_2'}
objects, relations = load_atlas(root)
index = index_objects(objects)
chosen = sorted([r for r in relations if r.get('id') in rids], key=lambda r: r['id'])
assert len(chosen) == 4 and {r['id'] for r in chosen} == rids
descriptors = [normalize_relation(r) for r in chosen]
assert {d.source_id for d in descriptors} | {d.target_id for d in descriptors} | {pair[0]} == ids
assert len(ids) == 6 and ids <= index.keys()
raw = {'objects': {i: deepcopy(index[i]) for i in sorted(ids)}, 'relations': deepcopy(chosen)}
fields = ['version', 'capabilities', 'description_zh', 'description_en',
          'scope_notes_zh', 'scope_notes_en', 'last_verified_at', 'last_verified_by']
comparison = project_compare('data_serialization', pair, fields, index)
explicit = {i: {f: project_field(index[i], f) for f in fields} for i in pair}
assert comparison['requested_ids'] == pair and comparison['included_ids'] == [pair[1]]
assert explicit[pair[0]]['capabilities']['state'] == 'not_recorded'
assert explicit[pair[0]]['capabilities']['value'] is None
assert explicit[pair[1]]['capabilities']['value'] == ['data_serialization']
for i in pair:
    for f in ['description_zh', 'description_en', 'scope_notes_zh', 'scope_notes_en']:
        assert explicit[i][f]['state'] == 'recorded' and explicit[i][f]['value'] == raw['objects'][i][f]
    p = project_evidence(index[i])
    assert p['evidence_state'] == 'recorded' and p['assessment']['state'] == 'not_recorded'
    assert 'notes_zh' not in index[i]
    assert p['assessment']['recoverable_from']['canonical_field'] == 'notes_zh'
    assert all('language' in s for s in raw['objects'][i]['sources'])
    assert all('language' not in s for s in p['sources'])
assert raw['objects'] == {i: index[i] for i in sorted(ids)} and raw['relations'] == chosen
for r, d in zip(raw['relations'], descriptors):
    assert dict(d.context) == r['context'] and list(d.evidence) == r['evidence']

# Serialization normalizes YAML dates to strings; no semantics or new fields are inferred.
def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str).encode()
raw_digest = hashlib.sha256(encoded(raw)).hexdigest()
assert encoded(json.loads(encoded(raw))) == encoded(raw)
paths = {r['_physical_source'] for r in [*raw['objects'].values(), *raw['relations']]}
paths |= {'02_Runtime/01_Engine/' + name for name in ['bootstrap_query.py',
          'workspace_projection.py', 'relation_model.py', 'repository_layout.py']}
print(json.dumps({
    'baseline': baseline,
    'selected_objects': {i: raw['objects'][i]['_physical_source'] for i in sorted(ids)},
    'selected_relations': {r['id']: r['_physical_source'] for r in raw['relations']},
    'capability_comparison_included_ids': comparison['included_ids'],
    'explicit_pair_ids': list(explicit),
    'sdk_capability_states': {i: explicit[i]['capabilities']['state'] for i in pair},
    'sdk_evidence_states': {i: project_evidence(index[i])['evidence_state'] for i in pair},
    'notes_zh_only_assessment_states': {i: project_evidence(index[i])['assessment']['state'] for i in pair},
    'preserved': ['raw description/scope/sources', 'raw relation context/evidence', 'original verification fields'],
    'raw_source_language': 'present in both SDKs; absent from evidence presentation',
    'raw_selected_records_sha256': raw_digest,
    'input_sha256': {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in sorted(paths)},
    'boundary': 'Fixed question only. Annotation absence is not lack of support; projections do not decide evidence sufficiency or conformance.',
}, ensure_ascii=False, indent=2))
```

本次在 Python 3.12.14 / PyYAML 6.0.3 下实际运行配方通过：capability 比较仅含 Kotlin，显式研究选择含两 SDK；两者 sources 均为 recorded，而 notes_zh-only assessment 均为 not_recorded。原始描述、scope、sources.language 及关系 context/evidence 保留，既有投影输出的省略没有被解释成否定事实。没有改写原核验日期或验证人。

- 配方输出 JSON 的 UTF-8 SHA256：`679273477bf5461d046f6bbe4dbedef7f6683ad26d3ef47928fcc431a86a820e`。
- 选定原始记录按配方序列化的 SHA256：`40aeece1af8a2fff86947a1e68c09a1c1c51929f3fcbe155bd494f499a85a833`。它是复现校验值，不是新 Canonical 事实或全域快照。
- 同一基线既有 `test_workspace_projection.py` 六项测试也通过。它们与上述真实记录适配检验相互补充，但都不是 SDK 执行、端到端交换或全 Runtime 验证。

### 从可恢复字段到真正尚未回答的问题

机器查询把资料带回来了，下面才是基于资料的研究判断。这里的“旧观察”指 [JavaScript 原冻结 packet](https://github.com/InteropAtlas/InteropAtlas/blob/640c41f7d0e2cadff1c9e6f2d7c156a85214b7ab/01_State/Inbox/review-packets/cloudevents-javascript-sdk-20261021.yaml#L171-L191) 所记录的 16 项命名检查，不是本轮重跑；该 packet 保存版本、依赖/integrity 和检查名称，但没有恢复出具体输入、输出或原 probe 脚本。Kotlin 依据[原冻结 packet](https://github.com/InteropAtlas/InteropAtlas/blob/7e79ce099bf8ac40644be0f09437caf874851d36/01_State/Inbox/review-packets/cloudevents-kotlin-json-20261029.yaml#L752-L816)及[当前对象的静态补充](https://github.com/InteropAtlas/InteropAtlas/blob/f521367cbf59033b40fee06b491576ce2bc0e3ac/01_State/01_Objects/cloudevents_kotlin_sdk.yaml)；本轮未恢复原源码捕获目录、重新下载上游或执行 Kotlin。两个冻结 packet 的 Git blob 分别核为 `3c29a02133fd8a8dc55942be818fd2dfe58bc6a2` 与 `edd1c782658e1e244cfc78642440a2a2843d9909`，这是记录身份核对，不是新 SDK 测试。

1. **缺省与自动生成。** Kotlin 的静态范围要求调用方提供有效核心字段，builder/encoder 不调用语义 validate，decoder 调用已实现的 STRICT 检查。JavaScript 旧观察包括补 id/time、拒绝缺 type；[当前描述](https://github.com/InteropAtlas/InteropAtlas/blob/f521367cbf59033b40fee06b491576ce2bc0e3ac/01_State/01_Objects/cloudevents_javascript_sdk.yaml)进一步区分 falsey id/time/specversion 的默认路径。剩余问题是应用允许自动生成身份/时间，还是要求缺省信息保持缺省。构造成功、生成 ID 或生成时间都不是事件真实性证据。
2. **缺值与显式 null。** Kotlin 静态路径区分没有 data 与 data:null；可选属性/扩展 null 视为 unset，data 与 data_base64 同时出现先被拒绝，包括 data:null。JavaScript 的 16 项命名检查没有明确的缺 data/null 配对用例，不能用“structured roundtrip”补造该结果。剩余问题是选定消费者是否区分缺值和显式空值，以及是否有同输入的两端观察。
3. **二进制与载荷含义。** Kotlin 内部 carrier 保留来源路线；普通 bytes 在 JSON/缺省 content type 下解析为 JSON，否则 Base64；任意改变 carrier content type 不在正面范围。JavaScript 旧观察明确记有 data_base64 编码/恢复及 HTTP binary/structured 表示往返，却没有可恢复的共同字节向量。要先选定应保留的是原字节、JSON 值、文本还是来源表示；HTTP binary binding 不能等同于 JSON 格式中的 data_base64。已有[关系条件](https://github.com/InteropAtlas/InteropAtlas/blob/f521367cbf59033b40fee06b491576ce2bc0e3ac/01_State/02_Relations/cloudevents-sdk-implementations.yaml)保留了这个范围，未证明跨 SDK 往返。
4. **扩展类型与名称。** Kotlin 仅恢复 string/int32/bool；URI/Timestamp/Binary 字符串不自动恢复包装类型，null 扩展不保留，允许的核心名冲突可覆盖成员。JavaScript 旧观察只明确默认 strict 拒非法扩展名、false 绕过该名称检查。问题是应用要求原扩展类型还是字符串值；名称有效、JSON 可读与类型往返不是同一证据。
5. **时间瞬间、拼写与真实性。** [CloudEvents→RFC3339 条件](https://github.com/InteropAtlas/InteropAtlas/blob/f521367cbf59033b40fee06b491576ce2bc0e3ac/01_State/02_Relations/protocol-data-representation.yaml)保留可选 time，不证明时钟准确或真实发生时刻。Kotlin 既有静态记录指出 Instant 重编码为 UTC，不保原 offset 拼写；JavaScript 旧观察只有默认 time，没有 offset/精度用例。需要同一瞬间、原拼写或真实发生时间，应分别提出要求，不能互相代替。
6. **数值精度。** JavaScript 旧观察记有默认解析超安全整数舍入、opt-in 大整数路径保值，但没有在本轮恢复具体数值/输出；[当前静态补充](https://github.com/InteropAtlas/InteropAtlas/blob/f521367cbf59033b40fee06b491576ce2bc0e3ac/01_State/01_Objects/cloudevents_javascript_sdk.yaml)仍将 JSON 绑定赋值及宿主副作用列为未评估范围。Kotlin 的 int32 限制针对扩展值，不等于载荷任意精度保证。应先定义某个大整数必须在哪些边界精确保留；不得由两段不同证据推出共同数值域，也不在本研究切换宿主设置。

本节的新执行结果只回答 **IA 的选择器和投影返回什么、哪些字段必须回源**；六项字段判断复用既有证据，仍没有新的 SDK 同输入对照。可以据此把下一个实际问题收敛到缺省/null 或明确扩展类型的一组输入，但须先取得可复现的具体输入、版本和输出记录，而不是重复旧 16 项名称或宣称已经互通。Kotlin 的缺失构建输入与 403 边界不被该提议解除。

服务事件、JSON/URI 表示和 RFC3339 时间之间的已有关系，为这个问题提供跨领域入口。查询返回的对象数、来源条数或字段存在状态不衡量这些领域的完整性；本节没有新增能力注释、implements 或技术关系，也没有替代任何全域快照。对于前文其他领域，同样应先核选择条件和字段语义，再决定一个“未显示”是否真的代表未记录；这里尚未在其他领域执行同样测试，不把一例结果推广成全域保证。


## 2026-11-05 追加：固定规范身份之外的验证资源证据

industrial 行的 JSON/JSON-LD 边界现在增加了[有限离线实验](../../02_Experiments/02_Pilots/wot-td-resource-runtime-2026-11-05.zh-CN.md)及[机器可读输入/来源](../../02_Experiments/03_Evidence/wot-td-resource-probe-20261105-manifest.json)、[完整结果](../../02_Experiments/03_Evidence/wot-td-resource-probe-20261105-result.json)。官方 TD1.1 errata 保留同一 Recommendation 身份，却修订了 TD/TM JSON Schema 资源。相同合成 context 输入在固定前后资源的 Draft7 验证中出现接受差异，涉及映射值和数组位置；空 context 数组及 old→other→new 对照仍被两版接受，不能把通过等同完整符合性。

这为 #276 的外部证据时效性问题提供一个实际边界：出版版本标签不独自固定机器资源字节、验证器方言或具体调用入口。它不是重新盘点领域数，也不自动要求更新全部日期或生成快照。现有 node-wot 十五例已经记录 March-2025 依赖标签，实验未证明其历史安装字节等于所查资源，亦未运行 node-wot/Ajv/JSON-LD 或设备链，因此没有把旧例作废、把剩余端到端问题说成已解决。下一处真正尚缺的证据是某个选定运行入口的确切依赖资源与处理路径，而不是再补一条无范围的“支持 TD1.1”。其他领域的未知仍须各自取证，本例不宣告整体底图完成。
