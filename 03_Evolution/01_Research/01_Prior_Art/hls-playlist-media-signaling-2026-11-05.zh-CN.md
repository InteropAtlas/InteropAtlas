# HLS 文本、媒体读取与定时信令的有限对照

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Comparison
Document Created At: 2026-11-05T05:47:21.084395+00:00
Document Updated At: 2026-11-05T05:49:54.416371+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Independent Agent — OpenAI / dot / review_hls_crossdomain
  GitHub Actor: ff6962757
-->

## 问题与结论

已有 m3u8、FFmpeg、HLS 和 SCTE-35 记录，是否就能建立“读入播放列表、取到媒体、按节目时间完成拼接”的完整链？**不能。所录关系分别覆盖播放列表文本处理、选定媒体读取路径、可选信令的文献映射；它们没有共同的播放或拼接执行证据。**

本次还直接读取固定 m3u8 的 DateRange 路径，找到比原实现边更具体的研究证据：`SCTE35-CMD` 可作为字符串进入模型并输出，但该路径不解码 splice_info_section；日期属性也是字符串。相对地，固定 FFmpeg HLS 解析器没有 DATERANGE 分支，落入通用注释跳过路径。这些差异解释了为何**文本可承载、媒体可读取、命令可解释**仍是不同问题，不判定整个库不存在其他能力。

