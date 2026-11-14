# Zoya r20: decision 467, ask mails to Akshay (4 Nov 18:00)

r20 is built on r19. **Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 08c214a6c2a17cc4571c523c1bd1750396cca4ba`, with `build_one.patch` at f70901f. Built twice, byte-identical, no em dashes.

| File | Bytes / sha256 |
|---|---|
| `zoya-one.txt` (hourly) | 56,857 / c109b6c25c81fbc3 |
| `zoya-slow.txt` (Zoya SLOW task) | 13,713 / ffe16d3ac6fc8ee5 |
| `zoya-slow-work.txt` (pinned SLOW file) | 83,046 / e572c950df047484 (83,042 characters), at 08c214a |
| `zoya-episodes.txt` (not live) | 46,635 / 89a1b1ef09aa3ad6 |

## Which routine sent today's clash mail

The **hourly Zoya run at 17:38 JST** sent it: run record "Run zoya 2026-11-04 17:38 JST: Completed", session cse_019pwcV4ZV1nLWpSRTyviUET.
- **Where it came from:** Zoya's Sent Mail:893, "Calendar clash: Ramakant (Scalar Field) 5 Nov", 17:43 JST, To ad@ only. That's checked read-only in her Sent folder and Activities.
- **No rule asked for it.** No live or proposed prompt text tells any routine to mail Akshay an ask. INVITES says a clash goes on "Akshay's list". The run improvised the mail, so 467 now makes it a defined path.

## Changes

1. **ASK MAILS** (shared SENDING, so FAST and SLOW).
   - **Which asks:** an ask on Akshay's list about a call or recording within 48 hours: a clash, a slot only he can pick, a reschedule or no-show decision. It also goes to him by mail from Zoya's inbox, once per ask.
   - **The mail:** To ad@thepodium.in alone, with no Cc. Subject "<what>: <guest> (<D Mon>)", the facts, one recommendation, the Engagement's Notion link on its own line, and "reply here with ok, not ok or your call".
   - **The log:** "Zoya sent: ask to Akshay: <what>", with the row linked and an Action key.
   - **Every other ask** stays on his list only.
   - **The recipient check:** PRE-SEND 2/ now allows ad@ in To only for an ask mail.
2. **ASK REPLIES** (FAST STEP 1 a0, every run).
   - **What counts:** a mail from ad@ in Zoya's inbox whose In-Reply-To is an ask mail's Message-ID.
   - **What happens:** its new text, above the quote, is copied word for word into that row's Your call, tagged "(Akshay, mail reply <D Mon HH:MM JST>)", once. It's logged, and nothing is sent back.
   - **The inbox actions routine** then handles it as any Your call: it acts, copies it to the Claude note, clears it, removes his ask and takes him off Waiting on.
3. **HARD RULES** (shared). Akshay's ad@ replies were feedback only on wording and client-show scheduling. Now his reply to one of Zoya's own ask mails, matched by In-Reply-To, also counts, and it goes only into that row's Your call. Everything else stays as it was.

**Status:** built, not replayed. For Cleanup. Nothing is deployed, and the pin ref hasn't moved.
