# HLS DateRange 零时长的有限内存往返实验

<!-- InteropAtlas Document Metadata v0
Document Status: bounded_experiment_record
Document Created At: 2026-11-05T12:16:15+00:00
Document Updated At: 2026-11-05T12:17:26+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / test_hls_daterange_evidence
  Reviewer: Independent Agent — OpenAI / dot / review_hls_daterange_evidence
  GitHub Actor: ff6962757
-->

## 问题与结果

[HLS 静态研究](../../01_Research/01_Prior_Art/hls-playlist-media-signaling-2026-11-05.zh-CN.md)发现了 DateRange 输出中的 truthiness 分支；[六维对照研究](../../01_Research/03_Tests/coverage-dimension-reconciliation-2026-11-05.zh-CN.md)将显式零 DURATION 的保持问题列为可继续缩小的证据缺口。本次只回答：在固定标签位置，m3u8 6.0.0 经 `loads → 模型 → dumps → 同库 loads` 是否保留零值与省略值的区别？

**九个固定输入中，显式 DURATION=0、PLANNED-DURATION=0 均先进入模型成为 float 0.0，输出时对应属性被省略，再解析后成为缺失字段和模型 None。** 非零对照 2.5 / 3.5 保持其数值，省略对照继续省略。固定 ID、START-DATE 字符串和 PROGRAM-DATE-TIME 的时间值保持。

这将一个静态推导收窄为有限的实际执行结果。再解析方仍是同一库，不是独立消费者；没有验证 FFmpeg、媒体读取、SCTE 命令或完整 HLS 符合性，也没有扩大任何 Canonical implements 关系。

## 固定输入和执行边界

