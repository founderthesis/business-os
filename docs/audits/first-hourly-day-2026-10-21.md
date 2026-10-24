# Observation: 20 Oct 11:47 UTC to ~23:00 UTC (20:47 JST 20 Oct to 08:00 JST 21 Oct)

Read-only. Names only, no addresses. Day = 08:00-23:00 JST, night = 23:00-08:00 JST.

## 1. Routines

### 1a. Installed (trigger config, read 23:01 UTC)

| Routine | Trigger | Cron (JST) | Model | Enabled | Prompt bytes | Last run (UTC) | Last status | Last session |
|---|---|---|---|---|---|---|---|---|
| Inbox | trig_0189eZvAD8x4357cfevgZ3No | :02 hourly | claude-sonnet-5-5 | yes | 65,324 (cap 65,536, 212 B headroom) | 22:04 | SUCCEEDED | cse_01KEfbBaPW99e1L64pnE8zd9 |
| Zoya | trig_01UPT8LDrBDL5JQqW91Awgbo | :30 hourly (fires ~:38) | claude-sonnet-5-5 | yes | 49,048 | 22:38 | SUCCEEDED | cse_01VvXcFZ77V52hLiZPqMAN5h |
| Calendar sync | trig_01Voiz5YsK2SnVf2STF8PoSH | :35 hourly | claude-sonnet-5-5 | yes | 56,059 | 22:36 | SUCCEEDED | cse_013FhzpAisCMsA2Yr9Uc9hSS |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | 13:10 Mon-Fri | claude-sonnet-5-5 | yes | (inline) | 04:10 (20 Oct, before window) | SUCCEEDED | cse_01RfCFtCsds32ZRTE4qnvFBU |
| WhatsApp | trig_01MnmJYorWrd61K7b5BCqXr1 | :45 hourly | claude-sonnet-5-5 | yes | (inline) | 22:46 | SUCCEEDED | cse_01LzwyDCp1rG3KxPhrJ7mN7U |
| Host boards | trig_01K8bueCr2xsPkbgQzjeRKsz | :15 hourly | claude-sonnet-5-5 | yes | (inline) | 22:15 | SUCCEEDED | cse_01JKJk4pTpPgdpE4zUhe7mjV |
| Evals | trig_01R1yHgEztVEo832zMwUugBr | :25 hourly | claude-sonnet-5-5 | yes | (inline) | 22:25 | SUCCEEDED | cse_018egwtLkDw8i4s1494DeqPZ |

All seven updated between 11:33 and 11:47 UTC on 20 Oct. Evals runs in a different environment (Cowork remote) with 17 connectors attached; the others run in the standard cloud env.

### 1b. Observed runs and cost

Mapping limits: list_sessions does not return scheduled-trigger sessions (and the tags filter is unavailable), so runs can only be mapped where a session id is known. Zoya writes a run record per run (Source ID `run:zoya:<session>`), so all 11 Zoya runs are mapped. For the other routines only the last run (from get_trigger) is known; their earlier runs in the window could not be enumerated, so their totals below are one run each, not the window total. Cost is `usage.cost_usd` from get_session. served model = session_context.model = last_served_model = claude-sonnet-5-5 on every session read (no fallback). All status_bucket REVIEW_READY, session_status IDLE.

