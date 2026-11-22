# Rulebook r1: the edits that turn the pinned prompts into the current rulebook.
# Each edit is (subject id, old text, new text). build.py applies them to the pinned
# bytes, asserts each old text occurs exactly once, and writes prompts/ plus a manifest.
# Subject ids match change-map.md. Plain ASCII where the source is ASCII; no em dashes.

# ---------------------------------------------------------------------------
# Shared current statements. Each is defined once here and written into every
# prompt that executes it, so one policy has one text.
# ---------------------------------------------------------------------------

STATUS_AUTHORITY = (
    "PARKED (decision 656). Only Akshay parks a row: his Your call, his own mail, his message in the Zoya group, "
    "or his answer on the Park proposals row. You never set Parked yourself, and nothing their side writes is a park: "
    "a no is They declined, a no-contact request is They declined plus the no-contact note. "
    "Where a rule ends a chase with nothing left to send, stop sending, leave Status as it is, set Waiting on to whoever "
    "holds the next move (Guest or PR, or Akshay if a decision of his is open), and add the row to this week's Park "
    "proposals: one Kind Task row in Engagements, Waiting on Akshay, Show AD Tasks, Source ID \"park:<Saturday date>\", "
    "one line per row (guest, reason, the date the chase ended). A Zoya step blocked past its date keeps that date "
    "unless something new has happened: it stays overdue and goes on the same list."
)

RECIPIENTS = (
    "RECIPIENTS (decisions 229, 586, 592, 643, 646, 647). One rule for every send and every draft, from either inbox, "
    "in every path (FAST, SLOW drafts, OUTBOX, loop-ins). "
    "1/ Reply on a thread with anyone outside the team: start from everyone on the thread's latest message (From, To, Cc). "
    "Remove only: your own address; addresses tagged \"Email bounced\" in People; People whose Role starts "
    "\"Ex-employee (mailbox dead)\"; Akshay's addresses other than ad@thepodium.in; Mamatha (on a long break, decision 646). "
    "Everyone else stays, whether or not they wrote: team members on it, Sri on un#, the host on Built to Share, Human by "
    "Design and Pathfinders, PR, comms and EAs. Then add whoever is missing of: Akshay (ad@thepodium.in) in Cc; Chaandini "
    "on Built to Share and Human by Design; Divir and Ankita Joshi on Pathfinders; Jaya and Sarika on revenue mail "
    "(sponsored from their yes onward: next steps, billing, invoices, payments; never expense mail); the guest or a "
    "company-side contact when the mail is guest-facing (the day-before note, prep note, recording link, reschedule, "
    "thank-you). "
    "2/ A new mail to someone outside the team (no thread exists): their side from the row and the step, plus the same "
    "additions. "
    "3/ Team-only mail (every recipient tagged Team): the team members only; never Akshay (decision 592), never Mamatha. "
    "Never add on your own: Sri or a host to a thread they are not on, Mamatha, Saurabh Garg (except decision 517's "
    "forwarded pitch). "
    "To is whoever's move it is; everyone else is in Cc; ad@thepodium.in is never in To; on outside mail no team address "
    "is in To. "
    "CHECK, before every send, in a Bash python step on the draft as read back (never by eye): build the required set from "
    "1/ to 3/, compare it with the draft's To and Cc (addresses only, case-insensitive), print both lists side by side, and "
    "assert they are equal and To is not empty. A difference on a reply draft: correct it once with draft action update "
    "(to, cc), which keeps the thread (decision 658), read it back and check again. Still different: delete the draft, "
    "send nothing, block the action \"recipients: <what differed>\"."
)

TEAM_ROLES = (
    "TEAM ROLES (decisions 226, 352, 646). Ranjita creates the Zencastr rooms for Founder Thesis recordings and sends you "
    "the links, downloads each Zencastr transcript and attaches it to the Episode's Transcript file herself, and publishes "
    "founderthesis.com features. Work for her is a \"Ranjita: <step>\" segment of Next action with Ranjita in Waiting on "
    "(her queue: the Engagements view \"Ranjita: my queue\"); you ask her on WhatsApp, one-to-one, opening \"Zoya ✨\", "
    "and chase once after 2 days. Jaya: invoices and payments. Sarika: edit feedback and release dates. Chaandini: Cc on "
    "Built to Share and Human by Design. Mamatha is on a long break: never mail, Cc, WhatsApp or ask her, never put her in "
    "Waiting on or Next action. A row still waiting on her moves to Ranjita (a room or transcript step), to Zoya (a "
    "routine step you run) or to Akshay (a decision), with a Claude note line."
)

