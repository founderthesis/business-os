"""B1 (5 Nov feedback, item 1): guest prep notes in broad strokes, never a word on edit rights.
Usage: python3 patch_skills.py <synced skills dir> <out dir>. Copies each dossier skill folder, applies the edits
(each asserted exactly once), checks no new em dash, and zips each folder for upload to claude.ai."""
import sys, os, shutil, zipfile
src, out = sys.argv[1], sys.argv[2]
NEVER = "Never mention edit rights, review or approval, in any form (Akshay, 5 Nov)."
_UNUSED = "Built from the dossier's own themes, in the order the dossier puts them, then stripped of everything rehearsable. Six to eight lines, one line each, as a timeline with phase markers."
EDITS = {
 # un-dossier: none (CTO, 5 Nov: Akshay updated it himself on claude.ai and closed item 1; never overwrite it).
 "ft-host-dossier": [("SKILL.md", [
  ("- [ ] Guest note 350-450 words, first-person Akshay, no edit or approval promise",
   "- [ ] Guest note 350-450 words, first-person Akshay, never a mention of edit rights, review or approval"),
  ("- [ ] Guest note themes: 5-6 broad territories, a few words each;",
   "- [ ] Guest note themes: 3 to 5 broad themes, one short line each, no running order, no sequence notes, no questions;"),
  ("Themes stay broad so guests don't script their answers (Akshay, 12 Oct).",
   "Themes stay broad so guests don't script their answers (Akshay, 12 Oct). " + NEVER),
 ]), ("references/guest-prep-template.html", [
  ("<!-- 5-6 broad themes, a few words each (Akshay, 12 Oct: guests must not", "<!-- 3 to 5 broad themes, one short line each, no running order (Akshay, 12 Oct and 5 Nov: guests must not"),
  ("  <li>{{THEME_4}}</li>\n  <li>{{THEME_5}}</li>\n  <li>{{THEME_6_OPTIONAL}}</li>\n", "  <li>{{THEME_4_OPTIONAL}}</li>\n  <li>{{THEME_5_OPTIONAL}}</li>\n"),
  ("DO NOT promise review, approval, or edit rights\n     over the final episode.", "Never mention edit rights, review or approval,\n     in any form (Akshay, 5 Nov)."),
 ])],
 "bts-host-dossier": [("SKILL.md", [
  ("- **No promises of edit rights or final approval** over the episode.", "- **" + NEVER + "**"),
  ("- [ ] Guest Prep Note doesn't promise edit rights or final approval", "- [ ] Guest Prep Note never mentions edit rights, review or approval"),
 ])],
 "hbd-host-dossier": [("SKILL.md", [
  ("- **Don't promise content approval or edit rights in the prep note** unless Akshay says so for that guest.", "- **" + NEVER + "**"),
  ("- [ ] Prep note has no specific questions and no content approval promise", "- [ ] Prep note has no specific questions and never mentions edit rights, review or approval"),
 ]), ("references/guest-prep-template.md", [
  ("- **No content approval, edit rights, or transcript review** unless Akshay says so for that guest. If he does, phrase it as a courtesy, not an entitlement.", "- **" + NEVER + "**"),
 ])],
}
os.makedirs(out, exist_ok=True)
for skill, files in EDITS.items():
    d = os.path.join(out, skill)
    if os.path.exists(d): shutil.rmtree(d)
    shutil.copytree(os.path.join(src, skill), d)
    for rel, edits in files:
        p = os.path.join(d, rel); s0 = s = open(p, encoding="utf-8").read()
        for a, b in edits:
            assert s.count(a) == 1, (skill, rel, a[:60], s.count(a))
            s = s.replace(a, b)
        assert s.count(chr(0x2014)) == s0.count(chr(0x2014)), (skill, rel, "new em dash")
        open(p, "w", encoding="utf-8").write(s)
    z = os.path.join(out, skill + ".zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, names in os.walk(d):
            for n in sorted(names):
                fp = os.path.join(root, n)
                zf.write(fp, os.path.join(skill, os.path.relpath(fp, d)))
    print(skill, os.path.getsize(z))
