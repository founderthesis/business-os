# Decision 563: transcripts from Mamatha, one thank-you rule (text alignment)

Main, 12 Nov. CTO ask. Text only, no new behaviour.

## What I found first

**No live prompt needs a change.** These already follow decisions 456 and 412: the live calendar (r24, and the calendar-prep-link build), the live sweep (r24), and the r26 Zoya builds (hourly, SLOW task, SLOW file, episodes).
- "Ranjita" appears in none of them except WhatsApp's list of team chats, which is about reading her chat, not transcripts.
- Calendar STEP 4c already drafts the thank-you as a standalone "Next Steps | ..." mail with no attachment and says Zoya sends the transcript later.
- The SLOW file's c(4) and c(4b) already say the thank-you never carries the transcript and Zoya sends it on the thank-you thread once it has gone.

So r26's hashes are unchanged, and nothing here needs a deploy except the Mac task.

The stale text was in the repo copies and in the Mac task, whose file is its prompt.

## Changed

**routines/mac/transcripts.md (the Mac task; it runs from this file, so this is the one real change):**
- THANKS is retired (decisions 412, 563). It existed only to attach the transcript to the thank-you draft, and for Founder Thesis to write that draft itself. Now the task:
  - writes, attaches to and edits no draft;
  - has two jobs, FILE and RECORDED;
  - has no draft-attach gate;
  - in TEST MODE creates no test draft;
  - reports no thank-you lines;
  - drops an open THANKS from an "## Open Mac jobs" line rather than working it.
- Its tool grants say MCP Emails draft create and draft update can be revoked. Akshay can do that on the Mac whenever suits.
- Source 5: "Mamatha's mail in Zoya's inbox (decision 456: transcripts come only from her)" replaces Ranjita's reply.

**Repo copies (stale; the live prompts are the docs/proposals builds):**
- **routines/daily-sweep.md:** the decision 376 line becomes "decision 456: transcripts to Mamatha", and STEP 3i's Next action becomes "Zoya: ask Mamatha for the transcript (decision 456)".
- **routines/calendar.md:**
  - the same two lines;
  - the intro's "drafted ... for him to send with the transcript" becomes "with no transcript; Zoya sends the transcript on that thread after it goes (decisions 412, 563)";
  - the DRIVE line no longer says transcripts are attached to the thank-you.
- **routines/zoya.md (the retired single prompt):**
  - INTERNAL TASKS a and c point to Mamatha. Waiting on goes to Zoya, not Mamatha, per decision 352: "Zoya: transcript from Mamatha for <guest>'s <D Mon> recording".
  - c(4) and (4b) now match the SLOW file: no attachment on the thank-you, and Zoya sends the transcript on its thread once it has gone.

## Left as is

- **routines/tasks.md:** Ranjita's three rows are copy work (themes and final copy, release emails and posts, title and show notes) that starts once the transcript is in. They're not transcript fetching, so she stays their owner.
- **zoya-slow-work.txt:** already handles 456. Its one "Ranjita" is "or on Ranjita from before decision 456 (take it ...)", which hands old rows over. Checked only, as asked.

No em dash added. The one in routines/daily-sweep.md was already there.
