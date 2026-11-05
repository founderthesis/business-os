# Zoya r21 offline replay (5 Nov)

Read only: docs/proposals/zoya-r21/{zoya-one,zoya-slow-work,zoya-episodes,zoya-slow}.txt against zoya-r19, the r21 edit list, and feedback items B2, B3, B8 to B12 and B15.

## Integrity
- Word diff r19 to r21: every change is an r21_edits.py entry, plus the version pins (zoya-one fad361f124d2, zoya-episodes 9b293b0051ba, zoya-slow 68882d1b0df7) and zoya-slow's SLOW-file pin. Nothing else changed.
- zoya-slow's pin checks out. Commit c2314a3c exists. The slow-work file in it has sha256 9af4c4633504ea3e..., which matches both the pinned prefix and the local file. Its length is 84,403 characters (84,407 bytes), matching "84,403 characters".
- No em dash (U+2014) in any of the four files. No "SLOW run" or "FAST run" strings.
- Sizes: zoya-one 57,147 bytes, episodes 47,176, slow 14,416. All are under 65,536.

## S1 (B2): PASS
Zoya replies to a PR who asked for slots on a Founder Thesis row. These are her calls, in order:
1. LOCK, then the run record, then RULES LOAD.
2. email_read: the inbound with include_html, then action original for its Message-ID. STEP 1 a logs the inbound.
3. STAKEHOLDERS FIRST (THREADING): PEOPLE MATCH, then Stakeholders and Via.
4. ACTIONS' Sent check.
5. PRE-SEND 2/ python assert on the planned To and Cc.
6. draft action reply on the latest message.
7. draft update with To and Cc, html with the gmail_quote, and the plain-text body.
8. draft_read, then the python assert again on draft_read's actual To and Cc (NO COMPOSE REPLY).
9. draft send with idempotency_key set to the action key.
10. Activity, then the row write (WRITE PATH and the note check).

The wording is "you can pick any slot available on this link: podm.in/book".

email_compose action reply is closed in every place it could slip in:
- SENDING: "a reply: THREADING's draft way, never email_compose action reply"
- ACTIONS: "idempotency_key on the draft send (a reply) or email_compose (a new mail)"
- Loop-in: "always the draft way, never email_compose reply's own addressing ... idempotency_key ... only on the draft send"
- PRE-SEND, and the HARD rule NO COMPOSE REPLY in all four files

No line anywhere still allows it. The loop-in from ad@ still goes the draft way. Nit: the loop-in line says only "read it back", while the python assert on draft_read comes from the HARD rule (defect 9).

## S2 (B3): PASS
- The sentence is "you can pick any slot available on this link: podm.in/30min" (BOOKING LINKS, in all four files).
- PLAIN ENGLISH now reads plainly ("works", "circling back", ...): "works" is banned and the exception is gone in one, slow-work and episodes. zoya-slow has no VOICE section and defers to the file.
- No "here works" or "any open" text is left.

## S3 (B8): FAIL on wording conflicts, though the main flow is right

### Founder Thesis
STEP 1 b applies: "Don't answer it (a themes or questions ask in it aside: that part is yours, below)".
- Thursday: Akshay goes in Waiting on, with the segment "Akshay: <EA> replied on your 3 Nov mail: asks to move to Thursday. Recommend: <step> (5 Nov)". The holding reply goes "only when it asks something".
- Themes, with no Prep note link: "once, 'will share the themes shortly' (a hold action), and 'Zoya: send <guest> the themes once the prep note is in' stays in Next action".
- Next run, once the Prep note link has landed: FAST picks up the reply action. The queue exception lets her mail a row that waits on Akshay ("the themes reply in STEP 1 b ... when his open ask is about something else"). She opens the prep page and replies on the thread with its broad themes in a few lines. That means no question list, no link and LEAK CHECK.

### un#
The flow is the same. The Thursday part becomes the decision 446 segment "Akshay: <guest> (un#) scheduling: ...? (5 Nov)", and SHOW CHECK runs on the themes reply.

