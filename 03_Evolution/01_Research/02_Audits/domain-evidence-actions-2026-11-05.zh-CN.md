# 既有领域的证据问题与跨域后续研究

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Evidence Reconciliation
Document Created At: 2026-11-05T12:42:00+00:00
Document Updated At: 2026-11-05T21:12:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot
  Reviewer: Independent Agent — OpenAI / dot
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


## 2026-11-05 追加：MCP 工具模式由谁实际验证

agents 行的方言问题现补有[固定源码责任矩阵及验证器实验](../../02_Experiments/02_Pilots/mcp-schema-responsibility-2026-11-05.zh-CN.md)。SDK1.26.0 的低层服务端在定义存在、输入开关启用时委派 jsonschema；直接 CallToolResult 返回跳过其后的低层输出模式分支。FastMCP 则关闭那一步低层输入检查，使用条件预解析与 Pydantic，某些直接结果仍有自己的输出模型检查；客户端只对非 isError 的结果检查结构化输出。这些分支不能概括为“全部验证”或“完全不验证”。

已有 jsonschema4.26.0 上，12个合成输入对进一步区分了省略、2020-12、Draft7和未知声明：同一 prefixItems 非整数输入在Draft7下被接受，未知URN则 warning 后回退，正面对照接受、非整数被拒绝。该结果只属于验证器，不是SDK端点运行或完整协议不符合裁决。SDK的依赖范围、锁文件4.25.1、历史13例及本轮4.26.0分别保留；IA的4.25.1对象与既有实现关系不因此改版。

与前述WoT资源修订和UBL结构/业务限制一起，这份证据回答了同一个组合问题的另一段：规范与模式存在后，是否确实到达预期验证器，错误又由谁转成可见结果。三类本地证据不能合成统一验证流水线或新的技术边。源码责任及依赖实验已不再未知；固定SDK实际方言调用、FastMCP转换后的值、真实协议响应和跨实现互通仍未执行。这个边界比缺少capability或notes注释更具体，但不要求为改变查询结果补标签，也不改变页面、维护机制或任何既有hold。


## 2026-11-05 追加：同一时间表示的跨领域含义

[时间字段可迁移性比较](../01_Prior_Art/timestamp-portability-2026-11-05.zh-CN.md)沿四条现有外部 RFC3339 uses，把 services 的事件时间、observability 的 Syslog 时间、geospatial 的查询条件及 agents 的记录创建时间放在同一组具体迁移问题下。共同语法不证明字段指称同一事实。OGC 条文还要求 datetime 匹配无 temporal geometry 的要素；Syslog 的可选 timeQuality 独立说明时区知识、同步状态与误差。这些事实不能从一个合法时间字符串或小数位数推出来。

固定实现源码进一步分开原始字符串、原生时间值、缺省时间和实际操作：pygeoapi 把参数与集合 extents 交给条件检查，再交 provider；所查 CSV/GeoJSON 路径未应用该过滤，响应 timeStamp 另取当前 UTC。CloudEvents 两 SDK 的 time 转换入口和 pyRFC3339 的既有精度/零偏移观察，说明表示可读、数值保留、偏移知识与真实发生时间不能互相替代。所有新结论是文献/源码比较，旧40/16/12观察没有重跑；没有新增关系、统一时间格式、页面、维护门槛或全局覆盖率。剩余缺口是具体字段映射的业务依据和实际选定入口的交换结果，不是缺少 capability 或 notes 标签。


## 2026-11-05 追加：失败信号从哪里来、消费者还需判断什么

[HTTP 与工具调用的失败信号比较](../01_Prior_Art/failure-signal-comparison-2026-11-05.zh-CN.md)连接 services 的问题详情、transport 的 HTTP 客户端、syntax/semantic 的 JSON/URI 与 agents 的 JSON-RPC/MCP。RFC9457 的状态生成一致性不等于接收端分歧时无条件优先级；HTTPX 的 JSON 解析和实际状态判断仍不解释问题类型。202 接受处理也不等于最终完成。

