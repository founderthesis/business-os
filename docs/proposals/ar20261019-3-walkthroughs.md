# AR-20261019-3: recording-to-Episode recovery (Main 2)

Owner: Main 2 (the Mac-routines chat). Branch claude/ar-20261019-3-episode-recovery, cut from main 01d0f9d. For cleanup review; Main 1 integrates and deploys. Nothing here was deployed, scheduled, mailed or put on a calendar.

## 1. Source versions (read 19 Oct, 06:00 to 06:30 UTC)

- Live "Calendar sync" (trig_01Voiz5YsK2SnVf2STF8PoSH): updated 18 Oct 07:57 UTC; prompt 49,476 bytes, sha256 3d9f8bd7bd5b, **identical** to the text block of routines/calendar.md at main 01d0f9d (blob 43252ccd0e58). STEP 4 a2 is live since 18 Oct 16:57 JST. Last run 18 Oct 23:36 UTC, succeeded, 38 s.
- Patch: docs/proposals/ar20261019-3-episode-recovery.patch, against blob 43252ccd0e58. Result blob cb13ab41ac6c; prompt block 53,029 bytes, under the 65,536-byte cap. Changed paths: routines/calendar.md only (STEP 4 parent line, STEP 4 a, a2, new STEP 4e, one sentence in 4c). No pending patch touches these lines: ar2 and p333 calendar hunks sit at lines 16 to 75.
- Mac package: main's routines/mac/transcripts.md (59154d7, FILE/COPY/THANKS with the work record on the backlog Task row). Not changed here. The older 785b296 prompt is not restored.

## 2. Reconciliation, 12 to 18 Oct (all shows)

