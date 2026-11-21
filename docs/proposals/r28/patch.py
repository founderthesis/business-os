"""r28 non-Zoya edits (Codex CX-20261113T0800 item 3), built on the live sweep (r24, 2203cc3f; also the day chat's copy).
Usage: python3 patch.py sweep docs/proposals/r24/sweep.txt <out>
Each edit is asserted once; no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"sweep": "2203cc3f"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the live %s" % which
s = b.decode("utf-8")
EDITS = {
"sweep": [
 # Saved skipped phases first, 3h first of all.
 ("Before your part's first step, read the previous run of the same part (its report Activity, Source ID \"sweep:<A|B>:<YYYY-MM-DD>\"): a step it skipped runs first.",
  "Before your part's first step, read the previous run of the same part (its report Activity, Source ID \"sweep:<A|B>:<YYYY-MM-DD>\"): every step it left unfinished, without a line, or with remaining above 0 runs first, in your part's order but STEP 3h before the rest."),
 # 3h reads the current audit channel; no duplicate of what the CTO already tracks.
 ("a. Auditor handoffs. Fetch the OS Audit page (3fc19a301a7f8171b1e2ef19ded7c239) and read only its section \"Independent review — latest checkpoint\". For each action it asks of the builder or main session, and each question or UI step it puts to Akshay, with its request id (AR-<date>-<n>; with none, use the checkpoint date and its position): if no Engagement has that id in its Name, create a Task row",
  "a. Auditor handoffs (decision 516). Read the \"Latest checkpoint\" on the CTO Audit page (40419a301a7f81c48c29d894e433750d); the OS Audit page (3fc19a301a7f8171b1e2ef19ded7c239) is history, never a source of new work. For each action it asks of the builder or main session, and each question or UI step it puts to Akshay, its id is \"<checkpoint id> item <n>\" (CX-<date>T<time>, else its AR- id). Skip it when a CTOA card on the Build board (collection://88a4d5c7-1880-4c65-b6de-b7c0a382f3c6) already carries that checkpoint id in its body (the CTO answers there), or an Engagement has the id in its Name or Source ID; else create a Task row"),
 # Billing search beyond "invoice".
 ("Search ad@thepodium.in (MAILBOX; not mail from ad@thepodium.in itself) since 4 days ago.",
  "Search ad@thepodium.in (MAILBOX; not mail from ad@thepodium.in itself) since 4 days ago, one search per term in subject or body: invoice, bill, payment, receipt, GST, remittance; merge the results by Message-ID, then judge each as below."),
 # Per-phase counts, and Completed only with nothing remaining.
 ("Then one line per step of your part, in TWO PARTS' order: \"step <name>: done <n> | unfinished",
  "Then one line per step of your part, in TWO PARTS' order: \"step <name>: selected <n>, done <n>, remaining <n> | unfinished"),
 ("Completed only if every step of your part has a line and each is done;",
  "Completed only if every step of your part has a line, each is done and its remaining is 0;"),
],
}
for a, c in EDITS[which]:
    assert s.count(a) == 1, (which, a[:70], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) <= b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, (which, len(ob))
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
