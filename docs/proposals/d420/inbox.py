"""Decision 420 (Akshay, 28 Oct; CTO 13:35 JST): the inbox reads and writes ad@thepodium.in only through MCP Emails (IMAP,
inbox cd37e47e), never the Gmail connector, and sends only the "adding @Zoya" loop-in. Inbox first: it is down.
Usage: python3 inbox.py <live inbox prompt> <out file>. Input: 61,957 B / aed0215a8bdf6a26 (trig_0189eZvAD8x4357cfevgZ3No).
Also: the inbox's RUN RECORD (decision 419), whose "read to" line anchors the read window, so a run reads only new mail."""
import sys, os, hashlib
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "aed0215a8bdf6a26", "not the live inbox prompt"
dashes = s.count(chr(0x2014))
AD = "cd37e47e-89d8-4259-b907-9a243baf7048"

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# Size: history out of provenance notes; every decision number and rule stays.
for a, b in [
    ("MESSAGE IDENTITY (Codex, 22 Oct: four sends were logged twice, once per mailbox).", "MESSAGE IDENTITY."),
    (" (CTO, 22 Oct: a loop-in reopened a Parked thread).", "."),
    ("(decision 316, Akshay, 18 Oct: \"why is eximple in my queue? I already replied\")", "(decision 316)"),
    ("(decision 399, Akshay, 22 Oct: \"pure AI tell\")", "(decision 399)"),
    ("(decision 325, Akshay, 18 Oct: \"My queue is a decision inbox, not a notification inbox\")", "(decision 325)"),
    ("STEP 2b. AKSHAY'S SENT MAIL (decision 387 retired the draft-and-edit comparison of decision 102)",
     "STEP 2b. AKSHAY'S SENT MAIL (decision 387)"),
]:
    rep(a, b)

rep("You capture; apart from the replies in STEPS 6 to 6e,", "You capture; apart from the loop-ins in STEPS 6 to 6b,")
rep("TOOLS: Gmail, Notion, Google Calendar and Blueticks (WhatsApp) connectors. If their tools are deferred, load them with "
    "ToolSearch (\"+Gmail\", \"+Notion\", \"+Google_Calendar\", \"+bluetick\"). If Gmail or Notion is missing, stop and say so.",
    "TOOLS: MCP Emails, Notion, Google Calendar and Blueticks (WhatsApp) connectors. If their tools are deferred, load them with "
    "ToolSearch (\"+MCPEmail\", \"+Notion\", \"+Google_Calendar\", \"+bluetick\"). If MCP Emails or Notion is missing, stop and "
    "say so (RUN RECORD still written).\n"
    "MAILBOX (decision 420, Akshay, 28 Oct, after the Gmail connector's quota ran out): ad@thepodium.in is read and written only "
    "through MCP Emails, inbox_id " + AD + "; never call the Gmail connector. Reading leaves mail unread (decision 199 holds). "
    "Where a step below names a Gmail tool, use instead: a Gmail search: email_read search (from, to, subject, body, since; "
    "include_folders [\"inbox\", \"sent\"]); get_thread: THREAD; RAW or rfc822msgid: email_read original (decode it in Bash, keep "
    "only the Message-ID line); delete_draft: draft delete; unlabel_thread: email_organize archive (never flag read or unread). "
    "THREAD: a message plus every message in inbox and sent whose References or In-Reply-To holds its Message-ID or whose "
    "Message-ID its References hold (find them by email_read search on its subject words, since a week before it; read each with "
    "action read; include_html only where a step needs the HTML, such as Gemini notes). A new row's Source ID \"gmail:<thread "
    "id>\" is \"msgid:<the first message's Message-ID>\" (older gmail: ids stay as they are). An Activity's Link: "
    "https://mail.google.com/mail/u/0/#search/rfc822msgid%3A<Message-ID>. The only mail you send from ad@thepodium.in is the "
    "loop-in (ZOYA LIVE): email_compose action reply on that message, inbox_id as above, reply_all false, To its sender, Cc set "
    "explicitly, include_signature false, the loop-in line as body and html_body (<p>...</p>), no link, idempotency_key "
    "\"loopin:<that message's Message-ID>\".")
