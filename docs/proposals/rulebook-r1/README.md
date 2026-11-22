# Rulebook r1 (staged, not live)

The system-wide rulebook cleanup Akshay asked for on 22 Nov (audit page 42019a301a7f81eb82d0cc814724b24e). Everything here is staged: the live day chat still reads routines/zoya-day.md and the 83e8fb0 prompts until the CTO cuts over.

| File | What it is |
|---|---|
| change-map.md | Each subject: authority, losing clauses, final wording, consumers, verification; before and after sizes |
| questions.md | The only questions Akshay must answer, each with a default |
| fixtures.md | Offline replay cases and expected outcomes |
| decisions-edits.md | Decisions ledger rewrites and Trash list, for the CTO at cutover |
| edits.py, build.py | Pinned prompt bytes plus edits, built into prompts/ and manifest.json |
| prompts/ | The rebuilt routine prompts (built output; never edit by hand) |
| notion_edits.py, apply_notion.py | Notion page edits, applied to a fresh fetch at cutover |
| routines/zoya-day.md | The new day instructions |
| claude-md/ | The staged CLAUDE.md and its diff |
| seeds/ | Staged seeds |
| prompts/upkeep.txt | The sweep's live steps, built from its own text; the day chat runs it once a weekday |
| routines/host-boards.md, routines/editing-checks.txt, routines/cowork-evals.md | Staged copies of the sources of stored prompts and the evals routine |
| recipients.py | RECIPIENTS as code, with fixture tests |
| routines/cto-round.txt | The CTO coordination round's stored prompt, staged for the CTO to deploy |
| inventory.md | Every worker and what it reads, stored prompts included |

## Cutover (CTO)

1. Cleanup reviews this folder read-only and reports sizes and sha256 against manifest.json.
2. `python3 docs/proposals/rulebook-r1/build.py --check` shows no drift.
3. Commit the prompts. Write `release.json` with `{"slow_work_commit": "<that commit>"}`, rebuild (the SLOW prompt gets the work file's commit and hash), commit again: that commit is RELEASE. `build.py --release` fails if the stamp is missing.
4. Create data/rulebook-r1/ids.json (git-ignored) with the two group chat ids from the live routines/zoya-day.md. Fetch every page in notion_edits.PAGES fresh (eighteen), run `apply_notion.py`, read the output, write each page, read it back to the end.
5. Move the four Rules for Zoya history child pages (inventory.md) under an archive page before writing Rules for Zoya.
6. Copy routines/zoya-day.md (with the RELEASE line filled), CLAUDE.md, seeds/composer-seed.md, routines/cowork-evals.md, routines/host-boards.md and routines/editing-checks.txt over the live files, and deploy routines/cto-round.txt as the CTO coordination round's stored prompt (trig_019sfzEHt9djonNhbxcATgYA) in one commit; delete skills/notion-business-os. Update the Host boards and the three Sarika's editing asks stored prompts from those files and byte-compare the readback.
7. Apply decisions-edits.md.
8. Let the day chat roll over to a fresh chat; edits don't reach a running conversation.
9. Watch the next natural runs against fixtures.md and Sent. Never resend a done action to prove the cutover.
