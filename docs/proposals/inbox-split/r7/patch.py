"""Capture r7 on the live r6c, plus actions' adid: line (Akshay, 2 Nov ~08:50 JST: option (a) of msgid-structural/proposal.md).
Usage: python3 patch.py <r6c capture> <live actions-v2> <outdir>
Inputs: docs/proposals/inbox-split/cleanup/r6/capture.txt 38,121 / d0f0e9bb (live capture);
        docs/proposals/inbox-split/actions-v2.txt 39,354 / 19701651 (live actions). Every edit asserted once."""
import hashlib, os, sys
cap_src, act_src, outdir = sys.argv[1:4]
os.makedirs(outdir, exist_ok=True)

def load(p, h):
    s = open(p, encoding="utf-8").read()
    assert hashlib.sha256(s.encode()).hexdigest()[:8] == h, p
    return s

def R(s, a, b):
    assert s.count(a) == 1, (a[:70], s.count(a))
    return s.replace(a, b)

c = load(cap_src, "d0f0e9bb")
a = load(act_src, "19701651")
cd, ad = c.count(chr(0x2014)), a.count(chr(0x2014))

# ---- capture ----
# KEY: ad@-only mail by UID; Zoya-on mail is hers first; RAW only after 2 hours.
c = R(c, "Wherever this prompt sets an Activity's Source ID to a message id, use \"msgid:<Message-ID without angle brackets>\" "
      "(no Message-ID, no Activity).",
      "KEY (Akshay, 2 Nov): a mail's Source ID is its key. Ad@-only mail (zoya@myunnati.com not on From, To or Cc): "
      "\"adid:<UID>\", the number after \"[Gmail]/All Mail:\" in its All Mail search id; no RAW. Mail Zoya is on: her routine "
      "logs it first. Find her row: Activities with Source ID msgid:, Date within a day of the message, People overlapping its "
      "From, To and Cc; confirm each with query HEADER Message-ID \"<its id>\", which must return this same UID. Found: it is "
      "logged (STEP 1's exception stamps it). None and the message is under 2 hours old: leave it for the next run (not "
      "pending). None and older: its key is \"msgid:<Message-ID without angle brackets>\" from RAW (no Message-ID, no "
      "Activity). Your loop-ins keep their msgid: key (MAILBOX).")
c = R(c, "email_read read has no Message-ID: get it from RAW", "For a msgid: key, email_read read has no Message-ID: get it from RAW")
c = R(c, "in every spelling older rows use: Source ID \"allmail:<its MCP Emails id>\",",
      "in every spelling older rows use: Source ID \"adid:<UID>\", \"allmail:<its MCP Emails id>\",")
c = R(c, "A lone allmail: row: set its Source ID to the msgid: key and work it as new on that row.",
      "A lone allmail: row: set its Source ID to its key (KEY) and work it as new on that row.")
c = R(c, "- Source: Gmail. Source ID: the msgid: key (MESSAGE IDENTITY). Link: as MAILBOX gives it.",
      "- Source: Gmail. Source ID: its key (KEY). Link: as MAILBOX gives it (adid: rows: none).")
c = R(c, "One copy per RFC Message-ID;", "One copy per message (KEY);")
c = R(c, "skip any whose msgid: key an Activity already holds,", "skip any whose key an Activity already holds,")
c = R(c, "idempotency_key \"loopin:<the pitch message's Message-ID>\"", "idempotency_key \"loopin:<the pitch's key>\"")
c = R(c, "and re-read the pitch by its Message-ID (STEP 6b's vendor loop-ins too).",
      "and re-read the pitch by its key (adid: by UID; STEP 6b's vendor loop-ins too).")
# STEP 0: allmail rows get KEY too
c = R(c, "allmail: read the message by that MCP Emails id and get its Message-ID (IDENTITY), then run STEP 2's full lookup",
      "allmail: read the message by that MCP Emails id and get its key (KEY; a Zoya-on row under 2 hours old waits), then "
      "run STEP 2's full lookup")
c = R(c, "No hit: set its Source ID to the msgid: key", "No hit: set its Source ID to its key")
c = R(c, "(several: the one whose Source ID is exactly the msgid: key, else the oldest)",
      "(several: the one whose Source ID is exactly its key, else the oldest)")
# SELF-CHECK and ledger
c = R(c, "Any whose Source ID doesn't start \"msgid:\" goes to Trash (it has no relations yet, decision 416) and the run ends "
      "Failed, \"<n> rows without msgid: trashed\".",
      "Any whose Source ID starts neither \"msgid:\" nor \"adid:\" goes to Trash (it has no relations yet, decision 416) and "
      "the run ends Failed, \"<n> rows without a mail key trashed\".")
c = R(c, "Each message worked has one body line \"<msgid>: Activity <id>", "Each message worked has one body line \"<key>: Activity <id>")
# read to and UIDVALIDITY
c = R(c, "never past a pending one but an mcp: one",
      "never past a pending one but an mcp: one, nor past a Zoya-on one left for her under 2 hours (KEY)")
c = R(c, "the report, the end time, counts,",
      "the report, the end time, \"UIDVALIDITY: not exposed\" (the tool shows none; note it if it ever does), counts,")

# ---- actions (one line, plus the THREAD read for adid: rows) ----
a = R(a, "(Kind Email in or Email out, Source ID msgid:, page body", "(Kind Email in or Email out, Source ID msgid: or adid:, page body")
a = R(a, "Query mail Activities (Kind Email in or Email out with Source ID msgid:,",
      "Query mail Activities (Kind Email in or Email out with Source ID msgid: or adid:,")
a = R(a, "read its THREAD by Message-ID only where a step needs the chain",
      "read its THREAD by Message-ID only where a step needs the chain (an adid: row: read [Gmail]/All Mail:<UID>, then "
      "the messages its References name)")

for name, s, d in (("capture.txt", c, cd), ("actions-v2.txt", a, ad)):
    b = s.encode()
    assert s.count(chr(0x2014)) == d and len(b) <= 40000, (name, len(b))
    open(os.path.join(outdir, name), "wb").write(b)
    print(f"{name:15s} {len(b):6d} {hashlib.sha256(b).hexdigest()[:16]}")