# ---------------------------------------------------------------------------
# Edits per prompt file. (subject, old, new)
# ---------------------------------------------------------------------------

EDITS = {}

EDITS["zoya-fast.txt"] = [
    ("S3-recipients",
     "- Akshay still decides un# guests; Sri picks recording slots. Never mail or WhatsApp Sri, and Sri is never in Cc on routine mail, unless he wrote on that thread himself: then he stays in Cc.",
     "- Akshay still decides un# guests; Sri picks recording slots. Never start a mail or WhatsApp to Sri and never add him to a thread; when he is on a thread's latest message he stays (RECIPIENTS)."),
    ("S3-recipients",
     "Never mail or WhatsApp the host, and the host is never in Cc on routine mail, unless the host wrote on that thread: then they stay in Cc.",
     "Never start a mail or WhatsApp to the host and never add them to a thread; when the host is on a thread's latest message they stay (RECIPIENTS)."),
    ("S4-ranjita",
     " Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Waiting on with Zoya and rewrite her step as yours when it is a step you run; a cold-outreach step is never yours, so leave that row as found and list it in the report.",
     " TEAM ROLES says who owns what; a row you touch that still waits on Mamatha moves as it says."),
    ("S3-recipients",
     ", and that To and Cc together hold everyone on the latest inbound, its From, To and Cc, less your own address, bounced addresses, Akshay's other addresses, Mamatha unless she is on the From, To or Cc of the message you reply to (then she stays in Cc, decision 489), on un#, Sri, and on Built to Share and Human by Design the host, unless they wrote on the thread themselves (then they are added back if missing), and anyone who handed over anywhere on the thread (a message saying a new contact takes over, the new contact on the thread since), plus Akshay; the read-back fails if any of those excluded is still on it; a handover that names the new contact also sets Via to them on the row), then send it;",
     ", and RECIPIENTS' check on its To and Cc; someone who handed over on the thread (a message saying a new contact takes over) is replaced by the new contact, and that handover also sets Via to them on the row), then send it;"),
    ("S3-recipients",
     " To: whoever's move it is (the person you're asking); move everyone else to Cc, Akshay included. Guest-facing mail",
     " To and Cc: RECIPIENTS. Guest-facing mail"),
    ("S3-recipients",
     " Cc: Akshay (ad@thepodium.in) on every mail you send, permanently until he says otherwise; never his other addresses in To or Cc: rebuild a reply's recipients without them; never add Mamatha (she stays in Cc only when she is on the From, To or Cc of the message you reply to or loop in on, decision 489; nothing waits on her); on revenue mail (sponsored from the guest's yes onward: next steps, billing, invoices, payments) also Jaya and Sarika (addresses from their People rows; not on expense mail). Saurabh Garg never, except decision 517:",
     " Saurabh Garg never, except decision 517:"),
    ("S5-senders",
     "Send the loop-in instead, from Akshay's inbox (inbox_id cd37e47e-89d8-4259-b907-9a243baf7048): always the draft way, never email_compose reply's own addressing: draft action reply on the latest message from the person you address (that person never wrote on it, a new contact after a handover: on the thread's latest message) (first delete any loop-in draft already on it, draft_list), draft update to set To and Cc, draft_read and the python assert on its actual To and Cc (NO COMPOSE REPLY), draft send with the draft_id the update returned; a step that fails: delete the draft. Either way include_signature false,",
     "Send the loop-in instead, from Akshay's inbox (inbox_id cd37e47e-89d8-4259-b907-9a243baf7048), with email_compose action reply on the latest message from the person you address (that person never wrote on it, a new contact after a handover: on the thread's latest message), to and cc passed explicitly: To that person, Cc everyone else RECIPIENTS 1/ keeps plus Zoya. Never the MCP Emails draft tool on ad@thepodium.in: it stops on a permission prompt. RECIPIENTS' check runs on the to and cc you are about to pass, in a Bash python step, before the call. include_signature false,"),
    ("S4-ranjita",
     "our side wrote last (a chase from Mamatha, say): \"adding @Zoya to coordinate further\", no thanks.",
     "our side wrote last (a chase from the team, say): \"adding @Zoya to coordinate further\", no thanks."),
    ("S4-ranjita",
     "Every run, read the mails in your inbox from Mamatha (tagged Team) in the last 14 days that carry Zencastr room links (either SENDING form) (a line with two links, or one marked host: send nothing, report it). Each link line names a guest and company; a later line from Mamatha for the same guest and recording replaces an earlier one (her correction):",
     "Every run, read Ranjita's messages from the last 14 days that carry Zencastr room links (either SENDING form): her mail to you, her one-to-one WhatsApp chat and the Zoya <> Team group (a line with two links, or one marked host: send nothing, report it). Each link line names a guest and company; a later line from her for the same guest and recording replaces an earlier one (her correction):"),
    ("S4-ranjita",
     "(ACTIONS; its Sent check runs from the arrival of Mamatha's mail, not the key's time;",
     "(ACTIONS; its Sent check runs from the arrival of Ranjita's link, not the key's time;"),
    ("S4-ranjita",
     "with no room link anywhere (Mamatha's mails and WhatsApp chat, the invite, Call link, Recording link) and no \"room asked\" note: one WhatsApp to Mamatha (Blueticks, her one-to-one chat; opens \"Zoya ✨\") listing them all, soonest first, \"<guest>, <D Mon HH:MM IST, or date open>\"; on each row the note \"room asked <date>\" and \"Zoya: room from Mamatha for <guest> (asked <D Mon>)\" in place of any ask-Mamatha segment.",
     "with no room link anywhere (Ranjita's mail, WhatsApp chat and the Zoya <> Team group, the invite, Call link, Recording link) and no \"room asked\" note: one WhatsApp to Ranjita (Blueticks, her one-to-one chat; opens \"Zoya ✨\") listing them all, soonest first, \"<guest>, <D Mon HH:MM IST, or date open>\"; on each row the note \"room asked <date>\", Ranjita added to Waiting on, and the segment \"Ranjita: create <guest>'s Zencastr room and send Zoya the link (recording <D Mon>)\" in place of any older room segment. When her link is handled, remove her segment and take her off Waiting on (OWNERS)."),
    ("S4-ranjita",
     "No link 24 hours after the ask: one reminder (note \"room reminded\").",
     "No link 2 days after the ask: one reminder on WhatsApp (note \"room reminded\")."),
    ("S5-senders",
     "- NO COMPOSE REPLY: never call email_compose with action reply, from either inbox. Every reply is:",
     "- NO COMPOSE REPLY: from your inbox, never call email_compose with action reply (the ad@thepodium.in loop-in is the one exception: SENDING). Every reply from your inbox is:"),
    ("S3-recipients",
     " 2/ recipients from the latest inbound's own headers (From, To, Cc) and the row (no inbound yet: the row and the thread's last message, if any), built into To and Cc before the draft and checked in a Bash python step, never by eye: To is not empty; ad@thepodium.in and every team address (People tagged Team) are never in To; every outside address meant to get the mail (that inbound's From, To and Cc less bounced, excluded and handed-over ones, plus the guest-facing rule's) is in To or Cc; a failed assert: send nothing, the action blocked \"recipients: <what failed>\";",
     " 2/ RECIPIENTS' check;"),
    ("S4-ranjita",
     "- No WhatsApp in FAST work but ROOM ASK to Mamatha; SLOW work: only to the team members TEAM WHATSAPP names.",
     "- No WhatsApp in FAST work but ROOM ASK to Ranjita; SLOW work: only to the team members TEAM WHATSAPP names.\n- " + RECIPIENTS + "\n- " + TEAM_ROLES + "\n- " + STATUS_AUTHORITY),
]

