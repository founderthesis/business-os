"""B round (5 Nov feedback page, docs/feedback/2026-11-05-5nov-page.md, CTO build list B1 to B15) for the
non-Zoya routines. Main, 5 Nov. Zoya's part is routines/zoya/r21_edits.py in the r21 build.
Usage: python3 patch.py <cal|sweep|wa|cap|act|dos> <input> <out>
Inputs: cal, sweep and wa are Cleanup's decision 409 outputs (docs/proposals/precall-409/patch.py on the live
prompts), so B15 is folded in; cap, act and dos are the live prompts. Asserts the input hash, each edit exactly
once, no new em dash, and the size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"cal": "27d7bdf6", "sweep": "191497f3", "wa": "b8b7c312", "cap": "40e787a2", "act": "07832eb6", "dos": "98875d4e"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the expected %s input" % which
s = b.decode("utf-8")
Q = chr(34)

EDITS = {"cal": [
 # B2: no email_compose reply (calendar sends the day-before note from Zoya's inbox, STEP 3b).
 ("A reply goes on the thread's latest message (action reply, reply_all false, To and Cc set explicitly); never pass include_attachments on a reply (MCP Emails rejects it; replies carry no attachments).",
  "A reply goes on the thread's latest message, never through email_compose action reply (Akshay, 5 Nov, item 2: a compose reply took the thread's last sender and went to ad@ alone): in Zoya's inbox (inbox_id c786413a-f604-4661-9312-e7226917028a; the one kind of draft you send), draft action reply, draft update with To and Cc set explicitly (reply_all false), draft_read, then a Bash python assert on draft_read's actual To and Cc (To not empty; no ad@thepodium.in or team address in To; everyone the step names in To or Cc; a failure: delete the draft, send nothing, report it), then draft send with the draft_id the update returned; never pass include_attachments on a reply (MCP Emails rejects it; replies carry no attachments)."),
 # B5: the day-before note never goes on an invitation thread; the guest's address can come from the invite.
 ("the way Zoya's THREADING says; no thread: a new mail), To the guest, Cc Via,",
  "the way Zoya's THREADING says; never a calendar-invitation thread, a subject starting \"Invitation:\", \"Updated invitation:\", \"Accepted:\" or \"Declined:\" (Akshay, 5 Nov, item 5); no other thread: a new mail), To the guest's People Email, else the guest's own address on the recording invite (write it to People's Email), Cc Via (PR),"),
 # B7: a blocked delete still does the row part and shows as a step until the event is gone.
 ("If two events could match, or the words are unclear, delete nothing: Claude note line and a report line.",
  "If two events could match, or the words are unclear, delete nothing: Claude note line and a report line. A delete the tool refuses or a permission prompt blocks (Akshay, 5 Nov, item 8): still do the row part below now, put \"Akshay: delete the <D Mon> <precall|recording> invite for <guest> (blocked: <error>)\" on the row with Akshay in Waiting on, log the Activity only once the event is gone, and add a report line every run until it is; while that segment is on the row, STEP 2's booking bullets, STEP 3, STEP 3b and STEP 4 skip the event; a later run that deletes it takes the segment off."),
 ("Nothing goes on his list.", "Nothing else goes on his list (a blocked delete, above, is the one step that does)."),
 ("never sent by you;", "an ad@thepodium.in draft is never sent by you;"),
 ("(read only; transcripts are attached to the thank-you, never shared)", "(read only; never share a Drive file; Founder Thesis transcripts go to the guest from Zoya, STEP 4f)"),
 # B14: no community segments on Engagements (the To invite list on Akshay's home is the only place).
 ("; the add itself is a promise segment on this row (New actions, below; decision 409).",
  "; the add itself is never a segment: the FT Community To invite list on Akshay's home is the only place for it (Akshay, 5 Nov, item 20)."),
 ("; a community add is the one \"Akshay: invite <first name> to the FT Community\" segment, added once.",
  "; a group or community add is never a segment (item 20)."),
 ("2. Community. If the guest's FT Community row is Added, nothing. If it is Invited, make sure Next action carries \"Akshay: WhatsApp addition pending: add <guest first name> to the FT Community. Blurb: <the Engagement's page URL>\" (add it once, with Akshay in Waiting on). Otherwise add Akshay to Waiting on and \"Akshay: invite <guest first name> to the FT Community (recorded <D Mon>). Blurb: <the Engagement's page URL>\" to Next action, once (decision 300). The WhatsApp routine clears these when the guest joins.\nClaude note line for each change, \"YYYY-MM-DD: <thank-you drafted for Akshay | thank-you sent by Akshay | community ask added>\".",
  "2. Community: never a Next action segment (Akshay, 5 Nov, item 20); STEP 4b's FT Community row puts the guest on the To invite list on Akshay's home, the only place for it.\nClaude note line for each change, \"YYYY-MM-DD: <thank-you drafted for Akshay | thank-you sent by Akshay>\"."),
 # B11: the new FT post-recording mail, a standalone new mail, one Akshay step, no transcript.
 ("Until Zencastr transcripts reach Drive on their own, the thank-you goes out from Akshay by hand (decision 300, Akshay, 17 Oct). Draft it in ad@thepodium.in with MCP Emails (draft: a reply on the latest thread with the guest or PR, else a new mail), plain text",
  "The thank-you goes out from Akshay by hand (decision 300). Draft it in ad@thepodium.in with MCP Emails on the recording day as a standalone new mail, never a reply on an older thread (Akshay, 5 Nov, item 14, as Rules for Zoya says), plain text"),
 ("\"FT thank-you after recording\" (Akshay's approved version, 21 Oct), read fresh each run and used exactly as the page has it: fill only its placeholders and follow its bracketed notes (patron paragraphs out for a Sponsored guest, the PR block only when a PR is on the To line, the transcript line only while transcripts are being attached, the form link as a real link);",
  "\"FT thank-you after recording\" (Akshay's 5 Nov text), read fresh each run and used exactly as the page has it: fill only its placeholders and follow its bracketed notes (the patron paragraph out for a Sponsored guest, the PR paragraph only when a PR or comms person is on To, the form link as a real link);"),
 ("put \"Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts; attach the transcript)\" in Next action. Log \"Zoya drafted: FT thank-you for <guest>\" (Kind Draft, Source Gmail, Engagement). Do it in the first run after Recorded; don't wait for a transcript.",
  "put the one segment \"Akshay: send the thank-you to <guest first name> (draft ready) and add <guest first name> to the FT Community WhatsApp\" in Next action. Log \"Zoya drafted: FT thank-you for <guest>\" (Kind Draft, Source Gmail, Engagement). Do it in the first run after Recorded; never wait for a transcript (Zoya sends it later, STEP 4f)."),
 ("Next action \"Zoya: ask Mamatha for the transcript (decision 456)\",",
  "Next action \"Zoya: ask Mamatha for the transcript (decision 456)\" (Founder Thesis: \"Zoya: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread\", Akshay, 5 Nov, item 14),"),
],
"sweep": [
 ("no proposal ending \"Write ok, not ok or a change in Your call\", ", "no proposal awaiting him in the page body, "),
 # B14: no community segment; one-time cleanup of the old ones.
 ("While its Membership is To invite or Invited, the guest's Founder Thesis Engagement carries one \"Akshay: invite <first name> to the FT Community\" segment with Akshay in Waiting on (add it once if neither it nor \"Akshay: WhatsApp addition pending\" is there; other segments kept); Added: none (the WhatsApp routine's b2 clears it).",
  "No Next action segment for it (Akshay, 5 Nov, item 20): the To invite list on Akshay's home is the only place. ONE-TIME CLEANUP (item 20), every run until none is left: on open Engagements take out each \"Akshay: invite <name> to the FT Community\" and \"Akshay: WhatsApp addition pending\" segment (other segments kept; never the thank-you segment that names the community), make sure that guest has an FT Community row (none: create it as above, To invite; an empty Membership: To invite; never change another Membership), remove Akshay from Waiting on when nothing else is his (STEP 3a2's OWNERS), Claude note \"YYYY-MM-DD: community ask moved to the To invite list (item 20)\"; at most 30 rows a run; report the count and how many are left."),
 # B12: one-time trim, then every run, of overlong Next action segments.
 ("At most 20 a run; list them in the report.\n",
  "At most 20 a run; list them in the report.\nSTEP 3a3. SHORT NEXT ACTION (decision 438; Akshay, 5 Nov, item 15). On open Engagements, each Next action segment (split on \" | \") is at most about 120 characters past its owner and any \"[...]\" action key: a longer one is cut to who, the step and its date, and the cut words go first in a Claude note line \"YYYY-MM-DD: Next action detail: <the cut words>\" (never lost); \"Write ok, not ok or a change in Your call.\" is dropped wherever it stands; of two segments with the same owner and the same step, the older leaves. Never change what a step asks, its owner, an action key or Waiting on. Longest rows first, at most 30 a run; report the count and how many are left.\n"),
 ("FT Community rows created for recorded guests, and blurbs due or waiting (STEP 3k);",
  "FT Community rows created for recorded guests, community asks moved off rows, and blurbs due or waiting (STEP 3k); Next action segments trimmed (STEP 3a3);"),
],
"wa": [
 # Cleanup's carry-overs (precall-409 proposal, "Also"): decisions 460 and 456.
 ("Shows: AD Personal page 3fa19a301a7f81638e55d12684ccad16.", "Shows: AD Tasks page 3fa19a301a7f81638e55d12684ccad16 (was AD Personal, decision 460)."),
 ("(Show Internal, decision 376: transcripts to Ranjita, anything to Jaya or Sarika)", "(Show Internal, decision 376: transcripts to Mamatha (decision 456), anything to Jaya or Sarika)"),
 # B14: no community segment on Engagements.
 ("On the Engagement add Akshay to Waiting on and \"Akshay: invite <first name> to the FT Community. Blurb: <Engagement URL>\" to Next action, once. Reply",
  "No Engagement segment (Akshay, 5 Nov, item 20: the To invite list on his home is the only place). Reply"),
 (", and on their open Engagement add Akshay to Waiting on with \"Akshay: WhatsApp addition pending: add <first name> to the FT Community\" in Next action, once (decision 173).",
  ", and no Engagement segment (item 20)."),
],
"cap": [
 ("Next action \"Replacement proposal: <PR> offers <new person, role> in place of <original guest> (<original Status, Tier>). Eval pending. Write ok, not ok or a change in Your call.\"",
  "Next action \"Akshay: <PR> offers <new person> for <original guest>, eval pending (<D Mon>)\" (role, Status and Tier in the Claude note)"),
 # B15 (decision 409) and decision 456, same exemption line as Cleanup's precall-409 set.
 ("(Show Internal, decision 376: transcripts to Ranjita, anything to Jaya or Sarika) and rows a step below keys by its own Source ID (transcript:, precall:) stay Kind Task rows.",
  "(Show Internal, decision 376: transcripts to Mamatha (decision 456), anything to Jaya or Sarika) and rows a step below keys by its own Source ID (transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409)."),
 # B6: no loop-in when Zoya is already on the pitch.
 ("where nobody on our side (Akshay, Zoya, anyone tagged Team) has written on the thread (a \"Thanks for sharing, SG\" to Saurabh doesn't count),",
  "where nobody on our side (Akshay, Zoya, anyone tagged Team) has written on the thread (a \"Thanks for sharing, SG\" to Saurabh doesn't count) and zoya@myunnati.com is not already on the pitch's To or Cc (Akshay, 5 Nov, item 6: then capture only, with the Claude note line \"loop-in skipped: Zoya already on the pitch\"; Zoya replies from her inbox),"),
 ("with nobody from our side on the thread: the loop-in (LOOP-IN) on the thread,",
  "with nobody from our side on the thread and zoya@myunnati.com not already on its To or Cc (else no loop-in, item 6: the Claude note line \"loop-in skipped: Zoya already on the pitch\", and the Engagement below still gets its Zoya step): the loop-in (LOOP-IN) on the thread,"),
 # B2: the loop-in reply goes the draft way, never email_compose action reply.
 ("email_compose action reply on that message, inbox_id as above, reply_all false, To its sender, Cc set explicitly;",
  "a reply on that message, never email_compose action reply (Akshay, 5 Nov, item 2: a compose reply took the thread's last sender): draft action reply on it, inbox_id as above, draft update with To its sender and Cc set explicitly, draft_read, a Bash python assert on draft_read's actual To and Cc (To is that sender; zoya@myunnati.com in Cc; ad@thepodium.in on neither; the same check on an action send's to and cc before it goes), then draft send with the draft_id the update returned (a failed step: delete the draft, send nothing);"),
 ("no link, idempotency_key \"loopin:", "no link, idempotency_key (on the draft send or the action send) \"loopin:"),
],
"act": [
 # B15 (decision 409) and decision 456, same exemption line as Cleanup's precall-409 set.
 ("(Show Internal, decision 376: transcripts to Ranjita, anything to Jaya or Sarika) and rows a step below keys by its own Source ID (transcript:, precall:) stay Kind Task rows.",
  "(Show Internal, decision 376: transcripts to Mamatha (decision 456), anything to Jaya or Sarika) and rows a step below keys by its own Source ID (transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409)."),
 # B12: short Next action segments.
 ("Read the current Waiting on first and write back the full list.",
  "Read the current Waiting on first and write back the full list. NEXT ACTION SIZE (decision 438; Akshay, 5 Nov, item 15): each segment you write is at most about 120 characters (\"<owner>: <step> (<D Mon>)\"); the detail and the reason go in the Claude note; a segment the new one supersedes leaves in the same write; never \"Write ok, not ok or a change in Your call\"."),
 ("\"Akshay: <guest> (<show>) scheduling: <what came in>. Recommend: <one step: put the slots on <host>'s board | confirm <slot> and create the invite | ask for new windows>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)\"",
  "\"Akshay: <guest> (<show>) scheduling: <one step: put the slots on <host>'s board | confirm <slot> and create the invite | ask for new windows>? (<D Mon>)\" (what came in and why: the Claude note)"),
 ("\"Akshay: <who> wrote again about <what>; earlier <how it closed>. Recommend: <re-open as <status> and have Zoya send <the reply> | have Zoya reply no>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)\"",
  "\"Akshay: <who> wrote again (<what>, closed <how>): <re-open as <status> and have Zoya send <the reply> | have Zoya reply no>? (<D Mon>)\" (the detail and why: the Claude note)"),
 ("Next action \"Akshay: <brand> wants <what>. Proposed: <price and terms>. Reply draft in the page body. Write ok, not ok or a change in Your call.\"",
  "Next action \"Akshay: <brand> wants <what>, proposed <price> (draft in the page body) (<D Mon>)\"."),
 ("\"Akshay: <who> replied on your <D Mon> mail: <what, a few words>. Recommend: <one step>, because <one line>. Write ok, not ok or a change in Your call. (<D Mon>)\"",
  "\"Akshay: <who> replied on your <D Mon> mail: <what, a few words>. Recommend: <one step> (<D Mon>)\" (the reason: the Claude note)"),
 # B8: a themes ask inside a reply to Akshay's own mail is still Zoya's.
 ("Zoya gets only the holding reply (decision 390), and only when it asks something.",
  "Zoya gets only the holding reply (decision 390), and only when it asks something; a themes or questions ask before a recording in it is still hers (decision 453, Akshay, 5 Nov, item 10): also \"Zoya: send <guest> the themes once the prep note is in\" (the dossier routine picks the row up)."),
],
"dos": [
 # B1: 3 to 5 broad themes, never a mention of edit rights; existing FT notes rewritten once (v3).
 ("- Themes we'll cover: 5 or 6 broad themes, a few words each (",
  "- Themes we'll cover: 3 to 5 broad themes, one short line each, no running order, no sequence notes, no questions (Akshay, 5 Nov, item 1) ("),
 ("Never promise edit rights.", "Never mention edit rights, review or approval, in any form (item 1)."),
 ("whose Claude note has no line \"prep note v2\": rewrite", "whose Claude note has no line \"prep note v3\": rewrite"),
 ("\"YYYY-MM-DD: prep note v2\"", "\"YYYY-MM-DD: prep note v3\""),
 ("Soonest recording first, at most 3 per run;",
  "Also, first of all, any Engagement whose Next action has a Zoya step \"send <guest> the themes once the prep note is in\" (with or without an action key) and whose Prep note link is empty, whatever its Next date or dossier state (item 10): build its prep note (and the dossier if none). Then soonest recording first, at most 3 per run;"),
],
}

def run():
    global s
    for a, c in EDITS[which]:
        assert s.count(a) == 1, (which, a[:80], s.count(a))
        s = s.replace(a, c)
    assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
    ob = s.encode("utf-8")
    assert len(ob) <= 65536 - 200, (which, len(ob))
    open(out, "wb").write(ob)
    print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])

if __name__ == "__main__":
    run()
