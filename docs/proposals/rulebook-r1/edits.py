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
    "RECIPIENTS (decisions 229, 586, 592, 643, 646, 647). One rule for every send and draft, both inboxes, every path (FAST, SLOW drafts, OUTBOX, loop-ins). "
    "1/ Reply on a thread with outsiders: everyone on its latest message (From, To, Cc), less only your own address, People tagged \"Email bounced\", "
    "People whose Role starts \"Ex-employee (mailbox dead)\", Akshay's addresses other than ad@thepodium.in, and Mamatha (on a long break). Everyone else stays, "
    "wrote or not: team members, Sri, client-show hosts, PR, comms, EAs. Then add whoever is missing of: Akshay (ad@thepodium.in) in Cc; Chaandini on "
    "Built to Share and Human by Design; Divir and Ankita Joshi on Pathfinders; Jaya and Sarika on revenue mail (sponsored from their yes on: next steps, "
    "billing, invoices, payments; never expenses); the guest or a company-side contact on guest-facing mail (day-before, prep note, recording link, "
    "reschedule, thank-you). 2/ New mail to outsiders: their side from the row and the step, plus the same additions. 3/ Team-only mail: the team members "
    "only, never Akshay (592), never Mamatha. Never add on your own Sri or a host to a thread they're not on, Mamatha, or Saurabh Garg (except decision 517). "
    "To is whoever's move it is, the rest Cc; ad@thepodium.in never in To; no team address in To on outside mail. "
    "CHECK before every send, in a Bash python step on the draft as read back: build the required set from 1/ to 3/, print it beside the draft's To and Cc "
    "(addresses, case-insensitive), assert equal and To not empty. A reply draft that differs gets one draft action update (to, cc), which keeps the thread "
    "(decision 658), then a re-read and a second check; still different: delete it, send nothing, block \"recipients: <what differed>\"."
)

FAST_PARKED = (
    "PARKED (decision 656). Never set Parked: only Akshay parks (his Your call, mail or Zoya-group message). Their side's no is They declined, a no-contact request They declined plus the note. A chase that ends with nothing to send keeps its Status and goes on the weekly Park proposals (SLOW and the day chat keep that list)."
)

RECIPIENTS_CALL = (
    "RECIPIENTS: Rules for Zoya section 2's recipient rule, for every send and draft from either inbox. "
    "Before every send, a Bash python step builds the required set from it and prints it beside the draft's To and Cc as read back; assert equal "
    "(addresses, case-insensitive) and To not empty. A reply draft that differs gets one draft update (to, cc), which keeps the thread (CTO, 22 Nov), "
    "and a second check; still different: delete it, send nothing, block \"recipients: <what differed>\"."
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
     " A row you touch that still waits on Mamatha: a room or transcript step moves to Ranjita, a routine step to you, a decision to Akshay."),
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
     "- No WhatsApp in FAST work but ROOM ASK to Ranjita. Ranjita creates the rooms and attaches transcripts; Mamatha is on a long break: never mail, Cc, ask or wait on her (decision 646).\n- " + RECIPIENTS_CALL + "\n- " + FAST_PARKED),
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
     "Not found, not before the day after the recording, and no ask to Ranjita on the row yet: the ask is the segment \"Ranjita: download <guest>'s Zencastr transcript and attach it to the Episode's Transcript file (<Episode link>)\" with Ranjita in Waiting on (on a guest row it replaces only its transcript segment, never the row's Next date or another segment), plus one WhatsApp to her per TEAM WHATSAPP that names the guest, company, recording date and Episode link; log \"Zoya sent: transcript ask to Ranjita for <guest>\" (Kind WhatsApp, Action key). un# and Zencastr-only recordings she can't reach: \"Akshay: download the Zencastr transcript for <guest>\" on his list instead. 2 working days after the ask with no Transcript file on the Episode: one WhatsApp chase (action key \"<row id>:team:transcript-chase-<recording key>\", Activity \"Zoya sent: transcript chase to Ranjita for <guest>\", note \"transcript chased\"); still none 2 days later: Akshay's list, \"Akshay: no transcript yet for <guest>'s <D Mon> recording (Ranjita asked <D Mon>)\", no more chases. A Transcript file now on the Episode closes her segment (remove it and her Waiting on entry)."),
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
     "- 1 Sponsored offers: rows at Status Sponsored offered whose Next date is today or earlier, whatever Next action says (a plan written as \"Waiting on <name>: reply to the sponsored offer\" is still a sponsored row). The sponsored table on Rules for Zoya: follow-ups decides, for every show, whether a mail is due at all: interest first, the follow-up count with earlier sends included, pauses and stops. No interest shown: no mail; drop any \"Zoya: sponsored step <n>\" segment, Waiting on Guest or PR; 7 days after the offer with still no interest, a Founder Thesis row goes on the Park proposals (PARKED) and a un# row to Status Unresponsive, note \"YYYY-MM-DD: no sponsored interest (decision 618)\". Read the thread first: a decline of the paid route from their side gets the close note, Status They declined, and no chase, whatever the plan says."),
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
     "- " + RECIPIENTS_CALL + "\n- " + TEAM_ROLES + "\n- " + STATUS_AUTHORITY + "\n- PRE-SEND CHECKS, FAST and SLOW"),
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
BOOKING_NEW = "\"you can book a 30-minute planning call with Akshay here: podm.in/30min\" (always named that way, decision 569); never a paragraph"
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

# ---------------------------------------------------------------------------
# upkeep.txt: the retired daily sweep's still-live steps (change-map S6), cut
# mechanically from daily-sweep.txt at 83e8fb0 by line number, then edited.
# The day chat runs it once a weekday (zoya-day.md). Not a new schedule.
# ---------------------------------------------------------------------------
UPKEEP_INTRO = (
    "You run the daily upkeep of ThePodium's Business OS in Notion, inside the Zoya day chat, once each weekday in the first wake at or after 13:00 JST (decision 657 retired the sweep that ran these steps at that hour). "
    "These steps were the daily sweep's; the sweep is retired (decision 657) and only the steps below still run. Zoya sends every routine mail; Akshay takes the decisions (decisions 207, 223). "
    "FLAGGED FT ROWS: Engagements with Show Founder Thesis, an open Status (not They declined, We declined, Unresponsive, Parked or Form filled) and Next date today or earlier. "
    "Run, in this order, every step in full: STEP 4b, 3p, 3h, 3g, 3k, 3d, 4, 5, 6c, 7b, then STEP 7. A step left unfinished by a cap or a tool error runs first next weekday. "
    "Log the report as one Activity, Kind Note, Summary \"Upkeep <D Mon>: <Completed|Partial|Failed>\", Source ID \"upkeep:<today>\", the report in its page body; one already there for today is updated, never a second."
)
# Line numbers in daily-sweep.txt (1-based) that carry over unchanged before editing.
UPKEEP_LINES = [5, 6, 7] + list(range(8, 21)) + [21] + list(range(22, 39)) + [39] \
    + list(range(70, 75)) + [75] + list(range(76, 86)) + [86, 87, 88, 89, 91, 92, 95, 96] \
    + list(range(97, 110)) + [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120] \
    + list(range(121, 137)) + [137, 138, 139]
