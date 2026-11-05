# 从 TinyCBOR 无符号整数编码前缀到 libcbor token 解码

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Fixed-source conditional handoff
Document Created At: 2026-11-05T21:12:00+00:00
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

本次是 **源码推导研究**，不是跨库执行实验。全部 110 个组合用例均为 `UNEXECUTED`，`actual_result: null`；十个值向量同样明确标记未执行。结论只是在下述真实缓冲、回调和平台前提成立时，两份固定实现的选中路径给出相互对齐的字节、值和消费长度预期。尚不能说「TinyCBOR 实际产出已被 libcbor 成功接收」。

## 固定来源与范围

基线是 [InteropAtlas 2b2e1672](https://github.com/InteropAtlas/InteropAtlas/tree/2b2e1672af71b575e5af2eaf766d10c2dc28868e)。冻结依据为 [TinyCBOR 完整复核包](https://github.com/InteropAtlas/InteropAtlas/blob/b7747706710c98bb1bd8e60455762f5e341d9e19/01_State/Inbox/review-packets/tinycbor-v7.1-20261105.yaml) 与 [libcbor 完整复核包](https://github.com/InteropAtlas/InteropAtlas/blob/9129b198b9549b95ea2715ea48c64ca862d06f14/01_State/Inbox/review-packets/libcbor-0.12.0-20261104.yaml)。TinyCBOR 7.1 是 release/tag 身份，固定 CMake project VERSION 仍是 7.0，不声称核对了二进制版本。

通过 GitHub 连接器按固定 commit 重新取得 12 份完整源码/接口文档，逐一计算 Git blob SHA-1（含 Git 对象头）、字节数、SHA256，均与冻结 manifest 一致；返回的 GitHub blob SHA 亦一致。[机器证据](cbor-uint-handoff-2026-11-05.json)内嵌逐文件 manifest 与固定公开链接。核对范围是这些文件，不是整个源树、发布归档、签名或构建产物。未安装、导入、构建或运行上游库、依赖、测试、生成器；参考脚本只用 Python 标准库做整数算术、证据组装与自检。

- TinyCBOR 固定 commit `da6421f2b5b91e3468c0af7265117427ea73f19e`：`cbor.h`、`cborencoder.c`、`cborinternal_p.h`、`cborinternalmacros_p.h`、`compilersupport_p.h`。
- libcbor 固定 commit `ae000f44e8d2a69e1f72a738f7c0b6b4b7cc4fbf`：`streaming.c/.h`、`callbacks.h`、`data.h`、`internal/loaders.c/.h`、`doc/source/api/streaming_decoding.rst`。

只连接 `cbor_encoder_init(&encoder, buffer, 9, 0)` 后恰一次 `cbor_encode_uint` 的实际长度前缀，与一次 `cbor_stream_decode` 的 major type 0 回调。不是新增 Canonical 互通关系，也不涉及工业协议组合、UI、工作流或项目规范变更。cbor2 原有 35 项观察（1 版本、34 行为）保持独立且未改动，不能拿来替代本组合的运行证据。

## 源码链与前提

[编码路径](https://github.com/intel/tinycbor/blob/da6421f2b5b91e3468c0af7265117427ea73f19e/src/cborencoder.c#L195-L370) 先初始化 remaining=2，编码时减为1；`encode_number_no_update` 依值域选择内嵌或1/2/4/8字节大端参数，随后 `append_to_buffer` 复制对应片段。[长度接口](https://github.com/intel/tinycbor/blob/da6421f2b5b91e3468c0af7265117427ea73f19e/src/cbor.h#L280-L288) 由输出指针减原 buffer 得到长度。

条件必须同时成立：

1. 新鲜、有效、相互不重叠、可写的 `CborEncoder` 和真实9字节缓冲，生命周期覆盖调用，无并发修改，`buffer+9` 合法。flags 恰为0，`CBOR_ENCODER_WRITER_CONTROL` 为默认0，无自定义 writer，只编码一次。
2. `uint8_t` 是8位 unsigned char，`uint64_t` 占8字节，所选 `cbor_htonll` 分支正确产生网络字节序。`would_overflow` 分别将指针转为 `ptrdiff_t`：转换后的 end 非零，与转换后的 buffer 的差恰为9，之后所有减法均有定义且不溢出。真实可写空间本身不足以证明这些平台前提。
3. libcbor 的端序配置正确，固定宽度整数类型和 [loaders 的移位、整数提升](https://github.com/PJK/libcbor/blob/ae000f44e8d2a69e1f72a738f7c0b6b4b7cc4fbf/src/cbor/internal/loaders.c#L12-L49) 均有定义。普通32位 int、8位 byte、正确端序配置的平台是这里的限定目标，不把源码推导提升为所有 C 平台可移植性结论。
4. decoder 输入指向真实、稳定、生命周期有效的字节对象；`source_size` 如实反映提供长度且不超过分配范围。空前缀也使用真实非空指针，仅长度为0；不借助伪缓冲或越界指针。
5. 回调表及 context 有效，四个 uint 回调类型与 [接口签名](https://github.com/PJK/libcbor/blob/ae000f44e8d2a69e1f72a738f7c0b6b4b7cc4fbf/src/cbor/callbacks.h#L20-L63) 一致、可调用且正常返回。记录器保留完整 uint64 值，不转入有损浮点或有符号窄类型；不修改输入或回调表，不发生数据竞争，每个独立用例重置记录器。
6. 只传输返回长度的前缀，不传未写后缀、不用 strlen。编码可以含零字节，也不附加 NUL。尾字节用例另备 `L+1` 字节真实缓冲，最大10字节；不能往9字节编码缓冲后越界追加。

在这些条件下，预期 encoder 返回 `CborNoError`，`cbor_encoder_get_buffer_size` 返回已写长度 L（JSON 字段 `get_buffer_size_result`，不是分配容量9），extra_bytes_needed=0，remaining=1，未写的9−L字节保留原内容。

## 十个整数的精确预期

以下全为 **UNEXECUTED，actual_result=null**。每行恰一次回调，回调值等于首列，decoder status=`CBOR_DECODER_FINISHED`，read=L，required=0。uint8 等是回调字段名，按 wire width 选择，不是按应用希望的统一类型选择。

| 十进制值 | 编码前缀 hex | L | 回调 |
| --- | --- | ---: | --- |
| 0 | 00 | 1 | uint8 |
| 23 | 17 | 1 | uint8 |
| 24 | 1818 | 2 | uint8 |
| 255 | 18ff | 2 | uint8 |
| 256 | 190100 | 3 | uint16 |
| 65535 | 19ffff | 3 | uint16 |
| 65536 | 1a00010000 | 5 | uint32 |
| 4294967295 | 1affffffff | 5 | uint32 |
| 4294967296 | 1b0000000100000000 | 9 | uint64 |
| 18446744073709551615 | 1bffffffffffffffff | 9 | uint64 |

推导依据是 [streaming.c 的初始化、claim_bytes 与 0x00..0x1b 分派](https://github.com/PJK/libcbor/blob/ae000f44e8d2a69e1f72a738f7c0b6b4b7cc4fbf/src/cbor/streaming.c#L11-L122)，以及上述 loaders。机器证据将所有整数值保存为十进制字符串并提供 hex，避免 JSON 消费端把 uint64 最大值舍入。

## 所有截断前缀、重试与尾字节

对每个完整前缀长度 L，穷列 k=0..L−1 共40个截断前缀，均 **UNEXECUTED / actual_result=null**：

- k=0：预期 `CBOR_DECODER_NEDATA`、read=0、required=1、零回调。此时 decoder 尚不知道最终 token 长度，只要求先取得首字节。
- 1≤k<L：预期同一 NEDATA、read=0、required=L、零回调。required 是从当前 token 起点计的所需输入总长，不是缺少量 L−k。
- k=L：对应表中完整用例，FINISHED/read=L/required=0，一次 uint 回调。

[data.h 第255行](https://github.com/PJK/libcbor/blob/ae000f44e8d2a69e1f72a738f7c0b6b4b7cc4fbf/src/cbor/data.h#L243-L257) 的空输入注释写了 read=1，与 `streaming.c` 的 `claim_bytes` 赋值不一致。本研究以固定实现为依据，明确预期 required=1、read=0，不复制该注释错误。

每个截断用例另配一个无状态重试用例，共40个，亦 **UNEXECUTED / actual_result=null**。第一次 NEDATA 后保留此前缀，补齐字节，再从原 token 起点把完整 L 字节重新提交；不能只提交新到字节，也不能按 k 推进输入指针。预期第一次无回调，第二次给出完整用例的一次回调。函数没有内部流解析状态；应用自己保留缓冲与记录器状态。重试并不保证应用回调幂等，也不授权把已经 FINISHED 的 token 重新提交当作续读。

每个完整整数分别追加 `00` 和 `ff`，共20个尾字节用例，亦 **UNEXECUTED / actual_result=null**。第一次解码仍只预期一次原整数回调、read=L、required=0，尾字节位于偏移L且未消费；没有第二次解码或尾字节回调的观察。即使尾部为 `ff`，第一次 FINISHED 也不是对完整输入的合法性认可。若应用要求单一完整项，必须在自己的封装层另检消费边界；本研究不实现该封装。

这里的110不是已执行测试数量，也不是一般覆盖率的分母。机器证据共110个组合用例：10完整、40截断、40重试、20带尾字节。静态覆盖这些选中分界，不等于穷尽 uint64、平台、配置、CBOR 数据模型或传输协议。

## 结论与未完成事项

已经建立一个可独立复核、可供未来实验使用的有界预期矩阵：编码前缀长度、解码回调和值、read/required、截断与尾部边界均能落到固定源码。源文件哈希核对和参考算术是本次实际完成的核验；上游行为和跨库组合运行次数仍为0。

未证明完整文档消费、完整确定性 CBOR profile、RFC整体符合性、安全、性能、生产部署、跨平台可移植性或跨实现运行成功。最短整数头只是这条路径的局部事实，不能提升为完整确定性编码认证。未来若获准执行，仍需先固定编译器、平台、宏配置，验证真实缓冲和回调记录器，再运行本矩阵并单独记录实际结果；本报告不把该未来步骤当成已经发生。
