"""r25 item 1: WhatsApp automation (decisions 535 and 537, Akshay, 10 Nov; spec 41419a301a7f8130a4ebeabffd289e35,
templates 41419a301a7f81ea8e73e0deb08052aa). Built on the live r24 prompts (deploy 311e607).
Usage: python3 patch.py <wa|act|cap> <live input> <out>; inputs r24/whatsapp.txt (bec8c1e1), r24/actions.txt (845d0a41),
r24/capture.txt (f64eb54e, decision 538).
- wa: STEP 0w becomes the one SEND step (ticked drafts and checked standing templates, the 486/522 chaser path folded
  in); 0a e0 writes the standing community invite; STEP 3n is the Saturday community news scan (drafts only).
- act: the section 6 pointer says the chaser goes in the WhatsApp draft column for Akshay's tick.
Each edit is asserted once (a span edit: each marker once, end after start); no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"wa": "bec8c1e1", "act": "845d0a41", "cap": "f64eb54e"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the live %s" % which
s = b.decode("utf-8")
TPL = "41419a301a7f81ea8e73e0deb08052aa"
SEND = (
 "STEP 0w. SEND WHATSAPP AS AKSHAY (decisions 486, 522, 535, 537; every run). The only path that sends from Akshay's number to anyone outside the team. "
 "Take each Engagement whose \"WhatsApp draft\" is not empty and either (a) \"Send WhatsApp\" is ticked: his approval of exactly the text now in the draft; or (b) the draft's first line is \"[standing: <template>]\" for an approved standing template on \"WhatsApp templates (sent as Akshay)\" (" + TPL + "), and its check holds: "
 "community-invite: one of the two exact note lines its writers produce, naming this person, \"Akshay's call: 'invite <name>' (WhatsApp); standing invite drafted\" (STEP 0a e0) or \"Akshay's call: 'invite <name>'; standing invite drafted\" (section 6), never any other note quoting \"invite\"; a recording on the row, and the person's FT Community row at To invite or Invited, never Added; "
 "release-day: a Claude note line \"YYYY-MM-DD: release-day WhatsApp drafted (Episode copywriter chat)\", the guest's Episode at Published or with Actual release set, and the draft holds that Episode's Short link. "
 "Only those two are standing: nothing on a PaaS row goes without his tick (Akshay, 10 Nov: \"don't automate paas messages\"). "
 "A standing line whose check fails, or written by anyone else: send nothing, leave the draft, add \"Akshay: tick Send WhatsApp: <first name> (<template> check failed: <why>) (<D Mon>)\", Akshay in Waiting on. Any other unticked draft waits. "
 "SPELLING (decision 539), before 1/: fix only obvious typos (podast -> podcast), never wording, case, punctuation, names, numbers, links or a doubtful word; write the fixed draft back (the one change allowed while ticked), Claude note line \"YYYY-MM-DD: spelling fixed: <old> -> <new>\". "
 "1/ Messages (Akshay, 10 Nov): split the draft in Bash python: a line starting \"<n>/ \" (1/, 2/, 3/ ...) starts a new message, which runs to the next such line; strip that prefix and blank lines at each end; text before the first such line is a message too; no such line: the whole draft is one message. A \"[standing: ...]\" or \"[to: ...]\" line is never sent, nor counted as text. Recipient: the person a first line \"[to: <full name>]\" names (the row's Guest, Via or a Stakeholder), else the row's Guest; \"[to: group The Founder Thesis Community, tag <full name>]\" is a news post (3/). "
 "2/ Key \"wa-send:<row id>:<the first 12 hex of the sha256 of the draft text, in Bash python>\": an Activity with that Source ID whose Summary starts \"Akshay to\" means it went: send nothing, just finish 6/; one starting \"Zoya sending\": read that chat's recent messages (list_messages) for each message before any resend; one found is never sent again. "
 "3/ Before a send, all must hold: outside quiet hours (01:30 to 07:30 JST, decision 547), and release-day only after 10:00 IST; fewer than 20 sets sent today (Activities whose Source ID starts \"wa-send:\" or \"wa-chase:\" and Summary starts \"Akshay to\", dated today in JST; one person's set counts once); and no set from his number to that person in the last 7 days (spec section 4: Activities whose Summary starts \"Akshay to <name> on WhatsApp\", Source ID \"wa-send:\" or \"wa-chase:\"; his own typed replies in the chat never count); else it waits, untouched, for the run when it may go. "
 "NO REPLY: nothing from that person since our last message to them, in ad@thepodium.in and Zoya's inbox (MCP Emails, read only, by every address on their People row) and in their WhatsApp chat with Akshay (list_messages since our last message), or any Email in Activity on the row from their side (Guest, Via or a Stakeholder) dated after the draft was written; a reply: send nothing, untick, add \"Akshay: <name> replied, draft held (<D Mon>)\", Akshay in Waiting on. "
 "NUMBER (decision 535): the recipient's People Phone only, with its country code (a leading + or 00); never a number from FT Community, a chat search, a thread, a signature, a form or memory; chat id = its digits, then \"@c.us\". None, or no country code: send nothing, untick, add \"Akshay: no WhatsApp number for <name>\", Akshay in Waiting on. "
 "A news post goes to the group named exactly \"The Founder Thesis Community\" (chats search, chatType group), at most one per member a quarter (Activities); the text holds \"@<their digits>\" with mentions [\"<their digits>@c.us\"] from their People Phone; NO REPLY and the 7-day rule don't apply. "
 "TIMING (Akshay, 10 Nov: \"I will put the send day/time in my call. don't schedule.\"): a ticked draft goes at the time Akshay names for it, in the row's Your call or in a Claude note line keeping his call written since the draft (\"Akshay's call: '...'\"), IST unless he names a zone; none named: it goes this run. You never choose a time: no window, no default delay. A day or time without a full date (\"tue 10am\", \"6pm\") is the next such time after the date he wrote it, never a past one. A named time already past at the run: it goes now only if he wrote a full date; otherwise send nothing, add \"Akshay: WhatsApp time '<his words>' passed: new time? (<D Mon>)\", Akshay in Waiting on. "
 "A named time still ahead: run 3/'s checks now (the cap and the 7-day rule on the day he named; his time stands even inside quiet hours), log as 4/ but with Summary \"Zoya scheduled: WhatsApp to <name> for <D Mon HH:MM IST>\", queue each message with scheduled_messages_write send (to: the chat id; send_at: that time with its offset, each next message 5 seconds after the one before), add the Claude note line \"YYYY-MM-DD: WhatsApp scheduled for <D Mon HH:MM IST> (<Blueticks ids>)\", untick the box and keep the draft; an Activity with that key at \"Zoya scheduled\", or a \"WhatsApp scheduled for\" note line on the row whose ids scheduled_messages_read get shows still pending, means it is never queued again. A re-tick, or a draft whose sha12 differs from that Activity's key, with ids still pending: cancel each id first (scheduled_messages_write cancel), Claude note line \"YYYY-MM-DD: scheduled WhatsApp cancelled (re-ticked or edited)\", then treat it as a new draft. Each later run before that time: NO REPLY again; a reply: cancel each id (scheduled_messages_write cancel), add \"Akshay: <name> replied, scheduled WhatsApp cancelled (<D Mon>)\", Akshay in Waiting on. At or after that time: scheduled_messages_read get each id; all sent: 5/ and 6/; any failed: 5/'s failure. "
 "4/ Log first: one Activity, Kind WhatsApp, Source WhatsApp, Source ID the key, Summary \"Zoya sending: WhatsApp to <name>\", Engagement, People, Date and Captured today. Then send each message in order, to the same chat, with chats_write send_message_text (idempotency_key: the key's last 40 characters plus \"-<message number>\"), a Bash sleep 5 between messages, exactly as written: no signature, no Zoya, nothing added. "
 "5/ Sent: rename the Activity \"Akshay to <name> on WhatsApp: <one line, no number>\", the sent text and every message id in its body (one Activity per set; the cap, the 7-day rule and the key count the set as one send). Failed: rename it \"WhatsApp send failed: <name> (<error>)\", clear its Source ID, untick, add \"Akshay: the WhatsApp to <first name> failed (<error>)\", Akshay in Waiting on, and stop for this row. "
 "6/ Clear \"WhatsApp draft\" and untick \"Send WhatsApp\", remove the row's \"Akshay: tick Send WhatsApp: ...\" segment (and Akshay from Waiting on unless another segment of his stays), Claude note line \"YYYY-MM-DD: WhatsApp sent as Akshay to <name> (<template, or approved>)\". Their reply comes in through STEP 2 as any message does. No routine changes a draft while its box is ticked (SPELLING aside).\n"
)
INVITE = ("Reply \"Zoya ✨ noted: <name> is on your invite list\" (decision 310).",
 "Then, when they have recorded (decision 537), write the standing invite on their Founder Thesis Engagement's \"WhatsApp draft\" unless it holds text: the line \"[standing: community-invite]\", then the community invite lines from the templates page (" + TPL + ", section 1) with {first name} from People and {rounded member count} and the member list from the invite kit page, each template message starting \"<n>/ \" (1/, 2/ ...) in order, the member list one message; Claude note line \"YYYY-MM-DD: Akshay's call: 'invite <name>' (WhatsApp); standing invite drafted\". STEP 0w sends it this run or the next. Reply \"Zoya ✨ noted: <name> is on your invite list\" (decision 310), plus \"invite goes out at the next run\" when drafted, or \"no WhatsApp number on their People row\" when it has none.")
NEWS = ("\nSTEP 3n. COMMUNITY NEWS (decision 535; the first run on a Saturday, JST; drafts only, never a send). For FT Community rows at Added, at most 25 a run, those with no \"news checked\" Activity in the last 28 days first: web search for news about the member or their company in the last 7 days (funding, launch, award, listing). Each hit you verify (an article with a URL and a date within those 7 days), on a member with no news post Activity in the last 90 days: on their Founder Thesis Engagement, unless its \"WhatsApp draft\" holds text, write the draft: the line \"[to: group The Founder Thesis Community, tag <full name>]\", then a fresh short post in Akshay's voice (not a template, Akshay, 10 Nov: \"don't templatise it\"): lowercase, 1 to 3 lines, tags the member as \"@<their name>\", includes the article link, no em dashes, nothing private; add \"Akshay: tick Send WhatsApp: news post for <first name> (<D Mon>)\", Akshay in Waiting on. One Activity per member checked, Summary \"news checked: <name> (<hit or none>)\".\n")
EDITS = {
"cap": [
 # Decision 538 (Akshay, 10 Nov): a pitch's Show comes from what it names or fits, not the address it reached.
 ("Show = the one of ours the mail names (un#, which mail may call Unhashed; Built to Share; Human by Design); anything else is Founder Thesis.",
  "Show = the one of ours the mail names (un#, which mail may call Unhashed; Built to Share; Human by Design); anything else is Founder Thesis. The address it came to alone never decides: a pitch to a client-show inbox (un#, Built to Share, Human by Design) with no link to that show's subject (un#: crypto and web3; Built to Share: teams, leadership, ownership; Human by Design: AI and human outcomes) is Founder Thesis (decision 538)."),
 # Decision 541 (Akshay, 10 Nov): every new pitch row starts on Akshay's list, never with Waiting on empty.
 ('Waiting on empty (Founder Thesis and un#: the evals routine sets it; Built to Share and Human by Design: inbox actions STEP 5)',
  'Waiting on Akshay, Next action "Akshay: new pitch from <PR or self> for <guest>, eval running (captured <D Mon HH:MM>)" on every show (decision 541; the eval, or inbox actions STEP 5 on Built to Share and Human by Design, replaces it)'),
 # Decision 547 (Akshay, 11 Nov): quiet hours are on Cadences (01:30 to 07:30 JST); the prompt cites no numbers.
 ('in the quiet hours on Cadences (read them there; decision 393: 00:30 to 07:30 JST);', 'in the quiet hours on Cadences (read them there; decision 547);'),
],
"wa": [
 ("for STEP 0d also Gmail and MCP Emails (read only) and Google Calendar", "for STEP 0d and STEP 0w's reply check also Gmail and MCP Emails (read only), and for 0d Google Calendar"),
 ("and STEP 0w sends one guest chaser as Akshay, only the text he approved, to that person's number (decisions 486, 519).",
  "and STEP 0w sends as Akshay (now, or scheduled at the time he names) only a draft he ticked or a checked standing template, to that person's People Phone or, for a news post, the FT Community group (decisions 486, 535)."),
 (("STEP 0w. APPROVED WHATSAPP CHASERS", "Their reply comes in through STEP 2 as any message does.\n"), SEND),
 INVITE,
 ("\nSTEP 3d. COMPLETE THE ROWS TO ADD", NEWS + "\nSTEP 3d. COMPLETE THE ROWS TO ADD"),
 ("in this order: 0, 0d, 0w, 1, 2, 2b, 3, 3d, 4:", "in this order: 0, 0d, 0w, 1, 2, 2b, 3, 3n, 3d, 4:"),
 ("WhatsApp chasers (STEP 0w: sent, waiting for quiet hours or the cap, failed, no number, by name);",
  "WhatsApp sends (STEP 0w: sent by template or tick, held for a reply, waiting for quiet hours or the cap, failed, no number, check failed, by name); news drafts (STEP 3n: names);"),
],
"act": [
 ("you only draft it on the row and queue it for the WhatsApp routine on Akshay's ok; you never send it.",
  "you only write the row's \"WhatsApp draft\" for his tick in \"Send WhatsApp\" (decision 535), and a Your call \"invite <name>\" writes the standing invite draft as section 6 says; the WhatsApp routine sends; you never send it."),
 # Decision 541: STEP 5's ask replaces capture's new-pitch segment on Built to Share and Human by Design.
 ('- A pitch for Built to Share or Human by Design: Akshay, "Akshay: new <show> pitch via <PR>: put it on <host>\'s board, decline or park?".',
  '- A pitch for Built to Share or Human by Design: Akshay, "Akshay: new <show> pitch via <PR>: put it on <host>\'s board, decline or park?", replacing capture\'s "Akshay: new pitch from" segment.'),
 # Decision 547 (Akshay, 11 Nov): quiet hours are on Cadences (01:30 to 07:30 JST); the prompt cites no numbers.
 ('in the quiet hours on Cadences (decision 393: 00:30 to 07:30 JST);', 'in the quiet hours on Cadences (decision 547);'),
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
