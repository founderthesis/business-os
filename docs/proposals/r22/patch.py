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
GUARD = ("and nothing mirrors a Task row's ask onto a guest row.",
         "and nothing mirrors a Task row's ask onto a guest row. PAAS (Akshay, 6 Nov; decision 496): Engagements on Show PaaS are production-service rows: no guest step, eval, chase, status change or flag by guest rules; mail on them is logged and anything it asks goes to Akshay's list. A Deal whose Next action starts \"Moved to Engagements\" is retired: never flag, update or link to it; use its Engagement.")
LINKS = "podm.in/book, /30min, /thank-you, /guest-list, /community or /note"

EDITS = {
"cal": [
 EX,
 GUARD,
 # 497: Zoya sends the Human by Design day-before note; its recording link is fscd.ai/studio.
 ("on Founder Thesis, un# and Built to Share: from Zoya's inbox", "on Founder Thesis, un#, Built to Share and Human by Design (decision 497): from Zoya's inbox"),
 ("house copies (Akshay; Chaandini on Built to Share)", "house copies (Akshay; Chaandini on Built to Share and Human by Design)"),
 ("Human by Design stays a draft in Akshay's account (decision 313) until Akshay names its recording link. ", ""),
 ("Human by Design: a draft in Akshay's account, new mail, To the guest, Cc the main PR contact (Via), every other Stakeholder on the Engagement and the house copies, never Saurabh Garg and never a team member who has left. ", ""),
 ("Human by Design, the row's Call link;", "Human by Design, fscd.ai/studio (decision 497);"),
 ("on un# and Built to Share its \"Recording tomorrow (client show)\" toggle", "on un#, Built to Share and Human by Design its \"Recording tomorrow (client show)\" toggle"),
 ("The Human by Design draft is signed Akshay (Akshay, 12 Oct), {guest full name}, {company}.", "{guest full name}, {company}."),
 ("built2share.in/studio or unhashed.co/studio link", "built2share.in/studio, unhashed.co/studio or fscd.ai/studio link"),
 ("Studio: Built to Share is always built2share.in/studio; un# is unhashed.co/studio;", "Studio: Built to Share is always built2share.in/studio; un# is unhashed.co/studio; Human by Design is fscd.ai/studio (decision 497);"),
 # Prep entry lines (6/nov item 12: Ramakant Yadav's 6 Nov precall entry, created 5 Nov 22:38 JST without its Eval line and never updated).
 ("then the bos-key line last. Leave out lines with no value.",
  "then the bos-key line last. Take every value from a fresh fetch of the row (Guest LinkedIn from the guest's People row, which SQL can't read) and leave out only lines whose value is empty on the row."),
 ("- One exists but its description lacks a line for an Eval, Dossier, Prep note or LinkedIn link the Engagement now has, or shows a different one (compare the lines with the row every run, never a memory of an earlier run; the dossiers routine rebuilds dossiers, decision 127): update the description only,",
  "- One exists: every run, fetch the row fresh and, in a Bash python step, build the Eval, Dossier, Prep note and LinkedIn lines it should carry and compare them with the entry's description line by line (never by eye or from an earlier run; the dossiers routine rebuilds dossiers, decision 127). Any line the row has that the entry lacks, or shows differently: update the description only,"),
 ("- One exists and nothing changed: leave it.", "- One exists and that python check finds nothing to add or change: leave it. Each update adds a report line \"prep entry updated: <guest> <D Mon> (<lines added or changed>)\"."),
 ("STEP 5. REPORT\nShort and plain, no em dashes: ", "STEP 5. REPORT\nShort and plain, no em dashes: prep entries updated (STEP 3: guest, date, lines); "),
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
 ("Akshay, Zoya, Sarika, Sri,", "Akshay, Zoya, Sarika, Sri, Builder (the CTO round, decision 488),"),
 ("Nothing else goes on his list (a blocked delete, above, is the one step that does).",
  "Nothing goes on his list (a blocked delete goes to the CTO round, decision 488)."),
 # 493: the transcript ask is a segment on the guest row.
 (("Else create a Task row: Name \"Transcript:", "Source ID \"transcript:cal:<event id>\", Captured today."),
  "Else (decision 493, one entry per person) add on the guest's row the segment \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript\" (Founder Thesis: \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread\"), Zoya in Waiting on, Claude note line \"YYYY-MM-DD: transcript ask added (cal:<event id>)\", unless that key is already on the row. A recording with no guest row only: a Task row, Name \"Transcript: <company or title> (<FT|un#|B2S|HBD>, <D Mon> recording)\", Kind Task, Show Internal (40019a301a7f81d1a33fd4fba7cd920c), Task state Handed over, Waiting on Zoya, Next action \"Zoya: ask Mamatha for the transcript\", Next date today, Source Agent, Source ID \"transcript:cal:<event id>\", Captured today."),
 ("At most 5 new rows a run, oldest recording first. Report the rows created.", "At most 5 a run, oldest recording first. Report the asks added."),
],
"sweep": [
 EX,
 GUARD,
 # 492: a settled route stays settled; a conditional route is Zoya's ask.
 ("- Eval verdict Book immediately and no contrary word from Akshay:",
  "- A route Akshay already settled (his Your call, his mail, or a decision line in the Claude note on this eval) is never re-opened by a re-run eval: no new approval ask (decision 492). An eval route \"ask for X first, Y as fallback\" is Zoya's: \"Zoya: ask <PR or guest> for X (Y as fallback)\", Waiting on Zoya; Akshay only once their side declines X.\n- Eval verdict Book immediately and no contrary word from Akshay:"),
 # 493: 3i adds the ask on the guest row.
 (("Each needs one open Kind Task row asking for its transcript:", "else \"transcript:episode:<Episode page id>\", Captured today)."),
  "Each needs one open ask for its transcript, on its guest's row (decision 493): skip it if the Episode's Engagement has a segment \"Zoya [team transcript:<the Episode's recording key (its Source ID or \"Recording key:\" line, cal:<event id>, without the start time), else episode:<Episode page id>>]\", or any Engagement has Source ID \"transcript:\" plus that key or \"transcript:episode:<Episode page id>\" (an older Task row, which STEP 3a4 folds). Else add on the Episode's Engagement the segment \"Zoya [team transcript:<that key>]: ask Mamatha for the transcript\" (Founder Thesis: \"Zoya [team transcript:<that key>]: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread\"), Zoya in Waiting on, Claude note line \"YYYY-MM-DD: transcript ask added (<that key>)\". An Episode with no Engagement only: a Task row, Name \"Transcript: <company or title> (<show>, <D Mon> recording)\", Kind Task, Show Internal (40019a301a7f81d1a33fd4fba7cd920c), Task state Handed over, Waiting on Zoya, Next action \"Zoya: ask Mamatha for the transcript\", Next date today, Source Agent, Source ID \"transcript:\" plus that key, Captured today."),
 ("At most 10 a run, oldest Recording date first. Report the rows created.\n\nSTEP 3k.", "At most 10 a run, oldest Recording date first. Report the asks added.\n\nSTEP 3k."),
 # 491 and 493: one-time moves.
 ("\nSTEP 3b. LINK STRAY MAIL",
  "\nSTEP 3a4. ONE-TIME MOVES (every run until none is left; at most 20 rows a run for each of a and b).\n"
  "a. Owner moves (decision 491): an open \"Akshay:\" segment that is a promise to send an approved link or template (" + LINKS + ") or an ask a later decision gave Zoya (decision 464: Spotlight and sponsored-vs-Spotlight answers; 237: a Founder Thesis discount ask at our terms) becomes \"Zoya: <the same step>\", Zoya in Waiting on, Akshay off unless another of his segments stays (STEP 3a2's OWNERS), Claude note \"YYYY-MM-DD: step moved to Zoya (decision 491)\". Unsure: leave it, report it.\n"
  "b. Transcript Task rows (decision 493): each open Kind Task row with Source ID starting \"transcript:\" whose For engagement is a guest row. Its transcript already on the Episode: Task state Done, no segment. Else carry its ask onto that guest row as \"Zoya [team transcript:<its Source ID after transcript:>]: ask Mamatha for the transcript\" (its own Next action's words where they differ, and its date in the text when later than today; never twice for one key), Zoya in Waiting on, one Claude note line \"YYYY-MM-DD: transcript ask folded in from <the Task row's link>: <its newest note line>\"; read the guest row back. Then relink each of the Task row's Activities to the guest row (the transcript request mail above all, so the SLOW run never re-asks), and the Task row: Task state Done, Claude note \"folded into <guest row link> (decision 493)\", clear For engagement, confirm no relation is left, move it to Trash (decision 416). Report each fold.\n"
  "\nSTEP 3b. LINK STRAY MAIL"),
 ("PART A: STEPS 2, 3, 3r, 3a and 3a2.", "PART A: STEPS 2, 3, 3r, 3a, 3a2, 3a3 and 3a4."),
 ("Claude note and Claude updated.", "Claude note and Claude updated, and, in STEP 3a4 b only, a Task row's Task state, For engagement and Activities links, and its move to Trash (decision 416)."),
 ("transcript task rows created (STEP 3i)", "transcript asks added (STEP 3i)"),
 # Cleanup C2 (r22 verdict): the relink keeps the Activity's other links.
 ("Then relink each of the Task row's Activities to the guest row", "Then relink each of the Task row's Activities to the guest row (fetch its Engagement relation and write back every link it had, plus the guest row, less the Task row; read it back)"),
 ("Next action segments trimmed (STEP 3a3);", "Next action segments trimmed (STEP 3a3); one-time moves (STEP 3a4: steps moved to Zoya, transcript asks folded, by name);"),
 # CTO 7 Nov 10:20 JST, item 1 (Sweep B 6 Nov, Activity 41019a301a7f814b95bfe89c6b6d4d7c): status in code, STEP 4 cap with
 # carry-over, 3h b reads the Live line, rows still waiting on Mamatha move.
 ("Do only your part's steps, then STEP 7.",
  "Do only your part's steps, every one in full, then STEP 7. Size, row counts (\"about 80 rows\"), effort, context or cost never skip or shorten a step; only a measured time limit, a cap this prompt sets or a tool error leaves one unfinished (STEP 7's STATUS IN CODE)."),
 ('Summary "Sweep <A|B> <D Mon>: <Completed|Partial>"', 'Summary "Sweep <A|B> <D Mon>: <Completed|Partial|Failed>" (STEP 7\'s STATUS IN CODE)'),
 ("No eligible mail yet: leave it, that is \"live, awaiting observation\".",
  "No eligible mail yet: leave it, that is \"live, awaiting observation\". The Live date is the \"Live\" line of the row's page body (Mail issues has no Live property); a row with no dated Live line is left and reported as \"no Live line: <issue>\"."),
 ("Flag (skip if Next action already says the same thing):",
  "Flag (skip if Next action already says the same thing). GMAIL CAP (CTO, 7 Nov): the three checks that read Gmail (revenue safety net, quiet, promise lapsed) never skip. A Bash python step lists every row they select, once each: first the urls on the previous Part B report's \"step 4 carry-over:\" line, then by Last activity oldest first (empty first), then by url. Read at most 40 in that order; the rest is the carry-over, written on a body line \"step 4 carry-over: <n>: <urls>\" (none: \"step 4 carry-over: 0\"), and the step line is then \"step 4: unfinished (cap: 40 read, <n> carried over)\". The checks that read only fields run on every row:"),
 ("At most 20 a run; list them in the report.",
  "At most 20 a run; list them in the report. MAMATHA (TEAM ROLES; CTO, 7 Nov: un# LT chase rows still waited on her): every open Engagement on any show with Mamatha in Waiting on or a \"Mamatha:\" or \"Waiting on Mamatha\" segment, whether or not you touch it otherwise. A routine step (a chase or nurture, a link or template send, a transcript or Zencastr link ask) becomes \"Zoya: <the step>\" with Zoya in Waiting on; a decision becomes \"Akshay: <the step>\" with Akshay; Mamatha leaves Waiting on; Claude note \"YYYY-MM-DD: step moved off Mamatha to <who> (TEAM ROLES)\". At most 30 a run, oldest Claude updated first; report them by name and how many are left."),
 ('First line: "Sweep <A|B> <D Mon>: Completed" only when every step of your part ran; else "Sweep <A|B> <D Mon>: Partial: skipped <STEP>: <why>" for each one. A step that ran and changed nothing is done, not skipped; a step cut short is skipped.',
  'First line: "Sweep <A|B> <D Mon>: <status>" from STATUS IN CODE. Then one line per step of your part, in TWO PARTS\' order: "step <name>: done <n> | unfinished (minute 40 at <time> | cap: <what> | tool error: <tool> <error>)". A step is done only when every row it selects was handled; counting rows without handling them, sampling, or "too many rows" is not done. A step that ran and changed nothing is done. TIME: Bash `date -u` at the start of your part and before this write; a "stop: minute 40 at <date -u time>" line only when that much time has measurably passed, and the steps left are then unfinished (minute 40) and run first next time. STATUS IN CODE (CTO, 7 Nov): before the report\'s write, a Bash python step is given the body verbatim (quoted heredoc), parses the step lines, the "stop:" line and the two times, and prints the status: Completed only if every step of your part has a line and each is done; Partial "<step>: <reason>; ..." only when each unfinished step is minute 40 (with the stop line, 40 or more minutes after the start), a cap this prompt sets for that step, or a tool error with its tool and error text; anything else, or a step with no line, is Failed "early exit: <step>". The Summary and first line are copied from that output, never rewritten.'),
],
"cap": [
 EX,
 GUARD,
 # 489: Mamatha stays in Cc when she is on the message.
 ("Never Mamatha.", "Never add Mamatha; when she is on the From, To or Cc of the message you loop in on, she stays in Cc (decision 489)."),
],
"act": [
 EX,
 GUARD,
 # 496: Akshay's own mail clears a PaaS follow-up reminder.
 ("An item his mail does not settle stays.", "A PaaS reminder \"Akshay: follow up <name> ...\" (decision 496) is settled by any mail of his to that person on that thread: take it out (the next reminder counts from his mail). An item his mail does not settle stays."),
 ("it keeps STEP 5's decision 448 segment.", "it keeps STEP 5's decision 448 segment, or none (decision 490). Each segment a bucket writes also removes the \"Waiting on <same person>\" segment it answers (STEP 5)."),
 ("(a reply to his own mail still comes to him in that bullet's form)", "(a reply to his own mail follows that bullet, decision 490 included)"),
 # 490: a reply that needs nothing never reaches Akshay's list.
 ("Even a \"will revert\" or a mail with no ask: add Akshay",
  "A reply that needs nothing of him (thanks, an acknowledgement, a \"will revert\", agreeing to what was asked; decision 490, amending 448): Last activity and a Claude note line only, never his list. Anything that asks or needs something of him: add Akshay"),
 # Stale segments (the Dinesh and George case).
 ("After STEPS 3 and 4, set Waiting on and Next action on every Engagement or Deal you touched:",
  "After STEPS 3 and 4, set Waiting on and Next action on every Engagement or Deal you touched (a segment you write for someone's reply, an answer to it or a decision on it removes, in the same write, the \"Waiting on <same person>\" segment that reply answers and any follow-up or chase segment it settles; 6 Nov, Dinesh and George; a reply that declines X on a row whose Next action carries \"Zoya: ask <who> for X (Y as fallback)\", decision 492, goes on Akshay's list as \"Akshay: <who> declined X: go to Y? (<D Mon>)\"):"),
],
"wa": [
 EX,
 GUARD,
 # Cleanup C1 (r22 verdict): never a guessed country code.
 ("chat id = its digits with the country code, an Indian 10-digit number with 91 in front, then \"@c.us\".",
  "chat id = its digits with the country code, then \"@c.us\"; a People Phone stored without a country code (no leading + or 00): send nothing, replace the segment with \"Akshay: <name>'s WhatsApp number has no country code\", Akshay in Waiting on (never guess one)."),
 # 491: WhatsApp 0b shows the owner as the row has it.
 ("then one \"- <owner>: <promise>\" line each", "then one \"- <owner>: <promise>\" line each (the owner as the row has it: a promise to send an approved link or template is Zoya's, decision 491)"),
 # CTO 7 Nov 10:20 JST, item 2 (WhatsApp 09:45 7 Nov left STEP 3, 3d and 4, "ran out of effort"): status in code.
 ("STEP 3. FT COMMUNITY (decision 171; once a day, on the first run of the JST day)",
  "STEP 3. FT COMMUNITY (decision 171; due on the first run of the JST day, and on each later run until a run's report has \"step 3: done\" for today)"),
 ("STEP 3d. COMPLETE THE ROWS TO ADD (decision 309; every run, even when STEP 3 is skipped).",
  "STEP 3d. COMPLETE THE ROWS TO ADD (decision 309; every run, whatever else the run did, even when STEP 3 is not due)."),
 ("STEP 4. PUBLIC DIRECTORY MIRROR (decision 190; every run, even when STEP 3 is skipped)",
  "STEP 4. PUBLIC DIRECTORY MIRROR (decision 190; every run, whatever else the run did, even when STEP 3 is not due)"),
 ("STEP 5. REPORT\nPlain and short, no em dashes, no phone numbers: ",
  "STEP 5. REPORT\nFirst line \"WhatsApp <D Mon HH:MM> JST: <status>\" from STATUS IN CODE. Then one line per step, in this order: 0, 0d, 0w, 1, 2, 2b, 3, 3d, 4: \"step <name>: done <n> | not due | unfinished (minute 25 at <time> | cap: <what> | tool error: <tool> <error>)\". Every step runs every run (STEP 3 as its heading says); size, effort, context or cost never leave one. A step is done only when everything it selects was handled; a step that ran and changed nothing is done. TIME: Bash `date -u` at the start and before this report; a \"stop: minute 25 at <date -u time>\" line only when that much time has measurably passed. STATUS IN CODE (CTO, 7 Nov): a Bash python step is given these lines verbatim (quoted heredoc), parses the step lines, the \"stop:\" line and the two times, and prints the status: Completed only if every step has a line and each is done or not due; Partial \"<step>: <reason>; ...\" only when each unfinished step is minute 25 (with the stop line, 25 or more minutes after the start), a cap this prompt sets for that step, or a tool error with its tool and error text; anything else, or a step with no line, is Failed \"early exit: <step>\". The first line is copied from that output, never rewritten. Then, plain and short, no em dashes, no phone numbers: "),
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
