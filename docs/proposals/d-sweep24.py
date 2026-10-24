"""Daily sweep fix (Build board card 40219a301a7f815a8aeeefbbff9657d1; CTO, 24 Oct). On 23 Oct the sweep read 52 rows,
changed none, skipped STEPS 3b to 5 (due vs done included) and still reported success.
1/ Two parts, two runs a weekday: PART A (13:10 JST) does STEPS 2 to 3a2, the Gmail-heavy row work; PART B (15:10 JST)
   does the checks and counts, due vs done first. At deploy the trigger's cron becomes CRON_TZ=Asia/Tokyo 10 13,15 * * 1-5.
2/ Every report opens with a status line: Completed only when every step of the part ran; else Partial, naming each
   step skipped and why. A step skipped runs first in its part's next run.
3/ Due vs done (b) selects overdue rows as Zoya's STEP 2 now does (d-sel23, live 23 Oct): pursuit Status and Next date,
   whoever the row waits on, and splits them into explained (a dated hold or a named blocker in the Claude note) and
   unexplained. The CTO's acceptance for the selector fix is 0 unexplained.
Sweep on the live prompt (32,478 / 6acd0d5b1ce40f20). Usage: python3 d-sweep24.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
SWEEP = "trig_01MdfUFg2qrebDWgiHwncgnd"
BASE = (32478, "6acd0d5b1ce40f20")
EDITS = [
 ("No human is watching this run: never stop to ask a question.\n",
  "No human is watching this run: never stop to ask a question.\n\nTWO PARTS (CTO, 24 Oct: the 23 Oct run skipped STEPS "
  "3b to 5 and still reported success). The sweep runs twice each weekday. A run starting before 14:00 JST is PART A: "
  "STEPS 2, 3, 3r, 3a and 3a2. A run at or after 14:00 JST is PART B, in this order: STEP 4b, 3i, 3h, 3g, 3b, 3d, 4, 5, "
  "6c. Do only your part's steps, then STEP 7. Before your part's first step, read the previous run of the same part "
  "(its report Activity, Source ID \"sweep:<A|B>:<YYYY-MM-DD>\"): a step it skipped runs first. Log your report as one "
  "Activity, Kind Note, Summary \"Sweep <A|B> <D Mon>: <Completed|Partial>\", Source ID \"sweep:<A|B>:<today>\", the "
  "report in the page body.\n"),
 ("(b) Overdue now: open Engagements (any Kind) with Zoya in Waiting on and Next date before today, with no linked "
  "Activity of Kind Email out dated on or after that Next date.",
  "(b) Overdue now, selected as Zoya's STEP 2 does (Codex, 23 Oct): open Engagements at Sponsored offered, Precall "
  "requested, Booking, Recorded or LT chase, and any with Zoya in Waiting on, whoever else Waiting on names, with Next "
  "date before today and no linked Activity of Kind Email out dated on or after that Next date. Split them: explained "
  "(the Claude note has a \"held:\" or \"deferred:\" line with a recheck date not yet passed, or names a blocker and its "
  "owner) and unexplained (the rest)."),
 ("overdue now <n>; no message id <n>;",
  "overdue now <n> (unexplained <n>); no message id <n>;"),
 ("then up to 10 overdue rows \"<Name> (due <D Mon>)\".",
  "then every unexplained overdue row \"<Name> (due <D Mon>, waiting on <who>)\", then up to 5 explained ones."),
 ("STEP 7. REPORT\nPlain and short,",
  "STEP 7. REPORT\nFirst line: \"Sweep <A|B> <D Mon>: Completed\" only when every step of your part ran; else \"Sweep "
  "<A|B> <D Mon>: Partial: skipped <STEP>: <why>\" for each one. A step that ran and changed nothing is done, not "
  "skipped; a step cut short is skipped. Then plain and short,"),
]
s = open(os.path.join(src, f"{SWEEP}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
for a, b in EDITS:
    assert s.count(a) == 1, (a[:50], s.count(a))
    s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{SWEEP}.txt"), "wb").write(b)
print(SWEEP, len(b), sha(b))
