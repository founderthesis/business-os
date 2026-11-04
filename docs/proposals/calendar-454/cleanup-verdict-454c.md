# Cleanup verdict: calendar sync 454c (decisions 453, 454, 445, 462, 456)

Cleanup session, 4 Nov 2026, about 21:40 JST. Read-only.

## Verdict: 454c accepted, 59,770 / e99618ff24e85247, with one deploy-timing condition

Base: the live prompt, which get_trigger saved to a file. It hashes to 57,968 / f6d140196f3b75b4, the hash patch.py asserts, and the trigger was last updated 1 Nov. Running patch.py twice gives the same bytes both times, equal to calendar.txt. The diff against live has only the handoff's edits:
- 454: the prep event links, "Dossier:" and "Prep note:" first.
- 453: the day-before note never waits on the link.
- 445: zencastr.app.link is recognised.
- 462: Zoya sends the day-before mail on FT, un# and Built to Share; Human by Design stays a draft.
- 454c: transcript rows name Mamatha.

This supersedes my earlier 454 acceptance (a06a8b37). Note that 454c doesn't carry the decision 460 AD Tasks rename I gave for 454 (a2ea9c6d). If the live prompt still says "AD Personal", re-apply `s.replace("AD Personal","AD Tasks")` after the patch and re-hash.

## Deploy condition

D1. Don't deploy before the 22:35 JST run tonight has finished, unless Adrian's 5 Nov row already has a "Zoya drafted: Recording tomorrow" or "Zoya drafted: day-before note" Activity. The old path drafted his note in Akshay's Drafts today. If 3b's skip check doesn't find that Activity, the new 3b would also send one from Zoya, and Akshay could still send the draft. After tonight, the 5 Nov recording is "today", not "tomorrow", so the new 3b never selects it.

## Should-fix (not blocking)

- S1. Guest with no email. 3b says "To the guest". Ryan Louvar's People row has no email (his 16 Nov row flags it). Use the fallback Zoya's guest-facing rule uses: the guest's invite address, else the company-side person on the row. If neither exists, put it on Akshay's list unsent.
- S2. Recipients and Sent check in code. Zoya's own sends assert To and Cc in python, and check both inboxes' Sent (PRE-SEND 2/ and 5/). 3b sends from her inbox without either. Carry both over.
- S3. The Human by Design question ("should HBD's go from Zoya too, and with which link?") is a handover to Akshay. Under decision 459 it goes on a Kind Task row (Source ID cto:2026-11-04:hbd-day-before-462), not in a handoff file.
