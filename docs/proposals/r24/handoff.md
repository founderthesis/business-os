# r24: Zoya's new rows go to evals, r23 should-fixes, the PaaS batch, Saurabh's forwards (517), Deals retired (518), chase numbers (519), BD prospect episodes (520), Prep doc link stage 1 (521), context-aware chasers (522)

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

## 7. Decision 520: BD prospect episodes get a PaaS pitch reminder

The new **sweep STEP 3p** is in Part B, after 3i. It sends no mail. The guard's PaaS line allows it, and HARD allows creating a PaaS Engagement in this step only.

- **Which episodes:** each Episode tagged "BD prospect" that went live in the last 7 days (Status Published, or Actual release set) and has no Activity with Source ID "bd:<episode id>".
- **Which row:** for each of its Guests, the Engagement on Show PaaS whose Guest is that People row. With none, it creates one: Name "<Guest> @ <Company>, PaaS", company from the guest's Organisation, Status New, Guest, Source Agent, Source ID "bd:<episode id>", Captured today.
- **What it writes:** a row at New or Contacted gets "Akshay: pitch PaaS to <first name> (<company>), episode out <D Mon>", Akshay in Waiting on, and one Claude note line. Any other status (Interested or beyond, or closed) is skipped.
- **Once per episode:** one Note Activity "bd:<episode id>" per episode, linked to the Episode and the rows, skipped rows included.
- **In the report:** the step line comes from STATUS IN CODE, like every Part B step.

I checked the fields read-only: Episodes have Tags (with "BD prospect"), Guests, Status and Actual release.

**Cuts to pay for it**, all history, no rules:
- the TWO PARTS incident note;
- MAILBOX's quota story;
- 3k's heading detail;
- the decision 325 quote.

The sweep is 49,722 bytes, 143 more than the live 49,579.

## 8. Decision 521, stage 1: Dossier link becomes Prep doc link, under either name

The Notion property is **not** renamed; the CTO does that in stage 2. Every live prompt that names the Engagements field now uses one wording, once, where the field is first listed: Prep doc link (named "Dossier link" until the rename; use whichever the row has, never create a new property). After that, each prompt says Prep doc link.

