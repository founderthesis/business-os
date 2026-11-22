# Rulebook r1: cutover runbook

Window: Sunday 22 Nov, 21:30 to 23:30 JST. The last Sunday wake is 20:38 and Monday's first is 07:38, so no day chat runs during the cutover and Monday's chat starts clean on the new rules. Main runs (a), (b) and (d) when the CTO sends "go cutover". The CTO runs (c). Every step is logged in docs/deploys/rulebook-r1-cutover.md (what ran, the commit or page, read-back result).

Stop rule: if any check below fails, stop at that step, roll that step back, and tell the CTO. Never continue past a failed check.

## 0. Preconditions (Main, read only)

1. `date -u` is between 12:30 and 14:30 UTC on 22 Nov (21:30 to 23:30 JST).
2. No day chat is working: get_session on the Sunday day chat (tag zoya-day) shows idle, and no session tagged zoya-oneshot is working.
3. The zoya-lock is free: `git fetch origin refs/heads/zoya-lock` and its subject starts "free:". Held: stop, wait for it; never touch it.
4. `git fetch origin claude/business-os-structure-k3sqo5 && git merge --no-edit FETCH_HEAD`, then `python3 docs/proposals/rulebook-r1/build.py --check` prints "no drift".
5. Live files unchanged since staging: `git log 5d1e917..HEAD -- CLAUDE.md routines/zoya-day.md docs/composer-seed.md routines/cowork-evals.md routines/host-boards.md routines/editing-checks.txt` prints nothing. If anything printed, stop: the staged copies must be rebuilt from the newer live text first.

## (d) ids.json (Main, before b)

1. `mkdir -p data/rulebook-r1` and write data/rulebook-r1/ids.json with the two group chat ids copied from the live routines/zoya-day.md (the Zoya <> Team group and The Founder Thesis Community), keys ZOYA_TEAM_GROUP_ID and FT_COMMUNITY_GROUP_ID.
2. `git check-ignore data/rulebook-r1/ids.json` prints the path (it is git-ignored). Never commit it.
- Rollback: delete the file.

## (a) Repo, one commit (Main)

1. Release stamp for the SLOW work file:
   - `W=$(git rev-parse HEAD)`; `git show $W:docs/proposals/rulebook-r1/prompts/zoya-slow-work.txt | sha256sum` equals the zoya-slow-work.txt sha256 in manifest.json.
   - Write docs/proposals/rulebook-r1/release.json: {"slow_work_commit": "<W>"}.
   - `python3 docs/proposals/rulebook-r1/build.py --release` (fails if the stamp is missing), then `--check` shows no drift.
   - `grep -c "{SLOW_WORK" docs/proposals/rulebook-r1/prompts/zoya-slow.txt` prints 0.
   - Commit "Rulebook r1: release stamp". This commit is RELEASE: `R=$(git rev-parse HEAD)`.
