# Pinned inbox routine (repo-backed), 29 Oct

Routine: "Inbox to Business OS (pinned)", trig_01V3hmg4syAUh3LJ8LbH11YB. **Disabled.** It has never fired.
Old routine: "Inbox to Business OS", trig_0189eZvAD8x4357cfevgZ3No, still live on 61,957 bytes / sha256 aed0215a8bdf6a26.

## 1. The safety rejection

What the record shows: on 28 Oct the deploy subagent's update_trigger call (the full 65,333-byte prompt as the argument) came back "Interrupted: the response that made this tool call was stopped by a safety classifier". A read-back right after showed the live prompt unchanged at 61,957 / aed0215a8bdf6a26.

What it doesn't show: a reason. The classifier names no rule, line or category. So we can't say which part of the content, if any, caused it. Finding out by trial would mean probing the classifier, which we won't do.

Codex's point stands: loading the same text from the repo would get it into a running routine without passing the check that stopped it. That's why the pinned routine stays disabled until this is settled through a supported route:

- **Recommended:** Akshay applies the accepted file himself in the claude.ai routine editor, to the existing routine. A person editing their own routine is the product's supported path, and the classifier only acts on model output. This keeps the old routine's id, connectors, model and history, so items 2 and 3 below aren't needed for this release. Detach Gmail from it at the same time (Cleanup verdict).
- If he'd rather not paste: report the interruption to Anthropic support and ask what triggered it, then fix that in the text before any deploy.

The pinned routine is kept for when it's genuinely needed: a prompt that outgrows the 65,536-byte stored-prompt cap. The accepted file is 65,333 bytes, 203 under it. Repo loading lifts only that cap. Model context, token cost and run limits are the same either way.

## 2. Pin (done)

The bootstrap prompt names the commit (full 40-character SHA), the path, the exact byte count and the full 64-character sha256:

- commit 01918284759cda0dcb13ff4f50074e873434136c
- docs/proposals/d420/inbox-deploy.txt
- 65333 bytes
- sha256 d1bba5802ca8872d2dcefe4c6f3942c9bfca0ee004ad3687e5e95bbd2c095190

It reads by commit, never a branch tip. Any failed fetch or check stops the run before any mail read, Notion write or send.

Model: claude-sonnet-5-5, matching the old routine. Schedule: CRON_TZ=Asia/Tokyo 2 7-23 * * *, the same as the old one. Repo and connectors can only be attached in the claude.ai UI: business-os, plus MCPEmail, Notion, Google-Calendar and bluetick. Not Gmail. Check them after attaching.

## 3. Cutover (only after item 1 is settled)

State carries over because it lives in Notion, not in the routine:

- Cursor: the new instructions take T from the newest inbox run record's "read to". The old prompt writes no such record. So the first new run finds none and reads the last 3 days.
- Pending: there is no pending list yet. The old prompt has none, and pending lines start with the new run records.
- Dedup: Activities already hold every logged mail's Source ID. The new instructions match by Message-ID and by every older id spelling before creating a row.

Steps:
1. Disable the old routine (enabled=false). Don't delete it; keep it for rollback.
2. Confirm its last run has finished: last_run has finished_at, and its session is idle.
3. Enable the pinned routine, or fire it once by hand.
4. Verify the first run:
   - instructions loaded and the sha256 matched;
   - a run record with "read to";
   - the 3-day catch-up read in full (every page);
   - no duplicate Activity for any mail the old routine already logged;
   - no Gmail calls;
   - sends only the loop-ins.
5. Rollback: disable the pinned routine and re-enable the old one.

## 4. Changing the pinned release

A new release goes through the existing review: Main builds the file, Cleanup accepts it and records its byte count and sha256 in its verdict, Codex sees the delta.

Then the CTO commits the file and changes the bootstrap prompt's four values together, in one update_trigger call: commit, path, bytes and sha256, all taken from Cleanup's verdict. The CTO reads the stored prompt back. Then the next run is observed.

Moving or force-pushing the branch changes nothing. The routine reads only the named commit and checks it against the named hash, so a different file fails closed. Only an edit to the stored prompt can change what runs, and that edit is the reviewed step.
