# Syslog 读写组合的有限内存实验

<!-- InteropAtlas Document Metadata v0
Document Status: bounded_experiment_record
Document Created At: 2026-11-05T05:15:24.694258+00:00
Document Updated At: 2026-11-05T05:17:27.272260+00:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / dot / advance_coverage_basemap
  Reviewer: Agent — OpenAI / dot / review_syslog_runtime (independent)
  GitHub Actor: ff6962757
-->

## 问题与结果

[消息组成研究](../../01_Research/01_Prior_Art/syslog-message-composition-coverage-2026-11-05.zh-CN.md) 从源码指出，格式化库与解析库的存在不等于无损往返。本次把其中四个问题收窄为可重复的本地观察：转义值是否还原、BOM 如何进入解析结果、重复参数是否保留，以及 PROCID 字面形式是否保留。

**在下述固定环境和输入中，格式化后的消息可经显式严格 UTF-8 解码再被解析，但这条组合并不保留全部应用值。** 特殊字符的结构化参数仍带协议转义；MSG 中的 BOM 成为 U+FEFF；重复参数在公开字典中只留下最后一个值；`0012` 变成整数 `12`。这些是该环境、该版本、该输入的执行观察，不是所有输入的推断，也不是整个标准、传输或部署的符合性结论。

## 执行边界

