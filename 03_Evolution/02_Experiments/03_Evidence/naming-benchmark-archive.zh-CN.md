# Naming Benchmark 候选归档

当前 Naming Benchmark 的执行事实源仍为 GitHub Issue #410；本目录中的 `naming-benchmark-proposals.json` 是用于检索、机器处理和长期保存的实验候选归档镜像。

## 使用规则

- 每个正式生成候选都必须进入 `naming-benchmark-proposals.json`；
- Issue #410 保留完整生成解释、method-fidelity review、screening、checkpoint 和 benchmark 结论；
- JSON 归档至少保存 `candidate_id / arm / round / ordinal / name / generation_status / source_issue / source_comment`；
- 后续如需完整机器读取，可逐步把 rationale、construction、strengths、risks、screening outcome 等字段从 Issue 回填进 JSON；
- JSON 不覆盖或取代 Issue 中已经存在的历史记录，避免形成第二套互相冲突的事实源。

## 当前覆盖

截至本文件建立时，已回填：

- G0：1–40，共 40 个正式候选；
- G1–G8 Round 1：尚待从 #410 批量回填。

后续生成的新候选应在 generation checkpoint 时同步进入 JSON，而不是只存在于 Issue 评论中。