MCP 的 result.isError 可在 JSON-RPC 结果信封内报告工具失败；固定 FastMCP 的普通异常包装和未知工具路径不能用规范示例机械预测。客户端还会为超时与断流在本地构造错误，因此 McpError 或内部 JSONRPCError 本身不能证明收到对端错误。已补23份规范/固定源码的字节身份、条件化责任比较及明确未执行的示例，历史17/13/12观察没有重跑。

具体未知现在落到真实生产端适配器、实际所收信封/本地异常来源，以及方法完成/副作用合同，而不是笼统的“有没有错误支持”或缺少注释。这些研究条件没有拼成通用错误映射、自动重试规则或已运行链路；未改 Canonical、Runtime、页面、维护机制与任何 hold。


## 2026-11-05 追加：共享 JSON 数字之外的量值含义

[SenML 与 FHIR Quantity 的量值保留比较](../01_Prior_Art/quantity-preservation-2026-11-05.zh-CN.md)把 industrial/measurement、health 与 syntax 的既有记录连接到一个具体交接问题。SenML base 值/单位的活动范围、FHIR显示单位与编码身份、comparator 的界限语义，以及缺值不能补零分别保留。最明确的合同差异是 SenML 1.1/1.10 语义相同，而 FHIR decimal 原表示精度须为展示保留，不能把同一重序列化策略无条件视作两边都无损。

证据文件绑定官方条文、固定源码、11个明确未执行的原始JSON输入和两条已有JSON uses；一次性配方恢复完整关系条件并检验字节、引用与有限 Decimal 算术，不运行上游实现或把反例误称符合性通过。实际单位映射、测量对象/时间/主体对应、限定词承载和选定实现的交换结果仍未知；无版本UCUM system不被强行当作出版版本。没有新转换器、Canonical边、快照、UI或维护机制，也没有重做或替代 held FHIR 摘要工作。


## 2026-11-05 追加：引用到资源的责任边界

[跨领域资源责任比较](../../02_Experiments/02_Pilots/resource-resolution-boundary-2026-11-05.zh-CN.md)连接 agents、industrial、语法/语义和服务事件中的具体问题，而不是再增加一份对象清单。九个实际离线 JSON Schema 案例区分同输入/不同 registry、同资源集合/不同 base、缺资源异常与普通实例拒绝；相同引用字符串不固定最终使用的资源。JSON-LD/PyLD 只读证据进一步区分上下文 base、最终文档 URL、缓存与 loader，CloudEvents source 则说明 URI-reference 也可以只承担事件标识。

机器证据保留具体 JSON 文本、实际输出、安装环境、规范/源码身份及七条已有关系的完整 context/evidence。未执行的 JSON-LD 说明例明确为空实际结果；未把 SDK 调用语句、node-wot 依赖标签、历史例或规范要求替换成新的端到端观测。资源实际供应和选定调用配置是比补一条无条件“支持 URI”更具体的缺口；它不授权联网加载、解除 hold、改写关系语义或设立新维护机制。

## 2026-11-05 追加：把已完成研究接回现有对象证据

六个后续研究问题已有固定报告和机器材料，但在本次基线 `314d70148ae1f154c852c85f9d4886804c74ac54` 的所选六个对象中，来源/判断字段尚未指向这些材料。资料已存在；缺少这条读取路径不是缺少研究，更不是对应标准、能力或实现不存在。#697–703 为七个 PR、六个实质研究问题，#703 只修正 #702 的 URL 用语，不能另计研究覆盖。

本次只接合既有字段：八条新增 `sources` 引用限定的历史来源身份/条款定位或真实结果，六条 `notes_zh` 列表项保留 IA 自有比较判断及固定报告链接。JSON 中的来源清单、实际观察、未执行说明例与研究判断不混称“通过的测试”。比较报告进入现有 assessment 投影，不作为外部规范权威；官方一手来源保留在前，原顺序、字段和 accessed 日期不变。

