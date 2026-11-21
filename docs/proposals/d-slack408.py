"""Decision 408 (Akshay, 24 Oct: "yes"): the WhatsApp routine also reads Akshay's Slack DMs with the hosts, Sri first,
read only, and logs scheduling lines and asks on the rows as it does for WhatsApp. New STEP 2c reuses STEP 2's Activity
shape and STEP 2b's row rules, so the Slack lines land exactly where WhatsApp's do. Activities has Source Slack but no
Slack Kind, so Kind is Note. At deploy, add the Slack connector to the WhatsApp trigger's connections.
WhatsApp on the live prompt (26,005 / 02c3c04c2e28591d). Usage: python3 d-slack408.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
BASE = (26005, "02c3c04c2e28591d")
EDITS = [
 ("Notion (ToolSearch \"+Notion\"); ",
  "Notion (ToolSearch \"+Notion\"); for STEP 2c the Slack connector (ToolSearch \"+Slack\", read only); "),
 ("\nSTEP 3. FT COMMUNITY",
  "\nSTEP 2c. SLACK DMS WITH THE HOSTS (decision 408, Akshay, 24 Oct). Read only: never post, reply, react or send in "
  "Slack. Find Akshay's direct message with each host, Sri first, then Satish and Arjun (search users by name, then "
  "read that DM), and read its messages in STEP 1's window. Skip greetings and chatter. For each DM and IST day, one "
  "Activity as in STEP 2, but Source Slack, Kind Note, Source ID \"slack:<DM channel id>:<YYYY-MM-DD>\", Summary "
  "\"<host> on Slack: <what happened>\", linked to the Engagements it names; then update those rows as in STEP 2b, "
  "with \"(Slack)\" where it says \"(WhatsApp)\". No Slack connector, or no DM with a host: skip it and say so in the "
  "report.\n\nSTEP 3. FT COMMUNITY"),
]
s = open(os.path.join(src, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
dashes = s.count("—")
for a, b in EDITS:
    assert s.count(a) == 1, (a[:50], s.count(a))
    s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and s.count("—") == dashes, len(b)
open(os.path.join(out, f"{WA}.txt"), "wb").write(b)
print(WA, len(b), sha(b))
