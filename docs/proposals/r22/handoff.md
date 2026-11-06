# r22: hand-off to Cleanup and the CTO

Main, 6 Nov. Nothing is deployed, the pin ref isn't moved, and nothing was written to Notion.

## What's in it

- **Cleanup's list:** L1, L2, the note checks, the hourly's status in code, sends counted by Message-ID.
- **PaaS rules (Zoya):** gated on the four PaaS toggles reading approved.
- **Decision 486:** the WhatsApp chaser as Akshay, carried from wa-chase-486.
- **Decisions 488 to 495:**

| Decision | Change | Where |
|---|---|---|
| 488 | A blocked calendar delete becomes "Builder: delete ..." with Builder in Waiting on, for the CTO round | calendar |
| 489 | Mamatha is never added, but stays in Cc when she's on the message we reply to or loop in on | Zoya, capture |
| 490 | A reply to Akshay's own mail that needs nothing goes to Last activity and the Claude note only | inbox actions, Zoya (step b and the HARD rule) |
| 491 | A precall promise to send an approved link is Zoya's; one-time sweep step 3a4 a moves old ones, and Spotlight asks, off his list | calendar 4a, WhatsApp 0b, sweep 3a4 |
| 492 | A settled route stays settled; "X first, Y as fallback" is Zoya's ask, and a decline of X goes to Akshay | sweep STEP 2, inbox actions STEP 5, Zoya; skill paragraph in writeouts.md |
| 493 | Transcript asks are a segment on the guest row; one-time 3a4 b folds the old Task rows | calendar 4f, sweep 3i and 3a4 b, Zoya SLOW INTERNAL TASKS a |
| 494 | One Zoya chase on Akshay's community invite after 5 working days | Zoya SLOW |
| 495 | un# thank-you uses C13u (its own subject, Sri in Cc, no transcript line or ask) | calendar 4d |
| CTO items 2 and 4 | One-form-per-guest line for co-guests; a reply segment clears the "Waiting on" it answers | Zoya, inbox actions STEP 5 and 6e |

Every prompt edit applies on every exemption line too. A Task row stays only for an internal ask with no guest row.

## PaaS follow-ups go as Akshay (his 6 Nov call, CTO 6 Nov)

Akshay rejected the Zoya-voice templates: "Send follow up as Akshay - very short one liners, not pushy, not asking for a call" (Your call on task row 41019a301a7f810da25cc4145a7de33d). r22's PaaS rules now read:

- **Sender:** PaaS follow-ups go from ad@thepodium.in as Akshay, on the company's existing thread with him, the draft way. This is a new exception to decision 420, PaaS rows only. The SLOW file's HARD "never pose as Akshay" line names it. **It needs a Decisions row** (CTO).
- **Recipients:** To the person his last mail there went to, Cc as that mail had it (Zoya included, decision 225).
- **Text:** the toggle's text exactly, with its "Akshay" sign-off. No Zoya name, signature, "best," or emoji. No call ask, no price, no link (PaaS 4's one episode link aside). "hi Sir" in place of the first name wherever Akshay wrote "Sir" to that person.
- **Schedule:**
  - New or Contacted: PaaS 1 at day 4 and day 10 after his first mail or intro.
  - Decision pending (proposal sent): PaaS 2 at day 3, PaaS 3 at day 10, then back to Akshay ("close or nurture?").
  - Nurture, only on his word: PaaS 4 monthly; 3 unanswered and the row goes Unresponsive.
  - Interested, Parked, Booked, They declined and Unresponsive rows: no mail.
- **Replies:** the hourly sends nothing on PaaS rows. Every inbound from their side goes to Akshay's list once, with no holding reply, and ends the chain.
- **Gate:** the wording page's four toggles, named exactly "PaaS 1: no reply", "PaaS 2: after the proposal", "PaaS 3: second proposal nudge" and "PaaS 4: monthly check-in", each with Status approved. Until all four are approved, nothing sends.
- **Removed:** the earlier proposal-link exception and the Zoya-voice templates. docs/proposals/paas-move/templates.md is superseded by the task row's one-liners.

## Prep entry lines (6/nov item 12, CTO 6 Nov)

**What happened.** The private entry "Prep: Ramakant Yadav @ Scalar Field (FT precall)" (event a7qe1ct0k0evapoeeqabelsl9g, 6 Nov 16:30 JST):
- It was created at 22:38 JST on 5 Nov, by the 22:35 calendar run, with Join, Engagement, Next action, Stakeholders and bos-key lines, but no Eval line and no LinkedIn line.
- The row (3f819a301a7f8182b7aafacb6430deb6) has carried Eval link https://claude.ai/artifact/UTmkMD5vRtrnKSkQX2BG17 since 13 Oct.
- The entry's updated time equals its created time, so the 07:35, 10:35 and 13:35 JST runs on 6 Nov read it and changed nothing.

