"""Inbox capture r13c (decision 457, then 463.7, then the 0L cursor, Akshay, 3 Nov, Tab 13 item 16): a pitch with Akshay on To or Cc is capture's to log at
once. Zoya hands those to the inbox and never logs them, so the 2-hour wait for her left Eshna Malhotra's two un# pitches
unlogged. One edit on the live capture r12e (46,565 / 9caf2cdb). Usage: python3 patch.py <capture r12e.txt> <out.txt>."""
import sys, hashlib
src, out = sys.argv[1], sys.argv[2]
b = open(src, "rb").read()
assert hashlib.sha256(b).hexdigest().startswith("9caf2cdb"), "not capture r12e (46,565 / 9caf2cdb)"
s = b.decode("utf-8")
EDITS = [
 ('Mail Zoya is on: her routine logs it first; MSGID FIND. Found: logged (STEP 1\'s exception stamps it). None, under 2 hours old: leave it for the next run',
  'Mail Zoya is on: her routine logs it first; MSGID FIND. Found: logged (STEP 1\'s exception stamps it). A pitch from outside the team (a guest, sponsored, PR or vendor pitch) with ad@thepodium.in on To or Cc is never left for her (decision 457: her STEP 1 d hands it to the inbox and logs nothing): MSGID FIND first, then REF, then RAW by HEAD, this run, no wait. Any other, none found, under 2 hours old: leave it for the next run'),
 # r13b, decision 463.7 (Akshay, 4 Nov): a new guest named on an existing thread gets their own Engagement.
 ("never merge People (decision 424). Then link the mail to it; create one only as below:",
  "never merge People (decision 424). A mail that names a new guest, a person who is not the Guest of the row its thread or sender belongs to (a new pitch on an old thread, as Thinking Balloon on the Parked CloudThat thread), is that guest's, whatever the old row's Status (open, Parked or closed; decision 463): find the new guest's own Engagement on that show, else create it as the pitch bullet below says, and link the mail there; the old row gets only a Claude note line \"YYYY-MM-DD: <new guest> pitched on this thread, own row <link>\", never a Status or Next action change. Then link the mail to it; create one only as below:"),
 # r13c (CTO, 4 Nov): STEP 0L takes rows behind a cursor, so already-classified rows never fill its limit.
 ('AND "Summary" NOT LIKE \'Zoya%\' ORDER BY createdTime LIMIT 10. Fetch each; one whose body has a "link:" line is passed over; work every other one as STEP 0\'s LINK says (these are STEP 0\'s LINK rows, never deferred).',
  'AND "Summary" NOT LIKE \'Zoya%\' AND (datetime(createdTime) > datetime(?) OR (datetime(createdTime) = datetime(?) AND url > ?)) ORDER BY createdTime, url LIMIT 10, bound to 0L\'s cursor (CTO, 4 Nov: classified rows kept filling the limit, so the rows behind them were never reached): the "0L after: <createdTime ISO> <url>" line of the newest run:inbox-capture: record that has one; none: "0L after: 2026-11-03T23:09:52Z https://app.notion.com/40d19a301a7f81b7b90afe7f62a427f3" (every row up to there was classified by 4 Nov 15:30 JST). Fetch each; one whose body has a "link:" line is passed over; work every other one as STEP 0\'s LINK says (these are STEP 0\'s LINK rows, never deferred). After the batch, write "0L after:" with the createdTime and url of the last row, in that order, such that it and every row before it in the batch now has a "link:" line; a row left without one holds the cursor there, gets a body line "0L try <n> <run id>", and at its third try the line "link: <run id> stuck <why>" (settled, in the report).'),
 # r13c (CTO and Cleanup 718ada8, 4 Nov): the loop-in is the bare introduction only.
 (' Optionally the ask in a few words.',
  ' Nothing else (CTO, 4 Nov, clarifying decision 421): no chase, offer, sponsored ask or reminder of ours and no restated ask; Zoya chases from her own inbox.'),
]
for a, c in EDITS:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, c)
assert "—" not in s
ob = s.encode("utf-8")
assert len(ob) <= 65536 - 200
open(out, "wb").write(ob)
print(len(ob), hashlib.sha256(ob).hexdigest()[:16])
