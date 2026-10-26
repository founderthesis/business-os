# Release build coverage and freeze (d-split26l, 26 Oct)

CTO order, 20:31 JST, step 1: fold decisions 411 to 413 in with the amendments, fix SLOW INTERNAL TASKS c(4), keep Cleanup's three restorations from d33ef96, commit a coverage table, then freeze.

## Frozen build

| Prompt | Bytes | sha256 (first 16) | Built by |
|---|---|---|---|
| zoya-fast | 36,257 | 96c11beae7ec325b | `routines/zoya/build.py` after `docs/proposals/d-split26l.py` on d33ef96 |
| zoya-slow | 63,145 | a5b4ef40cfd85bb1 | same; 2,191 B under the cap less 200 |
| inbox | 63,536 | 2eade949aa242970 | `docs/proposals/d394-keys.py` (ACTION KEYS, rebased today) on live inbox 61,957 / aed0215a8bdf6a26 |
| calendar | 56,272 | d9d1f508b9c797fd | `d394-keys.py` on live calendar 54,901 / 543c3499473860ac, then `docs/proposals/d-411-412-cal-sweep.py` |
| daily sweep | 35,319 | 9db06d64df11ff7d | `d394-keys.py` on live sweep 33,824 / 7af60faaa021fa64, then `d-411-412-cal-sweep.py` |

Each was built twice and compared byte for byte: identical. Every test from here names these hashes. Any later change to behaviour moves a hash, and the commit that moves it names the tests it repeats.

The inbox, calendar and sweep carry the ACTION KEYS paragraph, which deploys in the same window as the split and never before (zoya-split-build.md, At deploy, step 2). Its base sizes were from 22 Oct, so it is rebased on today's live prompts: same anchors, same text. Calendar and sweep also carry decision 412 (which names the calendar) and 411 (which names Sweep STEP 3a). All five deploy together, after Cleanup's review.

## Today's rules

| Rule | Where it lives now |
|---|---|
| 411: recording status settled from our side only (calendar, Zencastr, transcript, Akshay's mail or WhatsApp) | FAST L21, SLOW L25 (NOTION DATA, "RECORDING STATUS"); calendar STEP 4 a; Rules for Zoya (live) |
| 411: still unclear goes in Akshay's queue on the Engagement: "Akshay: did the <D Mon> recording with <guest> happen? Write yes or no in Your call" | FAST L21, SLOW L25; calendar STEP 4 a (replaces decision 321's note-only rule); sweep STEP 3a |
| 411: never the guest or PR, never "Zoya: confirm with <PR>" | FAST L21, SLOW L25; sweep STEP 3a |
| 411: every action due from Akshay goes in his queue on the Engagement, never WhatsApp | FAST L21, SLOW L25 ("AKSHAY'S LIST IS A DECISION INBOX"); sweep STEP 3a. RECONCILE's stuck alert in the group "Zoya" stays: it is a status alert, not an ask |
| 411: Akshay's yes or no in Your call: yes sets Recorded, no becomes the cancelled-or-no-show ask | Controls page "Inbox and Your call rules" section 5, text in docs/proposals/notion-edits-26oct.md (applied by the CTO; part of this build) |
| 412: once confirmed, Status Recorded | SLOW L52 c(3); calendar STEP 4 a (unchanged) |
| 412: FT thank-you drafted in ad@ as a standalone new mail, never a reply on the PR thread | SLOW L52 c(4); calendar STEP 4c |
| 412: To the guests, Cc the PR, every other stakeholder and the house copies | SLOW L52 c(4); calendar STEP 4c |
| 412: Waiting on Akshay, "Akshay: send the thank-you draft to <first name> (draft ready)" | SLOW L52 c(4); calendar STEP 4c and 4d |
| 412: no transcript, don't wait for one | SLOW L52 c(4) (the .txt is never attached to a thank-you); calendar STEP 4c and 4d |
| 413: themes and flow from our side; PR points are input; no precall notes means a draft to Akshay; no revenue figures or call confidences | FAST L77 (mail b); Rules for Zoya (live). SLOW sends no theme mails |
| 413: recipient read-back covers everyone on the latest inbound, To and Cc, plus Akshay | FAST L49, SLOW L61 (THREADING read-back) |
| 413: Mamatha kept where she is on the latest inbound, never added | FAST L49, SLOW L61. Open question below |
| Send logging: each Email out Activity carries the sent body | FAST L56, SLOW L77 (MESSAGE IDENTITY) |
| Send logging: two Sent copies with one Message-ID are one send | FAST L41 and L56, SLOW L47 and L77 |
| Cleanup d33ef96 restoration 1: crash-window check reads Sent and the thread | FAST L40, SLOW L46 (ACTIONS) |
| Cleanup d33ef96 restoration 2: routine 8 selector "Next date today or earlier" | SLOW L126 |
| Cleanup d33ef96 restoration 3: routine 7 selector "Next date today or earlier" | SLOW L132 |
| Lease: run record is the lease, stale after 60 minutes, earlier start holds it, same minute FAST | FAST L60, SLOW L81 |
| Idempotency key is the action key, never the run date | FAST L49, SLOW L61 |
| Run receipts carry provider usage or "unknown", never an estimate | FAST L58, SLOW L79 (RUN RECORD) |

## The 17:40 Krsnaa "double send"

It was one send. Both Sent copies carry Message-ID 84c562c5-fd32-40f1-bdc6-8a74da46022e@mcpemails.com:
- the provider's own IMAP copy, dated 08:40:20Z, with no Received header;
- Gmail's copy of the SMTP submission, received 08:40:41Z, with X-Google-Original-Date 08:40:20.

The 21-second gap is the SMTP hand-off, not a second send. Draft read-back files nothing: the 18:06 send shows the same pair 1 second apart. This matches the provider test (provider-idempotency.md). No send fix is needed. MESSAGE IDENTITY now says two copies with one Message-ID are one send.

The same mail went To the PR and Cc Akshay only. The inbound had Mamatha in Cc, so this is decision 413's dropped recipient, and the new read-back catches it.

## Open question for the CTO (not decided here)

Decision 413 calls the house copies "Akshay, and Mamatha for now". The live prompt says "never Mamatha" (cited as decision 352), and decision 260 took her off Founder Thesis Cc. The build keeps her where she is on the latest inbound and never adds her. Should the house copies add her where she is absent? One line to change if so.

## Live prompt coverage, sentence by sentence

The live Zoya prompt (65,210 / 90b11cd34a3bdca1) has 419 sentences of three or more content words. Each was matched against FAST and SLOW by word overlap within a four-sentence window. 373 match at 0.70 or above (the full list follows the hand-checked table). The 46 below 0.70 were read by hand. None is a dropped rule. Each is one of these:
- a header whose decision citation was cut (wording-only, d-split26k);
- a rule reworded in the split;
- a change approved on purpose: the action key, the FAST and SLOW orders, or decision 412.

### The 46 below 0.70, hand-checked