UPKEEP_EDITS = [
    ("S4-ranjita",
     "TEAM ROLES (decisions 154, 211, 223, 352). Nothing waits on Mamatha: never set Waiting on Mamatha or write \"Mamatha:\" on any row; a row you touch that waits on her moves to Zoya (a routine step) or Akshay (a decision).",
     "TEAM ROLES (decisions 154, 211, 223, 646). Mamatha is on a long break: never put her in Waiting on or Next action; a row you touch that waits on her moves to Ranjita (a room or transcript step), Zoya (a routine step) or Akshay (a decision)."),
    ("S5-senders",
     "A draft: MCP Emails draft (action create for a new mail with to and cc; action reply on a thread's latest message, then action update to set To and Cc, since a reply draft can't take them at creation) on that inbox, body plus html_body; never sent by you; log the draft_id the last call returned (it changes on every update).",
     "A draft in ad@thepodium.in: Gmail connector create_draft (never the MCP Emails draft tool on ad@, which stops on a permission prompt), body plus html_body; never sent by you; log the draft id it returns."),
    ("S6-sweep",
     ", and, in STEP 3a4 b only, a Task row's Task state, For engagement and Activities links, and its move to Trash (decision 416); in STEP 3p only, creating a PaaS Engagement. Never set Parked,",
     "; in STEP 3p only, creating a PaaS Engagement. Never set Parked (decision 656),"),
    ("S9-release",
     "on un#, Built to Share or Human by Design (not Founder Thesis: Zoya sends its release mail 1, decision 235),",
     "on Built to Share or Human by Design (not Founder Thesis or un#: their Mail 1 is the day chat's release duty, decisions 601, 638),"),
]
UPKEEP_EDITS += [
    ("S7-builder", "STEP 3h. AUDIT HANDOFFS AND FIX CHECKS (decisions 315, 329)", "STEP 3h. MAIL ISSUES FIX CHECKS (decision 315; auditor items go to the CTO and the Build board, decision 655)"),
    ("S7-builder", "otherwise Waiting on Builder.", "otherwise send the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the issue with send_message; no Engagements row (decision 655)."),
    ("S6-sweep", "First line: \"Sweep <A|B> <D Mon>: <status>\" from STATUS IN CODE. Then one line per step of your part, in TWO PARTS' order:",
     "First line: \"Upkeep <D Mon>: <status>\" from STATUS IN CODE. Then one line per step, in the intro's order:"),
    ("S6-sweep", "Bash `date -u` at the start of your part and before this write;", "Bash `date -u` at the start and before this write;"),
    ("S6-sweep", "Completed only if every step of your part has a line and each is done;", "Completed only if every step has a line and each is done;"),
    ("S6-sweep", "audit handoffs filed and fixes observed or reopened (STEP 3h); transcript asks added (STEP 3i);", "fixes observed or reopened (STEP 3h);"),
    ("S6-sweep", "old notes rewritten (STEP 3a); owners removed (STEP 3a2); rows changed from Gmail (name: old -> new, evidence date); ", ""),
    ("S6-sweep", "Next action segments trimmed (STEP 3a3); one-time moves (STEP 3a4: steps moved to Zoya, transcript asks folded, by name); ", ""),
]


EDITS["zoya-fast.txt"] += [
    ("S6-sweep",
     "You are the only routine that writes Zoya's work. You run at :38 every hour, 07:38 to 23:38 JST, under LOCK, and every run does your FAST work (FAST ORDER): replies owed to people who wrote to us, Akshay's decision mails and other steps from his calls, and holding replies. Your SLOW work (follow-up chains, nurture, team work, payments, snoozes, STEP 0) is the Zoya SLOW task's, on weekdays (decisions 449, 450, 546): it takes the same LOCK and shares your action keys, Sent checks, contact limits and daily cap. No run of yours does SLOW work.",
     "This is Zoya FAST, one pass inside the Zoya day chat's wake, under LOCK: replies owed to people who wrote to us, Akshay's decision mails and other steps from his calls, and holding replies (FAST ORDER). SLOW work (follow-up chains, nurture, team work, payments, snoozes) runs in the SLOW composer and shares your action keys, Sent checks, contact limits and daily cap; you never do it."),
    ("S6-sweep",
     "\n- SLOW work only: Rules for Zoya: follow-ups 40b19a301a7f81999c1acd8350d59a54\nRULES LOAD: read every page above in full every run; the follow-ups page and the routine pages it links are SLOW work's only, and FAST sends never wait on them.",
     "\nRULES LOAD: read every page above in full every run."),
    ("S0-links", "Approved links only: podm.in/30min, podm.in/book, podm.in/sponsored (the first sponsored link a lead sees), podm.in/why-sponsor (sponsored follow-ups and questions), podm.in/guest-list, podm.in/community, podm.in/note, podm.in/pitch-to-us, podm.in/thank-you, founderthesis.com (show site, guest profiles), and youtube.com/@spotlight-pod only in the Founder Thesis price negotiation reply (decision 237); a Zencastr room link (zencastr.app.link/<room> or zencastr.com/record/<user>/<room>) only in that guest's recording-link mail and invite; client show links: SCOPE.", "Approved links only: the list on Rules for Zoya, each for its job; client show links: SCOPE."),
    ("S6-sweep",
     " FAST work starts no new row 25 minutes after the run's start (measured, TIME).",
     ""),
    ("S6-sweep",
     "(\"step <name>: done <n> | not due | unfinished (minute 25 | cap | tool error: <tool> <error>)\"), a line \"sends <n> of <per-run cap>, today <n> of <daily cap>\", a \"stop: minute 25 at <time>\" line if that stop applied,",
     "(\"step <name>: done <n> | not due | unfinished (carried by the wake budget | cap | tool error: <tool> <error>)\"), a line \"sends <n> of <per-run cap>, today <n> of <daily cap>\","),
    ("S0-release",
     "deployment reference \"zoya-one ded73b07d8e3\" (this prompt's version),",
     "the release commit and this file's sha256 from manifest.json,"),
    ("S6-sweep",
     ", or minute 25 (a body line \"stop: minute 25 at <date -u time>\", 25 or more minutes after the start); anything else, or a FAST step with no line, is Failed \"early exit at minute <n>\".",
     ", or carried by the day chat's wake budget; anything else, or a FAST step with no line, is Failed \"early exit\"."),
    ("S6-sweep",
     " GATE: while it prints Failed and `date -u` shows under 25 minutes since the start, write nothing final: go back to the first unfinished step, work it, and check again.",
     " GATE: while it prints Failed and the wake budget has time, write nothing final: go back to the first unfinished step, work it, and check again."),
    ("S10-holding",
     "a negotiation other than the Founder Thesis lower-price ask in b, a call he offered, an upset guest or PR, press, a partnership, a release-date ask, any publishing ask, a request to see the cut or final episode from a Tier 1, sponsored or patron guest, anything new):",
     "a negotiation other than the Founder Thesis lower-price ask in b, a call he offered, an upset guest or PR, press, a partnership, any publishing ask, a request to see the cut from a guest who covered our cost (sponsored, patron, paid package; decision 208), anything new; a release-date ask is the wording page's \"Next steps and release date\" (decision 427) and a final-cut ask from anyone else \"Asks to see the video before release\" (decision 600), both yours):"),
    ("S10-holding",
     "one line, \"hi <first name>, checking with akshay, will come back to you.\" (no date: decision 418)",
     "one line, \"hi <first name>, will get back to you on this\" (decision 571: never Akshay's name, never a date)"),
    ("S10-holding",
     "A fresh guest pitch gets \"thanks <first name>! looping in Akshay\" with him in Cc,",
     "A fresh guest pitch gets \"thanks <first name>! looping in Akshay, will get back to you.\" (decision 584) with him in Cc,"),
]
LINKS_OLD_START = "Approved links only: podm.in/30min,"

for _f in ("zoya-fast.txt", "zoya-slow-work.txt"):
    EDITS[_f].append(("S3-recipients",
        " Set To and Cc explicitly: To is whoever's move it is, Cc the house copies; Akshay is never in To.",
        " To and Cc: RECIPIENTS."))
EDITS["zoya-fast.txt"].append(("S1-parking",
    " A chase that ends with nothing to send keeps its Status and goes on the weekly Park proposals (SLOW and the day chat keep that list).", ""))

