# AR-20261018-9: host-board repair (prepared 19 Oct, for cleanup)

This is the minimum field and writer repair, as a separate patch: `ar20261018-9-build.py`, `ar20261018-9-on-release.patch`.

What it does:
- Short pitch and Guest availability live on Engagements.
- The boards show a complete, current eval.
- Host input comes back into its own Engagement fields.

What stays as it is:
- Host inputs and calls, approvals, booking state, Next date, holds and every other ask on a row.
- The un# rule from 19 Oct 08:00 JST: Sri's call is advisory and Akshay decides.

It isn't deferred behind simplification. It does wait for one thing: the inbox headroom trim in dfd44ca.

## State

| | |
|---|---|
| Prepared | yes, this commit |
| Reviewed | no |
| Deployed | no: no property, prompt, board or row changed |
| Observed | no |

**ETA:**
- Reviewable patch: 19 Oct, 17:30 JST (this commit).
- Deployment: target 20 Oct, 09:00 to 12:00 JST.

**Actual blocker:** the inbox line (158 bytes) can go live only after the dfd44ca trim is live. Today the inbox has 172 bytes spare; with this line it would have 14. Cleanup's acceptance of dfd44ca and of this patch sets the date.

## Live base, read back 19 Oct

- **Host boards** (trig_01K8bueCr2xsPkbgQzjeRKsz, updated 17 Oct 16:51 UTC): 8,474 B, 5819ccf7528ca16f. Byte-equal to repo HEAD.
- **WhatsApp:** 22,647 B, byte-equal to the repo with its ids filled in.
- **Inbox:** 65,364 B, c9a74aee2245a0b7. Byte-equal.

## Writers per field, before and after