EDITS["zoya-slow-work.txt"] = [
    ("S3-recipients",
     "- Akshay still decides un# guests; Sri picks recording slots. Never mail or WhatsApp Sri, and Sri is never in Cc on routine mail, unless he wrote on that thread himself: then he stays in Cc.",
     "- Akshay still decides un# guests; Sri picks recording slots. Never start a mail or WhatsApp to Sri and never add him to a thread; when he is on a thread's latest message he stays (RECIPIENTS)."),
    ("S4-ranjita",
     "internal team requests (Show Internal, decision 376: transcripts to Mamatha (decision 456), anything to Jaya or Sarika)",
     "internal team requests (Show Internal, decision 376: anything to Ranjita, Jaya or Sarika)"),
    ("S4-ranjita",
     "team (Jaya, Sarika, Mamatha's transcripts, internal asks, payments, billing asks, vendor Your call steps) are SLOW's.",
     "team (Jaya, Sarika, Ranjita's transcript chase, internal asks, payments, billing asks, vendor Your call steps) are SLOW's."),
    ("S4-ranjita",
     " Nothing waits on Mamatha (decision 352): on any row you touch, replace her in Waiting on with Zoya and rewrite her step as yours when it is a step you run; a cold-outreach step is never yours, so leave that row as found and list it in the report.",
     " TEAM ROLES says who owns what; a row you touch that still waits on Mamatha moves as it says."),
    ("S4-ranjita",
     "a guest row with a segment \"Zoya [team transcript:<recording key>]: ask Mamatha for the transcript...\"",
     "a guest row with a segment \"Zoya [team transcript:<recording key>]: ask Ranjita for the transcript...\" or \"Ranjita: download <guest>'s Zencastr transcript...\""),
    ("S4-ranjita",
     "or on Ranjita from before decision 456 (take it: Waiting on Zoya, and her earlier ask is not this request).",
     "or on Ranjita."),
    ("S4-ranjita",
     "Not found, not before the day after the recording, and no transcript request to Mamatha linked to the row yet (an Email out Activity to her; a retry never resends): send the transcript request from your inbox in that wording, To Mamatha (decision 456), Cc Akshay (addresses from their People rows, tagged Team), naming the guest, company and recording date; then Waiting on Zoya (nothing waits on Mamatha, decision 352), Next action \"Zoya: transcript from Mamatha for <guest>'s <D Mon> recording (asked <D Mon>)\", Next date 2 working days after the send (on a guest row: rewrite only its transcript segment, \"Zoya [team transcript:<key>]: transcript from Mamatha for <guest>'s <D Mon> recording (asked <D Mon>) on <D Mon, 2 working days on>\", never the row's Next date or another segment); on that date with no transcript, one follow-up on the request thread To Mamatha, Cc Akshay, Next date 2 working days on; still none on that date: Akshay's list, \"Akshay: no transcript from Mamatha for <guest>'s <D Mon> recording\", no more follow-ups, Activity \"Zoya sent: transcript request for <guest>\" (Kind Email out, Source ID per MESSAGE IDENTITY, Action key on a send receipt, linked to the row).",
     "Not found, not before the day after the recording, and no ask to Ranjita on the row yet: the ask is the segment \"Ranjita: download <guest>'s Zencastr transcript and attach it to the Episode's Transcript file (<Episode link>)\" with Ranjita in Waiting on (on a guest row it replaces only its transcript segment, never the row's Next date or another segment), plus one WhatsApp to her per TEAM WHATSAPP that names the guest, company, recording date and Episode link; log \"Zoya sent: transcript ask to Ranjita for <guest>\" (Kind WhatsApp, Action key). un# and Zencastr-only recordings she can't reach: \"Akshay: download the Zencastr transcript for <guest>\" on his list instead. 2 days after the ask with no Transcript file on the Episode: one WhatsApp chase (note \"transcript chased\"); still none 2 days later: Akshay's list, \"Akshay: no transcript yet for <guest>'s <D Mon> recording (Ranjita asked <D Mon>)\", no more chases. A Transcript file now on the Episode closes her segment (remove it and her Waiting on entry)."),
    ("S4-ranjita",
     "when a .txt, .docx or .pdf transcript reaches your inbox from Mamatha on any thread, the request thread or not (decision 456), or a found one:",
     "when a .txt, .docx or .pdf transcript reaches you from Ranjita (mail or WhatsApp) instead of being attached by her, or a found one:"),
    ("S4-ranjita",
     "attach nothing, Akshay's list \"Akshay: <file name> from Mamatha doesn't fit <guest>'s recording (<why>)\", the item blocked;",
     "attach nothing, Akshay's list \"Akshay: <file name> doesn't fit <guest>'s recording (<why>)\", the item blocked;"),
    ("S4-ranjita",
     "\"Akshay: no transcript for <guest>'s <D Mon> recording (<what Mamatha said>)\"",
     "\"Akshay: no transcript for <guest>'s <D Mon> recording (<what Ranjita said>)\""),
    ("S3-recipients",
     ", and that To and Cc together hold everyone on the latest inbound, its From, To and Cc, less your own address, bounced addresses, Akshay's other addresses, Mamatha unless she is on the From, To or Cc of the message you reply to (then she stays in Cc, decision 489), on un#, Sri, and on Built to Share and Human by Design the host, unless they wrote on the thread themselves (then they are added back if missing), and anyone who handed over anywhere on the thread (a message saying a new contact takes over, the new contact on the thread since), plus Akshay; the read-back fails if any of those excluded is still on it; a handover that names the new contact also sets Via to them on the row), then send it;",
     ", and RECIPIENTS' check on its To and Cc; someone who handed over on the thread (a message saying a new contact takes over) is replaced by the new contact, and that handover also sets Via to them on the row), then send it;"),
    ("S3-recipients",
     " Cc: Akshay (ad@thepodium.in) on every mail you send, permanently until he says otherwise; never his other addresses in To or Cc: rebuild a reply's recipients without them; never add Mamatha (she stays in Cc only when she is on the From, To or Cc of the message you reply to or loop in on, decision 489; nothing waits on her); on revenue mail (sponsored from the guest's yes onward: next steps, billing, invoices, payments) also Jaya and Sarika (addresses from their People rows; not on expense mail).",
     " To and Cc: RECIPIENTS."),
    ("S4-ranjita",
     "our side wrote last (a chase from Mamatha, say): \"adding @Zoya to coordinate further\", no thanks.",
     "our side wrote last (a chase from the team, say): \"adding @Zoya to coordinate further\", no thanks."),
    ("S4-ranjita",
     "a transcript file from Mamatha \"transcript-file:<Message-ID>:<file name>\"",
     "a transcript file sent to you \"transcript-file:<Message-ID>:<file name>\""),
    ("S4-ranjita",
     "the prep note, recording link, room ask to Mamatha (decision 558) and day-before note are the hourly task's",
     "the prep note, recording link, room ask to Ranjita (decision 558) and day-before note are FAST's"),
    ("S7-builder",
     "create a Task row in Engagements: Name \"MI: <issue, short>\", Kind Task, Waiting on Builder, Task state Handed over, Next action \"Builder: <the prompt change>\", For engagement = the guest's row if the issue is about one, Source Agent, Captured today, its page body linking the Mail issues row.",
     "send the prompt change to the CTO session (send_message, session_015wSc87F8WCdJKB91Tm34tJ) naming the Mail issues row; engineering work lives on the Build board, never as an Engagements row (decision 655)."),
    ("S8-oneoffs",
     None, None),  # STEP 0f owner mail: removed whole, see REMOVE_LINES
    ("S2-sponsored",
     "- 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says (a plan written as \"Waiting on <name>: reply to the sponsored offer\" is still a sponsored row). Read the thread first: a decline of the paid route from their side gets the close note, Status They declined, and no chase, whatever the plan says.",
     "- 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says (a plan written as \"Waiting on <name>: reply to the sponsored offer\" is still a sponsored row). The sponsored table on Rules for Zoya: follow-ups decides, for every show, whether a mail is due at all: interest first, the follow-up count with earlier sends included, pauses and stops. No interest shown: no mail; drop any \"Zoya: sponsored step <n>\" segment, Waiting on Guest or PR. Read the thread first: a decline of the paid route from their side gets the close note, Status They declined, and no chase, whatever the plan says."),
    ("S2-sponsored",
     "UN# SPONSORED (decision 422; the number on Cadences): a un# row whose thread has our sponsored offer (the first mail linking unhashed.co/sponsored). At most 2 follow-ups after the offer, counting every chase on the thread by anyone (Mamatha, Zoya or ad@; not loop-ins or answers to their questions); a template change, deploy or Chase step reset never adds more. When the next step after follow-up 2 falls due with no reply from their side: send nothing, Status Unresponsive (see the end), note \"YYYY-MM-DD: un# sponsored follow-ups done (decision 422)\"; never nurture, revival or a last check.",
     "UN# SPONSORED (decision 422): a un# row whose thread has our sponsored offer (the first mail linking unhashed.co/sponsored), under the same table. Every chase on the thread by anyone counts toward its limit (not loop-ins or answers to their questions); a template change, deploy or Chase step reset never adds more. When the next step after the last follow-up falls due with no reply from their side: send nothing, Status Unresponsive, note \"YYYY-MM-DD: un# sponsored follow-ups done (decision 422)\"; never nurture, revival or a last check."),
    ("S2-sponsored",
     "(NURTURE; UN# SPONSORED rows follow their own rule instead)",
     "(NURTURE; sponsored rows follow the sponsored table instead and never move to nurture)"),
    ("S2-sponsored",
     "the routine's span is over, counted from the latest real reply from their side (or our first ask if they never replied); a sponsored lead has had no reply from their side for 60 days or more (for sponsored rows this is the only time rule; a reply restarts it); or our last message on the thread is a close-out",
     "the routine's span is over, counted from the latest real reply from their side (or our first ask if they never replied); or our last message on the thread is a close-out"),
    ("S2-sponsored",
     "A sponsored thread gets no fresh restart (no step R; a row still planned as step R goes to nurture instead).",
     "A sponsored thread gets no fresh restart (no step R)."),
    ("S2-sponsored",
     "When a routine runs out (last step, span over, 60 silent days on sponsored, our last mail a close-out, 3 unanswered chases)",
     "When a routine other than sponsored runs out (last step, span over, our last mail a close-out, 3 unanswered chases)"),
    ("S6-sweep",
     "REVIVAL: a closed row (Unresponsive, or LT chase gone silent) is followed up again only after the daily sweep moved it to nurture from a \"revival checked <date> (cleanup): eligible\" line in its Claude note.",
     "REVIVAL: a closed row (Unresponsive, or LT chase gone silent) is followed up again only once its Claude note has a \"revival checked <date> (cleanup): eligible\" line; you start its nurture yourself (NURTURE's move, within the nurture cap on Cadences)."),
    ("S6-sweep",
     "(Zoya)\" (the sweep's never count);",
     "(Zoya)\";"),
    ("S3-recipients",
     "- PRE-SEND CHECKS, FAST and SLOW",
     "- " + RECIPIENTS + "\n- " + TEAM_ROLES + "\n- " + STATUS_AUTHORITY + "\n- PRE-SEND CHECKS, FAST and SLOW"),
]

