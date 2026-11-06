# 两个响度库的比较前提：完整块、查询与测量结束

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-source Comparison
Document Created At: 2026-11-06T16:02:34+00:00
Document Updated At: 2026-11-06T16:02:34+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_authorized_work
  Reviewer: Independent Agent — OpenAI / dot / review_loudness_comparison
  GitHub Actor: ff6962757
-->

## 回答的具体问题

承接[measurement 行](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md#measurement测得一个-lufs-值是否已完成-r128-的归一化与交付判断)：同一份 48 kHz 立体声 PCM，怎样对齐 `broadcast-loudness` 与 `libebur128` 的输入、完整块和查询时点，才不会把不同生命周期的返回值误认为算法差异？

本次固定源码对照给出的答案是：**帧数相同还不够，Rust 的 finish 与 C 的 global 查询不能当成同一种检查点。** Rust 先累积完整门限块，调用 `finish()` 才计算并缓存集成响度，同时丢弃末尾不足 100 ms 的子块、拒收后续输入；C 在输入时处理已完整的块，`ebur128_loudness_global()` 读取已保存能量，不封口，也不清掉留待后续输入补齐的尾部。比较某个前缀时，Rust 应使用专属实例并在该前缀结束后 finish，而不是在一个持续测量实例上反复 finish。

此外，两条选定路径的门限表达式不同：Rust 在 LKFS 域使用严格 `>`，C 的非 histogram 路径在能量域使用 `>=`。这只证明源码分支条件不同，**没有产生一个两库实际读数不同的音频反例**，不裁决哪一个符合规范、精度更高或适合部署。

本研究没有安装、编译、导入、运行上游库或测试，没有生成或处理音频。下列输入与配方全部 **UNEXECUTED**，实际 LUFS、误差和跨库一致性均未知。IA 文档、指纹和整数算术检查不是音频运行验证。

## 固定身份与既有证据

- IA 基线：`ec90b3c983a84e7c7cf885156a268f7343f26765`。保持现有 [Rust 对象](https://github.com/InteropAtlas/InteropAtlas/blob/ec90b3c983a84e7c7cf885156a268f7343f26765/01_State/01_Objects/broadcast_loudness.yaml)、[C 对象](https://github.com/InteropAtlas/InteropAtlas/blob/ec90b3c983a84e7c7cf885156a268f7343f26765/01_State/01_Objects/libebur128.yaml)及技术关系不变。
- Rust：`fishloa/rust-broadcast` 中独立的 `broadcast-loudness` 0.5.0，固定提交 `579ad2c08b675fc52dee6db4ecb16b3038bb19ce`。本轮读取固定 Cargo.toml 和三个源码文件；不重新验证发行包、注册表或整个工作区。
- C：`jiixyj/libebur128` v1.2.6，固定提交 `67b33abe1558160ed76ada1322329b0e9e058b02`。本轮读取完整 ebur128.c/.h；头文件版本宏为 1.2.6，不重新认证 tag、归档或构建。
- [机器可读记录](loudness-comparison-boundaries-2026-11-06.json)列出六份完整文件的 Git blob、字节数、SHA256、相关行段与配方状态。完整字节核对不表示每行均已语义审计。
- Rust 的现有证据是有限 Annex 1 路径的静态映射，**未运行**；C 的既有核心构建和有限合成观察**已经运行**。本轮引用这些状态，没有把历史 C 观察改称新结果，也没有把 Rust 未运行泛化为两库都没有运行证据。C 仍无到 IA 当前 BS.1770-5 / R128 V5 端点的 implements 边，其上游 BS.1770-4 引用不能自动升级。

本次不访问曾受阻的 crates API、libsndfile 获取或 EBU 音频，不接受下载条款，不尝试上游 conformance suite；那些既有边界继续保留。

## 1. 先固定同一组样本，再转换存储布局

研究比较只取有限、调用方按满刻度缩放且位于 [-1,1] 的 f32 立体声 PCM，采样率 48,000 Hz。Rust 使用 `LoudnessMeter::new(48000, ChannelLayout::Stereo)` 和 `push_stereo_planar_f32(left, right)`；C 使用成功创建的 `ebur128_init(2, 48000, EBUR128_MODE_I)`，保留默认 L/R 映射，不开 histogram、不改历史上限，以 `ebur128_add_frames_float` 输入。

对 N 帧，Rust 的两个数组长度均为 N；C 是 2N 个 float，排列为 `L0,R0,L1,R1,...`，`frames` 参数仍是 N。这一步只重排已固定的 f32 值，不重新生成另一套 double 波形后分别取整。[Rust 输入检查与循环 L512–563](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L512-L563)、[Stereo 权重 L59–65](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/channel_layout.rs#L59-L65)、[C 头文件 L207–232](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.h#L207-L232)及[C 默认映射 L310–352](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L310-L352)支持这组前提。

C float 过滤入口的缩放因子为 1，随后转 double；Rust 同样先从 f32 转 f64。这不证明两者内部运算逐位相同。Rust 使用两个顺序 biquad；C 组合为一组四阶系数，另有 denormal/FTZ 处理。[Rust filter L81–95](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/filter.rs#L81-L95)、[C 系数组合 L286–306](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L286-L306)、[C 过滤 L601–686](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L601-L686)。因此不能以相同输入、标称算法或相近系数预先规定零差值，也不能用其中一个实现充当规范 oracle。

## 2. 完整块数量相同，不等于保存的合格块数量相同

在上述固定配置、从新状态开始、所有输入调用成功且不发生状态重置/历史截断的条件下，两者第一次完整 400 ms 窗口均需 19,200 帧，之后每 4,800 帧有一个新的候选门限块：

- Rust 的 100 ms 子块长度为 4,800；每完成一个子块，从最近四个完整子块产生一个 400 ms 值。[构造及 complete_sub_block L300–414](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L300-L414)。
- C 初始化 `samples_in_100ms=(samplerate+5)/10`，在 48 kHz 同为 4,800；初次 `needed_frames=4*4800`，之后为 4,800。跨调用仍保存未满的 needed_frames 和过滤状态。[C 初始化 L454–508](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L454-L508)、[输入 L978–1045](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L978-L1045)。不推广为任意采样率的相同舍入。

以下为**静态整数推导**，不是测试输出；“候选块”是本文解释用语，不是新增 IA 数据类别。

| 成功输入帧数 N | 可以形成的完整 400 ms 窗口数 | 尚未完成的 100 ms 尾段帧数 |
| --- | --- | --- |
| 19,199 | 0 | 4,799 |
| 19,200 | 1 | 0 |
| 19,201 | 1 | 1 |
| 23,999 | 1 | 4,799 |
| 24,000 | 2 | 0 |

窗口数是 `max(0, floor(N/4800)-3)`；尾段为 `N mod 4800`。Rust 先保留这些窗口的 LKFS 值，再在 finish 筛选；C 在 `ebur128_calc_gating_block` 中先过绝对能量门才保存到队列。因此该表既不是 C 队列长度，也不是最终参与集成的块数。零块必然不能产生此路径的有限集成结果，但一个或多个完整块**不保证**通过门限或得到有限读数。

## 3. 查询与封口，是比较方案需要修正的地方

### Rust：一次 finish 结束一次测量

[finish 与 getter L566–639](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L566-L639)设置 finished，清零未满子块，再计算 integrated；重复 finish 直接返回。初始 integrated 为负无穷，push 不更新该缓存，故 finish 前读取不是在线集成读数。后续 planar push 在入口返回 `Error::Finished`，而不是继续累积。

### C：global 查询并非流结束通知

[gated_loudness / global L1090–1180](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L1090-L1180)遍历已有块能量并给出结果，没有置 finished、刷新不完整窗口或清除输入尾段的操作。正常查询返回后，调用方仍可继续输入。这里的“可继续”限于有效状态、正常分配及所选 API；不是所有错误之后安全继续的承诺。

因此可比较的前缀检查点是：**每个 N 分别新建两库状态，输入同一前缀，Rust finish 后读取，C 在输入成功后查询。** 若要在同一个 C 状态上观察 19,201→24,000 帧，Rust 对应的是另一份重放到 24,000 帧后才 finish 的状态，而不是对已经 finish 的 19,201 帧状态追加 4,799 帧。

这也解释尾段为何暂时“没有影响读数”不等于永久丢失：在 C 中，第 19,201 帧仍可参与后来到 24,000 帧时形成的第二个窗口；在 Rust 的该次已结束测量中，它不进入集成块，且不能靠继续 push 补齐。这里没有声称第 19,201 帧会造成某个确定 LUFS 差值。

## 4. 门限表达式与错误状态，不能被一个浮点结果遮掉

Rust finish 使用 `lkfs > -70`，然后对绝对门通过集合的能量均值换回响度，按 `l > relative_threshold` 筛选；均值包含 log/pow 往返。[Rust L588–617](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L588-L617)、[mean_of_lkfs L683–690](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L683-L690)。

C 的非 histogram 路径在能量域执行绝对 `sum >= pow(10,(-70+0.691)/10)`，相对门为保存能量均值乘 `10^(-10/10)`，再以 `it->z >= relative_threshold` 选块，最后转换为 LUFS。[阈值初始化 L512–516](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L512-L516)、[存块 L708–778](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L708-L778)、[相对筛选 L1117–1152](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.c#L1117-L1152)。

**不能把数学上的“恰等于门限”直接当成已经找到的 PCM。** 滤波初始化、f32 量化、浮点计算与两种门限计算域都可能影响是否到达相等分支。构造并执行边界输入、记录内部/外部观察及误差依据是另一个尚未完成的问题。本轮没有这项证据，也不从 `>` / `>=` 直接宣称可听差异、规范违反或两库不互通。

返回状态同样独立于数值分类。C global 的 SUCCESS 可以伴随 `-HUGE_VAL`；输出参数必须在返回码成功后才解释。Rust 的有效前缀可能先改变内部状态，后面的非有限样本才报错，但 frame_count 只在整批成功后增加。这两个既有事实不能被比较器忽略。[C getter 合同 L233–241](https://github.com/jiixyj/libebur128/blob/67b33abe1558160ed76ada1322329b0e9e058b02/ebur128/ebur128.h#L233-L241)、[Rust L530–563](https://github.com/fishloa/rust-broadcast/blob/579ad2c08b675fc52dee6db4ecb16b3038bb19ce/broadcast-loudness/src/loudness_meter.rs#L530-L563)。本轮正面配方排除非有限值和错误后的复用；不重跑已完成的 C NaN 探针。

## 5. 精确的未执行配方与停止点

下面使用一个明确、无需外部音频的假设输入：从 n=0 开始，`L[n]` 随偶/奇 n 取 +0.25/-0.25；`R[n]` 随 `floor(n/2)` 的偶/奇取 +0.125/-0.125。它们均能被 f32 精确表示，左右不相同以暴露重排错误。这不是校准信号、官方向量或已验证能获得某个 LUFS 的信号。**本轮没有生成这些数组。**

| 配方 | 调用序列 | 源码支持的观察目标，不是实际结果 |
| --- | --- | --- |
| P1 前缀对齐 | 对上表每个 N 分别新建两库；同样本不同布局；Rust finish 后读、C 输入后 query | 完整窗口数与门后集合分开；分别记调用状态、finite / negative-infinity / NaN 分类；实际值未知 |
| P2 分块对齐 | N=24,000；分别一次输入与 19,201+4,799 输入，所有调用成功；Rust 仅最后 finish | 跨 API 调用保存尾段是源码条件；实际跨分块数值一致性仍待观察，不预设逐位相等 |
| P3 中间检查点 | C 输入 19,201、query、再输入 4,799、query；Rust 使用两个新实例分别输入 19,201 和 24,000 并各自 finish | 这是同前缀比较；不在已 finish 的 Rust 实例上模拟 C 的在线查询 |
| P4 封口负对照 | Rust 输入 19,201 并 finish，再尝试追加 4,799；与 C 的 query 后继续明确分开 | 源码预期 Rust 返回 Finished，C query 本身不封口；未调用，不记录为通过或失败实测 |

未来若执行，结果须保留输入字节/哈希、两种布局和 N、库与依赖身份、构建参数、fresh state、每次返回码及原始数值分类；不能把负无穷当作解析失败、把 API success 当作有限测量，也不能只给一个总 pass。比较误差阈值应有独立依据，本报告没有擅定容差。

本研究的完成点是澄清比较前提，不是申请运行批准或新增待审 Canonical 材料。实际数值、门限相等输入、规范误差、真峰值、LRA、多声道、其他采样率、增益归一化、广播交付、性能和安全均未由本次补证；没有修改分类、页面、关系、治理或未来维护方式。
