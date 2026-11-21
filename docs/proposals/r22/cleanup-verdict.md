# Cleanup verdict: r22 (decisions 486, 488 to 495, PaaS, Cleanup's list)

Cleanup session, 6 Nov 2026, about 18:00 JST. Read-only. Nothing deployed.

## Verdict: accepted, with two one-line conditions (C1 WhatsApp, C2 sweep)

Every build was reproduced twice, byte-identical, each equal to the committed copy, on the live bases in docs/deploys/2026-11-06-b-round.md (sweep 468 for the sweep). The Zoya numbers are from 8a925e8 ("PaaS follow-ups as Akshay"), which supersedes the 290b7b7 hand-off table.

| Routine | Base | Build | Bytes / sha256 |
|---|---|---|---|
| Calendar sync | 9dc4babe | r22/calendar.txt | 62,711 / b57aae215fe9115d |
| Daily sweep | 6e3d6606 | r22/sweep.txt | 46,451 / ba5cedefb895dd32 (with C2: 46,569 / 513e1a2acb1a6c9b) |
| Inbox capture | 72c4d81a | r22/capture.txt | 49,350 / bf80bfe26d78c331 |
| Inbox actions | 459e4041, then 486 (6a97144a) | r22/actions.txt | 47,496 / f7e380b94fa984d5 |
| WhatsApp | 174d9317, then 486 (9ef13725) | r22/whatsapp.txt | 30,220 / aa845019f55fcaa5 (with C1: 30,378 / f93f47f9f674dbe7) |
| Zoya hourly | r21 + C1 (187b4f54) | r22/zoya/zoya-one.txt | 62,875 / 88f802fd7df9fe7c |
| Zoya SLOW task | r21 | r22/zoya/zoya-slow.txt (pin 2cf95bb) | 15,813 / b240d5f2dc630467 |
| Zoya SLOW file | 2cf95bb | routines/zoya/release/zoya-slow-work.txt | 92,221 / efe54d1939348aa8 |
| Zoya episodes (not live) | r21 | r22/zoya/zoya-episodes.txt | 50,090 / 1a00663ee9b62574 |

No em dash was added; the sweep's one is in the live base. The hourly has 2,661 bytes left under the cap.

## Cleanup's list: all carried

- **L1:** the no-repo path writes a Failed record ("no repo, lock not checked"), in the hourly and the SLOW task.
- **L2:** before RELEASE, the record is re-fetched and python asserts the Summary carries the status. One retry, else "record status write failed".
- **Note checks:**
  - CLAUDE NOTE WRITES: a notion-fetch pasted verbatim. SQL, rows mode, previews and slices are never a read.
  - N1: new == line + "<br />" + old, or new == line when old is empty.
  - N2: re-fetch after the write and compare the tail with escapes normalised.
  - SLOW outcome lines carry "chk:<old>+<line>+<6|0>=<new> fetch", and 4/'s python fails a missing or wrong sum. "By construction" never passes.
- **Hourly STATUS IN CODE:**
  - Python sets the status from step lines, sends and stop lines.
  - Partial is allowed only for a cap, a tool error or minute 25.
  - Anything else, or a missing step line, is Failed "early exit at minute n".
  - "Rules loading, thread length or cost is never a reason" is in TIME.
- **SENDS ARE MESSAGE-IDS:** in the hourly and the SLOW file, covering the Sent check, PRE-SEND 5/, CRASH RECOVERY, the caps and duplicate checks.

## PaaS (8a925e8, as Akshay from ad@)

