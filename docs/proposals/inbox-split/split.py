"""Split the live inbox prompt into two routines (CTO, 1 Nov 18:35 JST; the 20 Oct audit's structural fix).

Input: the live inbox, 65,227 / 3bb46f9332241e3b (docs/proposals/inbox-msgid/cleanup/inbox.txt).
Usage: python3 split.py <live.txt> <outdir>   -> <outdir>/capture.txt, <outdir>/actions.txt, <outdir>/map.txt

Every block of the live prompt goes to capture, to actions, to both, or (STEP 7b) to the daily sweep; map.txt lists each
block's destination so nothing is lost. Blocks are copied verbatim and located by their opening words (asserted);
only the framing lines marked NEW below are new text.
"""
import hashlib, os, sys

src, outdir = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "3bb46f9332241e3b"
P = s.split("\n\n")
os.makedirs(outdir, exist_ok=True)


def para(i, start):
    assert P[i].startswith(start), (i, P[i][:60])
    return P[i]


def lines(i):
    return P[i].split("\n")


def line(i, start):
    hits = [l for l in lines(i) if l.startswith(start)]
    assert len(hits) == 1, (i, start, len(hits))
    return hits[0]


def bullets(i, starts):
    """The bullets of paragraph i that start with one of `starts` (each bullet is one line)."""
    out = []
    for st in starts:
        out.append(line(i, st))
    return "\n".join(out)


MAP = []


def take(dest, name, text):
    MAP.append((dest, name, len(text.encode())))
    return text


# ---- shared blocks (verbatim) ----
tools_mailbox = line(1, "MAILBOX (decision 420)")
loopin = line(1, "LOOP-IN (decision 421)")
notion_head = "\n".join(lines(2)[:2])  # "NOTION" + WRITES
assert lines(2)[0] == "NOTION" and lines(2)[1].startswith("WRITES:")
sources = "\n".join(lines(2)[2:13])
assert lines(2)[2].startswith("- Activities:") and lines(2)[12].startswith("- Episodes:")
wording = line(2, "WORDING (decisions 98, 194)")
context = line(2, "CONTEXT CHECK (decision 216)")
bounces = line(2, "BOUNCES (decision 217)")
roles = line(2, "TEAM ROLES (decisions 154, 223, 352)")
yourcall = line(2, "YOUR CALL (decision 157")
whatsapp = line(2, "WHATSAPP TO AKSHAY (decision 182)")
copies = line(2, "HOUSE COPIES (decisions 180, 305, 352)")
zoyalive = line(2, "ZOYA LIVE (decisions 207, 223, 307, 323")
cadences = line(2, "CADENCES (CTO, 20 Oct)")
fetch = line(2, "Fetch each data source once")
hard = para(3, "HARD RULES")
nextdate = para(4, "NEXT DATE AND WAITING ON (decision 81)")
runrec = para(5, "RUN RECORD (decision 419)")
step1 = para(6, "STEP 1. WHAT TO READ")
skip = para(7, "Skip, without logging:")
step2 = para(8, "STEP 2. ONE ACTIVITY PER EMAIL")
gemini = para(9, "Gemini meeting notes mails:")
step2b = para(10, "STEP 2b. AKSHAY'S SENT MAIL")
matching = para(11, "MATCHING PEOPLE")
forwards = para(12, "MAIL AKSHAY FORWARDS FROM HIS OTHER ADDRESSES")
step3_head = para(13, "STEP 3. ENGAGEMENTS (guest conversations)")
S3 = 14
assert P[S3].startswith("- A PR person or guest pitches a guest")
s3_capture = bullets(S3, ["- A PR person or guest pitches a guest", "- We invite someone (outbound)",
                          "- A different guest is proposed (decision 162)"])
s3_actions = bullets(S3, ["- They reply yes to an outbound invite", "- Akshay decides:", "- A precall happened",
                          "- A recording date is agreed", "- Slots, availability or logistics", "- The thank-you mail",
                          "- Edit notes on a recorded episode", "- The guest's form is in", "- They say no:",
                          "- They turn down the sponsored route", "- They put it on hold", "- \"Add to outbound\"",
                          "- Sponsored money on FT is Zoya's"])
assert len(lines(S3)) == 16, len(lines(S3))
also = para(15, "Also on every Engagement you touch:")
also_capture = "Also on every Engagement you touch:\n" + line(15, "- Stakeholders (decision 144)")
also_actions = "Also on every Engagement you touch:\n" + "\n".join(
    [line(15, "- Waiting on and Next action:"), line(15, "- Chase step:")])
