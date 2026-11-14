# One-off: reconcile the allmail: Activities

**Scope.** The 12:12 JST run on 1 Nov logged 15 Activities with Source ID `allmail:<MCP Emails id>`. They have no Engagement or People links, and at least 4 duplicate rows already keyed `msgid:`:
- Moni / One Source, Zoya's reply of 29 Oct;
- George / Candour, Zoya's reply;
- Yuvraj / Sri Samvardhini, the pitch;
- the same pitch's loop-in.

Any later run before the msgid patch goes live can add more. Once the patch is live, the inbox itself re-keys an `allmail:` row it re-reads when there's no `msgid:` row (STEP 2). This plan is for the rest. One writer: run it from a single session while no inbox run holds the hour (between :10 and :55), and pause nothing else.

## 1. Read-only inventory

1. In Activities, list every row with `"Source ID" LIKE 'allmail:%'`, with its Summary, Date, Kind, Engagement and People. Count them. On the CTO's figure, 15 are expected.
2. For each row, fetch its message on ad@ (MCP Emails `email_read read` on the id after `allmail:`). Then get its Message-ID with `email_read original`, one at a time, decoded in Bash, keeping only that line.
3. For each Message-ID, query Activities for the existing spellings: `msgid:<id>`, `Source ID LIKE '%<part before @>%'`, the bare id, `mcpemails:<part>`.
4. Classify each row:
   - **A.** No other row has this Message-ID. Re-key it.
   - **B.** A `msgid:` row exists. This is the duplicate.
   - **C.** No Message-ID can be read. Leave it.
5. Write the table to a review file in `data/` (git-ignored): Activity id, `allmail:` id, Message-ID, class, the other row's id. Report the counts. No writes yet.

## 2. Writes (after the table is read back)

**Class A:**
1. Set Source ID to `msgid:<Message-ID>`.
2. Link the Engagement, People and Deal the same way inbox STEPS 3 to 5 would. Use the existing match rules. Where a match is uncertain, link nothing and list the row.
3. Re-read the row.

**Class B:**
1. Keep the `msgid:` row. Copy across anything the `allmail:` row adds that the kept row lacks: the Link, People, the Engagement, and a body line not already there. Re-read the kept row.
2. Then check that the `allmail:` row has no relations left besides the ones just copied. Clear those, and move it to Trash (decision 416).
3. List each one in the report.

**Class C:** leave it as it is, list it, and let the next inbox run's pending line pick it up.

**Never:**
- merge People;
- change a kept row's Kind, Summary or author;
- send mail or do a loop-in. Any loop-in a re-keyed pitch still needs comes from the next inbox run's STEP 6 catch-up, which looks back 72 hours.

## 3. Check and report

1. Re-run the step 1 query. Zero `allmail:` rows should remain, apart from class C.
2. Report the counts per class, every row moved to Trash, every link left out as uncertain, and the class C rows.
3. Add one line to the run record of the next inbox run's day, Summary "Reconcile allmail <date>: <n> re-keyed, <n> folded, <n> left".

**Cost:** about 15 `original` reads, about 15 Activities queries, and up to about 30 writes. That's about one inbox run's worth.
