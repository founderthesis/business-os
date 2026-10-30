# B2S sheet to Notion daily sync (retired)

Scheduled task trig_01Hx7sC6XQXrLU8SAR2oVR98, paused since 9 Oct; B2S now lives on Engagements, fed by Salesblink sync. Deleted 16 Oct 2026 in the OS Audit clean-up. Prompt kept for history.

## Prompt

```text
Sync the Built to Share guest sheet into the Built-2-Share Notion database. One way: the Google Sheet feeds Notion. Run the whole thing, then report.

SOURCE, a Google Sheet called "B2S Guest list":
  fileId 1BmSDU1O2xOpEbrSNhuL6Fro1fwQzp0sEF95iN8hiVhA
  It is owned by a colleague and edited most days.

TARGET, a Notion database called "Built-2-Share guest list":
  database https://app.notion.com/p/60f9ca945eb5406aabd1e958cd528ded
  data source collection://40650bc2-077a-48c3-beee-e62c506c55bf
  Default view for bulk reads: view://88204eb0-850c-412d-9a9d-b76736269f11
  Properties: "Founder @ Company" (title, often a markdown link to LinkedIn), "Email", "Country", "Category", "Connect", "Status", "Next Follow-up" (date), "Rank" (formula, read-only).
  Status options: Not started, Emailed / Started, Chasing, Maybe later, Booked, Unresponsive, Declined, Do not contact.

STEP 1. Download the sheet.
Call mcp__Google_Drive__download_file_content with that fileId and exportMimeType "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet". Write the returned base64 to a file with the Write tool, then decode it to an .xlsx with a short python script (base64.b64decode). Do not paste base64 into a shell command.

STEP 2. Extract the sheet's state with python and openpyxl.
Tabs and their name columns:
  "India" -> "Founder / Company"
  "Global known in India" -> "Founder / CEO"
  "NEW" -> "Column 1"
  "N2" -> "Name" plus "Company"
  "N3 (6)" -> "Founder @ Company"
  "Global p3" -> "Founder / Company" plus "Company"
Cells may hold =HYPERLINK("url","Visible Text") formulas: take the visible text. Dates come back as datetimes; format them YYYY-MM-DD.
For each person build: a match key = lowercase of (person name + company) with every non-alphanumeric character stripped; the readable label; the Status cell; and the next follow-up date, which is the earliest date in that row's "Initial Mail" / "Follow Up N" / "Follow up N" columns that is today or later, falling back to the latest past date if none are in the future.
Map sheet statuses onto Notion's: declined -> Declined, unresponsive -> Unresponsive, chasing -> Chasing, maybe later and check later -> Maybe later, started and emailed -> Emailed / Started, booked -> Booked, do not contact -> Do not contact. An unrecognised or blank status means "no status information".
If the mapped status is Unresponsive, Declined or Do not contact, force the follow-up date to empty. That is a standing rule: dead rows carry no follow-up date.
Keep only people who have a status or a follow-up date.

STEP 3. Read every Notion row.
Use mcp__Notion__notion-query-data-sources in VIEW mode against the Default view above, paging with start_cursor until has_more is false. View mode has no usage quota. Do NOT use SQL mode for the bulk read, it has a quota that runs out. Capture each row's page id, title text, Status, Next Follow-up and Email.

STEP 4. Match, using the same normalisation on both sides: lowercase, strip everything that is not a letter or digit. Notion titles may be wrapped in markdown link syntax, so use the visible text. Also try a fallback that strips accents, because the sheet drops accented characters (Tobi Lutke, Kristo Kaarmann). Never force an uncertain match; report it unmatched instead.

STEP 5. Decide writes. These rules are strict:
  Status: write only if the sheet has a non-empty status that differs from Notion's. A blank in the sheet NEVER clears a Notion status.
  Next Follow-up: write if the sheet has a date that differs from Notion's. If the sheet date is empty AND the status is Unresponsive, Declined or Do not contact, clear Notion's date with {"date:Next Follow-up:start": null}. Otherwise leave it alone.
  Email: fill only when Notion's Email is empty. Never overwrite an existing email.
  Never touch Category, Connect, Country or the title. Those live only in Notion and the sheet has no column for them.
  Skip rows where nothing changes. No no-op writes.

STEP 6. Write with mcp__Notion__notion-update-page, command "update_properties", allow_async false, passing only the changed properties.

STEP 7. Report back in plain text, short:
  - how many sheet rows matched, how many did not, and name the unmatched ones
  - every status change as "Name: old -> new"
  - how many follow-up dates moved, and the date range they moved to
  - anyone in the sheet who is not in Notion at all, listed as candidates to add, but do NOT add them yourself
  - any failures
If nothing changed, say "No changes" and stop.

Do not create rows, do not delete rows, do not create a database, and do not touch any other Notion database.
```
