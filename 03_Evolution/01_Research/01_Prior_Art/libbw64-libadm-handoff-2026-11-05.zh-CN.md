# libbw64 与 libadm：从 AXML 字节到音轨关联的责任交接

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Static Evidence
Document Created At: 2026-11-05T13:26:00+00:00
Document Updated At: 2026-11-05T13:26:00+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_bw64_adm_boundary
  GitHub Actor: ff6962757
-->

这是一份有限源码研究，不是运行报告、规范符合性结论或新的维护合同。仓库基线为 `abba37b66f23b52a14e6aa1151cd3563fdd5a8f8`。研究延续[既有领域审计](../02_Audits/domain-evidence-actions-2026-11-05.zh-CN.md)中 editing 与 metadata 的共同问题，明确 `ebu_libbw64`、`ebu_libadm` 与既有 `libbw64_recommended_with_libadm` 关系之间的证据边界；不新增对象、分类或技术边，也不修改 Canonical、Runtime、页面或 held 工作。

## 已有证据与这次新增的问题

既有关系只记录 libbw64 0.10.0 README 的无日期、工作级 libadm 推荐。目标记录固定 0.14.0，不会把建议变成已测版本配对、强制依赖或兼容性认证。[既有关系](https://github.com/InteropAtlas/InteropAtlas/blob/abba37b66f23b52a14e6aa1151cd3563fdd5a8f8/01_State/02_Relations/audio-library-implementations.yaml)与[原接纳包](https://github.com/InteropAtlas/InteropAtlas/blob/abba37b66f23b52a14e6aa1151cd3563fdd5a8f8/01_State/Inbox/review-packets/audio-library-implementations-20261020.yaml)保留这一范围。

[#583](https://github.com/InteropAtlas/InteropAtlas/pull/583) 已记录默认小文件输出、采样率参数窄化、PCM32 精度、非 XML AXML 字节及 CHNA trackIndex=99 的有限运行结果。它还公开保留独立探针代码、真实输出、原始构建失败和配置适配后的结果。这次引用这些既有观察，不重跑或把它们计作新增覆盖。原 #456 接纳审核是已完成历史；libadm 的 README/CHANGELOG 补充同样不是从未核查，但它们没有回答具体 XML 接口的责任交接。

新问题是：**当同一段自制 XML（不称为完整 ADM 合规节目）经 libbw64 读出并交给 libadm，ADM 内部引用解析成功是否足以证明 CHNA 把它关联到了正确音轨？** 两个只在 CHNA UID 上不同的合成小文件可以把这个问题与旧的 trackIndex=99 反例分开。

## 固定来源与静态责任路径

固定 libbw64 0.10.0 commit `3a43f909f7e8f6bef93403816e9b73b8bfa5a133`，libadm 0.14.0 commit `1f3e87dc37736ed42104969f00b6c4cbd43221e6`。32 份选定完整源文件（204731 字节）按固定 Git tree/blob 核对，另留 SHA256；这证明取得字节与所指 Git 对象一致，不是发行者签名或与历史捕获逐字节相同的证明。没有运行上游库或测试。

1. **文件与块层。** libbw64 的 [reader.hpp L168–181](https://github.com/ebu/libbw64/blob/3a43f909f7e8f6bef93403816e9b73b8bfa5a133/include/bw64/reader.hpp#L168-L181)分别返回 CHNA/AXML 对象，缺少相应块时可返回空指针。[AxmlChunk L238–258](https://github.com/ebu/libbw64/blob/3a43f909f7e8f6bef93403816e9b73b8bfa5a133/include/bw64/chunks.hpp#L238-L258)保存字节并可写入 ostream。因此调用方可以先检查块存在，再把 AxmlChunk::write 的字节交给独立的输入流。这里没有把字节读出升级为 XML 或 ADM 验证。[CHNA parser L119–168](https://github.com/ebu/libbw64/blob/3a43f909f7e8f6bef93403816e9b73b8bfa5a133/include/bw64/parser.hpp#L119-L168)读取固定宽度 ID 字段、检查声明计数；这些结构检查仍存在。

2. **XML 入口及封套。** libadm [parseXml](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/include/adm/parse.hpp#L45-L65)接受 XML 文件名或 istream，没有 CHNA、PCM 通道数、采样率或位深参数。[实现 L43–98](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/xml_parser.cpp#L43-L98)调用 RapidXML 后选择封套搜索路径。默认必须是 `ebuCoreMain → coreMetadata → format → audioFormatExtended`，后三层在各自父节点中恰有一个同名节点，见 [L110–129](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/xml_parser.cpp#L110-L129)。`recursive_node_search` 则递归找到第一个同名 audioFormatExtended，见 [L140–152](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/xml_parser.cpp#L140-L152)。它不是对所有封套、namespace 或多份 ADM 的验证。头文件 [L25–36](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/include/adm/parse.hpp#L25-L36)的“尚未实现选项”注释与随后的枚举及实际分支不符，不能用这句旧注释否定该选项。

3. **ADM 身份与内部引用。** [parseAudioTrackUid L430–445](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/xml_parser.cpp#L430-L445)要求 UID，检查重复 ID，读取可选 sampleRate/bitDepth 与 track/channel/pack 引用。UID 解析另检查长度 12、`ATU_` 前缀和八个十六进制字符。必填 UID 缺失进入 [parseAttribute 的异常分支](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/include/adm/private/xml_parser_helper.hpp#L147-L160)。已提供的引用在 [resolveReference L140–150](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/include/adm/private/xml_parser.hpp#L140-L150)中查找，不存在则抛出 XmlParsingUnresolvedReference；track/channel 引用还互斥。没有提供某个可选引用与提供一个无法解析的引用不同。公开 parseXml 先加载 [内嵌 common definitions](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/parse.cpp#L9-L21)，不能把“当前 XML 没有定义该 ID”直接判作“无法解析”。

4. **写出并非原 XML 字节保真。** [AudioTrackUid](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/include/adm/elements/audio_track_uid.hpp#L28-L35)明确列出 audioMXFLookUp 未支持。已读 parser 不把这个子树存入 AudioTrackUid，所读 [formatter L662–673](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/rapidxml_formatter.cpp#L662-L673)只生成 UID、可选 rate/depth 和三类引用。因而这里是支持字段的对象化与重新生成路径，不能承诺任意 XML 内容往返保留。此为静态调用链判断，尚无新增运行观察。writer 的 `itu_structure` 确实生成 `ituADM → audioFormatExtended`，见 [wrapper L24–28](https://github.com/ebu/libadm/blob/1f3e87dc37736ed42104969f00b6c4cbd43221e6/src/private/rapidxml_wrapper.cpp#L24-L28)；这种输出再进 parser 时仍须明确选择相应搜索选项。

5. **文件与 ADM 的关联仍是调用方工作。** 对这组明确选定的 API，CHNA 没有作为参数进入 libadm。XML 内部引用解析不能比较 CHNA.uid 与 AudioTrackUid UID，不能比较 CHNA.trackRef/packRef 与该 UID 的引用，也不能把音轨索引和 fmt 中通道数、rate/depth 一并核对。libbw64 提供这些原始值、libadm 提供 ADM 对象与引用，调用方需完成所选输入的连接检查。这不否定其他应用或未审 API 可能提供组合校验，也不是所有 ADM/BW64 规则的清单。

## 未执行的最小配对见证

机器可读[来源清单与未执行见证](libbw64-libadm-handoff-2026-11-05.json) 包含精确 XML、固定 CHNA 值、源码依据和空的 actual_result。所有用例均标为 `UNEXECUTED`，未生成或解析任何媒体文件。XML 是本研究自制的引用解析切片，不称为完整 BS.2076 合规节目。

- A/B 共用一个只含本地 track UID、track format、pack format 的 EBU 封套 XML。计划文件都是一个通道、48000 Hz、PCM16、一个零样本的 tiny RIFF/WAVE，CHNA trackIndex=1、numTracks=1、numUIDs=1，完整标识 trackRef=`AT_00031001_01`、packRef=`AP_00031001`。小 RIFF 路径不代表已检验 BW64 大文件路径。
- A 的 CHNA UID 为 `ATU_00000001`，与 XML 一致。B 唯一变化为 CHNA UID=`ATU_00000002`；XML 中没有该 UID，其他数据不变。观察目标是分别记录块读出、XML 对象/引用解析，以及明确调用方检查的结果，而不是把调用方检查写成库自身行为。
- 两个封套控制共用相同 audioFormatExtended 子树：EBU 默认路径；`ituADM → audioFormatExtended` 的默认与 recursive 路径。源码预期默认 ITU 封套找不到节点，recursive 可找到；这些是待运行预期，不是实际输出。
- 必填 UID 缺失、ADM 引用指向不存在的用户自定义 ID 是备用 XML 层控制，不需要在最小 A/B 研究中扩成大量用例。执行前须固定是否采用它们及其前提，尤其核对引用没有命中内嵌 common definitions。

最小成功条件应是保存输入/输出哈希、精确库/编译配置、逐阶段实际结果和调用方检查依据，能证明一组给定输入中各层负责什么。它不会把原 recommended_with 提升成所有输入的兼容性证明。

## 执行准备、未知与复核边界

当前环境只完成源码阅读与字节身份核对。GCC 14.2.0、glibc 2.41 可见，已检查位置没有 CMake 或 Boost 头文件；没有安装依赖、构建 libadm、执行上游测试或运行配对程序。已检查可用环境目录，未发现另一处已授权且可用于此任务的执行环境。这里的准确状态是“未准备及未运行”，不是一般性的不可执行判断。

固定 libadm 的顶层 CMake 要求 Boost >=1.57，src/CMakeLists 实际要求 C++14，而 README 仍称 C++11。源码使用随仓库 RapidXML、生成的 export/version 头和内嵌 common_definitions 资源，Unix 链接 dl。资源生成脚本使用 list(POP_FRONT/PREPEND/JOIN) 和 string(PREPEND)，所以不能只用顶层 CMake 3.5 声明证明实际最低版本。针对这组尚未执行用例，候选准备方案是选择具体、已审的现代 CMake 与 Boost，核对完整固定树及必要构建脚本，以 library-only 配置关闭 tests/examples/package-and-install，输出只落在隔离临时目录；该方案不涉及服务、系统安装或绕过下载/环境限制，不构成未来执行许可或项目维护规则。此次决定不进行这一步。

独立复核应检查：固定文件身份与引用行号；default/recursive 分支及 stale comment；UID 的 required/optional 区别、common definitions 和引用互斥；A/B 只改变 CHNA UID；预期与实际状态分离；不从片段推论完整符合性；既有 #583 观察及推荐关系不被改写。若以后运行，审核还须分开文件字节核查、库行为、调用方连接检查与完整标准规则，保留任何构建失败或未运行项。

本次不处理 #680/#683/#684/#672/#591/#498/#416、既有身份 hold 或结果不确定的历史发布；亦不以这些 hold 阻止本次独立静态核对。