for _f in ('zoya-fast.txt','zoya-slow-work.txt'):
    EDITS[_f].append(('S11-zoya-date', "A write that changes Next action sets Next date to the earliest open segment date (a segment's date: the due date its text gives (\"on\", \"by\" or \"original due\", never a date the ask is about), else its key's; undated segments don't count, and with none dated it is the day of the write; \"original due <YYYY-MM-DD>\" counts; a snoozed or held-for-snooze one never does); any other write leaves Next date as it is.", "A write that changes Next action sets Zoya date (decision 637) to the earliest open Zoya segment date (a segment's date: the due date its text gives (\"on\", \"by\" or \"original due\", never a date the ask is about), else its key's; a snoozed or held-for-snooze one never counts), and Next date only from people's steps (Akshay's decision or step, their side's move, a call): never a Zoya-only date; while a row waits on an Akshay decision, Next date is the day he must act. Any other write leaves both as they are."))
EDITS['zoya-fast.txt'].append(('S11-next-action', "- NEXT ACTION SIZE (decision 438): each Next action segment you write is at most about 120 characters past its owner and key (\"<owner>: <step> (<D Mon>)\"); the detail, the reason and any quote go in the Claude note;", "- NEXT ACTION SIZE (decisions 438, 588): one segment per person, \"<Who>: <step>\" and a date if any, about 15 words; background goes in the page body or the Claude note;"))
EDITS['zoya-fast.txt'].append(('S0-trim', " KIND (decision 329): an Engagement with Kind Task is a work item, never a guest: never pitch-match, evaluate, book, chase or mail a guest about it, and skip it in every guest step; act on it only where a step names Task rows. Each Task row is one obligation with its own Waiting on, Next action, Next date and Task state (Captured, Handed over, Doing, Awaiting someone else, Done, On hold); closing it never touches the row in its For engagement or any other ask. FAST work creates no Task rows.", " KIND (decision 329): a Kind Task row is a work item, never a guest: skip it in every guest step. FAST work creates no Task rows."))
EDITS['zoya-slow-work.txt'].append(('S11-next-action', "- NEXT ACTION SIZE (decision 438): each Next action segment you write is at most about 120 characters past its owner and key (\"<owner>: <step> (<D Mon>)\"); the detail, the reason and any quote go in the Claude note;", "- NEXT ACTION SIZE (decisions 438, 588): one segment per person, \"<Who>: <step>\" and a date if any, about 15 words; background goes in the page body or the Claude note;"))
EDITS['zoya-fast.txt'].append(('S0-trim', " Fold only a proven duplicate: carry every Claude note line, open Next action segment and commitment, Waiting on, all Activities and the Call, Eval and Prep doc links (Prep doc link is named \"Dossier link\" until the rename; use whichever the row has, never create a new property; two Eval links: the kept row's stays, the other in a Claude note line) to the kept row, and its Guest, Via and Stakeholders to the kept row's Stakeholders; read it back, clear the duplicate's relations, then Trash it (decision 416) and report it; never merge People)", " Fold only a proven duplicate, exactly as CLAUDE.md's booker rule says (every note, open commitment, Activity and link carried to the kept row and read back, then Trash, decision 416), and report it; never merge People)"))
EDITS['zoya-fast.txt'].append(('S0-trim', " Guest-facing mail (day-before note, prep note, recording link, reschedule, thank-you) reaches the guest's side directly: To the guest when their People row has an Email, else the person from the guest's company on the Engagement (Stakeholders, Via, or any company-side attendee on its invites); PR goes in Cc.", " Guest-facing mail goes To the guest, else a company-side contact on the Engagement (Stakeholders, Via, an invite attendee); PR in Cc."))
EDITS['zoya-fast.txt'].append(('S0-trim', "TIME: Bash `date -u` at the start gives the run's start; the end time is `date -u` at your last write; elapsed minutes are always measured with `date -u`, never estimated, and size or context never ends a run early; rules loading, thread length or cost is never a reason to leave a step.", "TIME: start and end are `date -u` (at the start and at your last write), never estimated; size, context, rules loading, thread length or cost never ends a run or leaves a step."))
EDITS['zoya-fast.txt'].append(('S0-trim', "parses the step lines, the \"sends\" and \"stop:\" lines and the start and end times,", "parses the step lines, the \"sends\" line and the start and end times,"))
EDITS['zoya-fast.txt'].append(('S0-trim', " Where the FT routine pages set timing, follow them.", ""))
EDITS['zoya-fast.txt'].append(('S0-trim', "Never introduce or describe yourself (SLOW work: except in release mail 2).", "Never introduce or describe yourself."))
EDITS['zoya-fast.txt'].append(('S0-trim', "To the person who pitched (the founder if they wrote directly), Cc everyone else on the thread and Akshay.", "To the person who pitched (the founder if they wrote directly); the rest per RECIPIENTS."))
EDITS['zoya-fast.txt'].append(('S0-trim', "(a new mail: email_compose action send; a reply: THREADING's draft way, never email_compose action reply, NO COMPOSE REPLY)", "(a new mail: email_compose action send; a reply: NO COMPOSE REPLY)"))
EDITS['zoya-fast.txt'].append(('S0-trim', "a thread with no Engagement gets one as inbox capture STEP 3 creates it (a pitch: Show by subject, not inbox alone, decision 538; Status New, Waiting on Akshay, Next action \"Akshay: new pitch from <PR or self> for <guest>, eval running (captured <D Mon HH:MM>)\", decision 541), Source ID \"zoya-mail:<folder>:<uid>\", but first (decision 424): a sender acting for someone else is attached only on evidence naming the guest (the thread or form names them, or the sender works at the guest's own company, not an agency, which has exactly one open row on that show): they join that row's Stakeholders and no row is created; organisation or domain alone never attaches; no such evidence, or two candidates: create nothing, report it.", "a thread with no Engagement gets one (Show by subject, decision 538; Status New, Waiting on Akshay, \"Akshay: new pitch from <PR or self> for <guest>, eval running (captured <D Mon HH:MM>)\", decision 541; Source ID \"zoya-mail:<folder>:<uid>\"), but a sender acting for someone else is attached only as CLAUDE.md's booker rule says (decision 424): no evidence naming the guest, or two candidates: create nothing, report it."))
EDITS['zoya-fast.txt'].append(('S0-trim', "- CLIENT-SHOW SCHEDULING (decision 446): on client shows no recording time is proposed, created, moved or confirmed without Akshay's ok (SCOPE), whatever a page says. A reply to a mail Akshay wrote himself goes on his list and gets at most the holding reply (decision 448), plus the themes answer when it asks for themes or questions before a recording (decision 453), unless it needs nothing of him (Last activity and a Claude note line only, decision 490).", "- CLIENT-SHOW SCHEDULING (decision 446): on client shows no recording time is proposed, created, moved or confirmed without Akshay's ok (SCOPE), whatever a page says. A reply to a mail Akshay wrote himself: STEP 1 b (decisions 448, 453, 490)."))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', "STEP 0 (feedback, bounces, vendor forms, owner mail, scorecard)", "STEP 0 (feedback, bounces, vendor forms, scorecard)"))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', "; owner mail \"ownermail:<YYYY-MM-DD>\"", ""))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', "; an owner mail item sent at once in its own mail \"ownermail:<YYYY-MM-DD>:<row id>\"", ""))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', "(owner mail, feedback, vendor forms, the Monday scorecard)", "(feedback, vendor forms, the Monday scorecard)"))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', "team steps, owner mail and the scorecard go on their dates", "team steps and the scorecard go on their dates"))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', ", the owner mail and the Monday scorecard (sent or not due)", ", the Monday scorecard (sent or not due)"))
EDITS['zoya-slow-work.txt'].append(('S8-oneoffs', " Where the FT routine pages set timing, follow them.", ""))

