"""Decision 458: insert the Apify socials step (apify_step.md) into the installed guest-eval and dossier skills, just
before each one's next step after research. Usage: python3 build.py <installed skills dir> <out dir>."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
step = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "apify_step.md")).read().rstrip("\n")
ANCHORS = {
 "ft-guest-eval": "## Step 3: Calibrate against the channel",
 "un-guest-eval": "## Step 3a: score Fit (1 to 10)",
 "bts-guest-eval": "### Step 3: score Satish Fit (1 to 10)",
 "hbd-guest-eval": "### Step 3: Score Audience Fit (1 to 10)",
 "ft-host-dossier": "### Stage 2 — Gap-fill (3-6 targeted searches)",
 "un-dossier": "## 1b. Emit the Grok prompt, then STOP",
 "bts-host-dossier": "### Stage 2 — Gap-fill",
 "hbd-host-dossier": "#### Phase 1b: Set the technical depth dial",
}
for name, anchor in ANCHORS.items():
    s = open(os.path.join(src, name, "SKILL.md"), encoding="utf-8").read()
    a = "\n" + anchor + "\n"
    assert s.count(a) == 1, (name, s.count(a))
    assert "Apify" not in s, name
    s = s.replace(a, "\n" + step + "\n\n" + anchor + "\n", 1)
    os.makedirs(os.path.join(out, name), exist_ok=True)
    open(os.path.join(out, name, "SKILL.md"), "w", encoding="utf-8").write(s)
    print(name, len(s.encode()), hashlib.sha256(s.encode()).hexdigest()[:16])
