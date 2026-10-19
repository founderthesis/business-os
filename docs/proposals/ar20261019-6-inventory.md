# AR-20261019-6: before/after inventory and deletion checklist (19 Oct 2026)

Owner decision (Akshay, 19 Oct): retire Salesblink and Blue, kill FT Newsjack, run the response pipeline hourly, and run every recurring routine on Sonnet. Main owns deployment; cleanup reviews changed controls.

The states are kept apart:
- **Disabled/deleted:** done in the scheduler, read back.
- **Pinned:** a model setting changed, read back.
- **Prepared:** built, waiting on cleanup, not installed.
- **Installed:** pushed and read back.
- **Observed:** seen working in a real run.

## 1. Cloud scheduled tasks (claude.ai)

Read from the scheduler on 19 Oct, 12:05 to 12:16 UTC. The 19 one-shot reminders (all fired, all disabled) are left alone.

| Task | Id | Before | After now | After cleanup accepts (prepared) | Model, read back | Connectors |
|---|---|---|---|---|---|---|
| Salesblink sync | trig_01KpyDSfNqRKAGEABwyMBREA | weekdays 09:10, 15:10 IST | **disabled 12:09 UTC, then deleted** | gone | sonnet-5-5 (moot) | Salesblink, Notion (gone with it) |
| FT Newsjack, daily archive scan | trig_01WtqCKNrmaCGieif519N1WB | daily 02:30 UTC | **paused by Akshay** (his screenshot, Codex 21:51 JST: all triggers paused). Created by API, so agents can't change it | deleting it is optional housekeeping | claude-sonnet-5 | Canva, Slack, Unsplash, Drive, Remote, Calendar, Gmail, Notion |
| Inbox to Business OS | trig_0189eZvAD8x4357cfevgZ3No | 00, 08, 16, 21 JST | unchanged | **hourly at :02 JST**; prompt 64,848 to 64,995 B (541 spare) | sonnet-5-5 (already set) | Notion, Gmail, Calendar, Blueticks, MCP Emails |
| Host boards | trig_01K8bueCr2xsPkbgQzjeRKsz | 00:15, 08:15, 16:15, 21:15 JST | **pinned sonnet-5-5** (was empty) | **hourly at :15**; prompt unchanged | sonnet-5-5 | Notion |
| Founder Thesis guest evals | trig_01R1yHgEztVEo832zMwUugBr | 00:25, 08:25, 16:25, 21:25 JST | unchanged | **hourly at :25**; prompt unchanged | sonnet-5-5 (already set) | 17 account connectors incl. **Salesblink, Blue**: remove (UI step 2) |
| Zoya | trig_01UPT8LDrBDL5JQqW91Awgbo | 00:30, 08:30, 16:30, 21:30 JST | **pinned sonnet-5-5** (was empty); prompt unchanged 7f71e2302f155d6f | **hourly at :30**; prompt 43,704 to 44,601 B (rev 3) | sonnet-5-5 | MCP Emails, Notion, Gmail, Calendar, Blueticks |
| Calendar sync | trig_01Voiz5YsK2SnVf2STF8PoSH | 08:35, 16:35, 22:35 JST | unchanged | **hourly at :35**; audit once per window with a completion Activity; prompt 49,476 to 50,214 B (rev 2), before AR-3 | sonnet-5-5 (already set) | Gmail, Calendar, Notion, MCP Emails, Drive |
| WhatsApp to Business OS | trig_01MnmJYorWrd61K7b5BCqXr1 | hourly at :45 JST | **pinned sonnet-5-5** (was empty) | hourly at :45 (same); prompt 22,647 to 22,592 B | sonnet-5-5 | Blueticks, Notion |
| Daily sweep | trig_01MdfUFg2qrebDWgiHwncgnd | weekdays 13:10 JST | unchanged | **stays daily**; prompt 35,063 to 35,050 B | sonnet-5-5 (already set) | Gmail, Notion |
| Host dossiers and prep notes | trig_01WfLf8Zx9c34fSzfrTeUY5M | daily 06:50 JST | unchanged | **stays daily**; no change | sonnet-5-5 (already set) | 17 incl. **Salesblink, Blue**: remove (UI step 2) |
| FT Community directory sync | trig_01EoP9zjHnaAeyKthSWdcums | Saturdays 09:47 JST | **pinned sonnet-5-5** (was empty) | **stays weekly** | sonnet-5-5 | Blueticks, Notion, Apollo |

