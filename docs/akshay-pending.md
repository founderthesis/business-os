# Pending on Akshay

When Akshay asks what's pending on him, read this list, check each item is still open, and give him the open ones. Remove an item once it's done.

- FT Community cleanup: upload ft-community-cleanup.md to Notion AI (412 rows updated, 99 created, 33 marked Left). Then tell Claude, so it can check the count is 511.
- "whatsapp to business OS" routine (currently switched off): replace its prompt with whatsapp-routine-v3.txt (replaces v2), set the model to Sonnet, remove every connector except bluetick and Notion, set the schedule to "45 0,7,13 * * *" (UTC, which is 09:45, 16:45, 22:45 JST), then switch it on.
- "Calendar sync" routine: add the Google Drive connector (it needs Drive for recording checks, transcripts and precall notes).
- Mac transcript task (Claude desktop, Scheduled tasks): replace its prompt with mac-transcripts-v2.txt so it also saves each transcript to Drive.
- Zencastr: reply on whether they can back up transcripts to Drive. If yes, the Mac transcript task can go.
- "FT Newsjack, daily archive scan" routine: switch the model to Sonnet (Claude can't edit it).
- Blueticks support: report that get_participants ignores skip and cursor and stops at 100 members (draft text given 14 Oct).
- Inbox items left with Akshay on 13 Oct: FieldAssist contract revision; Sanjiv Bajaj call follow-up.
