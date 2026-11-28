# Zoya r22: hand-off to Cleanup and the CTO

Main, 6 Nov. Nothing is deployed, the pin ref isn't moved, and nothing was written to Notion.

## Builds

Built twice, byte-identical, no em dash, no "SLOW run" or "FAST run".

| File | Bytes / sha256 |
|---|---|
| zoya-one.txt (hourly) | 62,583 / 481f1ed1fef68dad |
| zoya-slow.txt (SLOW task, pin 79bc21a) | 15,239 / e91cf1448dd7e400 |
| routines/zoya/release/zoya-slow-work.txt at 79bc21a | 90,074 / a2b5e2962e9b519f |
| zoya-episodes.txt (not live) | 48,718 / 6396ad26e35c9257 |

**Command:** apply `build_one.patch` at f70901f. It adds `r21_edits.py` (r21 plus Cleanup's C1) and `r22_edits.py`. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 79bc21ad802f1728697870fec91fc4ca9b0ea141`.

**Base proof:** with the r22 list empty, the build reproduces the live hourly. The only difference is the version stamp: live is 58,053 / 187b4f54 and carries r21's stamp, because C1 was applied to the built file after it was stamped. The SLOW task and SLOW file reproduce r21's a81e3bc6 and 9d74718b exactly.

## What r22 adds

1. **L1:** a no-repo run writes a Failed record, "Run <routine> <start> JST: Failed: no repo, lock not checked" (hourly, SLOW task, episodes).
2. **L2:** before RELEASE, the record is re-fetched and asserted in python. Its Summary must no longer end "Started" and must start with the status that STATUS IN CODE printed (hourly), or that 4/'s OUTCOME CHECK printed (SLOW). On a miss: retry once and re-fetch, then add "record status write failed".
3. **Note checks (all four files):**
   - Only a notion-fetch is a read of the note; SQL, rows mode and slices never count.
   - N1: new == line + "<br />" + old (or new == line on an empty note).
   - N2: after the write, the stored note, escapes normalised, ends with the old note.
   - SLOW outcome lines carry "chk:<old>+<line>+<6 or 0>=<new> fetch", and 4/ marks a missing or wrong chk: as unfinished.
4. **Hourly status in code:** one line per FAST step (0e, 0e2, 0r, 1, 1-72h, order), plus the "sends" and "stop:" lines. A python STATUS IN CODE step prints the status:
   - No-op when no step was due.
   - Partial for a short RULES LOAD, or for a proven cap, tool error or minute 25.
   - Anything else is Failed "early exit at minute <n>".

   Rules loading, thread length or cost is never a reason. The step names are my proposal; please confirm them.
5. **SENDS ARE MESSAGE-IDS:** the unit for every count or comparison of sent mail is the Message-ID, never the Sent item.
6. **PaaS (Akshay, 6 Nov):**
   - **Scope:** rows on the Show named PaaS come into SCOPE.
   - **Gate:** until the wording page's four PaaS toggles all read approved, Zoya sends nothing on those rows. She notes each unanswered inbound once and reports it.
   - **After approval, Akshay's:** price, scope, terms, discounts, custom packages, meetings, references, a call with anyone but Akshay, a no, a "not now" with no date, a yes, and anything she's unsure of. She sends at most the holding reply on these.
   - **After approval, Zoya's (hourly):** booking a call with Akshay, and re-sending the row's own podm.in proposal link. That link is approved for that row only, and the HARD links rule carries the exception.
   - **Zoya's (SLOW):** PAAS FOLLOW-UPS. These are built from Activity dates (metadata only):
     - New or Contacted: day 4 and 10 from Akshay's first mail.
     - Interested: day 3, 7 and 14.
     - Proposal sent: day 3 questions, day 7 call offer, day 14 "should we keep this open?", then to Akshay.
     - Monthly nurture only on his word; Parked rows quarterly with a reason.
   - **Keys and categories:** follow-ups count in "STEP 2 follow-ups", and nurture is keyed as nurture.
   - **Migration segment:** the "PaaS row moved from Deals" segment is no hold, and the first PaaS send clears it.
   - **Wording:** comes from docs/proposals/paas-move/templates.md, once Akshay approves.

## Replay

replay/zoya22.md ran on the first r22 build (3af3584). Every defect it raised is fixed in this build, D1 to D18:
- **D1, the most urgent:** the chk: sum now counts the separator.
- **D10 and D11:** the call rule follows the PaaS page, where booking with Akshay is Zoya's. Akshay can change that.

Not re-run on this build. Cleanup's review is the check.

## Open

- PaaS rows are matched by the Show's name. Swap in the page id once the CTO creates the PaaS Show.
- MESSAGE IDENTITY still has its own "Two Sent copies with one Message-ID are one send" sentence, which SENDS ARE MESSAGE-IDS now repeats. It's harmless; cut it next round.
- r20 (decision 467, Cleanup C1 open) still needs rebasing onto r22.