EDITS["zoya-fast.txt"] += [
    ("S4-ranjita",
     "team (Jaya, Sarika, Mamatha's transcripts, internal asks, payments, billing asks, vendor Your call steps) are SLOW's.",
     "team (Jaya, Sarika, Ranjita's transcript chase, internal asks, payments, billing asks, vendor Your call steps) are SLOW's."),
]

LOOPIN_OLD = EDITS["zoya-fast.txt"][6][1]
LOOPIN_NEW = EDITS["zoya-fast.txt"][6][2]
NOCOMPOSE_OLD = "- NO COMPOSE REPLY: never call email_compose with action reply, from either inbox. Every reply is:"
NOCOMPOSE_NEW = "- NO COMPOSE REPLY: from your inbox, never call email_compose with action reply (the ad@thepodium.in loop-in is the one exception: SENDING). Every reply from your inbox is:"
PRESEND2_OLD = EDITS["zoya-fast.txt"][13][1]

EDITS["zoya-slow-work.txt"] += [
    ("S3-recipients",
     "Never mail or WhatsApp the host, and the host is never in Cc on routine mail, unless the host wrote on that thread: then they stay in Cc.",
     "Never start a mail or WhatsApp to the host and never add them to a thread; when the host is on a thread's latest message they stay (RECIPIENTS)."),
    ("S5-senders", LOOPIN_OLD, LOOPIN_NEW),
    ("S5-senders", NOCOMPOSE_OLD, NOCOMPOSE_NEW),
    ("S3-recipients", PRESEND2_OLD, " 2/ RECIPIENTS' check;"),
]