**Why these offsets.** The order is inbox, then boards, evals, Zoya, calendar and WhatsApp, as before, each about a quarter-hour apart.
- Last observed run lengths were 1.5 to 6.5 minutes, so a routine can't overlap its own next run.
- Inbox sits at :02 rather than :00, because the scheduler re-anchors minute-0 hourly crons to the edit minute.

**Opus fallback.** No task has Opus or Auto anywhere: every model field reads sonnet-5-5, except Newsjack (claude-sonnet-5), which is paused. The scheduler API has no fallback switch to set. The real check is each run's served model, `last_served_model`, on the first hourly runs. I'll report any fallback seen there.

**Interactive sessions** (main, cleanup, misc) are authoring tools, not recurring workers, and are not pinned by this. Codex's CTO review is not a Claude worker: unchanged.

## 2. Mac tasks (Claude desktop, local)

The cloud can't read or edit these. Akshay does UI step 3, and the cloud reads back the outcomes.

| Task | Before | After |
|---|---|---|
| Blue transcripts backfill (one-time, after maintenance) | paused | **delete** |
| Zencastr links for confirmed FT recordings (nightly) | paused, cutover per docs/install-2026-10-19.md | keep its reviewed cadence; set model **Sonnet 5.5** |
| Zencastr transcripts to Notion after FT recordings (nightly) | paused, same | keep its reviewed cadence; set model **Sonnet 5.5** |

## 3. Salesblink, before it goes (read-only, then made safe)

- **22 sequences.** Two were still running, both sending from Mamatha's mailbox:
  - "Human By Design Podcast Invite": 358 leads, 66 in progress, 28 not started, 1,269 sent.
  - "Test - Founder Thesis Podcast Invite".
  - **Both paused at 12:20 UTC.** A recheck shows 0 running. Nothing was restarted or sent.
