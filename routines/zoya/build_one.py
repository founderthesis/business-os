"""Build Zoya's one-writer release (CTO, 27 Oct 00:30 JST, option 1 with the fail-closed GitHub lock): one routine, hourly at
:38, 07:38 to 23:38 JST, whose 10:38 and 16:38 weekday runs also do the SLOW work. The SLOW work doesn't fit beside the FAST work
under the 65,536-byte prompt cap (the parts total about 77 KB), so it ships as a file in this repo, read by commit and sha256 in
those runs only. The lease and RECONCILE parts are gone: the LOCK part replaces them.

Usage: python3 build_one.py <out dir> [<branch> <commit>]
Writes zoya-slow-work.txt first and prints its sha256. With a branch and the commit that carries
routines/zoya/release/zoya-slow-work.txt, it also writes zoya-one.txt with that pin; without them the prompt keeps the
@@SLOW...@@ placeholders. Refuses a prompt over the cap less 200 or any em dash. Old builds stay reproducible with build.py."""
import sys, os, re, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()
part = lambda n: open(os.path.join(PARTS, n + ".txt"), encoding="utf-8").read().rstrip("\n")

ONE = ["intro-one", "tools", "rules-common", "rules-tail", "notion-data", "scope", "actions", "queue-fast", "voice", "sending",
       "limits-fast", "onemail", "identity", "lock", "runrecord", "fast-order", "decision", "daybefore", "invites", "mail",
       "report-fast", "slowwork-pointer", "hard"]
SLOWWORK = ["slowwork-intro", "tools", "rules-common", "rules-routines", "rules-tail", "notion-data", "scope", "actions",
            "queue-slow", "internal", "editnotes", "snoozed", "voice", "sending", "teamwa", "limits", "onemail", "identity",
            "slow-order", "feedback", "bounces", "vendor", "ownermail", "scorecard", "payments", "invites", "followups",
            "report-slow", "hard"]
VARIANT = {
 "one": [
  # Quote what you answer (Rules for Zoya; Akshay, 27 Oct, item 14), FAST work's replies only: the SLOW work file stays pinned
  # by tag at dedea9f8 (CTO, 27 Oct). MCP Emails adds the quoted original to a reply's plain body itself and never to html_body.
  ("sending", "Never action send with a \"Re:\" subject",
   "QUOTE WHAT YOU ANSWER: every reply carries, below the sign-off, the latest inbound message it answers as \"On <date>, "
   "<name> wrote:\" plus that message's own text, never the older chain, so Akshay in Cc sees what was asked (the quote is theirs: "
   "VOICE's and the link rules cover your text, not it). MCP Emails "
   "puts its quote of that message in the plain body itself: never paste one there; if html_body has none at the read-back, add "
   "it there as <p>On <date>, <name> wrote:</p><blockquote>its text</blockquote>, then read back again. In-Reply-To and "
   "References stay from that message. A reply from ad@thepodium.in (Gmail): put the quote in both bodies yourself. Never action "
   "send with a \"Re:\" subject"),
  ("sending", "(STEP 0c)", "(SLOW work's bounce scan)"),
  # FAST work never uses these (no WhatsApp, follow-ups, vendor forms, internal tasks, release mail); the SLOW work file has them
  ("tools", " Blueticks sends WhatsApp to the team (TEAM WHATSAPP). Web search finds news for news angles.", ""),
  ("tools", ', "+bluetick"', ""),
  ("tools", " Without Blueticks, put each WhatsApp you would have sent on Akshay's list instead.", ""),
  ("notion-data", "\n- Founder Thesis guests (peers for name-drops): collection://b460a8fa-1531-49e5-82f9-133478e2278d", ""),
  ("notion-data", "\n- Mail issues: collection://2a56fcad-3015-48e4-b811-e18ff4009fe0", ""),
  ("notion-data", "- Vendor Pitches (the podm.in/pitch-to-us form): collection://d4ca5f98-d7e7-4002-9ff3-a7b3a200953d (Company / "
   "Service Name, Contact Name, Email, Phone / WhatsApp, Website, Service Offering, Pricing, Sample Work, Why Founder Thesis?, "
   "Status, Submitted). Organisations:", "- Organisations:"),
  ("notion-data", "re: PERSON STEPS GO ON THEIR ROW \\(decision 385.*", " FAST work creates no Task rows."),
  ("scope", ", STEP 0d); AD Personal threads for misc chase (routine 4). Engagements with Kind Task and Show Internal "
   "(INTERNAL TASKS).", ")."),
  ("scope", "\n- Routines on un#: 1 to 4 and 7 run; 5 and 8 don't; 6 sends only C16 and C17, and only when the Episode has the "
   "episode link and Sri's post link. Name-drops come from the un# sheet's past guests.", ""),
  ("scope", "\n- A guest pitched for two shows on one thread (one Engagement per show): follow up once, on the row Akshay named, "
   "and keep the other row's Next action pointing to it.", ""),
  ("voice", ', with one exception: release mail 2 opens "Zoya here, I work with Akshay on the Founder Thesis podcast."', ""),
  ("hard", "Never introduce or describe yourself except in release mail 2.",
   "Never introduce or describe yourself (SLOW work: except in release mail 2)."),
  ("mail", "then WhatsApp Sarika the notes (guest, episode, each change with its timestamp, or the attachment's name).",
   "the WhatsApp to Sarika is SLOW work's (EDIT NOTES TO SARIKA)."),
  ("hard", "- WhatsApp only to the team members TEAM WHATSAPP names.",
   "- No WhatsApp in FAST work; SLOW work: only to the team members TEAM WHATSAPP names."),
  ("limits-fast", "shared with your SLOW run", "shared with your SLOW work"),
  ("queue-fast", "Follow-up chains, nurture and team steps are SLOW's: leave them.",
   "Follow-up chains, nurture and team steps are SLOW's: leave them to SLOW WORK."),
  ("runrecord", "Before your first Notion write, fix this run's id once: Bash printenv CLAUDE_CODE_REMOTE_SESSION_ID; if empty, "
   "once echo \"syn-$(date -u +%Y%m%dT%H%M%SZ)-$(od -An -N4 -tx1 /dev/urandom | tr -d ' \\n')\" (synthetic); if neither works, "
   "write no record and report \"run record skipped: no id\". Never derive it again. Then one Activity:",
   "Use LOCK's run id. Once you hold the lock, one Activity:"),
  ("runrecord", "Failed: stopped early)", "Failed: stopped early; Skipped: LOCK)"),
  ("fast-order", "Start no new row 25 minutes after you hold the lease.",
   "FAST work starts no new row 25 minutes after the run's start."),
  ("report-fast", "Summary \"Run zoya FAST <start> JST: <status>\"", "Summary \"Run zoya <start> JST: <status>\""),
 ],
 "slowwork": [
  ("slow-order", "SLOW ORDER. RECONCILE first, then STEP 0",
   "SLOW ORDER. SLOW work starts no new row 45 minutes after the run's start; the next run with SLOW work carries on. STEP 0"),
  ("report-slow", "STEP 3. REPORT\nAlso the run record's page body (RUN RECORD),",
   "SLOW REPORT\nAdd to the same run record's page body, after the FAST report,"),
  ("report-slow", "reconcile (FAST's last record, actions checked, alerts posted), ", ""),
 ],
}

