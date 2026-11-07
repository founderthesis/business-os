# Cleanup verdict: Zoya r20 (decision 467, ask mails)

Cleanup session, 4 Nov 2026, about 21:20 JST. Read-only. Nothing deployed.

## Verdict: not accepted yet. One blocker (C1); r19 can repin on its own

Reproduced twice, byte-identical, each equal to the proposal copy. I applied docs/proposals/zoya-r20/build_one.patch alone, on a clean worktree at f70901f6. It has to be clean: applying it over the r19 tree fails on four "already exists" files. Then I ran build_one.py refs/heads/zoya-slow-pin 08c214a6c2a17cc4571c523c1bd1750396cca4ba. No em dashes.

| File | Bytes | sha256 (first 16) |
|---|---|---|
| zoya-one.txt (hourly) | 56,857 | c109b6c25c81fbc3 |
| zoya-slow.txt (SLOW task) | 13,713 | ffe16d3ac6fc8ee5 |
| zoya-slow-work.txt (pin 08c214a) | 83,046 (83,042 characters) | e572c950df047484 |
| zoya-episodes.txt (not live, not reviewed) | 46,635 | 89a1b1ef09aa3ad6 |

Diff against r19 has only the three handoff changes:
- ASK MAILS in shared SENDING.
- STEP 1 a0 ASK REPLIES in the hourly only.
- The PRE-SEND 2/ exception and the widened HARD rule, in all three.
The SLOW task's pin sha, hash prefix and total match the file. Decision 467 matches the text.

## C1 (blocker): "ok" must approve exactly what the row will act on

Akshay answers "ok" to the recommendation in the mail. The inbox actions routine then acts on Your call against the row's current Next action. Two gaps:
- The mail's "one recommendation" is Zoya's own wording, so it can differ from the row's "Recommend:" text.
- By the time he replies, the ask may be gone (settled, superseded, rescheduled). His "ok" then lands on whatever the row asks now.

Either way, an "ok" can approve something he never read. On a clash or a reschedule that can mean a calendar change with guests. Fix, two sentences:
- ASK MAILS: the mail's recommendation is the Akshay segment's "Recommend:" text word for word. The segment has none: no recommendation, and the mail asks for his call.
- ASK REPLIES: copy only while the ask segment the mail was sent for is still on the row (match its key or its first 20 characters). Gone: copy nothing, log the reply, and add one report line "reply to <ask> arrived after it was settled".

## Should-fix (not blocking)

- S1. Make the ask key stable. "<raised ISO>" isn't defined for an Akshay ask: ACTIONS defines it only for msg, call and seq origins. A run that fills in "now" makes a new key every hour, and only the Sent check stands between that and a second mail. Define it as the segment's own date stamp ("(4 Nov)") at T00:00:00+09:00. Also dedupe on a "Zoya sent: ask to Akshay" Activity on that row with the same first 20 characters.
- S2. Prove the reply is really his. The In-Reply-To match is already hard to fake, because the Message-ID went only to ad@. Still, add one cheap check: the reply's Message-ID found in ad@'s Sent by MCP Emails `query HEADER Message-ID "<id>"` (the form that works on that inbox). No match: copy nothing, and add a report line.
- S3. Ask mails go only to Akshay. LEAK CHECK and SHOW CHECK exist to protect outsiders, and as written they can block an ask mail that names a tier or a show fact, so it's silently never mailed. Exempt ask mails from both, or say in the report that it was blocked.
- S4. A second reply that answers his own earlier reply has In-Reply-To set to that reply, not the ask, so it's ignored. That's fine, and conservative. Add one report line when a mail from ad@ on an ask thread isn't copied, so a changed mind isn't lost.
- S5. When Your call already holds his Notion text, the " | " join hands the inbox actions routine two instructions. Say that the newest tagged entry wins.

## Note on the clash mail trace

The handoff traces today's clash mail to the 17:38 hourly run (Sent Mail:893), which improvised it with no rule asking for it. That fits the r18 hourly text as I reviewed it. I didn't re-read the mail.
