# Notion edits for the CTO to apply (26 Oct)

This session's Notion connector still prompts on writes, so it makes none (CTO, 21:13 JST). The CTO applies each edit below from their own session and confirms it by commit. These edits are part of the frozen release build (coverage-26l.md).

## 1. Inbox and Your call rules: Akshay's yes or no on a recording

- Page: 3ff19a301a7f8148993ccea78fc66428 ("Inbox and Your call rules", Controls).
- Command: `insert_content`, position end.
- Why: decisions 411 and 412. The calendar, the sweep and Zoya now ask Akshay "did the <D Mon> recording with <guest> happen? Write yes or no in Your call". Today the inbox's YOUR CALL reads "yes" as approving the proposal in Next action, and this ask is a question, not a proposal. This section tells the inbox what each answer does.

Content to insert (exact):

```
## 5. Did the recording happen? (decisions 411 and 412, Akshay, 26 Oct)

- This applies when Akshay answers "Akshay: did the <D Mon> recording with <guest> happen? Write yes or no in Your call".
- "yes" (or "happened", "it did"):
  - Set Status Recorded and clear Call type.
  - Take that ask out of Next action, and take Akshay out of Waiting on unless another of his segments stays.
  - Claude note: "YYYY-MM-DD: recorded <D Mon> (Akshay, Your call)". Clear Your call.
  - The calendar's next run drafts the thank-you (STEP 4c for Founder Thesis, 4d for the other shows). Don't draft it here.
- "no" (or "didn't happen", "no-show", "cancelled"):
  - Leave Status alone.
  - Replace the ask with "Akshay: <guest>'s <D Mon> recording: cancelled or no-show?" unless his answer already says which. If it does, follow the existing no-show or cancel rule: no-shows go to Akshay first and Zoya sends the note after he decides (decision 236).
  - Claude note: "YYYY-MM-DD: <D Mon> recording didn't happen (Akshay, Your call)". Clear Your call.
- Never ask the guest, PR or anyone outside the team whether a recording happened. Never put this question on WhatsApp.
```

## 2. Crash window A recovery: log the unlogged send

- Data source: Activities, collection://290f715d-fd45-4203-ade6-3642c2326c6c.
- Command: `create-pages`, one row.
- Why: the frozen build's crash recovery (ACTIONS: "read your Sent and the thread for a message from us after the action was raised"; MESSAGE IDENTITY) finds the 19:20 JST crash A mail in Zoya's Sent. It has no Activity, so recovery logs one and sends nothing. Record: split-dryruns/crash-a-recovery.md.

Properties (exact):
- Summary: `Zoya sent: [split launch test] crash window A (recovered, not resent)`
- Kind: `Email out`
- Source: `Gmail`
- Source ID: `msgid:a21e2f20-99d5-4dce-a3ed-2d5a2c7c7ae4@mcpemails.com`
- Action key: `40519a301a7f8105a87edf64e65872b7:followup:seq-4-1:2026-10-26T00:00:00+09:00` (only if the Action key property exists yet; it is created at deploy, so otherwise put it as the first line of the page body)
- Engagement: 40519a301a7f8105a87edf64e65872b7
- Date: 2026-10-26 19:20 JST (10:20:28Z)
- Page body: `Action key: <as above>`, then the sent plain-text body as read from Zoya's Sent (message [Gmail]/Sent Mail:645).

## Applied by the CTO (26 Oct, about 21:50 JST)

- Edit 1: applied. Section 5 on 3ff19a301a7f8148993ccea78fc66428 replaced with the exact text above. It supersedes the 21:14 version, which carried Main's earlier wording.
- Edit 2: applied. Activity 40519a301a7f81daa9aec3268dac4369 (Email out, Source ID msgid:a21e2f20-99d5-4dce-a3ed-2d5a2c7c7ae4@mcpemails.com, Engagement 40519a301a7f8105a87edf64e65872b7, Date 10:20:28Z). The Action key is the first line of the page body, since the property doesn't exist yet.

## 3. Crash window B recovery: log the unlogged send

- Data source: Activities, collection://290f715d-fd45-4203-ade6-3642c2326c6c.
- Command: `create-pages`, one row. Record: split-dryruns/crash-b-recovery.md.

Properties (exact):
- Summary: `Zoya sent: [split launch test] crash window B (recovered, not resent)`
- Kind: `Email out`
- Source: `Gmail`
- Source ID: `msgid:f3ce2f38-067e-4e3e-99bb-f5e102852671@mcpemails.com`
- Action key: `40519a301a7f8105a87edf64e65872b7:followup:seq-4-2:2026-10-26T00:00:00+09:00` (property if it exists, else the first line of the page body)
- Engagement: 40519a301a7f8105a87edf64e65872b7
- Date: 2026-10-26 23:39 JST (14:39:43Z)
- Page body: `Action key: <as above>`, then the sent plain-text body as read from Zoya's Sent ([Gmail]/Sent Mail:654).