EDITS["zoya-slow.txt"] = [
    ("S5-senders", NOCOMPOSE_OLD, NOCOMPOSE_NEW),
    ("S3-recipients", PRESEND2_OLD, " 2/ RECIPIENTS' check (in the SLOW work file);"),
]

EDITS["zoya-slow.txt"] += [
    ("S6-sweep",
     "it runs at 00:08, 08:08, 11:08, 14:08, 17:08, 20:08 and 23:08 JST on weekdays (decision 546),",
     "it runs at 11:08 and 17:08 JST on weekdays (decision 657),"),
    ("S0-release",
     "git fetch origin refs/heads/zoya-slow-pin; git show 63d63ec2ef9211dbc6a6b77b388aa57f96201d1f:routines/zoya/release/zoya-slow-work.txt > /tmp/zoya-slow-work.txt; its sha256 (sha256sum) must start 78332307d8ba3cfd.",
     "git fetch origin {SLOW_WORK_COMMIT}; git show {SLOW_WORK_COMMIT}:docs/proposals/rulebook-r1/prompts/zoya-slow-work.txt > /tmp/zoya-slow-work.txt; its sha256 (sha256sum) must start {SLOW_WORK_SHA16}."),
    ("S0-release", "total = 94,829 characters", "total = {SLOW_WORK_CHARS} characters"),
]

