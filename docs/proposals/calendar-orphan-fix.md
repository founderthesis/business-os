# Calendar: orphan prep entries and blocked actions

CTO, 20 Oct, after Akshay flagged a "calendar sync error". In run cse_011mP2zw7ZY1xJQEKqKaL7iW (20 Oct 14:36 UTC), the auto-mode classifier blocked delete_event on the private, guest-less "Prep: Visakh @ Fyn Mobility" entry (its precall was cancelled). The run then refused a Notion fetch, abandoned the run, skipped the audit marker and sent Akshay a push. The CTO deleted that entry by hand.

Prepared, not reviewed, not deployed.

Build: `python3 docs/proposals/calendar-orphan-fix.py <live calendar prompt> <out>`. Live 56,059 / 5576c67e1181d79e becomes 56,754 / e09abea53c608d74 (695 B more, 8.8 KB under the cap). Cut 1's calendar part still composes on top: 51,600 B, which stays below this base.

## Changes

1. **ORPHAN ENTRIES** (new hard rule). A prep, cooling-off or Podcast prep entry whose call is gone is never deleted.
   - If its start has passed, it's left alone.
   - If it's in the future, was created by ad@thepodium.in and has no attendees, update_event renames it "Cancelled: <old summary>" with notificationLevel NONE and changes nothing else.
   - Anything else (the host's Podcast prep invite has an attendee), or a blocked rename, becomes the report line "orphan prep entry: <summary> <D Mon>".
2. **A blocked or refused tool call never ends the run.** The run skips that item, finishes every other step and reports the block in one line. The audit marker is still written, because a blocked item counts as handled once it's in the report. There's no push for one blocked item, only when the whole run fails.
3. **The four delete paths now point to ORPHAN ENTRIES:**
   - audit rule 5 (prep entry mismatch);
   - STEP 3, "the call was cancelled";
   - the cooling-off block;
   - the host's Podcast prep invite.
4. **Report:** "prep entries created, moved, marked cancelled; blocked actions".

Untouched deletes: the duplicate booking the booker asked us to cancel (decision 322, an invite) and expired day-before drafts (Gmail, not calendar).

## Notion, with the deploy

The prompt reads the "Calendar rules" page every run, and the page wins on a conflict. Rule 7's "What the run does" cell says "renames it, or deletes it if the call is gone". It changes to: "Fixes its own entry: renames it. If the call is gone, a future entry is renamed \"Cancelled: <title>\" (never deleted) and a past one is left alone. ..." The routine page also gets one Change log line.

## Replay

Fyn Mobility, 20 Oct: the entry's start had passed, so the run leaves it and goes on. Had it been in the future, it would have been renamed "Cancelled: Prep: Visakh @ Fyn Mobility (...)". If that rename were blocked too, the report would carry one line, the audit marker would still be written, and there'd be no push.
