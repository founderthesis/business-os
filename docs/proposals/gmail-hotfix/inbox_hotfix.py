"""Gmail quota incident, 28 Oct (CTO 13:20 JST): inbox hotfix. Usage: python3 inbox_hotfix.py <live inbox prompt> <out file>
Input: the live inbox prompt, 61,957 B / aed0215a8bdf6a26 (trig_0189eZvAD8x4357cfevgZ3No, read 28 Oct).
1/ RUN RECORD for the inbox (decision 419), the same block as R-runrec, because the read window anchors on it.
2/ STEP 1 reads only new mail: one search_threads per page in THREAD_VIEW_SUMMARY (latest message and count per thread),
   then get_thread only for threads with a message at or after the start that no Activity holds yet. Gmail's after: takes a
   date (midnight), never epoch seconds, so the narrowing happens after the search.
3/ GMAIL LIMITS: back off once, then read ad@thepodium.in through MCP Emails (IMAP, not the Gmail API); both fail: Failed.
4/ The report goes into the run record."""
import sys, os, hashlib
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "aed0215a8bdf6a26", "not the live inbox prompt"
dashes = s.count(chr(0x2014))

RUNREC = (
    "RUN RECORD (decision 419). "
    "Before any other Notion write, fix this run's id once: Bash printenv CLAUDE_CODE_REMOTE_SESSION_ID; if empty, once echo "
    "\"syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d ' \\n')\"; if neither works, write no record and "
    "say so in the report. Then one Activity: Kind Note, Source empty, Summary \"Run inbox "
    "<YYYY-MM-DD HH:MM> JST: Started\", Source ID \"run:inbox:<run id>\", Date the start, Captured today, linked to nothing "
    "(an unclear create response: query that Source ID, reuse the row if found, else create it once; never a second). Your "
    "last write updates that row: "
    "Summary \"Run inbox <start> JST: <Completed|No-op|Partial|Failed>\", page body = the report plus the end time, a line "
    "\"read to <ISO time of the newest message read>\" once STEP 1's read finished (any status), counts, "
    "each error as its tool gave it (shortened) and what was skipped, with why. No-op: nothing was due. Partial: a step "
    "failed, was skipped or was cut short. Failed: the run stopped early, or a connector error, quota or rate limit "
    "(\"exhausted\", \"quota\", \"429\", \"504\") left work undone that GMAIL LIMITS' fallback didn't cover (that fallback: "
    "Partial); such a run is never Completed. A run that stops for a "
    "missing tool still writes its record (Failed) if Notion works. The record never sets Last activity, Waiting on or a date "
    "on any row and never counts toward a cap. A failed record write: retry once, then report it.\n\n")

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)

# Size (the cap leaves no room otherwise): drop history from provenance notes, keep every decision number and rule.
for a, b in [
    ("MESSAGE IDENTITY (Codex, 22 Oct: four sends were logged twice, once per mailbox).", "MESSAGE IDENTITY."),
    (" (Codex, 23 Oct: Zoya's acknowledgement to Pranav got a second Activity keyed \"gmail:\" because the other reads have "
     "no headers):", ":"),
    (" (CTO, 22 Oct: a loop-in reopened a Parked thread).", "."),
    ("(decision 316, Akshay, 18 Oct: \"why is eximple in my queue? I already replied\")", "(decision 316)"),
    ("(decision 399, Akshay, 22 Oct: \"pure AI tell\")", "(decision 399)"),
    ("(decision 325, Akshay, 18 Oct: \"My queue is a decision inbox, not a notification inbox\")", "(decision 325)"),
    ("STEP 2b. AKSHAY'S SENT MAIL (decision 387 retired the draft-and-edit comparison of decision 102)",
     "STEP 2b. AKSHAY'S SENT MAIL (decision 387)"),
]:
    rep(a, b)
rep("STEP 1. WHAT TO READ\n", RUNREC + "STEP 1. WHAT TO READ\n")
rep("Find the newest Activity with Source = Gmail (SQL: ORDER BY \"date:Date:start\" DESC LIMIT 1). Start one day before that "
    "date; if there is none, start 3 days ago. Search Gmail for: after:YYYY/MM/DD -in:spam -in:trash -category:promotions "
    "-category:social\nThat covers sent mail too. Read every thread in full with get_thread.\n",
    "Start time T (Gmail quota incident, 28 Oct): 30 minutes before the "
    "\"read to\" time on the newest inbox run record that has one (RUN RECORD; a run whose read never finished has none, so "
    "its span is read again), never more than 3 days ago; none yet: the newest Activity with Source = Gmail (SQL: ORDER BY "
    "\"date:Date:start\" DESC LIMIT 1) minus one day; none at all: 3 days ago. Search with search_threads, view THREAD_VIEW_SUMMARY (each thread's latest message and message "
    "count; one call per page of 50), query after:<T's date, YYYY/MM/DD> -in:spam -in:trash -category:promotions "
    "-category:social (a date only, never epoch seconds). That covers sent mail too. Keep a thread only if its "
    "latest message is at or after T and no Activity already holds it (an Activity whose Link has this thread's id and whose "
    "Date is at or after that message's date); read only those, each once, with get_thread (messageFormat PLAIN_TEXT; "
    "FULL_CONTENT only where a step needs the HTML, such as Gemini notes).\n"
    "GMAIL LIMITS, for every Gmail call this run (a throttled Gmail is not a missing one: TOOLS' stop doesn't apply): a call "
    "that fails with \"exhausted\", a quota error or 429 is retried once, after your next step that needs no Gmail (no "
    "sleep: Bash refuses it); one a retry clears is not a failure. Fails "
    "again: make no more Gmail calls this run and read ad@thepodium.in through MCP Emails instead (ToolSearch \"+MCPEmail\"; "
    "email_read, inbox_id cd37e47e-89d8-4259-b907-9a243baf7048: action search since T's date in INBOX and sent, then action "
    "read for each new message, action original for its Message-ID): log those messages as STEP 2 says, Link empty, and leave "
    "every Gmail action (sends, drafts, RSVP archiving) to the next run: end Partial. MCP Emails fails too: end Failed, "
    "naming both errors.\n")
rep("End with a short report, nothing else written anywhere:", "End with a short report, in the run record (RUN RECORD) and as your final message:")
assert s.count(chr(0x2014)) == dashes and len(s.encode()) <= 65536 - 200, len(s.encode())
open(dst, "w", encoding="utf-8").write(s)
b = s.encode(); print(os.path.basename(dst), len(b), hashlib.sha256(b).hexdigest()[:16], "headroom", 65536 - 200 - len(b))
