# Zoya r15: the deploy set for decisions 445 to 453 (3 Nov)

**r15 replaces r12d, r13b, r14 and r14b.** It's r14b (decision 450's structure) plus three things:
- the re-replay's fixes N1 to N7, from `../zoya-r14/replay-b.json`;
- decision 452: the quoted chain in html_body;
- decision 453: themes from the prep note.

**Command:** `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin bfbadf9203bccad49b12b0b155d98574e793ba04`, with `build_one.patch` applied at f70901f (it adds the parts slowtask-intro and slowtask-load). Built twice, byte-identical, no em dashes.

| File | Task | Bytes / sha256 |
|---|---|---|
| `zoya-one.txt` | A: hourly Zoya (trig_01UPT8LDrBDL5JQqW91Awgbo), FAST only, Sonnet | 51,601 / 64de3918c2b93eef |
| `zoya-slow.txt` | B: **new** "Zoya SLOW", `CRON_TZ=Asia/Tokyo 8 8,11,17 * * 1-5`, Opus | 11,280 / 087c09ae63e0b436 |
| `zoya-slow-work.txt` | The pinned SLOW file B loads | 75,803 / 9f35df2d95121d5d (75,799 characters), at bfbadf9 |

What each decision does is in `../zoya-r14/handoff.md` (450), `../zoya-r13/handoff.md` (449) and `../zoya-r12/handoff.md` (445 to 448). Below is only what's new since r14b.

## Re-replay fixes (N1 to N7)

- **N1, dated: the pause starts Fri 6 Nov.** SENDING's "never Diwali week" barred release mails too. It now reads "the Diwali pause holds chases only, as SLOW BATCH 3/ says". **The CTO checks this against the Cadences Diwali line.**
- **N2.** A claimed "unfinished (cap)" now counts as no reason unless the python, from this run's sends and today's count, finds a cap actually reached: the per-run cap, or the daily cap less the FAST reserve.
- **N3.** A minute-22 stop writes a "stop: minute 22 at <date -u>" line, and the python checks it's at least 22 minutes after the start.
- **N4.** A RULES LOAD failure before the batch selects is Partial, not Failed.
- **N5.** The diff goes under its own "diff:" line, so a re-run of the check can't read it as outcomes.
- **N6.** The last "defer" wording is gone.
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
- pin bfbadf9203bccad49b12b0b155d98574e793ba04, file sha 9f35df2d;
- B's prompt sha 087c09ae;
- A's prompt sha 64de3918.

The set also includes actions r11b (46,112 / 07832eb6) and capture r12c (46,195 / 44b14c3e).

**Still open for Akshay or the CTO:**
- the FAST reserve number on Cadences;
- the Diwali line on Cadences;
- the Notion edits from the r12d list.

**Who deploys:** decision 450 names this session (Main) as deployer, but that arrived only through the CTO's session. This session asks Akshay directly before any trigger, pin or mailbox write.

**Status:** built. A short replay of the r15 changes is running (`replay.json`). Nothing is deployed, and the pin ref hasn't moved.
