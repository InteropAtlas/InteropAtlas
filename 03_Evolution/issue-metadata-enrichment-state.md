# Open Issue Metadata Enrichment State

Updated: 2026-09-23 (UTC+8)
Repository: `InteropAtlas/InteropAtlas`
Scope: all currently Open Issues; PRs excluded.

## Governing model

Source of truth:
1. Repository governance defines rules.
2. Issue Labels are the metadata source of truth.
3. GitHub Project is projection only and is out of scope for this task.

Core metadata completeness requires exactly one label in each dimension:
- Lifecycle: `lifecycle:research|active|backlog`
- Area: `area:knowledge|interface|operations`
- Priority: `priority:now|soon|long-term|someday`

Waiting is OPTIONAL. Add exactly one `waiting:*` only when a concrete current waiting condition exists:
- `waiting:prerequisite`
- `waiting:evidence`
- `waiting:scale`
- `waiting:owner`

Do not use `waiting:none`.

## Recovery instructions

A fresh Agent should:
1. Read `docs/03_Operation/02_Governance/github-issue-governance.zh-CN.md`.
2. Read `PROJECT_STATE.md`.
3. Read this checkpoint.
4. Re-run `is:issue is:open` and diff against the processed inventory below.
5. For new/changed Issues, read Title + Body + current Labels + Status + Parent/Dependencies/Blocked By + Acceptance Criteria, and related Parent/Successor when needed.
6. Preserve Lifecycle unless evidence clearly shows a state change.
7. Never infer Waiting from Lifecycle; absence of a waiting label means no explicit waiting condition is currently recorded.
8. After every write batch, re-read GitHub before recording completion.

## Current verified totals

Open Issues: **213**

Lifecycle:
- Research: **7**
- Active: **4**
- Backlog: **202**

Area:
- Knowledge: **67**
- Interface: **44**
- Operations: **102**

Priority:
- Now: **7**
- Soon: **2**
- Long-term: **178**
- Someday: **26**

Waiting conditions:
- Prerequisite: **73**
- Evidence: **67**
- Scale: **39**
- Owner: **4**
- Any explicit waiting condition: **183**
- No waiting label: **30**
- `waiting:none`: **0**

Completeness / integrity:
- Core metadata complete (Lifecycle + Area + Priority): **213**
- Core metadata missing: **0**
- Cross-dimension conflicts detected: **0**
- Final write failures: **0**
- Lifecycle corrections in this enrichment pass: **0**

Verification performed after writes:
- query for missing Area returned 0;
- query for missing Priority returned 0;
- query for `waiting:none` returned 0;
- all Area pairwise-conflict queries returned 0;
- all Priority pairwise-conflict queries returned 0;
- all Waiting pairwise-conflict queries returned 0;
- newest Open Issue remains #433, so the audited 213-Issue inventory has not gained a newer Issue during this pass.

## Batch checkpoints

The enrichment pass covered the same 213-Issue inventory established by `03_Evolution/issue-classification-audit-state.md`.

- Batch 1: #1, #2, #3, #4, #5, #6, #7, #8, #9, #10, #11, #12, #15, #16, #17, #18, #23, #24, #27, #86, #122, #125, #129, #146, #149. Cumulative 25/213.
- Batch 2: #150, #151, #152, #167, #172, #173, #174, #175, #176, #177, #178, #181, #183, #184, #185, #187, #188, #189, #195, #201, #202, #203, #204, #205, #206. Cumulative 50/213.
- Batch 3: #211, #212, #213, #214, #215, #216, #217, #219, #220, #221, #222, #223, #224, #225, #226, #227, #228, #229, #230, #231, #232, #233, #234, #235, #236. Cumulative 75/213.
- Batch 4: #237, #238, #239, #240, #241, #242, #243, #244, #245, #246, #247, #248, #249, #250, #251, #252, #253, #254, #255, #256, #257, #258, #259, #260, #261. Cumulative 100/213.
- Batch 5: #262, #263, #264, #265, #266, #267, #268, #269, #270, #271, #272, #273, #274, #275, #276, #277, #278, #279, #280, #281, #282, #283, #284, #285, #286. Cumulative 125/213.
- Batch 6: #287, #288, #289, #290, #291, #293, #294, #295, #296, #297, #298, #299, #300, #301, #302, #303, #304, #305, #306, #307, #308, #309, #310, #311, #312. Cumulative 150/213.
- Batch 7: #313, #314, #315, #316, #317, #318, #319, #320, #321, #322, #323, #324, #325, #326, #327, #328, #329, #330, #331, #332, #333, #334, #335, #336, #337. Cumulative 175/213.
- Batch 8: #338, #339, #340, #341, #342, #343, #344, #345, #346, #347, #348, #349, #350, #351, #352, #353, #358, #359, #360, #363, #365, #366, #367, #368, #369. Cumulative 200/213.
- Batch 9: #370, #371, #372, #373, #374, #375, #376, #407, #408, #411, #412, #417, #433. Cumulative 213/213; remaining 0.

Each batch was semantically assessed against Issue body/status/dependencies and PROJECT_STATE; final repository-wide re-read queries verified the resulting label state.

## Notable classification notes

- #125, #129, #146, #287 remain Lifecycle Active and Priority Now.
- #408, #411, #433 are Research but Priority Now because their Issue state/current recovery text shows live research activity; this does not convert them to Active Work.
- #24 remains Backlog but Priority Soon and Waiting Owner because implementation work is at review/final-authorization boundary.
- #152 remains Backlog but Priority Soon and Waiting Evidence because its reusable intake contract is intended to follow validated stress-test evidence.
- Conditional-future mechanisms whose need itself is not established are generally Priority Someday and carry the concrete trigger as Evidence or Scale waiting where the Issue explicitly defines such a trigger.
- Backlog alone never generated a Waiting label.
- Active alone never generated absence/presence of Waiting; waiting was judged independently.

## Lifecycle corrections

None.

## Pending / ambiguous queue

None currently requires Owner classification to complete the three core metadata dimensions.

## Conflicts

None detected after final verification.

## Write failures

No unresolved write failures.

During removal of legacy `waiting:none`, remove-label calls for #125, #129, #146 and #287 returned GitHub 404 “Label does not exist”; subsequent repository re-read confirmed `waiting:none` was already absent on those Issues. This is recorded as a transient/concurrent-state observation, not a final failed mutation.

## Next continuation point

The current 213 Open Issues are fully checked for this pass.

Next Agent action is incremental only:
- detect newly opened Issues or materially changed Issue state/dependencies;
- enrich/adjust their labels using the same model;
- append a dated checkpoint;
- do not restart Lifecycle classification from zero unless governance explicitly changes.
