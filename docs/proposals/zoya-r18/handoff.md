# Zoya r18: the CTO's 15:05 corrections plus Cleanup's r16 verdict (4 Nov)

r18 is built on r17, so it carries r16 (456, the 445 follow-up) and r17 (461, 462). **The SLOW file is what matters for the 17:08 run.**

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 513d32cb0a754dc381a4092dcb9d43f5732225c8`, with `build_one.patch` applied at f70901f. Built twice, byte-identical, no em dashes.

| File | Bytes / sha256 |
|---|---|
| `zoya-slow-work.txt` (the pinned SLOW file) | 81,459 / a3335c1abd10b006 (81,455 characters), at 513d32c |
| `zoya-slow.txt` (Zoya SLOW task) | 12,985 / 3378858b38b24c0b |
| `zoya-one.txt` (hourly) | 54,773 / 1a437c41c7a74d43 |
| `zoya-episodes.txt` (new task, after Akshay's go) | 45,279 / 3547a1dcf656d344 |

**For the 17:08 SLOW run:**
1. Move the pin to 513d32c.
2. Paste the SLOW task prompt (3378858b). It carries the new pin, hash and 81,455-character total, and the shared HARD RULES (PRE-SEND check 2) changed in it too.
3. Paste the hourly prompt in the same window, or the next. It shares the loop-in and recipient fixes.

## The CTO's A list

1. **Bare loop-in (shared LOOP-IN).** "Optionally the ask in a few words" becomes: "Nothing else (CTO, 4 Nov, clarifying decision 421): no chase, offer, sponsored ask or reminder of ours and no restated ask; a chase goes from your own inbox after the loop-in, as its own action." **CTO: log this as a clarification of 421.**
2. **Recipients checked in code (shared PRE-SEND 2/ and the loop-in path).**
   - To and Cc are built before the draft, then checked in a Bash python step:
     - To isn't empty;
     - ad@ and every team address are never in To;
     - every intended outside address is in To or Cc.
   - A failed assert sends nothing, and the action is blocked as "recipients: <what failed>".
   - **The loop-in always goes the draft way:** draft reply, then draft update for To and Cc, then read-back, then draft send. Never through email_compose reply's own addressing. That's the Taj Agra failure.
3. **Selection order (SLOW BATCH 2/).**
   1. Recording logistics within 7 days.
   2. Payments, invoices and billing (every STEP 1b step) and dated commitments (a promised date, an invoice or payment step, Akshay's written commitment).
   3. STEP 0 items (owner mail, feedback, vendor forms, the scorecard), edit notes, internal team tasks and snoozes due.
   4. Follow-ups and nurture, then anything else.
4. **Category lines and evidence (SLOW BATCH 3/ and 4/).**
   - **Category lines:** after the last chunk, there's one line per category: STEP 0a to 0g, 1b payments, edit notes, internal tasks, snoozes, follow-ups and nurture. Each reads checked, not due, blocked (with its owner) or unfinished. A category with no line makes the run Partial, "category missing: <name>".
   - **Evidence on completed items:** every completed item carries `act:<Activity id> note:<row id> <date> key:<key>` from a read-back. The python checks they're present, and checks the key form: `^loopin:<Message-ID>$` for a loop-in, the ACTIONS key form for Zoya mail. A miss makes that item unfinished.

## Cleanup 718ada8 (r16 verdict and the 14:01 addendum)

- **B1, attaching a transcript file:**
  - Only a file from Mamatha counts, never "anyone tagged Team".
  - It's matched to a recording whose date has passed, never a precall.
  - The decision 374 test runs **before** anything is attached.
  - An existing Transcript file is never replaced. A mismatch goes on Akshay's list and the item is blocked.
- **B2, the transcript-file key:** the key is `transcript-file:<Message-ID>:<file name>`. It's done when the Episode's "## Transcript" sha matches.
- **B3, recording-link corrections:** the exact replacement is the old zencastr.app.link URL in the invite's location and description, and in the row's Call link, becoming the new one. notificationLevel is ALL, and nothing else is touched. "Already done" is tested per guest and event, so a corrected link never triggers a second mail; it goes to Akshay's list. **CTO: log the replace-on-correction rule as a decision row**, since 445 said add-only.
- **Addendum 1:** the draft-only loop-in, as A2.
- **Addendum 2:** the selection classes, as A3.
- **Addendum 3:** evidence and key checks, as A4.
- **Addendum 4:** the FAST reserve needs only a Cadences line (CTO).
- **Addendum 5:** the bare loop-in, as A1.
- **Mojibake:** both bodies go straight in the tool arguments as UTF-8, never through Bash or a file. The read-back checks the sign-off.
- **Should-fix:**
  - LOOK BEFORE ASKING checks the Episode first.
  - Transcript rows are excluded from step b.
  - There's one follow-up to Mamatha, then Akshay's list.
  - **Not done:** reporting an event that can't be edited once instead of hourly, and retiring "Ranjita" from the Rules for Zoya wording, calendar 4f and sweep 3i.
- **460:** "AD Personal" becomes "AD Tasks" in SCOPE and the routine 4 line.

**Status:** built, not replayed. For Cleanup now. Nothing is deployed, and the pin ref hasn't moved. **If Cleanup can't accept by 16:40,** the CTO's stopgap HARD RULE can go into the live SLOW task prompt instead:

```
- LOOP-IN (decision 421): from ad@thepodium.in only the bare introduction, "thanks <first name>, adding @Zoya to coordinate" or "adding @Zoya to coordinate further", nothing else; send it the draft way (draft reply, draft update To and Cc, read back, draft send), never through email_compose reply's own addressing, and never with ad@ in To.
```