### Contradictions
1. In b, the holding reply ("checking with akshay, will come back to you") and the themes hold ("will share the themes shortly") are two separate sends. The rule that merges them into one mail exists only in c, so this run would put two mails on one thread (one reply per thread).
2. With a Prep note link, the themes reply says "no Akshay ask and no holding reply". The same mail's scheduling part still goes to Akshay, and b says the holding reply goes "when it asks something". These two lines conflict.
3. On a client show, SCOPE says "When their side wrote, the holding reply (decision 390) is all you send". That line was not amended. It conflicts with "on every show" and with the HARD rule's "plus the themes answer".
4. The Zoya segment "Zoya: send <guest> the themes once the prep note is in" has no key. ACTIONS wants "Zoya [reply msg-<id>-n <ts>]: ...".

Out of scope for these files: the dossier routine picking up the row (B8).

## S4 (B9): PASS, with one ambiguity
Before the reply, THREADING's STAKEHOLDERS FIRST changes the row:
- The company comms person on Cc joins Stakeholders (PEOPLE MATCH first).
- The new agency person becomes Via, and the old Vicara Via moves to Stakeholders.
- Claude note line: "Via changed <old> to <new> <D Mon>".
- The row Name "... via Vicara PR" is renamed to the new agency.

Ambiguity 1: a second person from the same agency would also swap Via, because the rule doesn't say "a different agency". THREADING's handover rule already covers that case.

Ambiguity 2: WRITE PATH says a write "changes only this action's own segment ..., its own Waiting on entry and its own Claude note line". A strict reading forbids the Via, Stakeholders and Name changes.

## S5 (B10): FAIL on one gap
- un# recording with Akshay's ok: INVITES gives "a recording gets no Google Meet (no conferenceData ...): its recording link is the location and the first description line". The link is unhashed.co/studio, from the un# links line in SCOPE.
- Founder Thesis precall: "a precall gets a Meet link".
- STEP 0r, for a Founder Thesis recording invite that already has the Zencastr link but still carries a Meet:
  - If the link mail has not gone yet, she sends it, then "an invite that already has the link but still a Meet gets the removal alone".
  - If the link mail already went (the Gulab Patil case), the Already-done branch says "still do the link add and Call link below when the invite lacks that link". The invite doesn't lack the link, so the Meet removal is never reached and the Meet stays.
  - Also, the scan only covers "mails ... from Mamatha in the last 14 days". A recording whose room mail is older than that is never revisited.
- HARD rules: zoya-one allows the edit ("beyond INVITES' adds and STEP 0r's link add and Meet removal"). zoya-slow-work, zoya-slow and episodes say only "INVITES' adds". That's fine there, since none of them run STEP 0r.

## S6 (B12): PASS for segment length; the keys part of B12 is not built
- Client-show scheduling segment: "Akshay: Priya Sharma (un#) scheduling: confirm Thu 13 Nov 16:00 SGT (C8) and create the invite? (5 Nov)". That's 95 characters past the "Akshay: " prefix.
- With three slots ("put Tue 11 Nov 15:00 SGT, Wed 12 Nov 10:00 SGT, Thu 13 Nov 16:00 SGT on Sri's board?"), it's 123. That's "about 120", but there's no headroom.
- Reply to Akshay's own mail: "Akshay: Neha Rao replied on your 3 Nov mail: asks to move the recording to Thursday. Recommend: offer Thu 13 Nov 11:00 IST (5 Nov)" is 122. The fixed words take about 55 characters, so a longer name overflows easily (182 with "(EA to Arjun Mehta, Acme Robotics)").
- "Write ok, not ok" is gone.

Remaining conflicts with the 120 cap:
- "Akshay: can't tell which mail completed <actions>: <each candidate's Message-ID and send time>. Write which in Your call". Two Message-IDs alone are about 100 characters. This template is in one, slow-work and episodes.
- The vendor segment in slow-work (template 122 before filling).

B12's "never action keys in Next action (they live in Action keys, decision 438)" is not built. ACTIONS still puts "Zoya [<type> <origin> <raised>]" in Next action, NEXT ACTION SIZE measures "past its owner and key", and Engagements has no "Action keys" field. The one-time trim of over-length rows is also not in these files, which is expected.

