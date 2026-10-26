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