| 既有对象入口 | 可继续追问的问题 | 新来源入口的限定 |
| --- | --- | --- |
| `wot_td_1.1` | 同一 Recommendation 身份是否固定验证资源？ | TD/TM 固定资源来源段与历史 Draft7 实际结果；不证明 node-wot/JSON-LD 运行 |
| `mcp_python_sdk` | 工具模式在哪些调用路径被验证？ | 同一 1.26.0 固定提交的静态源码清单；不将独立 jsonschema4.26.0 实验归到 SDK |
| `rfc3339` | 共同时间语法是否指同一事实并保留同样信息？ | 固定规范、实现来源和历史观察身份段；不声明新执行 |
| `problem_details_rfc9457` | HTTP 问题内容与其他失败信号分别说明什么？ | HTTP/JSON-RPC/MCP 来源身份段，排除未执行说明输入；不建立统一错误映射 |
| `senml_rfc8428` | 相同 JSON 数字是否足以跨格式保留量值？ | external_sources 定位段，不把未执行例子或研究比较当转换结果；不改 held FHIR 摘要 |
| `uri_rfc3986` | 引用标识何时成为被使用的资源？ | RFC3986 §1.2.2 及固定 context_sources 身份段；不是 RFC3986 任意实现的运行验证 |

[一次性复核配方](evidence-linkage-reproduce-2026-11-05.py)使用未改变的 `load_atlas`、`project_evidence`、`project_field`，对同一六个 ID 检查前后读取及原字段保留。[实际输出](evidence-linkage-result-2026-11-05.json)记录每个问题的来源入口、assessment 角色、恢复位置、原验证字段是否存在及原值、旧来源摘要和历史工件 hash。它不新增查询合同、能力标签、关系边、维护清单或 CI gate，也不执行上游库。

在一个已有依赖、保留基线历史的本地 checkout 中运行；基线目录须已检出上述精确提交，脚本不替调用方下载、切换或修改它：

```sh
PYTHONDONTWRITEBYTECODE=1 python 03_Evolution/01_Research/02_Audits/evidence-linkage-reproduce-2026-11-05.py \
  --root . --baseline-root /path/to/baseline-checkout
```

实际配方确认：六个原 assessment 为 not_recorded 的记录现在能恢复明确的 IA 自有 notes；这个变化只表示加入了有内容的判断链接，不把原 not_recorded 当作研究不存在。旧来源投影前缀保持不变，全部非所选对象和全部原关系保持不变。原 description/summary/scope、版本、标识、intake、record_created_at 和 last_verified_at/by 逐字段不变，原来缺少验证字段的记录也不补造。record_updated_at 与本次贡献身份反映这次实质接合；RFC3339 的生命周期来源改为 mixed，当前贡献来源改为 commit_explicit，以区分旧的重建创建时间和本次直接记录，不改变旧 metadata_backfilled_at。

当前 Human 输出的限制也实测保留：六个对象页都显示新来源入口；MCP 实现页显示可点击的研究报告链接。五个标准页的既有模板不打印 notes 正文，只保留 assessment 计数，机器投影仍能恢复完整内容。搜索索引没有纳入 sources/notes，本次字节不变；没有声称新报告关键词已可搜索，也不借此修改 renderer、页面展示或搜索规则。静态生成比较只变化六个对象页，其他生成文件不变。没有启动本地浏览器或重试既有 Chromium 拒绝。

这次接合使“从一个已知对象继续查到已完成的具体答案”可按现有机制复核；它不代表全部领域的证据均已接通、整体底图已完成、历史实现重新验证或资料判断升格为外部权威。原资源/部署、跨实现交换、未知和所有 hold 继续保留。


## 2026-11-05 追加：从实现记录找回已有保持性反例

前一节把六个研究问题接回标准/实现入口；本次处理另一个具体访问问题：**从两个 Syslog 库或 m3u8 的现有对象出发，能否直接找回已完成的“接受输入却不保留值”观察，并区分观察、关系范围与未知？** 基线固定为 `682fe7d50b6474aa35b6f8e6c1ec6a70987f3d3d`。这是已有证据的接合，不是新增上游实验、完整率测量或新维护合同。

