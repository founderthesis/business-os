# Cut 1: capture-only inbox, one wording source, one cadence source

CTO week plan, roadmap items 2 and 5 (due to Cleanup Wed 21 Oct 15:00 JST, deploy 19:00 JST). Decisions 352, 354, 355, 359, 360 (as amended: each precall promise is its own Task row). Design rule: cut before adding (decision 357).

Prepared, not reviewed, not deployed.

## What it prevents

- Two senders for one step: the inbox and Zoya both send close notes, acknowledgements, admin and asset replies.
- Rules the prompts still enforce for people and tools that are gone: Mamatha (decision 352), Salesblink (retired 19 Oct), the Templates database (wording lives on the wording page), dated switch-over text for un#, Built to Share and Human by Design (all past).
- Cadence numbers in six places that disagree (Cadences now holds them).
- Precall promises lost inside a guest row's Next action (decision 360).
- A recorded guest with no FT Community row, and Engagement URLs written into Blurb link (decision 359).
- Zoya stopping a follow-up run early on her own guess about the window (20 Oct 21:33 JST run: about 90 due, 1 sent).

## Build

`python3 docs/proposals/cut-1-build.py <dir with trig_<id>.txt live bases> <out dir>`. It checks each base's bytes and hash, composes the sweep on the due-versus-done build, refuses any output that is not smaller than its live base, and refuses an em dash.

| Routine | Live | Cut 1 | Output hash |
|---|---|---|---|
| Inbox | 65,324 / d09f63ec081186de | 56,677 | 2832aa83db2e70ed |
| Zoya | 49,048 / 487ebbf6feef8db7 | 48,900 | e7929bc75cb40caa |
| Calendar | 56,059 / 5576c67e1181d79e | 50,905 | 78f2abfe6d0688d3 |
| Sweep | 35,943 / b0888b6624e6848f | 30,105 (incl. due vs done) | d943bf0aa6137e04 |
| WhatsApp | 21,846 / 80c9f92041f3b548 | 21,598 | 0b4dda9276486041 |

Total: 228,220 to 208,185 bytes (minus 20,035).

## Per routine

**Inbox (cut-1-inbox.py).** Capture-only. It sends only the holding reply (STEP 6), the Saurabh thanks (6a), the vendor redirect (6b) and WhatsApp to Akshay. Akshay's decision mail was already Zoya's (d0); the sponsored close note, edit-notes reply, acknowledgements, admin and asset replies and routine replies become "Zoya: <step>" rows. Gone: TEMPLATE MODES, the Templates database, 6c b/d/e (the send and draft paths), the Mamatha eval bullet, every Mamatha step, the date-gated show text. New B2S and HBD pitches go to Akshay's list (they waited on Mamatha). Invite cancellations on a guest's plain request stay. Blurb link is never written (decision 359).

**Zoya (cut-1-zoya.py).** Cadences is the master for every number (LIMITS, nurture intervals, payment reminders, revival caps). Decision 354 for PR people. Decision 355 for sponsored revival. Follow-up runs work their due list until it is empty, the cap is reached or a hold applies; never an early stop on the window. STEP 0g Monday scorecard: 5 lines, last week, counted from Activities, Engagements and run records, dedupe key Source ID "scorecard:<Monday>". Gone: the one-time loop-ins (ran 19 Oct), STEP 0a go-live, dated scope text, Mamatha, Proposed mail. Kept on purpose: the Salesblink hold in ONE PERSON, ONE ASK, which still applies until 2 Nov.

**Calendar (cut-1-calendar.py).** ZOYA LIVE on every show. Wording from the wording page. The day-before note keeps its live behaviour: the Templates row's Mode was Send, so Founder Thesis sends it from Zoya's inbox with the existing checks and the unused draft-and-approve path goes; client shows stay drafts. The declined-invite question on client shows is now Zoya's (it was an ad@ mail). Decision 359: a confirmed Founder Thesis recording makes sure the guest's FT Community row exists (To invite, Person, Source FT guest, one per person), and no writer touches Blurb link. Decision 360: each precall promise is its own Kind Task row (For engagement, owner, date, Source ID "precall:<event id>:<n>"), never a Next action segment; a group add also ensures the FT Community row. Transcript location per decision 364.

**Sweep (cut-1-sweep.py, on due-vs-done-build.py).** STEP 3e and 6b (template review) go with the Templates database. 3d drafts take the client-show pre-release toggle. Every Mamatha step and the dated show text go. The cap points to Cadences.

**WhatsApp (cut-1-whatsapp.py).** Akshay's phone number and the community group id come out of the prompt (no phone numbers in committed files; both are found at run time). The stale STEP 3d line goes, and so does its Blurb writer (the calendar is the one writer, decision 331). New 0b: one line per precall in the Zoya group listing the promise Task rows, ending "anything else you promised?" (decision 360). A guest joining closes their community-add Task row.

## Notion, applied with the deploy

- Rules for Zoya and the routine subpages: duplicate numbers out (pointers to Cadences), and the eight contradictions the CTO listed: counts, titles, decision 346 in sections 2 and 5a, routine 5's ending, decision 355 on revival, "Stay awesome" samples, Mamatha in Cc, the follow-up window. Exact edits: `cut-1-notion.md`.
- Templates database: card moves to "Dead databases" on the home page. Agents can't delete it; Akshay can later.
- Developer page: Change log line; routine pages updated.

## Risks for review

1. The inbox stops sending acknowledgements and admin replies on every show; Zoya sends them from her inbox (or from ad@ with herself added when she isn't on the thread). Admin replies used to be signed "Akshay's team" from ad@.
2. A B2S or HBD pitch now lands on Akshay's list instead of Mamatha's.
3. The day-before draft path for Founder Thesis is removed. It was unused (Mode Send).
4. Zoya's early-stop removal can raise sends per run; the caps and the 7-day rule still bound it.
5. If the inbox part can't be reviewed in time, it ships separately: the other four parts don't depend on it (Zoya checks the thread before any close note).

## Replays

- Mobavenue (20 Oct 21:33): with "work until done", the run continues past the first send instead of stopping on the window.
- Abhijith (Codewave) 20 Oct precall: the group add becomes Task "Task: add Abhijith ... (Codewave, 20 Oct precall)" with Source ID precall:<event id>:1, matching the CTO's worked example, and the Zoya group gets one line.
- Matthew (Magic Bus): once audio is in Drive, Recorded plus an FT Community row exists (it already does: no second row).
- A sponsored no on an ad@ thread: the inbox records They declined and hands "Zoya: send Akshay's sponsored close note"; Zoya sends it once after reading the thread.
