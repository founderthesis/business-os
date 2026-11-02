"""Capture r10 on live r8h, and actions r10 on r9e (CTO, 2 Nov 17:00 JST: drain the 90 old allmail: rows in bounded batches).
Usage: python3 patch.py <r8h capture> <r9e actions> <outdir>. Each edit asserted once."""
import hashlib, os, sys
cs, as_, outdir = sys.argv[1:4]
os.makedirs(outdir, exist_ok=True)
def load(p, h):
    s = open(p, encoding="utf-8").read()
    assert hashlib.sha256(s.encode()).hexdigest()[:8] == h, p
    return s
def R(s, a, b):
    assert s.count(a) == 1, (a[:70], s.count(a))
    return s.replace(a, b)
c = load(cs, "de8465b8")
a = load(as_, "ac763528")
cd, ad = c.count(chr(0x2014)), a.count(chr(0x2014))

# ---- capture: STEP 0A, a stated allmail: batch with the cheap path first ----
c = R(c, "\n\nSTEP 0. OLD ROWS (one-off,",
  "\n\nSTEP 0A. OLD allmail: ROWS (CTO, 2 Nov): after STEP 0L, run this SQL on Activities: SELECT url, \"Source ID\" FROM "
  "<Activities> WHERE \"Source ID\" LIKE 'allmail:%' ORDER BY \"date:Captured:start\", \"date:Date:start\" LIMIT 10. Work all "
  "10 (or all if fewer) before STEP 0, never skipped as too heavy, each as STEP 0's allmail: rule says, cheapest path "
  "first: 1/ read it by that MCP Emails id (its UID, From, To, Cc, date); 2/ MSGID FIND by Date within 2 minutes against "
  "msgid: rows (Zoya's included), HEADER-confirmed: fold; 3/ ad@-only and not sent from ad@: adid:<UID>, STEP 2's lookup, "
  "then fold or re-key; 4/ only then RAW (mail sent from ad@, or Zoya on it, with no match), through its file. RAW fails: "
  "\"allmail: no Message-ID <date> <the error>\" as STEP 0 says, and the next row goes on. Every row it re-keys or links "
  "gets the \"capture:\" line and the body line \"link: <run id> recovered\", and its own page id goes on your record's "
  "\"stamped:\" line. Record lines: one per row, \"<allmail id>: re-keyed <key> | folded into <row> | linked <row> | "
  "pended <reason>\", then \"allmail left: <n>\" (the same SQL's count, no LIMIT, after the batch). These rows don't "
  "count toward STEP 1's cap; STOP TIME holds.\n\nSTEP 0. OLD ROWS (one-off,")
c = R(c, "the others filling the rest: rows whose Source ID starts \"allmail:\", and Kind Email in",
         "the others filling the rest: (allmail: rows are STEP 0A's) Kind Email in")

# ---- actions: recovered rows always get REPAIR, never a full replay or a resend ----
a = R(a, "except a stamped row with a \"link:\" line after its last \"actions: done\" (REPAIR: capture linked it late)",
         "except a stamped row with a \"link:\" line and no \"actions: done\" after it (REPAIR: capture linked or recovered it late)")

for name, s, d in (("capture.txt", c, cd), ("actions.txt", a, ad)):
    b = s.encode()
    assert s.count(chr(0x2014)) == d and len(b) <= 65336, (name, len(b))
    open(os.path.join(outdir, name), "wb").write(b)
    print(f"{name:12s} {len(b):6d} {hashlib.sha256(b).hexdigest()[:16]}")