EDITS["calendar.txt"] = [
    ("S4-ranjita",
     "Never set Waiting on Mamatha or write \"Mamatha:\".",
     "Mamatha is on a long break: never put her in Waiting on or Next action, never mail or Cc her (decision 646)."),
    ("S4-ranjita",
     "unless already on To or Cc; addresses from People rows; never Mamatha.",
     "unless already on To or Cc; addresses from People rows; never Mamatha (decision 646)."),
    ("S7-builder",
     "Akshay, Zoya, Sarika, Sri, Builder (the CTO round, decision 488), ...;",
     "Akshay, Zoya, Sarika, Ranjita, Sri, ...; never Builder, which is retired (decision 655);"),
    ("S4-ranjita",
     "\"no recording link yet (Zoya's STEP 0r asks Mamatha, and Akshay within 24 hours, decision 445)\"",
     "\"no recording link yet (Zoya's STEP 0r asks Ranjita, and Akshay within 48 hours, decisions 558, 646)\""),
    ("S7-builder",
     "A delete the tool refuses or a permission prompt blocks (Akshay, 5 Nov, item 8): still do the row part below now, put \"Builder: delete the <D Mon> <precall|recording> invite for <guest> (blocked: <error>)\" on the row with Builder in Waiting on (decision 488: the CTO round at 08:45 and 20:45 JST re-checks the written cancel and deletes it; an unclear case goes to Akshay in one line),",
     "Never call delete_event on an event with guests (decision 609: it stops on a permission prompt): do the row part below now, put \"Akshay: delete the <D Mon> <precall|recording> invite for <guest> (blocked: auto mode)\" on the row with Akshay in Waiting on, and send_message the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the event, guest and the written cancel (decision 488: the CTO round re-checks the cancel, deletes the event and clears the segment; an unclear case stays with Akshay),"),
    ("S4-ranjita",
     "add on the guest's row the segment \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript\" (Founder Thesis: \"Zoya [team transcript:cal:<event id>]: ask Mamatha for the transcript, then send it to <guest> on the thank-you thread\"), Zoya in Waiting on,",
     "add on the guest's row the segment \"Zoya [team transcript:cal:<event id>]: ask Ranjita for the transcript\" (Founder Thesis: \"Zoya [team transcript:cal:<event id>]: ask Ranjita for the transcript, then send it to <guest> on the thank-you thread\"), Zoya in Waiting on,"),
    ("S4-ranjita",
     "Next action \"Zoya: ask Mamatha for the transcript\", Next date today,",
     "Next action \"Zoya: ask Ranjita for the transcript\", Next date today,"),
]

