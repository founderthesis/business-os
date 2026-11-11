# r26 proposal: Zoya SLOW on Sonnet exits before work (draft, not built)

Main, 12 Nov ~09:00 JST, for the CTO's 08:45 ask. Read-only: page sizes measured with notion-fetch, nothing written to Notion, nothing built.

## What happened

Since decision 556 put SLOW on Sonnet (11 Nov 21:26), all three runs failed with "early exit at minute 4 to 9", 0 of 30 items done. The 20:17 Opus run worked.

The 00:12 run's report says loading used up its context. **It didn't.** Its session record (get_session cse_019pwcV3k7TMFmqjCdKPvtLT):

| Measure | Value |
|---|---|
| Context used at the end | **321,810 of 1,000,000 tokens** (auto-compact threshold 784,000) |
| Output tokens | 20,004 |
| Length | about 4 minutes |

So it stopped with two thirds of its window free. This is the same early exit as the hourly (stopped at 435k) and WhatsApp (162k): the model judged the load too big and wrote a report. That makes **the gate the first fix, not loading less**. Loading less only lowers the pressure that triggers the judgement.

## What SLOW loads every run (measured 11 Nov)

| Page | Characters |
|---|---|
| SLOW work file (the pin) | 94,833 |
| Rules for Zoya | 65,737 |
| Mail and WhatsApp wording | 63,445 |
| Client show mails | 26,170 |
| Rules for Zoya: follow-ups | 16,782 |
| Cadences | 9,900 |
| Routine pages 1 to 8 | 48,436 |
| Routine page 9 (Community congrats, Proposed, not running) | 2,463 |
| **Total** | **about 327,700 (about 82k tokens)** |

The 20,000-character slice prints of the big pages (each slice re-echoed in Bash output) and the fetches that come back inline roughly double what lands in context. That's consistent with about 200k tokens used by the end of loading, before any work.

## How much of it SLOW needs (from the pages' own sections)

| Page | SLOW needs | FAST or nobody |
|---|---|---|
| Rules for Zoya | about 37k: intro, audit corrections, who sends what, rules for every mail, the SLOW parts of section 5, WhatsApp, never followed up | about 29k: fresh pitches (3), replies (4), the booking and recording parts of 5 |
| Wording page | about 11k: intro, payment reminder and received, release (4), team mail and team WhatsApp | about 52k: Akshay's account (0), fresh-pitch replies (1, less payments), booking (2), after recording (3), and **Retired: do not send (6.9k, needed by nobody)** |
| Client show mails | about 13k (estimate): the three pitch sheets, C2, C17, C20 to C24 | about 13k: booking templates |
| Routine pages | only the categories due this run | the rest; page 9 is not running |

## Options

**1. The gate in the SLOW task (recommended first, about 200 bytes).** SLOW's OUTCOME CHECK IN CODE already prints Failed for an early exit. Add the same sentence the hourly and WhatsApp got:

> GATE: while it prints Failed and `date -u` shows under 22 minutes since the start, write nothing final: go back to the first unfinished item, work it, and check again.

- It goes in the SLOW task (15,646 bytes, room to spare), so the pin doesn't move.
- **I'd ship this with or without anything else, and before switching back to Opus.** Opus will hit the same judgement on a heavy day.

**2. Load routine pages only for the categories due (small, about 300 bytes in the SLOW file).**
- After SLOW BATCH selects, load the routine page of each selected item's routine (followup seq-N maps to routine N, nurture to 7), plus Cadences and the follow-ups page always.
- Page 9 is never loaded.
- **Saves 0 to 48k characters a run:** a typical batch of 30 touches 3 or 4 routines, so about 30k.
- **Risk:** low. RULES LOAD's "read = total" check then runs over the pages actually needed. The order changes: select first, then load.

**3. Section-scoped load of the two big pages (larger, about 600 bytes in the SLOW file).**
- Both are too large to come back inline, so the fetch is saved to a file and SLOW already prints them in python slices. The python can print only the needed `##` sections, chosen by heading text:
  - **Rules for Zoya:** all but sections 3 and 4;
  - **Wording page:** the intro, sections 4, 5 and 6, and the payment templates in section 1, never the Retired section.
- RULES LOAD's line becomes "<page>: <read> of <SLOW sections total> (sections: ...)", so the check stays measurable.
- **Saves about 75k characters a run.**
- **Risk:**
  - A heading renamed on the page drops a section silently. The fix: the python fails the load when an expected heading is missing.
  - A rule that SLOW needs could sit in a FAST section. The audit corrections and section 5 stay whole, so I'd keep section 5 entire (it's mixed). That costs about 11k of the saving.

**4. A cached digest (not recommended).** A repo file distilled from the pages, refreshed when a page's last-edited time changes.
- It saves the most, about 150k.
- But it's a second copy of the rules: decision 357 says never keep a record in two places, and CLAUDE.md says rules live on Rules for Zoya. Every page edit would need a rebuild and a review before SLOW sees it.
- Drift is exactly the failure the pin and RULES LOAD were built to prevent.

**5. One Notion edit, outside the prompts (the CTO's, about 10 seconds).** Move the wording page's "Retired: do not send" section (6.9k) to a subpage. Every routine that loads the page, the hourly too, stops reading 14 dead templates.

## Recommendation

1. **Now:** the gate in the SLOW task (option 1), plus moving the Retired section off the wording page (option 5). The gate is about 200 bytes with the pin unchanged.
2. **r26b:** due routines only (option 2). It's simple and safe, and cuts about 30k.
3. **Only if Sonnet still exits after the gate:** section-scoped load (option 3), with the missing-heading guard.
4. **Not the digest.**

On Opus versus Sonnet: the gate is what makes either model finish. I'd keep Sonnet (decision 556, cost) if the gate holds on the first two runs. I'd go back to Opus only if it doesn't.

Page sizes: subagent measurement 11 Nov, notion-fetch text length per page. Raw report in the session scratchpad.