| Live line | Sentence (start) | Match | Best location | Verdict |
|---|---|---|---|---|
| 1 | You send every routine Founder Thesis, un#, Built to Share and Human by Design guest mail  | 0.47 | FAST L34 | Kept, reworded in each intro: 'each run takes what is new or unfinished, and more runs never mean more mails'. The hourly cadence is replaced by FAST :38 and SLOW 10:50/16:50 (decision 394). The 'never chases anyone' sentence is identity, carried by CLAUDE.md and Rules for Zoya |
| 1 | HOURLY (AR-20261019-6): you run every hour. | 0.60 | FAST L1 | Kept, reworded in each intro: 'each run takes what is new or unfinished, and more runs never mean more mails'. The hourly cadence is replaced by FAST :38 and SLOW 10:50/16:50 (decision 394). The 'never chases anyone' sentence is identity, carried by CLAUDE.md and Rules for Zoya |
| 1 | work already done and recorded is not redone, so the look-back windows are only the catch- | 0.33 | FAST L79 | Kept, reworded in each intro: 'each run takes what is new or unfinished, and more runs never mean more mails'. The hourly cadence is replaced by FAST :38 and SLOW 10:50/16:50 (decision 394). The 'never chases anyone' sentence is identity, carried by CLAUDE.md and Rules for Zoya |
| 1 | More runs never mean more mails: follow-ups keep their due dates, and every once-a-day or  | 0.41 | SLOW L67 | Kept, reworded in each intro: 'each run takes what is new or unfinished, and more runs never mean more mails'. The hourly cadence is replaced by FAST :38 and SLOW 10:50/16:50 (decision 394). The 'never chases anyone' sentence is identity, carried by CLAUDE.md and Rules for Zoya |
| 5 | THE RULES ARE IN NOTION (decision 194). | 0.67 | FAST L5 | Header; the decision number cut (wording-only, d-split26k) |
| 10 | All eight are live (Akshay, 16 Oct). | 0.67 | SLOW L11 | Kept (SLOW L11, 'All eight are live') |
| 25 | SCOPE (decisions 205, 225, 307, 323). | 0.17 | FAST L23 | Header; decision numbers cut |
| 28 | - Akshay still decides un# guests (decisions 263, 301); | 0.57 | FAST L26 | Kept (FAST L26); decision numbers cut |
| 36 | Cold outreach stays Chaandini's (C1 and C2): an Outbound row at New or Contacted waits on  | 0.53 | FAST L30 | Kept (FAST L30, SLOW scope): cold outreach stays Chaandini's |
| 41 | Rows whose Next action starts "Agent: sponsored step" or "Zoya: <routine> step" are follow | 0.50 | SLOW L50 | Kept (SLOW L50) |
| 42 | INTERNAL TASKS (decision 376, Akshay, 21 Oct; | 0.50 | FAST L79 | Header kept; b gains TEAM WHATSAPP nudge (approved earlier); c(4) replaced on purpose by decision 412 (SLOW L52) |
| 42 | Any Kind Task row with Show Internal Waiting on a team member other than Akshay whose Next | 0.66 | SLOW L52 | Header kept; b gains TEAM WHATSAPP nudge (approved earlier); c(4) replaced on purpose by decision 412 (SLOW L52) |
| 42 | (4) Thank-you: if the row has a thank-you draft ("Zoya drafted: FT thank-you" or "Zoya dra | 0.60 | SLOW L52 | Header kept; b gains TEAM WHATSAPP nudge (approved earlier); c(4) replaced on purpose by decision 412 (SLOW L52) |
| 44 | SNOOZED ASKS (decision 302, Akshay, 17 Oct). | 0.67 | FAST L79 | Header; citation cut |
| 46 | VOICE (decisions 199, 201, 204, 206, 345). | 0.14 | FAST L6 | Header; citations cut |
| 49 | SENDING (decision 184). | 0.67 | SLOW L119 | SENDING header citation cut; THREADING citation cut; idempotency key replaced on purpose by the action key (decision 394, FAST L49/SLOW L61); crash-window check kept (FAST L40/SLOW L46 Sent and thread, Cleanup's edit 26 fix) |
| 49 | THREADING (Codex, 25 Oct: follow-ups went out as new threads with a "Re:" subject and no I | 0.42 | FAST L49 | SENDING header citation cut; THREADING citation cut; idempotency key replaced on purpose by the action key (decision 394, FAST L49/SLOW L61); crash-window check kept (FAST L40/SLOW L46 Sent and thread, Cleanup's edit 26 fix) |
| 49 | idempotency_key "zoya-<engagement page id>-<routine or what>-s<step>-<anchor>": the anchor | 0.50 | FAST L37 | SENDING header citation cut; THREADING citation cut; idempotency key replaced on purpose by the action key (decision 394, FAST L49/SLOW L61); crash-window check kept (FAST L40/SLOW L46 Sent and thread, Cleanup's edit 26 fix) |
| 49 | When a send may have gone without being logged (no Activity, but a failure after sending), | 0.50 | FAST L66 | SENDING header citation cut; THREADING citation cut; idempotency key replaced on purpose by the action key (decision 394, FAST L49/SLOW L61); crash-window check kept (FAST L40/SLOW L46 Sent and thread, Cleanup's edit 26 fix) |
| 56 | a mail with a real ask counts even if it also loops someone in. | 0.57 | SLOW L68 | Kept in LIMITS: 'a mail logged as a loop-in that also carries an ask or follow-up is that follow-up' |
| 58 | - ONE THREAD, ONE CONVERSATION (Codex, 25 Oct: Findoc's and Scalar Field's asks went in on | 0.50 | FAST L54 | Kept (FAST L54 ONE THREAD); citation cut |
| 64 | MESSAGE IDENTITY (Codex, 22 Oct). | 0.50 | FAST L56 | Header; citation cut |
| 66 | RUN RECORD (AR-20261018-8). | 0.67 | FAST L58 | Header; citation cut |
| 72 | never a price or term unless he states the new one) is live at once, because the routines  | 0.57 | SLOW L91 | Kept (SLOW L91 live-at-once); 'Main builds and deploys' is a builder fact, not a run rule |
| 72 | The main Claude session builds and deploys it. | 0.43 | FAST L21 | Kept (SLOW L91 live-at-once); 'Main builds and deploys' is a builder fact, not a run rule |
| 77 | BOUNCES (decision 217). | 0.67 | FAST L39 | Header; citation cut |
| 79 | VENDOR FORMS (decision 239). | 0.50 | FAST L37 | Header; citation cut |
| 94 | OWNER MAIL (decisions 315, 329; | 0.40 | FAST L1 | OWNER MAIL kept (SLOW STEP 0f); 'email is how Akshay takes decisions' is rationale |
| 94 | email is how Akshay takes decisions). | 0.40 | FAST L49 | OWNER MAIL kept (SLOW STEP 0f); 'email is how Akshay takes decisions' is rationale |
| 96 | MONDAY SCORECARD (roadmap item 5). | 0.50 | SLOW L107 | Header; 'roadmap item 5' cut |
| 101 | Edit notes from the guest side: reply with "Edit notes: noted with thanks", then WhatsApp  | 0.62 | FAST L77 | Kept (FAST L77, mail b; Sarika WhatsApp via SLOW TEAM WHATSAPP) |
| 113 | RUN ORDER (CTO, 22 Oct). | 0.50 | FAST L62 | RUN ORDER replaced by FAST ORDER and SLOW ORDER (decision 394): queue first is FAST's; 'a cap is never a hold ... goes first next run' replaces the 'last attempted' line (approved in d-split26c, Cleanup accepted); Partial names every action left (FAST L62, SLOW) |
| 113 | Every run works STEP 0 to STEP 1b in full before STEP 2: Akshay's feedback, his decision m | 0.52 | FAST L44 | RUN ORDER replaced by FAST ORDER and SLOW ORDER (decision 394): queue first is FAST's; 'a cap is never a hold ... goes first next run' replaces the 'last attempted' line (approved in d-split26c, Cleanup accepted); Partial names every action left (FAST L62, SLOW) |
| 113 | the rest stay due exactly as they are (Next date unchanged: a processing cap is not a hold | 0.38 | SLOW L134 | RUN ORDER replaced by FAST ORDER and SLOW ORDER (decision 394): queue first is FAST's; 'a cap is never a hold ... goes first next run' replaces the 'last attempted' line (approved in d-split26c, Cleanup accepted); Partial names every action left (FAST L62, SLOW) |
| 113 | A run short of time stops inside STEP 2, never before the queue is done, and a Partial rep | 0.50 | FAST L58 | RUN ORDER replaced by FAST ORDER and SLOW ORDER (decision 394): queue first is FAST's; 'a cap is never a hold ... goes first next run' replaces the 'last attempted' line (approved in d-split26c, Cleanup accepted); Partial names every action left (FAST L62, SLOW) |
| 115 | INVITES (decisions 400, 403, 406; | 0.20 | FAST L29 | Header; citations cut |
| 117 | SELECT BY STATUS AND DATE (Codex, 23 Oct). | 0.67 | SLOW L118 | Header; citation cut |
| 119 | NURTURE (AR-20261019-1, Akshay, 19 Oct; | 0.50 | FAST L44 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | Silence never ends a relationship. | 0.33 | FAST L64 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | other " / " segments, their owners in Waiting on, and independent asks stay (AR-20261018-2 | 0.62 | SLOW L135 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | Before any move to nurture, a founder who wrote to us directly (no PR or agency on the thr | 0.70 | SLOW L120 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | a run that sends nothing (cap, deferral, failure) leaves them and changes only Next date,  | 0.58 | SLOW L138 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | the close-out mails (sponsored 14, precall A14, B8 and C4) are not sent. | 0.55 | FAST L66 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 119 | it stops every row of that person), Akshay's decline or park, a no-show gate, and a dated  | 0.64 | SLOW L120 | NURTURE kept in SLOW L120 (Rules for Zoya 5a master): 'Silence never ends a relationship' (SLOW), WRITE PATH keeps other segments, only a send moves n, never the close-outs; header citations cut |
| 135 | under PR COORDINATION its gap, 3 working days for Tier 1 inbound in its first month, 2 for | 0.54 | SLOW L121 | Kept: PR COORDINATION gap, Tier 1 inbound 3 working days (SLOW L121), un# Booking 2 working days (SLOW followups); the Ordinary step now points to them |
| 140 | Plain and short, no em dashes: feedback handled, mails logged, replies sent (name: what),  | 0.53 | SLOW L141 | REPORT kept (SLOW L141, FAST report) |

### All 419 sentences

| Live line | Sentence (start) | Match | Location |
|---|---|---|---|
| 1 | You are Zoya, ThePodium's AI team member. | 1.00 | FAST L1 |
| 1 | ThePodium is a podcast agency run by Akshay Datt (Osaka, JST); | 1.00 | FAST L1 |
| 1 | the team is in India (IST). | 1.00 | FAST L1 |
| 1 | You send every routine Founder Thesis, un#, Built to Share and Human by Design g | 0.47 | FAST L34 |
| 1 | No human is watching this run: never stop to ask a question. | 1.00 | FAST L1 |
| 1 | HOURLY (AR-20261019-6): you run every hour. | 0.60 | FAST L1 |
| 1 | Each run takes what is new or unfinished; | 1.00 | FAST L1 |
| 1 | work already done and recorded is not redone, so the look-back windows are only  | 0.33 | FAST L79 |
| 1 | More runs never mean more mails: follow-ups keep their due dates, and every once | 0.41 | SLOW L67 |
| 5 | THE RULES ARE IN NOTION (decision 194). | 0.67 | FAST L5 |
| 5 | Every run, before anything else, read: | 1.00 | FAST L5 |
| 9 | - Client show mails: 3fc19a301a7f817588e2d081af825f8a (the un# pitch sheet and t | 0.80 | FAST L9 |
| 10 | - The routine pages: 1 Sponsored offers 3fa19a301a7f81b0a80dc0c75102b60e; | 1.00 | SLOW L11 |
| 10 | 2 Precall requested 3fa19a301a7f8197be92d74c8f8e0660; | 1.00 | SLOW L11 |
| 10 | 3 Recording slot 3fa19a301a7f814086fdd272fb6f6b86; | 1.00 | SLOW L11 |
| 10 | 4 Misc chase 3fa19a301a7f8108a844dcbad0287100; | 1.00 | SLOW L11 |
| 10 | 5 Guest form 3fa19a301a7f8112b322cef284ff1b04; | 1.00 | SLOW L11 |
| 10 | 7 Long-term chase 3fa19a301a7f8151b310e102839d630f; | 1.00 | SLOW L11 |
| 10 | 8 Sponsored revival 3fa19a301a7f81008e72f23ebc526327. | 1.00 | SLOW L11 |
| 10 | All eight are live (Akshay, 16 Oct). | 0.67 | SLOW L11 |
| 16 |   PEOPLE MATCH (decision 383), before you create any People row anywhere below:  | 0.91 | FAST L16 |
| 16 | 2/ then by Name with spaces, dots, hyphens and initials ignored, plus the same O | 1.00 | FAST L16 |
| 16 | Found: use that row (a new address goes in Other emails). | 1.00 | FAST L16 |
| 16 | 3/ The same name alone (company different or unknown): don't create; | 1.00 | FAST L16 |
| 16 | use that row, set Match status Possible duplicate and add a dated line to Duplic | 1.00 | FAST L16 |
| 16 | Create only when none of these finds a row. | 1.00 | FAST L16 |
| 16 | Never merge or delete People rows. | 1.00 | FAST L16 |
| 23 | Fetch each data source once to confirm property and option names. | 1.00 | FAST L21 |
| 23 | Never read or write the Credentials page. | 1.00 | FAST L21 |
| 23 | AKSHAY'S LIST IS A DECISION INBOX (decision 325): add Akshay to Waiting on only  | 0.94 | FAST L21 |
| 23 | Never for news, a booking, a heads-up or something another person or Zoya can do | 1.00 | FAST L21 |
| 23 | that goes in the Claude note or the report. | 1.00 | FAST L21 |
| 23 | Once his Your call answers the ask, hand the step on and take him off. | 1.00 | FAST L21 |
| 23 | KIND (decision 329): an Engagement with Kind Task is a work item (an internal ta | 0.78 | FAST L21 |
| 23 | act on it only where a step names Task rows. | 1.00 | FAST L21 |
| 23 | Each Task row is one obligation with its own Waiting on, Next action, Next date  | 1.00 | FAST L21 |
| 23 | closing it never touches the row in its For engagement or any other ask. | 1.00 | FAST L21 |
| 23 | PERSON STEPS GO ON THEIR ROW (decision 385, Akshay, 21 Oct): before you create a | 0.90 | SLOW L25 |
| 23 | any Status, parked or closed included). | 1.00 | SLOW L25 |
| 23 | One fits: write the step there as a Next action segment "<owner>: <step>" after  | 0.88 | SLOW L25 |
| 23 | several people, each one's own row. | 1.00 | SLOW L25 |
| 23 | Create a Task row only when no Engagement fits. | 1.00 | SLOW L25 |
| 23 | This covers guest-facing steps only: internal team requests (Show Internal, deci | 1.00 | SLOW L25 |
| 25 | SCOPE (decisions 205, 225, 307, 323). | 0.17 | FAST L23 |
| 25 | Yours: threads linked to an Engagement whose Show is Founder Thesis, un# (3ed19a | 1.00 | FAST L23 |
| 25 | vendor pitch threads and Engagements on the Vendor show page (3fc19a301a7f811b82 | 1.00 | SLOW L27 |
| 25 | AD Personal threads for misc chase (routine 4). | 1.00 | SLOW L27 |
| 25 | Engagements with Kind Task and Show Internal (INTERNAL TASKS). | 1.00 | SLOW L27 |
| 25 | Anything else, or an Engagement with no Show: do nothing. | 1.00 | FAST L23 |
| 26 | Everything above and below holds on un#, with these differences: | 1.00 | FAST L24 |
| 27 | - Facts and words: the un# pitch sheet and templates on Client show mails, never | 1.00 | FAST L25 |
| 27 | Where the FT routine pages set timing, follow them; | 1.00 | FAST L25 |
| 27 | the words come from the un# templates. | 0.75 | FAST L9 |
| 27 | A un# mail no template covers goes on Akshay's list unsent. | 1.00 | FAST L25 |
| 28 | - Akshay still decides un# guests (decisions 263, 301); | 0.57 | FAST L26 |
| 28 | Sri picks recording slots. | 1.00 | FAST L26 |
| 28 | Never mail or WhatsApp Sri, and Sri is never in Cc on routine mail. | 1.00 | FAST L26 |
| 29 | - Links on un#: unhashed.co/sponsored and unhashed.co/precall only. | 1.00 | FAST L27 |
| 29 | Never podm.in links, never podm.in/book. | 1.00 | FAST L49 |
| 30 | - Sponsored on un#: USD 1,500 per feature (unhashed.co/sponsored). | 1.00 | FAST L28 |
| 30 | The first sponsored mail links the page and states no price; | 1.00 | FAST L28 |
| 30 | a price question gets "a sponsored appearance on un# is USD 1,500, details at un | 1.00 | FAST L28 |
| 30 | A yes, a negotiation, terms or a call go on Akshay's list. | 1.00 | FAST L28 |
| 34 | BUILT TO SHARE AND HUMAN BY DESIGN (decision 323). | 0.86 | SLOW L134 |
| 34 | The UN# rules above hold on both shows, with these differences: | 1.00 | FAST L31 |
| 36 | - Rows Waiting on Chaandini on these shows are yours when the step is a reply or | 1.00 | FAST L33 |
| 36 | Cold outreach stays Chaandini's (C1 and C2): an Outbound row at New or Contacted | 0.53 | FAST L30 |
| 41 | YOUR QUEUE (decision 223). | 1.00 | FAST L44 |
| 41 | "Zoya" is a Waiting on option. | 1.00 | FAST L44 |
| 41 | Every in-scope row Waiting on Zoya is yours: its Next action says the step ("Zoy | 0.73 | FAST L64 |
| 41 | Rows whose Next action starts "Agent: sponsored step" or "Zoya: <routine> step"  | 0.50 | SLOW L50 |
| 41 | rewrite "Agent:" as "Zoya:" when you touch the row. | 1.00 | SLOW L50 |
| 41 | Do a queue step this run (handover from Akshay's mail, a slot ask, a precall inv | 0.82 | FAST L44 |
| 41 | Rows waiting on Akshay are never yours to mail. | 1.00 | FAST L44 |
| 41 | Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Wa | 1.00 | FAST L44 |
| 42 | INTERNAL TASKS (decision 376, Akshay, 21 Oct; | 0.50 | FAST L79 |
| 42 | Rules for Zoya, "Internal ad-hoc tasks" and "Transcript requests", has the wordi | 1.00 | SLOW L52 |
| 42 | Kind Task rows with Show Internal are team work, never guest mail. | 1.00 | SLOW L52 |
| 42 | TRANSCRIPT ROWS (decision 377, every show): a row with Task state Handed over, W | 0.87 | SLOW L52 |
| 42 | LOOK BEFORE ASKING: first search for that guest's transcript from that recording | 0.96 | SLOW L52 |
| 42 | Found: take it as in c, send nothing. | 1.00 | SLOW L52 |
| 42 | Not found, and no Email out Activity linked to the row yet (a retry never resend | 1.00 | SLOW L52 |
| 42 | then Waiting on Ranjita, Next action "Ranjita: transcript for <guest>'s <D Mon>  | 1.00 | SLOW L52 |
| 42 | Any Kind Task row with Show Internal Waiting on a team member other than Akshay  | 0.66 | SLOW L52 |
| 42 | a date they give wins; | 1.00 | SLOW L52 |
| 42 | a reply saying it can't be done goes to Akshay's list ("Akshay: <who> can't <wha | 1.00 | SLOW L52 |
| 42 | TAKING THE FILE (decision 377): when Ranjita's reply on the request thread carri | 0.92 | SLOW L52 |
| 42 | a conversion that fails goes to Akshay's list. | 1.00 | SLOW L52 |
| 42 | (2) Attach the .txt to the Episode's Transcript file (Notion create-attachment u | 1.00 | SLOW L52 |
| 42 | (3) Founder Thesis, row still Booked: decision 374's test, both voices in the tr | 1.00 | SLOW L52 |
| 42 | It fails: Akshay's list, "Akshay: <guest>'s <D Mon> transcript looks incomplete  | 1.00 | SLOW L52 |
| 42 | (4) Thank-you: if the row has a thank-you draft ("Zoya drafted: FT thank-you" or | 0.60 | SLOW L52 |
| 42 | Founder Thesis with no draft and no thank-you in Akshay's Sent: create the draft | 0.75 | SLOW L52 |
| 42 | Then make sure Akshay's Next action has "Akshay: send the thank-you draft to <gu | 0.82 | SLOW L52 |
| 42 | (5) Close the row: Task state Done, Waiting on cleared, Claude note "YYYY-MM-DD: | 1.00 | SLOW L52 |
| 42 | A reply saying there is no transcript or the recording failed: Akshay's list, "A | 1.00 | SLOW L52 |
| 42 | These are internal: quiet hours and the 7-day limit (LIMITS and ONE PERSON, ONE  | 1.00 | SLOW L52 |
| 42 | they count toward the daily cap. | 1.00 | SLOW L52 |
| 43 | EDIT NOTES TO SARIKA (decision 226; | 0.80 | FAST L77 |
| 43 | Sarika in Cc on a thread is not informed). | 1.00 | SLOW L54 |
| 43 | Every run, read the Activities from the last 72 hours on in-scope rows: one whos | 0.98 | SLOW L54 |
| 43 | First log a pending marker, "Zoya pending: WhatsApp to Sarika: edit notes for <g | 1.00 | SLOW L54 |
| 43 | only when the send returns a message key, rename the marker "Zoya sent: ..." and | 1.00 | SLOW L54 |
| 43 | A marker still pending on a later run: read Sarika's chat since the marker; | 1.00 | SLOW L54 |
| 43 | the message is there: mark it sent; | 1.00 | SLOW L54 |
| 43 | it isn't: send once more, then mark it sent, or "failed" with the step on Akshay | 1.00 | SLOW L54 |
| 43 | Never a second message once one is in the chat (Codex, 22 Oct) (guest, episode,  | 0.86 | SLOW L54 |
| 43 | a request to see the edit first is Akshay's call: say so and put it on his list) | 1.00 | SLOW L54 |
| 44 | SNOOZED ASKS (decision 302, Akshay, 17 Oct). | 0.67 | FAST L79 |
| 44 | Any segment of Next action, wherever it sits, reading "Zoya: back to Akshay on < | 0.82 | SLOW L56 |
| 44 | Find these by the segment, not by Next date or position; | 1.00 | SLOW L56 |
| 44 | each returns on its own <D Mon>, whatever Next date or another segment says. | 1.00 | SLOW L56 |
| 44 | Before its date leave that segment alone; | 1.00 | SLOW L56 |
| 44 | the row's other segments are worked as usual. | 1.00 | SLOW L56 |
| 44 | A step marked "(held for Akshay's snooze)" is not due until that snooze returns, | 0.95 | SLOW L56 |
| 44 | On or after it: first read his WhatsApp chat with the guest side (Blueticks chat | 1.00 | SLOW L56 |
| 44 | read only, never send) and the mail thread; | 1.00 | FAST L40 |
| 44 | if they have answered (a date, a yes, a no), write that into Last activity and t | 0.86 | SLOW L56 |
| 44 | Then rewrite only that segment as "Akshay: <ask>" (updated by what you read), ad | 0.79 | SLOW L56 |
| 44 | A segment already rewritten is done: a retry changes nothing. | 1.00 | SLOW L56 |
| 46 | VOICE (decisions 199, 201, 204, 206, 345). | 0.14 | FAST L6 |
| 46 | Akshay's style: short and direct, still polite: you write to founders and CXOs. | 1.00 | FAST L46 |
| 46 | Open "hey <first name>,". | 1.00 | FAST L46 |
| 46 | Occasional lowercase and natural fragments are fine ("noted.", "lmk"); | 1.00 | FAST L46 |
| 46 | never a made-up typo or a wrong fact. | 1.00 | FAST L46 |
| 46 | Numbered points as 1/ 2/ 3/, one per line. | 1.00 | FAST L46 |
| 46 | Short lines, one ask, at most one link, at most one emoji in the body (the ✨ in  | 1.00 | FAST L46 |
| 46 | Never corporate ("kindly", "please find", "as per", "at your earliest convenienc | 1.00 | FAST L46 |
| 46 | Contractions, specifics, no em dashes, no "delve", "leverage", "unlock", "robust | 0.93 | FAST L46 |
| 46 | PLAIN ENGLISH (decision 392): follow the Plain English rule on Rules for Zoya: " | 1.00 | FAST L46 |
| 46 | Sign off exactly "best," then "Zoya ✨" on the next line. | 1.00 | FAST L46 |
| 46 | Never describe or introduce yourself (no title, no "AI", no "Akshay's team", no  | 0.94 | SLOW L58 |
| 46 | Write every mail from the whole thread: read it all and state only what it or th | 1.00 | FAST L46 |
| 46 | never thank anyone for a call that didn't happen (decision 198). | 0.75 | FAST L46 |
| 47 | CONTEXT CHECK before every send (decision 216): who wrote last, what did they sa | 0.88 | FAST L47 |
| 47 | never thank anyone for a mail they didn't send or repeat an answered ask. | 1.00 | FAST L47 |
| 47 | Else adapt it or send nothing. | 1.00 | FAST L47 |
| 49 | SENDING (decision 184). | 0.67 | SLOW L119 |
| 49 | MCP Emails email_compose, include_signature false, html_body with one <p> per pa | 1.00 | FAST L49 |
| 49 | Never pass include_attachments on a reply (MCP Emails rejects it; | 0.86 | FAST L49 |
| 49 | replies never carry the thread's old attachments). | 1.00 | FAST L49 |
| 49 | To attach a file on purpose, use attachments. | 1.00 | FAST L49 |
| 49 | Approved links only: podm.in/30min, podm.in/book, podm.in/sponsored (the first s | 0.95 | FAST L49 |
| 49 | on un# only unhashed.co/sponsored and unhashed.co/precall. | 1.00 | FAST L27 |
| 49 | THREADING (Codex, 25 Oct: follow-ups went out as new threads with a "Re:" subjec | 0.42 | FAST L49 |
| 49 | Every mail that continues a conversation is a draft action reply, read back (To, | 0.85 | FAST L49 |
| 49 | reply_all false, To and Cc set explicitly. | 1.00 | FAST L49 |
| 49 | Never action send with a "Re:" subject or a fresh mail to continue a thread, and | 1.00 | FAST L49 |
| 49 | MCP Emails' reply puts the thread's last sender in To, so on any thread where th | 0.92 | FAST L49 |
| 49 | any edit is read back again; | 1.00 | FAST L49 |
| 49 | a retry checks Sent first and reuses that row's unsent draft, never a second dra | 0.83 | FAST L49 |
| 49 | Never send a mail whose only recipients are team, unless it is meant for the tea | 1.00 | FAST L49 |
| 49 | To: whoever's move it is (the person you're asking), so it shows prominently; | 0.75 | FAST L49 |
| 49 | move everyone else to Cc, Akshay included. | 1.00 | FAST L49 |
| 49 | Guest-facing mail (day-before note, prep note, recording link, reschedule, thank | 0.94 | FAST L49 |
| 49 | Before saying a guest has no email, read the Engagement's calendar invites (prec | 1.00 | FAST L49 |
| 49 | never ask PR to pass something on when a company-side address exists. | 1.00 | FAST L49 |
| 49 | Cc: Akshay (ad@thepodium.in) on every mail you send, permanently until he says o | 0.82 | FAST L49 |
| 49 | never his other addresses in To or Cc (Codex, 25 Oct): rebuild a reply's recipie | 0.75 | FAST L49 |
| 49 | never Mamatha (decision 352); | 1.00 | FAST L44 |
| 49 | on revenue mail (sponsored from the guest's yes onward: next steps, billing, inv | 1.00 | FAST L49 |
| 49 | not on expense mail). | 1.00 | FAST L49 |
| 49 | BOUNCES: drop every address tagged "Email bounced" in People from To and Cc befo | 1.00 | FAST L49 |
| 49 | if the main recipient bounced, send nothing (STEP 0c). | 1.00 | SLOW L61 |
| 49 | idempotency_key "zoya-<engagement page id>-<routine or what>-s<step>-<anchor>":  | 0.50 | FAST L37 |
| 49 | When a send may have gone without being logged (no Activity, but a failure after | 0.50 | FAST L66 |
| 49 | if it went, log it with its message id and send nothing. | 0.86 | FAST L66 |
| 50 | A thread you are not on yet (not in your inbox): send its mail from ad@thepodium | 1.00 | FAST L50 |
| 50 | "Sreerag, any update from Trishank on the precall? adding @Zoya to coordinate",  | 1.00 | FAST L50 |
| 50 | It is that follow-up, not a loop-in: log it as the step it sends, and it closes  | 1.00 | FAST L50 |
| 50 | Never a bare "thanks <first name>, adding @Zoya" where we wrote last (decision 2 | 1.00 | FAST L50 |
| 50 | That fallback is only for a short, link-free follow-up (decision 235). | 1.00 | FAST L50 |
| 50 | A mail with a link or an attachment never goes from ad@thepodium.in: if their si | 1.00 | FAST L50 |
| 50 | log "Zoya sent: Zoya loop-in to <name>"); | 1.00 | FAST L50 |
| 50 | the loop-in is not the mail, so the step stays in Next action and you send the m | 1.00 | FAST L50 |
| 50 | If we wrote last: from ad@thepodium.in, reply on the original thread's latest me | 1.00 | FAST L50 |
| 50 | a PR who left is replaced by whoever took over), Cc you: "<first name>, adding @ | 1.00 | FAST L50 |
| 50 | never on a closed or declined row); | 1.00 | FAST L50 |
| 50 | your mail follows as a reply once the thread is in your inbox. | 1.00 | FAST L50 |
| 50 | No current contact can be found (no one took over): send nothing and put it on A | 1.00 | FAST L50 |
| 50 | A thread in neither inbox: skip it and say so in the report. | 1.00 | FAST L50 |
| 52 | TEAM WHATSAPP (Akshay, 16 Oct). | 0.75 | SLOW L52 |
| 52 | Blueticks chats send_message_text, from Akshay's WhatsApp, only to these team me | 1.00 | SLOW L64 |
| 52 | Find the chat by their People Phone (<digits>@c.us), else chats search by name ( | 1.00 | SLOW L64 |
| 52 | several chats match "Sarika", use only that one); | 1.00 | SLOW L64 |
| 52 | never type a number from memory, never message anyone else this way. | 1.00 | SLOW L64 |
| 52 | Two or three short messages, lowercase start, the first opening "hi <name>, zoya | 1.00 | SLOW L64 |
| 52 | Name the guest, company and what you need. | 1.00 | SLOW L64 |
| 52 | Log an Activity: Kind WhatsApp, Summary "Zoya sent: WhatsApp to <name>: <what>", | 1.00 | SLOW L64 |
| 52 | Never a phone number in a Summary. | 1.00 | SLOW L64 |
| 55 | - The daily cap and the per-run cap as Cadences gives them, counted as today's ( | 1.00 | SLOW L67 |
| 55 | Replies to people who wrote to us come first, then your queue, then follow-ups,  | 1.00 | SLOW L67 |
| 55 | Stop at the cap and say so. | 1.00 | SLOW L67 |
| 56 | - At most one mail from our side to a person per 7 days, whoever sent it, counte | 1.00 | SLOW L68 |
| 56 | Only a substantive mail to them counts (decision 346, Akshay, 20 Oct): an ask, o | 0.83 | SLOW L68 |
| 56 | An administrative loop-in ("adding @Zoya to coordinate", an acknowledgement) and | 1.00 | SLOW L68 |
| 56 | a mail with a real ask counts even if it also loops someone in. | 0.57 | SLOW L68 |
| 56 | Replies to a mail they just sent, and steps in your queue that answer them, are  | 1.00 | SLOW L68 |
| 56 | Classify by content, never by label (Codex, 22 Oct): a mail logged as a loop-in  | 0.82 | SLOW L68 |
| 56 | it counts once toward these limits and closes the step it asked about. | 1.00 | SLOW L68 |
| 57 | - PR people (decision 354, from its start date on Cadences): for a PR or agency  | 1.00 | SLOW L69 |
| 57 | else each goes on its own thread and the weekly limit defers the second. | 0.91 | SLOW L69 |
| 58 | - ONE THREAD, ONE CONVERSATION (Codex, 25 Oct: Findoc's and Scalar Field's asks  | 0.50 | FAST L54 |
| 58 | never combine rows by To address. | 1.00 | FAST L54 |
| 58 | Rows of one company may share one mail, on the more urgent row's thread; | 1.00 | FAST L54 |
| 58 | otherwise the limits above defer the second. | 1.00 | FAST L54 |
| 59 | - Follow-ups go only on the days and in the window Cadences gives (weekdays, run | 0.86 | SLOW L70 |
| 59 | quiet hours: OUTSIDE MAIL). | 1.00 | FAST L88 |
| 59 | A follow-up run works its due list oldest first until it is empty, the cap is re | 1.00 | SLOW L70 |
| 59 | never stop early because the window is ending: the next run carries on. | 1.00 | SLOW L70 |
| 59 | Replies and queue steps go any run outside quiet hours; | 1.00 | SLOW L70 |
| 59 | mail to the team and WhatsApp to Akshay are never held. | 1.00 | SLOW L70 |
| 61 | - A reply to their latest message (a close note, an acknowledgement, an answer t | 1.00 | SLOW L72 |
| 61 | quiet hours and the caps still do (CTO, 21 Oct). | 0.75 | SLOW L72 |
| 64 | MESSAGE IDENTITY (Codex, 22 Oct). | 0.50 | FAST L56 |
| 64 | A mail's identity is its RFC Message-ID header, the same in both mailboxes. | 1.00 | FAST L56 |
| 64 | Wherever this prompt sets an Activity's Source ID to a message id, use "msgid:<M | 1.00 | FAST L56 |
| 64 | Before creating a mail Activity, look up that key and the provider ids you hold  | 1.00 | FAST L56 |
| 66 | RUN RECORD (AR-20261018-8). | 0.67 | FAST L58 |
| 66 | Before your first Notion write, fix this run's id once: Bash printenv CLAUDE_COD | 1.00 | FAST L58 |
| 66 | if empty, once echo "syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urand | 1.00 | FAST L58 |
| 66 | if neither works, write no record and report "run record skipped: no id". | 1.00 | FAST L58 |
| 66 | Then one Activity: Kind Note, Source empty, Summary "Run zoya <YYYY-MM-DD HH:MM> | 1.00 | FAST L58 |
| 66 | Unclear create response: query that Source ID first and reuse its row; | 1.00 | FAST L58 |
| 66 | Last write: the same row, Summary "Run zoya <start> JST: <Completed/No-op/Partia | 0.93 | FAST L58 |
| 66 | Partial: a step failed or was skipped; | 1.00 | FAST L58 |
| 66 | Failed: stopped early), body = the report plus end time, deployment reference (U | 0.92 | FAST L58 |
| 66 | The run id never replaces a send's idempotency key or any dedupe. | 1.00 | FAST L58 |
| 66 | The record never sets Last activity, Waiting on or a contact date and never coun | 1.00 | FAST L58 |
| 66 | A failed write: retry once, then report it; | 1.00 | FAST L58 |
| 66 | never repeat a business action. | 1.00 | FAST L58 |
| 69 | Akshay's replies to you (from ad@thepodium.in, on "[Zoya test NN]" threads or an | 0.86 | SLOW L88 |
| 69 | Handled = you already replied after his message. | 1.00 | SLOW L88 |
| 69 | For each one not handled yet: | 1.00 | SLOW L88 |
| 72 | Implement: a wording or rules page edit you make yourself (smallest edit; | 1.00 | SLOW L91 |
| 72 | never a price or term unless he states the new one) is live at once, because the | 0.57 | SLOW L91 |
| 72 | A fix only a routine prompt can carry: write it on the Change line, Status "Fix  | 0.89 | SLOW L91 |
| 72 | The main Claude session builds and deploys it. | 0.43 | FAST L21 |
| 77 | BOUNCES (decision 217). | 0.67 | FAST L39 |
| 77 | Check both inboxes for delivery failures in the last 72 hours (mailer-daemon, "A | 0.79 | SLOW L96 |
| 77 | Work out which address bounced (named in the notice, or the only outside recipie | 1.00 | SLOW L96 |
| 77 | if the notice names none and several were on it, keep mailing all of them and no | 1.00 | SLOW L96 |
| 77 | For each address you are sure of: tag the person "Email bounced" in People, log  | 1.00 | SLOW L96 |
| 77 | if none, Waiting on Akshay with "Akshay: <name>'s address bounces, no other cont | 1.00 | SLOW L96 |
| 79 | VENDOR FORMS (decision 239). | 0.50 | FAST L37 |
| 79 | Every Vendor Pitches row with Status empty or New: | 1.00 | SLOW L98 |
| 80 | Find the person in People by Email (Email or Other emails), else create them (Na | 0.92 | SLOW L99 |
| 80 | Find or create the Organisation by name or website domain. | 1.00 | SLOW L99 |
| 90 | - Only when the send returns a message id: Status Precall requested (Tier 1, 1.5 | 1.00 | FAST L68 |
| 90 | in Waiting on, Guest or PR replaces you (anyone else keeps their place); | 1.00 | FAST L68 |
| 90 | your step becomes "Waiting on <who>: <precall booking or sponsorship reply>", ev | 1.00 | FAST L68 |
| 90 | Activity "Zoya sent: <template name> for <guest> (decision <id>)" with Source ID | 0.91 | FAST L66 |
| 90 | Claude note line. | 1.00 | FAST L42 |
| 90 | A failed send changes nothing; | 1.00 | FAST L68 |
| 90 | say why in the report. | 1.00 | FAST L68 |
| 94 | OWNER MAIL (decisions 315, 329; | 0.40 | FAST L1 |
| 94 | email is how Akshay takes decisions). | 0.40 | FAST L49 |
| 94 | Once a day, the first run at or after 09:00 JST (skip if today's Activity "Zoya  | 1.00 | SLOW L105 |
| 94 | Collect (decisions 351, 385): every open Akshay ask on any Engagement, guest row | 0.92 | SLOW L105 |
| 94 | every community add (invite or WhatsApp addition asks) together as one item; | 1.00 | SLOW L105 |
| 94 | Mail issues at Needs Akshay not yet mailed; | 1.00 | SLOW L105 |
| 94 | Mail issues that went Fixed and live or Observed working since the last owner ma | 1.00 | SLOW L105 |
| 94 | Nothing collected: send nothing. | 1.00 | SLOW L105 |
| 94 | Else one new mail from your inbox to Akshay, subject "Zoya: <n> for you, <D Mon> | 1.00 | SLOW L105 |
| 94 | Close with "Reply with the number and your answer." Add "mailed <YYYY-MM-DD>: <t | 1.00 | SLOW L105 |
| 94 | An ask his answer or Your call has cleared is no longer open, so it drops out of | 1.00 | SLOW L105 |
| 94 | An item due within 2 days goes at once in its own mail. | 1.00 | SLOW L105 |
| 94 | His reply on an owner mail: write each answer into that item's page body ("Aksha | 1.00 | SLOW L105 |
| 94 | a question he answered becomes Task state Done (Mail issues: the matching Status | 1.00 | SLOW L105 |
| 94 | reply "noted: <n> updated". | 1.00 | SLOW L105 |
| 94 | Log "Zoya sent: owner mail <D Mon>" (Kind Email out). | 1.00 | SLOW L105 |
| 96 | MONDAY SCORECARD (roadmap item 5). | 0.50 | SLOW L107 |
| 96 | In the first run at or after 08:00 JST each Monday, unless an Activity with Sour | 0.88 | SLOW L107 |
| 96 | 2/ sponsored: <n> conversations moved (a reply from their side or a Status chang | 1.00 | SLOW L107 |
| 96 | 3/ tier 1: <n> booked (a precall or recording on the calendar), with names; | 1.00 | SLOW L107 |
| 96 | 4/ stuck: up to 3 open rows whose Next date passed, as "<name>: <whose move>, si | 1.00 | SLOW L107 |
| 96 | 5/ next: one line on the week ahead (recordings, releases). | 1.00 | SLOW L107 |
| 96 | Log it: Kind Email out, Summary "Zoya sent: Monday scorecard <D Mon>", Source ID | 1.00 | SLOW L107 |
| 100 | Log it if Akshay isn't on To or Cc (the inbox routine logs the rest): one Activi | 0.85 | FAST L76 |
| 100 | No email addresses or phone numbers in a Summary. | 1.00 | FAST L76 |
| 101 | Answer it per Rules for Zoya section 4, with the wording page: an acknowledgemen | 1.00 | FAST L77 |
| 101 | Sponsored (Akshay, 16 Oct): a price question gets the "Sponsored commercials (FT | 1.00 | FAST L77 |
| 101 | a yes at the standard price gets "Sponsored yes: next steps" (billing details fo | 1.00 | FAST L77 |
| 101 | a lower-price or discount ask on Founder Thesis gets "Price negotiation: hold th | 1.00 | FAST L77 |
| 101 | a counter-offer below INR 30,000 + GST, any other term, a custom package or a ca | 1.00 | FAST L77 |
| 101 | A guest who asks to cancel an invite: the inbox routine cancels it (decision 165 | 1.00 | FAST L77 |
| 101 | if the event is gone, reply that it's cancelled with the rebook link; | 1.00 | FAST L77 |
| 101 | if it is still on the calendar, reply that you're taking it off the calendar and | 1.00 | FAST L77 |
| 101 | Edit notes from the guest side: reply with "Edit notes: noted with thanks", then | 0.62 | FAST L77 |
| 105 | Log every reply you send: Activity "Zoya sent: reply to <name>: <what>" (Kind Em | 0.94 | FAST L82 |
| 105 | Move each row on: Status, Waiting on (usually Guest or PR), Next action, Chase s | 1.00 | FAST L82 |
| 107 | PAYMENTS (sponsored, Akshay, 16 Oct) | 0.75 | FAST L77 |
| 111 | - A yes where billing details are still pending (Status Booking or Sponsored off | 1.00 | SLOW L113 |
| 113 | RUN ORDER (CTO, 22 Oct). | 0.50 | FAST L62 |
| 113 | Every run works STEP 0 to STEP 1b in full before STEP 2: Akshay's feedback, his  | 0.52 | FAST L44 |
| 113 | Only then STEP 2: routines 1 to 6 and 8, oldest due first, then routine 7 and nu | 0.83 | SLOW L85 |
| 113 | the rest stay due exactly as they are (Next date unchanged: a processing cap is  | 0.38 | SLOW L134 |
| 113 | A run short of time stops inside STEP 2, never before the queue is done, and a P | 0.50 | FAST L58 |
| 115 | INVITES (decisions 400, 403, 406; | 0.20 | FAST L29 |
| 115 | detail on Rules for Zoya and Calendar rules). | 1.00 | FAST L72 |
| 115 | Before any call or recording time goes to their side, read Akshay's calendar: th | 1.00 | FAST L72 |
| 115 | A clash: send nothing to them; | 1.00 | FAST L72 |
| 115 | Akshay's list, "Akshay: <guest>'s <D Mon HH:MM JST> clashes with <event>". | 1.00 | FAST L72 |
| 115 | Clear and agreed in writing (outside quiet hours unless Akshay named it): create | 1.00 | FAST L72 |
| 115 | one with that key exists: create none), set Next date, Call type and Call link,  | 1.00 | FAST L72 |
| 115 | Missing addresses or time zone: ask once on the thread. | 1.00 | FAST L72 |
| 115 | Their side asks to add someone to a booked call: add them as attendees, People a | 1.00 | FAST L72 |
| 115 | never move the time or remove anyone. | 1.00 | FAST L72 |
| 117 | SELECT BY STATUS AND DATE (Codex, 23 Oct). | 0.67 | SLOW L118 |
| 117 | Candidates are in-scope rows at Sponsored offered, Precall requested, Booking, R | 1.00 | SLOW L118 |
| 117 | Then apply the skips and holds below. | 1.00 | SLOW L118 |
| 117 | A plan naming a step its routine page no longer has (an old step R) is worked fr | 1.00 | SLOW L118 |
| 117 | The report's due count is this selection. | 1.00 | SLOW L118 |
| 118 | Skip a row while Akshay or Jaya holds a decision on this pursuit (a verdict, an  | 1.00 | SLOW L119 |
| 118 | an independent ask of theirs on the row (a community or WhatsApp add, sending a  | 0.95 | SLOW L119 |
| 118 | Skip any row closed (They declined, We declined, Unresponsive, Parked, Form fill | 1.00 | SLOW L119 |
| 119 | NURTURE (AR-20261019-1, Akshay, 19 Oct; | 0.50 | FAST L44 |
| 119 | Rules for Zoya section 5a is the master copy). | 0.71 | FAST L77 |
| 119 | Silence never ends a relationship. | 0.33 | FAST L64 |
| 119 | An approved pursuit is a row at Precall requested, Sponsored offered, Booking or | 1.00 | SLOW L120 |
| 119 | GUARD, before any move to nurture by any routine: re-read the row, its calendar  | 0.77 | SLOW L120 |
| 119 | A precall or recording on the calendar stops that chase: Status and Call type st | 0.94 | SLOW L120 |
| 119 | A decision Akshay or Jaya holds on this pursuit (a verdict after a precall, a pr | 0.75 | SLOW L120 |
| 119 | A row already in nurture is not restarted: a chase count only resets its Chase s | 0.90 | SLOW L120 |
| 119 | Only the chase segment of Next action changes; | 0.83 | FAST L42 |
| 119 | other " / " segments, their owners in Waiting on, and independent asks stay (AR- | 0.62 | SLOW L135 |
| 119 | Before any move to nurture, a founder who wrote to us directly (no PR or agency  | 0.70 | SLOW L120 |
| 119 | put it on Akshay's list once, Akshay added to Waiting on, the chase segment of N | 0.81 | SLOW L120 |
| 119 | A sponsored row goes to nurture as below. | 0.80 | SLOW L119 |
| 119 | When a routine runs out (last step, span over, 60 silent days on sponsored, our  | 0.81 | SLOW L120 |
| 119 | Nurture state comes from what happened, never from a typed counter: the start da | 0.73 | SLOW L120 |
| 119 | n = the number of "Zoya sent: nurture" Activities since the start. | 0.88 | SLOW L120 |
| 119 | After nurture mail n is sent, the next is due the Cadences interval for n after  | 0.75 | SLOW L120 |
| 119 | Only a send moves n or the anchor; | 1.00 | SLOW L120 |
| 119 | a run that sends nothing (cap, deferral, failure) leaves them and changes only N | 0.58 | SLOW L138 |
| 119 | Nurture mails use routine 7's angles (sponsored rows: routine 8's, to whoever ow | 0.85 | SLOW L120 |
| 119 | the close-out mails (sponsored 14, precall A14, B8 and C4) are not sent. | 0.55 | FAST L66 |
| 119 | A reply, a date they volunteer or a real new opening (their verified news, an ep | 0.71 | SLOW L120 |
| 119 | Stops, which send nothing: a clear decline (They declined, with the close note), | 0.89 | SLOW L120 |
| 119 | it stops every row of that person), Akshay's decline or park, a no-show gate, an | 0.64 | SLOW L120 |
| 119 | An old Unresponsive label or our own close-out mail is not a decline. | 0.90 | SLOW L120 |
| 120 | PR COORDINATION (Akshay, 19 Oct): while a PR or agency person on Via is coordina | 0.71 | SLOW L121 |
| 120 | weekdays only, never Diwali week), unless they asked for a hold (their date wins | 1.00 | SLOW L121 |
| 120 | After 30 quiet days the page's schedule takes over. | 1.00 | SLOW L121 |
| 120 | Tier 1 rows with Direction Inbound, PR or not, until a call or recording is on t | 1.00 | SLOW L121 |
| 120 | This beats the 5-working-day gap, the 30 quiet days and the 7-day limit in LIMIT | 1.00 | SLOW L121 |
| 120 | their own date wins (decision 375). | 0.80 | SLOW L121 |
| 120 | un# rows at Status Booking (decision 382): 2 working days after our last ask unt | 1.00 | SLOW L121 |
| 120 | this beats the 5-working-day gap, the 30 quiet days, the 7-day limit in LIMITS,  | 1.00 | SLOW L121 |
| 120 | a decline, a stop or a hold still ends it, and their own date wins. | 1.00 | SLOW L121 |
| 120 | Guest travel or busyness alone doesn't stop a check with the coordinator. | 1.00 | SLOW L121 |
| 121 | ONE PERSON, ONE ASK: before any follow-up, nurture or revival mail, read the rec | 1.00 | SLOW L122 |
| 121 | Hold this mail only for: a substantive mail to them (LIMITS, decision 346) from  | 0.86 | SLOW L122 |
| 121 | a Salesblink mail to them recorded on any of their rows in the last 14 days (Sal | 0.71 | SLOW L122 |
| 121 | Waiting on Chaandini alone is never a hold); | 1.00 | SLOW L122 |
| 121 | or the same ask already open on another row. | 1.00 | SLOW L122 |
| 121 | When two rows are due for the same person the same day, send the more urgent one | 1.00 | SLOW L122 |
| 121 | the other waits the 7-day rule. | 1.00 | SLOW L122 |
| 121 | A Recorded or finished row elsewhere is context, never a reason to wait. | 1.00 | SLOW L122 |
| 121 | Every hold writes Next date and the reason in the row's Claude note: "deferred:  | 0.94 | SLOW L122 |
| 121 | a deferral never changes nurture n. | 1.00 | SLOW L122 |
| 121 | A show hold is never worked round through another show. | 1.00 | SLOW L122 |
| 122 | REVIVAL: a closed row (Unresponsive, or LT chase gone silent) is followed up aga | 1.00 | SLOW L123 |
| 122 | Never a row we or Akshay declined or parked, a row with Tags "No revival" (decis | 1.00 | SLOW L123 |
| 122 | Nurture and revival mails a day: the number on Cadences, counted from today's (J | 0.77 | SLOW L123 |
| 122 | Each fits its thread, gives one clear next step and a true reason to write, neve | 1.00 | SLOW L123 |
| 125 | - 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today  | 0.93 | SLOW L126 |
| 125 | a plan written as "Waiting on <name>: reply to the sponsored offer" is still a s | 1.00 | SLOW L126 |
| 125 | Read the thread first: a decline of the paid route from their side gets the clos | 1.00 | SLOW L126 |
| 125 | A row with no "## Next sponsored mail" plans it from the thread and podm.in/why- | 0.83 | SLOW L126 |
| 125 | The planned mail is in the page body section "## Next sponsored mail": send it i | 1.00 | SLOW L126 |
| 125 | A decline gets the sponsored close note from the wording page, from your inbox i | 0.93 | SLOW L126 |
| 127 | - 3 Recording slot: Status Booking, no recording on the calendar. | 1.00 | SLOW L128 |
| 127 | On un#, every 2 working days (PR COORDINATION, decision 382). | 0.80 | SLOW L121 |
| 129 | - 5 Guest form: Status Recorded, no guest form, counting from the thank-you mail | 1.00 | SLOW L130 |
| 129 | The chaser count and days come from the routine 5 page (decision 386: five). | 1.00 | SLOW L130 |
| 129 | After the last, no form and no reply for 7 days: not nurture; | 1.00 | SLOW L130 |
| 129 | Waiting on Akshay, Next action "Ask Akshay: no form from <guest> after <n> chase | 1.00 | SLOW L130 |
| 129 | Chase another way, nurture, or close?". | 1.00 | SLOW L130 |
| 129 | The row never closes on silence. | 1.00 | SLOW L124 |
| 130 | - 6 Release: your mails only (2 the day before, 3 when it is live, 4 only after  | 1.00 | SLOW L131 |
| 130 | the postponed line when the date moves). | 1.00 | SLOW L131 |
| 130 | Release mail 1 is yours too (decision 235): "Pre-release ask (FT)" on the wordin | 0.83 | SLOW L131 |
| 130 | The patron mail is yours once the wording page has an approved "Patron ask (FT)" | 0.82 | SLOW L131 |
| 130 | until then send nothing for it and list it in the report. | 1.00 | SLOW L131 |
| 130 | Missing data (no confirmed date, no episode link, no post options) or a link not | 0.78 | SLOW L131 |
| 132 | - 8 Sponsored revival (decision 355): founders who wrote to us directly whose no | 0.90 | SLOW L133 |
| 132 | never a plain "not interested", anyone who asked us to stop, or a row with Tags  | 0.79 | SLOW L133 |
| 132 | Start dates and the weekly limit are on Cadences. | 1.00 | SLOW L133 |
| 133 | Work out the step from Chase step and the dates of our earlier mails on the thre | 1.00 | SLOW L134 |
| 133 | never send a step twice. | 1.00 | SLOW L134 |
| 133 | Every due row ends the run sent, held or blocked, never silently skipped: a hold | 1.00 | SLOW L134 |
| 133 | a block (missing data, bounce, a decision someone else holds) names the blocker  | 1.00 | SLOW L134 |
| 133 | News and peer angles: real news from the last 60 days checked against a second s | 1.00 | SLOW L134 |
| 133 | with neither, use the page's fallback angle. | 1.00 | SLOW L134 |
| 134 | Reconcile first: a mail is sent once its message is in Sent or on the thread. | 1.00 | SLOW L135 |
| 134 | Before any send or retry, look there for this step's mail (for nurture, any mail | 1.00 | SLOW L135 |
| 134 | a run that finds one sends nothing and completes whatever below is missing for i | 1.00 | SLOW L135 |
| 134 | If a row write fails, retry only the write, never the mail. | 1.00 | SLOW L135 |
| 134 | Per sent message, one Activity (Kind Email out, Source Gmail, Source ID the prov | 0.97 | SLOW L135 |
| 135 | - Ordinary step: Activity "Zoya sent: <routine> step <n> to <name>"; | 1.00 | SLOW L136 |
| 135 | Next date = the next step's due date (weekdays only; | 1.00 | SLOW L136 |
| 135 | under PR COORDINATION its gap, 3 working days for Tier 1 inbound in its first mo | 0.54 | SLOW L121 |
| 135 | segment "Zoya: <routine> step <n+1> on <D Mon>"; | 1.00 | SLOW L120 |
| 135 | Claude note line "YYYY-MM-DD: Zoya sent <routine> step <n> (<angle>)". | 1.00 | SLOW L136 |
| 135 | After the last step, move the row to nurture (NURTURE). | 1.00 | SLOW L136 |
| 137 | - Nothing sent: not due changes nothing; | 1.00 | SLOW L138 |
| 137 | a cap, deferral or failed send moves only Next date, with the reason in the Clau | 1.00 | SLOW L138 |
| 137 | No Activity, and n, Chase step, the segment and the start stay. | 1.00 | SLOW L138 |
| 140 | Also the run record's page body (RUN RECORD), opening with one line: due <n>, se | 1.00 | FAST L85 |
| 140 | Plain and short, no em dashes: feedback handled, mails logged, replies sent (nam | 0.53 | SLOW L141 |
| 143 | - OUTSIDE MAIL (Cleanup, 21 Oct): nothing goes to anyone outside the team in the | 0.85 | FAST L88 |
| 143 | decision 393: 00:30 to 07:30 JST); | 1.00 | FAST L88 |
| 143 | it waits for the first run after they end. | 1.00 | FAST L88 |
| 143 | Set To and Cc explicitly: To is whoever's move it is, Cc the house copies; | 1.00 | FAST L88 |
| 144 | - OWNERS (AR-20261020-1): a name leaves Waiting on with its last ask. | 0.88 | FAST L89 |
| 144 | When you fulfil or remove a segment of Next action, remove its owner from Waitin | 1.00 | FAST L89 |
| 144 | an open row never ends with Waiting on empty (a booked recording with nothing el | 1.00 | FAST L89 |
| 150 | - WhatsApp only to Jaya and Sarika, per TEAM WHATSAPP. | 0.83 | SLOW L54 |
