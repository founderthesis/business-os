"""Decision 420 batch (CTO 28 Oct 13:35 JST): calendar, sweep, WhatsApp, evals and dossiers read ad@thepodium.in only through
MCP Emails, never the Gmail connector; drafts for Akshay go through MCP Emails draft; no agent mail from ad@ but the loop-in.
Usage: python3 batch.py <input dir> <output dir>; inputs <trigger id>.txt as for docs/proposals/r-runrec/build.py.
Zoya's FAST prompt and SLOW file change through routines/zoya/parts (build_one.py), not here."""
import sys, os, hashlib
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
AD = "cd37e47e-89d8-4259-b907-9a243baf7048"

def mailbox(drafts=False):
    return ("MAILBOX (decision 420, Akshay, 28 Oct, after the Gmail connector's quota ran out): read ad@thepodium.in only "
            "through MCP Emails (inbox_id " + AD + "), never the Gmail connector, also inside every skill you run (a skill "
            "step that says Gmail means this); reading leaves mail unread (decision 199 holds). Where a step says Gmail, use: "
            "a search: email_read search (from, to, subject, body, since; include_folders [\"[Gmail]/All Mail\"], which holds "
            "inbox, sent and archived mail once each; in:sent means folder \"[Gmail]/Sent Mail\"); a message by Message-ID: email_read search with "
            "text = that Message-ID; a thread: the message, the messages its References name and every message whose headers "
            "hold its Message-ID (search text = it), each read with action read; a \"gmail:<thread id>\" Source ID: the most "
            "recent thread with the guest's name from the guest's or PR's address; a Message-ID header: email_read original."
            + (" A draft: MCP Emails draft (action create for a new mail with to and cc; action reply on a thread's latest "
               "message, then action update to set To and Cc, since a reply draft can't take them at creation) on that inbox, "
               "body plus html_body; never sent by you; log the draft_id the last call returned (it changes on every update)." if drafts else "") + "\n")

def patch(tid, name, ok, edits, mb_after=None, drafts=False):
    s = open(os.path.join(src, tid + ".txt"), encoding="utf-8").read()
    h = hashlib.sha256(s.encode()).hexdigest()[:16]
    assert h in ok, (name, h)
    dashes = s.count(chr(0x2014))
    for a, b in edits:
        assert s.count(a) == 1, (name, a[:60], s.count(a))
        s = s.replace(a, b)
    if mb_after:  # its own line right after the TOOLS line
        i = s.find("\n", s.index("TOOLS:"))
        s = s[:i + 1] + mailbox(drafts) + s[i + 1:]
    out = s.encode()
    assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200, (name, len(out))
    open(os.path.join(dst, name + ".txt"), "wb").write(out)
    print(f"{name:9s} in {h} out {len(out):6d} {hashlib.sha256(out).hexdigest()[:16]} headroom {65536 - 200 - len(out)}")

patch("trig_01Voiz5YsK2SnVf2STF8PoSH", "calendar", {"8fb664a1c94776b5"}, [
    ("TOOLS: Google Calendar, Notion, Gmail, Google Drive and MCP Emails connectors (ToolSearch \"+Google_Calendar\", \"+Notion\", "
     "\"+Gmail\", \"+Google_Drive\", \"+MCPEmail\" if deferred), and the Skill tool. MCP Emails sends Akshay's mail from "
     "ad@thepodium.in (inbox_id " + AD + ") and Zoya's",
     "TOOLS: Google Calendar, Notion, Google Drive and MCP Emails connectors (ToolSearch \"+Google_Calendar\", \"+Notion\", "
     "\"+Google_Drive\", \"+MCPEmail\" if deferred), and the Skill tool. MCP Emails reads Akshay's ad@thepodium.in (inbox_id "
     + AD + "; MAILBOX) and sends Zoya's"),
    ("from the right inbox (Akshay's mail from ad@thepodium.in, Zoya's from zoya@myunnati.com)",
     "from Zoya's inbox zoya@myunnati.com (from ad@thepodium.in agents send only the loop-in, decision 420)"),
    ("Drafts stay Gmail create_draft with the same <p> layout.", "Drafts: MCP Emails draft on ad@thepodium.in (MAILBOX), same <p> layout."),
    ("Gmail use is otherwise limited to reading threads and creating drafts.",
     "ad@thepodium.in is otherwise only read (MAILBOX) and drafted in."),
    ("in ad@thepodium.in with the Gmail connector (create_draft; a reply on the latest thread with the guest or PR, else a new mail),",
     "in ad@thepodium.in with MCP Emails (draft: a reply on the latest thread with the guest or PR, else a new mail),"),
    ("Tags PR contact, Source Agent, Source ID \"gmail:<thread id>\", Captured today). Set Via",
     "Tags PR contact, Source Agent, Source ID \"msgid:<the thread's first Message-ID>\", Captured today). Set Via"),
    ("in ad@thepodium.in with the Gmail connector: create_draft as a NEW mail,", "in ad@thepodium.in with MCP Emails: draft create as a NEW mail,"),
], mb_after=True, drafts=True)


