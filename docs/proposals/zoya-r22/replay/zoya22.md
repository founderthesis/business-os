# Zoya r22 offline replay (6 Nov)

Read-only. Files: docs/proposals/zoya-r22/{zoya-one,zoya-slow,zoya-slow-work,zoya-episodes}.txt against zoya-r21, the edit list zw21/routines/zoya/r22_edits.py, and the asks (b-round-5nov "Not carried", zoya-r19 L1/L2, zoya-r20 cleanup-runs-5nov items 1 to 3, paas-move README and templates).

## Mechanical checks

- **Diff maps to r22: PASS.** I applied r22_edits.py to each r21 file in its variants (each old string found exactly once). zoya-slow-work then equals r22 byte for byte. The only other differences:
  - zoya-one: the deployment reference (90338a1ea12c to ab399390cdfd), plus the C1 change on line 81 ("Then the link add on that recording event (the guest's recording invite only, ... Akshay, 5 Nov, item 13)"), which is the live hourly's C1.
  - zoya-episodes: the deployment reference (ee97f93c9684 to 41bd86ad4f6b).
  - zoya-slow: the deployment reference (5793f45c1352 to 5cde1c7ac800), plus the pin (201f730 to 3af3584780e2, sha 9d74718b to 63da4ddf09663834, total 85,084 to 88,634 characters).
  - The pin checks out: `git show 3af3584:routines/zoya/release/zoya-slow-work.txt` equals the r22 file, sha256 63da4ddf09663834..., 88,634 characters.
- **Sizes: PASS.** zoya-one is 61,429 bytes, zoya-slow 15,135 and zoya-episodes 48,642, all under 65,336. zoya-slow-work (88,638) is a pinned file, not a prompt.
- **Banned strings: PASS.** No U+2014, no "SLOW run" and no "FAST run" in any of the four files.
- **Names defined in the same file: FAIL (2 names).**
  - STATUS IN CODE: defined and used only in zoya-one. OK.
  - SENDS ARE MESSAGE-IDS: defined in one, slow-work and episodes. OK.
  - PAAS: defined in one and slow-work. OK.
  - N1 and N2: defined inline in CLAUDE NOTE WRITES in all four. slow-work's 2/ use (line 85) points to line 153 of the same file. OK.
  - RUN RECORD: defined in one, episodes and slow. slow-work relies on the slow task's RUN RECORD, as it always has. OK.
  - **PAAS FOLLOW-UPS:** used in zoya-one's PAAS ("and in SLOW work PAAS FOLLOW-UPS") but defined only in slow-work. That's D8.
  - **CRASH RECOVERY:** the new SENDS ARE MESSAGE-IDS line names it in zoya-one and zoya-episodes, but it's defined only in slow-work. That's D9.

## Scenarios

### P1 (L1, no repo): PASS, hourly and SLOW

The governing line is LOCK in zoya-one:61 and zoya-slow:5: `none: write the run record anyway, created once and never Started first, Summary "Run <this routine, as RUN RECORD names it> <start> JST: Failed: no repo, lock not checked", Source ID as RUN RECORD forms it with the run id from 1. below, then end at once (L1, Cleanup)`.

- **Hourly:** one Activity, Kind Note, Summary "Run zoya <YYYY-MM-DD HH:MM> JST: Failed: no repo, lock not checked", Source ID "run:zoya:<run id>". The run id comes from step 1 (printenv, else syn-).
- **SLOW:** the same, with "Run zoya-slow ..." and "run:zoya-slow:<run id>".

There's no RELEASE, since no lock is held. This matches L1. Nit: the no-repo write has no "fails twice: stop anyway" bound like step 3's. RUN RECORD's "retry once, then report" covers it.

### P2 (L2, a silent Summary failure): PASS, with a nit

RELEASE now runs `after the run record's last write and its check (L2, Cleanup: re-fetch the record and assert in a Bash python step that its Summary no longer ends "Started" and starts with the status line you wrote; a miss: retry the Summary write once, then add "record status write failed" to its body)`.

Before RELEASE, the run re-fetches the record, the python assert fails, it retries the Summary write once and adds "record status write failed" to the body. Then it releases.

Nits (D19):
- It's unclear whether the run re-checks after the retry.
- "the status line you wrote" checks the model against itself. The ask said "the status line 4/ printed", which is STATUS IN CODE in the hourly.

### P3 (note checks): FAIL

- **(a) SQL read: correctly invalid.** `SQL results, a full column included, rows mode, a preview or any slice are never a read of the note`. PASS.
- **(b) A valid write: PASS, with an edge gap.** The checks are:
  - before the write, python asserts `new == line + "<br />" + old exactly (N1)`, with old from a notion-fetch pasted into a quoted heredoc;
  - after the write, it re-fetches and asserts the stored note, escapes normalised, ends with old normalised (N2).
  - The gap: a row with an empty note (a new Engagement) can never pass N1 without a stray trailing "<br />" (D2).
