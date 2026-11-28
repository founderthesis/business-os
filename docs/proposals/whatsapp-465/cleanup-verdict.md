# Cleanup verdict: WhatsApp to Business OS, decision 465.2

Cleanup session, 4 Nov 2026, about 21:40 JST. Read-only.

## Verdict: accepted, 27,361 / 8628f42a4f4803d4

The live prompt came back inline and its base isn't committed. So I reversed the three edits on whatsapp.txt: that gives 26,336 / ca8009c24aaeda15, the hash patch.py asserts. The trigger was last updated 29 Oct, before the 4 Nov read-back, so live is that base. Each old string appears once in the live text I read.

The edits:
- 0a e1: Akshay's "added <name>" in the Zoya group sets Added, never from Left, and clears his asks.
- STEP 3a (3): his word in Your call, or in a Claude note line from the last 14 days, sets Added.
- b2: clears asks for rows Added by any signal, and for rows already Added that still carry one.
No new em dash. No send beyond the existing Zoya-group reply.

## Should-fix (not blocking)

- S1. When the person isn't clear in e1 ("added to whatsapp group" with no name, or two candidates), ask the one question in f., as a. does. Don't guess.
- S2. 3a (3) and b2 sit inside STEP 3, which runs on the first run of the day. (3) says every run, but b2's clearing still waits for the next day's first run, unless (3) clears them the way e1 does. Say which.
- S3. Limit (3)'s scan to the Engagements of FT Community rows at To invite or Invited, instead of every Engagement's notes every hour.
- Not in this change: the live prompt still says "AD Personal" (decision 460) and "transcripts to Ranjita" (decision 456). Carry both on the next edit.