assert len(lines(15)) == 4
step4 = para(16, "STEP 4. DEALS")
step5 = para(17, "STEP 5. WHO IS IT WAITING ON")
step6 = para(18, "STEP 6. NEW PITCH: ADD ZOYA")
step6a = para(19, "STEP 6a. GUEST PITCHES FORWARDED BY SAURABH GARG")
step6b = para(20, "STEP 6b. VENDOR PITCH REDIRECT")
step6c = para(21, "STEP 6c. AKSHAY DECIDED ON THE ROW")
step6d = para(22, "STEP 6d. ADMIN AND LOGISTICS ASKS")
step6e = para(23, "STEP 6e. NO ROUTINE MAIL LEFT HANGING")
step7 = para(24, "STEP 7. ARCHIVE CALENDAR RSVP MAIL")
step7b = para(25, "STEP 7b. GUEST FORM SUBMISSIONS")
report = para(26, "STEP 8. REPORT")
fail = para(27, "If a step fails")
assert len(P) == 28

# ---- NEW framing text ----
CAP_INTRO = (
    "You are ThePodium's inbox capture. ThePodium is a podcast agency run by Akshay Datt (Osaka, JST); the team is in India. "
    "You read the ad@thepodium.in mailbox and log each mail once in Notion, linked to its Engagement or Deal and its People. "
    "You never handle Your call or apply a decision, and move a Status only where STEP 3's creating bullets say so; the "
    "inbox actions routine does the rest from what you log, and rules here naming STEPS 2b, 4, 5, 6c to 6e, Your call or "
    "WhatsApp to Akshay are its: leave them. Your only "
    "mail is the loop-in (STEPS 6 to 6b) and your only other mailbox action is RSVP archiving (STEP 7). HOURLY "
    "(AR-20261019-6): only new or unfinished work; more runs never mean more mails.\n"
    "CURSOR, NOT PRECEDENT: from the newest inbox capture run record read only its Summary's \"read to\" and its body's "
    "\"pending:\" line. Never read or cite another run's report: what an earlier run skipped is never a reason to skip.")
CAP_TOOLS = ("TOOLS: MCP Emails and Notion connectors. If their tools are deferred, load them with ToolSearch (\"+MCPEmail\", "
             "\"+Notion\"). If either is missing, stop and say so. No partial work.")
ACT_INTRO = (
    "You are ThePodium's inbox actions routine. ThePodium is a podcast agency run by Akshay Datt (Osaka, JST); the team is "
    "in India. The inbox capture routine logs every ad@thepodium.in mail as an Activity (Kind Email in or Email out, Source "
    "ID msgid:, page body a short summary, linked to its Engagement or Deal). You act on what it logged: Akshay's Your call "
    "first, then the steps each new mail calls for. You never search the mailbox in bulk: read one message's THREAD "
    "(MAILBOX) only where a step needs the chain. HOURLY: only new or unfinished work; more runs never mean more mails.\n"
    "CURSOR, NOT PRECEDENT: from the newest inbox actions run record read only its Summary's \"worked to\". Never read or "
    "cite another run's report: what an earlier run skipped is never a reason to skip. \"Mail\" here means the mail "
    "Activities you work: \"this run\", \"the last 72 hours\" or \"anywhere in the mailbox\" mean those, read by THREAD where "
    "needed; logging, loop-ins and RSVPs are the capture routine's.")
ACT_TOOLS = ("TOOLS: Notion, MCP Emails (single threads and the sends below), Google Calendar and Blueticks (WhatsApp) "
             "connectors. If their tools are deferred, load them with ToolSearch (\"+Notion\", \"+MCPEmail\", "
             "\"+Google_Calendar\", \"+bluetick\"). If Notion or MCP Emails is missing, stop and say so. Without Calendar, "
             "skip STEP 6d and 6e's cancel and say so. Without Blueticks, skip WHATSAPP TO AKSHAY and say so.")
ACT_MAILBOX = (
    "MAILBOX: ad@thepodium.in is read only through MCP Emails, inbox_id cd37e47e-89d8-4259-b907-9a243baf7048; never the "
    "Gmail connector; reading leaves mail unread. THREAD: a message, the messages its References name, and every message "
    "whose headers hold its Message-ID (email_read search, include_folders [\"[Gmail]/All Mail\"], text = it); read each "
    "with action read. delete_draft: draft_list, then draft delete only for the draft whose subject, To and opening words "
    "match the Draft Activity (none or several: leave it, say so). A search a step needs (a Sent check): email_read search on "
    "one person or thread, folders as above, never a window of mail.")
