# Gmail quota incident, 28 Oct: tally and hotfix

**What happened.** From the 12:03 JST inbox run on 28 Oct, the Gmail connector has returned "Resource has been exhausted (e.g. check quota)" for ad@thepodium.in. While it lasts, no ad@ mail is logged and nothing reaches Akshay's list.

## 1. Gmail calls per routine per run

**Method.** This builder session has no tool to read other sessions' events, so the transcripts couldn't be read. The tally is worked out from each live prompt's read rules, plus one read-only count of the mailbox through MCP Emails (IMAP), with no Gmail calls. The CTO can confirm the numbers against list_events on the last day's run sessions.

**Mailbox size.** ad@thepodium.in had 145 inbox messages from 27 Oct 00:00 to 28 Oct 12:40 JST, before counting sent mail.

| Routine | Runs a day | Gmail reads per run, from the prompt | A day, roughly |
|---|---|---|---|
| **Inbox** | 17 (hourly :02) | STEP 1: one search from one day before the newest Gmail Activity, then `get_thread` on **every** thread in it (about 80 to 100 threads with this mailbox's volume). STEP 2: one RAW `get_message` per message not yet logged. Plus CONTEXT CHECK reads before sends, and Your call rows. | **1,500 to 1,800**, almost all re-reads of the same threads |
| Daily sweep | 2 (13:10, 15:10, weekdays) | STEP 3: Gmail reads "row by row" for every flagged FT row and stale client-show row, up to 60 a run, each a search plus a thread read. STEP 2 and 4 likewise per row. 6c: one billing search. | 100 to 250 |
| Zoya | 17 (hourly :38) | `get_thread` on ad@ for loop-in threads (STEP 1), `rfc822msgid` searches for Message-IDs, and ad@ full threads when needed. MCP Emails does the rest. | 50 to 150 |
| Calendar | 6 | 3b stakeholder thread reads, CANCELLED IN WRITING checks, 4a precall notes search: a handful a run | 20 to 60 |
| Evals | 1 | One `get_thread` per eval (at most 18) | up to 18 |
| Dossiers | 1 | One pitch thread per dossier (at most 3) | up to 3 |
| WhatsApp | 17 | Only when a team member's "@zoya" question needs mail (0d) | about 0 to 5 |
| Host boards | 4 | none | 0 |

**Cause confirmed:** the inbox's STEP 1 re-reads the whole last day every hour, about 1,600 thread reads a day. That's about 80% of the account's Gmail reads.
- The sweep's per-row Gmail reads are the next biggest, and they land at 13:10, right after the 13:02 inbox run. A one-off burst of the CTO's own reads at 13:10 added to that.
- This tally can't show whether the throttle is per-minute (bursts) or per-day. The 12:03 failure, after a night of hourly full re-reads, points to a daily or rolling budget.

## 2. Inbox hotfix (`inbox_hotfix.py`)

**Input and output.**
- Input: the live inbox prompt, 61,957 B / aed0215a8bdf6a26.
- Output (round 2): **64,417 B / 4f85894fcfea6b25**, built twice, byte-identical, 919 B under the build's limit (the cap less 200).
- To make room, seven provenance notes lose their history. Every decision number and rule stays. For example, "(decision 325, Akshay, 18 Oct: \"My queue is a decision inbox...\")" becomes "(decision 325)", and two Codex incident explanations go.

**a. Window.**
- Every run that finishes its Gmail read writes "read to <ISO time of the newest message read>" in its run record, whatever its status.
- The start time T is 30 minutes before the newest such line, and never more than 3 days ago. A run whose read didn't finish has no line, so its span is read again.
- Anchoring on Completed runs only would have let a run of Partial runs (Calendar missing, say) widen the window every hour. The replays found this.
- With no record yet, T is one day before the newest Gmail Activity. That reproduces today's start point once only, and b keeps even that run cheap.
- It doesn't anchor on the newest Gmail Activity alone. Zoya and the sweep log Gmail Activities too, so that anchor could pass over unread mail.
- Gmail's `after:` takes a date only (the tool's own docs: midnight of the day). Epoch seconds aren't documented, which fits the CTO's `{}` result. So the search stays `after:<date>` and the narrowing happens after the search.