- **(c) SLOW, note: with no chk::** 4/ makes that item "unfinished, no reason". It's carried over and stays due. The status is Failed "early exit at minute <n>, <k> of <selected> unfinished". That matches the ask.
- **But the chk: formula contradicts N1.** chk is "<old length>+<line length>=<new length>", while N1 makes new = line + 6 ("<br />") + old. A correct write therefore never "adds up", and 4/ marks every completed item unfinished, so the run is Failed. Otherwise the model fudges the numbers. That's D1, high severity.
- Held, blocked and overtaken lines carry note: "the same way". It isn't explicit that they carry chk:, but 4/ demands it (D3).

### P4 (hourly status): PASS for the scenario, with contradictions

- **Skipped STEP 0r for "rules loading took long" at minute 12.**
  - Governing text: `rules loading, thread length or cost is never a reason to leave a step` and STATUS IN CODE: `Partial only when each unfinished step is a cap ..., a tool error with its tool and error text, or minute 25 with the measured elapsed at 25 or more; anything else, or a FAST step with no line, is Failed "early exit at minute <n>". The record's status is copied from that output`.
  - The run ends Failed "early exit at minute 12", printed by the STATUS IN CODE python. PASS.
- **Per-run cap hit.** FAST ORDER says "the run ends Partial". A step line "unfinished (cap)" gives Partial. PASS.
- **Contradictions inside zoya-one:**
  - (D4) RULES LOAD (line 11) says a short page makes "the run ends Partial "rules not loaded ..."". STATUS IN CODE can't print that Partial: its blocked actions count as done, so it prints Completed, or Failed if a step is marked unfinished. And its output is "never rewritten".
  - (D5) RUN RECORD lists No-op, but STATUS IN CODE prints only Completed, Partial or Failed. An all-"not due" run prints Completed.
  - (D6) "one line per FAST step" has no list of FAST steps, so the python can't detect "a FAST step with no line". The 12:39 skip was the over-72-hour sweep inside STEP 1, which has no step name of its own.
  - (D7) The minute-25 proof is the record's end time, which a late last write can push past 25. SLOW requires a "stop: minute 22 at" line. The cap proof is also unchecked: the python is only "given the record body".

### P5 (one Message-ID, two Sent items): PASS

SENDS ARE MESSAGE-IDS covers ACTIONS' Sent check, PRE-SEND 5/, CRASH RECOVERY and the caps: "two Sent items with one Message-ID are one send". It's not a double send for the Sent check, for CRASH RECOVERY (slow-work 2/ logs "completed match <Message-ID>") or for the cap. The cap also counts Activities "one per unique Source ID" (one:55).

Notes:
- CRASH RECOVERY is undefined in one and episodes (D9).
- MESSAGE IDENTITY already says "Two Sent copies with one Message-ID are one send" (one:59, slow-work:80). That's now said twice. Cut-before-add: the new line could replace that sentence.

### P6 (PaaS gate): FAIL

**Gated, contact asks "can you resend the proposal?":**
- **Hourly:** sends nothing, writes "only a Claude note line" and reports "PaaS gated: templates not approved". That matches the gate. But:
  - the note line isn't limited per inbound, so 17 runs a day each add a line to that row (D12);
  - nothing says the thread stays owed, so STEP 1's "thread <id>: no reply needed" settle mark could bury it for good (D12);
  - the report doesn't name who is waiting.
- **SLOW:** PAAS FOLLOW-UPS yields no candidates while gated, and a reply "stops the chain". SLOW does no FAST work, so it sends nothing. Still, "handled as PAAS says" reads as if SLOW handles the reply (D14).

**Approved, the same reply:** it's Zoya's ("re-sends the proposal's podm.in link"), but that fails on three counts:
- (D10) A proposal podm.in link isn't on the approved-links list (one:52). HARD RULES say "Never a link ... outside the approved list", so it's blocked.
- (D10) PAAS doesn't say where the link is. Engagements has no Proposal link field; it's in the page body's "## PaaS deal" section.
- (D13) THREADING replies "on the original thread's latest message in your inbox". PaaS threads are Akshay's ad@ threads that Zoya was never looped into, so there's no thread for her to reply on. And "never a fresh mail where one exists" forbids a new one.

**Approved, a discount ask:** it goes to Akshay's list as one segment "Akshay: <who> at <company>: <what> (<D Mon>)", with at most the holding reply. PASS.

**Contradictions inside PAAS:**
- (D11) "any ask for a call ... always go to Akshay's list" vs "Yours: a reply that only books a call with Akshay (podm.in/30min)".
- (D10) "no price that isn't in their proposal" vs HARD RULE "Never a price ... that isn't on the wording page or the sales page".

