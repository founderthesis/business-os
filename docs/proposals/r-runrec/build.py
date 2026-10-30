"""R-runrec (decision 419; CTO, 28 Oct 13:05 JST): one run record per run for the seven routines that had none, reusing Zoya's
RUN RECORD shape, plus the inbox's Gmail quota handling and a narrower read. One minimal patch per live prompt.
Usage: python3 build.py <input dir> <output dir>
Input dir holds the live prompts as <trigger id>.txt (exact bytes as read back on 28 Oct; host boards, evals, dossiers and the
sweep from the repo copies the CTO confirms at deploy, see README.md). WhatsApp may also be the B2 build (1afc777019d1aefd).
Each patch asserts its input hash, exact-count anchors, an unchanged em-dash count and a size under the 65,536-byte cap less 200."""
import sys, os, hashlib
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
CAP = 65536 - 200

def runrec(name, label=None):
    label = label or name
    return (
        "RUN RECORD (decision 419: the scheduler's \"succeeded\" only means the run ended, so every run records what it did). "
        "Before any other Notion write, fix this run's id once: Bash printenv CLAUDE_CODE_REMOTE_SESSION_ID; if empty, once echo "
        "\"syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d ' \\n')\"; if neither works, write no record and "
        "say \"run record skipped: no id\" in the report. Then one Activity: Kind Note, Source empty, Summary \"Run " + label +
        " <YYYY-MM-DD HH:MM> JST: Started\", Source ID \"run:" + name + ":<run id>\", Date the start, Captured today, linked to "
        "nothing (an unclear create response: query that Source ID and reuse its row, never a second). Your last write updates "
        "that row: Summary \"Run " + label + " <start> JST: <Completed|No-op|Partial|Failed>\", page body = the report plus the "
        "end time, counts, each error as its tool gave it (shortened) and everything skipped, with why. No-op: nothing was due. "
        "Partial: a step failed, was skipped or was cut short. Failed: the run stopped early, or a connector error, quota or rate "
        "limit (\"exhausted\", \"quota\", \"429\", \"504\") left work undone; such a run is never Completed. A run that stops for "
        "a missing tool still writes its record (Failed) if Notion works. The record never sets Last activity, Waiting on or a "
        "date on any row and never counts toward a cap. A failed record write: retry once, then say so in the report.\n\n")

def patch(tid, name, ok_hashes, edits):
    s = open(os.path.join(src, tid + ".txt"), encoding="utf-8").read()
    h = hashlib.sha256(s.encode()).hexdigest()[:16]
    assert h in ok_hashes, (name, "unexpected input", h)
    dashes = s.count(chr(0x2014))
    for a, b in edits:
        assert s.count(a) == 1, (name, a[:60], s.count(a))
        s = s.replace(a, b)
    out = s.encode()
    assert s.count(chr(0x2014)) == dashes and len(out) <= CAP, (name, len(out))
    open(os.path.join(dst, name + ".txt"), "wb").write(out)
    print(f"{name:12s} {tid}  in {h}  out {len(out):6d} {hashlib.sha256(out).hexdigest()[:16]}  headroom {CAP - len(out)}")

# Inbox: run record, Gmail quota back-off, a narrower read, and the report goes into the record.
patch("trig_0189eZvAD8x4357cfevgZ3No", "inbox", {"aed0215a8bdf6a26"}, [
    ("STEP 1. WHAT TO READ\n", runrec("inbox") + "STEP 1. WHAT TO READ\n"),
    ("Start one day before that date; if there is none, start 3 days ago. Search Gmail for: after:YYYY/MM/DD -in:spam",
     "Start 30 minutes before the start of the newest inbox run record that ended Completed or No-op (RUN RECORD), as "
     "after:<Unix seconds>: every run since then failed or stopped part-way, so its mail is read again, and a run reads only "
     "new mail (never anchor on the newest Gmail Activity alone: Zoya and the sweep log Gmail Activities too). No such "
     "record yet: one day before the newest Gmail Activity's date (after:YYYY/MM/DD); no Gmail Activity at all: 3 days "
     "ago. Search Gmail for: after:<start> -in:spam"),
    ("That covers sent mail too. Read every thread in full with get_thread.\n",
     "That covers sent mail too. Read every thread in full with get_thread.\nGMAIL LIMITS (28 Oct: a run hit \"Resource has "
     "been exhausted\" and logged nothing): a Gmail call that fails with \"exhausted\", a quota error or 429: Bash sleep 30 and "
     "retry it once; fails again: sleep 60, once more; still failing: no more Gmail calls this run, finish the steps that need "
     "no Gmail, and end Failed (RUN RECORD), naming the error and the threads not read.\n"),
    ("End with a short report, nothing else written anywhere:",
     "End with a short report, written only to the run record (RUN RECORD):"),
])

# Calendar.
patch("trig_01Voiz5YsK2SnVf2STF8PoSH", "calendar", {"8fb664a1c94776b5"}, [
    ("STEP 1. READ THE CALENDAR\n", runrec("calendar") + "STEP 1. READ THE CALENDAR\n"),
])

# WhatsApp: live (26,007) or the B2 build; STEP 0 writes to Notion, so the record goes before it.
patch("trig_01MnmJYorWrd61K7b5BCqXr1", "whatsapp", {"9e8b9f4891e9c03d", "1afc777019d1aefd"}, [
    ("STEP 0. ZOYA GROUP (decision 304", runrec("whatsapp") + "STEP 0. ZOYA GROUP (decision 304"),
])

# Host boards.
patch("trig_01K8bueCr2xsPkbgQzjeRKsz", "host-boards", {"5819ccf7528ca16f"}, [
    ("STEP 1. PULL THE HOSTS' EDITS INTO ENGAGEMENTS\n",
     runrec("host-boards") + "STEP 1. PULL THE HOSTS' EDITS INTO ENGAGEMENTS\n"),
])

# Daily sweep: its per-part report Activity becomes the run record (Summary "Run sweep <A|B> ..."), so there is one record per run.
patch("trig_01MdfUFg2qrebDWgiHwncgnd", "sweep", {"7af60faaa021fa64"}, [
    ("read the previous run of the same part (its report Activity, Source ID \"sweep:<A|B>:<YYYY-MM-DD>\")",
     "read the previous run of the same part (its run record: the newest Activity whose Summary starts \"Run sweep <A|B>\"; "
     "before 29 Oct, Source ID \"sweep:<A|B>:<YYYY-MM-DD>\")"),
    ("Log your report as one Activity, Kind Note, Summary \"Sweep <A|B> <D Mon>: <Completed|Partial>\", Source ID "
     "\"sweep:<A|B>:<today>\", the report in the page body; one already there for today is updated, never a second.",
     "Your report goes in your run record (RUN RECORD below, \"Run sweep <A|B>\"), never a second Activity."),
    ("\nFLAGGING (decisions 79 and 81)\n", "\n" + runrec("sweep", "sweep <A|B>") + "FLAGGING (decisions 79 and 81)\n"),
])

# Evals.
patch("trig_01R1yHgEztVEo832zMwUugBr", "evals", {"1d87f124107a06c6"}, [
    ("STEP 1. FIND THE WORK\n", runrec("evals") + "STEP 1. FIND THE WORK\n"),
])

# Dossiers.
patch("trig_01WfLf8Zx9c34fSzfrTeUY5M", "dossiers", {"68e94cb7d30ca645"}, [
    ("STEP 1. FIND THE WORK\n", runrec("dossiers") + "STEP 1. FIND THE WORK\n"),
])