rep(" LINKS (decision 135): the Gmail connector turns links into google.com/url redirects with a warning page, so in mail to "
    "anyone outside the team every link is unlinked text, short as Akshay types it (podm.in/sponsored, podm.in/why-sponsor, "
    "podm.in/30min, podm.in/book, podm.in/guest-list, podm.in/community, podm.in/note, podm.in/pitch-to-us, podm.in/thank-you, "
    "unhashed.co/sponsored; a claude.ai link without https:// only to the team), its first dot broken with an empty span: "
    "podm<span>.</span>in/sponsored, claude<span>.</span>ai/artifact/... Never an <a> tag (keep its visible words), never "
    "http:// or https://, never tracking parameters. FORMAT (decisions 123, 184): always pass htmlBody, never plain text alone: "
    "each paragraph in its own <p>, lists as <ul><li>, short paragraphs; where a body below shows <br><br>, that is a new <p>. "
    "Never one block of lines joined with <br>: a mail must look typed by a person. Mail only to team members may keep normal "
    "links.",
    " LINKS: text you prepare for Zoya keeps each link as the wording page writes it (approved short links only); Zoya sends it "
    "from her inbox.")
rep("You send only the STEP 6 holding reply, STEP 6a, STEP 6b and WHATSAPP TO AKSHAY. Every other mail on every show (Akshay's "
    "decision mail, the sponsored close note, edit-notes, acknowledgement, admin, asset and routine replies, an approved "
    "proposal) is Zoya's: set Waiting on Zoya with \"Zoya: <step>\" first in Next action and log nothing as sent.",
    "You send only the loop-ins of STEPS 6 to 6b (MAILBOX; decision 420: the one mail agents send from ad@thepodium.in) and "
    "WHATSAPP TO AKSHAY. Every other mail on every show (Akshay's decision mail, the sponsored close note, edit-notes, "
    "acknowledgement, close and no-show notes, admin, asset and routine replies, an approved proposal) is Zoya's: set Waiting "
    "on Zoya with \"Zoya: <step>\" first in Next action and log nothing as sent; a mail only Akshay can send goes on his list as "
    "\"Akshay: <send what to whom>\".")
rep("- Mail actions allowed: only the sends,", "- Mail actions allowed, all through MCP Emails: only the sends,")

RUNREC = (
    "RUN RECORD (decision 419). Before any other Notion write, fix this run's id once: Bash printenv "
    "CLAUDE_CODE_REMOTE_SESSION_ID; if empty, once echo \"syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d "
    "' \\n')\"; if neither works, write no record and say so in the report. Then one Activity: Kind Note, Source empty, Summary "
    "\"Run inbox <YYYY-MM-DD HH:MM> JST: Started\", Source ID \"run:inbox:<run id>\", Date the start, Captured today, linked to "
    "nothing (an unclear create response: query that Source ID, reuse the row if found, else create it once; never a second). "
    "Your last write updates that row: Summary \"Run inbox <start> JST: <Completed|No-op|Partial|Failed>\", page body = the "
    "report plus the end time, a line \"read to <ISO time of the newest message read>\" once STEP 1's read finished (any "
    "status), counts, each error as its tool gave it (shortened) and what was skipped, with why. No-op: nothing was due. "
    "Partial: a step failed, was skipped or was cut short. Failed: the run stopped early, or a connector error, quota or rate "
    "limit left work undone; such a run is never Completed (an error a retry cleared is not a failure). The record never sets "
    "Last activity, Waiting on or a date on any row and never counts toward a cap. A failed record write: retry once, then "
    "report it.\n\n")
