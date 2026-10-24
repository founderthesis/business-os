"""Build Zoya's two trial prompts (decision 394, FAST/SLOW; spec docs/proposals/zoya-split.md) from the shared part files
in routines/zoya/parts. Every rule lives in one part file; the manifests below say which parts each prompt carries, and the
few per-prompt rewrites are listed in VARIANT. Usage: python3 build.py <out dir> [<single-prompt source to check coverage>]
Writes zoya-fast.txt and zoya-slow.txt, prints bytes and the first 16 of sha256, flags a FAST prompt over the 25 KB target, refuses any
prompt over the 65,536-byte cap less 200, or an em dash. With a source prompt, it also lists every source line that neither
output carries word for word (the lines the split rewrote on purpose). Each prompt's run record names its version, "zoya-<fast|slow>
<12 hex>": to check one, write that stamp back as @@VERSION@@ and sha256 the prompt."""
import sys, os, re, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
part = lambda n: open(os.path.join(PARTS, n + ".txt"), encoding="utf-8").read().rstrip("\n")

FAST = ["intro-fast", "tools", "rules-common", "rules-tail", "notion-data", "scope", "actions", "queue-fast", "voice",
        "sending", "limits-fast", "onemail", "identity", "runrecord", "fast-order", "decision", "daybefore", "mail", "report-fast",
        "hard"]
SLOW = ["intro-slow", "tools", "rules-common", "rules-routines", "rules-tail", "notion-data", "scope", "actions",
        "queue-slow", "internal", "editnotes", "snoozed", "voice", "sending", "teamwa", "limits", "onemail", "identity", "runrecord",
        "reconcile", "slow-order", "feedback", "bounces", "vendor", "ownermail", "scorecard", "payments", "followups",
        "report-slow", "hard"]
# (part, old, new): rewrites that only one prompt needs
VARIANT = {
 "fast": [
  # FAST-only cuts: text this run never uses (no WhatsApp, follow-ups, vendor forms, internal tasks, release mail)
  ("tools", " Blueticks sends WhatsApp to the team (TEAM WHATSAPP). Web search finds news for news angles.", ""),
  ("tools", ', "+bluetick"', ""),
  ("tools", " Without Blueticks, put each WhatsApp you would have sent on Akshay's list instead.", ""),
  ("notion-data", "\n- Founder Thesis guests (peers for name-drops): collection://b460a8fa-1531-49e5-82f9-133478e2278d", ""),
  ("notion-data", "\n- Mail issues: collection://2a56fcad-3015-48e4-b811-e18ff4009fe0", ""),
  ("notion-data", "- Vendor Pitches (the podm.in/pitch-to-us form): collection://d4ca5f98-d7e7-4002-9ff3-a7b3a200953d (Company / "
   "Service Name, Contact Name, Email, Phone / WhatsApp, Website, Service Offering, Pricing, Sample Work, Why Founder Thesis?, "
   "Status, Submitted). Organisations:", "- Organisations:"),
  ("notion-data", "re: PERSON STEPS GO ON THEIR ROW \\(decision 385.*", " This run creates no Task rows."),
  ("scope", ", STEP 0d); AD Personal threads for misc chase (routine 4). Engagements with Kind Task and Show Internal "
   "(INTERNAL TASKS).", ")."),
  ("scope", "\n- Routines on un#: 1 to 4 and 7 run; 5 and 8 don't; 6 sends only C16 and C17, and only when the Episode has the "
   "episode link and Sri's post link. Name-drops come from the un# sheet's past guests.", ""),
  ("scope", "\n- A guest pitched for two shows on one thread (one Engagement per show): follow up once, on the row Akshay named, "
   "and keep the other row's Next action pointing to it.", ""),
  ("voice", ', with one exception: release mail 2 opens "Zoya here, I work with Akshay on the Founder Thesis podcast."', ""),
  ("hard", "Never introduce or describe yourself except in release mail 2.", "Never introduce or describe yourself."),
  ("onemail", "(the order in ONE PERSON, ONE ASK)", "(FAST ORDER)"),
  ("runrecord", "Run zoya <", "Run zoya FAST <"),
  ("mail", "then WhatsApp Sarika the notes (guest, episode, each change with its timestamp, or the attachment's name).",
   "the WhatsApp to Sarika is your SLOW run's (EDIT NOTES TO SARIKA)."),
  ("hard", "- WhatsApp only to Jaya and Sarika, per TEAM WHATSAPP.", "- No WhatsApp from this run."),
 ],
 "slow": [
  ("runrecord", "Run zoya <", "Run zoya SLOW <"),
  ("hard", "- WhatsApp only to Jaya and Sarika, per TEAM WHATSAPP.",
   "- WhatsApp only to Jaya and Sarika, per TEAM WHATSAPP, and RECONCILE's one alert in the group \"Zoya\"."),
 ],
}

def build(name, manifest):
    texts = {n: part(n) for n in manifest}
    for n, a, b in VARIANT[name]:
        if a.startswith("re:"):  # a regex, to the end of its line
            texts[n], k = re.subn(a[3:], b, texts[n])
            assert k == 1, (name, n, a[:50], k)
            continue
        assert texts[n].count(a) >= 1, (name, n, a[:50])
        texts[n] = texts[n].replace(a, b)
    s = "\n\n".join(texts[n] for n in manifest) + "\n"
    # version stamp for the run record: first 12 of the sha256 of the prompt with the stamp written as @@VERSION@@
    assert s.count("@@VERSION@@") == 1, (name, "version placeholder")
    s = s.replace("@@VERSION@@", f"zoya-{name} {hashlib.sha256(s.encode()).hexdigest()[:12]}")
    b = s.encode()
    assert "—" not in s, (name, "em dash")
    assert len(b) <= 65536 - 200, (name, len(b))
    if name == "fast" and len(b) > 25 * 1024:
        print(f"zoya-fast is over the spec's 25 KB target by {len(b) - 25 * 1024} bytes")
    open(os.path.join(out, f"zoya-{name}.txt"), "wb").write(b)
    print(f"zoya-{name}", len(b), sha(b))
    return s

used = set(FAST) | set(SLOW)
unused = sorted(f[:-4] for f in os.listdir(PARTS) if f.endswith(".txt") and f[:-4] not in used)
fast, slow = build("fast", FAST), build("slow", SLOW)
print("parts not in either prompt:", unused or "none")
if len(sys.argv) > 2:
    src = open(sys.argv[2], encoding="utf-8").read().split("\n")
    missing = [l for l in src if l.strip() and l not in fast and l not in slow]
    print(f"source lines carried by neither prompt word for word: {len(missing)}")
    for l in missing:
        print("  -", l[:110])