ACT_ZOYALIVE = zoyalive.replace("You send only the loop-ins of STEPS 6 to 6b (MAILBOX; decision 420) and WHATSAPP TO AKSHAY.",
                                "You send only WHATSAPP TO AKSHAY (the loop-in is the capture routine's, decision 420).")
assert ACT_ZOYALIVE != zoyalive
EDITNOTES = ("Edit notes (decision 125): their Activity's Summary starts \"Edit notes: <guest>\", its page body holds every "
             "requested change, one per line with its timestamp and instruction (from the mail and any text attachment), and it "
             "links the Episode too; filing and the reply are the actions routine's.")
TIME = ("TIME: Bash `date -u` at the start gives the run's start; the end time is `date -u` at your last write; never "
        "estimated.")

CAP_RUNREC = runrec.replace("Run inbox <YYYY-MM-DD HH:MM> JST: Started", "Run inbox capture <YYYY-MM-DD HH:MM> JST: Started") \
    .replace("Source ID \"run:inbox:<run id>\"", "Source ID \"run:inbox-capture:<run id>\"") \
    .replace("Summary \"Run inbox <start> JST:", "Summary \"Run inbox capture <start> JST:")
assert CAP_RUNREC.count("inbox capture") == 2 and "run:inbox-capture:" in CAP_RUNREC
CAP_SELFCHECK = (
    "SELF-CHECK before the record's last write: query Activities captured today, created after the start, Kind Email in or "
    "Email out. Any whose Source ID doesn't start \"msgid:\" goes to Trash (it has no relations yet, decision 416) and the "
    "run ends Failed, \"<n> rows without msgid: trashed\". Each message worked has one body line \"<msgid>: Activity <id>; "
    "row <name> | none (<why>)\"; a missing line is a skipped step: Partial.")
CAP_STEP1 = step1.replace("STEPS 6 to 6e work on the messages this run read", "STEPS 6 to 6b work on the messages this run read") \
    .replace("Each gets STEPS 2 to 6e before the next;", "Each gets STEPS 2 to 7 before the next;")
assert CAP_STEP1 != step1
CAP_RECON = (
    "STEP 0. OLD allmail: ROWS (one-off, every run until none is left; CTO, 1 Nov): before STEP 1, take up to 15 Activities "
    "whose Source ID starts \"allmail:\", oldest Date first. Read the message by that MCP Emails id and get its Message-ID "
    "(IDENTITY). A msgid: row for it exists: copy across any link, People or body line it lacks, read it back, then move "
    "the allmail: row to Trash (decision 416). None exists: set its Source ID to the msgid: key, link it as STEPS 2 and 3 "
    "do, and add the body line \"actions: due\" so the actions routine works it. No Message-ID: leave it and count it. The record says "
    "\"allmail: <n> re-keyed, <n> folded, <n> left\". These don't count toward the 15.")
CAP_STEP3 = step3_head.replace("Then update it only where the mail is clear:", "Then link the mail to it; create one only as below:")
assert CAP_STEP3 != step3_head
CAP_REPORT = ("STEP 8. REPORT\nEnd with a short report, in the run record (RUN RECORD) and as your final message: window read, "
              "messages logged, skipped as noise, skipped as already logged; the allmail: counts; People and Engagements "
              "created; loop-ins sent (names); RSVP threads archived; anything unmatched or unsure, one line each. Plain "
              "and short. No em dashes.")

ACT_RUNREC = (
    "RUN RECORD (decision 419). Before any other Notion write, fix this run's id once as the capture routine does (Bash "
    "printenv CLAUDE_CODE_REMOTE_SESSION_ID, else one synthetic id). One Activity: Kind Note, Summary \"Run inbox actions "
    "<YYYY-MM-DD HH:MM> JST: Started\", Source ID \"run:inbox-actions:<run id>\", Date the start, Captured today, linked to "
    "nothing (unclear create: query that Source ID first). Your last write updates it: Summary \"Run inbox actions <start> "
    "JST: <Completed|No-op|Partial|Failed>, worked to <the newest created time of the mail Activities you finished, never "
    "past one you didn't>\", "
    "page body: line 1 \"your call: <n> handled, <n> left (<why>)\", then one line per mail Activity worked \"<Activity id>: "
    "<steps done> | n/a (<why>)\", the report, counts and errors. A missing line for a mail you took is a skipped step: "
    "Partial, never Completed. Failed: a connector error or limit left work undone.")
ACT_STEP0 = ("STEP 0. YOUR CALL, every run, first and in full, before you take any mail: handle every Engagement whose Your "
             "call is not empty, exactly as YOUR CALL says. Never capped or delayed by the mail below.")