- **Hourly:** right as written. FAST sends nothing on a PaaS row, and each inbound goes to Akshay's list once per Message-ID with no holding reply. This also answers my paas-move note on r22.
- **SLOW PAAS FOLLOW-UPS:**
  - The gate is the four "PaaS 1" to "PaaS 4" toggles all approved, so nothing sends before Akshay's ok.
  - Mail goes from ad@ the draft way (NO COMPOSE REPLY), to the person his last mail went to, Cc as that mail had it.
  - The toggle text is used exactly, as Akshay: no Zoya name or emoji, no call ask, price or link (PaaS 4's one episode link aside).
  - Quiet hours and caps hold, and any mail from their side ends the chain.
  - The HARD line now names this as the one other ad@ exception. That matches his call.
- **Before any of the four toggles is approved:**
  - Log the decision 420 exception (PaaS one-liners from ad@ as Akshay, sent by Zoya) as a row in the Decisions database. It isn't there yet: the newest rows are 486 to 495.
  - Carve it out in CLAUDE.md's sending paragraph, together with 486's WhatsApp carve-out in Writing rules.
- **The SLOW file names the migration segment word for word** ("Akshay: PaaS row moved from Deals, Zoya waits for the PaaS templates") as no hold. If the move uses another text (paas-move C3), update this quote to match in the same round.
- **Not in r22:** the PaaS guard in calendar, sweep, actions, capture and WhatsApp. Without it the PaaS write is unsafe (paas-move C1). Fold the one line into this round's non-Zoya builds if the move is to run soon. Otherwise the move waits for the next round.

## C1 (WhatsApp 0w, decision 486): no guessed country code

0w builds the chat id as "an Indian 10-digit number with 91 in front". A People Phone saved without its code isn't always Indian: a US number is 10 digits too. That chaser goes as Akshay, and he approves the text, not the number. Decision 486 says "only to a number already on the person's People row", and a prefixed guess isn't that number.

- **Replace:** `chat id = its digits with the country code, an Indian 10-digit number with 91 in front, then "@c.us".`
- **With:** `chat id = its digits with the country code, then "@c.us"; a People Phone stored without a country code (no leading + or 00): send nothing, replace the segment with "Akshay: <name>'s WhatsApp number has no country code", Akshay in Waiting on (never guess one).`
- **Result:** 30,378 / f93f47f9f674dbe7, reproduced twice.

## C2 (sweep 3a4 b, decision 493): relink keeps the Activity's other links

"Relink each of the Task row's Activities to the guest row" doesn't say how. The Engagement relation is written whole, so a transcript-request Activity that also links an Episode's other row could lose that link.

- **Replace:** `Then relink each of the Task row's Activities to the guest row`
- **With:** `Then relink each of the Task row's Activities to the guest row (fetch its Engagement relation and write back every link it had, plus the guest row, less the Task row; read it back)`
- **Result:** 46,569 / 513e1a2acb1a6c9b, reproduced twice.

## Also checked, holding

- **486 (inbox actions section 6, the WhatsApp routine):**
  - Only the "approved text" line, copied at Akshay's ok, is ever sent.
  - The number comes from People Phone only, and the person must be the row's Guest, Via or a Stakeholder.
  - The Activity is logged before the send, keyed wa-chase:<row id>:<draft date>, with a crash check against the chat before any resend.
  - At most 10 a day by JST, outside quiet hours.
  - Team messages keep Zoya's signature.
  - Section 6's page text is a CTO write, deployed with actions. Main's note about its leftover "Write ok, not ok" sentence stands.
- **488:** a blocked delete becomes a Builder step for the CTO round, as the ledger row says.
- **490:** no list item for a reply that needs nothing, in actions and the Zoya HARD rule.
- **491, 3a4 a:** only promises to send an approved link, plus 464 and 237 asks, move to Zoya. Anything unsure is left and reported.
- **492:** in sweep STEP 2: a settled route is never re-opened, and "X first, Y as fallback" is Zoya's.
- **493, 3a4 b:** each fold is read back, then the Task row is set Done, cleared, checked for relations and moved to Trash (decision 416). At most 20 a run.
- **Calendar prep lines (9aff5ab):** built from a fresh fetch and compared in python every run, with a report line per update.

## Should-fix (not blocking)

- **S1. Two chasers on one row on the same day** share the key wa-chase:<row id>:<draft date>, so the second never sends. That's safe, but add the draft's time to the key if Akshay ever asks for two.
- **S2. Neither replay was re-run on the final build** (hand-off). The first live runs are the test. Check the first SLOW record for chk: lines and the first hourly record for step lines and STATUS IN CODE output.

## Deploy order

As the hand-off says: calendar, capture, inbox actions with section 6, WhatsApp (with C1), Zoya (pin 2cf95bb, then the hourly and SLOW task), then the sweep (with C2) last. Read each back byte for byte against the sizes above.