EDITS['zoya-slow-work.txt'].append(('S0-retired', "; a Salesblink mail to them recorded on any of their rows in the last 14 days (this hold ends 2 Nov; Waiting on Chaandini alone is never a hold)", ""))
EDITS['zoya-slow-work.txt'].append(('S0-retired', "\"held: <other row or Salesblink>, <why>, recheck <D Mon>\"", "\"held: <other row>, <why>, recheck <D Mon>\""))
EDITS['zoya-slow-work.txt'].append(('S0-retired', "a Salesblink or cold-outreach hold", "a cold-outreach hold"))
EDITS['calendar.txt'].append(('S0-retired', "A show guest with no eval goes to the evals routine as usual.", "A show guest with no eval gets one from its engagement chat, which the day chat starts (decision 593)."))
EDITS['calendar.txt'].append(('S0-retired', "The eval re-run is the evals routine's job once Status is Precall done (decision 172).", "The eval re-run is the engagement chat's once Status is Precall done (decisions 172, 593)."))
EDITS['inbox-actions.txt'].append(('S0-retired', "Founder Thesis and un# pitches go to the evals routine.", "Founder Thesis and un# pitches get their eval from the engagement chat the day chat starts (decision 593)."))
EDITS['whatsapp.txt'].append(('S6-sweep', "unfinished (minute 25 at <time> | cap: <what>", "unfinished (carried by the wake budget | cap: <what>"))
EDITS['whatsapp.txt'].append(('S6-sweep', "TIME: Bash `date -u` at the start and before this report; a \"stop: minute 25 at <date -u time>\" line only when that much time has measurably passed.", "TIME: Bash `date -u` at the start and before this report."))
EDITS['whatsapp.txt'].append(('S6-sweep', "\" only when each unfinished step is minute 25 (with the stop line, 25 or more minutes after the start), a cap this prompt sets for that step, or a tool error with its tool and error text", "\" only when each unfinished step is carried by the day chat's wake budget, a cap this prompt sets for that step, or a tool error with its tool and error text"))
EDITS['zoya-slow.txt'].append(('S0-release', "deployment reference \"zoya-slow 4c4c9f7accde\" (this prompt's version),", "the release commit and this file's sha256 from manifest.json,"))
EDITS['inbox-capture.txt'].append(('S3-recipients', "Recipients follow RECIPIENTS in the Zoya prompt: everyone on the message you loop in on stays, less bounced and dead addresses and Mamatha (decision 646).", "Recipients follow the recipient rule on Rules for Zoya section 2: everyone on the message you loop in on stays, less bounced and dead addresses and Mamatha (decision 646)."))

