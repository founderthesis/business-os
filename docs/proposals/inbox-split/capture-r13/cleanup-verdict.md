# Cleanup verdict: capture r13 (7169c68, decision 457), 4 Nov ~09:00 JST

**Accepted. No blocker.** Deploy `capture-r13/capture.txt`, **46,842 / 7482f2f1132bd2e6**.

## Rebuild

`capture-r13/patch.py` on the live r12e (`capture-r12/capture.txt`, 9caf2cdb), twice, gives 46,842 / 7482f2f1132bd2e6. It's byte-identical to the repo, with no em-dashes.

## The diff

**One edit, in KEY's "Mail Zoya is on" sentence.** It adds: "A pitch from outside the team (a guest, sponsored, PR or vendor pitch) with ad@thepodium.in on To or Cc is never left for her (decision 457 ...): MSGID FIND first, then REF, then RAW by HEAD, this run, no wait." The 2-hour wait now applies only to "Any other".

**No duplicate risk.**
- If Zoya logs the same mail before capture does, MSGID FIND (Date within 2 minutes, or People overlap, HEADER-confirmed) finds her row.
- If capture logs it first, Zoya's STEP 1 a looks the msgid: key up before logging ("or if no Activity has its msgid: Source ID yet").
- Either way, one row.

## The CTO's two gaps

**1. Eshna's un# pitches sat unlogged.**
- That's exactly the case 457 closes. Zoya was on the pitches with Akshay in Cc, so Zoya handed them to the inbox, and capture was waiting for Zoya.
- The rows you created by hand: when r13 next reads those messages, STEP 3 finds the guest's existing Engagement (Guest, Via or Stakeholder, decision 424) and links to it rather than creating one.
- **Check after the first r13 run:** one Engagement per Eshna pitch, and one Activity each.

**2. No Engagement when the pitch names no show.** The text already covers this.
- STEP 3's pitch bullet says "every inbound pitch is processed, including ... pitches that name no show ... anything else is Founder Thesis".
- So that gap wasn't a rule. It was either the same Zoya-wait case (now closed), or a run that didn't reach STEP 3 for that message.
- **Please send the message's UID or the run id.** If Zoya wasn't on it, I'll trace that run's ledger line, which says why it stopped.

Nothing deployed by Cleanup.