基线中，三对象的 `project_evidence` 分别返回 4、10、10 条原 sources，notes-only assessment 均为 `not_recorded`；这些状态不表示没有研究。Syslog 已可从 RFC3339 经前节时间比较清单间接抵达，全文研究也已有链接。本次补的是**实现对象本身的直接恢复路径**，不宣称证据原来全局不可发现。没有因为 notes 缺失而补能力标签或技术边。

| 实现入口 | 新的直接证据入口 | 能回答的有限问题与边界 |
| --- | --- | --- |
| `python_rfc5424_logging_handler` 与 `python_syslog_rfc5424_parser` | 同一份 [Syslog 清单](../../02_Experiments/03_Evidence/syslog-composition-probe-20261105-manifest.json)、[12 输入结果](../../02_Experiments/03_Evidence/syslog-composition-probe-20261105-result.json)和[报告](../../02_Experiments/02_Pilots/syslog-composition-runtime-2026-11-05.zh-CN.md) | 10 项 formatter 输入、2 项手写输入，不是两套24例。严格 UTF-8 解码后的语法接受并不还原所有应用值：协议转义、BOM、重复参数和 PROCID 分别保留其观察层次。手写重复参数不归给 formatter。两库仍 object-only，没有从实验补 implements。 |
| `python_m3u8` | [HLS 清单](../../02_Experiments/03_Evidence/hls-daterange-probe-20261105-manifest.json)、[九输入结果](../../02_Experiments/03_Evidence/hls-daterange-probe-20261105-result.json)和[报告](../../02_Experiments/02_Pilots/hls-daterange-runtime-2026-11-05.zh-CN.md) | 在固定位置及组合中，显式零值在输出后成为缺失；非零/省略对照分开。DURATION 与 PLANNED-DURATION 不混为一项含义。再解析是同一库，既有静态 implements 切片不因链接扩大到 DateRange、SCTE35 或完整 HLS。 |

两个实验不互相组合为一个交换系统，也不合并成21项“互操作覆盖”。它们共同提醒本次使用者先指定需要保留的内容：应用值、参数的重数、标识的字面形式、实际/预计时长、或者原始字节；“返回成功”不能替代该项判断。这个判断放在三对象各自 `notes_zh` 字符串列表中，由既有 projection 标为 IA-authored assessment。来源字段追加的是固定提交下的历史清单/观察 JSON，不把报告解释当成新的外部权威。

### 历史身份、范围与时间没有被合并

Syslog 结果固定 handler1.4.3、parser0.3.2、Lark0.6.7、tzlocal5.3.1、pytz2025.2、CPython3.12.14 和 UTC；这是选定实验环境，不是上游历史锁定。parser 的 message.py、parser.py 与原提交字节相同，handler wheel 中的 handler.py、transport.py 则仅在 CRLF→LF 后与原提交相同，不能笼统称所有源码字节相等。HLS 结果固定 m3u8 6.0.0 官方 wheel，八个 Python 文件与 `49417d05602fc472b518ec61aa9b327cd00e079d` 字节相同。

三对象原描述和 `last_verified_at/by` 保留静态接纳范围及原日期；原文的未执行陈述不被改写为实验结论，也不抹去另有环境与日期的后续实验。新增 notes 明确这种分层，`record_updated_at` 与当前贡献信息只标识此次接合。旧 sources 的顺序、值和 accessed、版本、身份、intake、created 与全部关系不变。历史报告、脚本、清单和结果字节也不变。本次没有下载、安装、导入或运行这些上游库。

### 用既有读取机制恢复

在含本次接合的干净 tracked checkout 中，使用当前 Engine 已有依赖可执行下方一次性只读配方。输出原有对象来源、独立 assessment 和核验字段，不执行历史实验、不判断完整符合性，也不创建通用查询合同。历史 JSON 中的输入、输出与版本可从返回的固定 URL 继续恢复。