EDITS['inbox-capture.txt'].append(('S21-oneoffs', "Every mail Activity you create or re-key, every one STEP 0 finds in ad@, and", "Every mail Activity you create or re-key, and"))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', "except the Trash steps of STEP 0 and the SELF-CHECK (decision 416)", "except the Trash steps of the SELF-CHECK (decision 416)"))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', "page body = first the lines \"0L: <n> due, <n> worked (<n> passed over)\" and \"0A: <n> due, <n> worked (meeting <n>, fold <n>, adid <n>, REF <n>, RAW <n>, pended <n>)\" (due: the row count each SQL returned; worked: rows settled this run, by the path that settled them, a 0L row passed over for its \"link:\" line and a 0A row struck or pended with its record line included; a row left by a quota, rate-limit or 5xx error is not worked), then the \"stamped:\" line as built (kept), then", "page body = first the \"stamped:\" line as built (kept), then"))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', " MEASURED STOP (CTO, 3 Nov): a stop for time, here or at STEP 0A's or STEP 0's window, is read from Bash date -u at that moment, never estimated, and the record says \"stopped at minute <n> of <limit>\" (minutes since the run's start; limit 18, or the window's own minute). Rows of this run's 0L or 0A batch left unworked while no measured limit has passed (STOP TIME, or 0A's window: 5 minutes after 0L ends or minute 10) make the run Failed, \"0A skipped at minute <n>\" (or \"0L skipped at minute <n>\"), never Partial; rows left only by a quota, rate-limit or 5xx error are Failed as RUN RECORD says, naming that error, never \"skipped\".", " MEASURED STOP: a stop for time is read from Bash date -u at that moment, never estimated, and the record says \"stopped at minute <n> of 18\". Rows left only by a quota, rate-limit or 5xx error are Failed as RUN RECORD says, naming that error."))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', "ORDER GATE (CTO, 3 Nov): after the run record (and OVERLAP's check), your first two SQL queries (the data-source fetches and the run record's own checks aside) are STEP 0L's SQL and then STEP 0A's SQL, both run before STEP 1's search or any other MCP Emails call, each one's row count logged in the record as the \"due\" figure of its 0L or 0A line (RUN RECORD); then work 0L's rows, then 0A's. A run that searched mail first, or whose record lacks either line or gives a due figure no SQL returned (a line like \"0L: not run\" lacks it), is Failed, \"order gate\". OVERLAP's No-op record is exempt; with no record (RUN RECORD's no-id case), the two lines open the final report instead.\n", ""))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', " (BACKLOG: more than 15 due at the start: 25; STEP 0 only shares the time window)", " (BACKLOG: more than 15 due at the start: 25)"))
EDITS['inbox-capture.txt'].append(('S21-oneoffs', "REF first (STEP 0A's path 4: the later messages' In-Reply-To and References, each HEADER-confirmed to return this same MCP Emails id)", "REF first (read the later messages of its thread (All Mail search by its subject, Re: and Fwd: dropped, since its date; then Zoya's inbox the same way) with read_batch, body_max_chars 0, and take every id in their In-Reply-To and References that no Activity holds; confirm each with email_read search, include_folders [\"[Gmail]/All Mail\"], query HEADER Message-ID \"<id>\", until one returns this same MCP Emails id)"))
REMOVE_LINES.setdefault("inbox-capture.txt", []).extend([
    ("S21-oneoffs", "STEP 0L. LINK FIRST (through 2026-11-05; CTOA-03)"),
    ("S21-oneoffs", "STEP 0A. OLD allmail: ROWS (CTO, 2 Nov)"),
    ("S21-oneoffs", "STEP 0. OLD ROWS (one-off, every run until none is left; CTO, 1 Nov)"),
])
EDITS['zoya-fast.txt'].append(('C2-loopin', ", to and cc passed explicitly: To that person, Cc everyone else RECIPIENTS 1/ keeps plus Zoya.", ", to and cc passed explicitly as the loop-in rule in Rules for Zoya section 2 gives them (To that person; Cc the rest of that message's people, less ad@thepodium.in itself, plus Zoya)."))
EDITS['zoya-fast.txt'].append(('C2-loopin', "RECIPIENTS' check runs on the to and cc you are about to pass, in a Bash python step, before the call.", "RECIPIENTS' check runs on the to and cc you are about to pass, in a Bash python step, before the call. After the send, read ad@'s Sent copy (email_read) and assert in Bash its To and Cc and that its In-Reply-To is the message you replied on; a miss: send nothing more on that thread, report it, and put \"Akshay: loop-in to <who> went wrong (<what>)\" on the row."))
EDITS['zoya-fast.txt'].append(('C2-loopin', "and idempotency_key \"loopin:<the thread's latest Message-ID>\" only on the draft send;", "and idempotency_key \"loopin:<the thread's latest Message-ID>\" on the email_compose call;"))
EDITS['zoya-slow-work.txt'].append(('C2-loopin', ", to and cc passed explicitly: To that person, Cc everyone else RECIPIENTS 1/ keeps plus Zoya.", ", to and cc passed explicitly as the loop-in rule in Rules for Zoya section 2 gives them (To that person; Cc the rest of that message's people, less ad@thepodium.in itself, plus Zoya)."))
EDITS['zoya-slow-work.txt'].append(('C2-loopin', "RECIPIENTS' check runs on the to and cc you are about to pass, in a Bash python step, before the call.", "RECIPIENTS' check runs on the to and cc you are about to pass, in a Bash python step, before the call. After the send, read ad@'s Sent copy (email_read) and assert in Bash its To and Cc and that its In-Reply-To is the message you replied on; a miss: send nothing more on that thread, report it, and put \"Akshay: loop-in to <who> went wrong (<what>)\" on the row."))
EDITS['zoya-slow-work.txt'].append(('C2-loopin', "and idempotency_key \"loopin:<the thread's latest Message-ID>\" only on the draft send;", "and idempotency_key \"loopin:<the thread's latest Message-ID>\" on the email_compose call;"))
EDITS['inbox-capture.txt'].append(('C9-report', "STEP 8. REPORT\n", "STEP 8. REPORT\nYou run as the capture composer inside the Zoya day chat's wake and send nothing. Every loop-in STEPS 6 to 6b call for becomes a report line \"loop-in due: <row>, <name>, <the thread's latest Message-ID>\". When the run record is written, send_message (load claude-code-remote's tools with ToolSearch \"+claude-code-remote\") to the day chat session id your brief names, else the newest session tagged zoya-day: one line with the status, counts and every \"loop-in due\" line.\n"))
EDITS['inbox-capture.txt'].append(('C9-report', "You send only the loop-ins of STEPS 6 to 6b (MAILBOX; decision 420).", "You send nothing: the loop-ins of STEPS 6 to 6b go in your report as \"loop-in due\" lines and the day chat sends them (STEP 8; decision 420)."))
EDITS['inbox-capture.txt'].append(('C9-report', "; the old-row counts", ""))
EDITS['inbox-capture.txt'].append(('C9-report', "- Mail actions allowed, all through MCP Emails: only the loop-in sends and RSVP archiving the steps below describe, limited by ZOYA LIVE.", "- Mail actions allowed, all through MCP Emails: only the RSVP archiving the steps below describe; no sends (ZOYA LIVE)."))
EDITS['zoya-slow-work.txt'].append(('C5-slow', "SLOW WORK FILE (the Zoya SLOW task, 08:08, 11:08 and 17:08 JST on weekdays, decisions 449, 450).", "SLOW WORK FILE (the Zoya SLOW task, 11:08 and 17:08 JST on weekdays, decision 657)."))
EDITS['zoya-slow-work.txt'].append(('C5-slow', " (none there: never before 09:00 or after 20:00 IST, so the 08:08 JST run, 04:38 IST, sends none)", " (none there: never before 09:00 or after 20:00 IST)"))
EDITS['zoya-slow-work.txt'].append(('C5-slow', "only to these team members: Jaya (invoices, payment confirmations), Sarika (guest edit feedback), and for the 24-hour nudge in INTERNAL TASKS b the team member whose Task it is (a transcript row waits on Zoya and gets no WhatsApp, decision 456).", "only to these team members: Jaya (invoices, payment confirmations), Sarika (guest edit feedback), Ranjita (rooms, transcripts, features: TEAM ROLES), and for the 24-hour nudge in INTERNAL TASKS b the team member whose Task it is."))
EDITS['zoya-slow-work.txt'].append(('C5-slow', "(Jaya's chat is named \"Jaya Lakshmi Unnati Support\", Sarika's \"Sarika Karnik Work\"; several chats match \"Sarika\", use only that one)", "(Jaya's chat is named \"Jaya Lakshmi Unnati Support\", Sarika's \"Sarika Karnik Work\", Ranjita's \"Ranjita Chattopadhyay Unnati Rec\"; several chats match \"Sarika\", use only that one)"))
EDITS['zoya-slow-work.txt'].append(('C5-slow', "Two or three short messages, lowercase start, the first opening \"hi <name>, zoya here.\" and the last signed \"Zoya, Akshay's AI Chief of Staff\".", "Two or three short messages, lowercase start, the first opening \"Zoya ✨\" (TEAM ROLES)."))
EDITS['zoya-slow-work.txt'].append(('C8-nurture', "Approved pursuit (never a UN# SPONSORED pursuit; a guest booking on the same row still can): Precall requested, Sponsored offered, Booking or LT chase, Tier 1, or one Akshay asked to nurture.", "Approved pursuit (never a sponsored pursuit, 5c; a guest booking on the same row still can): Precall requested, Booking or LT chase, Tier 1, or one Akshay asked to nurture."))
EDITS['zoya-slow-work.txt'].append(('C8-nurture', "Mails use routine 7's angles (sponsored: routine 8's, to whoever owns the thread)", "Mails use routine 7's angles"))
EDITS['zoya-slow-work.txt'].append(('C8-nurture', "a no-contact request from that person anywhere (Standing, note, Your call, thread; Status Parked)", "a no-contact request from that person anywhere (Standing, note, Your call, thread; Status They declined with the no-contact note)"))
UPKEEP_EDITS.append(('C10-upkeep', " (daily sweep)\" or \"(daily sweep)\" for a plain flag", " (upkeep)\" or \"(upkeep)\" for a plain flag"))
UPKEEP_EDITS.append(('C10-upkeep', "set <who> (daily sweep)\"", "set <who> (upkeep)\""))
UPKEEP_EDITS.append(('C10-upkeep', "revenue step moved to Akshay (daily sweep)\"", "revenue step moved to Akshay (upkeep)\""))
UPKEEP_EDITS.append(('C10-upkeep', "(STEP 3a2's OWNERS)", "(OWNERS: a name leaves Waiting on with its last ask)"))
UPKEEP_EDITS.append(('C10-upkeep', "Read Gmail first (as STEP 3); only if nothing settles it", "Read the row's mail first (MAILBOX: since its last Activity, the guest's name and company); only if nothing settles it"))
UPKEEP_EDITS.append(('C10-upkeep', "Read Gmail first (as STEP 3); if nothing newer", "Read the row's mail first (MAILBOX: since its last Activity, the guest's name and company); if nothing newer"))
UPKEEP_EDITS.append(('C10-upkeep', "the previous Part B report's \"step 4 carry-over:\" line", "the previous upkeep report's \"step 4 carry-over:\" line"))
UPKEEP_EDITS.append(('C10-upkeep', "in itself) since 4 days ago", "in itself) since the start of the last \"upkeep:\" report (none: 4 days ago)"))
UPKEEP_EDITS.append(('C10-upkeep', "b. Create a draft in ad@thepodium.in (MAILBOX):", "b. Create a draft in ad@thepodium.in with the Gmail connector create_draft (load it with ToolSearch \"+Gmail\"; in mail to outsiders write each approved link as plain text with its first dot broken, podm<span>.</span>in/..., never an <a> tag, decision 123):"))
UPKEEP_EDITS.append(('C10-upkeep', "send the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the issue with send_message;", "send the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the issue with send_message (load its tools with ToolSearch \"+claude-code-remote\"; if send_message is missing or fails, put it on Akshay's list as \"Akshay: for the CTO: <what>\" instead);"))
EDITS['calendar.txt'].append(('C10-cto-msg', "and send_message the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the event, guest and the written cancel", "and send_message the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) the event, guest and the written cancel (load its tools with ToolSearch \"+claude-code-remote\"; if send_message is missing or fails, put it on Akshay's list as \"Akshay: for the CTO: <what>\" instead)"))
EDITS['zoya-slow-work.txt'].append(('C10-cto-msg', "and send the prompt change to the CTO session (send_message, session_015wSc87F8WCdJKB91Tm34tJ) naming the Mail issues row", "and send the prompt change to the CTO session (send_message, session_015wSc87F8WCdJKB91Tm34tJ) naming the Mail issues row (load its tools with ToolSearch \"+claude-code-remote\"; if send_message is missing or fails, put it on Akshay's list as \"Akshay: for the CTO: <what>\" instead)"))
EDITS['zoya-fast.txt'].append(('S0-trim', "- LEAK CHECK (decision 215) before every send, on the text you write, and on the gmail_quote and MCP's plain-text quote with every nested part, unless every recipient outside the team was on the quoted message's own From, To or Cc (decision 452); a quote that fails goes, with the mail, to Akshay's list unsent: no \"eval\", \"verdict\", \"score\", \"fit\", \"/10\", \"tier\", \"route\", \"sponsored only\", \"organic\" (outside the approved sponsored wording), no verdict name, no revenue, valuation or funding figure the guest's side hasn't made public, no criticism of the guest or their company, no description of their company in brackets or anywhere else (decision 399: name it and stop). A mail that can't be written without one of these goes to Akshay's list unsent.", "- LEAK CHECK (decision 215) before every send: Rules for Zoya section 2 leak check, on the text you write and on the gmail_quote and plain-text quote with every nested part, unless every outside recipient was on the quoted message (decision 452); never a description of their company (decision 399: name it and stop). A fail goes to Akshay's list unsent."))
EDITS['zoya-fast.txt'].append(('S0-trim', "- SHOW CHECK (decision 306) before every send (the gmail_quote and MCP's plain-text quote aside): every fact about a show (name, premise, host, audience, past guests, format, links) comes word for word from that show's pitch sheet on the Notion page \"Client show mails\" (3fc19a301a7f817588e2d081af825f8a), or for Founder Thesis from the wording page. The show is the Engagement's Show. No word from another show's \"Only on this show\" list in subject, body, signature or links, and nothing the sheet marks \"to confirm\". A mail that fails goes unsent: \"Akshay: show check failed for <guest>: <what>\" on his list.", "- SHOW CHECK (decision 306) before every send (quotes aside): Rules for Zoya section 2 show check against that show's pitch sheet on Client show mails (3fc19a301a7f817588e2d081af825f8a), or the wording page for Founder Thesis. A fail goes unsent: \"Akshay: show check failed for <guest>: <what>\" on his list."))
EDITS['zoya-slow-work.txt'].append(('S0-trim', "- LEAK CHECK (decision 215) before every send, on the text you write, and on the gmail_quote and MCP's plain-text quote with every nested part, unless every recipient outside the team was on the quoted message's own From, To or Cc (decision 452); a quote that fails goes, with the mail, to Akshay's list unsent: no \"eval\", \"verdict\", \"score\", \"fit\", \"/10\", \"tier\", \"route\", \"sponsored only\", \"organic\" (outside the approved sponsored wording), no verdict name, no revenue, valuation or funding figure the guest's side hasn't made public, no criticism of the guest or their company, no description of their company in brackets or anywhere else (decision 399: name it and stop). A mail that can't be written without one of these goes to Akshay's list unsent.", "- LEAK CHECK (decision 215) before every send: Rules for Zoya section 2 leak check, on the text you write and on the gmail_quote and plain-text quote with every nested part, unless every outside recipient was on the quoted message (decision 452); never a description of their company (decision 399: name it and stop). A fail goes to Akshay's list unsent."))
EDITS['zoya-slow-work.txt'].append(('S0-trim', "- SHOW CHECK (decision 306) before every send (the gmail_quote and MCP's plain-text quote aside): every fact about a show (name, premise, host, audience, past guests, format, links) comes word for word from that show's pitch sheet on the Notion page \"Client show mails\" (3fc19a301a7f817588e2d081af825f8a), or for Founder Thesis from the wording page. The show is the Engagement's Show. No word from another show's \"Only on this show\" list in subject, body, signature or links, and nothing the sheet marks \"to confirm\". A mail that fails goes unsent: \"Akshay: show check failed for <guest>: <what>\" on his list.", "- SHOW CHECK (decision 306) before every send (quotes aside): Rules for Zoya section 2 show check against that show's pitch sheet on Client show mails (3fc19a301a7f817588e2d081af825f8a), or the wording page for Founder Thesis. A fail goes unsent: \"Akshay: show check failed for <guest>: <what>\" on his list."))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', "STEP 0g. MONDAY SCORECARD. In the first run at or after 08:00 JST each Monday, unless an Activity with Source ID \"scorecard:<that Monday, YYYY-MM-DD>\" exists: one new mail from your inbox to Akshay only, subject \"Zoya: last week (<D Mon> to <D Mon>)\", in his voice, five numbered lines for last Monday 00:00 to Sunday 24:00 JST, counted only from Activities and Engagements, never estimated: 1/ follow-ups: <due> due, <sent> sent (the sums of last week's run records); 2/ sponsored: <n> conversations moved (a reply from their side or a Status change on a Sponsored offered row), <n> won (Payment 1 received or a yes), with names; 3/ tier 1: <n> booked (a precall or recording on the calendar), with names; 4/ stuck: up to 3 open rows whose Next date passed, as \"<name>: <whose move>, since <D Mon>\"; 5/ next: one line on the week ahead (recordings, releases). Log it: Kind Email out, Summary \"Zoya sent: Monday scorecard <D Mon>\", Source ID \"scorecard:<that Monday>\", the sent message id in the page body, Captured today.", "STEP 0g. MONDAY NUMBERS (decisions 554, 589, 619: no scorecard mail). In the first run each Monday, write these lines into this run record's body, never a mail, for last Monday 00:00 to Sunday 24:00 JST, counted only from Activities, Engagements and Episodes, never estimated: 1/ follow-ups: <due> due, <sent> sent (the sums of last week's run records); 2/ sponsored: <n> conversations moved (a reply from their side or a Status change on a Sponsored offered row), <n> won (Payment 1 received or a yes), with names; 3/ tier 1: <n> booked (a precall or recording on the calendar), with names; 4/ stuck: up to 3 open rows whose Next date passed, as \"<name>: <whose move>, since <D Mon>\"; 5/ next: one line on the week ahead (recordings, releases); 6/ share rate: <shared> of <released> Founder Thesis episodes released last week whose guest shared (Guest shared). The morning brief reads them from there. Written once: skip if a run record dated this Monday already has a \"6/ share rate\" line."))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', "; the scorecard \"scorecard:<Monday YYYY-MM-DD>\"", ""))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', ", the Monday scorecard (sent or not due)", ", the Monday numbers (written or not due)"))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', "(feedback, vendor forms, the Monday scorecard)", "(feedback, vendor forms, the Monday numbers)"))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', "team steps and the scorecard go on their dates", "team steps and the Monday numbers go on their dates"))
EDITS['zoya-slow-work.txt'].append(('R6-scorecard', "STEP 0 (feedback, bounces, vendor forms, scorecard)", "STEP 0 (feedback, bounces, vendor forms, Monday numbers)"))
EDITS['zoya-fast.txt'].append(('R2-rules-once', "RULES LOAD: read every page above in full every run.", "RULES LOAD: read every page above in full every run. Inside the day chat, the wake's RULES GATE read is your RULES LOAD; read again only a page fetched before this wake or edited since."))
EDITS['inbox-actions.txt'].append(('R5-cancel', "A plain cancel request still cancels the event as section 8 says, then hands the reply to Zoya (\"invite cancelled\").", "A plain cancel request is handled as section 8 says (the blocked-delete segment, never delete_event), then the reply goes to Zoya."))