**Where it changed** (the live prompts, not the repo's older copies):
- **Calendar:** the field list; the prep entry's line is "Dossier: <Prep doc link>" on a guest row and "Pitch: <Prep doc link>" on a PaaS row; the host prep invite ("has a Prep doc link", its "Dossier:" line, the not-a-claude.ai-link check, the move-on-change rule); and the fold.
- **Host boards:** a new r24 build from the live prompt (8,474 / 5819ccf7). It has the dual wording in the Engagements field list. The board's own field is still named "Dossier link", with one line saying its value is the Engagement's Prep doc link and that boards only take guest rows, so a PaaS pitch never reaches a host.
- **Host dossiers and prep notes:** a new r24 build from the live prompt (6,401 / 28a2d9b7). The field list carries the dual wording; the find rule, the republish-to-the-same-link rule and step c say Prep doc link.
- **Zoya hourly:** the fold rule ("the Call, Eval and Prep doc links", with the dual wording). It's 62,943 bytes, still under 63,000. The SLOW file and episodes never named the field, so the pin stays e93bd71.
- **Sweep 3p (decision 520):** the segment gets " (pitch: <Prep doc link>)" when the PaaS row has one.

**Unchanged:** capture, inbox actions and WhatsApp, because none of them names the field. Also untouched, as the CTO asked: migration/*.py and Episodes' own Dossier link.

**Repo copies:** routines/calendar.md, host-boards.md and cowork-dossiers.md get the same wording. They're descriptions; calendar.md is older than the live calendar prompt. docs/schema.md and docs/statuses.md have the row renamed, "(was Dossier link, decision 521)".

**Two things the CTO's list assumed that the live prompts don't do:**
- **Host boards never copied the Dossier link to a board** (STEP 3 copies the eval, pitch, Eval link, availability, date and LinkedIn). I described where the board field's value comes from and added no new copying. If boards should show the dossier, that's a separate change.
- **Of the four dossier skills, only ft-host-dossier writes the field**; the other three leave it to the dossiers routine. Separately, pitch-builder's closing step wrote every pitch to Deals, so under decision 518 it now logs on the PaaS Engagement and writes its link to the Prep doc link. The upload set is docs/proposals/skills-521 (handoff and hashes there).

**Check for Cleanup:** no live build in r24 (or the SLOW file at e93bd71) names "Dossier link" outside the dual wording or the board's own field. I checked with a script over every r24 build, and every build is under 65,536.

## 9. Decision 522: WhatsApp chasers read the chat first (refines 486's draft only)

Akshay, 7 Nov 23:34 JST (intake 41119a301a7f81d29ae6e81035ab952b). The draft is written by inbox actions under section 6. STEP 0w only sends approved text, so the rules sit in section 6, and the prompts change only where they have to. Contact matching (519), cadence, holds, the exact-draft ok and the send-as-Akshay rule are unchanged. There's no new sender and no new routine.

- **Section 6 (Controls page; the CTO pastes it):** r24/section6-522.md replaces the whole WHATSAPP CHASE block and supersedes section6-519.md.
  - **Read first:** before drafting, it reads the person's one-to-one chat with Akshay (read only), plus the newest Activities and mail where useful. Already answered: no draft, just a note line.
  - **Style:** it mirrors Akshay's greeting, name form, language, case and length in that chat.
  - **Shape:** 1 or 2 short messages joined by " || ", with one ask.
  - **One true detail:** from their own chat, or recent news it verifies, never on every draft. Nothing invented and no implied sightings.
  - **Context line:** a "context:" line sits under the draft and is never sent. It names the chat's date range, the detail used and any news URL, or says the chat wasn't found or the person isn't certain.
- **Inbox actions:** the section 6 pointer now says to read that person's chat through Blueticks, read only, before drafting. Size +100.
- **WhatsApp STEP 0w:** sends one message, or two in order when the approved text holds " || ". It never sends the context line, and its crash check looks for each part so nothing goes twice. Size +208.

**Decision 522 isn't in Notion yet.** This session doesn't write to Notion on a relayed ask. The row for the CTO to create:
- No. 522
- Decision: "WhatsApp chasers read the chat first, mirror Akshay's style, 1 or 2 short messages"
- Area: WhatsApp and community
- Who: Akshay
- Date: 2026-11-07
- Status: In force
- What we decided: "Before drafting a decision 486 chaser, Zoya reads the person's WhatsApp chat with Akshay (and the row's Activities and mail), skips the draft if it's already answered, mirrors his salutation, name form, language, case and length, writes 1 or 2 short messages with one ask and at most one true, verified detail, and notes what she read on a context line that is never sent. Refines 486's draft only; 519's number lookup and the exact-draft ok are unchanged."
- Why: his 7 Nov 23:34 JST words, quoted.

## Builds

Each was built twice, byte-identical. The Zoya builds were also rebuilt from a fresh worktree at f70901f with build_one.patch applied. No new em dash.

| Routine | Base (live) | Build | Bytes / sha256 |
|---|---|---|---|
| Calendar sync | r22 0e755649 | r24/calendar.txt | 62,916 / c613af00ddf02c8c |
| Inbox capture | r23 c31d1295 | r24/capture.txt | 50,417 / e60b51056027141e |
| Inbox actions | r22 c17734c2 | r24/actions.txt | 47,204 / 829a8cc8fb21251f |
| WhatsApp | r22 eb41ecdd | r24/whatsapp.txt | 32,720 / 46545ea347702e55 |
| Daily sweep | r22 51412bd9 | r24/sweep.txt | 49,792 / dadce5178987afa7 |
| Host boards | live 5819ccf7 (r24/live/host-boards.txt) | r24/host-boards.txt | 8,733 / 7f5c87ab1b7883c4 |
| Host dossiers and prep notes | live 28a2d9b7 (b-round-5nov/dossiers.txt) | r24/dossiers.txt | 6,503 / 67e07a00a19e3c60 |
| Zoya hourly | r23 8b0165ba | r24/zoya/zoya-one.txt | 62,943 / d2875ffdfd3b2f99 |
| Zoya SLOW task | r23 988433fa | r24/zoya/zoya-slow.txt (pin e93bd71) | 15,949 / 92090193c020b148 |
| Zoya SLOW file | 8faf930 (d8ffcafe) | routines/zoya/release/zoya-slow-work.txt at **e93bd71** | 90,973 / 99825b35df05874c |
| Zoya episodes (not live) | r23 cd422006 | r24/zoya/zoya-episodes.txt | 49,987 / d516c14021568d4f |

The earlier r24 hashes (capture 179034c5, hourly 6a8ae791, SLOW task 93b32d68) are superseded by these.

**The pin moves:** decision 517 changes the SLOW file, so the proposed pin is e93bd715bd442594f281bafa43ba2d624efb1d81. The ref isn't moved; the CTO moves refs/heads/zoya-slow-pin at deploy.

The SLOW file loses the stale PaaS citation, the Samiksha story and the SENDING incident notes, the same cuts as the hourly. The hourly also loses SENDING's incident notes and examples: the heredoc emoji note, the Commix example, the 4 Nov compose note, the attachments rationale and the team-note examples.

**How to build:**
- Non-Zoya: `python3 docs/proposals/r24/patch.py <cal|sweep|cap|act|wa|hb|dos> <live input> <out>`, with these inputs: cal r22/calendar.txt, sweep r22/sweep.txt, cap r23/capture.txt, act r22/actions.txt, wa r22/whatsapp.txt, hb r24/live/host-boards.txt, dos b-round-5nov/dossiers.txt.
- Zoya: apply `r24/zoya/build_one.patch` at f70901f, then run `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin e93bd715bd442594f281bafa43ba2d624efb1d81`.

No replay was run on r24.

Deploy order: calendar, capture, inbox actions (with the section6-522.md paste, which supersedes section6-519.md), WhatsApp, then the Zoya pin (e93bd71), the hourly and the SLOW task, then the sweep, host boards and host dossiers. Akshay uploads skills-521, and then the CTO renames the property (stage 2). Read each back byte for byte.
