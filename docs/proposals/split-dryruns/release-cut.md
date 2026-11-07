# Release cut (d-split26k)

Goal: zoya-slow at most 62,300 bytes (3,236 under the 65,536 cap) by removing repetition and history only, no rule change. Script: `docs/proposals/d-split26k.py`, run once on parts that already carried d-split26j. 106 edits, every `old` asserted to occur exactly once.

## Result

| prompt | before bytes | before sha256/16 | after bytes | after sha256/16 | cut |
|---|---|---|---|---|---|
| zoya-slow | 65,594 | 1a5f696a7b030ad0 | 62,217 | 1a833d7a8062f1b6 | 3,377 |
| zoya-fast | 36,536 | b2127eef6782e064 | 35,141 | 6b3bc064ebbe1c60 | 1,395 |

The "before" build ran with the 65,336-byte assert disabled (it failed there); the "after" build is the unmodified `build.py`, which passes, and every FAST VARIANT rewrite still matches (including the `PERSON STEPS GO ON THEIR ROW \(decision 385.*` regex). zoya-slow is 83 bytes under 62,300 and 3,319 under the cap.

## Edits

Every edited part is in SLOW, so the bytes column sums to SLOW's cut. Shared parts also shrink FAST.

| # | part | removed (short) | why it is safe to drop | bytes |
|---|---|---|---|---|
| 1 | intro-slow | : the FAST/SLOW trial | history: trial label; decision 394 kept | 21 |
| 2 | intro-slow | the follow-up chains (routines 1 to 8), nurture and revival, team w... (now: SLOW ORDER's work: follow-up chains (...) | duplicate: SLOW ORDER and each section define the run's work; the summary now names them as SLOW ORDER groups them (revival is part of nurture; feedback, bounces, vendor forms, owner mail and scorecard are STEP 0) | 131 |
| 3 | rules-common | , decisions 305, 306 | history: attribution only | 20 |
| 4 | rules-routines | (Akshay, 16 Oct) | history: dated attribution, the rule is unchanged | 17 |
| 5 | notion-data | (an internal task, reminder, builder action or other commitment) | definition gloss: Kind Task is defined by its own fields in the same sentence; every Task rule stays | 65 |
| 6 | notion-data | , Akshay, 21 Oct | history: dated attribution, the rule is unchanged | 16 |
| 7 | scope | (decisions 205, 225, 307, 323) | history: decision list | 31 |
| 8 | scope | (decisions 263, 301) | history: decision list | 21 |
| 9 | scope | : an Outbound row at New or Contacted waits on no one, and you pick... (now: ; Outbound rows as on un#) | duplicate: un# rule (Outbound at New or Contacted waits on no one, picked up once their side replies) holds on both shows by the line above; now a pointer | 72 |
| 10 | actions | , the FAST/SLOW trial; spec docs/proposals/zoya-split.md | history: trial label and spec path; decision 394 kept | 56 |
| 11 | actions | , so the same obligation always gets the same key | rationale: the instruction (write the key back before acting) stays | 49 |
| 12 | actions | Every other old-format segment is keyed once, before launch, by the... (now: Any other old-format segment still un...) | history: how the keys were migrated; the rule (any unkeyed old-format segment is FAST's to key by the fixed rules) stays | 80 |
| 13 | queue-slow | Reply, decision and hold actions are FAST's (RECONCILE). | duplicate: intro, ACTIONS (types and runs) and RECONCILE all say reply, decision and hold are FAST's | 57 |
| 14 | internal | decision 376, Akshay, 21 Oct; | history: dated attribution, the rule is unchanged | 30 |
| 15 | editnotes | Codex, 22 Oct) ( | history: dated attribution, the rule is unchanged | 16 |
| 16 | snoozed | (decision 302, Akshay, 17 Oct) | history: dated attribution, the rule is unchanged | 31 |
| 17 | snoozed | (AR-20261020-1) | history: dated attribution, the rule is unchanged | 16 |
| 18 | snoozed | (rev 2c) | history: revision tag | 9 |
| 19 | voice | (decisions 199, 201, 204, 206, 345) | history: decision list | 36 |
| 20 | sending | , decision 218 | history: attribution only; the decision is cited, the rule text is whole without it | 14 |
| 21 | sending | , decision 332 | history: attribution only; the decision is cited, the rule text is whole without it | 14 |
| 22 | sending | MCP Emails rejects it; | rationale: the never-include_attachments rule and its reason (replies never carry old attachments) stay | 23 |
| 23 | sending | (Codex, 25 Oct: follow-ups went out as new threads with a "Re:" sub... (now: . Every mail that continues a convers...) | history (Codex story) plus duplicate: the team-wrote-last draft/read-back steps restated the same draft, read-back, To/Cc and retry rule; merged into one statement, every step kept | 207 |
| 24 | sending | , so it shows prominently | rationale only | 25 |
| 25 | sending | (Codex, 25 Oct) | history: dated attribution, the rule is unchanged | 16 |
| 26 | sending | ; its SHA-256 hex if longer than 200 characters), never the run dat... (now: ), never the run date; a send that ma...) | duplicate: SHA-256/200-char rule is in ACTIONS; the logged-or-not check (Activity, then Sent and thread, log and send nothing) is ACTIONS' Before sending check, now a pointer | 175 |
| 27 | sending | as before | filler | 10 |
| 28 | teamwa | (Akshay, 16 Oct) | history: dated attribution, the rule is unchanged | 17 |
| 29 | teamwa | ; chat by People Phone | duplicate: next sentence says find the chat by People Phone | 22 |
| 30 | limits | , Akshay, 20 Oct | history: dated attribution, the rule is unchanged | 16 |
| 31 | limits | ; a mail with a real ask counts even if it also loops someone in | duplicate: the last sentence of the same bullet says a loop-in that carries an ask is that follow-up and counts | 64 |
| 32 | limits | (Codex, 22 Oct) | history: dated attribution, the rule is unchanged | 16 |
| 33 | limits | runs inside the follow-up window on Cadences, | duplicate: same sentence already says in the window Cadences gives | 46 |
| 34 | limits | (CTO, 21 Oct) | history: dated attribution, the rule is unchanged | 14 |
| 35 | onemail | (Codex, 25 Oct: Findoc's and Scalar Field's asks went in one mail) | history: incident story; the rule stays | 67 |
| 36 | identity | (Codex, 22 Oct) | history: dated attribution, the rule is unchanged | 16 |
| 37 | runrecord | (AR-20261018-8) | history: AR id | 16 |
| 38 | runrecord | , CTO 22 Oct | history: dated attribution, the rule is unchanged | 12 |
| 39 | feedback | , because the routines read those pages every run | rationale only | 49 |
| 40 | ownermail | (decisions 315, 329; email is how Akshay takes decisions) | history: decision list and rationale | 58 |
| 41 | ownermail | (decisions 351, 385) | history: decision list | 21 |
| 42 | scorecard | (roadmap item 5) | history: roadmap label | 17 |
| 43 | payments | , Akshay, 16 Oct | history: dated attribution, the rule is unchanged | 16 |
| 44 | invites | cisions 400, 403, 406; de | history: decision list; pointer to Rules for Zoya and Calendar rules kept | 25 |
| 45 | followups | (Codex, 23 Oct) | history: dated attribution, the rule is unchanged | 16 |
| 46 | followups | (Codex, 26 Oct) | history: dated attribution, the rule is unchanged | 16 |
| 47 | followups | (AR-20261018-2) | history: AR id | 16 |
| 48 | followups | AR-20261019-1; Rules for Zoya 5a is the master). Silence never ends... (now: Rules for Zoya 5a is the master)) | history AR id, and duplicate: STALENESS GATE keeps 'Silence never closes a row: only a stop NURTURE names does' | 50 |
| 49 | followups | ; other segments, owners and asks stay (AR-20261018-2 (now: (WRITE PATH) | duplicate: WRITE PATH says every other segment, owner and line stays; now a pointer | 41 |
| 50 | followups | (Akshay, 19 Oct) | history: dated attribution, the rule is unchanged | 17 |
| 51 | followups | retired 19 Oct, so this (now: this hold) | history: retirement date; the end date (2 Nov) stays | 14 |
| 52 | followups | so a retry or a run that sends nothing uses none, | rationale: follows from 'one per sent message' | 50 |
| 53 | followups | AR-20261020-1; | history: AR id | 15 |
| 54 | followups | (the no came through a PR or agency; decision 379) | rationale for the No revival tag; the tag rule and 'founders who wrote to us directly' stay | 51 |
| 55 | followups | ; an undated Akshay hold or cold outreach is a hold, never a block | duplicate: the same sentence already classes cold outreach and an undated Akshay hold as holds (7-day recheck segment) | 66 |
| 56 | followups | (AR-20261019-1) | history: AR id | 16 |
| 57 | hard | (Cleanup, 21 Oct) | history: dated attribution, the rule is unchanged | 18 |
| 58 | hard | (AR-20261020-1) | history: AR id | 16 |
| 59 | notion-data | (other segments kept) | duplicate: WRITE PATH keeps other segments | 22 |
| 60 | scope | , never podm.in/book | duplicate: 'Never podm.in links' already covers podm.in/book | 20 |
| 61 | queue-slow | decision 223). "Zoya" is a Waiting on option, and a Zoya segment of... (now: "Zoya" is a Waiting on option). This...) | duplicate: ACTIONS defines a Zoya segment as an action; decision number dropped as attribution | 72 |
| 62 | internal | (decision 377) | history: decision 377 already cited in a. on the same paragraph | 15 |
| 63 | snoozed | , wherever it sits, | duplicate: next sentence says find by the segment, not by Next date or position | 19 |
| 64 | snoozed | and put the ask back reflecting it. Then rewrite only that segment... (now: . Then rewrite only that segment as "...) | duplicate: 'updated by what you read' says put the ask back reflecting it; other segments and owners kept and Next date = earliest open are WRITE PATH | 103 |
| 65 | sending | on un# only unhashed.co/sponsored and unhashed.co/precall (now: client show links: SCOPE) | duplicate: SCOPE lists the un#, Built to Share and Human by Design links in full (both prompts carry SCOPE) | 33 |
| 66 | feedback | The main Claude session builds and deploys it. | description: who deploys; Zoya's steps (Waiting on Builder, Fix written) stay | 47 |
| 67 | bounces | (cross-inbox search fails) | rationale for 'each inbox on its own' | 27 |
| 68 | vendor | in People by Email (Email or Other emails (now: (PEOPLE MATCH) | duplicate: PEOPLE MATCH governs every People create and is stricter (LinkedIn, Email, Other emails, name) | 28 |
| 69 | followups | In-scope Engagements only. | duplicate: SELECT already says in-scope rows | 27 |
| 70 | followups | under PR COORDINATION its gap, 3 working days for Tier 1 inbound in... (now: PR COORDINATION's gap where it applie) | duplicate: PR COORDINATION states the 3-working-day Tier 1 and 2-working-day un# Booking gaps in full; pointer | 69 |
| 71 | scope | ; the words come from the un# templates | duplicate: first bullet of UN# says the words come from the un# templates | 39 |
| 72 | internal | first | filler | 6 |
| 73 | report-slow | , Summary "Run zoya SLOW <start> JST: <status>" | duplicate: RUN RECORD gives the Summary format | 47 |
| 74 | followups | Next date is always the earliest date still open on the row. | duplicate: WRITE PATH sets Next date to the earliest open segment date on every Next action write | 61 |
| 75 | followups | , decision 346 | history: decision 346 cited in LIMITS, which this points to | 14 |
| 76 | followups | whose Next date is today or earlier | duplicate: SELECT picks Sponsored offered rows with Next date today or earlier | 36 |
| 77 | followups | A row with no "## Next sponsored mail" plans it from the thread and... (now: The planned mail is in the page body...) | wordy: same instruction (plan the mail from the thread and podm.in/why-sponsor when the section is missing) in fewer words | 33 |
| 78 | followups | , decision 382 | history: decision 382 cited in PR COORDINATION, which this points to | 14 |
| 79 | followups | The row never closes on silence. | duplicate: STALENESS GATE 'Silence never closes a row' | 33 |
| 80 | followups | Next date today or earlier, | duplicate: SELECT picks LT chase rows with Next date today or earlier | 28 |
| 81 | followups | (a hold changes only "on <D Mon>", never the key) | duplicate: AFTER SEND's Nothing sent branch says a hold moves only 'on <D Mon>' (never its key); the hold rule says the same | 50 |
| 82 | rules-common | (decision 194) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 83 | sending | (decision 184) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 84 | bounces | (decision 217) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 85 | vendor | (decision 239) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 86 | voice | (decision 216) | history: decision 216 cited in SENDING | 15 |
| 87 | voice | (decision 208) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 88 | voice | (decision 152) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 89 | voice | (decision 198) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 90 | feedback | (decision 329) | history: decision 329 cited in KIND | 15 |
| 91 | feedback | (decision 315) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 92 | sending | (decision 352) | history: decision 352 cited in YOUR QUEUE | 15 |
| 93 | sending | (decision 373) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 94 | sending | (decision 262) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 95 | followups | (decision 235) | history: decision 235 cited in SENDING | 15 |
| 96 | followups | (decision 238) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 97 | followups | (decision 355) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 98 | followups | (decision 375) | history: decision 375 cited in LIMITS | 15 |
| 99 | followups | (decision 379) | history: decision 379 cited in REVIVAL | 15 |
| 100 | scope | (decision 323) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 101 | scope | (decision 307) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 102 | scope | (unhashed.co/sponsored) | duplicate: the link is in the price-question wording in the next sentence and in the links line | 24 |
| 103 | notion-data | (decision 383) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 104 | notion-data | (decision 325) | history: attribution only; the decision is cited, the rule text is whole without it | 15 |
| 105 | internal | decision 377, | history: decision number; 'every show' kept | 14 |
| 106 | editnotes | decision 226; | history: decision number; the Sarika-in-Cc rule kept | 14 |
| | | | **total** | **3,377** |

By kind: about 660 bytes are dated attributions, AR ids and revision tags, and about 665 are decision numbers that only attribute. The other 2,050 are duplicated rules turned into pointers or merged (THREADING, idempotency and the Sent check, client-show links, WRITE PATH and SELECT restatements, un# rules repeated for Built to Share and Human by Design), plus rationales, the two incident stories and wordy phrasing.

## Checks, before and after (built prompts)

| prompt | item | before (distinct) | after (distinct) |
|---|---|---|---|
| SLOW | collection:// ids | 8 (8) | 8 (8) |
| SLOW | page ids (32 hex) | 19 (18) | 19 (18) |
| SLOW | inbox_id | 2 (2) | 2 (2) |
| SLOW | "never"/"Never" (word) | 120 (2) | 115 (2) |
| SLOW | placeholders <...> | 199 (88) | 196 (87) |
| SLOW | approved links (occurrences) | 29 (17) | 25 (17) |
| FAST | collection:// ids | 5 (5) | 5 (5) |
| FAST | page ids (32 hex) | 11 (10) | 11 (10) |
| FAST | inbox_id | 2 (2) | 2 (2) |
| FAST | "never"/"Never" (word) | 72 (2) | 71 (2) |
| FAST | placeholders <...> | 97 (54) | 97 (54) |
| FAST | approved links (occurrences) | 28 (17) | 24 (17) |

Every collection id, page id and inbox_id is unchanged, by count and value.

Drops explained, line by line:

- "never" in SLOW, 120 to 115 (FAST 72 to 71). Edit 23 moves the THREADING "Never action send..." sentence; it isn't removed. The five dropped:
  1. ", never podm.in/book" (edit 60, both prompts): "Never podm.in links" in the same sentence covers it.
  2. "Silence never ends a relationship." (edit 48): STEP 2 keeps "Silence never closes a row: only a stop NURTURE names does."
  3. "The row never closes on silence." (routine 5, edit 79): the same STALENESS GATE sentence covers it.
  4. "an undated Akshay hold or cold outreach is a hold, never a block" (edit 55): the same sentence already says a hold with no first day (cold outreach, an Akshay hold with no date) rechecks in 7 days as its own segment. That makes it a hold.
  5. '(a hold changes only "on <D Mon>", never the key)' in AFTER SEND's ordinary step (edit 81): the Nothing-sent branch of AFTER SEND says a hold or deferral moves the segment's "on <D Mon>" (never its key).
- Placeholders in SLOW, 199 to 196: one `<D Mon>` (edit 81, above) and `<start>` plus `<status>` from the REPORT's copy of the run-record Summary (edit 73). RUN RECORD keeps the full Summary "Run zoya SLOW <start> JST: <Completed|No-op|Partial|Failed>".
- Link occurrences, 29 to 25 (FAST 28 to 24). All 17 distinct links are still present. The four dropped: unhashed.co/sponsored and unhashed.co/precall in SENDING (edit 65; SCOPE lists every client-show link in both prompts); unhashed.co/sponsored after "USD 1,500 per feature" (edit 102; it is in the price wording in the next sentence); podm.in/book (edit 60).
- Numbers: apart from decision numbers, dates and AR ids, the only numbers removed are AFTER SEND's copy of the gaps, "3 working days for Tier 1 inbound in its first month, 2 for un# Booking rows" (edit 70). PR COORDINATION states both in full and keeps them. The "SHA-256 ... 200 characters" copy in SENDING (edit 26) is still in ACTIONS.
