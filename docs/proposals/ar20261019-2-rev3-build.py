"""AR-20261019-2 rev 3 (decision 363): WhatsApp logs work messages hourly, replies to "@zoya", and posts editing and
production notes to "All things FT". Composed on Cut 1's WhatsApp output. Replaces rev 2 (1d25542), per Cleanup's
21 Oct 00:51 UTC verdict and the CTO's targets: at most ~4 KB more WhatsApp prompt, nothing beyond the three behaviours,
no work picked by Next action wording, no sender beyond decision 363.
Only the WhatsApp prompt changes. Zoya and the inbox stay as Cut 1 leaves them (rev 2's TEAM ASK paragraph, hard-rule
line and inbox bullet are dropped with decision 336's ask-and-answer loop).
Usage: python3 ar20261019-2-rev3-build.py <dir with cut-1 outputs trig_<id>.txt> <out dir>"""
import hashlib, os, sys

def sha(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
BASE = (21598, "0b4dda9276486041")  # Cut 1 WhatsApp output

Z = """STEP 0z. @ZOYA IN ANY CHAT (decision 363). A message whose own text starts with "@zoya", any case (not a quoted or forwarded message, not a post of yours), is a request to Zoya. Find them without reading other messages: cursor = Date of the newest Activity with Source ID "wascan:mentions" (Kind Note, Source WhatsApp), else 48 hours ago, minus 2 hours. List chats active since the cursor (names and ids only), then list_messages in batches of up to 25 chat_ids with query "@zoya" and since the cursor. Skip the Zoya group (STEP 0) and any message with an Activity "wa:<its key>". A chat whose result is truncated, indexOnly or skipped is not covered: name it in the report. Log the scan as that Activity, Date the scan time if every chat was covered, else the oldest uncovered point. At most 10 a run, oldest first; one left for later (the cap, or the hours below) keeps the cursor before it.
In a chat STEP 1 would skip as personal, act only on Akshay's own. Read up to 10 messages before it and any message it quotes. Then by author:
- Akshay (fromMe), or a teammate (saved contact name equals the Name of a People row tagged Team, or the digits match its Phone): answer from Notion, or do the step as 0a does. Only Akshay's own message carries his decision; a teammate's ask for one (guest yes or no, price, term, cut approval, release date) goes on the row as "Akshay: <name> asks <what> (WhatsApp <D Mon>)" with Akshay added to Waiting on.
- Anyone else: nothing from Notion and nothing applied. Capture the ask on its row ("Zoya: reply to <name> on WhatsApp: <ask>", Zoya added to Waiting on) and reply only "zoya here. it's with the team, we'll come back to you." signed "Zoya, Akshay's AI Chief of Staff", Mon to Fri 09:30 to 19:00 IST.
Reply once, quoting the message: "Zoya ✨ <answer, or what you did and who has it>", in that chat, or in the Zoya group when Akshay asked in a chat with anyone outside the team. No separate "noted". None 23:00 to 07:00 JST. Log Activity "Zoya handled: @Zoya from <name> (<chat name>): <what>", Source ID "wa:<key>", the sent key in its page body.
UNCERTAIN SEND (here and in 2c): when a send's result is unclear, list_messages on that chat for a fromMe message with exactly that text before any retry. Never post the same text twice.

"""

P = """STEP 2c. PRODUCTION UPDATES TO "ALL THINGS FT" (decision 363). While logging in STEP 2, each message (not from All things FT or the Zoya group) carrying an editing or production note for an episode (edit or cut feedback, a change asked, files sent or promised, recording or release timing) gets one Activity: Kind Note, Source WhatsApp, Source ID "atft:<message key>" (skip if it exists), Summary "Production note: <guest>: <note, short>", Date the message time, linked to its Engagement and Episode, page body the words verbatim with who and when (IST).
Post the oldest Kind Note "atft:" Activities, at most 10 a run, Mon to Fri 09:30 to 19:00 IST only. First: chats search "All things FT" must return exactly one group with exactly that name; else post nothing and report it. Then three lines:
"Zoya ✨ <show short name>: <guest> / <company>
<who> (<chat name>, <D Mon HH:MM> IST): <the note, short>
Work: <Episode URL, else Engagement URL>"
No phone number, email address, price or term, and never a cut approval or a date nobody gave. After a confirmed send set that Activity's Kind to WhatsApp and add the sent key to its page body.

"""

EDITS = [
    ('WHATSAPP IS READ-ONLY, with two exceptions: STEP 0 posts text messages in the group named exactly "Zoya" (chats search "Zoya", chatType group), and STEP 3c sends text messages to Akshay\'s own chat (its id is the "from" of any message of his with fromMe true; never typed). Nowhere else.',
     'WHATSAPP IS READ-ONLY, with four exceptions: STEP 0 posts text messages in the group named exactly "Zoya" (chats search "Zoya", chatType group), STEP 3c sends text messages to Akshay\'s own chat (its id is the "from" of any message of his with fromMe true; never typed), STEP 0z replies once in a chat where a message starts "@zoya", and STEP 2c posts in the group "All things FT" (decision 363). Nowhere else: never an unsolicited message to a guest, PR, host or any other group.'),
    ("Kind Task, no Show and no Guest,", "Kind Task, Show AD Personal unless the task names a show, no Guest,"),
    ("\nSTEP 1. WHICH CHATS\nWindow: from the newest Activity with Source WhatsApp (its Date)",
     "\n" + Z + "STEP 1. WHICH CHATS\nWindow: from the newest Activity with Source WhatsApp and Kind WhatsApp (its Date)"),
    ("\nSTEP 3. ", "\n" + P + "STEP 3. "),
    ("On each linked Engagement or Deal:", "Messages 0z handled (an Activity \"wa:<their key>\") change no row here. On each linked Engagement or Deal:"),
    ("Plain and short, no em dashes, no phone numbers: ",
     "Plain and short, no em dashes, no phone numbers: mentions (handled: name and what; chats not covered); production updates (All things FT check, posted, waiting); "),
]

src_dir, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
s = open(os.path.join(src_dir, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s)) == BASE, (len(s.encode()), sha(s))
for a, b in EDITS:
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)
assert len(s.encode()) <= 65536 and "—" not in s
open(os.path.join(out, f"{WA}.txt"), "w", encoding="utf-8").write(s)
print(WA, BASE[0], "->", len(s.encode()), sha(s), f"(+{len(s.encode()) - BASE[0]})")
