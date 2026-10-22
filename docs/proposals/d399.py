"""Decision 399 (Akshay, 22 Oct: "pure AI tell"): mails never describe the guest's company, in brackets or anywhere else;
name the company and stop. The CTO fixed the wording page, the two Templates rows and Rules for Zoya. The inbox's STEP 6c
still told it to fill the founder template's bracketed line with a sentence about the business: that instruction goes, and
a one-line guard takes its place. Checked: Zoya (live, d-dbl22, d398), the split parts, calendar, sweep, WhatsApp and evals
carry no such instruction.
Zoya (CTO, 22 Oct 15:45: her 15:39 run sent Anuj Jain's decision mail with "(supply chain tech and RFID, 25+ years in
the space)", word for word from the page-body draft): STEP 0e strips any company description from the drafted mail before
sending, and the LEAK CHECK bans one in every mail. Inbox on the live prompt (d-codex22 + fix); Zoya on d-dbl22 + fix +
d398 + fix. Usage: python3 d399.py <live dir> <d398-fix out dir> <out dir>"""
import sys, os, hashlib
src, d398f, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
INBOX, ZOYA = "trig_0189eZvAD8x4357cfevgZ3No", "trig_01UPT8LDrBDL5JQqW91Awgbo"
BASE = {INBOX: (src, 60937, "40b7edec9145134e"), ZOYA: (d398f, 64152, "9e9624a73692f1c4")}
EDITS = {
 INBOX: [
  ("For the founder template's bracketed line, write one specific, true sentence from the eval page (Eval link) or the "
   "Engagement's eval section: a number, a customer, a sharp idea; never generic praise. ",
   "Never describe the guest's company, in brackets or anywhere else: name it and stop (decision 399, Akshay, 22 Oct: "
   "\"pure AI tell\"). "),
 ],
 ZOYA: [
  ("the section's text in your voice (facts, price, terms and links unchanged; on un# SHOW CHECK and un# links only),",
   "the section's text in your voice (facts, price, terms and links unchanged; on un# SHOW CHECK and un# links only; "
   "first strip any description of the guest's company, such as \"(supply chain tech and RFID, 25+ years in the "
   "space)\": name the company and stop, decision 399),"),
  ("no criticism of the guest or their company.",
   "no criticism of the guest or their company, no description of their company in brackets or anywhere else (decision "
   "399: name it and stop)."),
 ],
}
for tid, edits in EDITS.items():
    d, n, h = BASE[tid]
    s = open(os.path.join(d, f"{tid}.txt"), encoding="utf-8").read()
    assert (len(s.encode()), sha(s.encode())) == (n, h), (tid, len(s.encode()), sha(s.encode()))
    dashes = s.count("—")
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("—") == dashes, (tid, len(b))
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
