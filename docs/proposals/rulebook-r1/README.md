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

## Cutover (CTO)

1. Cleanup reviews this folder read-only and reports sizes and sha256 against manifest.json.
2. `python3 docs/proposals/rulebook-r1/build.py --check` shows no drift.
3. Commit the prompts. Write `release.json` with `{"slow_work_commit": "<that commit>"}`, rebuild (the SLOW prompt gets the work file's commit and hash), commit again: that commit is RELEASE. `build.py --release` fails if the stamp is missing.
4. Fetch the five Notion pages fresh, run `apply_notion.py`, read the output, write each page, read it back to the end.
5. Copy routines/zoya-day.md (with the RELEASE line filled), CLAUDE.md and seeds/composer-seed.md over the live files in one commit.
6. Apply decisions-edits.md.
7. Let the day chat roll over to a fresh chat; edits don't reach a running conversation.
8. Watch the next natural runs against fixtures.md and Sent. Never resend a done action to prove the cutover.
