"""Decision 399 (Akshay, 22 Oct: "pure AI tell"): mails never describe the guest's company, in brackets or anywhere else;
name the company and stop. The CTO fixed the wording page, the two Templates rows and Rules for Zoya. The inbox's STEP 6c
still told it to fill the founder template's bracketed line with a sentence about the business: that instruction goes, and
a one-line guard takes its place. Checked: Zoya (live, d-dbl22, d398), the split parts, calendar, sweep, WhatsApp and evals
carry no such instruction. Inbox on the live prompt (d-codex22 + fix as deployed 22 Oct).
Usage: python3 d399.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX = "trig_0189eZvAD8x4357cfevgZ3No"
BASE = {INBOX: (60937, "40b7edec9145134e")}
EDITS = {
 INBOX: [
  ("For the founder template's bracketed line, write one specific, true sentence from the eval page (Eval link) or the "
   "Engagement's eval section: a number, a customer, a sharp idea; never generic praise. ",
   "Never describe the guest's company, in brackets or anywhere else: name it and stop (decision 399, Akshay, 22 Oct: "
   "\"pure AI tell\"). "),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