2. Live files, in one commit:
   - routines/zoya-day.md ← docs/proposals/rulebook-r1/routines/zoya-day.md, with the line "RELEASE: (set at cutover)" replaced by "RELEASE: <R>".
   - docs/composer-seed.md ← docs/proposals/rulebook-r1/seeds/composer-seed.md, with "{release}" left as a placeholder (the day chat fills it from zoya-day.md).
   - CLAUDE.md ← docs/proposals/rulebook-r1/claude-md/CLAUDE.md.
   - routines/cowork-evals.md, routines/host-boards.md, routines/editing-checks.txt ← their staged copies.
   - routines/cto-round.txt ← docs/proposals/rulebook-r1/routines/cto-round.txt (new: the source of the CTO round's stored prompt).
   - Retire: `git mv routines/daily-sweep.md routines/retired/daily-sweep.md`; `git rm -r skills/notion-business-os`.
   - Keep docs/proposals/zoya-day/prompts/ (83e8fb0's copies) in place until Monday evening, as the rollback source; delete it in a later commit after a good Monday.
   - Checks: `grep -c "Overrides on top of" routines/zoya-day.md` prints 0; `grep -cE "[0-9]{8,}[-0-9]*@g\.us" routines/zoya-day.md` prints 0; for every prompt, `git show $R:docs/proposals/rulebook-r1/prompts/<file> | sha256sum` equals manifest.json.
   - Commit "Rulebook r1 cutover: live files", fetch and merge, push. Log both commit ids.
- Rollback: `git revert --no-edit <live-files commit>` and push. The day chat then reads 83e8fb0 again, as before. The release-stamp commit can stay.

## (b) Notion (Main)

Write pages one at a time, in this order, never two writers. Every write uses the plan files, so Akshay's inline comments outside the changed spans stay anchored.

1. Archive the history child pages of Rules for Zoya first: notion-move-pages with ids 3fa19a301a7f81959333c3f38b93c90c (Background, 12 to 14 Oct), 3fa19a301a7f8149bea3eb60422ba660 (Mail feedback, 15 Oct), 3fa19a301a7f814f925ef20c8c4a659c (Routine audit, 16 Oct), 3ff19a301a7f81e2b13ec0b339cd9bbe (Mock follow-ups) to new parent CTO Audit (40419a301a7f81c48c29d894e433750d). Read back each page's parent.
   - Rollback: move them back under Rules for Zoya (3f719a301a7f81a09de3ee3ad6ad98a3).
2. Fresh fetch of all 18 pages in notion_edits.PAGES into data/rulebook-r1/notion-cutover/<short-name>.md (content only, first line a comment with the page id and fetch time). These are also the rollback copies.
3. `python3 docs/proposals/rulebook-r1/apply_notion.py data/rulebook-r1/notion-cutover data/rulebook-r1/notion-new`. It must print every page with no error. It fails on a moved anchor, a lost required title, an unfilled id or a dropped child page. Any failure: stop. That page's edits must be rebased on the new text first.
4. For each page, in the order the script printed them, run data/rulebook-r1/notion-new/<page>.plan.json:
   - "update_content" ops: one notion-update-page call per page, command update_content, content_updates = the ops in order (old_str, new_str, and replace_all_matches where set). Never allow_deleting_content.
   - "replace_content" (fu-1-sponsored, fu-6-release, rules-inbox, links-limits): command replace_content with new_str; never allow_deleting_content. A validation error listing child pages is a stop.
   - A warning that an op matched nothing is a stop for that page.
5. Read back each page with a fresh fetch, and compare it in python with data/rulebook-r1/notion-new/<page>.md (whitespace normalised). Also check it ends with the same last 200 characters. A mismatch: put the page back with replace_content from notion-cutover/<page>.md, then stop.
6. Decisions ledger (collection://cfcc0ef3-3e83-4655-98ed-56ed950b02ec), from decisions-edits.md:
   - Before writing, fetch each row and save its current "What we decided" to data/rulebook-r1/decisions-before.json (the rollback copy).
   - Write each "Rewrite whole" row's What we decided, one row at a time, and read it back.
   - Trash list: first run the grep check in decisions-edits.md on the live files. It must return only decisions-edits.md and change-map.md. Then move each row to Trash.
   - Rollback: write the saved text back, and restore Trashed rows (notion-restore-pages).
7. Update the Notion home and Business OS developer pages as CLAUDE.md asks: one Change log line on the Zoya routine page, "Rulebook r1 cutover: <date>, commit <live-files commit>".

## (c) Stored prompts (CTO, with update_trigger)

Deploy after (a) is pushed. Run `python3 docs/proposals/rulebook-r1/build.py` first: it writes the exact stored-prompt texts to data/rulebook-r1/stored/ (git-ignored, since they carry mail addresses) and their sizes and sha256 to manifest.json. For each one: get_trigger first, and check its stored prompt still equals the live repo text from before cutover, so nobody changed it meanwhile. Then update_trigger with the whole file. Compare the prompt in update_trigger's own result with the file, byte for byte; on a mismatch, redeploy until they are equal. Log each in docs/deploys/.

| Scheduled task | Trigger id | Source file (after cutover) | Bytes | sha256 |
|---|---|---|---|---|
| Host boards | trig_01K8bueCr2xsPkbgQzjeRKsz | data/rulebook-r1/stored/host-boards.prompt.txt, built by build.py from the code block of routines/host-boards.md | 8585 | 8ace96f5e9031c1a4c73b5bcb97352ade4fba31cba75053a543ceb6a7ac4ae16 |
| Sarika's editing asks (11:17, 12:17, 18:17 IST) | trig_01AU4fQevmq39TDZX6LvC4cq | data/rulebook-r1/stored/editing-checks.prompt.txt (routines/editing-checks.txt) | 9067 | 216d73acc272c4f18bd2494586ff4f9885424ea20e782c3aecdd7fc6e9629afd |
| Sarika's editing asks (13:15 IST) | trig_01SXrnWJb2iz5Q3zts34VZu4 | same file | 9067 | same |
| Sarika's editing asks (15:47, 22:47 IST) | trig_0177CBiFc4zP8SGCaVip97Gc | same file | 9067 | same |
| CTO coordination round | trig_019sfzEHt9djonNhbxcATgYA | data/rulebook-r1/stored/cto-round.prompt.txt (routines/cto-round.txt) | 7101 | 366fbeaee7d17fb383f023ffba57bfd77a49e9f55a61acfa928e1c73c83449b0 |

The figures are from manifest.json at the head commit; re-read them there at cutover. Unchanged, so not deployed: the day-wake triggers ("Wake: run what is due now per routines/zoya-day.md"), the monitor ("Check"), FT Community directory sync.

Monday's day chat: the CTO seeds it from the new routines/zoya-day.md, with SLOW at 11:08 and 17:08, upkeep from 13:00, and no sweep. The six sweep duties the CTO bridged by hand as carry-overs are now covered by upkeep.txt, so drop them from the carry-over list.

- Rollback for each trigger: update_trigger with the prompt text saved from its pre-deploy get_trigger (keep those saved texts in data/rulebook-r1/triggers-before/, git-ignored).

## After cutover (watch, never resend)

- Monday 07:38 wake: the wake record shows the RULES GATE read in full, capture's report and loop-in lines, and no send before the gate.
- Monday 11:08 SLOW composer: drafts only; Monday numbers in its run record.
- Monday 13:00+ wake: an "Upkeep <D Mon>" record.
- Check the fixtures against what actually happened, and Sent against the day's Activities. Never resend a completed action to prove the cutover.
