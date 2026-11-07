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
  "10 (or all if fewer) before STEP 0, starting none more than 5 minutes after STEP 0L ends nor after minute 10 of the run "
  "(the rest stay first next run), never skipped as too heavy, each as STEP 0's allmail: rule says, cheapest path first: 0/ a Kind Meeting "
  "row (Gemini notes): read the mail, take the Doc id from its HTML first; its key is the Doc id, Source Gemini notes and Link the Doc, as Gemini notes says, no RAW; 1/ read it by that MCP Emails id (its UID, From, To, Cc, date); 2/ MSGID FIND as KEY defines it "
  "(Zoya's rows included), HEADER-confirmed: fold; 3/ ad@-only and not sent from ad@: adid:<UID>, STEP 2's lookup, "
  "then fold or re-key; 4/ only then RAW (mail sent from ad@, or Zoya on it, with no match), through its file. RAW fails: "
  "\"allmail: no Message-ID <date> <the error>\" as STEP 0 says, and the next row goes on; a quota, rate-limit or 5xx "
  "error is no strike: the row waits for the next run; any other failure, an id that no longer resolves included, is "
  "a strike, at most one per JST day. Every row it re-keys or links "
  "gets the \"capture:\" line and the body line \"link: <run id> recovered\", and its own page id goes on your record's "
  "\"stamped:\" line; a fold does the same for the row it keeps unless its Summary starts \"Zoya\" or its body has "
  "\"actions: done\", whatever the kept row's age. Every row 0A touches gets Captured today (first \"first captured <old>\"), so STEP 0 never takes "
  "it again. No loop-in for a 0A row, here or in STEP 6's catch-up. Record lines: one per row, \"<allmail id>: re-keyed <key> | folded into <row> | linked <row> | "
  "pended <reason>\", then \"allmail left: <n>, unread: <n>\" (the same SQL's count, no LIMIT, after the batch, "
  "and the allmail-unread: count). These rows don't "
  "count toward STEP 1's cap; STOP TIME holds.\n\nSTEP 0. OLD ROWS (one-off,")
c = R(c, "the others filling the rest: rows whose Source ID starts \"allmail:\", and Kind Email in",
         "the others filling the rest: (allmail: rows are STEP 0A's) Kind Email in")

# should-fix 1 and 6: STEP 0's own window sentence; no catch-up loop-in for a recovered row.
c = R(c, "Start no row more than 8 minutes after the run's start.",
         "Start no row more than 8 minutes after STEP 0A ends, nor after minute 12 of the run.")
c = R(c, "A pitch skipped on purpose gets the Claude note line \"loop-in skipped: <why>\" and is never caught up.",
         "A pitch skipped on purpose gets the Claude note line \"loop-in skipped: <why>\" and is never caught up; nor is a row "
         "with a \"link: <run id> recovered\" line.")

# ---- actions: recovered rows always get REPAIR, never a full replay or a resend ----
a = R(a, "except a stamped row with a \"link:\" line after its last \"actions: done\" (REPAIR: capture linked it late)",
         "except a stamped row with a \"link:\" line and no \"actions: done\" or \"actions: stuck\" after it (REPAIR: capture "
         "linked or recovered it late; a recovered row is never given a full first run)")
REP = ("work it again for effects not yet performed only. First read its thread in ad@ and Zoya's inbox, its Engagement's "
       "newest Activities, Sent and Action keys; never resend what went, never undo a newer Your call, Status or decision; "
       "ledger \"<id>: repair: <steps> | nothing left\".")
a = R(a, REP,
  "work it for effects not yet performed only, checked against the row's current state and today's threads: first read "
  "its thread in ad@ and Zoya's inbox, its Engagement's newest Activities, Sent, Action keys, the calendar, and the row's "
  "Status, Waiting on, Next action and Next date. Each effect the mail calls for (STEPS 2b to 6e, decisions 443 and 444 "
  "included; name each in the ledger): already done, or overtaken, which means a newer item (dated after this mail) "
  "that settles or replaces that same effect, such as their later reply, our answer to that ask, a decision on it, a "
  "booked call; an unrelated newer item (a chase to someone else, an RSVP, a holding reply) never overtakes it: ledger "
  "\"n/a (overtaken: <what>)\" and write nothing for it. Still missing: apply it, or hand it over "
  "as a visible step with the date it was asked (\"Zoya: reply to <who>: <what> (asked <D Mon>)\", or Akshay's list under "
  "decision 325), added as a segment with the others kept; never resend what went, never set a Next date or call date "
  "already past (443: Next date today, the step \"offer the next slots (asked for <date>)\"), never write Waiting on, "
  "Next action or Next date over a value set after this mail. Ledger \"<id>: repair: "
  "<effect>: applied | handed over | n/a (overtaken: <what>)\", one per effect.")

# r10e lows (C1 to C3): a recovered 443/444 step replaces the chase segment; a past date is not "today" for 425; past-date wording.
a = R(a, "Next action or Next date over a value set after this mail.",
         "Next action or Next date over a value set after this mail, except that a 443 or 444 step replaces the chase segment "
         "for that person, and its Next date, as STEP 3 says.")
a = R(a, "A Tier 1 guest or a date today or tomorrow (decision 425):",
         "A Tier 1 guest or a date today or tomorrow (decision 425; a date already past is not today):")
a = R(a, "\"Zoya: reply to <who>: slots for <date>\"; the row's chase",
         "\"Zoya: reply to <who>: slots for <date>\" (a date already past: \"offer the next slots (asked for <date>)\"); the row's chase")

for name, s, d in (("capture.txt", c, cd), ("actions.txt", a, ad)):
    b = s.encode()
    assert s.count(chr(0x2014)) == d and len(b) <= 65336, (name, len(b))
    open(os.path.join(outdir, name), "wb").write(b)
    print(f"{name:12s} {len(b):6d} {hashlib.sha256(b).hexdigest()[:16]}")
