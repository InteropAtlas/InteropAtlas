# P5 Bounded Intake Batch 1 — Source / Dedup Preflight v1 Draft

> Lifecycle: Historical / Completed P5 Experiment Artifact
> Original Work Item: #136
> Checked At: 2026-09-04

本文件记录首批 5 个 Candidate 的官方来源确认、基础去重与身份预检。它不写入生产 Canonical，不冻结最终 V1 Schema。

## Experiment summary

代表性候选：RFC 9114、ISO/IEC 27001:2022、Fetch Living Standard、FAPI 2.0 Security Profile、BCP 47 / RFC 5646。

结果：
- RFC 9114 → proceed ordinary intake；
- Fetch Living Standard → proceed with lifecycle/freshness boundary；
- ISO/IEC 27001:2022 → defer；
- FAPI 2.0 Security Profile → defer；
- BCP 47 / RFC 5646 → duplicate/existing overlap。

实验验证了 immutable publication、editioned standard、living standard、profile/framework 与 intentional dedup 等不同 identity / intake pressure，并发现 Candidate Pool carrier、dedup engine 与 experiment fixture / Canonical boundary 等实施摩擦。

完整形成过程仍可从 Git history 恢复；本文保留实验结论和归档身份，不作为当前 Intake Contract。