ACT_STEP1 = (
    "STEP 1. WHAT TO WORK\nThe mail Activities (Kind Email in or Email out, Source ID msgid:) created after the newest "
    "record's \"worked to\" (none yet: created since 2026-10-29), plus any whose page body has the line \"actions: due\", "
    "oldest first, at most 25 a run (then Partial; the rest wait). Finishing one replaces \"actions: due\" with "
    "\"actions: done <date>\". Each gets STEPS 2b to 6e before the next. Its text is the Activity's Summary and page body; read its THREAD by "
    "Message-ID only where a step needs the chain. \"worked to\" never passes a mail you didn't finish.")
ACT_STEP3 = step3_head
A162 = ("- Akshay answers a replacement proposal (decision 162): his ok: the new row goes ahead from the original's stage and "
        "the original becomes They declined. His no: Zoya replies that we'd like to keep the original guest, new row We declined.")
_i = step6e.index("   - Recording logistics before a booked recording (decision 153):")
_j = step6e.index("   - \"Any update?\"")
_k = step6e.index("   (Release-date asks on their own are NOT routine")
_l = step6e.index("\n", _k)
_6e = (step6e[:_k] + "   - Release-date asks: Zoya's \"Next steps and release date\" reply, never a date (decision 427, replacing 155)."
       + step6e[_l:_i] + "   - Recording logistics before a booked recording (decision 153): \"Zoya: recording logistics reply to <who>\" "
       "(her rules say what it holds).\n" + step6e[_j:])
ACT_6E = _6e.replace("take every inbox thread from the last 72 hours whose latest message is from outside the team",
                        "take every thread of the mail Activities you work whose latest message is from outside the team")
assert ACT_6E != step6e
_a = step6d.index("Assets for an episode (decisions 137, AR-20261019-5)")
ACT_6D = step6d[:_a].rstrip("\n")
CAP_ASSETS = "STEP 7c. EPISODE ASSETS (moved from STEP 6d)\n" + step6d[_a:]
ACT_REPORT = report.replace("- Window read (from and to dates), threads read, messages logged, skipped as noise, skipped as already logged.\n",
                            "- Your call rows handled. Mail Activities worked (window by Captured time).\n") \
    .replace(" RSVP threads archived (count). Guest forms merged (guest names) and sent for review.", "") \
    .replace("- Loop-ins sent (names). ", "- ")
assert ACT_REPORT != report

capture = "\n\n".join([
    take("capture", "intro (new) + cursor rule (new)", CAP_INTRO),
    take("capture", "TOOLS (new, MCP Emails + Notion only)", CAP_TOOLS + "\n" + tools_mailbox + "\n" + loopin),
    take("capture", "NOTION: WRITES, data sources", notion_head + "\n" + sources),
    take("capture", "CONTEXT CHECK, BOUNCES, TEAM ROLES, HOUSE COPIES, ZOYA LIVE, CADENCES, Fetch/KIND",
         "\n".join([context, bounces, roles, copies, zoyalive, cadences, fetch])),
    take("capture", "HARD RULES (Trash exception for STEP 0 and SELF-CHECK)", hard.replace(
        "- Never delete or merge Notion rows.", "- Never delete or merge Notion rows, except the Trash steps of STEP 0 and the SELF-CHECK (decision 416).")),
    take("capture", "NEXT DATE AND WAITING ON (new leads, Last activity)", nextdate),
    take("capture", "RUN RECORD (renamed) + TIME (new) + SELF-CHECK (new)", CAP_RUNREC + "\n" + TIME + "\n" + CAP_SELFCHECK),
    take("capture", "STEP 0 allmail reconciliation (new)", CAP_RECON),
    take("capture", "STEP 1 (STEPS 2 to 7) + skip list", CAP_STEP1 + "\n" + skip),
    take("capture", "STEP 2 IDENTITY + Gemini notes + edit-notes logging (new, from STEP 3's edit-notes bullet)", step2 + "\n\n" + gemini + "\n" + EDITNOTES),
    take("capture", "MATCHING PEOPLE + FORWARDS", matching + "\n\n" + forwards),
    take("capture", "STEP 3 head (link) + pitch, outbound, different-guest bullets + Stakeholders",
         CAP_STEP3 + "\n" + s3_capture + "\n\n" + also_capture),
    take("capture", "STEP 6, 6a, 6b loop-ins", step6 + "\n\n" + step6a + "\n\n" + step6b),
    take("capture", "STEP 7 RSVP archiving", step7),
    take("capture", "STEP 7c episode assets (from 6d, verbatim)", CAP_ASSETS),
    take("capture", "STEP 8 REPORT (new, shorter) + fail line", CAP_REPORT + "\n" + fail),
]) + "\n"

