# #287 分支与 PR 整理归档

此 tag 是历史保留引用，不是发行版、当前规则或工作分支。**不要把此归档提交链合入 main。**

manifest.json 为逐分支决定和完整 SHA、77 项实际 tree 等效证据；source-inventory.json.gz 为完整原始分页审计快照。归档提交的父提交链只用于保证所有原分支及 PR 提交可达，不表示接受其代码、规范、方法或实验。

恢复：`git fetch origin refs/tags/archive/maintenance-287-2026-09-11:refs/tags/archive/maintenance-287-2026-09-11`，从 manifest 查原 SHA，使用 `git switch -c recover/<name> <original_sha>`。浏览中间脚本用 `git log <sha>` / `git show <sha>:<path>`。恢复分支或运行旧脚本需新的工作授权；本次不恢复命名 benchmark。

实时执行结果及后续 head 漂移见 Issue #287；此处记录冻结基线，不冒称所有计划均已执行。