patch("trig_01MdfUFg2qrebDWgiHwncgnd", "sweep", {"7af60faaa021fa64"}, [
    ("TOOLS: Notion and Gmail connectors (ToolSearch \"+Notion\", \"+Gmail\" if deferred).",
     "TOOLS: Notion and MCP Emails connectors (ToolSearch \"+Notion\", \"+MCPEmail\" if deferred)."),
    ("The Gmail connector turns every link into a google.com/url redirect that shows readers a warning page, so in outside mail "
     "every link is unlinked text: write it short, as Akshay types it, and break its first dot with an empty span so Gmail does "
     "not turn it into a link: podm<span>.</span>in/sponsored. Never an <a> tag (strip any a template carries and keep the "
     "visible words), never http:// or https://, never tracking parameters. Always pass the mail text as htmlBody (plain lines "
     "joined with <br>); never a plain-text body alone (decision 123). Mail only to team members may keep normal links.",
     "Drafts carry real links to the approved short links (<a href=\"https://podm.in/30min\">podm.in/30min</a>), html_body "
     "with one <p> per paragraph plus a plain-text body, never tracking parameters."),
    ("Create a Gmail draft from ad@thepodium.in:", "Create a draft in ad@thepodium.in (MAILBOX):"),
    ("Search Gmail since 4 days ago (-in:sent -in:spam -in:trash). Forward to Jaya (the Email on her People row, tagged Team; "
     "never typed from memory; Akshay, 15 Oct) every mail",
     "Search ad@thepodium.in (MAILBOX; not mail from ad@thepodium.in itself) since 4 days ago. Forward to Jaya (the Email on her "
     "People row, tagged Team; never typed from memory; Akshay, 15 Oct) every mail"),
    ("Use Gmail forward on that message (attachments travel with it), forwardText \"For the tax records: <vendor or client>, "
     "<what it is>, <amount if shown>.\" Never forward:",
     "Use MCP Emails email_compose forward on that message, inbox_id as in MAILBOX (decision 423; attachments travel with it), "
     "include_signature false, idempotency_key \"billing:<its Message-ID>\", body \"For the tax records: <vendor or client>, "
     "<what it is>, <amount if shown>.\" Never forward:"),
    ("Once per message, by Gmail message id, never by subject (one vendor sends many invoices under one subject): before "
     "forwarding, skip the message if an Activity whose Summary starts \"Zoya sent: billing doc to Jaya\" or \"Agent sent: "
     "billing doc to Jaya\" already holds its message id as Source ID. Forwards logged before 16 Oct hold the sent forward's id "
     "instead, so for a message older than 16 Oct also skip it if Sent has a forward to Jaya of that same message (same sender "
     "and date). Log one Activity per forward (Kind Email out, Summary \"Zoya sent: billing doc to Jaya: <vendor>, <what>\", "
     "Source Gmail, Source ID = the forwarded original message's Gmail id, Captured today); these count toward the daily cap.",
     "Once per message, by RFC Message-ID, never by subject (one vendor sends many invoices under one subject): before "
     "forwarding, skip the message if an Activity whose Summary starts \"Zoya sent: billing doc to Jaya\" or \"Agent sent: "
     "billing doc to Jaya\" already holds it as Source ID (msgid:<Message-ID>), or if [Gmail]/Sent Mail has a forward to Jaya "
     "of that same message (same subject, sender and date; this also covers forwards logged with a Gmail id before 29 Oct, and "
     "a forward sent before its Activity was written). Log one Activity per forward (Kind Email out, Summary \"Zoya sent: billing doc to Jaya: <vendor>, "
     "<what>\", Source Gmail, Source ID \"msgid:<the original's Message-ID>\", Captured today); these count toward the daily cap."),
    ("Never send mail other than STEP 6c (billing forwards to Jaya), within the daily cap on the Notion page \"Cadences\" "
     "(3ff19a301a7f8143aa95cd89bd6519ec; decision 317, JST);", "Never send mail other than STEP 6c (billing forwards to Jaya through "
     "MCP Emails, decisions 420 and 423), within the daily cap on the Notion page \"Cadences\" "
     "(3ff19a301a7f8143aa95cd89bd6519ec; decision 317, JST);"),
    ("For rows at Unresponsive or LT chase whose Claude note has \"revival checked",
     "For rows at Unresponsive or LT chase (never a un# sponsored pursuit, decision 422: a un# row whose thread has our "
     "sponsored offer, the first mail linking unhashed.co/sponsored) whose Claude note has \"revival checked"),
], mb_after=True, drafts=True)

