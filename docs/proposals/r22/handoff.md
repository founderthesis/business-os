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

## 7 Nov round (CTO 08:50 JST): Cleanup's conditions, the PaaS guard, 499 and 514

1. **Cleanup's C1 and C2 are in patch.py.**
   - C1 (WhatsApp 0w): no guessed country code.
   - C2 (sweep 3a4 b): the relink keeps the Activity's other links.
   - On their own they reproduce Cleanup's accepted 30,378 / f93f47f9 and 46,569 / 513e1a2a; commit 1958305 holds exactly those builds. The hashes in the table add item 2 on top.
2. **PaaS guard, both lines,** on the shared exemption line in calendar, sweep, inbox actions, inbox capture and WhatsApp:
   - "Engagements on Show PaaS are production-service rows: no guest step, eval, chase, status change or flag by guest rules; mail on them is logged and anything it asks goes to Akshay's list."
   - "A Deal whose Next action starts "Moved to Engagements" is retired: never flag, update or link to it; use its Engagement."
3. **paas-move (plan 5d5f02cd0d57931a, placeholder Show id), C2 and C3:**
   - Snapshot every listed Activity's Engagement relation first.
   - Append, never replace: old links plus the new Engagement, then read back.
   - `verify` takes the snapshot and fails on any lost link.
   - Every open step has its owner in front and runs to about 120 characters (the longest is 118). The two stale "untouched 14+ days" flags are dropped. Parked and Unresponsive rows have Waiting on empty and a "Closed: ..." line.
4. **Decisions 499 to 515.** Two touch a routine, both in Zoya SLOW:
   - **514:** a release date counts as confirmed when Sarika (or Akshay) states it. A missing date is "Sarika: release date for <guest>'s release mail" with Sarika in Waiting on, never Akshay's list. The decision 427 hold on sharing dates stays as it is.
   - **499:** INTERNAL TASKS says post-production work lives in the Team tasks database and is never created, chased or closed as an Engagements Task row.

   No routine creates post-production Task rows, and no other routine puts a release-date ask on Akshay's list (checked by search). The other decisions in that range cover the episode editor and copywriter chats, not these routines.

The Zoya hourly is unchanged (62,955 / f366f769).

Deploy order, with the move in the same window:
1. calendar
2. capture
3. inbox actions with section 6
4. WhatsApp
5. Zoya: pin 8faf930, then the hourly and the SLOW task
6. the sweep
7. the PaaS move (create the Show, re-run plan, snapshot, write, verify)

## PaaS: reminders only (decision 496), and Human by Design day-before (decision 497)

This supersedes the as-Akshay version. Decision 496 (Akshay, 6 Nov): "actually don't automate the follow ups - I will do manually for now. Just surface them into my queue when a follow up is due."

**PaaS:**
- **No PaaS mail from any inbox.** The PaaS templates and their gate are gone, and so is the as-Akshay exception.
- **Hourly:** every inbound on a PaaS row goes to Akshay's list once, with no holding reply.
- **SLOW PAAS REMINDERS** (metadata only) write one segment, "Akshay: follow up <first name> (<no reply since D Mon | proposal sent D Mon | nurture>) (<D Mon>)", with Akshay in Waiting on. They fall due:
  - day 4 and day 10 after his first mail with no reply;
  - day 3 and day 10 after the proposal;
  - monthly on rows he puts in nurture.
  There's never a second while one is open. Each carries a key on a Claude note line and gets a "blocked" outcome line, so 4/'s check passes.
- **Inbox actions 2b:** his own mail to that person on that thread clears the reminder, and the next one counts from his mail.
- **Move plan** (docs/proposals/paas-move/plan.json, regenerated, 721dc6f2b9eac806 with the placeholder Show id): each moved row starts with the Deal's own Next action and its Waiting on (Mamatha dropped). An open row with neither gets "Akshay: next step for <company>? (moved from Deals 6 Nov)" and Akshay. There's no "waits for the templates" segment.
- docs/proposals/paas-move/templates.md and the one-liners on task row 41019a301a7f810da25cc4145a7de33d are no longer used.

**Human by Design (497):**
- Calendar 3b sends the day-before note from Zoya, as on FT, un# and Built to Share: no Akshay draft, with Chaandini in the house copies.
- {call link} is fscd.ai/studio.
- fscd.ai/studio is recognised as a recording link in 4e and is the studio line on the host prep invite.
- Zoya's Human by Design links list allows fscd.ai/studio for recording mails and the recording invite only.
- **CLAUDE.md's short links list needs fscd.ai/studio added** (CTO).

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
| Calendar sync | 9dc4babe | r22/calendar.txt | 62,814 / 0e755649ab95d9ba |
| Daily sweep | 6e3d6606 (sweep 468) | r22/sweep.txt | 46,913 / b7e69dbc6def649c |
| Inbox capture | 72c4d81a | r22/capture.txt | 49,694 / a4ac5ae216da6103 |
| Inbox actions | 459e4041, then wa-chase-486 (6a97144a) | r22/actions.txt | 48,017 / c17734c21ca88163 |
| WhatsApp | 174d9317, then wa-chase-486 (9ef13725) | r22/whatsapp.txt | 30,722 / 4ce4920ddd88bffa |
| Zoya hourly | r21 + C1 (187b4f54) | r22/zoya/zoya-one.txt | 62,955 / f366f769a799e92d |
| Zoya SLOW task | r21 (a81e3bc6) | r22/zoya/zoya-slow.txt (pin 8faf930) | 15,813 / d2253a1923da5de1 |
| Zoya SLOW file | 9d74718b | routines/zoya/release/zoya-slow-work.txt at 8faf930 | 91,394 / d8ffcafefbb11e7c |
| Zoya episodes (not live) | r21 | r22/zoya/zoya-episodes.txt | 50,171 / aaf08db2321ca288 |

### How to build

- **Non-Zoya:**
  1. Run `python3 docs/proposals/wa-chase-486/patch.py <act|wa> <live> <tmp>`.
  2. Run `python3 docs/proposals/r22/patch.py <cal|sweep|cap|act|wa> <live or tmp> <out>`.
- **Zoya:** apply `r22/zoya/build_one.patch` at f70901f. It holds r21_edits.py (with C1) and r22_edits.py. Then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 8faf93058516e43a35cd534c4a4d8cb8f61b6177`.

The zoya-r22/ folder (pin 79bc21a) is superseded by this one.

**The hourly is 62,955 bytes, about 2,380 under the cap.** The next Zoya round has to cut before it adds.

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
