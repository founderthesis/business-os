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