| Routine | Session | Start UTC | Start JST | Band | Duration | cost_usd |
|---|---|---|---|---|---|---|
| Zoya | cse_015sB33dxtkJGt4jFZNkfErh | 12:32 | 21:32 | day | 3m36s | 1.689 |
| Zoya | cse_01PJt5nZ7hGXcxNifb7rNGwB | 13:38 | 22:38 | day | 2m23s | 1.471 |
| Zoya | cse_01GbCGKHP4nLcXpVNPTsmpcC | 14:38 | 23:38 | night | 59s | 0.773 |
| Zoya | cse_013WfiaJ6KHiRryPCN4oiZYL | 15:38 | 00:38 | night | 1m11s | 0.926 |
| Zoya | cse_01FBdPLjGXAZpM8ZTMhL3ixm | 16:38 | 01:38 | night | 3m34s | 1.828 |
| Zoya | cse_01ByAuhSPGR21gRRPhS996PU | 17:38 | 02:38 | night | 1m38s | 1.047 |
| Zoya | cse_01J3QVt1THDXRG2SyaxP6GdJ | 18:38 | 03:38 | night | 1m43s | 1.003 |
| Zoya | cse_01AGLxTBjHYwpRagXgq6u7Af | 19:38 | 04:38 | night | 1m31s | 1.014 |
| Zoya | cse_018NyBqtwAAAdcqLuc41uSX7 | 20:38 | 05:38 | night | 1m16s | 0.774 |
| Zoya | cse_01JpUruwqMhHhNdqbqEYnHpq | 21:38 | 06:38 | night | 1m34s | 0.893 |
| Zoya | cse_01VvXcFZ77V52hLiZPqMAN5h | 22:38 | 07:38 | night | 52s | 0.910 |
| Inbox | cse_01KEfbBaPW99e1L64pnE8zd9 | 22:04 | 07:04 | night | 1m32s | 0.902 |
| Host boards | cse_01JKJk4pTpPgdpE4zUhe7mjV | 22:15 | 07:15 | night | 2m27s | 1.380 |
| Evals | cse_018egwtLkDw8i4s1494DeqPZ | 22:25 | 07:25 | night | 4m11s | 5.255 (5 eval pages published) |
| Calendar | cse_013FhzpAisCMsA2Yr9Uc9hSS | 22:36 | 07:36 | night | 1m10s | 1.039 |
| WhatsApp | cse_01LzwyDCp1rG3KxPhrJ7mN7U | 22:46 | 07:46 | night | 1m06s | 0.880 |
| Daily sweep | none in window | | | | | |

| Routine | Runs mapped | Day $ | Night $ | Total $ | Complete for window? |
|---|---|---|---|---|---|
| Zoya | 11 | 3.16 | 9.17 | 12.33 | yes |
| Inbox | 1 | 0 | 0.90 | 0.90 | no (about 11 runs expected) |
| Calendar | 1 | 0 | 1.04 | 1.04 | no |
| WhatsApp | 1 | 0 | 0.88 | 0.88 | no |
| Host boards | 1 | 0 | 1.38 | 1.38 | no |
| Evals | 1 | 0 | 5.25 | 5.25 | no |
| Daily sweep | 0 | 0 | 0 | 0 | yes (no run in window) |
| Mapped total | 16 | 3.16 | 18.62 | 21.78 | partial |

Zoya alone: 9 night runs cost $9.17 and sent 2 mails between them. Evals is the most expensive single run seen ($5.25).

## 2. Activities

Activities data source: collection://290f715d-fd45-4203-ade6-3642c2326c6c. Kind options: Email in, Email out, Meeting, Call notes, Form, WhatsApp, Note, Draft.

### 2a. Zoya run records (11)