```python
from pathlib import Path
import json, sys
sys.dont_write_bytecode = True
root = Path('.').resolve()
sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
from bootstrap_query import load_atlas, index_objects
from workspace_projection import project_evidence, project_field
objects, _ = load_atlas(root)
index = index_objects(objects)
ids = ['python_rfc5424_logging_handler', 'python_syslog_rfc5424_parser', 'python_m3u8']
print(json.dumps({i: {
    'evidence': project_evidence(index[i]),
    'historical_verification': {f: project_field(index[i], f)
                              for f in ['last_verified_at', 'last_verified_by']},
} for i in ids}, ensure_ascii=False, indent=2, default=str))
```

本次本地实际读取恢复 6、12、12 条 sources，各含两条追加的固定历史来源，并恢复三个 IA-authored notes；两条 Syslog 路径是同一清单/结果。原始核验字段逐值保留。这是 IA 数据读取检验，不是重新执行12例或9例。所有既有 hold、取消的 live-page retrieval 及页面/显示暂停保持不变。


## 2026-11-05 追加：哪些原始信息真正进入下一步检查

本次选择一个已有材料能够具体回答的问题：**原始信息经过转换、选取或 API 传递后，哪一部分真正成为下一步检查的输入？** 基线为 `815c973e5ee8e7ee755417718e70f892f3e8d977`。接合的是两份已完成研究，分别连接 `pyld` / `pyshacl` 与 `ebu_libbw64` / `ebu_libadm` 的拥有者记录；两组不是彼此兼容的技术，也不组成共同管道。

| 既有研究 | 可直接恢复的具体判断 | 证据模式与未回答项 |
| --- | --- | --- |
| [JSON-LD→RDF→SHACL](../../02_Experiments/03_Evidence/jsonld-shacl-boundary-probe-2026-10-21.zh-CN.md) | 固定输入的未映射属性在展开时丢弃，随后图验证通过没有检查该原属性。调用方显式复制默认图或 union 后再调用验证器；同一混合数据集得到不同结果，仅命名图数据还显示 targetClass 无焦点与 targetNode 的区别。 | 历史实际观察：七输入、十二个预期结果，包含不符合、returned failure 与异常，不是十二个符合文档。它们不是原 PyLD十八例/pySHACL十九例的替代资产。不推断所有图选择、远程数据或 RDF1.2。 |
| [libbw64/libadm 交接](../01_Prior_Art/libbw64-libadm-handoff-2026-11-05.zh-CN.md) | 所选块 API 提供 AXML/CHNA 原始值；parseXml 入口没有 CHNA/fmt 参数。XML 内部引用解析不能代替调用方的跨块音轨关联检查，支持字段再生成也不是任意 XML 字节保留。 | 已复核静态源码判断；配对/封套见证均 UNEXECUTED，actual_result 为 null。没有此配对的编译或运行结果；common-definitions 完整标识库存等准备前提仍待核对。既有推荐不变为已测版本组合。 |

这不是又一份“验证不足”的泛论：第一组能指出丢弃和显式选取发生在验证器之前；第二组能指出相关信息未作为所选 API 的输入。两组证据强度不同，不能把静态预期换名为实测，也不把案例数合成覆盖分数或新分类。UBL 的既有对象/关系已说明 #488 的 IND5 与 XSD 反例，本次不机械追加它或重跑任何探针。

### 恢复路径、身份与旧边界

两组原来都可从本审计及历史研究抵达；JSON-LD 实验另有 URI 研究经本审计的间接入口。四对象原有 sources 数分别是14、7、13、2，均无 notes_zh，但这不表示没有条件、判断或研究。新增的是**从拥有者对象直接恢复对应输入/输出或静态来源的路径**，不宣称全局发现了缺失知识。