def build(name, manifest):
    texts = {n: part(n) for n in manifest}
    for n, a, b in VARIANT[name]:
        if a.startswith("re:"):
            texts[n], k = re.subn(a[3:], b, texts[n])
            assert k == 1, (name, n, a[:50], k)
            continue
        assert texts[n].count(a) == 1, (name, n, a[:50], texts[n].count(a))
        texts[n] = texts[n].replace(a, b)
    s = "\n\n".join(texts[n] for n in manifest) + "\n"
    assert "\u2014" not in s, name
    for bad in (r"\bRECONCILE\b", r"\bLEASE\b", r"(?<!with-)\blease\b", r"\bSLOW run\b", r"\bFAST run\b"):
        assert not re.search(bad, s), (name, bad, re.search(".{60}" + bad + ".{40}", s))
    return s

slow = build("slowwork", SLOWWORK)
rel = os.path.join(HERE, "release")
os.makedirs(rel, exist_ok=True)
for path in (os.path.join(out, "zoya-slow-work.txt"), os.path.join(rel, "zoya-slow-work.txt")):
    open(path, "w", encoding="utf-8").write(slow)
sb = slow.encode()
print("zoya-slow-work", len(sb), sha(sb)[:16])
one = build("one", ONE)
if len(sys.argv) >= 4:
    one = (one.replace("@@SLOWBRANCH@@", sys.argv[2]).replace("@@SLOWPIN@@", sys.argv[3])
              .replace("@@SLOWHASH@@", sha(sb)[:16]))
    assert "@@SLOW" not in one
assert one.count("@@VERSION@@") == 1, "version placeholder"
one = one.replace("@@VERSION@@", "zoya-one " + sha(one.encode())[:12])
ob = one.encode()
assert len(ob) <= 65536 - 200, ("one", len(ob))
open(os.path.join(out, "zoya-one.txt"), "w", encoding="utf-8").write(one)
print("zoya-one", len(ob), sha(ob)[:16], "(pinned)" if len(sys.argv) >= 4 else "(unpinned)")
