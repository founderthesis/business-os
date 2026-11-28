# Replay 21: B round (5 Nov) for calendar, sweep, WhatsApp, capture, actions, dossiers

Offline, read-only. Nothing sent, nothing written outside replay21/.

## Build check

Rebuilt from the live copies: precall-409/patch.py (cal, sweep, wa), then b-round-5nov/patch.py (all six). All six outputs are byte-identical to docs/proposals/b-round-5nov/*.txt, so the only changes are the patch edits (each asserted exactly once).

| Prompt | Bytes | sha256[:16] | Em dashes live / new |
|---|---|---|---|
| calendar | 60,705 | 55c75cdd76a31793 | 0 / 0 |
| sweep | 43,547 | 383febfb5cd969ec | 1 / 1 (line 85, "Independent review — latest checkpoint", a quoted page section name, pre-existing) |
| whatsapp | 27,410 | 174d931773dd6cc0 | 0 / 0 |
| capture | 48,967 | bf5bd96cdde44722 | 0 / 0 |
| actions | 46,424 | 7d2ff9fc1a50bc89 | 0 / 0 |
| dossiers | 6,151 | fb00212e026fcf94 | 0 / 0 |

All under 65,336. Largest is calendar with 4,631 bytes of headroom.

## C1 (B2, B5, calendar 3b): PASS, with 2 defects

What governs it: 3b, "never a calendar-invitation thread, a subject starting "Invitation:", "Updated invitation:", "Accepted:" or "Declined:" ... no other thread: a new mail), To the guest's People Email, else the guest's own address on the recording invite (write it to People's Email), Cc Via (PR), every other Stakeholder and the house copies (Akshay; Chaandini on Built to Share)".

- Thread: none, so it's a new mail. Subject per the toggle.
- To: the guest's address from the invite, which also gets written to People Email. Cc: Via, Stakeholders, Akshay.
- Calls in order: Notion fetch of the prep note page, then email_compose (a new mail) from Zoya's inbox (c786...) with include_signature false, html_body plus body, then the Activity "Zoya sent: day-before note for <guest> (<event id>)" with msgid:.
- Any path to email_compose action reply? No. MAIL FORMAT forbids it: "never through email_compose action reply".

Defects:
- D1 (risk of sending from ad@): the reply recipe never names the inbox. The same paragraph says "Drafts: MCP Emails draft on ad@thepodium.in (MAILBOX)", and MAILBOX says a draft is "never sent by you". So on a reply path, a model could build the draft in ad@ and then either send it from ad@ (against decision 420) or refuse to send at all.
- D2 (minor, pre-existing): "Stakeholders first" still reads "the most recent thread with the guest's address". In this scenario that is the "Updated invitation:" thread. Also, "Zoya's THREADING" is never defined in this prompt.

## C2 (B7, CANCELLED IN WRITING with a blocked delete_event): FAIL

What governs it: "A delete the tool refuses or a permission prompt blocks ...: still do the row part below now, put "Akshay: delete the <D Mon> <precall|recording> invite for <guest> (blocked: <error>)" on the row with Akshay in Waiting on, log the Activity only once the event is gone, and add a report line every run until it is; a later run that deletes it takes the segment off."

Run 1:
- Row: Call type cleared, Booked goes to Booking, and the segment above is added with Akshay in Waiting on.
- No Activity is logged.
- One report line.
- Prep and cooling-off entries: unclear. "Then delete its own prep..." comes after the blocked sentence.

Run 2, which succeeds: the cancel:<event id> lookup finds nothing, so the delete runs. Then it deletes the entries, logs "Zoya cancelled: ...", takes the segment off and removes Akshay per OWNERS.

Why it fails:
- D3 (flapping). The event still exists after run 1. STEP 2's first bullets ("For each matched, confirmed event in the future: Recording: Status -> Booked ... Call type Recording", with Next action "Recording on <date>" first) undo the row part on every run until the event is gone. STEP 3 prep entries and STEP 3b still see a live event. 3b's guard, "Akshay is not in Waiting on for a hold on this recording (no-show, cancellation or reschedule question)", only covers this if the model reads a delete step as a "cancellation question".
- D4 (contradictions in the same bullet). The row part says "take any Akshay ask about this cancellation out of Next action (and Akshay out of Waiting on ...). Nothing goes on his list." The blocked rule puts an Akshay ask about this cancellation on the row. Also, B7's text says "Zoya: delete <event> (blocked: <error>)" and the prompt says "Akshay: delete ...". Akshay is defensible, because Zoya's prompt has no delete_event path and decision 325 allows steps only he can take. But it's a departure from B7 and needs the CTO's ok.
- Pre-existing: the row part's "a recording at Booked goes back to Booking" contradicts the HARD RULE "Never move an Engagement Status backward".
- Not a prompt change: B7's "allow Google Calendar delete_event" is a permission setting on the calendar task. It isn't in this build.

## C3 (B11, calendar 4c and 4f): PASS, with 1 contradiction

- Draft: "on the recording day as a standalone new mail, never a reply on an older thread". It goes in ad@ as MCP Emails draft action create. Subject "Next Steps | <Guest full name> @ <Company> <> Founder Thesis", To the guest plus Via, Cc Stakeholders plus the house copies, no attachment.
- The one segment: "Akshay: send the thank-you to <first> (draft ready) and add <first> to the FT Community WhatsApp". That's about 94 characters.
- 4f Task row: Name "Transcript: <guest> @ <company> (FT, <D Mon> recording)", Next action "Zoya: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread", Waiting on Zoya, Source ID transcript:cal:<event id>.
- "Attach the transcript" is gone from FT. 4c.2's community segment is gone.
- Left over: 4d (client shows) still writes "attach the transcript". That's outside B11.
- D5 (contradiction): the DRIVE header "(read only; transcripts are attached to the thank-you, never shared)" now contradicts 4f, where Zoya sends the transcript on the thank-you thread.
- Minor: open rows from before this build keep the old "...attach the transcript" segment until Akshay sends. No cleanup covers it.

## C4 (B14): PASS for every writer; FAIL on the sweep cleanup's Membership rule

- Calendar 4a: sets Membership Invited; "the add itself is never a segment". New actions: "a group or community add is never a segment (item 20)".
- Sweep 3k: "No Next action segment for it".
- WhatsApp e0: "No Engagement segment". The reply is "Zoya ✨ noted: <name> is on your invite list".
- WhatsApp 3a(1): "and no Engagement segment (item 20)".
- The only segment that still names the community is 4c's thank-you, which is intended.
- Cleanup removes "Akshay: invite <name> to the FT Community" and "Akshay: WhatsApp addition pending" segments, and keeps "the thank-you segment that names the community". The kept one starts "Akshay: send the thank-you", so prefix matching is safe.
- D6: the cleanup's "make sure that guest's FT Community row is To invite or Invited (never lower an Added row)" would also raise Declined, Unresponsive or Left rows to To invite. That contradicts the same step's "set Membership To invite only if it is empty, never another change".
- Pre-existing: calendar 4a's WhatsApp paragraph sets Invited when Akshay "said he would add them". The new-actions paragraph says "To invite (Invited if Akshay already sent the invite)" for the same notes.
- Minor: WhatsApp b2 doesn't trim the "and add <first> to the FT Community WhatsApp" half of the thank-you segment when the guest joins.

## C5 (B12, sweep 3a3 and actions): PASS for sweep and actions; FAIL across prompts (capture)

Sweep, on the 779-character row:
- It splits the Next action on " | " and measures each segment past its owner and its "[reply msg-... ts]" key. The key is kept ("Never change ... an action key").
- Any segment over about 120 characters is cut to who, step and date. The cut words go first in "YYYY-MM-DD: Next action detail: ...".
- "Write ok, not ok or a change in Your call." is dropped. Of two segments with the same owner and step, the older one goes.
- Waiting on is untouched. Longest row first, at most 30 a run, with a count in the report.

B12's "never action keys in Next action" is not done here. The sweep deliberately keeps them, which matches live Zoya ("Zoya [reply msg-<id>-n <ts>]: <ask>"). That's deferred to decision 438's Action keys field.

Actions segments, with sample fills (total characters / characters past the owner):

| Decision | Segment | Total | Past owner |
|---|---|---|---|
| 446, confirm | "Akshay: Dinesh Venugopal @ Infogain (Built to Share) scheduling: confirm Thu 12 Nov 16:00 IST and create the invite? (5 Nov)" | 124 | 116 |
| 446, board | the slots on Satish's board | 94 | 86 |
| 444, re-open | "Akshay: Priya Nair wrote again (new guest pitch for Rahul, closed We declined 12 Oct): re-open as Decision pending and have Zoya send the eval reply? (5 Nov)" | 157 | 149 (over) |
| 444, reply no | | 96 | 88 |
| 448 | "...replied on your 3 Nov mail: wants a 30 min precall first. Recommend: have Zoya send podm.in/30min (5 Nov)" | 124 | 116 |
| Brand | "Akshay: Acme Fintech wants a sponsored LinkedIn mention, proposed USD 1,150 (draft in the page body)" | 100 | 92 |

The 444 re-open branch runs over unless <the reply> is kept to a few words.

- D7: capture line 91 (decision 162) still writes Next action "Replacement proposal: ... Eval pending. Write ok, not ok or a change in Your call." on a row Waiting on Akshay. That's about 164 characters with no owner prefix. Sweep 3a3 then strips the "Write ok" phrase. After that, sweep 3a2 ("no Next action segment starting "Akshay:" ... no proposal ending "Write ok, not ok or a change in Your call"") finds nothing of Akshay's and removes him from Waiting on. The replacement decision falls off his list.
- D8: the actions brand line lacks the full stop after the quote: `(draft in the page body)" Put the proposed reply`. It also has no "(<D Mon>)", unlike NEXT ACTION SIZE's own shape.
- Stale: sweep 3a2's "no proposal ending "Write ok, not ok or a change in Your call"" is a dead marker once 3a3 runs.

## C6 (B6, capture STEP 6 and 6b): PASS, with 2 defects

- PR pitch with Zoya already in Cc: no loop-in. The rule is "zoya@myunnati.com is not already on the pitch's To or Cc (... then capture only; Zoya replies from her inbox)".
- Vendor pitch with Zoya in To: capture only ("else capture only, item 6").
- Normal pitch:
  1. email_read action read on the pitch with include_html true, plus the RAW Message-ID.
  2. draft action reply on the pitch message, in ad@ (cd37...).
  3. draft update: To the sender; Cc everyone else on it except Saurabh, plus the house copies (Zoya); body and html_body with the gmail_quote blockquote.
  4. draft_read.
  5. The Bash python assert on To and Cc.
  6. draft send with draft_id and idempotency_key "loopin:<Message-ID>".
  7. email_read original from Sent for the Message-ID.
  8. The Activity "Akshay to <name>: Zoya loop-in".
- No email_compose action reply anywhere. The Saurabh or other-address case is "action send ... "Re: <original subject>"", a new mail.

Defects:
- D9: the assert checks only "(To is that sender; ad@thepodium.in on neither)". It doesn't check that Zoya is in Cc, which is the whole point of a loop-in. The "action send" path has no assert at all.
- D10: the Zoya-already-on case gets no "loop-in skipped: <why>" note. So it never counts as "skipped on purpose" and the 72-hour catch-up re-evaluates it every run. For a vendor with Zoya on To, it's unclear whether the row still gets Waiting on Zoya with "Zoya: ask <first name> to fill podm.in/pitch-to-us". As written it doesn't, so nothing ensures her reply.

## C7 (B1, dossiers): PASS for themes, edit rights and v3; FAIL for the themes priority

- Themes: "3 to 5 broad themes, one short line each, no running order, no sequence notes, no questions". The four examples fit.
- Edit rights: "Never mention edit rights, review or approval, in any form (item 1)".
- Rewrites: every Founder Thesis row at Booked, recording within 21 days, with a Prep note link and no "prep note v3" line. Prep note only, done first. un#, Built to Share and Human by Design notes aren't rewritten; their skills are B1's zip handover.
- D11a: "a row whose Next action has "Zoya: send <guest> the themes" goes first of all" only reorders STEP 1's set: Call type Recording, Booked, within 21 days, and a missing or stale dossier or prep note. A themes row outside 21 days, or with a current dossier but no Prep note link, is never picked. B8 wants the dossier routine to pick that row up.
- D11b: actions B8 writes "Zoya: themes reply to <who>". Dossiers looks for "Zoya: send <guest> the themes". Only Zoya's r21 wording ("Zoya: send <guest> the themes once the prep note is in") matches, so rows from the actions routine are never prioritised.

## C8 (B15): PASS

- No "precall:" key or precall Task row in any of the six prompts.
- All five exemption lines read "(transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409)", with Mamatha in place of Ranjita.
- WhatsApp 0b: "for each Engagement whose Claude note gained a line "precall <date> actions checked (<event id>), <n> promises: ..." with n of 1 or more since your last post", deduped by promises:<event id>. Calendar 4a writes that exact line.
- WhatsApp carry-overs are in: AD Tasks (decision 460), and Mamatha (decision 456).
- WhatsApp b2's "open Task row for the community add (decision 360)" is legacy and harmless.

## Defects and fixes

1. Calendar MAIL FORMAT (D1). Change "A reply goes on the thread's latest message, never through email_compose action reply (Akshay, 5 Nov, item 2: a compose reply took the thread's last sender and went to ad@ alone): draft action reply," to "A reply goes on the thread's latest message, never through email_compose action reply (Akshay, 5 Nov, item 2: a compose reply took the thread's last sender and went to ad@ alone): in Zoya's inbox (inbox_id c786413a-f604-4661-9312-e7226917028a; the one kind of draft you send), draft action reply,". In MAILBOX, change "never sent by you;" to "an ad@thepodium.in draft is never sent by you;".
2. Calendar CANCELLED IN WRITING (D3, D4). Change "log the Activity only once the event is gone, and add a report line every run until it is; a later run that deletes it takes the segment off." to "log the Activity only once the event is gone, and add a report line every run until it is; while that segment is on the row, STEP 2's booking bullets, STEP 3, STEP 3b and STEP 4 skip the event; a later run that deletes it takes the segment off." Then change "Nothing goes on his list." to "Nothing else goes on his list (a blocked delete, above, is the one step that does)." Get the CTO's ok on Akshay instead of B7's "Zoya:".
3. Calendar DRIVE (D5). Change "DRIVE (read only; transcripts are attached to the thank-you, never shared)" to "DRIVE (read only; never share a Drive file; Founder Thesis transcripts go to the guest from Zoya, STEP 4f)".
4. Sweep 3k cleanup (D6). Change "make sure that guest's FT Community row is To invite or Invited (never lower an Added row)" to "make sure that guest has an FT Community row (none: create it as above, To invite; an empty Membership: To invite; never change another Membership)".
5. Capture line 91 (D7). Change "Next action "Replacement proposal: <PR> offers <new person, role> in place of <original guest> (<original Status, Tier>). Eval pending. Write ok, not ok or a change in Your call."" to "Next action "Akshay: <PR> offers <new person> for <original guest>, eval pending (<D Mon>)" (role, original Status and Tier: the Claude note)". In sweep 3a2, change "no proposal ending "Write ok, not ok or a change in Your call", " to "no proposal awaiting him in the page body, ".
6. Actions brand line (D8). Change "Next action "Akshay: <brand> wants <what>, proposed <price> (draft in the page body)" Put" to "Next action "Akshay: <brand> wants <what>, proposed <price> (draft in the page body) (<D Mon>)". Put".
7. Capture MAILBOX assert (D9). Change "(To is that sender; ad@thepodium.in on neither)" to "(To is that sender; zoya@myunnati.com in Cc; ad@thepodium.in on neither; the same check on an action send's to and cc before it goes)".
8. Capture STEP 6 and 6b (D10). In STEP 6, change "(Akshay, 5 Nov, item 6: then capture only; Zoya replies from her inbox)" to "(Akshay, 5 Nov, item 6: then capture only, with the Claude note line "loop-in skipped: Zoya already on the pitch"; Zoya replies from her inbox)". In 6b, change "(else capture only, item 6)" to "(else no loop-in, item 6: the Claude note line "loop-in skipped: Zoya already on the pitch", and the Engagement below still gets its Zoya step)".
9. Actions 448 (D11b). Change "also "Zoya: themes reply to <who>"." to "also "Zoya: send <guest> the themes once the prep note is in" (the dossier routine picks the row up)."
10. Dossiers STEP 1 (D11a). Change "Soonest recording first (a row whose Next action has "Zoya: send <guest> the themes" goes first of all, item 10)," to "Also, first of all, any Engagement whose Next action has "Zoya: send <guest> the themes" and whose Prep note link is empty, whatever its Next date or dossier state (item 10): build its prep note (and the dossier if none). Then soonest recording first,".

Low priority, pre-existing:
- Calendar: Booked going back to Booking against "Never move an Engagement Status backward".
- Calendar 4a: Invited vs To invite for "said he would add them".
- Calendar 3b: "Stakeholders first" reads the most recent thread, which can be an invitation thread.
- Calendar: "Zoya's THREADING" is undefined.