rep("STEP 1. WHAT TO READ\n", RUNREC + "STEP 1. WHAT TO READ\n")
rep("Find the newest Activity with Source = Gmail (SQL: ORDER BY \"date:Date:start\" DESC LIMIT 1). Start one day before that "
    "date; if there is none, start 3 days ago. Search Gmail for: after:YYYY/MM/DD -in:spam -in:trash -category:promotions "
    "-category:social\nThat covers sent mail too. Read every thread in full with get_thread.\n",
    "Start time T: 30 minutes before the \"read to\" time on the newest inbox run record that has one (a run whose read never "
    "finished has none, so its span is read again), never more than 3 days ago; none yet: the newest Activity with Source = "
    "Gmail (SQL: ORDER BY \"date:Date:start\" DESC LIMIT 1) minus one day; none at all: 3 days ago. email_read search, inbox_id "
    "as in MAILBOX, since <the day before T's date> (a date matches from midnight UTC), include_folders [\"inbox\", \"sent\"], every page (next_offset). Keep only messages dated at "
    "or after T; read each once (action read, then original for its Message-ID) and skip any whose msgid: key an Activity "
    "already holds. Read a message's THREAD only where a step needs the chain. An error: retry the call once after your next "
    "step that needs no mail; fails again: end Failed, naming it.\n")
rep("In Gmail only messageFormat RAW carries the header (Codex, 23 Oct: Zoya's acknowledgement to Pranav got a second Activity "
    "keyed \"gmail:\" because the other reads have no headers): for each new message under 200 KB (sizeEstimate), get it as RAW, "
    "decode it in Bash and keep only its Message-ID line.",
    "email_read read has no headers (23 Oct: a second Activity keyed by provider id): for each new message, read it with "
    "email_read original, decode it in Bash and keep only its Message-ID line.")
rep("Link: the thread's Gmail URL.", "Link: as MAILBOX gives it.")
rep("- Reply on the thread from ad@thepodium.in to Saurabh, Cc the house copies. Body, exactly:\n  \"Thanks for sharing, SG.\n\n"
    "  Thanks & Regards,\n  Akshay Datt\"\n",
    "- Nothing to Saurabh (decision 420: only loop-ins go from ad@thepodium.in); the original sender gets STEP 6's loop-in.\n")
i = s.find("- Log the reply as an Activity (Kind Email out, Summary \"Zoya sent: thanks to Saurabh\"")
j = s.find("Other forwards that are not guest pitches: capture only.")
assert 0 < i < j
s = (s[:i] + "A forward from Saurabh that is a vendor or service pitch (decision 124): STEP 6b's loop-in to the original sender "
     "(a new mail, subject \"Re: <original subject>\" without \"Fwd:\"; Saurabh not on it), nothing to Saurabh. Skip it if a "
     "loop-in already went out on that pitch. " + s[j:])
rep("send, never draft, a one-line reply on the thread from ad@thepodium.in, To the sender, Cc the house copies: \"thanks "
    "<first name>, pls could you fill out this form for us to evaluate your offering: podm.in/pitch-to-us\". Mail to team "
    "aliases (built2share@ and the like) counts. Log \"Zoya sent: vendor redirect to <name>\", within the daily cap.",
    "the loop-in on the thread, To the sender, Cc the house copies: \"thanks <first name>, adding @Zoya to coordinate\". Mail to "
    "team aliases (built2share@ and the like) counts. Log \"Akshay to <name>: Zoya loop-in\" and on its Engagement (Vendor show "
    "page 3fc19a301a7f811b829ae03fa68e235b, created as STEP 3 would) Waiting on Zoya, Next action \"Zoya: ask <first name> to "
    "fill podm.in/pitch-to-us\".")
rep("Search: in:inbox subject:(Accepted OR Declined OR \"Tentatively Accepted\") invitation\n",
    "Search: email_read search, inbox_id as in MAILBOX, folder inbox, subject \"invitation\", since 3 days ago.\n")
rep("remove the INBOX label only (unlabel_thread); never UNREAD.", "archive each message (email_organize archive); never flag read or unread.")
rep("End with a short report, nothing else written anywhere:", "End with a short report, in the run record (RUN RECORD) and as your final message:")
rep("- Pitch replies sent (guest names; Saurabh forwards thanked).", "- Loop-ins sent (names).")

assert s.count(chr(0x2014)) == dashes and len(s.encode()) <= 65536 - 200, len(s.encode())
assert "(unlabel_thread)" not in s and "get it as RAW" not in s and "in:inbox subject" not in s
open(dst, "w", encoding="utf-8").write(s)
b = s.encode(); print(os.path.basename(dst), len(b), hashlib.sha256(b).hexdigest()[:16], "headroom", 65536 - 200 - len(b))