Sources: the ad@thepodium.in work calendar (read directly; Akshay's myunnati calendar holds no events that week), Notion Engagements and Episodes, Drive "Zencastr" audio folders, Gmail.

| Recording (calendar) | Show | Independent evidence it happened | Episode | Transcript on Episode |
|---|---|---|---|---|
| Amit Das @ Think360.ai, 13 Oct 15:00 JST | FT | Zencastr folder ft-podcast-recording-amit-das-think360ai (13 Oct); thank-you sent 14 Oct | 3fc19a301a7f8193b976 (13 Oct), linked both ways | empty |
| Vicky Dodani @ Agrizy, 14 Oct 13:30 JST | FT | Zencastr folder (14 Oct 04:37 UTC); guest form in 15 Oct | 3fc19a301a7f81cfa0ae (14 Oct), linked | empty |
| Amit Patni @ Raay Neo Pharma, 14 Oct 19:30 JST | FT | Zencastr folder (14 Oct 10:32 UTC); thank-you with transcript sent 15 Oct | 3fc19a301a7f81b68bf5 (14 Oct), linked | empty |
| Sankalp Arora @ Gather AI, 15 Oct 19:00 JST | FT | Zencastr folder (15 Oct 11:07 UTC); thank-you 16 Oct | 3fc19a301a7f812e8eee (15 Oct), linked | filled |
| Prashant Sachan @ AppsForBharat, 16 Oct 18:30 JST | B2S | Riverside; Satish's 16 Oct mail; B2S thank-you 17 Oct (1a149f36e53a11c9) | 3fc19a301a7f81b98f37 (16 Oct, Built to Share), linked | empty |

- Five recordings, five correct Episodes, no duplicates. Prashant's earlier Founder Thesis Episode (3ed19a301a7f81848e98, Published) is separate and stays separate; both carry the same People row.
- No un#, Human by Design or co-guest recording that week on the work calendar or in Notion (no un#/HBD Engagement at Booked or Recorded with a date in the window).
- **Not identified:** two Zencastr files in Drive "Zencastr/_external_": a final mix stamped 12 Oct 06:08 UTC (15:08 JST, 118 MB mp3) and one stamped 15 Oct 10:07 UTC (106 MB). No ad@ calendar event, Engagement or mail matches 12 Oct 15:08 JST. The 15 Oct one may belong to Sankalp's session but its time doesn't fit. A file alone is not proof of a guest recording, so **no Episode was created**. To settle: Akshay names them, or the Mac task opens Zencastr's _external_ recordings.
- **Data repairs: none.** No confirmed recording is missing an Episode.

Why the automatic path never fired for these five: they went Recorded through the inbox or by hand (thank-you sent, Satish's mail), or straight to Form filled. Call type stayed "Recording" on all five (only STEP 4 a clears it). The live STEP 4 takes only Status Booked rows, ending within 3 days, so a2 could never reach them. a2 also wasn't live until 18 Oct 16:57 JST, after all five windows had closed. The five Episodes are the 17 Oct manual backfill (Migration batch transcript-audit-2026-10-17): they prove the data, not the automation.

## 3. The correction (patch summary)

1. **STEP 4 retry window**: Booked rows are rechecked for 30 days, not 3. A "recorded <date>? no Zencastr audio" line no longer blocks retries (it matched the old skip by substring, so late Drive audio was never picked up). The line is written once. After 3 days only the Founder Thesis Drive-audio check runs; client shows are never set Recorded from the calendar alone after 3 days.
2. **a2 identity and matching**: an Episode's Source ID holds "cal:<calendar event id>". Lookup order: that key across all Episodes, then one candidate on the same Show (guest in Guests, or this Engagement in Engagements) with Recording date within 14 days, or an empty date and Status not Published or Not releasing. Two or more candidates: create nothing, note "ambiguous". Found: add missing links both ways, fill only empty fields, never touch another Show's Episode or a Published one. Create: with the key, then re-read both sides and write any missing link.
3. **STEP 4e, Episode recovery**: every run, the work-calendar recordings that ended 2 hours to 30 days ago, not cancelled. The Engagement is matched by the Prep entry's bos-key, else the STEP 1 match. It goes on to a2 only if the recording happened (Status Recorded or Form filled, or "recorded <date> ("), skipping cancelled, moved and no-show rows and Booked ones (STEP 4's). Already done means no write. At most 5 creates a run, oldest first. Unfinished work (over the cap, a failed write, an ambiguous match) gets one "Episode pending ... (cal:<event id>)" Claude note line, and stays eligible past the 30 days until a later "created" or "linked" line closes it.
4. 4c no longer calls a2 itself; it points to 4e.

Not changed: guest routing, Status, Waiting on, Next action, bookings, commercial terms, thank-yous, blurbs, transcript fields.

## 4. Replay tests (traced against the patched text)

| # | Case | Expected |
|---|---|---|
| 1 | Marked Recorded by the inbox or Akshay before the calendar run (all five above) | STEP 4 skips (not Booked). 4e: event in window, Status Recorded, so a2; key or candidate found, links already there, so it stamps Source ID and writes no note. If missing: one create, note "Episode created". |
| 2 | Call type cleared by STEP 4 a | 4e doesn't read Call type. Same as 1. |
| 3 | Call type still "Recording" on a Recorded row (Amit Das, Raunak) | STEP 4 needs Booked, so skip; 4e as 1. No double handling. |
| 4 | Existing "recorded <date> (" note | STEP 4 skips (success line). 4e treats it as proof it happened. |
| 5 | "recorded <date>? no Zencastr audio" note, audio lands 2 days later | STEP 4 retries (the "?" line no longer skips), finds the audio, sets Recorded, runs a2. The "?" line is not rewritten. |
| 6 | Calendar run down for 5 days | STEP 4 still sees the Booked row (30-day window) for FT; 4e sees any Recorded row up to 30 days. Client show Booked over 3 days: not auto-Recorded; Akshay or the inbox sets it, then 4e. |
| 7 | Transcript missing | Never read by STEP 4, a2 or 4e; the Episode exists, and FILE stays open in the Mac work record. |
| 8 | Thank-you and blurb already done | 4e doesn't depend on 4b or 4c; same as 1. |
| 9 | Existing Episode not linked to the Engagement (e.g. made by hand) | Candidate by guest, Show and date, then link both ways, note "linked". |
| 10 | Returning guest across two shows (Prashant: FT Published + B2S 16 Oct) | B2S event: candidates are same-Show only, so the FT Episode is never matched; the B2S one is found by date. |
| 11 | Returning guest, same show, new date | Old Episode's date is over 14 days away (or it is Published), so not a candidate; a new Episode with " - <D Mon YYYY>" in the title. |
| 12 | Co-guests (one event, two guests) | One event key, one Episode; Guests = everyone on the Engagement who recorded; a missing guest is added, never removed. |
| 13 | Interrupted after create, before linking | Next run: key "cal:<event id>" found across all Episodes, link written, no second Episode. |
| 14 | Second run with nothing new | Key found and linked both ways: no write at all. |
| 15 | Cancelled event, or no-show | Cancelled event: never considered. No-show: Status not Recorded or Form filled, or a note says no-show or didn't happen: skip. |
| 16 | Event moved, held on another date | A later "recorded <other date> (" line: this event is skipped; the event that matches the held date is the one that counts. |
| 17 | Legacy Episode with a different date (Raghu Pareddy: event 22 Sep, Episode 1 Oct) | One candidate within 14 days: link, stamp key, leave the date, report the mismatch. No duplicate. |
| 18 | Legacy Episode with an empty date, not Recorded (Raagulan, un#, Editing) | Empty date and not Published: a candidate. Date filled with 25 Sep. The old rule (Recorded or Scheduled only) would have created a duplicate. |
| 19 | Two candidates | Nothing created; "ambiguous" and "Episode pending" notes, report line every run until linked by hand. |
| 20 | Over the 5-a-run cap, or a write fails, then the outage passes 30 days | "Episode pending (cal:<id>)" line keeps it eligible; the event is read by id after it leaves the window; closed by the later "created" or "linked" line. |

**Real-data dry run of 4e on the first live run** (work-calendar recordings 19 Sep to 18 Oct, 19 events; every Engagement is Recorded or Form filled and already linked): expected 0 creates, 0 Claude note lines, 19 silent Source ID stamps, Recording date filled on 3 (Raagulan 25 Sep, Nand Kishore Chaudhary 1 Oct, Saravana Maruthamuthu 7 Oct), and 1 date-mismatch report line (Raghu Pareddy). If the first run creates any Episode for these 19, the matching is wrong: stop and review.

## 5. Transcripts (reuse, no new tracker)

Four of the five Episodes still have no Transcript file: Amit Das, Amit Patni, Vicky Dodani, Prashant Sachan (B2S). They are already within the Mac transcripts task (main's routines/mac/transcripts.md, FILE and COPY; its 30-day look-back covers 13 to 16 Oct). THANKS doesn't apply: all four thank-yous were sent. The backlog Task row 3fc19a301a7f81e8b013e8fb2206e787 is the work record. Current state, read 19 Oct: Handed over, Waiting on Zoya, Next action still "mail Akshay the mac-transcripts-v2 prompt" (stale against main's install doc), no "## Open Mac jobs" section yet. So the Mac task isn't confirmed installed, and no progress is claimed. The draft-attach probe gate is unchanged.

Proposed delta for Main 1, not written by Main 2: when the install doc is the current ask, the backlog Task row's Next action should point to docs/install-2026-10-19.md instead of the v2 prompt.

## 6. Acceptance still open after deploy

Automatic creation is proven only by a real future recording getting its Episode from 4e or a2 with Source ID "cal:<event id>" and Captured on that day. The next booked ones are Matthew Spacie (20 Oct), Rohan Ganapathy (22 Oct) and Sreepriya NS (23 Oct). Historical backfills don't pass this test.
