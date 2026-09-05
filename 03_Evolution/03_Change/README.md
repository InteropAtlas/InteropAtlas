# 03_Change

<!-- InteropAtlas Document Metadata v0
Document Status: change_record
Document Created At: 2026-09-01T15:04:02+08:00
Document Updated At: 2026-09-05T14:25:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

这里保存已经进入“准备改变项目本身”阶段的内容，以及理解项目演化所需的迁移与过渡历史。Change 不是当前规则的默认入口；正式生效后的规则应回到 `docs/`、`01_State` 或 `02_Runtime` 的 Primary Home。

## 三个主要入口

1. [`01_Direction/`](01_Direction/) — Roadmap、Route、Phase Plan、Future Direction 与阶段性实施计划。
2. [`02_Architecture/`](02_Architecture/) — 架构草案、设计决策、Contract、兼容性设计与方法形成记录。
3. [`03_Migration/`](03_Migration/) — Current→Target Mapping、迁移预检、Dry Run、边界审计与过渡记录。

它们分别回答：**往哪里变？准备怎样设计？怎样安全迁移？**

## 与 `docs/` 的边界

- `docs/`：现在项目是什么、当前应该遵守什么；
- Change：项目曾经或准备怎样改变，以及这些改变如何被安全实施。

历史材料可以长期保留，但应清楚保持其历史身份，避免被新贡献者误认为当前事实。
