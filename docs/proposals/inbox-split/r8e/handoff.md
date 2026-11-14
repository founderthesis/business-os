# Capture and actions r8e (CTO, 2 Nov 13:20 JST): CTOA-03 expedite (CX-20261102T1307)

Built on Main's r8d (capture 39,998 / 5ef8b937) and live actions r7 (39,553 / c80b1cee) by `patch.py`, rebuilt byte-identical.

| File | Bytes / sha256 |
|---|---|
| capture.txt | 40,447 / c0abafcd8755c77b |
| actions.txt | 39,935 / 1d483cbdc43a58ba |

What changes on top of r8d:
1. LINK also takes today's known batch: rows created before 2026-11-02T03:00Z (the 10:03 run's 13 unlinked rows), whatever their Captured, passed over once they carry a "link:" line. No wait until 3 Nov.
2. LINK writes "link: <run id> <linked to | internal | no fit>". A row it links to an Engagement or Deal goes on the run record's "stamped:" line, which actions already reads. Internal team-only mail is linked to the team's People rows, not to invented guest rows. No fit goes in the report. A found row keeps Status, Waiting on, Next action and later decisions, but a repeat pitch gets STEP 3's repeat-pitch handling in full, so it lands on Akshay's list.
3. Actions REPAIR: a stamped row whose "link:" line comes after its last "actions: done" is worked again, for unperformed effects only. It first reads both inboxes, the Engagement's newest Activities, Sent and Action keys; never resends, never undoes a newer Your call, Status or decision. Its new "actions: done" ends the repair, so it can't loop.

Unchanged from r8d: old ad@-only allmail rows re-key to adid: with no RAW; a RAW failure pends and the run goes on.

The 13 rows (Zoya's own owner mail is excluded by the existing rule): Dhiraj call move; Team Nxt x6 (cold ask, Akshay's sponsored pitch, phone number exchange, WhatsApp ask); Steakhouse thanks (Adrian); Elsol pricing (Ishita); Fully Vested 17 Nov hold (Ava); Nexla thanks (Saket); Richard Bagshaw (Mike Cagney slot); Gemini notes to Sarika (internal); Zencastr room naming (internal).
