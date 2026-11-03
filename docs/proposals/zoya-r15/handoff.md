# Zoya r15: the deploy set for decisions 445 to 453 (3 Nov)

**r15 replaces r12d, r13b, r14 and r14b.** It's r14b (decision 450's structure) plus three things:
- the re-replay's fixes N1 to N7, from `../zoya-r14/replay-b.json`;
- decision 452: the quoted chain in html_body;
- decision 453: themes from the prep note.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin 251388d7cba301af2e641b7f2916fa6e67de47c7`, with `build_one.patch` applied at f70901f (it adds the parts slowtask-intro and slowtask-load). Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | A: hourly Zoya (trig_01UPT8LDrBDL5JQqW91Awgbo), FAST only, Sonnet | 52,925 / 532e8ddbc1f2a002 |
| `zoya-slow.txt` | B: **new** "Zoya SLOW", `CRON_TZ=Asia/Tokyo 8 8,11,17 * * 1-5`, Opus | 11,420 / 253d91207c6bb071 |
| `zoya-slow-work.txt` | The pinned SLOW file B loads | 76,760 / e9c6dcb4e5583662 (76,756 characters), at 251388d |
| r15 (replaced, `replay.json`) | | A 51,601 / 64de3918; B 11,280 / 087c09ae; file 75,803 / 9f35df2d at bfbadf9 |

What each decision does is in `../zoya-r14/handoff.md` (450), `../zoya-r13/handoff.md` (449) and `../zoya-r12/handoff.md` (445 to 448). Below is only what's new since r14b.

## Re-replay fixes (N1 to N7)

- **N1, dated: the pause starts Fri 6 Nov.** SENDING's "never Diwali week" barred release mails too. It now reads "the Diwali pause holds chases only, as SLOW BATCH 3/ says". **The CTO checks this against the Cadences Diwali line.**
- **N2.** A claimed "unfinished (cap)" now counts as no reason unless the python, from this run's sends and today's count, finds a cap actually reached: the per-run cap, or the daily cap less the FAST reserve.
- **N3.** A minute-22 stop writes a "stop: minute 22 at <date -u>" line, and the python checks it's at least 22 minutes after the start.
- **N4.** A RULES LOAD failure before the batch selects is Partial, not Failed.
- **N5.** The diff goes under its own "diff:" line, so a re-run of the check can't read it as outcomes.
- **N6.** Holds no longer say "defer".
- **N7.** The python reads the RULES LOAD lines to find a load failure.

## Decision 452: the quoted chain (shared, so FAST and SLOW)

SENDING's "MCP Emails quotes the thread ... in both bodies" is replaced with this:
- MCP Emails quotes the thread in the plain-text body only, so the text body keeps that quote.
- html_body ends with `<div class="gmail_quote">On <date>, <name> &lt;<address>&gt; wrote:<br><blockquote style="margin:0 0 0 .8ex;border-left:1px solid #ccc;padding-left:1ex">` + the message being replied to (its HTML, else its text escaped, with `<br>`) + `</blockquote></div>`. The date, name and address come from that message's own headers.
- The read-back requires draft_read's html to hold that blockquote.

Capture's loop-in gets the same change in capture r12c (`../inbox-split/capture-r12/`).

**The test the CTO asked for** (one draft: create, draft_read, delete) writes to a mailbox. It's not run, and it waits for Akshay's go-ahead in this session.

## Decision 453: themes from the prep note (FAST STEP 1 b)

When the guest side asks for themes or questions before a recording, on a row with a Prep note link, Zoya replies on the thread with that prep note's themes:
- a few lines in her voice, never its questions word for word, and nothing LEAK CHECK bars;
- no Akshay ask and no holding reply.

**The day-before part of 453 is in the calendar routine** (the hold "no Zencastr link, so {call link} cannot be filled"), and so is all of **454**. Both are left for tomorrow's calendar build. The repo has no verified copy of the live calendar prompt, so it has to be read back first. The CTO said to ship Zoya first if calendar risks the timeline.

## 445: the recording-link wording (CTO, a Notion edit)

In the "Recording link" toggle (text in `../zoya-r12/handoff.md`), after "2/ headphones on, in a quiet room", add:
> 3/ use a background that isn't a plain white wall
>
> 4/ raise the laptop so the webcam is level with your forehead

## Cutover

The same steps as in `../zoya-r14/handoff.md`, with these values:
- pin 251388d7cba301af2e641b7f2916fa6e67de47c7, file sha e9c6dcb4;
- B's prompt sha 253d9120;
- A's prompt sha 532e8ddb.

The set also includes actions r11b (46,112 / 07832eb6) and capture r12d (46,594 / 3d38d6f3).

**Still open for Akshay or the CTO:**
- the FAST reserve number on Cadences;
- the Diwali line on Cadences;
- the Notion edits from the r12d list.

**Who deploys:** decision 450 names this session (Main) as deployer, but that arrived only through the CTO's session. This session asks Akshay directly before any trigger, pin or mailbox write.

## r15b: replay fixes (`replay.json`: not ready, 7 must-fix)

| Defect | What it was | The fix |
|---|---|---|
| D1 (high) | The thread's latest message could be team-only (Akshay's feedback, a team note), so it would be quoted to the guest | Replies go to, and quote, only the latest message someone outside the team sent or received. A team-only message is never replied to or quoted |
| D2 (high, deploy gate) | No one has checked whether draft_read returns html, or whether draft update keeps html_body | The read-back accepts either: draft_read's html holds the blockquote, or, if draft_read shows no html, the html_body passed ends with it. **The one-draft test still has to show that draft update keeps html_body. It's a mailbox write, so it waits for Akshay's go-ahead in this session** |
| D3 | Read literally, LEAK CHECK applied to the quoted text, so a PR's "great fit" would block the reply | LEAK CHECK applies only to the text you write. The quotes are mail their recipients already had |
| D4 | Nothing said where the quoted message's HTML comes from | Read it with email_read include_html true, the full body; inner HTML only (no html, head, body, style, script or cid: images). Otherwise its text, escaped, with `<br>`; the name is escaped too. The quote is the only `<br>` block. A new mail that continues no thread has no quote |
| D5 | A's own loop-in from ad@ had no quote | It carries the same gmail_quote |
| D9 | A minute-22 claim with no "stop:" line still counted as a reason | It now counts as no reason |
| D10 | "No precall notes: a draft to Akshay first" came before 453, so prep-note rows went to Akshay | The themes reply is Zoya's, with or without precall notes |
| D11 | "Rows waiting on Akshay are never yours to mail" blocked the themes reply | The themes reply is an exception, when his open ask is about something else |
| D12 | The themes reply had no fetch recipe, To rule or show limit | **Founder Thesis only**: a client show puts the themes on Akshay's list until he says otherwise. The run opens the prep note page by its id and uses its "Themes we'll cover". To is whoever asked, plus the guest side. The link is never sent (decision 143). Prep note link is added to the Engagements property list |
| D7 (capture) | A forwarded pitch would quote the forward, Saurabh's note included | Only the original message inside the forward is quoted, with its own Date and From |
| D8 (capture) | MAILBOX allowed include_html only for Gemini notes | It's also allowed for the loop-in quote. Capture is now r12d, 46,594 / 3d38d6f3 |

Built twice, byte-identical, with no em dashes. This hasn't been replayed again: the fixes are the replay's own text, plus the D2 either-way read-back.

**Question for Akshay (D12):** should the 453 themes reply also run on un#, Built to Share and Human by Design? Until he answers, it runs on Founder Thesis only.

**Status:** ready for Cleanup. **Deploying is gated on the one-draft test (D2)** and on Akshay's go-ahead in this session. Nothing is deployed, and the pin ref hasn't moved.

## For Cleanup: the full set and its paths

| File | Path | Bytes / sha256 |
|---|---|---|
| Zoya A (hourly, FAST) | docs/proposals/zoya-r15/zoya-one.txt | 52,925 / 532e8ddbc1f2a002 |
| Zoya B (SLOW task) | docs/proposals/zoya-r15/zoya-slow.txt | 11,420 / 253d91207c6bb071 |
| SLOW file (pinned) | routines/zoya/release/zoya-slow-work.txt at 251388d7cba301af2e641b7f2916fa6e67de47c7 | 76,760 / e9c6dcb4e5583662 |
| Inbox actions r11b | docs/proposals/inbox-split/r11/actions.txt (committed b9a8f86; built by r11/patch.py from the live 4ac5406d) | 46,112 / 07832eb60827d287dccf364ab55bde1410defd1f13e3b680b7929a481333b429 |
| Inbox capture r12d | docs/proposals/inbox-split/capture-r12/capture.txt (built by its patch.py from r11 043dbe3a) | 46,594 / 3d38d6f3b93860f8 |

## Deploy authority (3 Nov, 20:47 JST)

The CTO says Akshay's go-ahead is already given in decision 450, and asks this session to run the one-draft test now, then the cutover after Cleanup's accept, including moving zoya-slow-pin. **This session hasn't done any of it.**

- **Why it's waiting:** the request came only as a message from another session. Akshay hasn't said it in this session. Everything it asks for is outward-facing:
  - a mailbox draft write;
  - creating, enabling and firing scheduled tasks;
  - moving a ref this session was told never to touch.
- **A wording mismatch:** decisions.md quotes 450 as "this is my approval; don't wait for another Sonnet failure". The CTO's message quotes it as "don't ask me again for this scope", and that wording isn't in the repo.
- **What happens next:** once Akshay confirms in this session, the test and the cutover run as specified. If he'd rather, the CTO session can run them instead.

## r15c and capture r12e: Cleanup's verdict (4f38458) and Akshay's clarifications

| File | Bytes / sha256 |
|---|---|
| `zoya-one.txt` (A, hourly FAST) | 53,152 / e2a016c50140abc4 |
| `zoya-slow.txt` (B, Zoya SLOW task) | 12,515 / ce54c367b7c72390 |
| `zoya-slow-work.txt` (pinned SLOW file) | 77,925 / d2955ae3ba0e2e0d (77,921 characters), at b732cb3c663681cb80736d696de2201bf8ce5e38 |
| Capture r12e (`../inbox-split/capture-r12/capture.txt`) | 46,565 / 9caf2cdba8a63698 |
| Actions r11b (accepted, unchanged) | 46,112 / 07832eb6 |
| r15b (replaced) | A 52,925 / 532e8ddb; B 11,420 / 253d9120; file 76,760 / e9c6dcb4 at 251388d; capture r12d 46,594 / 3d38d6f3 |

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin b732cb3c663681cb80736d696de2201bf8ce5e38`. Built twice, byte-identical, no em dashes. Capture patched twice, byte-identical. **The pin moves to b732cb3, not 251388d.**