基线固定为 [`a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c`](https://github.com/InteropAtlas/InteropAtlas/tree/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c)。[既有 intake 导航](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/Inbox/relations/intake-coverage-20260913.yaml)中，HLS、m3u8、SCTE-35 位于 `media_network`，FFmpeg 位于 `image_color`。本文沿这些已有入口连接媒体描述、读取和信令问题，不新建或推断分类成员，不用记录数量表示覆盖完整度，也不是整体互操作底图完成声明。

## 版次与既有边

- HLS 目标仍为 **RFC 8216，2017年8月，Informational Independent Submission**，描述 HLS 协议第7版，不是 IETF Standards Track，也不纳入后来 Apple/LL-HLS 扩展。
- m3u8 **6.0.0** 是 Python 库版本，固定 commit `49417d05602fc472b518ec61aa9b327cd00e079d`，不等于 HLS 协议版本6。
- FFmpeg **9.0.2** 固定 commit `946fcce07b6dcd0331c8cc609192aeff5e1924f8`，具体构建和组件可用性未运行验证，不宣称最新版本。
- SCTE-35 目标保留现有工作级 ID `scte35`，按 RFC8216 §11.1 限定 **ANSI/SCTE35，2014年8月**。本次没有通读或执行该标准的二进制命令解码。

| 既有关系 | 已记录范围 | 不得从它推导的下一步 |
| --- | --- | --- |
| `python_m3u8_implements_hls_rfc8216` | 已有字符串经 loads/M3U8、parse 字典、Media Playlist 模型到 dumps；选定 EXTINF、URI、TARGETDURATION、MEDIA-SEQUENCE、VERSION、PLAYLIST-TYPE、ENDLIST、EXTM3U 路径。默认非 strict，严格模式也仅做部分检查；输出有规范化和省略。 | URI 被记录不等于媒体已下载；文本成功不等于完整校验、播放或 SCTE-35 支持。原边排除后续扩展与网络，其选定正面范围未覆盖 SCTE35，不因本研究新增静态观察而扩大。 |
| `ffmpeg_implements_hls_rfc8216` | 固定 hls.c 选定标签/URI读取与受支持的未加密 MPEG-TS 片段经可用子解复用器打开；受调用方流选择、协议/扩展名约束、IO、构建组件、后端和子解复用器条件限制。 | 允许扩展名不是编解码兼容；不推出所有标签、完整版本7客户端、动态质量切换、加密/DRM、fMP4/CMAF、播放或任意构建可用。原边及代码中的排除项仍保留。 |
| `hls_rfc8216_uses_scte35` | 固定 §4.3.2.7.1 的可选 DateRange 表示，具体限第二段 SCTE35-CMD 的四类命令和相应时间绑定。 | HLS 对 SCTE-35 的文献 uses 不传递成两个库的 SCTE-35 implements；不保证命令解码、广告交付、无缝拼接或实际互通。 |

原始关系文件分别是 [m3u8](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/python-m3u8-rfc8216.yaml)、[媒体传输实现](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/media-transport-implementations.yaml)、[HLS-SCTE35](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/hls-scte35-signaling.yaml)。按明确 relation ID 读取完整 context；FFmpeg 还存在 DPX、FFV1 等其他关系，本次没有把它们纳入所选片段或重新核验。

## 可选信令的规范条件

这里直接核对 [RFC8216 §4.3.2.6](https://www.rfc-editor.org/rfc/rfc8216.html#section-4.3.2.6)、[§4.3.2.7](https://www.rfc-editor.org/rfc/rfc8216.html#section-4.3.2.7)、[§4.3.2.7.1](https://www.rfc-editor.org/rfc/rfc8216.html#section-4.3.2.7.1) 的有限条件：

- 源媒体 SCTE-35 拼接信息 **MAY** 用 Media Playlist 的 EXT-X-DATERANGE 表示，不是所有 HLS 播放列表的必选特性。
- 包含 `splice_null()`、`splice_schedule()`、`bandwidth_reservation()` 或 `private_cmd()` 的 splice_info_section **SHOULD** 用 SCTE35-CMD 表示，值为整个 section 的大端二进制十六进制序列。不把 SHOULD 升为 MUST，也不把属性名称当作二进制语义验证。
- DateRange 的 ID 和 START-DATE 是 REQUIRED；有 DateRange 的播放列表 MUST 至少含一个 EXT-X-PROGRAM-DATE-TIME。SCTE35-CMD 的 START-DATE MUST 对应命令中的 splice_time；若命令不带该时间，则对应它出现在源流中的节目时间。
- PROGRAM-DATE-TIME 将下一 Media Segment 的第一个样本关联到绝对日期/时间，原文引用 ISO/IEC8601:2004。本文没有因此制造 HLS→RFC3339 的边，也没有核验媒体时钟同步或日期换算。
- DURATION 必须非负，单一瞬间 SHOULD 用0表示。若没有 DURATION、END-DATE 或 END-ON-NEXT=YES，持续时间是未知，即使有 PLANNED-DURATION。本条件用于理解下述输出差异，不代表完整 DateRange 符合性审计。

`splice_insert()`、`time_signal()`、segmentation_descriptor 的其他映射、所有一致性规则及§8.10例子的解释不扩入本次结论。

## 新的静态观察：文本载体不等于命令处理

以下是本研究新读取的源码路径，单独留在 Research，不更新 Canonical implements 或给库增加能力断言。载体分析限定默认 strict=False、无自定义回调、DATERANGE 位于后续普通 EXTINF/片段 URI 之前；不保证悬在尾部而没有后续片段的标签被保留。

[m3u8 parser.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/parser.py) 的 DATERANGE 分支进入 `_parse_daterange`：id/class/start_date/end_date 去掉引号，duration/planned_duration 转 float，scte35_cmd/out/in 使用 str；结果先进入 state，随后被选中 segment 路径取走。[model.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/model.py) 构造 DateRange 对象，Segment.dumps 在片段前输出这些标签。

`DateRange.__init__` 通过 kwargs["id"] 取 ID，其他成员通过 kwargs.get 获取；`DateRange.dumps` 仅在属性 truthy 时输出 START-DATE、DURATION、PLANNED-DURATION 和 SCTE35-CMD。由这段控制流可作以下有限静态判断，**不是运行结果**：

- 非空 SCTE35-CMD 字符串被拼入输出；该选中路径没有解码或验证完整 splice_info_section，没有把其命令时间与 START-DATE 对齐。
- 日期字符串的保存和再次加引号不是日期合法性、时区或节目时钟验证。缺失/空 START-DATE 会被这段输出省略；源码注释讨论规范例子，但本文不采用注释作为规范解释，也不把它升级为标准矛盾结论。
- 解析所得数值 `0.0` 在 duration/planned_duration 的 truthiness 检查中为假，因此该属性不会由这段 dumps 输出。这与“显式零时长”和“没有持续时间信息”的区别有关；没有把它泛化为所有输入、所有调用或整库符合性裁决。
- 上述路径的存在也不保证未知属性、所有 DateRange 标签位置或文本字节无损往返；本文没有执行示例、测试或真实播放列表。

[FFmpeg hls.c](https://github.com/FFmpeg/FFmpeg/blob/946fcce07b6dcd0331c8cc609192aeff5e1924f8/libavformat/hls.c) 的选中 `parse_playlist` 没有 EXT-X-DATERANGE 分支；未匹配的 `#` 行经通用 Skip/continue 路径跳过。它也没有 EXT-X-VERSION 分支，因此不能把媒体读取路径当作完整协议版本验证。这里不判断 FFmpeg 的全部 demuxer、媒体内 SCTE 数据处理、下游不连续性或播放器功能是否存在，更没有建立 m3u8 输出与 FFmpeg 输入的组合测试。

## 可复查的机器读取

下方只按三个明确关系 ID 选取记录，再读取实际端点与现有导航；它刻意不是 FFmpeg 的全部邻接图。沿用既有 loader/normalizer，保留完整 context/evidence/provenance，不创造传递边、第二事实源或新接口。断言只重现本次选择，不增加 CI gate。

```python
from pathlib import Path
import sys,json,yaml
root=Path('/path/to/checkout-at-a9320267').resolve()
sys.path.insert(0,str(root/'02_Runtime/01_Engine'))
from bootstrap_query import load_atlas,index_objects
from relation_model import normalize_relation
objects,relations=load_atlas(root)
index=index_objects(objects)
relation_ids={'python_m3u8_implements_hls_rfc8216','ffmpeg_implements_hls_rfc8216','hls_rfc8216_uses_scte35'}
selected=[row for row in relations if row['id'] in relation_ids]
assert {row['id'] for row in selected}==relation_ids
ids={normalize_relation(row).source_id for row in selected}|{normalize_relation(row).target_id for row in selected}
assert ids=={'python_m3u8','ffmpeg','hls_rfc8216','scte35'}
nav=yaml.safe_load((root/'01_State/Inbox/relations/intake-coverage-20260913.yaml').read_text())
memberships=[row for row in nav['memberships'] if row['ref']['id'] in ids]
print(json.dumps({'objects':[index[key] for key in sorted(ids)],'relations':selected,'navigation_memberships':memberships},ensure_ascii=False,indent=2,default=str))
```

固定输出的四个对象、三条关系和四项导航引用只是查询范围，不是媒体域或实现全集的分母。正式记录中没有某条组合边、或本次未验证某个实现，不表示现实中没有方案。

## 剩余问题与边界

如果以后选择具体工作流，仍需单独证明文本处理是否保留所需信令、消费者如何读取它、完整 SCTE 命令内容/时序是否正确，以及媒体样本与节目时间的对应和实际拼接结果。这个列表是未完成的证据问题，不是部署批准、测试排期或新增维护义务。

本次没有下载网络播放列表/媒体、安装/构建/执行上游、播放内容、启动流服务或发送信令。只做固定源文件阅读和 Atlas 自身查询/检查。它不重新验证全部历史记录，不修改 Canonical、导航成员、Runtime、分类或关系语义，不用这一片段替代其他领域或整体底图工作。

## 来源与文件指纹

一手文件为本次下载并静态读取的完整字节，URL 固定出版物或提交。散列只识别来源，不证明执行、完整审计或所有记录正确；不镜像第三方全文。

| 一手文件 | SHA256 |
| --- | --- |
| [rfc8216.txt](https://www.rfc-editor.org/rfc/rfc8216.txt) | `954910a5ad73506cfdb5abe11571f6b859d49d1f82191ffe616595a40687e58e` |
| [m3u8/README.md](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/README.md) | `2e749a45c85e45f667f51c733504598ad0ca4bfdaec75df50a390751bbd909e8` |
| [m3u8/m3u8/__init__.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/__init__.py) | `3b7d07eb3dc43dff194e5e42508e2f5043ef432d9a116e70cb42e7c35e0526c7` |
| [m3u8/m3u8/parser.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/parser.py) | `9227b3d5d722f124dfe0578939e8eaf45023458b4df218b3c6dee2cad28f2ae1` |
| [m3u8/m3u8/model.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/model.py) | `c125c13aed8b5c037381d9604dbb101e3f3a9a7c136a0a661641d5bd58b1ff8c` |
| [ffmpeg/libavformat/hls.c](https://github.com/FFmpeg/FFmpeg/blob/946fcce07b6dcd0331c8cc609192aeff5e1924f8/libavformat/hls.c) | `fd08aae89dc14520501ffa231597a0e47dd959e3fa62d264d2dbfb8298bcaaa9` |
| [ffmpeg/doc/demuxers.texi](https://github.com/FFmpeg/FFmpeg/blob/946fcce07b6dcd0331c8cc609192aeff5e1924f8/doc/demuxers.texi) | `d8dfe0ac1ea18fc30d85471a11d6b1a9641c997706cce0407020e87629de9491` |
| [m3u8/m3u8/protocol.py](https://github.com/globocom/m3u8/blob/49417d05602fc472b518ec61aa9b327cd00e079d/m3u8/protocol.py) | `b1bbb5407d727735c43862325e5e96642703e1f1b30d847afecacaf13542e469` |

IA 输入均固定到上述基线；整关系文件哈希不扩大被选关系的范围。

| IA 输入 | SHA256 |
| --- | --- |
| [01_State/01_Objects/ffmpeg.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/01_Objects/ffmpeg.yaml) | `6b09dad411033e3ac9b2d0a4281613106372173ab7ba7a3679692e7516b12bec` |
| [01_State/01_Objects/hls_rfc8216.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/01_Objects/hls_rfc8216.yaml) | `ba577b88444de6633c4a7f77e1d2f545a8b5f5dbad1d0622c814150fcd9ead0b` |
| [01_State/01_Objects/python_m3u8.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/01_Objects/python_m3u8.yaml) | `26d71860ca1d06f72136124dd46d72b890e29b21f810c4f7cdf11562e58c9bd2` |
| [01_State/01_Objects/scte35.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/01_Objects/scte35.yaml) | `9e44cd3ddd12987d68cbd330635d20bc39864228b9c2fdb06de1c25cd3aacaf2` |
| [01_State/02_Relations/hls-scte35-signaling.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/hls-scte35-signaling.yaml) | `fcb42bcf05c619f708e40146c632fa310fb16a4abb299e577810d34886658454` |
| [01_State/02_Relations/media-transport-implementations.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/media-transport-implementations.yaml) | `3d9fc04842ad47da02df84010d2904c89037c737655eb33d6caf4a395bd5db3b` |
| [01_State/02_Relations/python-m3u8-rfc8216.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/02_Relations/python-m3u8-rfc8216.yaml) | `b9a7744230d05b6cb811e5425b81da33f4eef32ab5a83081eb67a5e2516d1ae9` |
| [01_State/Inbox/relations/intake-coverage-20260913.yaml](https://github.com/InteropAtlas/InteropAtlas/blob/a9320267aed8581cd2d6b17dd1cda2cd5d1a7b9c/01_State/Inbox/relations/intake-coverage-20260913.yaml) | `45d0270be0bdfed6609b0ac17ae2fe985804d598e9f99a21bdcfc87c9c796efc` |