TEAM_ROLES_OLD = "TEAM ROLES (decisions 154, 223, 352). Nothing waits on Mamatha: never set Waiting on Mamatha or write \"Mamatha:\" on any row. Waiting on holds Akshay (a decision only he can make: \"Akshay: <step>\"), Zoya (every routine mail step: \"Zoya: <step>\"), a host, or Guest or PR."
TEAM_ROLES_NEW = "TEAM ROLES (decisions 154, 223, 646). Waiting on holds Akshay (a decision only he can make: \"Akshay: <step>\"), Zoya (every routine mail step: \"Zoya: <step>\"), Ranjita (a room, transcript or feature-publishing step: \"Ranjita: <step>\"), a host, or Guest or PR. Mamatha is on a long break: never put her in Waiting on or Next action."

EDITS["inbox-actions.txt"] = [("S4-ranjita", TEAM_ROLES_OLD, TEAM_ROLES_NEW)]
EDITS["inbox-capture.txt"] = [
    ("S4-ranjita", TEAM_ROLES_OLD, TEAM_ROLES_NEW),
    ("S4-ranjita",
     "our side wrote last (a chase from Mamatha, say): \"adding @Zoya to coordinate further\", no thanks.",
     "our side wrote last (a chase from the team, say): \"adding @Zoya to coordinate further\", no thanks."),
    ("S3-recipients",
     "Never add Mamatha; when she is on the From, To or Cc of the message you loop in on, she stays in Cc (decision 489).",
     "Recipients follow RECIPIENTS in the Zoya prompt: everyone on the message you loop in on stays, less bounced and dead addresses and Mamatha (decision 646)."),
]
EDITS["whatsapp.txt"] = [
    ("S4-ranjita", "Never set Waiting on Mamatha (decision 352).", "Never put Mamatha in Waiting on (decision 646)."),
]