patch("trig_01MnmJYorWrd61K7b5BCqXr1", "whatsapp", {"9e8b9f4891e9c03d", "1afc777019d1aefd", "051764ff6b21b716"}, [
    ("for STEP 0d also Gmail and MCP Emails (read only) and Google Calendar (ToolSearch \"+Gmail\", \"+MCPEmail\", "
     "\"+Google_Calendar\")",
     "for STEP 0d also MCP Emails (read only) and Google Calendar (ToolSearch \"+MCPEmail\", \"+Google_Calendar\")"),
    ("(Gmail on ad@thepodium.in and MCP Emails on Zoya's inbox, read only)",
     "(MCP Emails on ad@thepodium.in, inbox_id " + AD + ", and on Zoya's inbox, read only; never the Gmail connector, decision 420)"),
    ("thank-you drafts waiting in Gmail", "thank-you drafts waiting in Akshay's Drafts"),
], mb_after=True)

patch("trig_01R1yHgEztVEo832zMwUugBr", "evals", {"1d87f124107a06c6"}, [
    ("TOOLS: Notion and Gmail connectors (ToolSearch \"+Notion\", \"+Gmail\" if deferred), the Skill tool, and the Artifact "
     "tool. If Notion, Gmail or the Artifact tool is missing, stop and say so. Gmail is read only: you read pitch threads and "
     "never send, reply, draft, label or mark anything read.",
     "TOOLS: Notion and MCP Emails connectors (ToolSearch \"+Notion\", \"+MCPEmail\" if deferred), the Skill tool, and the "
     "Artifact tool. If Notion, MCP Emails or the Artifact tool is missing, stop and say so. Mail is read only: you read pitch "
     "threads and never send, reply, draft, move or mark anything."),
    ("(Gmail get_thread on the thread id in Source ID \"gmail:<thread id>\", or else the Gmail Link on the latest Email in "
     "Activity linked to the Engagement)",
     "(MAILBOX: the thread of the latest Email Activity linked to the Engagement, by its msgid:, else by the guest's or PR's "
     "address)"),
    ("Gemini notes mails in Gmail", "Gemini notes mails in ad@thepodium.in (MAILBOX)"),
], mb_after=True)

patch("trig_01WfLf8Zx9c34fSzfrTeUY5M", "dossiers", {"68e94cb7d30ca645"}, [
    ("it has already searched Drive and Gmail;", "it has already searched Drive and ad@thepodium.in (MAILBOX);"),
    ("TOOLS: Notion, Gmail and Google Drive connectors (ToolSearch \"+Notion\", \"+Gmail\", \"+Google_Drive\" if deferred)",
     "TOOLS: Notion, MCP Emails and Google Drive connectors (ToolSearch \"+Notion\", \"+MCPEmail\", \"+Google_Drive\" if deferred)"),
    ("and the pitch thread in Gmail (Source ID \"gmail:<thread id>\").",
     "and the pitch thread in ad@thepodium.in (MAILBOX; Source ID \"gmail:<thread id>\" or msgid:)."),
], mb_after=True)
