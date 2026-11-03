"""Run receipts on four routines (CTO, 3 Nov 13:07 JST; Akshay: "ran", "completed business work" and "independently verified"
stay separate). Adds capture's RUN RECORD (decision 419) to calendar, evals, WhatsApp and the daily sweep; no other behaviour change.
Usage: python3 patch.py <live dir> <out dir>. Inputs are the live prompts read back on 3 Nov (live/*.txt); each edit asserted once.
The deployment reference is "<routine> <first 12 hex of the sha256 of the prompt with the placeholder in place>", as Zoya's build does."""
import hashlib, os, sys
live, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
LIVE = {"calendar": "f6d140196f3b75b4", "evals": "1d87f124107a06c6", "whatsapp": "ca8009c24aaeda15", "sweep": "6783dd01e396e5ab"}

def R(s, a, b):
    assert s.count(a) == 1, (a[:70], s.count(a))
    return s.replace(a, b)

def block(name, record, mandatory, extra=""):
    return (
        "RUN RECORD (decision 419; Akshay, 3 Nov: \"ran\", \"completed business work\" and \"independently verified\" are "
        "kept apart). Before any other Notion write, fix this run's id once: Bash printenv CLAUDE_CODE_REMOTE_SESSION_ID; "
        "if empty, once echo \"syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d ' \\n')\"; if neither "
        "works, write no record and say so in the report. " + record + " Your last write updates that row: its final "
        "status in the Summary, and a page body with \"run <run id>\", \"deployment @@VERSION@@\", start and end (Bash "
        "date -u, never estimated), then one line per step of this prompt in order, \"STEP <n>: done <count> | skipped "
        "(<reason>) | n/a (<why there was nothing to do>)\", counts, each error as its tool gave it (shortened), then the "
        "report. " + mandatory + " Completed only when every one of them is done or n/a; one skipped, cut short or run as "
        "a lighter pass (a sample, \"a light pass\", checks not made) is Partial, whatever the reason; Failed: stopped "
        "early, or a connector error, quota or rate limit left work undone. \"done\" means the step went through every "
        "item it selects; a check you didn't make is never written as done. " + extra + "The record never sets Last "
        "activity, Waiting on or a date on any row. A failed record write: retry once, then report it.")

def std_record(name):
    return ("Then one Activity (Activities, parent named as its data source, then fetched back): Kind Note, Source empty, "
            "Summary \"Run " + name + " <YYYY-MM-DD HH:MM> JST: Started\", Source ID \"run:" + name + ":<run id>\", Date the "
            "start, Captured today, linked to nothing (unclear create: query that Source ID first; never a second row). "
            "Final Summary: \"Run " + name + " <start> JST: <Completed|No-op|Partial|Failed>\".")

def finish(name, s):
    assert s.count("@@VERSION@@") == 1
    s = s.replace("@@VERSION@@", name + " " + hashlib.sha256(s.encode()).hexdigest()[:12])
    b = s.encode()
    assert chr(0x2014) not in s.replace(chr(0x2014), "", 0) or True
    assert len(b) <= 65536 - 200, (name, len(b))
    open(os.path.join(out, name + ".txt"), "wb").write(b)
    print(f"{name:9s} {len(b):6d} {hashlib.sha256(b).hexdigest()[:16]}")

src = {}
for n, h in LIVE.items():
    t = open(os.path.join(live, n + ".txt"), encoding="utf-8").read()
    assert hashlib.sha256(t.encode()).hexdigest()[:16] == h, n
    src[n] = t
dash = {n: t.count(chr(0x2014)) for n, t in src.items()}

# calendar: record, mandatory steps, and the audit marker carries the run id and its findings or isn't written
c = src["calendar"]
c = R(c, "\n\nSTEP 1. READ THE CALENDAR\n", "\n\n" + block("calendar", std_record("calendar"),
    "Mandatory every run: STEPS 1, 1a, 2, 3, 3b, 4a, 4, 4f, 4e, 4c, 4d and 5, each with its per-item Notion and Drive "
    "checks; STEP 1b once per window (a window already audited: \"STEP 1b: n/a (window <08|16|22> audited by <run id>)\").") +
    "\n\nSTEP 1. READ THE CALENDAR\n")
c = R(c, "Write that Activity only after the whole audit finished and every finding is written;",
         "Write that Activity only after the whole audit finished and every finding is written, with the page body \"run <run "
         "id>\" and one line per finding (or \"no findings\"); a marker without them is never written;")

# evals: 2b and 2c every run
e = src["evals"]
e = R(e, "\n\nSTEP 1. FIND THE WORK\n", "\n\n" + block("evals", std_record("evals"),
    "Mandatory every run: STEPS 1, 2, 2b, 2c and 3 (2b and 2c run even when STEP 1 finds nothing).") + "\n\nSTEP 1. FIND THE WORK\n")

# whatsapp: 0a2, 3d, 4 every run; creates confirmed in their parent data source
w = src["whatsapp"]
w = R(w, "\n\nSTEP 0. ZOYA GROUP", "\n\n" + block("whatsapp", std_record("whatsapp"),
    "Mandatory every run: STEP 0 with 0a2, 0b, 0c and 0d, STEPS 1, 2, 2b, 3d, 4 and 5; STEP 3 on the first run of the JST "
    "day (other runs: \"STEP 3: n/a (not the day's first run)\").",
    "Every create names its parent data source and is fetched back; the record has \"creates: <n> confirmed in their data "
    "source, <n> not\", and one not confirmed is a failed write: Partial. ") + "\n\nSTEP 0. ZOYA GROUP")

# sweep: its report Activity becomes the run record, Started first; the part's steps are mandatory
sw = src["sweep"]
sw = R(sw, "\n\nSTEP 2. DECISIONS\n", "\n\n" + block("sweep",
    "Your report Activity (TWO PARTS: Source ID \"sweep:<A|B>:<today>\") is the run record: create it, or reuse today's, "
    "before any other write, with Summary \"Sweep <A|B> <D Mon>: Started\"; its final Summary is STEP 7's first line.",
    "Mandatory: every step of your part (TWO PARTS), STEP 4 row by row, each check on each row; a check that cannot run "
    "(a missing field or page) is \"skipped (<what is missing>)\".") + "\n\nSTEP 2. DECISIONS\n")

for n, t in (("calendar", c), ("evals", e), ("whatsapp", w), ("sweep", sw)):
    assert t.count(chr(0x2014)) == dash[n], n
    finish(n, t)
