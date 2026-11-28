# Zoya r16 and capture r13: decisions 456 and 457, and the 445 follow-up (4 Nov)

r16 is built on the live r15c (A e2a016c5, B ce54c367, file d2955ae3 at b732cb3). Capture r13 is built on the live r12e (9caf2cdb).

| File | Bytes / sha256 |
|---|---|
| `zoya-one.txt` (A, hourly FAST) | 53,588 / e49b4170b842b5c3 |
| `zoya-slow.txt` (B, Zoya SLOW task) | 12,515 / 728358a1d8c8464e |
| `zoya-slow-work.txt` (pinned SLOW file) | 78,719 / 274cd09057943c0b (78,715 characters), at 8a3f733f5ce4576b2b6e0ab52b1485ed23edd6e6 |
| Capture r13 (`../inbox-split/capture-r13/capture.txt`) | 46,842 / 7482f2f1132bd2e6 |

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 8a3f733f5ce4576b2b6e0ab52b1485ed23edd6e6`. Built twice, byte-identical, no em dashes. Capture: `python3 patch.py ../capture-r12/capture.txt <out>`, which asserts the base 9caf2cdb. Patched twice, byte-identical.

**What changes in each prompt:**
- **A:** STEP 0r only (item 3).
- **B:** only the SLOW file's pin, hash and character total.
- **SLOW file:** INTERNAL TASKS a and c, NOTION DATA's decision 376 line, and TEAM WHATSAPP's example.
- **Capture:** one KEY sentence.

## 1. Decision 457, capture: pitches with Akshay on them are logged at once

In KEY, mail Zoya is on still waits up to 2 hours for her, but now with one exception. A pitch from outside the team (a guest, sponsored, PR or vendor pitch) with ad@thepodium.in on To or Cc is never left for her: her STEP 1 d hands it to the inbox and logs nothing. Capture logs it in the same run: MSGID FIND first, then REF, then RAW by HEAD, with no wait.

**Still to check (the CTO):** the 07:02 JST run on Wed is the first natural one on r12e, since capture runs 07:02 to 23:02. Read its record's "pending:" line and the 0A line:
- Do the 11 pends from the 23:03 run clear by HEAD?
- Are Eshna Malhotra's two pitches (All Mail 109182 and 109183) logged?

If HEAD doesn't clear them, send me the record's error lines and they go into r13b. I didn't check this, because the run hasn't happened yet.

## 2. Decision 456, transcripts (SLOW file, INTERNAL TASKS)

- **(a) The request goes to Mamatha:** To Mamatha, Cc Akshay, and not before the day after the recording.
  - Nothing waits on Mamatha (decision 352), so the row stays Waiting on Zoya, with Next action "Zoya: transcript from Mamatha for <guest>'s <D Mon> recording (asked <D Mon>)".
  - Next date is 2 working days on. On that date, with no transcript, there's one follow-up on the request thread, To Mamatha, Cc Akshay, and the date moves another 2 working days.
  - A transcript row gets no WhatsApp nudge.
  - NOTION DATA's "decision 376: transcripts to Ranjita" now says Mamatha.
  - **CTO:** the "Transcript requests" wording on Rules for Zoya should name Mamatha (a Notion edit).
- **(b) TAKING THE FILE:** this now takes any .txt, .docx or .pdf transcript that reaches Zoya's inbox from Mamatha, or anyone tagged Team, on any thread.
  - Zoya matches it to one guest's recording by the file name, the thread and the guest's name, and to its transcript row if there is one. With no row, she files it on the Episode anyway.
  - If she isn't sure which recording it is, it goes on Akshay's list and nothing is filed.
  - The source line names the real sender.
- **(c) Checked read-only in Notion (Episodes and Engagements, 4 Nov ~01:20 JST).** The calendar's STEP 4f did create rows for five of the six. They're stuck, not missing:

| Recording | Episode | Transcript row | Why it's stuck | r16 |
|---|---|---|---|---|
| Sameet Gupte, 3 Nov | Recorded, no file | Handed over, Waiting on Zoya (created 3 Nov 22:38 JST) | Not stuck: the request is due the day after | Request to Mamatha on 4 Nov |
| Saket Saurabh (Nexla), 30 Oct | Recorded, file attached by the CTO | Task state **empty**, Waiting on Zoya | Step a needed "Handed over", so it never matched | Matches now. The file is already on the Episode, so it's "found: take it as in c", and the row closes |
| Rohan Ganapathy (Bellatrix), 22 Oct | Scheduled, no file | Handed over, **Waiting on Ranjita** | The old flow: Ranjita was asked and never answered, and the row waits on her | Zoya takes it and asks Mamatha. The old ask to Ranjita doesn't block the new request |
| Matthew Spacie (Magic Bus), 20 Oct | Hold, no file | Handed over, **Waiting on Ranjita** | Same as Bellatrix | Same as Bellatrix |
| Entrust Family Office, 23 Oct | Scheduled, no file | **On hold** | Put on hold, probably by step c's "no transcript" | Unchanged. It's on Akshay's list as on hold; reopen it to Handed over if a transcript should still be asked for |
| Sanjay Varnwal (Spyne), 23 Jul | Scheduled, no file | **None** | Older than STEP 4f's 30-day and the sweep's 60-day windows | Not created by any routine. Create it by hand, or ask Mamatha directly |

## 3. The 445 follow-up (A, STEP 0r)

- **The link add still runs after a hand send.** When the recording-link mail already went (by hand, or from ad@), Zoya still adds the link to the invite and sets the Call link if the invite lacks it. This covers Col. Sai and Gulab once Mamatha confirms their links.
- **Mamatha's correction wins.** A later line from her for the same guest replaces an earlier link: the invite and the Call link take the new one. If the mail already went with the old link, it goes on Akshay's list as "Akshay: <guest>'s recording link changed after the mail went". Zoya never sends a second mail on her own. That's Sameet's case: the wrong room went to him.

## Not in this build

- **Item 5, calendar 454 (the prep event links).** It's next, built from a read-back of the live calendar prompt (trig_01Voiz5YsK2SnVf2STF8PoSH).
- **Item 4, the Apify socials step (458).** It comes after 454, as skill patches in `skills/`.

**Status:** built, not replayed. Ready for Cleanup. Nothing is deployed, and the pin ref hasn't moved. The CTO deploys.
