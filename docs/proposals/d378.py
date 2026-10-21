"""Decision 378 (Akshay, 21 Oct, via the CTO): a team member's WhatsApp message that starts "@zoya" gets an answer from
Notion within the hour. WhatsApp routine only: a new STEP 0d (STEP 0b is already the precall promises) and a third
exception to WHATSAPP IS READ-ONLY. Built on the live prompt (routines/whatsapp.md at 7eec76c).
Usage: python3 d378.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
WA = "trig_01MnmJYorWrd61K7b5BCqXr1"
BASE = (21598, "0b4dda9276486041")
EDITS = [
 ("WHATSAPP IS READ-ONLY, with two exceptions:", "WHATSAPP IS READ-ONLY, with three exceptions:"),
 ("never typed). Nowhere else.",
  "never typed), and STEP 0d replies in the chat or group a team member's \"@zoya\" question came from (decision 378). Nowhere else."),
 ("rows completed in STEP 3d (name: LinkedIn); ", "rows completed in STEP 3d (name: LinkedIn); team questions answered (STEP 0d: member, one line each); "),
 ("\nSTEP 1. WHICH CHATS",
  "\n0d. TEAM QUESTIONS (decision 378, Akshay, 21 Oct: the team can ask Zoya on WhatsApp; every run). Read the work chats STEP 1 reads that hold team members: their one-to-one chats with Akshay (Sarika Karnik Work, Ranjita Chattopadhyay Unnati Rec, Jaya Lakshmi Unnati Support, Chaandini) and team groups such as \"All things FT\" and \"Podium Content\". Take only messages not fromMe, from the last 48 hours, whose text starts \"@zoya\" (any case), from a sender whose phone matches a People row tagged Team (PHONES), with no Activity Source ID \"wa:<message key>\" yet, oldest first. A question about a guest, an episode or a show: answer it from Notion only (Engagements, People, Episodes, Activities: status, recording and release dates, eval and dossier links, transcript status, edit notes). Never the Credentials page, never fees, prices or commercial terms, never Akshay's Your call text or private notes, never a phone number or email address. Reply in that same chat with chats send_message_text, a short text starting \"zoya here:\" and signed \"Zoya, Akshay's AI Chief of Staff\". Not in Notion: say so and that you've asked Akshay, and put \"Akshay: <member> asks <question>\" on the matching Engagement's Next action with Akshay in Waiting on (no row: a Task row as in 0a b). A request to do something (send a mail, change a date): a Task row as in 0a b, and reply \"zoya here: noted, <owner> has it\". Log an Activity \"Zoya answered <member> on WhatsApp: <one line>\" (Kind WhatsApp, Source WhatsApp, Source ID \"wa:<message key>\", Engagement if one, Captured today). If list_messages fails or the engine is not connected, answer nothing and say so in the report.\n\nSTEP 1. WHICH CHATS"),
]
s = open(os.path.join(src, f"{WA}.txt"), encoding="utf-8").read()
assert (len(s.encode()), sha(s.encode())) == BASE, (len(s.encode()), sha(s.encode()))
for a, b in EDITS:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
b = s.encode()
assert len(b) <= 65536 - 200 and "—" not in s
open(os.path.join(out, f"{WA}.txt"), "wb").write(b)
print(WA, len(b), sha(b))