BOOKING_OLD = "\"you can pick any slot available on this link: podm.in/30min\"; never a paragraph"
BOOKING_NEW = "\"you can book a 30-minute planning call with Akshay here: podm.in/30min\" (decision 569: podm.in/30min is always named as a 30-minute planning call with Akshay); never a paragraph"
for _f in ("zoya-fast.txt", "zoya-slow.txt", "zoya-slow-work.txt"):
    EDITS[_f].append(("S0-carried-569", BOOKING_OLD, BOOKING_NEW))

PAUSE = (
    "PAUSES ON THEIR WORD (Rules for Zoya: follow-ups, sponsored and pause table, is the master). Read their side's last mail before any chase. "
    "\"We'll reach out when ready\" (as and when, will get back, we'll reach out, will revert once): send nothing for 30 days from that mail, "
    "then at most one short warm check-in on the primary thread, then nothing unless they write; that row goes on the Park proposals (PARKED). "
    "\"Seems difficult\" or \"not the right time\": the decision 550 reply, then one check-in 3 months out. \"Waiting for internal approval\": "
    "the decision 551 reply, then their date. A date they name always wins. A pause covers every chase on that row, the Tier 1 recording chase included (decision 625)."
)
EDITS["zoya-slow-work.txt"] += [
    ("S2-sponsored",
     "- 3 Recording slot: Status Booking, no recording on the calendar. On un#, every 2 working days (PR COORDINATION).",
     "- 3 Recording slot: Status Booking, no recording on the calendar. On un#, every 2 working days (PR COORDINATION). "
     "On Founder Thesis only Tier 1 rows are chased, and a Sponsored row only after their yes to the sponsored appearance "
     "(decisions 594, 618); any other FT row at Booking gets no slot follow-up: at its next touch drop its \"Zoya: recording step <n>\" "
     "segment, Waiting on Guest or PR, Claude note \"YYYY-MM-DD: no recording chase, Tier <x>\"; Status stays Booking and a reply "
     "from their side is handled as usual. No Founder Thesis slot ask (podm.in/book) before a precall with Akshay has happened, "
     "unless he said in writing to skip it (decision 654).\n" + PAUSE),
]

# Whole lines removed from a file (subject, line prefix that must match exactly one line).
REMOVE_LINES = {
    "zoya-slow-work.txt": [
        ("S8-oneoffs", "STEP 0f. OWNER MAIL. Once a day,"),  # decision 619
    ],
}