| Field | Today | After |
|---|---|---|
| Engagement Scheduling | inbox STEP 3, WhatsApp STEP 2b, the team, **and host boards STEP 1 (host text)** | inbox, WhatsApp, the team. Host boards stops writing it. It stays dated history. |
| Engagement Short pitch (new) | none | host boards STEP 0, from the eval's own "Short pitch:" line; a person's edit wins |
| Engagement Guest availability (new) | none | inbox STEP 3 and WhatsApp STEP 2b reset it to the guest side's current items; the team can edit it |
| Engagement Host approval | host boards STEP 1 (the host's call) | unchanged; the description says what it is |
| Engagement Host notes, Host availability (new) | none (host text went into Scheduling and Next action) | host boards STEP 1, copied from the board only |
| Board Short pitch, Guest availability, eval body, Eval, Eval link | host boards STEPS 2 and 3, from eval sections and the newest two Scheduling lines | host boards only, projecting the Engagement fields and the EVAL SNAPSHOT |
| Board host fields (call, notes, availability) | the host | the host |

There's one writer per mirrored field. No Notion agent, rollup or second updater is added. The native-agent pilot prompt on the task stays an AUDIT-only option for later and isn't part of this cutover.

## The change

### Engagements schema

Add four text properties. Main adds them at deploy, after review.

| Property | Type | Description (as it will read) | Layout |
|---|---|---|---|
| Short pitch | text | One or two sentences for hosts and the team, from the guest's newest eval. Optional. Edit it freely: the host-boards routine never overwrites a person's text. | Decide section, after Eval date, hide if empty |
| Guest availability | text | What the guest side offers now, one line each: Offer, Preference, Request (they want our times) or To confirm, as written with time zone and source date. Never host slots. Scheduling keeps the history. | Next step section, before Scheduling, hide if empty |
| Host notes | text | The host's latest notes on their board, with the date copied. Written only by the host-boards routine. | Decide section, after Host approval, hide if empty |
| Host availability | text | The host's latest availability on their board, with the date copied. Written only by the host-boards routine. Never guest offers. | Decide section, after Host notes, hide if empty |

Existing descriptions:
- **Host approval:** add "The host's call from their board. On un# from 19 Oct 2026 Sri's call is advice; Akshay decides."
- **Scheduling:** replace "The daily sweep copies it to the host board" with "Dated history only; the host board shows Guest availability."

No rename and no migration of Host approval. It already is the host's call as pulled; the un# rule keeps it from being treated as the internal approval.

Views: add Short pitch, Guest availability, Host approval, Host notes and Host availability, in that order, after Next action, to each un#, Built to Share and Human by Design working view the team uses. One table per view, no grouping.

### Host boards (`routines/host-boards.md`)

- **New STEP 0.** It keeps Short pitch on every open host-show Engagement with an eval, on a board or not.
  - It writes only an empty field, or one still equal to its own last "short pitch from eval <date>" line.
  - If the newest eval has no pitch, it uses the latest one that has, and says so.
  - It never composes a pitch.
- **EVAL SNAPSHOT,** defined once:
  - the newest-dated eval section, chosen by date, plus the sections above it that belong to it ("Numbers", "added to the eval") and are dated on or after it;
  - internal sections stripped;
  - two sections with the same newest date: the "## Eval (" format wins over an older-format copy; still tied, the page is left unchanged and reported.
- **FIELD OWNERS** line under ROW RULES.
- **STEP 1, HOST INPUT RETURN** replaces "copy into Next action and Scheduling".
  - It compares the board's notes and availability with Host notes and Host availability every run, whether or not the call changed. It writes only what differs and clears what the host cleared.
  - It adds one next step per change, after the other asks:
    - host availability on a decided guest: "<team member>: offer <Host>'s slots to <guest side>";
    - a note that asks or answers something: the owner (Akshay for a decision).
  - It removes the host's own ask once the board answers it.
  - On un#, before Akshay decides, host availability is recorded only.
- **STEP 2:** a new row at Approval pending puts the question to the host ("<Host>: your call on <guest> on your board") unless it's already asked.
- **STEP 3 projection:**
  - Short pitch is the Engagement's. An empty one leaves the board's until a canonical one exists.
  - The board page body is the EVAL SNAPSHOT, replaced whole when it differs.
  - Guest availability is the Engagement's, minus passed items. An empty field clears the cell, and nothing ever falls back to Scheduling or Next action.
- **Report:** lists the returns, the pitches and the cleared cells.

### Inbox (`routines/inbox.md`): one line, 158 bytes, in STEP 3's Scheduling bullet

> …keeping the older lines; then reset Guest availability to their side's current items (Offer, Preference, Request, To confirm), as written with zone and source date, never host slots. No email…

### WhatsApp (`routines/whatsapp.md`): the same, in STEP 2b's Scheduling bullet, for the guest side's WhatsApp

## One-time backfill at deploy (8 rows, written directly)

These are cleanup's source-checked lines of 18 and 19 Oct, put into the new kinds. I wrote nothing; these are the proposed values.

| Row | Guest availability (proposed) |
|---|---|
| Alex Cutler (un#) | Offer: Mon 26 Oct 9-10am CT / 10pm SGT (PR, 7 Oct)<br>Offer: Tue 27 Oct 9-10am CT / 10pm SGT (PR, 7 Oct)<br>Offer: Wed 28 Oct 8-9am CT / 9pm SGT, their preferred (PR, 7 Oct)<br>To confirm: likely Thu 29 Oct; the mail says "Thursday, October 27: 8-9am CT / 10PM SGT", and 8am CT is 9pm SGT, so date and time to confirm (PR, 7 Oct) |
| Luca Prosperi (un#) | Offer: Thu 5 Nov 9am ET = 10pm SGT (PR, 30 Sep)<br>Offer: Thu 5 Nov 2pm ET = Fri 6 Nov 3am SGT (PR, 30 Sep)<br>Offer: Fri 6 Nov 9am ET = 10pm SGT (PR, 30 Sep) |
| Ryan Louvar (un#) | Offer: Mon 26 Oct, Thu 29 Oct, Fri 30 Oct, 7-9am "EST", a one-hour hold in each (PR, 6 and 12 Oct)<br>To confirm: ET is on daylight time until 1 Nov, so 7-9pm SGT; if they mean EST, 8-10pm SGT<br>Preference: October over November (PR, 6 Oct) |
| Mike Cagney (un#) | Preference: end of October, around 9am New York = 9pm SGT (precall, 6 Oct); no dates offered yet, their side to send them |
| Todd McDonald (un#) | Request: they ask us for times; Todd is open the last week of October (PR, 13 and 16 Oct) |
| Adrian Cachinero Vasiljevic (un#) | Preference: end of October; Tuesdays are tricky (Adrian, 11 Oct)<br>Request: send a few slots once Sri is back; he picks one (Adrian, 11 Oct) |
| Guy Tytunovich (B2S, Booked) | Offer: 24 Nov 14:00-17:00 IST, hard stop, for the recording (CHEQ, 18 Oct)<br>Offer: 22 Nov 13:30 IST or 19 Nov 14:00 IST for the check call (CHEQ, 18 Oct) |
| Fred Hsu (un#) | empty: nothing offered |

- The one hidden un# row with a board value (Not now) is left to clear by the projection. The value stays in its Scheduling history.
- Host notes and Host availability start empty and fill from the boards on the first run. All seven visible Sri availability cells are blank today.

## Dry run, read only, 19 Oct

### Board Guest availability: today and after the backfill

| Row | Board today | After | What it fixes |
|---|---|---|---|
| Alex | 18 Oct source-check line, then "wants to record before or around the 21 Oct Aero launch" | The four lines above | The superseded launch line is gone; the 29 Oct date and time stay qualified |
| Todd | "Asked availability for remote recording - Last week of October" | Request line | No longer reads as offered slots |
| Luca | "Nov 5th and 6th - 10 PM SGT" | Three offers | The 2pm ET option is back, with its SGT date |
| Ryan | "26th Oct, 29th Oct and 30th Oct - 7 PM SGT" | Window plus the EST question | The window and zone ambiguity are kept |
| Mike | "Last week of October" | Preference with time | The 9am New York time is kept, and it's marked a preference |
| Adrian | "End of October; will pick one of a few slots Sri offers" | Preference plus Request | Same meaning, typed |
| Fred | empty | empty | none |

### Eval snapshot and short pitch

A helper fetched the 7 Engagement and 7 board pages read-only and applied the EVAL SNAPSHOT rule.

| Row | Selected eval (added sections) | Short pitch source | Board today | Change on first run |
|---|---|---|---|---|
| Alex | Eval (2026-10-17) | 17 Oct eval's own line | Eval (2026-10-09), old pitch and verdict | **Replaced** with the 17 Oct eval; pitch updated |
| Fred | Eval (2026-10-17) + Numbers (18 Oct, "added to the eval") | 9 Oct (the 17 Oct eval has none; the two 9 Oct copies have the same text) | Eval (2026-10-17), no Numbers | **Numbers added**; pitch unchanged, noted "newest eval has none" |
| Todd | un# eval (2026-10-09) | 9 Oct | same date | none, except it now says where the pitch came from |
| Luca | un# eval (2026-10-09) | 9 Oct | same date; **board pitch is the old sheet pitch** | Board pitch replaced by the eval's |
| Ryan | un# eval (2026-10-09) | 9 Oct | same date | none |
| Mike | Eval (2026-10-09) over the same-date un# eval copy | 9 Oct | the shorter copy | Fuller copy (Logistics and Next step lines) |
| Adrian | un# eval (2026-10-09) | 9 Oct | same date | none |

Mike's two same-date sections are the case that made me add the tie-break: the "## Eval (" format wins. Without it the rule would have left his row and reported it.

Seen, not changed by this patch:
- Fred's Eval date field says 18 Oct, which is the Numbers date; his eval heading says 17 Oct.
- Ryan's and Adrian's Eval links use the old claude.ai/public/artifacts form.
- Adrian's eval still says "booked to record 12 Oct"; that recording was cancelled. Source facts are cleanup's.
- Luca's board Eval "Strong consider" is decision 192's mapping of Pre-call needed, as intended.

## Acceptance replays (traces against the patched text)

| # | Case | Trace | Result |
|---|---|---|---|
| H1 | Sri writes a note on Alex's row without changing his Yes | STEP 1 return: board note differs from Host notes. Host notes = note (date), and one ask for its owner. Host approval, Status, Next date untouched. | Visible in Engagements; call unchanged |
| H2 | Sri adds his availability after the guest offered slots (Luca, Booking) | Host availability = his text (date). Zoya added to Waiting on, with "Zoya: offer Sri's slots to the guest side (Host availability, date)". "Sri: pick Nov 5 …" removed (answered). Guest availability unchanged. | Host and guest kept apart; next owner Zoya |
| H3 | Sri revises his availability, then clears it | Each change rewrites Host availability; a clear empties it with a Claude note. Each change adds its ask once; the same value next run adds nothing. | No ping-pong, no duplicates |
| H4 | Sri says Yes, but Akshay's decision differs (un# from 19 Oct 08:00) | The existing STEP 1 rule: Host approval = Yes, "Akshay: Sri says Yes … Your call?". STEP 2 keeps Approval pending until Akshay decides. Host availability is recorded only. | Akshay's authority kept |
| H5 | A team member reads only Engagements | Short pitch, Guest availability, Host approval, Host notes and Host availability are on the row and in the show views; Next action names the next owner | Nothing needs the board |
| H6 | PR withdraws Alex's 26 Oct slot by mail | Inbox STEP 3: dated Scheduling line, Guest availability reset without it. The board cell follows next run. | Stale offer gone |
| H7 | All of Ryan's dates pass with no booking | The projection drops passed items; the board cell clears. Engagement history stays. | Never a stale slot |
| H8 | A new eval for Alex dated 25 Oct | EVAL SNAPSHOT picks 25 Oct by date. The board body is replaced whole. Short pitch follows only if it was still the last eval's. | Current eval, person's edit kept |
| H9 | Fred's 18 Oct Numbers above the 17 Oct eval | Included: belongs to the eval, dated after it | Numbers on the board |
| H10 | Repeated run, nothing changed | Every write is "only if different"; asks are added once per change | No writes, no rows created |
| H11 | Existing board row, new pitch, eval and availability | STEP 3 updates the existing row found by Engagement relation, else OS key; never re-created by name | No duplicate row |
| H12 | Two eval sections with the same newest date (Mike) | The "## Eval (" copy wins; if both are the same format, the board body is left as is and the row reported | No guessing |
| H13 | Todd's "Request" with empty host availability, To be scheduled | The existing host's-move rule: "Sri: share availability …" once | Correct owner |
| H14 | Mike's Next action asks Sri to pick a slot, but no dates were offered | Out of scope for this patch, which changes no other ask; listed for Zoya or Akshay (cleanup flagged it on 19 Oct) | Reported, not changed |

## Bytes and compatibility (prompt block, sha256 first 16)

| Build | Host boards | Inbox (spare) | WhatsApp |
|---|---|---|---|
| Live today | 8,474 / 5819ccf7528ca16f | 65,364 (172) | 22,647 |
| Release + this | 12,167 / b436e8962f58a6c3 | 65,006 (530) / d2515bfe06a65ad8 | 22,918 / 0b355b96ffe6162b |
| Release + AR-20261019-2 + this | 12,167 | 65,197 (339) / d185f9708aa6378d | 32,628 / 95490a2e3b53f345 |
| Chain end + release + AR-20261019-2 + this | 12,167 | 65,260 (276) / ae0a13b03e7a04f2 | 33,199 / b77c9a41ba449a5f |

The WhatsApp hashes are on the repo text with id placeholders.

**Order checks (all replayed):**
- The on-release patch applies on the release, and also after AR-20261019-2. Both are byte-equal to the script build.
- AR-20261019-2 applied after this gives the same prompts as before it.
- The pending chain's after-release patches apply after this (inbox with an offset) and give the same chain-end build.
- On bare live, without the trim, the script still applies, but the inbox would have 14 bytes spare, so that order isn't offered.

## Deploy steps (main, after cleanup accepts)

1. Confirm dfd44ca's inbox is live, by readback.
2. Add the four properties and update the two descriptions and the layout. Read back the schema.
3. Write the 8 backfill values above. Read them back.
4. Push host boards, inbox and WhatsApp, in that order, each with a byte and hash readback.
5. The first host-boards run is supervised: compare all 7 visible un# rows and the B2S row with this dry run, and record the results on the task.

**Rollback:**
- Re-push the three previous prompts.
- The four properties can stay empty; nothing reads them once the old prompt is back.
- Board values restore themselves on the old prompt's next run, from Scheduling, as today.

## Not in this patch

- **Eval maintenance triggers for un#** (item 4 of the design note): unchanged. Cleanup's source checks found no row needing a rerun.
- **Public claude.ai link host access:** still unverified. The board keeps the Notion fallback unless a public link is recorded.
- **Stale "Mamatha" in Waiting on** for Luca, Ryan and Adrian (un# moved to Zoya on 19 Oct): Zoya rewrites these when she touches the rows. This patch doesn't change them.

## v2 delta: Codex's focused review of 01d0f9d (19 Oct)

Only the three paths Codex named changed. The change-only diff is `ar20261018-9-01d0f9d-to-v2.diff`. Everything else in this package is as reviewed: fields, STEP 0, EVAL SNAPSHOT, projection, backfill and deploy steps.

### 1. Guest availability is updated in part, and only from the guest side (inbox, WhatsApp)

**Inbox, before:**
> then reset Guest availability to their side's current items (…), never host slots.

**Inbox, after:**
> if their side states availability, update Guest availability: add or correct only what they state (Offer, Preference, Request, To confirm, as written with zone and source date), drop what they withdraw or replace and passed ones, keep the rest; host slots and other logistics never touch it.

WhatsApp says the same, and adds that nothing here books a slot.

### 2. Host return owns one step per field

- A change writes the field, sets that field's own step and records "host … <date> routed", all in one page update.
- A revision replaces that one step and never adds a second.
- A clear removes the step and never leaves an offer with no slots.
- After an interrupted run (field written, no routed line), the next run sets the step once.
- A step someone has since done isn't added back.
- Every other ask and owner stays.
- A host note or availability is never a booking, approval or commercial decision.

### 3. B2S and HBD call branches keep other obligations

- The owner is added to Waiting on.
- The step replaces only the host's own "your call" ask, and every other ask stays after " | ".
- The host comes off Waiting on only if nothing else of theirs is left.
- Each call is applied once ("<Host>'s call <call> pulled").
- The team member is whoever sends that show's guest mail: Zoya on B2S and HBD from 19 Oct 08:00 JST (decision 323). Under the Built to Share hold, Zoya's own rules page stops her sending.

### Replays for the delta

| # | Case | Trace | Result |
|---|---|---|---|
| D1 | Alex's PR withdraws only Mon 26 Oct | Inbox: "drop what they withdraw" removes the 26 Oct line; 27 and 28 Oct and the qualified 29 Oct line stay | Three items left, uncertainty kept |
| D2 | Ryan's PR writes "sorry, we meant EDT" | A correction of what they stated: the To confirm line is replaced by the corrected offer; the dates stay | Zone fixed, nothing else touched |
| D3 | A mail that only carries Sri's slots or studio instructions | Not their side stating availability: Guest availability unchanged; Scheduling gets its dated line as before | Field untouched |
| D4 | Luca's PR offers a new Nov 9 slot and says nothing about the old ones | Added; the three earlier offers kept | Partial update |
| D5 | Sri's availability A, then B, then cleared | A: field, the Zoya offer step and a routed line. B: field and step replaced, one step only. Cleared: field emptied, step removed, cleared line, no empty offer | One step at most, never stale |
| D6 | Unchanged rerun after D5's B | Routed line for B's stamp exists: nothing | No duplicate |
| D7 | Run stops after writing Host availability, before Next action | Next run: field equals board, no routed line for the stamp, so it sets the step and the line once | Recovered, once |
| D8 | Zoya offers Sri's slots and removes the step herself | The routed line for that stamp exists, so the step isn't re-added | No ping-pong |
| D9 | B2S Yes on Approval pending, while the row also carries "Akshay: invite to the FT Community" | Host approval Yes, Status Booking (if Decision pending or Precall done); "Zoya: Satish said yes, get recording slots" replaces "Satish: your call on …"; Akshay's ask and his place in Waiting on stay | Independent ask kept |
| D10 | HBD No while "Zoya: send the guest form" is open | Host approval No, Status We declined, "Zoya: send the decline (Arjun said no)" first; the form step stays after " | " for its owner to settle | Nothing erased |
| D11 | The same B2S Yes seen on the next run | Claude note "Satish's call Yes pulled": not applied again | Once |

### Bytes after the delta (prompt block, sha256 first 16)

| Build | Host boards | Inbox (spare) | WhatsApp |
|---|---|---|---|
| Release (live now) + this | 13,369 / bf7ae5df8f1fa099 | 65,140 (396) / 38b73856e0e5bd86 | 23,083 / ec951c5796f58953 |
| + AR-20261019-2 | 13,369 | 65,331 (205) / b64fd79f45ad87e1 | 32,793 / 422fc33384c11598 |
| + pending chain | 13,369 | 65,394 (142) / 2ac894e097421c8d | |

**Headroom flag:** this delta costs the inbox 134 bytes. With both AR-20261019-2 and AR-9 in, the margin is 205 bytes, and 142 with the chain as well. AR-9 alone on the live release leaves 396.

**Orders replayed, all byte-equal:**
- on-release patch (6d6c65b5…) on the release;
- the same patch after AR-20261019-2;
- AR-20261019-2 after this, by script and by its patch;
- the pending chain's after-release patches after this.

**Build:** ar20261018-9-build.py (905d4cea…).
