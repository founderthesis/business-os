# r24: Zoya's new rows go to evals, r23 should-fixes, the PaaS batch, Saurabh's forwards (517), Deals retired (518), chase numbers (519)

Main, 7 Nov. This is the CTO's 20:55 JST list (items 1 to 3) and 23:15 JST list (items 4 and 5, decisions 517 and 518, both In force in the Notion ledger). It's built on the live r23 builds (deploy log docs/deploys/2026-11-07-r23.md). Nothing is deployed, no ref is moved, and nothing was written to Notion. The "caught via Saurabh" WhatsApp line isn't in r24; it waits on Akshay's yes.

## 1. Zoya hourly STEP 1: a row she creates from a pitch goes to evals, not Akshay's list

The Sung Hong un# row put "Akshay: evaluate and decide" on his list. STEP 1 said only "as inbox STEP 3 would create it", which left the owner to the model. It now reads:

> a thread with no Engagement gets one as inbox capture STEP 3 creates it (a pitch: Status New, Waiting on empty, nothing on Akshay's list; the evals routine takes it)

That matches capture's own create rule. Founder Thesis and un# rows get their owner from the evals routine.

**For Cleanup:** capture's rule says the Built to Share and Human by Design owner comes from "STEP 5", but capture has no STEP 5 (its steps go 3, 6, 6a, 6b, 7, 7c, 8). That pointer is already dangling in the live capture prompt, and r24 doesn't change it. Worth a look: say whether the evals routine also covers those two shows, or where that step went.

## 2. Cleanup's r23 should-fixes

- **S1 (capture RAWID):** a result with no sha256 now counts as NONE ("NONE sha256 missing or mismatch"), so every id printed comes from a checksum-checked message. The script pulled out of the build was tested on message 108971:
  - the saved result gave the id;
  - a tampered result gave NONE;
  - the same result with its sha256 removed gave NONE.
- **S2 (lock release):** "sleep 5" comes before each re-push. The rest of the retry is as live: re-read first, the same $R and the same `--force-with-lease`, at most 3 pushes, each only after a re-read shows $H, never a new commit-tree. It's in the hourly, the SLOW task and episodes.
- **S4 (size):** I cut before adding. With items 4 and 5 in, the hourly is **62,830 bytes**, under 63,000. Nothing cut is a rule:

| Cut | Where |
|---|---|
| The superseded PaaS citation (the 6 Nov "send follow up as Akshay" quote and the follow-up rules page id; decision 496 replaced both). It now reads "PAAS (decision 496)." | hourly |
| The Samiksha incident story behind "(Akshay, 5 Nov, item 2)" | hourly, SLOW task, episodes |
| The rationale in brackets after "never a + refspec or --force" (the ban stays) | hourly, SLOW task, episodes |
| "(Akshay, 27 Oct: ...)" becomes "(decision 415: one Zoya run at a time, fail-closed)" | hourly, SLOW task, episodes |
| The quotes in the decision 446 and 445 headings (the decision, Akshay and date stay) | hourly (446 also in episodes) |
| Shorter wording in the RELEASE retry | hourly, SLOW task, episodes |

Decision 517 (item 4) does change the SLOW file, so the pin moves after all, and the same cuts are applied there.

## 3. migration/paas_move.py: the batch comes from the date argument

`BATCH` is now "paas-move-%s", filled with the plan's date. The 6 Nov inputs still give plan 5d5f02cd0d57931a, byte-identical to the committed plan.json, so the written move is unaffected. With 2026-11-09, all 33 ops carry "paas-move-2026-11-09".

## 4. Decision 517: Saurabh's forwards stay on his chain

**Capture STEP 6a** is rewritten, and it's shorter.
- The loop-in is a reply on Saurabh's forward from ad@, through LOOP-IN's draft path: To Saurabh, Cc Zoya and the house copies, body "thanks SG, looping in Zoya".
- The pitch is captured as before: the guest is the person pitched, the pitcher goes in Via, the others in Stakeholders. Saurabh is never Via or Stakeholder.
- The Claude note line is now "forwarded by Saurabh <date>, thread <the forward's Message-ID>".
- The old new-mail route and its "reply on the original if it also reached ad@" branch are gone.
- STEP 6's own line now sends a forwarded pitch to STEP 6a.
- The vendor-forward rule (decision 124) is unchanged.

**Zoya hourly and SLOW file, SENDING.** "Saurabh Garg never" now has one exception: on a pitch he forwarded (the Claude note line), she replies on his chain To the pitcher, using the address inside his forward, with him and Akshay in Cc, and keeps him in Cc on every mail there. Her existing read-back still passes, because Saurabh is on the latest inbound.

**Unchanged:** the stakeholder drop list, the quote stripping and the recording invite (calendar) keep Saurabh off, since none of those is that chain. The "caught via SG" WhatsApp line is dropped.

**CTO, Notion:** if "Rules for Zoya" or its wording page says Saurabh is never copied, it needs the same exception.

## 5. Decision 518: Deals is retired

I cut the Deal paragraphs rather than amending them. All five routines carry one shared line in place of the old "Moved to Engagements" sentence: never create, update, flag or link a Deal; a moved Deal's Engagement is on Show PaaS; a new production-sales conversation is an Engagement on Show PaaS (41119a301a7f81ba9373d86fa6f4fea1).

- **Inbox actions:**
  - STEP 4 is now "PRODUCTION SALES AND BRAND ASKS". A new production-sales conversation creates an Engagement on Show PaaS (Guest, Stakeholders, Organisation, Status New, Waiting on Akshay with one "Akshay:" segment, Source ID gmail:<thread>), and PAAS applies from then on. The brand-request paragraph stays.
  - Dropped: the Deal stage ladder, the Deal create and decision 156's line.
  - Also cut: the Deals schema, Deal from the Activities fields, the "Cold outreach Deal" Waiting on line, the Deal clauses in STEP 5 and Akshay's-list bullets, "(or Deal)" in Next date, and "Deals created and moved" in the report.
- **Capture:**
  - Cut: the Deals schema, Deal from the Activities fields, "Engagement or Deal" in linking, Last activity and the stamped line, and "(or Deal)".
  - Kept: one read-only selector in STEP 0 ("no Engagement and no Deal") still names Deal, so old Deal-linked rows aren't re-worked.
- **Sweep:**
  - Cut: the Deals schema, Deal Stage in HARD, "Deals have no Claude note", the Deal clause in 3b, the no-owner check and the revenue safety net, and STEP 4's whole Deals flag.
  - PaaS rows are already outside the guest checks under the guard.
- **WhatsApp:**
  - Cut: the Deals schema and Deal from the Activities fields.
  - "a Contact on a Deal" is now "an Engagement that is not closed (Show PaaS included)", and "a company with an open Deal" is now "an open Engagement on Show PaaS".
  - 2b updates only Engagements.
- **Calendar:** cut the Deals schema and the "Deal contact sets that Deal's Next date" line.

No routine prompt now writes to Deals.

**CTO, Notion:** move Deals to "Dead databases" on the home page (decision 518), and archive the database whenever you choose.

## 6. Decision 519: the WhatsApp chase finds the number (amends 486)

WhatsApp STEP 0w 3/ looks for the number in this order:
1. People Phone.
2. The WhatsApp ID on the person's FT Community row, matched by Person.
3. Chats search on their full name, using the one saved one-to-one chat whose saved name is that full name (with their company where the saved name has one).

A number found in 2 or 3 is written to People Phone first, with its country code, and then used. If none of the three gives one, or two chats match, the row gets "Akshay: no WhatsApp number for <name>". Never a number from a thread, signature, form or memory. The no-country-code guard (Cleanup's C1) stays.

**Section 6 on the Controls page** is a Notion paste at deploy. The exact old and new text for step 1/ is in r24/section6-519.md. Step 1/ no longer stops on an empty People Phone; it leaves the lookup to STEP 0w.

The inbox actions prompt only points to section 6, so it isn't changed.

## Builds

Each was built twice, byte-identical. The Zoya builds were also rebuilt from a fresh worktree at f70901f with build_one.patch applied. No new em dash.

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| Calendar sync | r22 0e755649 | r24/calendar.txt | 62,772 / 45f6ea7d192728db |
| Inbox capture | r23 c31d1295 | r24/capture.txt | 50,417 / e60b51056027141e |
| Inbox actions | r22 c17734c2 | r24/actions.txt | 47,104 / 5e8aab462e207834 |
| WhatsApp | r22 eb41ecdd | r24/whatsapp.txt | 32,512 / bf5d360b63103215 |
| Daily sweep | r22 51412bd9 | r24/sweep.txt | 49,133 / c61acd3682101155 |
| Zoya hourly | r23 8b0165ba | r24/zoya/zoya-one.txt | 62,830 / 5cd5c5390be8d9a4 |
| Zoya SLOW task | r23 988433fa | r24/zoya/zoya-slow.txt (pin e93bd71) | 15,949 / 92090193c020b148 |
| Zoya SLOW file | 8faf930 (d8ffcafe) | routines/zoya/release/zoya-slow-work.txt at **e93bd71** | 90,973 / 99825b35df05874c |
| Zoya episodes (not live) | r23 cd422006 | r24/zoya/zoya-episodes.txt | 49,987 / d516c14021568d4f |

The earlier r24 hashes (capture 179034c5, hourly 6a8ae791, SLOW task 93b32d68) are superseded by these.

**The pin moves:** decision 517 changes the SLOW file, so the proposed pin is e93bd715bd442594f281bafa43ba2d624efb1d81. The ref isn't moved; the CTO moves refs/heads/zoya-slow-pin at deploy.

The SLOW file loses the stale PaaS citation, the Samiksha story and the SENDING incident notes, the same cuts as the hourly. The hourly also loses SENDING's incident notes and examples: the heredoc emoji note, the Commix example, the 4 Nov compose note, the attachments rationale and the team-note examples.

**How to build:**
- Non-Zoya: `python3 docs/proposals/r24/patch.py <cal|sweep|cap|act|wa> <live input> <out>`, with these inputs: cal r22/calendar.txt, sweep r22/sweep.txt, cap r23/capture.txt, act r22/actions.txt, wa r22/whatsapp.txt.
- Zoya: apply `r24/zoya/build_one.patch` at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin e93bd715bd442594f281bafa43ba2d624efb1d81`.

No replay was run on r24.

Deploy order: calendar, capture, inbox actions (with the section6-519.md paste), WhatsApp, then the Zoya pin (e93bd71), the hourly and the SLOW task, then the sweep. Read each back byte for byte.
