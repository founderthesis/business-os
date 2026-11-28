# Cleanup verdict: r24 accepted (all 11 builds reproduce); one condition before the Zoya pin moves (C1: the quote on Saurabh's chain)

Cleanup session, 8 Nov 2026, about 09:30 JST. Read-only: repo builds, the live SLOW task text (list_triggers), and the installed skills. Nothing deployed, no Notion data write.

## Builds (each twice, byte-identical, equal to the commit; under 65,536; no new em dash)

Deploy order and hashes:

| # | Routine | Base | Bytes / sha256 |
|---|---|---|---|
| 1 | Calendar sync | r22 0e755649 | 62,916 / c613af00ddf02c8c |
| 2 | Inbox capture | r23 c31d1295 | 50,417 / e60b51056027141e |
| 3 | Inbox actions (+ section6-519.md paste) | r22 c17734c2 | 47,104 / 5e8aab462e207834 |
| 4 | WhatsApp | r22 eb41ecdd | 32,512 / bf5d360b63103215 |
| 5 | Zoya pin e93bd71: SLOW file | 8faf930 | 90,973 / 99825b35df05874c (90,969 characters) |
| 5 | Zoya hourly (after C1) | r23 8b0165ba | 62,943 / d2875ffdfd3b2f99 |
| 5 | Zoya SLOW task | r23 988433fa | 15,949 / 92090193c020b148 |
| 6 | Daily sweep | r22 51412bd9 | 49,792 / dadce5178987afa7 |
| 7 | Host boards | r24/live 5819ccf7 | 8,733 / 7f5c87ab1b7883c4 |
| 8 | Host dossiers and prep notes | 28a2d9b7 | 6,503 / 67e07a00a19e3c60 |

Zoya episodes (not live): 49,987 / d516c14021568d4f. The sweep's one em dash is the live base's.

Skills (built twice from the installed copies, byte-identical):
- ft-host-dossier 19,663 / 6739b98f16645bc5, 10 changed lines;
- pitch-builder 57,404 / 4be1c84ec544471a.

The host-boards base is r24/live/host-boards.txt, as Main read it back. I didn't re-read that trigger, so the CTO should byte-compare it at deploy.

## The CTO's seven checks

1. **Dossier link: holds.** No build, and not the SLOW file at e93bd71, names the Engagements "Dossier link" outside the dual wording:
   - calendar, host boards, dossiers and the hourly fold each carry it once;
   - host boards keeps its own board field "Dossier link", with a line that boards take only guest rows, so a PaaS pitch never reaches a host.

   One gap the other way: **sweep 3p names "Prep doc link" with no dual wording** (S1).
2. **Sweep 3p: holds, with two should-fixes.**
   - Once per episode, by an Activity with Source ID "bd:<episode id>" written last.
   - No mail, and only rows at New or Contacted get the segment.
   - A re-run after a crash finds the row it created, by Guest on Show PaaS, so there's no duplicate from an earlier run.
   - Should-fix S2: the match is by Guest only, and the segment isn't guarded against a re-add.
3. **519: holds.**
   - The lookup order is People Phone, then the FT Community WhatsApp ID by Person, then the one saved one-to-one chat named the exact full name. Two chats mean no send.
   - Any number found is written to People Phone first, with its country code. The no-country-code guard stays.
   - Never a number from a thread, signature, form or memory.
   - No number in any committed file: I grepped r24 and section6-519.md.
4. **517: the recipients hold, the quote doesn't (C1).**
   - Capture 6a loops in on Saurabh's forward (To SG, Cc Zoya and the house copies).
   - Zoya replies on his chain To the pitcher, Cc SG and Akshay, in both the hourly and the SLOW file. That passes PRE-SEND 2/: To isn't empty, no team address is in To, and SG and Akshay come from the latest inbound.
5. **Pin: holds.** The SLOW task fetches e93bd715bd442594f281bafa43ba2d624efb1d81, expects sha prefix 99825b35df05874c and a total of 90,969 characters, all matching the file at e93bd71.
6. **Sizes:** every prompt is under 65,536. The hourly is 62,943, under 63,000, but C1 adds about 150 bytes, so pay for it with a cut.
7. **skills-521: holds.** The ft-host-dossier diff is 10 lines (the field name and the dual wording). Pitch-builder's Phase 6 now logs on the PaaS Engagement: find by Guest, Stakeholders or Organisation; stop on two candidates; status forward only; never Booked or closed. There's no Deals write left; "Deals" appears only in "retired; never read it for current state and never write to it".

The r23 items are all in:
- S1: RAWID requires sha256 ("NONE sha256 missing or mismatch").
- S2: `sleep 5` before each re-push, in the hourly, SLOW task and episodes.
- S4: the hourly is under 63,000.
- The alias-row eval fix: a pitch row is created at Status New, Waiting on empty, for the evals routine.

## C1 (condition on the Zoya part): quote only the pitcher's own mail on Saurabh's chain

On a 517 chain, Zoya's reply quotes the message it replies on, by decision 452's gmail_quote and MCP's plain-text quote. That message is Saurabh's forward, or capture's "thanks SG, looping in Zoya" on top of it. Either way, Saurabh's own words to Akshay above the forwarded pitch reach the pitcher.

LEAK CHECK does run on that quote, because the pitcher wasn't on the quoted message, but it only stops its listed words, such as criticism, revenue and verdicts. Any other remark of Saurabh's goes out.

Add to the 517 sentence in SENDING (hourly and SLOW file):

> "; there the quote is only the pitcher's own forwarded mail, never Saurabh's note above it or the loop-in"

This moves the pin, so Main rebuilds both, with a cut in the hourly to stay under 63,000.

The non-Zoya builds can deploy before C1. Until Zoya r24 is live, a 517 chain has no recipient Zoya may reply to. Capture's loop-in goes to SG, and r23 Zoya never copies SG, so her assert blocks the send: nothing goes, and the row waits.

## Should-fix (not blocking)

- **S1. Sweep 3p:** add the dual wording once ("Prep doc link (named 'Dossier link' until the rename)"). Until then 3p never finds the field and silently drops the pitch link.
- **S2. Sweep 3p:**
  - Find the PaaS row by Guest **or Stakeholders** on Show PaaS. A company already pursued through someone else, where this guest is a Stakeholder (Cygnet.One: Kesha as Guest, Niraj as Stakeholder), otherwise gets a second PaaS row.
  - A match by Organisation alone: report it, create nothing (decision 424).
  - Add the segment only when it isn't already on the row, so a crash between the segment and the Activity can't add it twice.
- **S3. Capture's dangling "STEP 5"** (Main's question): it means **inbox actions STEP 5**. That's where a Built to Share or Human by Design pitch goes to Akshay ("new <show> pitch via <PR>: put it on <host>'s board, decline or park?"), a holdover from before the capture and actions split. Reword it as "(Built to Share and Human by Design: inbox actions STEP 5)". Nothing is missing.
- **S4. 519 saved-contact match:** Akshay approves the text, not the number. Step 3's saved-chat match is his own contact list, and two matches mean no send, so the risk is low. A report line naming the source ("number from saved contact") would let him spot a wrong one after the fact.