- **30 reply threads, all read.**
  - **Already settled in the OS or closed:** Euan, Barto, Bengio, Shoham/Noa, Koller, Farhadi, Hinton, Kaelbling, Simon Jagers (recorded), Maxim Galash, and the unsubscribes. Six are internal tests.
  - **Never answered inside Salesblink and never in the OS: 8**, from January to July 2026. They went to Akshay as two Task rows (a decision, not a bulk create), with their Salesblink message ids as evidence:
    - Human by Design, 7: [Task](https://app.notion.com/p/3fe19a301a7f8158899cee76e0167331).
    - un#, 1: [Task](https://app.notion.com/p/3fe19a301a7f81508c2cd55163459e3b).
  - **The named blocker:** these threads sit in Mamatha's and Chaandini's mailboxes, which no OS routine reads. A revive means Zoya writes a new mail, or Mamatha replies.
- **Notion rows that mention Salesblink:**
  - 132 B2S "Queued in Salesblink", 119 B2S and 134 HBD cold holds, 11 decision 328 holds, plus a handful of one-offs.
  - All have no owner and no date except one HBD row waiting on Arjun, so none is due or mailable.
  - Left as written: that's history, not a live integration. No bulk relabel.

## 4. Source and controls

**Prepared, not installed** (`ar20261019-6-build.py`, `ar20261019-6-prompts.patch`):
- **Inbox:** an HOURLY line (new or unfinished work only; look-back windows are catch-up; more runs never mean more mails). "(Salesblink)" is dropped from cold outreach.
- **Zoya:**
  - The HOURLY line.
  - Cold outreach is "(C1 and C2; Salesblink is retired)".
  - ONE PERSON, ONE ASK no longer holds a mail for "Waiting on Chaandini" or an active Salesblink sequence. Only a real Salesblink mail on their rows in the last 14 days still holds it, which runs out by 2 Nov 2026.
  - Nurture and revival mails, and nurture moves, are capped at 20 a day (JST) instead of 10 a run, so hourly can't multiply them and the old two-run maximum of 20 is kept (sections 7 and 8).
- **Calendar:** the HOURLY line and the "(Salesblink)" drop. The 30-day audit runs once in each window (08 to 16, 16 to 22, 22 to 08 JST), guarded by a completion Activity (section 7), so its mails don't multiply.
- **WhatsApp:** inbox timing reads "hourly, a few minutes past each hour"; "still open" means two hours after it went into Your call.
- **Sweep:** the "(Salesblink)" drop.
- **Unchanged and still safe hourly:**
  - The daily guards: owner mail once a day, briefs, FT Community once a day.
  - Follow-ups only in the 16:00 to 22:00 JST runs, the 150-a-day send cap, and the 7-day per-person rule.
  - The one-time loop-ins, already run.

**Done in the repo now:**
- `routines/salesblink-sync.md` and `routines/mac/transcripts-blue-youtube.md` removed (git history keeps both).
- The Mac README, install doc, CLAUDE.md and architecture source line updated.
- Decision 344.
- The owner UI steps added to the pending list.

**Notion (developer page):** the Salesblink sync routine page is marked retired, with a Change log line.

**Not changed:**
- Historical Source IDs, Activities, People, Episodes and transcripts.
- The bts-guest-eval skill's "never Salesblink" guard, which is harmless.
- The Salesblink and Blue accounts and billing.

## 5. Deletion checklist

| # | Item | Who | State |
|---|---|---|---|
| D1 | Salesblink sync schedule | main | disabled, then deleted (19 Oct 12:09 to 12:25 UTC) |
| D2 | Two running Salesblink sequences | main | paused, rechecked 0 running |
| D3 | FT Newsjack schedule | Akshay | **paused** (owner screenshot, 19 Oct 21:51 JST); delete optional |
| D4 | Salesblink and Blue on evals and dossiers | Akshay, UI step 2 | open |
| D5 | Mac Blue backfill task | Akshay, UI step 3 | open |
| D6 | Mac Zencastr tasks on Sonnet | Akshay, UI step 3 | open |
| D7 | Repo routine files for Salesblink and Blue | main | removed in this commit |
| D8 | Hourly crons plus prompt edits on 5 routines, and Rules R1 | main, after cleanup | prepared (rev 3) |
| D9 | Account-level Salesblink and Blue connectors | Akshay, optional | open |

## 6. Deploy (after cleanup accepts; current as of rev 3)

1. **Fresh base check.** Each live prompt must still be byte-equal to its base:

   | Routine | Base sha256 (first 16) |
   |---|---|
   | Inbox | 07fbac63b5ca3509 |
   | Zoya | 7f71e2302f155d6f |
   | Calendar | 3d9f8bd7bd5bcef9 |
   | Sweep | f0bf956ef3253898 |
   | WhatsApp | d4c9986b750e9cbd |

   Rebuild if any moved.
2. **Push prompt and cron together**, one routine at a time in this order: WhatsApp, calendar, Zoya, host boards (cron only), evals (cron only), inbox. Read back the sha and the cron after each.

   | Routine | Cron | Expected sha after |
   |---|---|---|
   | WhatsApp | `45 * * * *` (unchanged) | a501ba2a88a4080d |
   | Calendar | `35 * * * *` | 800801f0906446cd alone; with AR-3 the composed hash is measured at deploy |
   | Zoya | `30 * * * *` | d528541c31a5f390, then Rules R1 the same hour |
   | Host boards | `15 * * * *` | prompt unchanged |
   | Evals | `25 * * * *` | prompt unchanged |
   | Inbox | `2 * * * *` | c05203e2ccb0faba |

   All crons are CRON_TZ=Asia/Tokyo. The sweep prompt goes with no cron change (651198505a972a60).
3. **Observe the first three hourly passes:**
   - no duplicate Activities, replies or loop-ins;
   - Zoya sends no more than before;
   - one owner mail and one of each brief per day;
   - served model sonnet on every run.

## 7. Revision 2 (19 Oct, 22:20 JST): Codex's three cutover corrections

Prepared, not installed. Build and patch regenerated on the same live bases (`ar20261019-6-build.py`, `ar20261019-6-prompts.patch`). Changed vs eb6a9ec: calendar and Zoya only.

| Routine | After (rev 2) |
|---|---|
| Calendar | 50,214 B / 800801f0906446cd |
| Zoya | 44,517 B / 4c83e50a013430ce (superseded by rev 3: 44,601 B / d528541c31a5f390, section 8) |
| Inbox, WhatsApp, Sweep | unchanged from section 4 |

**1. Calendar audit, once per window, with a completion record.**
- Windows: 08:00 to 16:00, 16:00 to 22:00 and 22:00 to 08:00 JST. Each is keyed by the date it starts.
- A run skips the audit when its window already has the Activity "Calendar audit done: <YYYY-MM-DD> <08|16|22> JST" (Kind Note, Source Calendar).
- That Activity is written only after the whole audit has finished and every finding is written.
- Everything else in the calendar run stays hourly.

| Case | Result |
|---|---|
| Consecutive hourly runs | 08:35 audits and writes "done 08"; 09:35 to 15:35 skip it |
| Missed first slot | The 08:35 run fails; 09:35 finds no "done 08" and audits. Exactly one catch-up, the current window only |
| Crash part way | No completion Activity, so the next run audits again. Findings already written are Claude note lines that the audit skips when already present |
| Midnight | A run at 01:35 on 21 Oct belongs to window "20 Oct 22", so it skips if 22:35 on 20 Oct completed |
| Outage across a whole window | Only the current window is audited when runs resume. Missed windows are not replayed |

**2. Nurture capacity kept at today's maximum.**
- Today Zoya does follow-ups in two runs a day (16:30 and 21:30 JST, weekdays) at 10 a run, which is 20 a day. The new cap is 20 a day (JST), not 10.
- **Nurture and revival mails** are counted from today's "Zoya sent: nurture" Activities, one per sent message.
- **Moves** are counted from today's Zoya move entries, so the sweep's own nurture starts never use her budget. (The revision 2 wording missed the date prefix; section 8 corrects it.)
- It's a ceiling, not a target. The 150-a-day cap, the 7-day per-person rule, due dates and the 16:00 to 22:00 JST follow-up hours still apply.

| Case | Result |
|---|---|
| Two runs share the remainder | 16:30 sends 12; 17:30 sees 12 and may send up to 8 |
| Retry after a real send | The mail is found in Sent first and logged once, so it counts once and isn't resent |
| No-op run | Sends nothing, uses nothing |
| Next JST day | The count starts again from 0 at 00:00 JST |

**3. Decision number.** Misc's 341 to 343 stand. The retirement record is **344**, in every active reference: decisions.md, CLAUDE.md, notion.md, the Change log and the AR-6 page.

**Matching Rules for Zoya edit (R1).** Applied in the same cutover as the Zoya prompt, then read back:
- Section 5a, before: `**Caps.** At most 10 nurture and revival mails a Zoya run, inside the 150-a-day cap and the one-mail-per-person-per-7-days rule.`
- After: `**Caps.** At most 20 nurture and revival mails a day (JST), inside the 150-a-day cap and the one-mail-per-person-per-7-days rule.`

**Owner UI.** Akshay's screenshot shows FT Newsjack paused, with all triggers paused (Codex, 21:51 JST). Its future runs are stopped. Deleting it is housekeeping, not a blocker.

**Composition note (Codex, 21:51).** AR-3 (calendar) and the WA-Blurb rename also change these files. Main 1 composes each routine against everything actually integrated at deploy time and re-measures, never against an isolated hash.

## 8. Revision 3 (19 Oct, 23:20 JST): dated move counter (Codex, 22:07)

Prepared, not installed. Zoya only: **44,601 B / d528541c31a5f390** on the same live base 7f71e2302f155d6f. The other four routines are unchanged from revision 2.

**The defect.** Revision 2 counted note lines that *start* "nurture started", but Zoya writes them as "YYYY-MM-DD: nurture started (<why>)", so nothing matched.

**The change, two strings:**
- The cap now counts Claude note entries dated today whose text *after* the "YYYY-MM-DD: " date starts "nurture started" and ends "(Zoya)", once per move.
- Zoya's move writer becomes "YYYY-MM-DD: nurture started (<why>) (Zoya)". The date and the "nurture started" start are unchanged, so every reader of the start date still finds it.

| Case | Note entry | Counted? |
|---|---|---|
| Zoya's move today | `2026-10-20: nurture started (3 chases unanswered, 6, 9, 13 Oct) (Zoya)` | yes, once |
| Sweep's move today | `2026-10-20: nurture started (3 chases unanswered, 6, 9, 13 Oct)` | no, no "(Zoya)" |
| Sweep's revival | `2026-10-20: nurture started (revival, cleanup check 2026-10-18)` | no |
| Zoya's move yesterday | `2026-10-19: nurture started (...) (Zoya)` | no, not today |
| Row moved before rev 3 | `2026-10-18: nurture started (...)` | no (old date); its start date still reads |
| Retry after the note was written | the entry is already there, so no second entry and no second count | once |
| 20 counted by 18:30 | later runs that day make no moves; the next JST day starts from 0 | capped |

## 9. Deploy checklist (current)

Section 6 holds the full list. This is its current state:

1. Fresh base checks: the live prompt shas must equal the bases in section 6.
2. Calendar is composed with AR-3 once cleanup accepts AR-3, re-measured, and sent to cleanup with the composed size before it's pushed. If AR-3 isn't accepted, calendar ships on revision 2 alone (50,214 B / 800801f0906446cd) and AR-3 lands on top later.
3. Push one routine at a time (prompt, cron, model) and read each back. Zoya goes with Rules R1.
4. Watch the first hourly passes. Check the served model, that nothing duplicates, and that sends don't go up.
