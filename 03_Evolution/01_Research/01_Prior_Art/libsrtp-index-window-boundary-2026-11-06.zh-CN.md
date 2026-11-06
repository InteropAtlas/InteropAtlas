# libSRTP 包索引估计与重放窗口的条件边界

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed Source Evidence
Document Created At: 2026-11-06T06:24:52.695440+00:00
Document Updated At: 2026-11-06T06:24:52.695440+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_independent_ia_work
  Reviewer: Independent Agent — OpenAI / dot / review_srtp_evidence
  GitHub Actor: ff6962757
-->

## 问题和结论

本研究续接[领域证据审计的 media_network 问题](https://github.com/InteropAtlas/InteropAtlas/blob/af2f5502ea67820696da5629ff6839534257127e/03_Evolution/01_Research/02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md#L227-L241)：libSRTP 2.8.1 的 README 提到乱序超过65k包会失步，公共 API 合同却要求乱序少于32768包。现有记录保留这个差异，但尚未解释索引估计和重放窗口分别负责什么。

固定源码揭示了一个更具体的使用边界：**32768参与16位序号的回卷计数估计，而实际重放接纳还受独立窗口及“是否已见过”约束。** 默认窗口长度为128时，落后当前索引128的输入会在重放检查中被拒绝，即使这个差距远小于32768。窗口内的未见索引只通过重放检查，随后仍有认证、解密及其他失败出口。

这不能把两段文档改写成一致，也不能从任一数字推出安全重排阈值。本文给出固定实现的条件解释，不修订上游合同、不作密码安全认证或部署建议。

## 固定输入与证据等级

- IA 基线为 `af2f5502ea67820696da5629ff6839534257127e`。既有 [libSRTP 对象](https://github.com/InteropAtlas/InteropAtlas/blob/af2f5502ea67820696da5629ff6839534257127e/01_State/01_Objects/cisco_libsrtp.yaml)与有界 implements 保持不变；原接纳与后来的描述补充仍为历史。
- 上游固定 `cisco/libsrtp` 2.8.1、commit `6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa`。本次读取十份完整选定源码/文档，各自字节数、Git blob 与 SHA256见[证据附件](libsrtp-index-window-boundary-2026-11-06.json)。不是完整树、发布包、签名或可复现构建验证。
- 本文没有安装、构建、执行库或上游测试，没有处理任何包、生成/使用密钥、启动网络或改变安全设置。九组索引例子全部是 **UNEXECUTED_SOURCE_DERIVATION**，`actual_result=null`；本地只核源文件身份和手写预期中的整数算术，不把它当 libSRTP 运行。
- 选择普通16位序号及64位整数路径，`ROC_TEST`和`NO_64BIT_MATH`未定义，已有接收流、`pending_roc=0`，不在ROC计数溢出边界。公共调用链进一步限定非GCM、启用认证、有效调用输入及前置步骤成功；不覆盖SRTCP、显式ROC设置、新流模板或并发。

## 序号先被解释为哪一个包索引

[类型与常量](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/include/rdbx.h#L57-L78)固定序号为16位，因此 `seq_num_median=32768`、`seq_num_max=65536`。完整索引包含回卷计数（rollover counter，ROC）与低16位序号。

[`srtp_index_guess`](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/replay/rdbx.c#L122-L164)根据当前低位序号和新序号的差距，在当前ROC及相邻ROC之间选择估计值。比较使用严格大于；差距恰好半圈时保留当前ROC，而非证明输入在时间上属于哪一圈。索引的真实来源还需调用环境和后续认证支持。

调用前还存在[初始状态特例](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/replay/rdbx.c#L309-L344)：`srtp_rdbx_estimate_index`仅在完整本地索引大于32768时调用上述猜测，否则直接使用ROC0和传入序号。代码条件不是注释所说的“序号和ROC非零”。例如初始索引0、传入65000会产生估计索引65000与delta65000；不能用成熟流的半圈推理覆盖首次同步。

以下全是未执行的条件推导。表中“窗口允许”只指 `srtp_rdbx_check` 返回成功；它不表示公共API已成功。

| 本地ROC / 序号 | 新序号 | 估计ROC / delta | 长度128窗口的预期 |
| --- | --- | --- | --- |
| 1 / 1000 | 873 | 1 / -127 | 对应槽未标记时允许；已标记则 replay_fail |
| 1 / 1000 | 872 | 1 / -128 | replay_old，已在窗口之外 |
| 1 / 1000 | 1000 | 1 / 0 | 当前索引已标记时 replay_fail |
| 1 / 65530 | 5 | 2 / +11 | 向前估计，窗口允许 |
| 2 / 5 | 65530 | 1 / -11 | 前一圈的窗口内索引，未标记时允许 |
| 1 / 1000 | 33768 | 1 / +32768 | 半圈相等仍选当前ROC，窗口允许 |
| 1 / 40000 | 7232 | 1 / -32768 | 半圈相等仍选当前ROC，窗口拒绝为过旧 |

最后两行尤其不能被解读为“正向半圈安全、反向半圈不安全”。单个16位序号不携带真实ROC；同一低位值还可以来自更早或更晚的一圈。上述结果只显示特定本地状态下的估计与窗口分支，没有证明真实发送索引或认证结果。

## 窗口长度和已见标记是另一层条件

[流初始化](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/srtp/srtp.c#L1505-L1529)把policy的0解释为默认128；非零配置须至少64且小于32768，否则返回bad_param。底层[bitvector分配](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/math/datatypes.c#L258-L286)会把长度向上对齐到字长，所以任意请求值不应直接当实际窗口长度。本文只使用128这一已对齐值。

[`srtp_rdbx_check`](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/replay/rdbx.c#L251-L268)分开三个条件：delta大于0直接允许；非正delta使 `W-1+delta<0` 时返回replay_old；否则检查该槽，已标记返回replay_fail，未标记允许。对W=128，最旧可检查槽对应delta=-127，而非-128。

这解释了为什么“没有超出序号估计的半圈范围”不足以说明旧包会被接纳。另一个限制是索引是否已经记录；仅给差距而不交代窗口状态，不能决定重放检查结果。[add_index](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/crypto/replay/rdbx.c#L278-L295)负责前移/标记，本身不重做接纳检查。

## 接收路径仍需通过后续处理

在所选已有流且无pending ROC路径，[估计和重放检查](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/srtp/srtp.c#L2810-L2830)发生在认证之前。随后代码按算法分流，[GCM另有处理器](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/srtp/srtp.c#L2849-L2857)，不在这里借非GCM路径推断它。

所选启用认证的非GCM路径把估计ROC纳入[认证计算](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/srtp/srtp.c#L2954-L3000)，认证失败可以返回auth_fail。通过认证后仍可能在密钥使用限额、头部处理或解密等步骤失败。到达[末段](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/srtp/srtp.c#L3095-L3116)才标记重放数据库、调整长度并返回成功。

因此，重放检查的ok、认证通过、公共unprotect返回ok是不同观察。本文没有获得任何一个实际包的这些结果，也不把接收路径结论推广到发送端protect的状态更新顺序或不启用认证的配置。

## 上游测试定义能支持怎样的后续核验

所查测试没有执行。阅读它们是为避免把“有测试”提升成“任意重排都已证明正确”：

- [`rdbx_driver`的validation入口](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/test/rdbx_driver.c#L105-L126)分别选窗口128和1024、每项4096轮。其[乱序辅助函数](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/test/rdbx_driver.c#L198-L223)允许replay_old返回而不把该项作为测试失败；“重复应拒绝”的辅助函数只要求返回非ok，不区分已见与过旧。注释明确真实使用还需认证，测试辅助函数没有模拟认证。
- [large gaps循环](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/test/rdbx_driver.c#L296-L309)每步增量是 `1 << (random % 12)`，即1至2048中的二次幂，不是直接覆盖32768或65k阈值。
- [`roc_driver`](https://github.com/cisco/libsrtp/blob/6ff02afa8d2dc3f2e8896af391d137c1c66ff6fa/test/roc_driver.c#L126-L167)的乱序部分记录估计与参考不符，并把local重设为参考值；对“估计值与参考值不一致”这一累计计数，比率超过1%才因该判据返回算法失败；另有 `local+delta != est` 时立即失败的检查。因此即使未来运行打印passed，也应同时读其具体判据，不能译成零次估计偏差。测试数据宽度还受编译宏影响。

这些都是固定源码中的测试设计，不是发现部署漏洞、不代表上游CI实际运行了这些入口，也不提出放宽安全检查的建议。

## 留下的具体未知

README与公共头文件的措辞差异仍然保留。当前源码证据已能分开16位估计、窗口接纳及调用结果，下一份真正新增的运行证据应固定一个授权的离线配置，记录相同包索引序列下的实际返回码和状态变化，明确是否涵盖初始同步、回卷和窗口边界。本研究未进行该运行，也不提供未来测试、联网或维护的授权。

原有SRTP→RTP规范关系与libSRTP→SRTP实现关系不扩展为整套媒体系统、WebRTC、握手或端点认证的保证。此研究只补一个已有明确问题的证据段，不声明media_network、trust、transport或整体底图完成；Canonical、分类、关系语义、UI、快照和既有holds不改。