### P7 (SLOW, Decision pending, our last mail 7 days ago): FAIL

**What gets selected is ambiguous (D14).** "counted from our side's last mail" resets the clock at every rung. The templates count from the proposal ("Proposal sent, day 3 / day 7") and from "Akshay's first mail" (New or Contacted).
- If the 7-day-old mail is the proposal itself, both day 3 and day 7 are past and nothing picks the rung.
- If it was Zoya's day-3 mail, "Proposal call offer" goes, keyed "<row id>:followup:seq-paas-Decision pending-2:<ISO of that mail>". That key has a space in it, and the effective ladder becomes 3, 10, 24 days.

**The selection can't be built as SLOW BATCH 1/ requires.** 1/ allows metadata only ("never a thread or page read to build the list"). PAAS FOLLOW-UPS needs the thread: our last mail, their reply, and Akshay's first mail on it.

**Rows are dropped by existing skips (D15):**
- The closed-row skip drops Parked rows ("Skip any row closed (... Parked ...) unless routine 8 or a revival"), which contradicts PaaS Parked's quarterly nurture.
- Every moved row carries "Akshay: PaaS row moved from Deals, Zoya waits for the PaaS templates (6 Nov)". Under "Skip a row while Akshay ... holds a decision" and PRE-SEND 4/, that's read as a hold, and nothing removes it once the gate opens.