- Canonical 基线固定为 [`626ede0b12e965f41739f02593baa3712282fc00`](https://github.com/InteropAtlas/InteropAtlas/tree/626ede0b12e965f41739f02593baa3712282fc00)，没有更改对象、关系、Canonical 导航成员或 Runtime。两个库的 object-only 状态保持不变。
- Linux / CPython 3.12.14；`rfc5424-logging-handler==1.4.3`、`syslog-rfc5424-parser==0.3.2`、`lark-parser==0.6.7`、`tzlocal==5.3.1`、`pytz==2025.2`。这是明确选定的现代实验环境，不是上游历史环境或原始依赖锁定。`TZ=UTC` 使用系统 ZoneInfo UTC。
- 下载来源为官方 PyPI，逐包核对 SHA256。仅解包 wheel 和 lark 源码目录；没有执行 `setup.py`、安装钩子或更改全局 Python 环境。没有把第三方源码复制进仓库。
- 格式化采用上游原样构造器，显式传入 `io.BytesIO()`、固定 hostname/appname/PROCID，时间固定为 `1704067200.0`。只调用 `build_msg`，断言流始终为空；不调用 `emit`、`transmit` 或网络构造器。手写输入另行标记，不冒充格式化库能生成重复参数。
- 唯一衔接步骤是 `wire.decode('utf-8', errors='strict')`，没有去除 BOM、反转义、分帧或其他适配。观察文法层 `parser.parse`，再观察公开 `SyslogMessage.parse(...).as_dict()`；前者用于区分语法接受与字典映射。
- 执行前验证所有封存的 Python / Lark 源文件哈希；用 `-I -S -B`、显式依赖路径、20 秒 CPU / 512 MiB 地址空间限制和外层 30 秒超时运行。输入共 12 个，均小于 1 KiB；这个数量只是夹具范围，不是覆盖完整度。
- 导入上游前安装 CPython audit hook，阻止 socket、子进程、进程启动和 ctypes 事件；用合成事件自测，真实实验没有触发阻止事件。它是防止意外外部操作的保护，不是安全沙箱或操作系统网络隔离。[Python 的相应限制](https://docs.python.org/3.12/library/sys.html#sys.addaudithook)同样适用。此环境的独立网络命名空间不可用，未绕过该限制。

## 观察与限定

| 有限问题 | 本次观察 | 不能由此推出 |
| --- | --- | --- |
| 普通文本与可选 MSG | 普通文本 `hello`、无 BOM 的中文保留；空消息在格式化结果中省略，解析 MSG 为 null。 | 所有文本编码或非法字节均受支持。 |
| UTF-8 BOM | 开启 `msg_as_utf8` 时，字节中的 `EF BB BF` 经严格解码后成为解析 MSG 开头的 U+FEFF。 | 解析器必须替应用移除 BOM，或网络消息一定显示异常。 |
| SD 转义 | 空值和中文保留；反斜杠、双引号、右方括号及其组合均被接受，但参数值仍是格式化后的转义文本，不等于输入应用值。JSON 中的反斜杠还会再按 JSON 规则显示，不能凭屏幕字符数量判断协议内容。 | 所有转义形式都被接受；或该库整体不符合 RFC 5424。 |
| 重复 SD-PARAM | 单一 `probe@32473` 元素内两次 `p` 在文法结果中都存在；公开 `sd` 字典只保留 `second`。这是手写合法重复参数形状，不是重复 SD-ID。 | 格式化器的 Python dict 能生成重复键，或这项丢失适用于所有上游/下游系统。 |
| PROCID | 格式化器保留消息头字面值 `0012`，解析后为整数 `12`；非数字 `worker-12` 仍为字符串。 | PROCID 是必须解释为整数的协议字段。 |

十项格式化输入记录实际 wire hex 和解码字符串；两项手写输入只记录原始文本。所有输入的文法参数序列与公开结果均保存在 [结果 JSON](../03_Evidence/syslog-composition-probe-20261105-result.json)。断言只固定这些观察，不把全部成功解析计作完整符合性。实验未调用解析对象的 `__str__`，因此也没有测量再序列化后的字节往返。

## 来源对应与复现

[清单](../03_Evidence/syslog-composition-probe-20261105-manifest.json)记录五个发行包的哈希，以及解包所得的 Python / Lark 源文件指纹（包括未执行的文件，不是加载轨迹）。parser 的 `message.py`、`parser.py` 与研究中固定提交 `578bf58922a8cb90c3340f072a307721642cb8ff` 字节相同。handler 的 `handler.py`、`transport.py` 与提交 `8426fd9d143accbfccd1db43553729a53b3f08e9` 并非字节相同：wheel 使用 CRLF，GitHub 源码使用 LF；只将 CRLF 转为 LF 后完全一致。实验执行 wheel 原字节，未修改上游。

发行元数据：
- [syslog-rfc5424-parser 0.3.2](https://pypi.org/pypi/syslog-rfc5424-parser/0.3.2/json)
- [rfc5424-logging-handler 1.4.3](https://pypi.org/pypi/rfc5424-logging-handler/1.4.3/json)
- [lark-parser 0.6.7](https://pypi.org/pypi/lark-parser/0.6.7/json)
- [tzlocal 5.3.1](https://pypi.org/pypi/tzlocal/5.3.1/json)
- [pytz 2025.2](https://pypi.org/pypi/pytz/2025.2/json)

在独立目录下载清单中同名发行包并核对 SHA256。将四个 wheel 解包至空的 `deps` 目录；从 lark sdist 只取 `lark-parser-0.6.7/lark/` 到 `deps/lark/`，不要执行 setup.py。解包时拒绝绝对路径、`..`、符号链接和硬链接。Linux 下这些版本没有额外必须依赖：tzlocal 的 tzdata 条件只适用于 Windows，开发 extras 不启用。

在仓库根目录运行 [实验脚本](../03_Evidence/syslog-composition-probe-20261105.py)：

```bash
timeout 30 python -I -S -B \
  03_Evolution/02_Experiments/03_Evidence/syslog-composition-probe-20261105.py \
  --deps /absolute/path/to/deps > /tmp/syslog-composition-result.json
```

脚本只读取旁边的指纹清单并向标准输出写 JSON，不自行下载或安装依赖。必须在普通断言启用的 Python 中运行，不使用 `-O`。相同环境复跑的观察和结果字节应一致；不同 Python 版本的环境字符串可能变化，行为差异需单独记录，不能覆盖本次原始结果。

## 留下的未知

这次只把原研究中的几个静态未知收窄为明确输入下的执行证据。原版 RFC 5424 全部约束、后续修订/勘误、恶意输入与资源耗尽、无效 UTF-8、全部转义组合、时间范围校验、传输分帧、TLS、网络重连、消息送达和生产可用性都未验证。未新增接口、分类、CI gate 或以后必须遵循的维护要求；不以该实验推进库的 implements 关系。原研究其余未知和所有历史 holds 保留。