# Fix 1 (23 Nov, Auditor CX-20261123T0800 finding 2): decision 637 date ownership.
# Zoya's own chase steps write Zoya date; Next date holds only people's steps.
_F1 = 'F1-zoya-date'
for _f in ('zoya-slow-work.txt', 'zoya-fast.txt'):
    EDITS[_f].append((_F1, "A follow-up STEP 2 selects by Status and Next date needs no wording", "A follow-up STEP 2 selects by Status and Zoya date needs no wording"))
EDITS['zoya-slow-work.txt'] += [
    (_F1, "stays due (Next date unchanged)", "stays due (Zoya date unchanged)"),
    (_F1, "Booking, Recorded or LT chase with Next date today or earlier", "Booking, Recorded or LT chase with Zoya date today or earlier (decision 637; a row with no Zoya date yet is selected by its Next date once, and that run writes its Zoya date)"),
    (_F1, "Chase step 0, Next date 30 days after our last mail", "Chase step 0, Zoya date 30 days after our last mail"),
    (_F1, "Every hold writes Next date and the reason", "Every hold writes Zoya date and the reason"),
    (_F1, "Status LT chase, Next date today or earlier, nurture rows included", "Status LT chase, Zoya date today or earlier, nurture rows included"),
    (_F1, "moves its segment's date and Next date to the first day it may go", "moves its segment's date and Zoya date to the first day it may go"),
    (_F1, "names the blocker and its owner and moves Next date 7 days on", "names the blocker and its owner and moves Zoya date 7 days on"),
    (_F1, "Chase step = n; Next date = the earliest of the next step's due date and any other open segment's date", "Chase step = n; Zoya date = the earliest of the next step's due date and any other open Zoya segment's date"),
    (_F1, "Chase step 0; Next date = this send's date plus the NURTURE interval for n", "Chase step 0; Zoya date = this send's date plus the NURTURE interval for n"),
    (_F1, "a hold moves the segment's \"on <D Mon>\" (never its key) and Next date; a failed send moves only Next date", "a hold moves the segment's \"on <D Mon>\" (never its key) and Zoya date; a failed send moves only Zoya date; none of these ever moves Next date"),
]
EDITS['zoya-slow-work.txt'] += [
    (_F1, "Eval verdict, Next date, Next action", "Eval verdict, Next date, Zoya date, Next action"),
    (_F1, "SQL on Engagements (Waiting on, Next action, Next date, Status, Show)", "SQL on Engagements (Waiting on, Next action, Next date, Zoya date, Status, Show)"),
    (_F1, "other than Akshay whose Next date is today or earlier", "other than Akshay whose Next date or Zoya date is today or earlier"),
    (_F1, "either way set Next date 2 working days on", "either way set Zoya date 2 working days on"),
]
EDITS['zoya-slow-work.txt'].append((_F1, "rows at Status Sponsored offered whose Next date is today or earlier", "rows at Status Sponsored offered whose Zoya date is today or earlier (no Zoya date yet: its Next date once, as SELECT says)"))