## S7 (B11, SLOW INTERNAL TASKS c): FAIL
- (2) attaches the .txt to the Episode, or holds it as "no Episode yet".
- (4) The thank-you draft is a standalone new mail in ad@ with the "FT thank-you after recording" wording, Cc the PR, the Stakeholders and Zoya, and no attachment. Next action: "Akshay: send the thank-you to <first> (draft ready) and add <first> to the FT Community WhatsApp".
- (4b) Thank-you not sent yet: "the row waits". Once it has gone (ad@ Sent), she replies on the thank-you thread in her inbox (she's on Cc) with the "Transcript for review" toggle, To the guest, Cc their side and Akshay, with the .txt attached.
- (5) closes the row only after (4b).

Problems:
1. Wording: nothing in the repo or the feedback creates a "Transcript for review" toggle (Akshay's template only promises it: "We will share the episode transcript for your review shortly"). As built, every (4b) sends nothing and reports "wording missing". The toggle needs Akshay's text, or (4b) is dead.
2. Action key: "<transcript row id>:team:seq-transcript-4b:<the attach ISO>".
   - The type (team) is fine.
   - The origin doesn't fit ACTIONS' shapes. "seq-<routine>-<step n>" means a follow-up routine number and step number, not "transcript-4b". And a seq origin's raised time must be "that step's due date ... T00:00:00+09:00", not an attach time.
   - The attach time is written nowhere. The "## Transcript" line holds the name, bytes, sha256 and source; the Claude note is written only at (5). A later run, the one where the thank-you has gone, can't rebuild the same key, which defeats idempotency.
   - There's no row to key on when the file has no transcript row ("its transcript row if there is one").
3. Quiet hours: section c ends "These are internal: quiet hours and the 7-day limit ... don't apply". The header says "Kind Task rows with Show Internal are team work, never guest mail". (4b) is guest mail. The HARD rule OUTSIDE MAIL still wins, but the two lines contradict each other.
4. Waiting row: while it waits for the thank-you, the transcript row keeps "Zoya: transcript from Mamatha for ... (asked ...)", which is stale. No line says what its Next action becomes.

## S8 (B15): PASS
"precall:" appears in none of the four files. slow-work and episodes now say "(transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409)". zoya-one and zoya-slow never carried the line.

Leftover, not in the edit list: ACTIONS' team type still lists "Ranjita" (one, slow-work, episodes) after decision 456.

## Defects (exact line, then the proposed replacement)

1. **STEP 0r Already-done branch (zoya-one, B10).**
   - Old: `and still do the link add and Call link below when the invite lacks that link (Akshay, 3 Nov: a mail sent by hand leaves the invite to you)`
   - New: `and still do the link add (or the Meet removal alone) and Call link below when the invite lacks that link or still carries a Google Meet (Akshay, 3 Nov: a mail sent by hand leaves the invite to you; 5 Nov, item 13)`
   - Optional: add a pass over every Founder Thesis Booked recording invite in the next 14 days that carries a Meet, so invites whose Mamatha mail is older than 14 days are also fixed.

2. **STEP 1 b themes hold (zoya-one, B8). Two mails on one thread.**
   - Old: `no Prep note link yet: once, "will share the themes shortly" (a hold action),`
   - New: `no Prep note link yet: once, "will share the themes shortly" (a hold action; one mail with any holding reply this thread gets this run, e.g. "checking with akshay on the timing, will share the themes shortly"),`

3. **STEP 1 b with a Prep note link (zoya-one, B8). Conflicts with b's own holding reply.**
   - Old: `no Akshay ask and no holding reply;`
   - New: `no Akshay ask for the themes; a part of the same mail that went to Akshay gets its holding line inside this mail, never a second one;`

4. **SCOPE client-show scheduling (zoya-one; slow-work and episodes carry the same line). Conflicts with "on every show".**
   - Old: `When their side wrote, the holding reply (decision 390) is all you send.`
   - New: `When their side wrote, the holding reply (decision 390) is all you send on the scheduling part (a themes or questions ask in the same mail: STEP 1 b, decision 453).`

5. **STEP 1 b themes segment is unkeyed (zoya-one).**
   - Old: `"Zoya: send <guest> the themes once the prep note is in" stays in Next action`
   - New: `its reply action stays open as "Zoya [reply msg-<id>-n <ts>]: send <guest> the themes once the prep note is in"`

6. **INTERNAL TASKS c (4b) action key (slow-work, B11). Doesn't fit ACTIONS, and the next run can't rebuild it.**
   - Old: `action key "<transcript row id>:team:seq-transcript-4b:<the attach ISO>"`
   - New: `action key "<transcript row id, else the guest's row id>:team:call-<Episode id>:<the attach time, ISO with offset>", the attach time being the "attached <ISO>" that (2) adds to the "## Transcript" line`
   - Also in (2): `source (<sender>'s mail of <D Mon>, or where you found it)` becomes `source (<sender>'s mail of <D Mon>, or where you found it), attached <ISO with offset>`
   - The "call-<Activity or row id>" origin covers a row id.

7. **INTERNAL TASKS c closing line (slow-work). Conflicts with guest mail in (4b).**
   - Old: `These are internal: quiet hours and the 7-day limit (LIMITS and ONE PERSON, ONE ASK) don't apply to them; every other check does.`
   - New: `These are internal: quiet hours and the 7-day limit (LIMITS and ONE PERSON, ONE ASK) don't apply to them, except (4b), which is guest mail: quiet hours hold (OUTSIDE MAIL); every other check does.`

8. **(4b) waiting row Next action (slow-work).**
   - Old: `The thank-you not sent yet: the row waits.`
   - New: `The thank-you not sent yet: the row waits, its Next action "Zoya: send <guest first name> the transcript once the thank-you has gone" in place of the request segment.`

9. **Missing wording toggle (Notion, prerequisite for B11).** Rules for Zoya "Mail and WhatsApp wording" needs a "Transcript for review" toggle with Akshay's approved text before r21 deploys. Without it, every (4b) blocks on "wording missing". Hand it over as a decision 459 row if Akshay has to write it.

10. **"can't tell" segment over the 120 cap (one, slow-work, episodes, B12).**
    - Old: `"Akshay: can't tell which mail completed <actions, short>: <each candidate's Message-ID and send time>. Write which in Your call", Claude note "YYYY-MM-DD: held for review (<keys>)"`
    - New: `"Akshay: can't tell which mail completed <actions, short>: pick one (candidates in the Claude note)", Claude note "YYYY-MM-DD: held for review (<keys>): <each candidate's Message-ID and send time>"`

11. **Next action keys (B12, decision 438). Not built.**
    - Engagements has no "Action keys" field. ACTIONS still writes "Zoya [<type> <origin> <raised>]" into Next action.
    - This needs the field created (a schema change, outside the prompt) and then an edit to ACTIONS: `A Zoya segment carries its key in short form: ...` becomes `A Zoya segment is "Zoya: <step>"; its key goes in the row's Action keys field, one per line, "<segment step, short> = <key>"`.
    - Until then, NEXT ACTION SIZE's "past its owner and key" is the right interim wording. Say so in the build notes.

12. **STAKEHOLDERS FIRST vs WRITE PATH (one, slow-work, episodes, B9).**
    - WRITE PATH old: `changes only this action's own segment of Next action (and the segments of asks the same inbound completes, each with its completion line), its own Waiting on entry and its own Claude note line;`
    - New: append ` STAKEHOLDERS FIRST's Stakeholders, Via and Name changes and their note line aside;`
    - STAKEHOLDERS FIRST old: `an agency person now writing for the guest becomes Via`
    - New: `a person from an agency other than the current Via's, now writing for the guest, becomes Via (a colleague at the same agency: Stakeholders, Via as THREADING's handover rule says)`

13. **Loop-in alignment with NO COMPOSE REPLY (one, slow-work, episodes). A nit: the HARD rule already covers it.**
    - Old: `draft update to set To and Cc, read it back, draft send with the draft_id the update returned;`
    - New: `draft update to set To and Cc, draft_read and the python assert on its actual To and Cc (NO COMPOSE REPLY), draft send with the draft_id the update returned;`

14. **Leftover Ranjita (one, slow-work, episodes). Optional, not in the edit list.**
    - Old: `team (Jaya, Sarika, Ranjita, internal asks,`
    - New: `team (Jaya, Sarika, Mamatha's transcripts, internal asks,`

Not in these files, for the other builds: calendar STEP 3b (B2) and 4c/4f (B11), the dossier routine's pickup (B8), the one-time Next action trim (B12), and the Notion page edits (B3, B11).