- PyLD/pySHACL 各追加同一对[原始输入与转换输出](../../02_Experiments/json-ld/jsonld-shacl-produced-20261021.json)、[验证结果](../../02_Experiments/json-ld/jsonld-shacl-result-20261021.json)。只看后者会遗漏哪些原始字段已不在 RDF 中。JSON 记录的安装包版本与当前对象3.3.0/0.40.1 相同，但没有执行发行包的哈希或与 Canonical 固定 Git 提交字节相等的证据。Python3.12.14 和分离环境/进程由报告记录，不能说它们写在两份结果 JSON 中。四个原脚本/输出哈希与报告相符；本次仅核历史资产字节，没有执行上游。原 PyLD十八例完整脚本/输出未恢复的历史限制不被这组不同实验补齐。
- libbw64/libadm 各追加同一[静态 source_verification 区段](https://github.com/InteropAtlas/InteropAtlas/blob/815c973e5ee8e7ee755417718e70f892f3e8d977/03_Evolution/01_Research/01_Prior_Art/libbw64-libadm-handoff-2026-11-05.json#L17-L387)：32 份选定文件身份、哈希、Git commit/tree 记录及静态范围。facts 区段止于 findings/合成见证之前；不把整个混合 JSON 标成运行证据。研究判断和完整报告入口放 notes_zh，而不是新增外部权威来源。文件身份核对不等于签名验证或与更早捕获的字节相等。

原描述、scope、版本/身份、source 顺序和值/日期、intake、record_created 和 last_verified_at/by 保持原样，包括 libadm 未记录核验字段的状态。现有技术关系逐字节不变，#583 既有 libbw64 实测不转移给 libadm，旧接纳例与本次所接研究不合并计数。仅 record_updated 与当前贡献信息反映此次接合；历史报告、输入、脚本和结果也不改写。

### 沿用现有读取，不另造查询机制

沿前节完整只读配方，将 `ids` 列表替换为 `['pyld', 'pyshacl', 'ebu_libbw64', 'ebu_libadm']`，其余读取/投影代码不变，即可恢复四个 owning-record 入口。本次实际执行该替换后的 IA 查询：sources 数为16、9、14、3，恢复四个独立 IA-authored assessment；六条追加引用对应三份不同历史 JSON，其中 ADM 仅指限定行段。新 notes 不作为外部证据，原核验字段保持原值或 not_recorded。

这份读取检查不重做七输入/十二观察、构建 libadm 或运行未执行见证，不创建新 API、字段、规范、自动队列或维护合同。所有关系、既有 holds、取消的 live-page retrieval 及页面/显示暂停保持不变。


## 2026-11-05 追加：恢复替代关系时，选择结果与条件在哪里

现有底图能回答“记录了哪些替代路线、比较条件是什么”，但只读一个 capability 查询的三元组还不够。本次固定基线为 `b5e96ae4799a2a8a7271e7629a3d52409d44cb56`，遍历既有 loader 返回的关系，得到三条显式 `alternative_to`。这里只清点该基线已录的这个谓词，不建立现实方案全集、全域快照或替代充分性判断，也不重复核验三条边的外部来源。

[六维研究](../03_Tests/coverage-dimension-reconciliation-2026-11-05.zh-CN.md)已用 URL/URI 说明有界替代，并指向会保留条件的 `alternative_relations()`；[领域选择审计](domain-selection-audit-2026-11-05/README.zh-CN.md)处理导航、implements 与对象字段。本次补的是它们尚未并列检验的两种读取差异：**已有边未被能力查询选中**，以及**选中后的 CLI 输出未携带已有条件**。这两种差异都不能直接归为 Canonical 缺陷。

### 三条已有比较，各自能回答什么

| 已录关系与固定来源 | 本次能力查询 | 能恢复的条件与未回答的问题 |
| --- | --- | --- |
| [semver_alternative_calver](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/01_State/02_Relations/versioning-alternatives.yaml#L13-L51) | `version_expression` 未选中此边 | SemVer 2.0.0 的公共 API/兼容性表达与 CalVer 的时间/节奏目标可作条件性比较；可组合使用，不是规则可互换或必须二选一。原边有两个 evidence 项及版本限定，但没有显式关系 capability context。两端对象和 notes 中的同一能力不自动补成该 context；空查询不表示没有这项知识。 |
| [url_standard_alternative_context_uri](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/01_State/02_Relations/engine-v0.1-bootstrap.yaml#L248-L307) | `resource_identification` 选中此边 | WHATWG 所定义的 Web URL 行为与 RFC3986 通用语法/引用解析按应用要求比较。明确要求 RFC3986 的协议不能据此自动替换；解析成功也不证明原输入符合两套规则。原边保留三个 evidence 项，以及当时观察的 Living Standard 与固定 RFC 的不同身份。 |
| [forgejo_actions_alternative_to_github_actions](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/01_State/02_Relations/ci-cd-implementations.yaml#L1-L77) | `automated_build_deployment` 选中此边 | 熟悉的工作流模型不表示完全兼容。已有六个 evidence 项限定文档级 OIDC 比较：启用设置、workflow/job 优先级、Forgejo fork 限制和外部 provider trust 分开。v17.0 文档观察不扩展为所有版本、实机迁移成功或 token exchange 已完成。 |

以上 source 数量只是核对既有载体，不是证据充分性或覆盖评分。三条边原有的观察/核验日期保持原值；本次实际执行的是 IA 读取，不是重新观察上游网站或运行这些技术。

### 按现有读取层次保留条件

[选择函数](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/02_Runtime/01_Engine/bootstrap_query.py#L112-L131)检查 `normalize_relation()` 后的显式 capability context，返回匹配的完整加载记录。[兼容读取](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/02_Runtime/01_Engine/relation_model.py#L115-L136)会把已有 legacy `capability_context` 与顶层 conditions 纳入规范化 context；Forgejo 的正面结果走的是这条既有路径，不需要修改数据。SemVer/CalVer 没有相应显式字段，normalizer 也不从端点能力或 notes 推断它。

随后，[`run()` / CLI](https://github.com/InteropAtlas/InteropAtlas/blob/b5e96ae4799a2a8a7271e7629a3d52409d44cb56/02_Runtime/01_Engine/bootstrap_query.py#L134-L171)把选中边缩成 source/relation/target 三元组。条件、版本、evidence 与关系 ID 不在这个投影里，但仍在原记录中。因此，六维研究所说的“保留条件”适用于该 helper 返回的记录，不能扩大为 CLI 三元组自身已经包含这些材料。查询没有选中一条边，与记录没有这项比较，是不同答案。

下面是一段固定基线、只读、仅向 stdout 输出的完整例子。使用已有 Engine 依赖，在该提交的干净 checkout 根目录运行；它不下载或切换 checkout，也不改写记录。三条完整加载记录保留既有字段，loader 追加的 `_physical_source` / `_source` 只是物理/逻辑恢复位置，不是原 YAML 字节或外部证据。`normalized_context` 另列现有 normalizer 的结果，避免把 legacy 字段移动误说成源文件修改。

```python
from pathlib import Path
import json
import subprocess
import sys

root = Path.cwd()
baseline = "b5e96ae4799a2a8a7271e7629a3d52409d44cb56"
assert subprocess.check_output(
    ["git", "rev-parse", "HEAD"], text=True
).strip() == baseline
sys.dont_write_bytecode = True
sys.path.insert(0, str(root / "02_Runtime/01_Engine"))
from bootstrap_query import load_atlas, index_objects, alternative_relations, run
from relation_model import normalize_relation

objects, relations = load_atlas(root)
index = index_objects(objects)
alternatives = sorted(
    (r for r in relations if normalize_relation(r).predicate == "alternative_to"),
    key=lambda r: r["id"],
)
assert {r["id"] for r in alternatives} == {
    "semver_alternative_calver",
    "url_standard_alternative_context_uri",
    "forgejo_actions_alternative_to_github_actions",
}
capabilities = [
    "version_expression", "resource_identification", "automated_build_deployment"
]
assert all(capability in index for capability in capabilities)
result = {
    "baseline": baseline,
    "loaded_alternative_records": alternatives,
    "normalized_context": {
        r["id"]: normalize_relation(r).context for r in alternatives
    },
    "capability_queries": {
        capability: {
            "capability_exists": capability in index,
            "selected_relation_ids": [
                r["id"] for r in alternative_relations(relations, capability)
            ],
            "cli_triples": run(root, capability)["alternative_relations"],
        }
        for capability in capabilities
    },
}
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
```

本次执行确认三个 capability 均存在，所选关系数依次为0、1、1；后两项分别是表中 URL/URI 与 Forgejo/GitHub Actions 边。完整加载记录恢复三条边自己的条件、版本和 evidence；未选择的 SemVer/CalVer 也通过谓词遍历保持可见。所有 source/target 方向照录，包括 SemVer→CalVer，不根据比较文字反转。这只是让既有比较连同限制可读取，不给它补 capability 注释，不改变查询或关系语义，也不生成新的替代边。

具体应用仍需给出自己的任务约束、所用版本和迁移/交换证据，才能判断一条记录是否足够支持选择。当前三条记录不能证明替代方案已穷尽，也不能证明某项现实任务无解。本次在这一有限问题上停止，不把读取差异升级为新 API、通用选择器、维护规则或覆盖评分；原有页面/显示暂停与全部 hold 保留。


## 2026-11-05 追加：已提取父上下文如何到达采样与处理器

前文 observability 行将 API 传播与 SDK 批处理之间的衔接保留为未回答问题；原固定基线和历史结论不改写。本次[固定源码研究](../01_Prior_Art/otel-sampling-handoff-2026-11-05.zh-CN.md)及[机器可读证据](../01_Prior_Art/otel-sampling-handoff-2026-11-05.json)补充了其中的 parent-context → sampler → on_end 路径。

在明确把 extract 返回的有效远程父 Context 传给启用的 SDK tracer、未提供 sampler 且未设置 OTEL_TRACES_SAMPLER 的条件下，固定1.45.1源码的默认 ParentBased(ALWAYS_ON) 将 sampled / unsampled 父分别导向 RECORD_AND_SAMPLE / DROP。显式对照 AlwaysRecordSampler(DEFAULT_ON) 仅把后者改为 RECORD_ONLY：子 span 在结束前可 recording，正常首次结束可到达已注册 on_end，但 BatchSpanProcessor 因 sampled=false 不调用内部 emit。处理器链此前的回调均正常返回等条件详见报告。

这让“关联 trace ID”“处理器观察结束”“通过批处理 sampled 筛选”三个问题能分别追溯，不把上下文存在当作导出成功。extract 本身不激活 SDK 或自动选择后续父上下文；无效 carrier 返回保留的有效 base Context 时，也不能直接认定生成新 root。

这是九份固定官方源码及九个**未执行**假设案例的条件推导，实际结果全部为 null；不是 SDK 运行、跨服务互通、队列保留或网络送达证据。API 历史22例汇总、SDK 静态批处理记录、2021/Trace Context 2 版次边界仍分别保留。没有新增技术边、Canonical 验证日期、页面或维护要求。


## 2026-11-05 追加：从无符号整数编码前缀到 token 解码

在 syntax 原行基础上，追加 TinyCBOR 7.1 → libcbor 0.12.0 的有界源码推导：十个 uint 分界值，10个完整前缀、40个截断前缀、40个从原 token 起点重试及20个尾字节用例。12份固定文件的 Git blob、字节数和 SHA256 与冻结复核包一致。全部110个组合用例仍为 UNEXECUTED、actual_result=null，没有运行任一上游库，也没有新增已观察互通边。

核心增量是把输出前缀长度与 uint 回调、read/required 对齐：空输入预期 read=0/required=1；非空截断 required 是 token 所需总长；完整项后追加字节仍只消费首项。真实缓冲、回调与平台条件必须成立。FINISHED 不表示完整文档已消费或验证，局部最短整数头不证明确定性 profile。原 cbor2 35项观察、两条实现边与原审计边界保持不变。

详见[固定源码报告](../01_Prior_Art/cbor-uint-handoff-2026-11-05.zh-CN.md)与[机器可读证据](../01_Prior_Art/cbor-uint-handoff-2026-11-05.json)。原审计行的固定基线与历史表述保持不变。
