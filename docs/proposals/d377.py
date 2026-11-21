"""Decision 377 (Akshay, 21 Oct, via the CTO), widening decision 376 as live (calendar c84e76c9db708291, Zoya
d74d56bb06f20147), plus the edit-notes trigger to Sarika (decision 226, never fired). 1/ Every show: the calendar makes the
"Transcript: " task for every recording, and the sweep makes one for any recent Episode without a Transcript file. 2/ Zoya
looks before asking (Akshay's Sent thank-you, her inbox, Drive "Zencastr Transcripts"), asks Ranjita only if nothing is
found, takes the file herself (attach to the Episode, read back, the decision 374 test on Founder Thesis, the thank-you
draft with the transcript), then closes the row. 3/ Edit notes in any guest or PR mail reach Sarika on WhatsApp.
Rows made by hand on 21 Oct have no "transcript:" Source ID, so the calendar also skips a recording that already has a
hand-made "Transcript: " row for its date. Usage: python3 d377.py <live dir> <out dir>"""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()[:16]
CAL, ZOYA, SWEEP = "trig_01Voiz5YsK2SnVf2STF8PoSH", "trig_01UPT8LDrBDL5JQqW91Awgbo", "trig_01MdfUFg2qrebDWgiHwncgnd"
BASE = {CAL: (53973, "c84e76c9db708291"), ZOYA: (52034, "d74d56bb06f20147"), SWEEP: (30059, "60aa8ecdbe064c78")}
EDITS = {
 CAL: [
  ("STEP 4f. TRANSCRIPT REQUESTS (decision 376, Akshay, 21 Oct: Zencastr no longer gives a standalone transcript; runs on its own, outside STEP 4's filter). For every Founder Thesis recording event on ad@thepodium.in",
   "STEP 4f. TRANSCRIPT REQUESTS (decisions 376, 377, Akshay, 21 Oct: Zencastr no longer gives a standalone transcript; every show; runs on its own, outside STEP 4's filter). For every recording event (Founder Thesis, un#, Built to Share, Human by Design) on ad@thepodium.in"),
  ("or if any Engagement already has Source ID \"transcript:cal:<event id>\" (look it up first; a retry never creates a second row).",
   "or if any Engagement already has Source ID \"transcript:cal:<event id>\" (look it up first; a retry never creates a second row), or if a Kind Task row with For engagement = that guest row and a Name starting \"Transcript: \" already names that recording's date (rows made by hand on 21 Oct have no Source ID)."),
  ("Name \"Transcript: <guest> @ <company> (FT, <D Mon> recording)\"",
   "Name \"Transcript: <guest> @ <company> (<FT|un#|B2S|HBD>, <D Mon> recording)\""),
 ],
 SWEEP: [
  ("\nSTEP 4. FLAG WHAT HAS GONE QUIET OR IS MISSING",
   "\nSTEP 3i. EPISODES WITHOUT A TRANSCRIPT (decision 377). Episodes (collection://5d250752-6db8-4ab6-8467-c68f5838278a) on any show with Recording date in the last 60 days, Status not Published and not Not releasing, and no Transcript file. Each needs one open Kind Task row asking for its transcript: skip it if any Engagement has Source ID \"transcript:\" plus the Episode's recording key (its Source ID or \"Recording key:\" line, cal:<event id>) or \"transcript:episode:<Episode page id>\", or if a Kind Task row with For engagement = the Episode's Engagement and a Name starting \"Transcript: \" names its Recording date. Else create it as the calendar's STEP 4f does (Name \"Transcript: <guest> @ <company> (<show>, <D Mon> recording)\", Kind Task, Show Internal 40019a301a7f81d1a33fd4fba7cd920c, For engagement = the Episode's Engagement, Task state Handed over, Waiting on Zoya, Next action \"Zoya: ask Ranjita for the transcript (decision 376)\", Next date today, Source Agent, Source ID \"transcript:\" plus the recording key, else \"transcript:episode:<Episode page id>\", Captured today). At most 10 a run, oldest Recording date first. Report the rows created.\n\nSTEP 4. FLAG WHAT HAS GONE QUIET OR IS MISSING"),
  ("audit handoffs filed and fixes observed or reopened (STEP 3h);",
   "audit handoffs filed and fixes observed or reopened (STEP 3h); transcript task rows created (STEP 3i);"),
 ],
 ZOYA: [
  ("Kind Task rows with Show Internal are team work, never guest mail. a. A row with Task state Handed over, Waiting on Zoya and Source ID starting \"transcript:cal:\", and no Email out Activity linked to it yet (a retry never resends): send the transcript request from your inbox in that wording,",
   "Kind Task rows with Show Internal are team work, never guest mail. a. TRANSCRIPT ROWS (decision 377, every show): a row with Task state Handed over, Waiting on Zoya and a Name starting \"Transcript: \". LOOK BEFORE ASKING: first search for that guest's transcript from that recording date: a .txt attached to Akshay's sent thank-you to the guest or PR (ad@thepodium.in Sent, since the recording), your own inbox, and the Drive folder \"Zencastr Transcripts\". Found: take it as in c, send nothing. Not found, and no Email out Activity linked to the row yet (a retry never resends; rows whose Next action already says the request went need none): send the transcript request from your inbox in that wording,"),
  ("c. When Ranjita's reply carries a .txt, .docx or .pdf transcript, leave the mail in your inbox and set Next action \"Mac: attach transcript from Zoya's thread\"; on the first run after its Episode has a Transcript file, set Task state Done and clear Waiting on.",
   "c. TAKING THE FILE (decision 377): when Ranjita's reply on the request thread carries a .txt, .docx or .pdf transcript, or a found one: (1) save it with MCP Emails (action attachment) or Drive and convert .docx or .pdf to plain .txt with Bash; a conversion that fails goes to Akshay's list. (2) Attach the .txt to the Episode's Transcript file (Notion create-attachment up to 200 KB, else a file upload), re-fetch the Episode and confirm the file is there, then write \"## Transcript\" at the top of its page body: file name, bytes, sha256 (Bash sha256sum), source (Ranjita's reply of <D Mon>, or where you found it). (3) Founder Thesis, row still Booked: decision 374's test, both voices in the transcript (Akshay and the guest each speak at length) and 20 minutes or more of conversation: set Status Recorded, clear Call type, Claude note \"YYYY-MM-DD: recorded <date> (transcript)\". It fails: Akshay's list, \"Akshay: <guest>'s <D Mon> transcript looks incomplete (<why>)\", and stop here. (4) Thank-you: if the row has a thank-you draft (\"Zoya drafted: FT thank-you\" or \"Zoya drafted: client thank-you\" Activity), attach the .txt to that draft in ad@thepodium.in (MCP Emails draft) and read the draft back to confirm the attachment; Founder Thesis with no draft and no thank-you in Akshay's Sent: create the draft in ad@thepodium.in the way the calendar's STEP 4c does (approved \"FT thank-you after recording\" wording in Akshay's voice, To the guest and the main PR, Cc every other Stakeholder and the house copies), the .txt attached, read back, log \"Zoya drafted: FT thank-you for <guest>\". Then make sure Akshay's Next action has \"Akshay: send the thank-you draft to <guest first name> (transcript attached)\". (5) Close the row: Task state Done, Waiting on cleared, Claude note \"YYYY-MM-DD: transcript attached (<bytes> B, <sha256 first 16>)\". A reply saying there is no transcript or the recording failed: Akshay's list, \"Akshay: no transcript for <guest>'s <D Mon> recording (<what Ranjita said>)\", row On hold."),
  ("\nSNOOZED ASKS (decision 302",
   "\nEDIT NOTES TO SARIKA (decision 226; Sarika in Cc on a thread is not informed). Every run, read the Activities from the last 72 hours on in-scope rows: one whose Summary starts \"Edit notes:\", or any mail from the guest or PR side (to ad@thepodium.in or to you) asking to cut, trim or remove a part, use a re-shot segment, change a tag or a bio line, gets a queue step \"Zoya: WhatsApp Sarika the edit notes for <guest>\" unless an Activity \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\" is dated after it. Send it this run per TEAM WHATSAPP (guest, episode, each change with its timestamp, or the attachment's name; a request to see the edit first is Akshay's call: say so and put it on his list), log \"Zoya sent: WhatsApp to Sarika: edit notes for <guest>\", and take the step out.\nSNOOZED ASKS (decision 302"),
 ],
}
for tid, edits in EDITS.items():
    s = open(os.path.join(src, f"{tid}.txt"), encoding="utf-8").read()
    dashes = s.count("\u2014")
    assert (len(s.encode()), sha(s.encode())) == BASE[tid], (tid, len(s.encode()), sha(s.encode()))
    for a, b in edits:
        assert s.count(a) == 1, (tid, a[:60], s.count(a))
        s = s.replace(a, b)
    b = s.encode()
    assert len(b) <= 65536 - 200 and s.count("\u2014") == dashes, tid
    open(os.path.join(out, f"{tid}.txt"), "wb").write(b)
    print(tid, len(b), sha(b))