# Fix 2 (23 Nov, Cleanup findings 2 and 3 on fix 1): decision 637 outside SLOW.
_F2 = 'F2-zoya-date'
EDITS['inbox-actions.txt'] += [
    (_F2, "NEXT DATE AND WAITING ON (decision 81). Next date belongs to the team. You set it in exactly five cases and never otherwise:",
          "NEXT DATE, ZOYA DATE AND WAITING ON (decisions 81, 637). Next date holds people's steps; Zoya date holds Zoya's own next step. You set Next date in three cases (a new lead, a calendar booking, a scheduling request) and Zoya date in two (a hold, a routine 5 start), and never otherwise:"),
    (_F2, "- A hold (decision 104): the guest or PR puts it on hold or gives a timing reason (STEP 3, LT chase). Next date = the date they give, else 90 days from today.",
          "- A hold (decision 104): the guest or PR puts it on hold or gives a timing reason (STEP 3, LT chase). Zoya date = the date they give, else 90 days from today (Zoya's revisit); Next date unchanged."),
    (_F2, "- A routine 5 start (STEP 2b c): Next date = the earliest open segment date on the row.",
          "- A routine 5 start (STEP 2b c): Zoya date = the earliest open Zoya segment date on the row; Next date unchanged."),
    (_F2, "Zoya in Waiting on; Next date = the earliest open segment date (NEXT DATE);",
          "Zoya in Waiting on; Zoya date = the earliest open Zoya segment date (NEXT DATE);"),
    (_F2, "Zoya added to Waiting on, Next date our last mail + 30 days, Chase step 0",
          "Zoya added to Waiting on, Zoya date our last mail + 30 days, Chase step 0"),
]
UPKEEP_EDITS += [
    (_F2, "- You never change Next date, with two exceptions: the hold below, and STEP 4's Form backstop (Next date = the earliest open segment date when you add the seq-5 segment). Next date belongs to the team; only a new lead (the inbox), a calendar booking (the calendar routine) or a hold sets it. The exception (decision 104): when mail shows the guest or PR put it on hold or gave a timing reason and you move the row to LT chase, set Next date to the date they give, else 90 days from today,",
          "- You never change Next date (decision 637: it holds people's steps; only a new lead or a calendar booking sets it). You set Zoya date, Zoya's own next step, in two cases only: STEP 4's Form backstop (Zoya date = the earliest open Zoya segment date when you add the seq-5 segment), and a hold (decision 104): when mail shows the guest or PR put it on hold or gave a timing reason and you move the row to LT chase, set Zoya date to the date they give, else 90 days from today,"),
    (_F2, "with Zoya in Waiting on and Next date = the earliest open segment date (the second Next date exception)",
          "with Zoya in Waiting on and Zoya date = the earliest open Zoya segment date (decision 637)"),
    (_F2, "whoever else Waiting on names, with Next date before today and no linked Activity of Kind Email out dated on or after that Next date.",
          "whoever else Waiting on names, with a due date before today and no linked Activity of Kind Email out dated on or after that date. The due date is Zoya date for Zoya's own step and Next date for a people's step (decision 637); a row with both overdue counts once, under the earlier date."),
    (_F2, "Parked or Form filled) and Next date today or earlier.",
          "Parked or Form filled) and Next date or Zoya date today or earlier."),
    (_F2, "with Next date empty and no Activity in 14 days",
          "with Next date and Zoya date both empty and no Activity in 14 days"),
]
EDITS['calendar.txt'].append((_F2, "Next action \"Zoya: ask Ranjita for the transcript\", Next date today,",
                                    "Next action \"Zoya: ask Ranjita for the transcript\", Zoya date today (decision 637),"))
EDITS['inbox-actions.txt'] += [
    (_F2, "LT chase, Next date = the date they give, else 90 days from today (decision 104)", "LT chase, Zoya date = the date they give, else 90 days from today (decisions 104, 637; Next date unchanged)"),
    (_F2, "Next date as NEXT DATE's fourth case", "Next date as NEXT DATE's scheduling-request case"),
    (_F2, "whatever the chase step or a chase Next date said", "whatever the chase step or a chase Zoya date said"),
    (_F2, "Eval link, Next action, Next date, Chase step", "Eval link, Next action, Next date, Zoya date, Chase step"),
]
UPKEEP_EDITS.append((_F2, "Tier, Payment, Next date, Next action", "Tier, Payment, Next date, Zoya date, Next action"))
EDITS['inbox-actions.txt'].append((_F2, "Waiting on and Next action: per decision 81 above. Next date only in the four cases above.", "Waiting on and Next action: per decision 81 above. Next date only in NEXT DATE's three cases; Zoya date only in its two."))
UPKEEP_EDITS += [
    (_F2, "only a new lead or a calendar booking sets it)", "only a new lead, a calendar booking or a scheduling request (decision 443) sets it)"),
    (_F2, "Window: since the previous sweep run (Friday's on a Monday)", "Window: since the previous upkeep report (Source ID \"upkeep:<date>\"; Friday's on a Monday)"),
]