| Created UTC | Summary (as written) | due | sent | held | blocked | remaining | Notes |
|---|---|---|---|---|---|---|---|
| 12:32 | 21:33 JST: Partial | ~90 | 1 | 0 | 0 | ~89 | Only send: LT chase to Simran (Mobavenue), from ad@. Window "nearly spent"; the rest left |
| 13:39 | 22:39 JST: Partial | 70+ | 1 (owner mail) | all follow-ups | 0 | carried to 21 Oct 16:00 | Started after the 22:00 window closed |
| 14:38 | 23:39 JST: No-op | 0 | 0 | 70+ | 0 | to 21 Oct 16:00 | |
| 15:39 | 00:38 JST: No-op | 0 | 0 | 70+ | 2 | 0 | Nutrishilp, ShelfRadar loop-ins blocked |
| 16:38 | 01:38 JST: Completed | 0 | 1 | 0 | 0 | 0 | Reply to Katherine (Serotonin, un#); 2 bounces tagged |
| 17:38 | "2026-10-20 23:38 JST": No-op | 0 | 0 | 0 | 0 | 0 | Label wrong: real time 02:38 JST 21 Oct; run noted its clocks disagreed |
| 18:38 | 03:38 JST: Completed | 1 | 1 | 0 | 0 | 0 | Reply to Abhinav (TYC); Akshay landed in To, not Cc |
| 19:38 | 04:38 JST: No-op | 0 | 0 | 0 | 2 | 0 | Shilpi Goel, Madhu Sudan loop-ins blocked |
| 20:38 | 05:40 JST: No-op | 0 | 0 | many | 0 | 0 | |
| 21:39 | 06:40 JST: No-op | 0 | 0 | many | 0 | 0 | |
| 22:38 | 07:38 JST: No-op | 0 | 0 | 0 | 0 | 0 | Mail issues, bounces, vendor forms, owner mail not checked |

Mixed Date conventions on these rows (some date-only, some datetime; Captured flips between 20 and 21 Oct). Two night runs (01:38, 03:38) did send routine replies inside quiet hours.

### 2b. Email out created in window (56 rows)

Zoya sends (10):

| Created UTC | Summary | Source ID | Engagement |
|---|---|---|---|
| 12:35 | Zoya sent: LT chase follow-up to Simran (Mobavenue), from ad@ with Zoya added | 1a1594eed7fbbcf9 | Ishank Joshi @ Mobavenue row (3f019a301a7f81688a10fb6d95f13243) |
| 13:40 | Zoya sent: owner mail 20 Oct | mcpemails id | none |
| 13:53 | Zoya sent: recording slot ask to Muskaan (Value360) for Vijay Bansal (Cantabil) | mcpemails id | 3f719a301a7f812fbf1bc5a207741bd8 |
| 15:07 | Zoya sent: holding reply to Kristina (Bigleap) | 1a159d8b207301b2 | 3ff19a301a7f81a98224ee27aa4a5a7d |
| 15:07 | Zoya sent: sponsored close to David (Pranos) | 1a159d8ac6717814 | 3f319a301a7f81ba8cb6d924ae0eef78 |
| 16:40 | Zoya sent: reply to Katherine: still waiting on the host's slots | mcpemails id | 3f119a301a7f81f0b3e9f9d4ed8a2cf6 |
| 17:05 | Zoya sent: vendor redirect to Bharti (Beyondbrnd) | 1a15a45e36b603cd | none |
| 18:38 | Zoya sent: Recording tomorrow to Michelle (Nucleus PR) for Rohan Ganapathy (Bellatrix) | **EMPTY** | 3f019a301a7f81b68cdcd52ae33e1e90 |
| 18:39 | Zoya sent: reply to Abhinav: thanks, will wait for Naresh's answer | mcpemails id | 3f019a301a7f8143ad15c89c1bcd4418 |
| 20:04 | Zoya sent: holding reply to Emmanuel (Podcast Works) | 1a15aea80437c6d9 | 3ff19a301a7f81a8a754c14597421e3e |

The 5 "Zoya sent" rows with Gmail-style ids (Simran, Kristina, David, Bharti, Emmanuel) went from ad@thepodium.in via Gmail, not from Zoya's inbox. The 18:38 Recording tomorrow row is the only Email out with an empty Source ID. Run records mention only 4 Zoya sends; the inbox/calendar routines account for the others.

Other Email out (46): 20 "Akshay: Zoya loop-in to <name>" rows at 14:36 (one batch, one row each for Nikhil Madan, Nitin Kaushal, Abhishek Srivastava, Director (name not given), Varun Mukhi, Teja Gudena, Sashank Rishyasringa, Naresh Kumar Kumawat, Harpreet Singh and Abhinav Awal, Vaibhav Krishnaswamy, David Astoria, Pavan Kosaraju, Sonu Kumar Yadav, Yash Varyani, Praveen Gadelli, Ajinkya Dhariya, Navneet Chitkara, Arushi Kapoor, Shekar Swamy and Srinivasan K. Swamy, Lavanya Jayashankar); Akshay to Lital (CHEQ) x3, Veer (Fyn), Thomas Johnson x3, Ashmita (FieldAssist) x3, others; plus the re-logged 19 Oct mails below. Rows with no Engagement: owner mail, Ashmita x3 (FieldAssist Pathfinders), Chaandini to Jessica, Tanuj (Wryto), Vineeta (AppsForBharat), Bharti.

### 2c. Duplicates

**Simran / Mobavenue (1a1594eed7fbbcf9): one Activity only.** No second row from the inbox for the Cc copy, none from the calendar routine. Not duplicated.

**Inbox re-logging (real duplicates).** 24 message ids already logged on 19 Oct were logged again at 15:07:11 UTC, and 5 of them a third time at 21:05:27 UTC. 29 duplicate rows created in the window, 18 of them Kind Email out.

| Source ID | Copies | What |
|---|---|---|
| 1a156014a249f711 | 3 (19 Oct 23:11, 20 Oct 15:07, 21:05) | Akshay to Surabhi (EvoluteIQ): which time zone |
| 1a1560038717dc7a | 3 | Akshay to Amanda (Gather AI): assets via thank-you form |
| 1a155ff1f7230684 | 3 | Akshay to Amanda (Gather AI): release is 3+ months |
| 1a155f3b6ac335d6 | 3 | Amanda to Akshay (Email in) |
| 1a15508f8eeda88e | 3 | Surabhi to Akshay (Email in) |
| 1a1531a61598725a | 3 | Neeti (Think Que): logged as "Zoya sent: loop-in", then "Akshay ... adding Zoya", then "Akshay ... Zoya loop-in" |
| 1a15414f5120037b, 1a154bc0d42425a3, 1a154bc17c2ec63d | 2 each | Same message logged 19 Oct as "Zoya sent: holding reply" and 20 Oct as "Akshay to ...: Zoya loop-in" (Hrithik, Vishnupriya, Palak). Conflicting authorship |
| 1a14fbc892a03516, 1a1519cb70911a28 | 2 each | Tanuj, company named Apex Market Intelligence first, Wryto second |
| 1a1527ce749067db, 1a152d1642506511, 1a1530fc9d935090, 1a1531a34ec804fd, 1a1533b1b0db3c63, 1a15344433c1202f, 1a15347cffecf261, 1a15424891159f17, 1a15426fca608b54, 1a15458f279fd4a5, 1a1547191cffc08a, 1a154738a99fecb9, 1a15479f0462dbe0 | 2 each | Aanshul (RedSeer), Vineeta, Chaandini (Damsun: Email out first, Email in second), Neeti, Jessica, Hrithik, Vishnupriya, Palak, Ashmita x3, Merlin (Lemma) |

The 15:07 and 21:05 timestamps line up with inbox runs (00:02 and 06:02 JST, about 5 minutes in). The inbox's Source ID check is not catching rows it wrote the day before.

**Same person within 10 minutes (Email out).** None found among sends: no person got two sends within 10 minutes. The 3 Akshay to Lital rows and 3 Akshay to Thomas Johnson rows are separate real mails logged in one batch (Date is date-only, so their true gap can't be checked).

## 3. Overdue on Zoya

Open Engagements, Waiting on contains Zoya, Next date before 21 Oct JST: **26**. None has an Email out Activity since its Next date. Another 5 are due today (21 Oct); 22 sit at 27 Oct. Zoya's own runs give the reason: follow-ups only go 16:00-22:00 JST on weekdays, and the one in-window follow-up run (21:32 JST) sent 1 of ~90.

| Name | Status | Next date | Last Email out |
|---|---|---|---|
| Annanya Sarthak @ Awign | LT chase | 17 Oct | none |
| Nithyambika Gurukumar and Sashi Gundala @ ALIF | LT chase | 19 Oct | none |
| Simha Sadasiva @ Ushur | LT chase | 19 Oct | none |
| Divya Kamerkar @ Pinky Promise | LT chase | 19 Oct | none |
| Renita Rajan @ CHOSEN | LT chase | 19 Oct | none |
| Arvind Narayanan @ Growize Farms | LT chase | 19 Oct | none |
| Pritesh Mohite @ KIT Global | LT chase | 19 Oct | none |
| Durgadutt Nedungadi @ Netradyne | LT chase | 19 Oct | none |
| Emil Eifrem @ Graph database | LT chase | 19 Oct | none |
| Neha Jain @ Zerocircle | LT chase | 19 Oct | none |
| Priya Kumar @ Priya Kumar's Training Systems | LT chase | 19 Oct | none |
| Mukund Jha @ Emergent | LT chase | 19 Oct | none |
| Manoj Meena @ ATOMBERG | LT chase | 19 Oct | none |
| Yosha Gupta @ MeMeraki | LT chase | 19 Oct | none |
| Tanuj Shori @ Square Yards | LT chase | 19 Oct | none |

Not listed (11 more, all 19 to 20 Oct): Govind Sandhu (Customer Capital); 20 Oct: Andrey Fedorov (STON.fi, un#), Mukesh Bansal (CureFit), Pravesh Dudani (NSDC, Next action still the old note "Preliminary call"), Kalyan Sivalenka (Hyderabad Angels, Next action still "Agent: ..."), Vadim Voss, Andrea Muttoni, Corey Petty, Sergii Gerasymovych, Zach Ipour (un# sponsored steps), Ashay Mehta (DALPL). 4 of the LT chase rows say "eval says Decline, check before chasing" and 1 (Mukund Jha) says there is nothing to send yet.

## 4. Waiting on Builder (open, not Done): 17

| Name | Kind | Task state | Next action (150 chars) | Page id | Looks finished? |
|---|---|---|---|---|---|
| Task: verify a WhatsApp instruction runs end to end without the build chat | Task | Awaiting someone else | Builder: on the first real instruction Akshay posts in the Zoya group after the decision 330 deploy, record captured, handed over, action completed an | 3fc19a301a7f8181b57ddf15e17b362d | no, waiting on a real instruction |
| Task: observe the first real outcomes of decision 313 | Task | Awaiting someone else | Builder: after 19 Oct 08:00 JST, find the first un# Your call or Tier decision and the first un#, B2S or HBD recording day-before; record whether each | 3fc19a301a7f81fdaa38edc67bef4bf0 | unknown, not checked |
| Task: pilot canonical run reporting in Inbox and Zoya (AR-20261018-8) | Task | Doing | Builder: AR-8 v3 semantics cleanup-accepted; unchanged text recomposed on Stage B v4 (844fdbd). Final Stage B/Notion approval-hold review remains; dep | 3fd19a301a7f81dfa168d9d08358408e | half: Zoya writes `run:zoya:<session>` records (11 in window), so it is live for Zoya; no run records from the inbox. Row text still says not deployed |
| AR-20261018-2: preserve independent obligations across eval and work writers | Task | Doing | Builder: AR-2 patch prepared (commit 8923fab); cleanup review, then deploy after Stage B and AR-8; cowork-evals and skills need owner-side install | 3fd19a301a7f81588908e583e1dd5ac9 | no evidence either way; row stale since 18 Oct |
| Task: require Show on every Engagement (AD Personal fallback) | Task | Doing | Builder: Show rule in the AR-2 patch (commit 8923fab); deploys with AR-2 | 3fd19a301a7f818f97bdeb30646eb3af | goes with AR-2 |
| CTO-20261018-4: consolidate instructions and remove duplicate processing | Task | Doing | Builder: part 1 prepared (commit 88218ab, directory writer and sweep 3g); part 2 next (sender authority, inbox trim, eval context) | 3fd19a301a7f81159ab6fbd7c10ecae2 | no; inbox duplicates in 2c show the duplicate-processing problem is still live |
| AR-20261018-9: fix Sri-board eval, pitch and availability provenance | Task | Awaiting someone else | Cleanup: review AR-9 v3 delta 130f810 (per-revision host-return marker, traces M1 to M8) plus the final inbox size and composition \| Builder/main: dep | 3fd19a301a7f818e9238f430f593a3e8 | unknown; target deploy was 20 Oct 09:00-12:00 JST |
| AR-20261019-1: ensure follow-up coverage across every show | Task | Doing | Main: claimed feedback/coverage batch; implement Akshay's 20 Oct approved clock exception (ignore administrative loop-ins/incidental Cc, count substan | 3fe19a301a7f81bcaba2de3bad3bfda5 | no; 26 overdue rows (section 3) |
| AR-20261019-2: WhatsApp team coordination and @Zoya handling | Task | Awaiting someone else | Cleanup: review AR-20261019-2 (main, 8398b02): changed permissions, routing, dedupe and return paths in docs/proposals/ar20261019-2-whatsapp.md \| Buil | 3fe19a301a7f8155ac45e560517705a3 | unknown |
| AR-20261019-3: recording-to-Episode recovery and Main 2 scope | Task | Awaiting someone else | Cleanup: verify eccf34f's narrow v3-to-v4 delta and current build; Codex accepts the changed recovery text and revised walkthroughs. Main 1: integrate | 3fe19a301a7f81df86b7f8303fbeddc0 | unknown |
| AR-20261019-4: narrow B2S pause to cold outreach and recover active commitments | Task | Doing | Main: Salesblink implementation superseded by Akshay's tool retirement (AR-20261019-6). Stop sync patches; preserve/reconcile outstanding active repli | 3fe19a301a7f81309435c88ed3441a9e | superseded; only the reconcile of active replies remains |
| AR-20261019-5: capture production and episode-marketing attachments in Notion | Task | Awaiting someone else | Cleanup: verify 8148594 rev5's single-paragraph link-key delta, same-key/same-day-new-key and uncertain-write replays plus final package composition;  | 3fe19a301a7f81319d45e329d23f453f | unknown |
| Misc: B2S list re-eval (tags, blurbs, B2S target shortlist) | Task | Awaiting someone else | Misc: prepare local Sonnet API-credit enrichment pilot on existing ten-person sources, $5 initial cap; script/public packet, offline checks, exact Mac | 3fe19a301a7f81cda29cfdece4b65a76 | no |
| Misc: extend the cold-outreach pause to Human by Design (Salesblink sync) | Task | On hold | Superseded by AR-20261019-6: Main retires Salesblink rather than extending its sync. Preserve actual HBD cold holds and active replies/Arjun's obligat | 3fe19a301a7f8185b20bc9fbb96e1dc7 | yes, superseded; can close |
| AR-20261019-6: retire Salesblink, Blue and FT Newsjack; hourly response loop on Sonnet | Task | Doing (Builder, Akshay) | Main: 7b48ce5 addresses the three design points; correct the dated nurture-start counter phrase and align stale operational deploy tables with revisio | 3fe19a301a7f8197b071fe31d3aeb2c6 | looks deployed: all 7 triggers are on claude-sonnet-5-5, five on hourly crons, every session served Sonnet. Row still says "not installed" (19 Oct 22:55) |
| FT blurb workflow: guest editing chats, retire WhatsApp loop and coordinate WA-Blurb rename | Task | Handed over | Main: new owner-approved scope captured 20 Oct 08:06 JST, receipt not yet verified. Stop automatic blurb posts/WhatsApp rewrites; prove one source-loa | 3fe19a301a7f8131afaac655d2eeb2d9 | mostly: the live WhatsApp prompt has 0b retired (decision 347), and 8 "Blurb chat: <guest>" sessions exist (7 created 20 Oct 13:22 UTC) |
| Task: after every precall, Zoya checks in with Akshay on what he promised (decision 360) | Task | (empty) | Builder (Main): build in Friday's package. After a precall, the calendar run reads the call notes for Akshay's offers and promises and creates one Kin | 3ff19a301a7f81719cc7dfed5358c0f9 | no, Friday package; Task state empty |

None of the rows mentions "AR-8 Zoya pilot deployed" in its text; the AR-8 and AR-20261019-6 rows look finished only from installed-config and run evidence, not from their own notes.

## 5. Matthew @ Magic Bus (3f019a301a7f81bd9ed6c7020bf96f3d)

| Field | Value |
|---|---|
| Status | Booked |
| Waiting on | Akshay |
| Next date | 20 Oct 05:30 UTC (14:30 JST) |
| Next action | "Akshay: send Matthew the thank-you note. The calendar run drafts it in your Gmail about 6 hours after the recording; attach the transcript and send (decision 300). \| Scheduled as on Oct 20th. Dossier is ready and guest prep note sent" |
| Last Claude note line | "2026-10-20: research: Tier 1.5, ask_akshay, The row is Booked with the thank-you note as Akshay's action, but there is no guest audio in Drive, so only Akshay can confirm whether the 20 Oct recording happened. I did not read the threads. (pipeline review)" |
| Last activity | 19 Oct, Zoya to Matthew: recording link and prep note for the 20 Oct recording |
| Thank-you Activity | **none** (no Email out, no Draft) |
| Activities since 18 Oct | 19 Oct "Zoya sent: Recording tomorrow"; 19 Oct recording link and prep note; 20 Oct 07:15 UTC Meeting "Gemini notes: 20 Oct meeting with Matthew Spacie, audio and connectivity trouble, moved to the recording link" |

Still Booked, not Recorded, about 17 hours after the slot. No thank-you draft has been logged, though Next action says the calendar run drafts one about 6 hours after the recording.