**Why.** Nothing was skipped. The step ran on a matched row, and the entry was created after the match, since its bos-key carries the row id.
- The create left out a line the row had.
- Each later run then decided "nothing changed".

Both point at the same weak spot. The rule asks the model to "compare the lines with the row", which it can do by eye or from an incomplete read. I can't read the run transcripts from this session (no session-events tool), so the exact read it used isn't confirmed.

**Fix (calendar STEP 3).**
- The create takes every value from a fresh fetch of the row, with LinkedIn from the guest's People row, which SQL can't read. It leaves out only lines that are empty on the row.
- Every run, for each existing entry, a Bash python step builds the Eval, Dossier, Prep note and LinkedIn lines from a fresh fetch and compares them with the description line by line. Any missing or different line updates the description.
- Each update adds the report line "prep entry updated: <guest> <D Mon> (<lines>)", and STEP 5 lists them.

**This entry.** The 6 Nov 16:30 precall is past by the time this deploys, so no fix is needed for it.

## Builds

Each built twice, byte-identical, with no new em dash.

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| Calendar sync | 9dc4babe | r22/calendar.txt | 62,711 / b57aae215fe9115d |
| Daily sweep | 6e3d6606 (sweep 468) | r22/sweep.txt | 46,451 / ba5cedefb895dd32 |
| Inbox capture | 72c4d81a | r22/capture.txt | 49,350 / bf80bfe26d78c331 |
| Inbox actions | 459e4041, then wa-chase-486 (6a97144a) | r22/actions.txt | 47,496 / f7e380b94fa984d5 |
| WhatsApp | 174d9317, then wa-chase-486 (9ef13725) | r22/whatsapp.txt | 30,220 / aa845019f55fcaa5 |
| Zoya hourly | r21 + C1 (187b4f54) | r22/zoya/zoya-one.txt | 62,875 / 88f802fd7df9fe7c |
| Zoya SLOW task | r21 (a81e3bc6) | r22/zoya/zoya-slow.txt (pin 2cf95bb) | 15,813 / b240d5f2dc630467 |
| Zoya SLOW file | 9d74718b | routines/zoya/release/zoya-slow-work.txt at 2cf95bb | 92,221 / efe54d1939348aa8 |
| Zoya episodes (not live) | r21 | r22/zoya/zoya-episodes.txt | 50,090 / 1a00663ee9b62574 |

### How to build

- **Non-Zoya:**
  1. Run `python3 docs/proposals/wa-chase-486/patch.py <act|wa> <live> <tmp>`.
  2. Run `python3 docs/proposals/r22/patch.py <cal|sweep|cap|act|wa> <live or tmp> <out>`.
- **Zoya:** apply `r22/zoya/build_one.patch` at f70901f. It holds r21_edits.py (with C1) and r22_edits.py. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 2cf95bb36ce7468148b2747e54ee13d6d63dbf15`.

The zoya-r22/ folder (pin 79bc21a) is superseded by this one.

**The hourly is 62,875 bytes, about 2,460 under the cap.** The next Zoya round has to cut before it adds.

## Replays (offline, read-only)

- **replay/zoya22.md:** the first r22, D1 to D18. All fixed.
- **replay/r22b.md:** decisions 488 to 495, D1 to D14. All fixed in this build. That covers:
  - the sweep's TWO PARTS, which now run 3a3 and 3a4 (3a3 was already missing in the base);
  - the sweep HARD rule, which now allows 3a4 b's Task row writes;
  - the recording key, the Task-row fields and the Activity relink in 3a4 b;
  - the 490 line in Zoya's HARD rule, plus a no-reply-needed note;
  - the decline of X going to Akshay;
  - the transcript origin key in ACTIONS;
  - the guest-row transcript segment in SLOW;
  - the community chase's row;
  - Builder in the calendar's Waiting on list;
  - inbox actions 6e.

Neither replay was re-run on the final build. Cleanup's review is the check.

## Before or with the deploy (CTO; details in writeouts.md)

- **W3:** the C13u toggle, named exactly "C13u Thank-you after recording (un#)". Without it, 4d drafts nothing for un# and reports it.
- **W4:** section 6 text for decision 486, on the Controls page. Deploy it with inbox actions.
- **W1 and W2:** the co-guest form line and the "Community invite chase" toggle. These need Akshay's ok; until then Zoya leaves the line out or sends no chase, and reports it.
- **W5:** the decision 492 paragraph for Akshay's eval skills on claude.ai.
- **W6:** the CTO round picks up rows with Builder in Waiting on.
- **PaaS:** the Show page, the guard in the other routines (paas-move README), and the templates (paas-move/templates.md).

Deploy order: calendar, capture, inbox actions with section 6, WhatsApp, Zoya (pin, then the hourly and SLOW task), then the sweep. The sweep's 3a4 b folds transcript Task rows, so it goes last, after calendar 4f and Zoya SLOW handle segments.
