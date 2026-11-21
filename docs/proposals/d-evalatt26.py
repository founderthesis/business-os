"""Evals read pitch attachments first (Build board card 40519a301a7f818ea871de8279841422; Akshay, 26 Oct: yes; Mail
issues 3fa19a301a7f81399958c214a4748fd9). A pitch whose profile sat in a .docx got "nothing public to verify". The evals
routine has Gmail but not MCP Emails, so attachments come from Gmail RAW: a large result is saved to a file by the
runtime, and Bash decodes it there (tested 26 Oct on the Krisp pitch, a 967 KB .docx, 1,578 characters of bio, and the
Escobar Bandra pitch, two PDFs, 2,072 characters, with Python's email, zipfile and pypdf). The text goes to the skill as
the backgrounder; an attachment that can't be read is named in the eval. Evals on the live prompt (14,795 /
1d87f124107a06c6). Usage: python3 d-evalatt26.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
EVALS = "trig_01R1yHgEztVEo832zMwUugBr"
BASE = (14795, "1d87f124107a06c6")
EDITS = [
 ("or else the Gmail Link on the latest Email in Activity linked to the Engagement).",
  "or else the Gmail Link on the latest Email in Activity linked to the Engagement). ATTACHMENTS FIRST (Akshay, 26 Oct: a "
  ".docx profile was missed): for every message on the pitch thread with attachments (get_message FULL_CONTENT lists "
  "them), read each PDF, .docx, .doc, .txt or .md before the eval: get_message RAW (a large result is saved to a file; "
  "never print it), then in Bash decode the base64url and the MIME parts (python3 email), and take the text: .docx from "
  "word/document.xml (zipfile), PDF with pypdf or else the Read tool on the saved file, text files as they are. Images, "
  "decks you can't parse and anything else: name the file. Keep only the text; never paste raw data into a row."),
 ("and the full pitch text.",
  "and the full pitch text plus every attachment's text as the backgrounder (\"Attachment <file name>:\" before each). "
  "The eval says which attachments it read, and names any it couldn't read and why; it never says \"nothing public to "
  "verify\" about facts an attachment gives."),
]
s = open(os.path.join(src, f"{EVALS}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
for a, b in EDITS:
    assert s.count(a) == 1, (a[:50], s.count(a))
    s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{EVALS}.txt"), "wb").write(b)
print(EVALS, len(b), sha(b))
