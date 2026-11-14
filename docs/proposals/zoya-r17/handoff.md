# Zoya r17: decisions 461 and 462 (4 Nov)

r17 is built on r16 (`../zoya-r16/`, waiting on Cleanup), so it carries 456 and the 445 follow-up too. Apply `build_one.patch` to `routines/zoya/build_one.py` at f70901f; it adds the parts slowtask-intro, slowtask-load, episodes-intro and episodes-work.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 2f7b8c3bc5bdc5c45ad29f5aa35bd2e143c0459d`. Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | Hourly Zoya (trig_01UPT8LDrBDL5JQqW91Awgbo) | 53,674 / 3a53c85f10d5c436 |
| `zoya-slow.txt` | Zoya SLOW | 12,515 / 840a47dc4151e46c |
| `zoya-slow-work.txt` | The pinned SLOW file | 78,805 / b21a4a03c87384d8 (78,801 characters), at 2f7b8c3 |
| `zoya-episodes.txt` | **New:** Zoya episodes | 44,425 / f9eac17185ca21db |

## 462: the day-before mail

- **Where the change lives:** the day-before mail is sent by the calendar routine's STEP 3b, not by Zoya's prompts. So the 462 change is in `../calendar-454/` (454b, 59,755 / 675f3493). There, Zoya sends it on Founder Thesis, un# and Built to Share, on the guest's thread, with the recording link. Human by Design stays a draft.
- **The Zoya side:** SCOPE's un# link list adds "unhashed.co/studio for a recording only (decision 462)". That's shared text, so the SLOW file moves to 2f7b8c3.
- **Wording (CTO, Notion):** a "Recording tomorrow (client show)" toggle, in Zoya's voice. The details are in calendar-454's hand-off.

## 461: the Zoya episodes task (new)

**Schedule: recommend `CRON_TZ=Asia/Tokyo 10 13 * * 1-5`, Opus, with the same connectors as Zoya SLOW (MCPEmail, Notion, Gmail, Google-Calendar, bluetick).**
- **Why not 10:40:** the hourly Zoya starts at 10:38 and holds the lock, so a 10:40 run would skip every day.
- **Why not 10:10:** that's 06:40 IST, outside team hours, so the editors' WhatsApp would never go.
- **Why 13:10:** it's 09:40 IST and clear of 12:38. Choose another slot clear of :38, 11:08 and 17:08 if you prefer.

**What's in it:** the shared text (TOOLS, RULES LOAD, NOTION DATA, SCOPE, ACTIONS, VOICE, SENDING, TEAM WHATSAPP with team hours, LIMITS, ONE MAIL, MESSAGE IDENTITY, LOCK, RUN RECORD with "Run zoya-episodes ...", HARD RULES), plus EPISODES WORK:
- **Timing:** no new item after minute 22, measured. Each item gets one line: done, sent, held, blocked, or unfinished with a real reason. An unexplained early exit is Failed.
- **E1, Your call on Episodes:**
  - **What it applies:** Tags (existing options only), Planned release, a Status he names, and Editor notes as a dated line. Work started stays at most 6: a seventh goes on Akshay's list.
  - **Editors:** an editor note also goes to **Sarika** on WhatsApp, in a team hour. **To confirm:** the prompts and Notion name no other editor. If the editors are someone else, say who.
  - **Then:** one Activity with his text, and Your call is cleared.
  - **Unclear:** it goes on the guest Engagement for Akshay, and Your call is left as it is.
- **E2, release-date mails:** for an Episode at Scheduled, Work started, Draft ready or Ready to release with a future Planned release, and no "Zoya sent: release date for <guest> (<date>)" for that date.
  - **How it goes:** on the guest's thread, from the wording page's **"Release date" toggle (the CTO adds it; with no toggle, nothing sends)**, with the 461 disclaimer word for word.
  - **A moved date** says it moved, in one line.
  - **Checks:** SHOW CHECK, LEAK CHECK, PRE-SEND checks, quiet hours and the caps all apply.
  - **The key** is ACTIONS', with a 60-day Sent check.
  - **Replies:** a reply to one of these mails is the hourly task's, as today.
  - **Watch the first run:** once the dates are final, it mails every set date, within the caps. A cap carries the rest to the next day.
- **E3, working docs:** for a Founder Thesis Episode at Scheduled or Work started, releasing within 21 days, with no Working doc.
  - **With a transcript:** the run uses the ft-working-doc skill to make the doc and sets Working doc. Status is never touched. If the scheduled task can't load the skill, the item is blocked, "ft-working-doc not available; CTO". **To check:** whether the skill loads in a scheduled run.
  - **With no transcript:** one line to Mamatha every 2 working days, on her request thread, Cc Akshay.
  - **Client-show Episodes:** a report line only.
- **E4:** a report.
- **EPISODES SETUP (461.1, one time):**
  - **"SETUP PREVIEW":** fire the task with this as its message to list the Work started Episodes by Planned release, the first 6 to keep and the rest to move. It writes only its record, so the CTO can post the six to Akshay.
  - **"SETUP":** moves the rest back to Scheduled, with one Activity each, and reads each back.
  - **Neither sends anything.** A second SETUP does nothing.
- **Shared change:** ACTIONS' Sent reconcile now counts run:zoya-episodes: records too.

**Known noise:** the shared SCOPE text still names INTERNAL TASKS and routine steps this task doesn't have. They're harmless here, because its steps are only E1 to E4.

## Deploy (CTO)

1. The pin moves to 2f7b8c3, with the sha256 read back (b21a4a03).
2. Paste A (zoya-one) and B (zoya-slow).
3. Deploy calendar 454b in the same window.
4. **The episodes task, only after Akshay's go (461):**
   - create it disabled, set it to Opus, and read it back;
   - fire it with "SETUP PREVIEW";
   - post the six to Akshay;
   - on his ok, fire it with "SETUP", then enable it.

**Status:** built, not replayed. Ready for Cleanup. Nothing is deployed, and the pin ref hasn't moved.