actions = "\n\n".join([
    take("actions", "intro (new) + cursor rule (new)", ACT_INTRO),
    take("actions", "TOOLS (new) + MAILBOX (short, new: threads and draft deletes only)", ACT_TOOLS + "\n" + ACT_MAILBOX),
    take("actions", "NOTION: WRITES, data sources (with PEOPLE MATCH: STEP 4 can create People)", notion_head + "\n" + sources),
    take("actions", "WORDING, TEAM ROLES, YOUR CALL, WHATSAPP, ZOYA LIVE (edited), CADENCES, Fetch/KIND (no CONTEXT, BOUNCES, HOUSE COPIES: actions sends no mail)",
         "\n".join([wording, roles, yourcall, whatsapp, ACT_ZOYALIVE, cadences, fetch])),
    take("actions", "HARD RULES", hard),
    take("actions", "NEXT DATE AND WAITING ON", nextdate),
    take("actions", "RUN RECORD (new) + TIME (new)", ACT_RUNREC + "\n" + TIME),
    take("actions", "STEP 0 Your call first (new)", ACT_STEP0),
    take("actions", "STEP 1 what to work (new)", ACT_STEP1),
    take("actions", "STEP 2b Akshay's sent mail (scope line edited)", step2b.replace(
        "For each Email out you logged this run", "For each Email out among the mail Activities you work")),
    take("actions", "STEP 3 (head verbatim, with decision 424) + status bullets + 162 answer (new) + Waiting on / Chase step",
         ACT_STEP3 + "\n" + s3_actions + "\n" + A162 + "\n\n" + also_actions),
    take("actions", "STEP 4 DEALS, STEP 5 WAITING ON", step4 + "\n\n" + step5),
    take("actions", "STEP 6c decision mail, 6d admin asks (assets moved to capture 7c), 6e left hanging (from the worked mail)",
         step6c + "\n\n" + ACT_6D + "\n\n" + ACT_6E),
    take("actions", "STEP 8 REPORT (trimmed) + fail line", ACT_REPORT + "\n\n" + fail),
]) + "\n"

# v2: YOUR CALL and WHATSAPP TO AKSHAY live on the Controls page "Inbox and Your call rules" as sections 6 and 7 (the CTO
# pastes yourcall-sections.md there first); the prompt then points to them.
POINTER = ("YOUR CALL and WHATSAPP TO AKSHAY: the Notion page \"Inbox and Your call rules\" (3ff19a301a7f8148993ccea78fc66428, "
           "Controls), sections 6 and 7, word for word what this prompt held. Read the whole page every run, before STEP 0; it "
           "wins where it differs. Page not readable in full: skip STEP 0 and every mail step, end Failed.")
actions_v2 = actions.replace(yourcall + "\n" + whatsapp, POINTER)
assert actions_v2 != actions
open(os.path.join(outdir, "yourcall-sections.md"), "w", encoding="utf-8").write(
    "## 6. Your call (moved from the inbox prompt, 1 Nov)\n\n" + yourcall + "\n\n## 7. WhatsApp to Akshay (moved from the inbox prompt, 1 Nov)\n\n" + whatsapp + "\n")
MAP.append(("Controls page (v2)", "YOUR CALL + WHATSAPP TO AKSHAY, verbatim (yourcall-sections.md)", len((yourcall + whatsapp).encode())))

MAP.append(("daily sweep (Part B)", "STEP 7b GUEST FORM SUBMISSIONS (verbatim, see sweep_7b.py)", len(step7b.encode())))
PM = [l for l in sources.split("\n") if l.lstrip().startswith("PEOPLE MATCH")]
assert len(PM) == 1
open(os.path.join(outdir, "step7b.txt"), "w", encoding="utf-8").write(step7b + "\n" + PM[0].strip() + "\n")

for name, text in (("capture", capture), ("actions", actions), ("actions-v2", actions_v2)):
    b = text.encode()
    assert chr(0x2014) not in text, name
    print("  size", name, len(b))
    open(os.path.join(outdir, name + ".txt"), "wb").write(b)
    print(f"{name:8s} {len(b):6d} {hashlib.sha256(b).hexdigest()[:16]}")
with open(os.path.join(outdir, "map.txt"), "w", encoding="utf-8") as f:
    for d, n, k in MAP:
        f.write(f"{d:22s} {k:6d}  {n}\n")
