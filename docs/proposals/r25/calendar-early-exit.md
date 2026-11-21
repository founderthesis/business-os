# Calendar sync quits early: diagnosis and proposal (r25, nothing built)

Main, 9 Nov 23:50 JST, for the CTO's 23:35 ask. Read-only.

## What I could and couldn't see

This session has **no tool that reads a routine run's events**. Claude_Code_Remote has get_session but no list_events, and the Notion session tools cover Notion agents only. So I haven't read the 22:36 run's own steps. What I did read is the trigger and the session record of last_run (cse_019pwcV4ahw9Ym4E1aH5eukm):

| Measure | 22:36 JST run |
|---|---|
| Prompt | 62,916 bytes, sha c613af00 (r24, as deployed) |
| Model | claude-sonnet-5-5, auto permission mode |
| Duration | 55 seconds (13:36:48 to 13:37:43 UTC) |
| Output tokens, whole run | **3,196** |
| Context used at the end | **165,204 tokens** (window 1,000,000; no compaction) |
| Cache read / write | 924,456 / 133,313 |
| Cost | USD 0.66 |
| Connectors | Gmail, Google Calendar, Notion, MCP Emails, Google Drive |

The CTO saw the 16:35 run (the r22 prompt) do the same, so this predates r24.

## Diagnosis

1. **It isn't the prompt's size limit.** 62,916 bytes is under the 65,536 cap, the prompt loaded whole (its sha matches), and 165k tokens is a sixth of the window. Nothing truncated or compacted.
2. **It is a short run that chose to stop.** 3,196 output tokens covers maybe 10 to 15 tool calls plus a short report. About 148k tokens of tool results came in over those few calls. That fits STEP 1's list_events (3 days back to 30 ahead, full events with descriptions and attendees), the Engagement and People matching reads, and STEP 3's prep entries. After that the model wrote a report calling itself "a partial run, not the full step list", skipped STEP 4 to 4f and the Calendar rules page, and ended.
3. **Nothing in the prompt makes stopping costly.** The calendar prompt has no run record, no step lines, no TIME rule ("size, context or effort never end a run") and no status in code. Every other big routine got those after the same failure (the sweep and WhatsApp, 7 Nov; Zoya earlier). So quitting after the heavy reads ends as an ordinary report, and the scheduler shows "Succeeded".
4. **Step order makes it worse.** The steps run 1, 1a, 1b, 2, 3, 3b, 4a, 4, 4b, 4f, 4e, 4c, 4d, so all the after-recording work (thank-you, community, transcript, Episode recovery) comes last, behind the heaviest reads. Each early stop drops exactly those steps. The Calendar rules page is read in STEP 1b, and the report says it wasn't, so the run may have stopped even before 1b. Only the run's events can settle that.

Confidence: the numbers make points 2 and 3 likely, not proven. The run's events would show the exact last tool call and any error. If the CTO can open the session in the web UI, the last few events settle it.

## Proposed fix (r25; nothing built until the CTO replies)

1. **STATUS IN CODE, like WhatsApp's.**
   - The report's first line is "Calendar <D Mon HH:MM> JST: <status>".
   - Then one line per step: 1, 1a, 1b, 2, 3, 3b, 4a, 4, 4b, 4f, 4e, 4c, 4d. Each reads "step <name>: done <n> | not due | unfinished (minute 20 at <time> | cap: <what> | tool error: <tool> <error>)".
   - A Bash python step prints the status from those lines: Completed, Partial only for a measured minute limit, a cap or a tool error, else Failed "early exit: <steps>".
   - TIME: size, context, effort or the number of events never end a run.
   - About +900 bytes.
2. **A run record**, as the r25 run-records item proposes: "Run calendar <start> JST: Started", then the status. That lets a check see whether the early exits repeat. About +400 bytes.
3. **Lighter reads, so the size pressure goes away:**
   - STEP 1 reads the calendar in two windows: 3 days back to 7 ahead for everything, and 8 to 30 ahead for STEP 1b's audit and new bookings only.
   - It uses list_events with pageSize 50, and never pulls a full event body twice; a later step re-reads one event with get_event.
   - The Engagement matching uses one SQL query on Email and Other emails for all attendees, not one fetch per event.
4. **Put the after-recording steps first.** Run 4a to 4d before STEP 3's prep-entry pass (or at least before 3b). They're time-bound (a thank-you is due the day after), while prep entries for next week can wait an hour.
5. **Size budget:** the calendar is at 62,916, and 1 and 2 add about 1.3 KB. I'd pay for it with cuts in the long history notes (the decision 373, 209 and 424 quotes and the STEP 1a story), keeping it under 63,000, as with Zoya.

On the CTO's "yes" I build it as r25's first item: patch on the live c613af00, built twice, sizes and hashes, for Cleanup.
