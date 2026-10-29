"""WhatsApp hotfix on the live prompt (CTO, 30 Oct): the same parentless creates (two loose pages at 13:01Z on 29 Oct).
Input: the live WhatsApp prompt, 26,007 / 9e8b9f4891e9c03d. Usage: python3 patch_wa.py <live.txt> <out.txt>.
B2 and the d420 batch rebase on this output once it is accepted."""
import hashlib, os, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "9e8b9f4891e9c03d"
dashes = s.count(chr(0x2014))
a = "Fetch each data source once to confirm property and option names."
assert s.count(a) == 1
s = s.replace(a, a + " WRITES: every create names parent {\"type\": \"data_source_id\", \"data_source_id\": \"<the collection id "
    "above>\"}, allow_async false, the title set; never a create with no parent (it makes a loose workspace page). Then query that "
    "data source by Source ID: not found is a failed write, never logged; retry once, else report it.")
out = s.encode()
assert s.count(chr(0x2014)) == dashes and len(out) <= 65536 - 200
open(dst, "wb").write(out)
print(os.path.basename(dst), len(out), hashlib.sha256(out).hexdigest()[:16])