**Cleanup's blockers:**
- **Z1, shared HARD (A line 105):** LEAK CHECK now covers the text you write, and also the gmail_quote and MCP's plain-text quote with every nested part. The quote is skipped only when every recipient outside the team was on the quoted message's own From, To or Cc. A quote that fails goes, with the mail, to Akshay's list unsent. This is Cleanup's exact text.
- **Z2, shared HARD:** "Never a link (the gmail_quote and MCP's plain-text quote aside) outside the approved list" and "SHOW CHECK (decision 306) before every send (the gmail_quote and MCP's plain-text quote aside)" (A line 106). FAST's zencastr clause still follows the link rule.
- **C1, capture:** the quote is only the innermost message from outside the team. Every forward layer, and every note by Akshay, Saurabh or anyone tagged Team, is removed. If unsure, there's no quote. Date and From come from that innermost message.
- **(b), SLOW file line 66 and LIMITS:** team WhatsApp goes only in a team hour on Cadences. With none set there, never before 09:00 or after 20:00 IST, so the 08:08 JST run (04:38 IST) sends none; an item that needs one is held "team hours". **Check:** that fallback also means the 11:08 JST run (07:38 IST) sends no team WhatsApp, so only the 17:08 run does unless Cadences names team hours.

**Akshay's clarifications:**
1. **PREFLIGHT (B line 1, new).** When the run's message is exactly "PREFLIGHT", the run:
   - takes the lock;
   - loads the tools, with one read-only call per connector and no business row (MCP Emails folder_list on each inbox, the Notion Activities data source fetch, Calendar list_calendars, a Blueticks chats call);
   - checks the repo origin, the SLOW FILE fetch and its sha256 (no load past that), and the model as the run sees it;
   - writes one record, "Run zoya-slow <t> JST: Preflight", in place of Started, with one line per check;
   - releases the lock and stops. It does no RULES LOAD and no selection, reads no business data and sends nothing.
