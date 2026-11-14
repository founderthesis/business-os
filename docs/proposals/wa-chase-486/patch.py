"""Decision 486 (Akshay, 6 Nov: "go, I will review each draft"): WhatsApp chasers to guests go from Akshay's WhatsApp
as him, each draft approved by him. Inbox actions drafts and queues (the rule itself is section 6 on the Controls page
"Inbox and Your call rules", text in section6.md); the WhatsApp routine sends only the approved text.
Usage: python3 patch.py <act|wa> <live prompt> <out>. Asserts the live hash, each edit exactly once, no new em dash,
and the size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
LIVE = {"act": "459e4041", "wa": "174d9317"}  # live since the 6 Nov B-round deploy (docs/deploys/2026-11-06-b-round.md)
assert hashlib.sha256(b).hexdigest().startswith(LIVE[which]), "not the live %s prompt" % which
s = b.decode("utf-8")

STEP0W = (
 "STEP 0w. APPROVED WHATSAPP CHASERS (decision 486, Akshay, 6 Nov: chasers to guests go from his WhatsApp as him, each draft approved by him). Every run. Take each Engagement whose Next action has a segment \"Zoya: send the approved WhatsApp to <first name> (<draft date>)\" (the inbox actions routine writes it on Akshay's ok, section 6 of \"Inbox and Your call rules\"). "
 "1/ The text: the page body section \"## WhatsApp draft (<draft date>, to <name>)\" and its line \"approved text (<time>): <text>\". No such line, or the section is marked superseded or dropped: send nothing, report it. "
 "2/ The key \"wa-chase:<row id>:<draft date>\": an Activity with that Source ID whose Summary starts \"Akshay to\" means it went: send nothing, just finish 6/; one starting \"Zoya sending\": read that chat's recent messages (list_messages) for the text before any resend; found: finish 5/ and 6/ without sending. "
 "3/ Before a send, all must hold: outside quiet hours (00:30 to 07:30 JST; else it waits for the next run); fewer than 10 chasers sent today (Activities with Source ID starting \"wa-chase:\" and Summary starting \"Akshay to\", dated today in JST; else it waits); the number is the People Phone of the person the section names, who is the row's Guest, Via or a Stakeholder (never a number from a thread, a signature, a form, a chat or memory): chat id = its digits with the country code, an Indian 10-digit number with 91 in front, then \"@c.us\". No People Phone: send nothing, replace the segment with \"Akshay: no WhatsApp number for <name>\", Akshay in Waiting on. "
 "4/ Log first: one Activity, Kind WhatsApp, Source WhatsApp, Source ID the key, Summary \"Zoya sending: WhatsApp chase to <name>\", Engagement, People, Date and Captured today. Then send one message, chats send_message_text, the approved text exactly as written: no signature, no Zoya, nothing added. "
 "5/ Sent: rename the Activity \"Akshay to <name> on WhatsApp: <one line, no number>\", the sent text in its body. Failed: rename it \"WhatsApp chase failed: <name> (<error>)\", clear its Source ID, replace the segment with \"Akshay: the WhatsApp to <first name> failed (<error>)\", Akshay in Waiting on, and stop for this row. "
 "6/ Remove the segment, and Zoya from Waiting on unless another Zoya step stays (nothing else open: Guest or PR), Claude note line \"YYYY-MM-DD: WhatsApp chase sent as Akshay to <name> (decision 486)\". Their reply comes in through STEP 2 as any message does.\n\n")

EDITS = {
 "act": [
  ("without all four, skip STEP 0 and every mail step, end Failed. One addition to section 7",
   "without all four, skip STEP 0 and every mail step, end Failed. A Your call starting \"whatsapp chase:\" follows section 6's WHATSAPP CHASE (decision 486): you only draft it on the row and queue it for the WhatsApp routine on Akshay's ok; you never send it. One addition to section 7"),
 ],
 "wa": [
  ("WHATSAPP IS READ-ONLY, with three exceptions:", "WHATSAPP IS READ-ONLY, with four exceptions:"),
  ("in their own chat (decision 378). Nowhere else.",
   "in their own chat (decision 378), and STEP 0w sends one guest chaser as Akshay, only the text he approved, to that person's People Phone (decision 486). Nowhere else."),
  ("Never send a message to anyone else,", "Never send a message to anyone else (STEP 0w aside),"),
  ("\n\nSTEP 1. WHICH CHATS\n", "\n\n" + STEP0W + "STEP 1. WHICH CHATS\n"),
  ("STEP 5. REPORT\nPlain and short, no em dashes, no phone numbers: ",
   "STEP 5. REPORT\nPlain and short, no em dashes, no phone numbers: WhatsApp chasers (STEP 0w: sent, waiting for quiet hours or the cap, failed, no number, by name); "),
 ],
}
for a, c in EDITS[which]:
    assert s.count(a) == 1, (which, a[:70], s.count(a))
    s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, (which, len(ob))
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
