"""Evals selector (CTO, 21 Oct, decision 160): a legacy "claude.ai/share/" chat link in Eval link counts as missing, so
STEP 2b rebuilds the decision page for open rows; closed rows are outside 2b's selector and stay as they are.
Built on the live Evals prompt. Usage: python3 d160-share.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
EV = "trig_01R1yHgEztVEo832zMwUugBr"
s = open(os.path.join(src, f"{EV}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == (14795, "1d87f124107a06c6")
a = "take up to 8 Engagements where Eval link is not a claude.ai link and either"
b = "take up to 8 Engagements where Eval link is not a claude.ai link (a \"claude.ai/share/\" chat link counts as not one: it opens a shared chat, not the decision page, decision 160) and either"
assert s.count(a) == 1
s = s.replace(a, b)
# Cleanup: STEP 2c must not republish to a share link (the Artifact tool can't publish to a chat URL); it makes a new page instead.
a = "If Eval link is empty or not a claude.ai link, publish a new page"
assert s.count(a) == 1
s = s.replace(a, "If Eval link is empty, not a claude.ai link or a \"claude.ai/share/\" link, publish a new page")
b = s.encode()
open(os.path.join(out, f"{EV}.txt"), "wb").write(b)
print(EV, len(b), sha(b))