**Nurture isn't selectable (D16).** "Nurture" isn't an Engagement Status (the README's mapping has none). It's flagged only by a Claude note line, which 1/ can't read.

**Category (D17).** "the work category is followup" names no category. 4/'s category lines are "STEP 2 follow-ups" and "nurture". A separate PaaS category isn't needed: PaaS sits in class (4) and the "STEP 2 follow-ups" line, but the text should say so. "Monthly nurture" keyed as followup also escapes the nurture limits ("Zoya sent: nurture" count, 10 a run).

**Templates (D18).** The day-14 ask "should we keep this open?" from templates.md isn't carried.

## Defects (old text, then replacement)

D1. **chk: sum contradicts N1 (high).** In slowwork:
- old: `the note: followed by "chk:<old length>+<line length>=<new length> fetch" from N1 and N2;`
- new: `the note: followed by "chk:<old length>+<line length>+<6, or 0 when the old note was empty>=<new length> fetch", the lengths N1's python printed, written only after N2 passed;`

D2. **N1 with an empty old note.** In all four files:
- old: `check in a Bash python step that new == line + "<br />" + old exactly (N1)`
- new: `check in a Bash python step that new == line + "<br />" + old exactly, or new == line when old is empty (N1)`

D3. **chk: on held, blocked and overtaken lines.** In slowwork:
- old: `a held, blocked or overtaken line carries "note:<row id> <YYYY-MM-DD>" the same way`
- new: `a held, blocked or overtaken line carries "note:<row id> <YYYY-MM-DD>" and its chk: the same way`

D4 and D5. **The hourly status vs RULES LOAD, and No-op.** In one:
- old: `anything else, or a FAST step with no line, is Failed "early exit at minute <n>".`
- new: `every step not due: No-op; a RULES LOAD line with read short of total: Partial "rules not loaded: <page> <read> of <total>", whatever the steps show; anything else, or a FAST step with no line, is Failed "early exit at minute <n>".`

D6. **The FAST step list.** In one. Confirm the names with the CTO.
- old: `body = one line per FAST step ("step <name>:`
- new: `body = one line per FAST step, these names in this order: 0e, 0e2, 0r, 1 (new mail), 1-72h (threads over 72 hours), order (FAST ORDER's actions) ("step <name>:`

D7. **Minute 25 and cap proof.** In one:
- old: `Partial only when each unfinished step is a cap (this run's sends or today's count reaching it), a tool error with its tool and error text, or minute 25 with the measured elapsed at 25 or more;`
- new: `Partial only when each unfinished step is a cap (a body line "sends <n> of <per-run cap>, today <n> of <daily cap>", from LIMITS' count, shows one reached), a tool error with its tool and error text, or minute 25 (a body line "stop: minute 25 at <date -u time>", 25 or more minutes after the start);`

D8. **PAAS FOLLOW-UPS is undefined in one.** Split PAAS per variant. In one only:
- old: `, and in SLOW work PAAS FOLLOW-UPS.`
- new: `; follow-ups on PaaS rows are the SLOW task's, never yours.`

D9. **CRASH RECOVERY is undefined in one and episodes.** In one and episodes only (keep slowwork as is):
- old: `(ACTIONS' Sent check, PRE-SEND CHECKS 5/, CRASH RECOVERY, the caps, any duplicate check)`
- new: `(ACTIONS' Sent check, PRE-SEND CHECKS 5/, the caps, any duplicate check)`
- Optional: drop MESSAGE IDENTITY's "Two Sent copies with one Message-ID are one send (the provider files its own copy)." It now repeats this rule.

D10. **The proposal link isn't approved, its source isn't named, and price conflicts.** In PAAS (one and slowwork):
- old: `or re-sends the proposal's podm.in link`
- new: `or re-sends the proposal's podm.in link (the Proposal link in the row's "## PaaS deal" page-body section; a podm.in link there is approved for that row's PaaS mail only; any other link, or none: Akshay's list)`
- old: `one ask, no price that isn't in their proposal, approved links only`
- new: `one ask, no price, approved links only`

D11. **A call ask: Akshay's list or Zoya's?** In PAAS. Akshay's call; this is the proposed default.
- old: `any ask for a call, a meeting or a reference;`
- new: `any ask for a meeting, a reference, or a call with anyone but Akshay;`

D12. **Gated note spam and the settle mark.** In PAAS:
- old: `write only a Claude note line, and report "PaaS gated: templates not approved" once a run.`
- new: `write only one Claude note line per inbound from their side ("PaaS gated: <Message-ID> unanswered (<D Mon>)", never twice for one Message-ID, never a settled mark, so the thread stays owed), and report "PaaS gated: templates not approved, <n> replies waiting: <companies>" once a run.`

D13. **Threads Zoya isn't on.** In PAAS:
- old: `Every PaaS mail goes from your inbox on the company's existing thread (THREADING; never a fresh mail where one exists)`
- new: `Every PaaS mail goes from your inbox on the company's existing thread (THREADING; never a fresh mail where one exists; a thread with no message in your inbox gets SENDING's ad@ loop-in first, and your mail waits for a later run)`

D14. **The ladder anchor and metadata-only selection.** In PAASF (slowwork):
- old: `Candidates: PaaS rows whose due date below is today or earlier, counted from our side's last mail on the company's thread (by Message-ID, SENDS ARE MESSAGE-IDS); any reply from their side since stops the chain and is handled as PAAS says.`
- new: `Candidates, from metadata only (SLOW BATCH 1/): PaaS rows whose next rung below is due today or earlier, every day counted from the anchor mail's Activity Date (Decision pending: the proposal mail; New or Contacted: Akshay's first mail or intro; Interested: our last mail when the row went Interested), each mail one Activity by Message-ID (SENDS ARE MESSAGE-IDS); the rung due is the lowest n not yet sent, one rung a run, at least 3 days after the last; an Email in Activity from their side after the anchor stops the chain and is the hourly's, as PAAS says (SLOW sends nothing on it).`
- old: `Key: "<row id>:followup:seq-paas-<status>-<n>:<our last mail's ISO time>"`
- new: `Key: "<row id>:followup:seq-paas-<status, lowercase, hyphens for spaces>-<n>:<the anchor mail's ISO time>"`

D15. **The Parked skip and the migration hold.** In slowwork SELECT:
- old: `plus PaaS rows due under PAAS FOLLOW-UPS (gated),`
- new: `plus PaaS rows due under PAAS FOLLOW-UPS (gated; the closed-row skip below never drops a Parked row PAAS FOLLOW-UPS names, and the migration segment "Akshay: PaaS row moved from Deals, Zoya waits for the PaaS templates" is no hold: the row's first PaaS send removes it, OWNERS),`

D16. **Nurture isn't selectable.** In PAASF:
- old: `Nurture (only on Akshay's word, Claude note line "PaaS nurture"):`
- new: `Nurture (only on Akshay's word: a Next action segment "Zoya: PaaS nurture monthly (<D Mon>)" with its Next date, so selection sees it, and Claude note line "PaaS nurture"):`

D17. **The category name and the nurture type.** In PAASF:
- old: `; the work category is followup.`
- new: `; it counts in the category line "STEP 2 follow-ups"; a "Monthly nurture" is keyed "<row id>:nurture:seq-paas-..." and counts in "nurture" and toward nurture's limits.`

D18. **The day-14 ask (templates.md).** In PAASF, or put it in the toggle itself:
- old: `day 14 "PaaS chase (no reply)" as a last nudge,`
- new: `day 14 "PaaS chase (no reply)" as a last nudge with the ask "should we keep this open?",`

D19. **L2 wording (low).** The text is shared across LOCKV, so make it per variant.
- old: `starts with the status line you wrote; a miss: retry the Summary write once, then add "record status write failed" to its body)`
- new: `starts with the status <STATUS IN CODE (one) | 4/'s OUTCOME CHECK (slow) | you wrote (episodes)> printed; a miss: retry the Summary write once and re-fetch; still a miss: add "record status write failed" to its body)`

Low, no edit now: PaaS rows are matched by "the Show named PaaS", a name. Swap in the page id once the Show exists (README write step 1).
