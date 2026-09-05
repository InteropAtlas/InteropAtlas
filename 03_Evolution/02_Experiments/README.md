# 02_Experiments

<!-- InteropAtlas Document Metadata v0
Document Status: experiment_record
Document Created At: 2026-09-01T15:04:02+08:00
Document Updated At: 2026-09-05T14:55:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

这里存放尚未进入正式 State / Runtime 的可复现实验、原型、试运行、Dry Run 和验证工作。它回答：**我们实际怎样试过，这个想法能不能工作。**

## 三个主要入口

1. [`01_Foundations/`](01_Foundations/) — 早期 Bootstrap、能力验证、开放替代方案、格式适配与协作基线实验。
2. [`02_Pilots/`](02_Pilots/) — 代表性迁移、Gate walkthrough、bounded intake 等带明确对象与边界的 Pilot / Preflight。
3. [`03_Evidence/`](03_Evidence/) — 实验索引、Gate synthesis、Coverage baseline 等用于证明实验结果的 Evidence。

它们分别回答：**先怎么试？在真实边界里怎么跑？最后留下什么证据？**

编号目录承担人类阅读与注意力导航；无编号资产不参与这三个主要入口的排序。

## 无编号可复现资产

以下目录不是新的主要注意力入口，而是实验所依赖的可执行 / 可复现资产，因此暂时保持稳定路径：

- [`json-ld/`](json-ld/)
- [`rdf-1.2/`](rdf-1.2/)
- [`p5-v1-experiments/`](p5-v1-experiments/)
- [`v1_contract_fixtures/`](v1_contract_fixtures/)

这些路径可能被 Runtime、测试或历史复现流程引用；在没有完成依赖迁移前，不为了视觉整齐强制改名或搬动。

实验结果如果被正式采用，应进入 `01_State`、`02_Runtime` 或 `docs/` 中相应的当前产物；本目录继续保存其试验过程和证据。

## 与 `docs/` 的边界

- `docs/`：当前应该遵守的规范、规则与说明；
- Experiments：我们怎样试过，以及试验结果是什么。

仓库不再维护第二个 `docs/experiments/` 区域。