- 仓库基线为 [`079e7b053ef1a8aadb57f2ae512043ef342fb282`](https://github.com/InteropAtlas/InteropAtlas/tree/079e7b053ef1a8aadb57f2ae512043ef342fb282)。原研究自己的基线、日期、来源与静态结论保持历史原样，不被改写为本次运行结果。
- Linux x86_64 / CPython **3.12.14**；官方 PyPI **m3u8 6.0.0** wheel。发行元数据要求 Python >=3.7；唯一条件依赖 `backports-datetime-fromisoformat` 仅适用于 Python <3.11，本环境未安装或加载该依赖。
- 下载后核对官方 PyPI 的 wheel SHA256 和大小；安全解包到独立目录，不安装、不构建、不运行 setup 或 hooks。全部八个包内 Python 文件与固定提交 [`49417d05602fc472b518ec61aa9b327cd00e079d`](https://github.com/globocom/m3u8/tree/49417d05602fc472b518ec61aa9b327cd00e079d) 的文件逐字节相同，包括原研究已记录的 `__init__.py`、`parser.py`、`model.py`、`protocol.py` 指纹；未修改上游文件。
- 九个夹具是 DURATION 的省略、0、2.5 与 PLANNED-DURATION 的省略、0、3.5 的笛卡尔积。每个输入不足1 KiB，含一个 DateRange 和一个普通 EXTINF/URI；ID 固定为 `probe`，START-DATE 和 PROGRAM-DATE-TIME 固定为 `2024-01-01T00:00:00Z`。没有 END-DATE 或 END-ON-NEXT；没有 SCTE 属性。
- DateRange 位于 PROGRAM-DATE-TIME 之后、普通 EXTINF/片段 URI 之前。`segment.ts` 只是内存中的惰性字符串，没有对应媒体输入或文件读取。调用 `loads` 时不提供 URI 或自定义回调，使用 `M3U8` 默认 `strict=False`；仅用 `dumps()` 返回字符串，不调用 `load()`、`dump()`、下载方法或媒体执行器。
- `-I -S -B` 隔离启动、跳过 site、不写字节码；执行前核对完整13文件清单和每个文件哈希。CPU 上限20秒、地址空间512 MiB、文件大小1 MiB，外层超时30秒。脚本拒绝优化模式和非 CPython3.12 环境；复现环境的 patch 版本另见结果。
- 导入上游前安装 audit guard，阻止 socket、子进程/进程启动、ctypes 及所列文件写入/变更事件。八个合成事件自测均被拒绝，真实导入和九个实验没有触发阻止事件。合成事件没有实际创建 socket、启动进程或写文件。此保护只能防止意外外部操作，**不是安全沙箱或操作系统网络隔离**，参见 [CPython 限制](https://docs.python.org/3.12/library/sys.html#sys.addaudithook)。本次没有重试先前不可用的网络命名空间或 bwrap 路径。

## 逐层观察

结果同时记录初始文本、解析字典、模型值及类型、完整 dumps 字符串、输出 DateRange 属性名和再解析结果，避免把“接受输入”误写成“保持语义”。以下每个零值/非零值均与另一个属性的三种状态组合过：

| 输入属性 | 初次解析字典与模型 | 输出属性 | 再解析字典与模型 |
| --- | --- | --- | --- |
| DURATION 省略 | 字典无该键；模型 None | 省略 | 字典无该键；模型 None |
| DURATION=0 | 字典有键；模型 float 0.0 | 省略 | 字典无该键；模型 None |
| DURATION=2.5 | 字典有键；模型 float 2.5 | 保留 2.5 | 字典有键；模型 float 2.5 |
| PLANNED-DURATION 省略 | 字典无该键；模型 None | 省略 | 字典无该键；模型 None |
| PLANNED-DURATION=0 | 字典有键；模型 float 0.0 | 省略 | 字典无该键；模型 None |
| PLANNED-DURATION=3.5 | 字典有键；模型 float 3.5 | 保留 3.5 | 字典有键；模型 float 3.5 |

以 DURATION=0、PLANNED-DURATION 省略这一行为例：

```text
输入：#EXT-X-DATERANGE:ID="probe",START-DATE="2024-01-01T00:00:00Z",DURATION=0
输出：#EXT-X-DATERANGE:ID="probe",START-DATE="2024-01-01T00:00:00Z"
模型：duration float 0.0 → NoneType None
```

按原研究核对的 [RFC8216 §4.3.2.7](https://www.rfc-editor.org/rfc/rfc8216.html#section-4.3.2.7)，显式零时长与未知持续时间不同。三个 DURATION=0 输入均没有 END-DATE、END-ON-NEXT；输出丢失 DURATION 后，即使仍有非零 PLANNED-DURATION，也不能将实际持续时间解释为已知零。PLANNED-DURATION=0 的丢失则是预计时长信息的变化，不能混同为每种组合的实际持续时间都从已知变为未知。例如 DURATION=2.5、PLANNED-DURATION=0 输出后仍保留实际持续时间2.5。

九个 DateRange 的 ID 与 START-DATE 字符串均原值保持。PROGRAM-DATE-TIME 经 datetime 解析后按默认输出格式变成 `2024-01-01T00:00:00.000+00:00`，再解析时间值相同；这不是原始文本逐字节保持，也不是日期合法性、媒体时钟或时区组合的完整验证。

## 来源、证据与复现

- [官方 PyPI 6.0.0 元数据](https://pypi.org/pypi/m3u8/6.0.0/json)与 [wheel](https://files.pythonhosted.org/packages/f8/31/50f3c38b38ff28635ff9c4a4afefddccc5f1b57457b539bdbdf75ce18669/m3u8-6.0.0-py3-none-any.whl)：24133字节，SHA256 `566d0748739c552dad10f8c87150078de6a0ec25071fa48e6968e96fc6dcba5d`。
- [指纹清单](../03_Evidence/hls-daterange-probe-20261105-manifest.json)：包含发行文件、完整解包清单、八个固定提交来源及与 wheel 的比较。清单是文件库存，不冒充模块加载轨迹。PyPI JSON 指纹只标识本次读取，发行元数据今后可能变化。
- [实验脚本](../03_Evidence/hls-daterange-probe-20261105.py)与[完整结果](../03_Evidence/hls-daterange-probe-20261105-result.json)：脚本不下载、不安装；读取旁边的清单与已解包依赖，只向标准输出写 JSON。断言固定这些观察，不建立 CI gate 或持续维护合同。

复现时下载上述 wheel 并核对大小、SHA256，解包到新的空 `deps` 目录。拒绝绝对路径、`..`、反斜杠路径、重复项、符号链接和其他非普通文件；限定少于100项及总解包大小小于2 MB。不要运行任何安装/构建脚本。保留 wheel 中全部13个文件，不加入其他依赖或缓存。然后在仓库根目录运行：

```bash
timeout 30 python -I -S -B \
  03_Evolution/02_Experiments/03_Evidence/hls-daterange-probe-20261105.py \
  --deps /absolute/path/to/deps > /tmp/hls-daterange-result.json
```

执行者复跑所得结果字节一致；独立复核从同一已验证 wheel 另行安全解包、复制脚本和清单后复跑，结果也逐字节一致。哈希如下，独立复跑不等于跨实现互通：

| 产物 | SHA256 |
| --- | --- |
| 脚本 | `23704a07d5efe3562ced01bcad80bdfa0f8d3220bad8fc12670eeb9ad35ec7e4` |
| 清单 | `a38d1b5c4dbb277d456b2bc3e82ae6f3e578a23cc7e21511c81e5c07034fa85c` |
| 结果 | `b5030ff9126fcf9f1f243b68f8ad5a653e5054bab0ed23356ef65fc815f06fb9` |

## 保留的未知

本次只回答上述两个数值字段在指定位置、版本和环境中的保持问题。未验证其他 DateRange 位置/数量、其他字段/未知属性、END-DATE 或 END-ON-NEXT 组合、strict 模式、任意浮点数、恶意输入、全部 RFC 约束、日期语义、独立消费者、SCTE-35 二进制内容/命令时间、媒体时间线、FFmpeg 或实际拼接，也未运行上游全套测试。未下载网络播放列表/媒体、解码、启动流服务或发送信令。

这份有限执行证据只落在既有 Evolution 入口，不修改 Canonical、导航成员、Runtime、页面、日期快照或六维定义，不表示整体底图完成。PR #680/#683/#684/#672/#591/#498/#416、PROV-O、NMOS、RO-Crate、Tomli 与2026-10-31不确定发布事项的既有 holds / 未决状态均不因本实验改变。