# Fix 3 (23 Nov, CTO): 443 resets Zoya date to today; Zoya-inbox keys are eligible.
_F3 = 'F3-443-and-keys'
EDITS['inbox-actions.txt'] += [
    (_F3, "Query mail Activities (Kind Email in or Email out with Source ID msgid: or adid:, or Kind Meeting with Source Gemini notes)",
          "Query mail Activities (Kind Email in or Email out with Source ID msgid: or adid:, or a Zoya-inbox key mcpemails:, zoya: or zoyaid: (handled exactly as msgid: and adid: rows), or Kind Meeting with Source Gemini notes)"),
    (_F3, "and Zoya date in two (a hold, a routine 5 start), and never otherwise:",
          "and Zoya date in three (a hold, a routine 5 start, a scheduling request's reply owed now), and never otherwise:"),
    (_F3, "Next date = that date (a window: its first day; a date already past: today, the step keeps the date they asked for), replacing any Next date but a calendar booking's.",
          "Next date = that date (a window: its first day; a date already past: today, the step keeps the date they asked for), replacing any Next date but a calendar booking's; Zoya date = today, for the reply owed now (decision 637)."),
    (_F3, "Next date as NEXT DATE's scheduling-request case.",
          "Next date and Zoya date as NEXT DATE's scheduling-request case."),
    (_F3, "Zoya date only in its two.", "Zoya date only in its three."),
]
# Fix 3b (Cleanup on fix 3): who owns the 443 reply; how Zoya-inbox rows are read; capture dedupe.
_F3b = 'F3b-cleanup'
EDITS['inbox-actions.txt'] += [
    (_F3b, "Zoya date = today, for the reply owed now (decision 637).",
           "Zoya date = today when Zoya owns the reply owed now (decision 637); when it goes to Akshay (a Tier 1 row, a date today or tomorrow, a host-show recording), Zoya date untouched."),
    (_F3b, "a Zoya-inbox key mcpemails:, zoya: or zoyaid: (handled exactly as msgid: and adid: rows)",
           "a Zoya-inbox key mcpemails:, zoya: or zoyaid: (a provider id, not a Message-ID: read the message by that id in the mailbox the key names, Zoya's inbox unless it says ad:, take its Message-ID and work it as a msgid: row, THREAD searching Zoya's inbox as well as ad@; no Message-ID readable: as an adid: row, the subject search in that mailbox)"),
    (_F3b, "Yours only: its body has a \"capture:\" line (a row Captured before 2026-11-02 has none until capture's STEP 0 stamps it).",
           "Yours only: its body has a \"capture:\" line (a row Captured before 2026-11-02 has none until capture's STEP 0 stamps it; a row with a Zoya-inbox key needs none)."),
]
EDITS['inbox-capture.txt'].append((_F3b, "in every spelling older rows use: Source ID \"adid:<UID>\", \"allmail:<its MCP Emails id>\",",
    "in every spelling older rows use: Source ID \"adid:<UID>\", \"allmail:<its MCP Emails id>\", \"zoya:\", \"zoyaid:\" or \"mcpemails:\" followed by its MCP Emails id or its folder:UID,"))
EDITS['inbox-capture.txt'].append((_F3b, "followed by its MCP Emails id or its folder:UID,", "followed by its MCP Emails id, its folder:UID or (zoyaid:) its bare UID,"))

# Fix 4 (23 Nov, decisions 660, 661, 662).
_F4 = 'F4-free-feature'
EDITS['zoya-slow-work.txt'] += [
    (_F4, "7 days after the offer with still no interest, a Founder Thesis row goes on the Park proposals (PARKED) and a un# row to Status Unresponsive, note \"YYYY-MM-DD: no sponsored interest (decision 618)\".",
          "7 days after the offer with still no interest, a Founder Thesis row gets FREE FEATURE and a un# row Status Unresponsive, note \"YYYY-MM-DD: no sponsored interest (decisions 618, 661)\"."),
    (_F4, "then at most one short warm check-in on the primary thread, then nothing unless they write; that row goes on the Park proposals (PARKED).",
          "then at most one short warm check-in on the primary thread, then nothing unless they write; then a Founder Thesis sponsored lead gets FREE FEATURE, any other row the Park proposals (PARKED). A pending free feature (not money): one check-in 7 days after that mail instead."),
    (_F4, "founders who wrote to us directly whose no was to the sponsored price, at most one mail a quarter and only with a new reason to write;",
          "founders who wrote to us directly whose no was to the sponsored price, at most one mail a quarter, only FREE FEATURE's revival text, and only with a new reason to write;"),
    (_F4, "PAUSES ON THEIR WORD (",
          "FREE FEATURE (decisions 660, 661; Founder Thesis only). A sponsored lead silent 7 days after the offer, or after its fifth follow-up, gets the free feature offer once, never the Park proposals. Only the wording page's approved toggle for the case: one still PROPOSED is never sent, the step stays \"Zoya: free feature offer to <name> (wording awaiting Akshay)\" with its Zoya date. A yes: \"Feature interest: book the call with Akshay\". No reply: no chase.\nPAUSES ON THEIR WORD ("),
    (_F4, "A decline gets the sponsored close note from the wording page, from your inbox in your voice and signed as you, once: not if the thread already shows it or a \"sponsored close\" Activity is on the row (the inbox hands these to you as \"Zoya: send the sponsored close note to <name>\", older rows \"Zoya: send Akshay's sponsored close note to <name>\").",
          "The close note goes once, from your inbox in your voice: never if the thread shows it or a \"sponsored close\" Activity is on the row (the inbox hands it to you as \"Zoya: send the sponsored close note to <name>\")."),
]
EDITS['zoya-slow-work.txt'] += [
    (_F4, " (CTO, 4 Nov: 8 such items on the 17:08 run left no note line)", ""),
    (_F4, "(decisions 496, 535, 537; Akshay, 10 Nov: PaaS follow-ups 1 and 2 go on WhatsApp as him from the approved templates, and \"don't automate paas messages - propose the draft to me and I will finalise and check the box\")",
          "(decisions 496, 535, 537: follow-ups 1 and 2 go on WhatsApp as Akshay, from the approved templates, only as drafts he ticks)"),
]
EDITS['zoya-slow-work.txt'] += [
    (_F4, "COMMUNITY INVITE CHASE (decision 494, Akshay, 6 Nov).", "COMMUNITY INVITE CHASE (decision 494)."),
    (_F4, "which keeps the thread (CTO, 22 Nov), and", "which keeps the thread, and"),
    (_F4, "to the FT Community WhatsApp\" (Akshay, 5 Nov, item 14).", "to the FT Community WhatsApp\"."),
]
UPKEEP_EDITS += [
    (_F4, "5, 6c, 7b, then STEP 7.", "5, 6c, 7b, 7c, then STEP 7."),
    (_F4, "STEP 7. REPORT", "STEP 7c. PEOPLE LINKEDIN ENRICHMENT (decisions 659, 662). Read only: Reach MCP (ToolSearch \"+reach\"; missing: report \"step 7c: blocked: Reach not connected\" and go on). "
          "1/ QUOTA FIRST: get_account_quotas. Today's budget is 35 reads a day across every agent (decision 662) less the reads already used today, and never more than the account's own remaining daily quota; 0: report \"step 7c: done 0 (quota)\" and stop. "
          "2/ PICK, oldest relationship first, at most the budget: People rows with LinkedIn, Role or What they do blank who have a real relationship: FT guest ticked, In WhatsApp group ticked, an FT Community row, or an Engagement with an Email in Activity, a precall or a recording. Never a row whose only Engagements are cold outreach with no reply from them (untouched cold outreach stays out), never a team member (Tags Team), never a row with Tags \"No enrichment\". "
          "3/ READ, one person at a time: the LinkedIn URL on the row, else scrape_search on name plus company confirmed by scrape_profile (same name, same company or a past one on the row; not certain: skip, note it in the report, read nothing more for them). "
          "4/ WRITE only blank fields, never overwrite: LinkedIn, Role, What they do, City, Country; then Researched = today and one page-body line \"YYYY-MM-DD: LinkedIn via Reach (upkeep): filled <fields> (decision 662)\". Never a phone number or email from LinkedIn, never Tags, Blurb or Engagements. "
          "5/ STOP AT ONCE on any LinkedIn verification, captcha, checkpoint, sign-in prompt, rate or quota error: no retry today, report \"step 7c: stopped: <what> after <n> reads\", and put one line for the CTO on the run record. "
          "Report \"step 7c: done <n> read, <n> rows filled, <n> skipped (not certain), budget <b> of 35\".\nSTEP 7. REPORT"),
]
