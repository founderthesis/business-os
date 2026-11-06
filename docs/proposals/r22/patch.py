"""r22 for the non-Zoya routines (decisions 486 and 488 to 495; CTO, 6 Nov ~11:30 JST). Zoya's part is
routines/zoya/r22_edits.py in the r22 build.
Usage: python3 patch.py <cal|sweep|cap|act|wa> <input> <out>
Inputs: cal, the live calendar (b-round-5nov/calendar.txt, 9dc4babe); sweep, the live sweep (sweep-468/sweep.txt,
6e3d6606); cap, the live capture (b-round-5nov/capture.txt, 72c4d81a); act and wa, the decision 486 builds
(wa-chase-486/patch.py on the live 459e4041 and 174d9317), so 486 rides in this round.
Each edit is asserted exactly once (a span edit: each marker once, end after start); no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"cal": "9dc4babe", "sweep": "6e3d6606", "cap": "72c4d81a", "act": "6a97144a", "wa": "9ef13725"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the expected %s input" % which
s = b.decode("utf-8")

EX = ("(Show Internal, decision 376: transcripts to Mamatha (decision 456), anything to Jaya or Sarika) and rows a step "
      "below keys by its own Source ID (transcript:) stay Kind Task rows; precall promises go on the guest's own row (decision 409).",
      "(Show Internal, decision 376: anything to Jaya or Sarika, and a transcript for a recording with no guest row) stay "
      "Kind Task rows; a guest's transcript ask and precall promises go on the guest's own row as segments (decisions 409, "
      "493), and nothing mirrors a Task row's ask onto a guest row.")
LINKS = "podm.in/book, /30min, /thank-you, /guest-list, /community or /note"

EDITS = {
"cal": [
 EX,
 # 495: un# has its own thank-you, C13u.
 ("Subject exactly \"Thank You <guest first name>!\" (the first name tells the team who the chain is about). Wording: C13 on Client show mails, its theme from the show's pitch sheet (SHOW CHECK), plain text plus html_body, one <p> per paragraph, no attachment, the transcript line kept so Akshay attaches it.",
  "Subject exactly \"Thank You <guest first name>!\" (the first name tells the team who the chain is about); on un# \"un# >> thank You <guest first name>!\". Wording: C13 on Client show mails, its theme from the show's pitch sheet (SHOW CHECK), plain text plus html_body, one <p> per paragraph, no attachment, the transcript line kept so Akshay attaches it. un# (decision 495, Akshay, 6 Nov): the toggle \"C13u Thank-you after recording (un#)\" instead, as written there (no transcript line, nothing attached), Sri always in Cc whatever the host line below says; no C13u toggle on the page yet: draft nothing for un#, report \"wording missing: C13u\"."),
 ("Then add Akshay to Waiting on and put \"Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts; attach the transcript)\" in Next action. Log \"Zoya drafted: client thank-you for <guest>\"",
  "Then add Akshay to Waiting on and put \"Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts; attach the transcript)\" in Next action (un#: \"Akshay: send the thank-you draft to <guest first name> (in your Gmail Drafts)\", never \"attach the transcript\"). Log \"Zoya drafted: client thank-you for <guest>\""),
 # 491: a promise to send an approved link or template is Zoya's, whoever made it.
 ("(Akshay for what he said he would do, Guest or PR for what their side owes, Zoya for a routine mail)",
  "(Zoya for any promise to send an approved link or template, " + LINKS + ", whoever made it on the call, decision 491; Akshay only for what only he can do; Guest or PR for what their side owes; Zoya for a routine mail)"),
 # 488: a blocked delete goes to the CTO round, not to Akshay.
 ("put \"Akshay: delete the <D Mon> <precall|recording> invite for <guest> (blocked: <error>)\" on the row with Akshay in Waiting on,",
  "put \"Builder: delete the <D Mon> <precall|recording> invite for <guest> (blocked: <error>)\" on the row with Builder in Waiting on (decision 488: the CTO round at 08:45 and 20:45 JST re-checks the written cancel and deletes it; an unclear case goes to Akshay in one line),"),
 ("Nothing else goes on his list (a blocked delete, above, is the one step that does).",
  "Nothing goes on his list (a blocked delete goes to the CTO round, decision 488)."),
 # 493: the transcript ask is a segment on the guest row.
 (("Else create a Task row: Name \"Transcript:", "Source ID \"transcript:cal:<event id>\", Captured today."),
  "Else (decision 493, one entry per person) add on the guest's row the segment \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript\" (Founder Thesis: \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread\"), Zoya in Waiting on, Claude note line \"YYYY-MM-DD: transcript ask added (cal:<event id>)\", unless that key is already on the row. A recording with no guest row only: a Task row, Name \"Transcript: <company or title> (<FT|un#|B2S|HBD>, <D Mon> recording)\", Kind Task, Show Internal (40019a301a7f81d1a33fd4fba7cd920c), Task state Handed over, Waiting on Zoya, Next action \"Zoya: ask Mamatha for the transcript\", Next date today, Source Agent, Source ID \"transcript:cal:<event id>\", Captured today."),
 ("At most 5 new rows a run, oldest recording first. Report the rows created.", "At most 5 a run, oldest recording first. Report the asks added."),
],
"sweep": [
 EX,
 # 492: a settled route stays settled; a conditional route is Zoya's ask.
 ("- Eval verdict Book immediately and no contrary word from Akshay:",
  "- A route Akshay already settled (his Your call, his mail, or a decision line in the Claude note on this eval) is never re-opened by a re-run eval: no new approval ask (decision 492). An eval route \"ask for X first, Y as fallback\" is Zoya's: \"Zoya: ask <PR or guest> for X (Y as fallback)\", Waiting on Zoya; Akshay only once their side declines X.\n- Eval verdict Book immediately and no contrary word from Akshay:"),
 # 493: 3i adds the ask on the guest row.
 (("Each needs one open Kind Task row asking for its transcript:", "else \"transcript:episode:<Episode page id>\", Captured today)."),
  "Each needs one open ask for its transcript, on its guest's row (decision 493): skip it if the Episode's Engagement has a segment \"Zoya [team transcript:<the recording key, else episode:<Episode page id>>]\", or any Engagement has Source ID \"transcript:\" plus that key or \"transcript:episode:<Episode page id>\" (an older Task row, which STEP 3a4 folds). Else add on the Episode's Engagement the segment \"Zoya [team transcript:<that key>]: ask Mamatha for the transcript\" (Founder Thesis: \"..., then send it to <guest> on the thank-you thread\"), Zoya in Waiting on, Claude note line \"YYYY-MM-DD: transcript ask added (<that key>)\". An Episode with no Engagement: a Task row as the calendar's STEP 4f gives for a recording with no guest row."),
 ("At most 10 a run, oldest Recording date first. Report the rows created.\n\nSTEP 3k.", "At most 10 a run, oldest Recording date first. Report the asks added.\n\nSTEP 3k."),
 # 491 and 493: one-time moves.
 ("\nSTEP 3b. LINK STRAY MAIL",
  "\nSTEP 3a4. ONE-TIME MOVES (every run until none is left; at most 20 rows a run for each of a and b).\n"
  "a. Owner moves (decision 491): an open \"Akshay:\" segment that is a promise to send an approved link or template (" + LINKS + ") or an ask a later decision gave Zoya (decision 464: Spotlight and sponsored-vs-Spotlight answers; 237: a Founder Thesis discount ask at our terms) becomes \"Zoya: <the same step>\", Zoya in Waiting on, Akshay off unless another of his segments stays (STEP 3a2's OWNERS), Claude note \"YYYY-MM-DD: step moved to Zoya (decision 491)\". Unsure: leave it, report it.\n"
  "b. Transcript Task rows (decision 493): each open Kind Task row with Source ID starting \"transcript:\" whose For engagement is a guest row. Its transcript already on the Episode: Task state Done, no segment. Else carry its ask onto that guest row as \"Zoya [team transcript:<its Source ID after transcript:>]: ask Mamatha for the transcript\" (its own Next action's words where they differ, and its date in the text when later than today; never twice for one key), Zoya in Waiting on, one Claude note line \"YYYY-MM-DD: transcript ask folded in from <the Task row's link>: <its newest note line>\"; read the guest row back. Then the Task row: Task state Done, Claude note \"folded into <guest row link> (decision 493)\", clear For engagement, confirm no relation is left, move it to Trash (decision 416). Report each fold.\n"
  "\nSTEP 3b. LINK STRAY MAIL"),
 ("Next action segments trimmed (STEP 3a3);", "Next action segments trimmed (STEP 3a3); one-time moves (STEP 3a4: steps moved to Zoya, transcript asks folded, by name);"),
],
"cap": [
 EX,
 # 489: Mamatha stays in Cc when she is on the message.
 ("Never Mamatha.", "Never add Mamatha; when she is on the From, To or Cc of the message you loop in on, she stays in Cc (decision 489)."),
],
"act": [
 EX,
 # 490: a reply that needs nothing never reaches Akshay's list.
 ("Even a \"will revert\" or a mail with no ask: add Akshay",
  "A reply that needs nothing of him (thanks, an acknowledgement, a \"will revert\", agreeing to what was asked; decision 490, amending 448): Last activity and a Claude note line only, never his list. Anything that asks or needs something of him: add Akshay"),
 # Stale segments (the Dinesh and George case).
 ("After STEPS 3 and 4, set Waiting on and Next action on every Engagement or Deal you touched:",
  "After STEPS 3 and 4, set Waiting on and Next action on every Engagement or Deal you touched (a segment you write for someone's reply, an answer to it or a decision on it removes, in the same write, the \"Waiting on <same person>\" segment that reply answers and any follow-up or chase segment it settles; 6 Nov, Dinesh and George):"),
],
"wa": [
 EX,
 # 491: WhatsApp 0b shows the owner as the row has it.
 ("then one \"- <owner>: <promise>\" line each", "then one \"- <owner>: <promise>\" line each (the owner as the row has it: a promise to send an approved link or template is Zoya's, decision 491)"),
],
}

for e in EDITS[which]:
    a, c = e
    if isinstance(a, tuple):
        st, en = a
        assert s.count(st) == 1 and s.count(en) == 1, (which, st[:50], s.count(st), en[:50], s.count(en))
        i, j = s.index(st), s.index(en)
        assert j > i, (which, "span order", st[:40])
        s = s[:i] + c + s[j + len(en):]
    else:
        assert s.count(a) == 1, (which, a[:70], s.count(a))
        s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, (which, len(ob))
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