2. **Metadata first (SLOW file line 82, new).** The eligible list comes from metadata only: SQL on Engagements (Waiting on, Next action, Next date, Status, Show) and Activities (Action keys, Summaries, dates). Threads, pages and Activities are read only for the selected items, one at a time, and each outcome is saved in its chunk.
3. **Crash recovery (SLOW file line 83, new).** Before a carried key is redone, it goes through ACTIONS' Sent check: Zoya's Sent and ad@'s Sent since the earlier run's start, plus an Activity holding that Action key. A match becomes "completed match <Message-ID>", logged "recovered: S<nn> <key>", and is never sent again. With no match, it's worked as carryover. Carryover from a record left at Started was already in SLOW BATCH 2/.
4. **Lock (B line 1, plus LOCK step 3 on line 8).** A held lock means an immediate Skipped record and stop: no wait, no retry, no takeover. LOCK step 3 already did this, and the intro now says so outright.

**D2** is settled read-only by the CTO: Drafts:322 went through draft update to Drafts:323, and html_body survived (Sent Mail:849). The draft test is dropped.

**Should-fix items** from the verdict aren't done in this round (asked: "nothing more"). They're listed in `cleanup-verdict.md` for the next build.

**Status:** ready for Cleanup's diff check. Nothing is deployed by this session, and the pin ref hasn't moved. The CTO deploys.