**b. Metadata-only read first.**
- `search_threads` with `view THREAD_VIEW_SUMMARY` returns each thread's latest message and message count, one call per page of 50.
- A thread is kept only if its latest message is at or after T and no Activity holds it (an Activity whose Link has the thread id and whose Date is at or after that message's date).
- Only those get `get_thread`, as `PLAIN_TEXT`. `FULL_CONTENT` is used only where a step needs the HTML, such as Gemini notes.
- The expected cost is a few `get_thread` calls an hour, not about 100.

**c. Quota**, for every Gmail call in the run, Your call reads included. "exhausted", quota or 429:
1. Retry once, after the next step that needs no Gmail. There's no sleep: Claude Code's Bash refuses a standalone `sleep`, as the replay confirmed. An error a retry clears isn't a failure.
2. Fails again: no more Gmail calls this run. Read ad@ through MCP Emails (inbox_id cd37e47e-89d8-4259-b907-9a243baf7048): search since T's date in INBOX and sent, `read` each new message, and `original` for its Message-ID. Log messages as STEP 2 does, with Link empty. Every Gmail action (sends, drafts, RSVP archiving) is left to the next run. The run ends Partial.
3. MCP Emails also fails: the run ends Failed, naming both errors.

MCP Emails reads ad@ over **IMAP** (its search answered `SINCE 27-Oct-2026` on `INBOX:48820`), not through the Gmail API. So it doesn't share the throttled quota.

**d. Run record.** The inbox's run record (decision 419) is in this hotfix, because the window anchors on it. It's the same block as R-runrec. R-runrec's inbox patch is replaced by this one, and R-runrec rebases on this output.

## 3. Zoya: MCP Emails first for ad@ reads

**Change.** Three VARIANT entries in `routines/zoya/build_one.py` touch the FAST prompt only. The SLOW work file stays pinned at e20647b and still hashes to dedea9f8eb7af561.
- **TOOLS:** read ad@ threads with MCP Emails first. Gmail `get_thread` only when MCP Emails can't give the thread. A Gmail quota, "exhausted" or 429 error means no more Gmail calls this run.
- **MESSAGE IDENTITY:** the Message-ID from MCP Emails `original` first, and Gmail `rfc822msgid` only if that fails.
- **STEP 1:** loop-in threads on ad@ are read with MCP Emails, Gmail only if it can't.

**Sizes.** zoya-one goes from 40,975 B / 56953088cc0ddf82 to **41,285 B / 7ac090bdc4b1d4cd**. Built twice, identical, with the version stamp recomputed.

## For Akshay (via the CTO): a CLAUDE.md rule changes

CLAUDE.md, "Sending mail" paragraph: **"Reading Gmail stays on the Gmail connector."**
- Both hotfixes read ad@thepodium.in through MCP Emails: always first in Zoya, and as the quota fallback in the inbox.
- Proposed wording: "Reading ad@thepodium.in: MCP Emails (IMAP) first, Gmail connector when MCP Emails can't, and never in bulk (decision <n>, 28 Oct Gmail quota incident)."
- Sending is unchanged. Akshay's automated mail still goes through the Gmail connector, because a send through MCP Emails would file a second Sent copy.

## Not in this hotfix

**Sweep STEP 3's per-row Gmail reads** are the second-largest load: up to 60 rows a run, each a search and a thread read. A follow-up should make them MCP Emails first too, or read only rows whose thread changed since the row's Last activity. The sweep's prompt is unchanged here.

## Tests

The scenarios are in scenarios.md (H1 to H8). Results are in replayA.json and replayB.json: offline, two independent runs, no MCP calls.
