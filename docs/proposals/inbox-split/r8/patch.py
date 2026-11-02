"""Capture r8 on the live r7 (CTO, 2 Nov 12:25 JST). Usage: python3 patch.py <r7 capture> <out>
Input: docs/proposals/inbox-split/cleanup/r7/capture.txt, 39,522 / 3f08b76e (live). Each edit asserted once."""
import hashlib, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:8] == "3f08b76e"
dashes = s.count(chr(0x2014))

def R(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# 1. Link pass: a third STEP 0 class, unlinked mail rows since 1 Nov 12:00 JST, whatever their Captured; counted in STEP 1's cap.
R("or created since 2026-11-01 12:00 JST (rows the old inbox never worked); within each,",
  "or created since 2026-11-01 12:00 JST (rows the old inbox never worked); and LINK, until 2026-11-06: msgid: or adid: "
  "mail, no People and no Engagement, created since 2026-11-01T03:00Z, Captured before today, not "
  "an Email out whose Summary starts \"Zoya\"; within each,")
R("The record says \"old rows: <n> re-keyed, <n> folded, <n> linked, <n> left\".",
  "LINK: link only, as STEPS 2 and 3 do (no loop-in), read by its key (adid: by UID); no row fits: say so. The record says "
  "\"old rows: <n> re-keyed, <n> folded, <n> linked, <n> left\".")
# 2. allmail: ad@-only rows re-key to adid: with no RAW (lookup first, as now).
R("allmail: read the message by that MCP Emails id and get its key (KEY; MSGID FIND first for every allmail: row)",
  "allmail: read the message by that MCP Emails id and get its key (KEY; MSGID FIND first for every allmail: row; "
  "ad@-only and not sent from ad@: adid:<UID>, never RAW; an id outside [Gmail]/All Mail: find it there by from, "
  "subject and date for its UID)")
# D5: a STEP 0 row whose RAW fails gets the body line only, never an mcp: pending entry.
R("No key (a row whose RAW gives no Message-ID):", "No key (a row whose RAW gives no Message-ID; not pended):")
# 3. RAW always through a saved file, whole data value in chunks; never decoded by eye; failure pends, never stops.
R("Returned inline: copy the data value's first 8000 characters into a file in Bash (a heredoc), then base64 -d <file> "
  "2>/dev/null | grep -aim1 -A1 '^Message-ID:'; no complete id (one ending \">\"), append the next 8000 to the same file "
  "and run it again.",
  "Returned inline: write the data value in Bash, in order, 8000 characters per heredoc, "
  "to a new file per message (cat > r<id> <<'X' first, >> after), until a complete id (one ending \">\") "
  "shows; after each chunk run tr -d '\\n' < r<id> | base64 -d 2>/dev/null | grep -aim1 -A1 '^Message-ID:'.")

out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65336
open(dst, "wb").write(out)
print("capture r8", len(out), hashlib.sha256(out).hexdigest()[:16])
