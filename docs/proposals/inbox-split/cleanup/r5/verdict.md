# Cleanup verdict: CTO r5 capture fix (2 Nov, ~00:45 JST)

**Accept with one fix:** deploy `cleanup/r5/capture.txt`, **36,833 / 5d514d9aab17f4b2**, not 405a30d3. It is CTO r5 plus one replacement (`cleanup/r5/fix2.py`), built twice, byte-identical, with no em-dashes.

## What I checked

- **Rebuild.** `cto-r5/fix.py` applied to 60ee33ad reproduces **36,666 / 405a30d3ba6cbea2** twice. The diff holds only the two intended replacements:
  - the RAW recipe;
  - IDENTITY's pointer to that recipe.
- **Real ad@ originals (read-only).** I fetched two with `email_read original`:
  - Molly Ruland's reply, `[Gmail]/All Mail:108738`, 17,423 bytes;
  - a Luma notice, `:108938`, 27,335 bytes.
- **Result shape.** Both came back inline, as JSON with a `data` field holding the base64 .eml.
  - In both, the Message-ID header sits after 6 to 7 KB of ARC, DKIM and Received headers. That puts it past base64 offset 8,000, so the recipe's second chunk is used every time.
- **Saved-file one-liner.** It works. On a JSON file shaped like the tool result, it printed the full id `CAN8JMk1W=sGA7xLzDSpaVY8NjswRjT+rApUZDvFL+v9d1h3_eg@mail.gmail.com`.
  - HEADER search confirmed that id is Molly's message in ad@.

## Defect (fixed in the rev)

**The inline recipe can return a truncated Message-ID.**
- "not there, the next 8000" decodes the next chunk on its own.
- **Reproduced:** a header that starts 25 bytes before the 8,000-character boundary.
  - Chunk 1 alone gives `Message-ID: <CAN8JMk1W=sG`, a truncated id that matches the grep.
  - Chunk 2 alone gives nothing.
  - The two decoded together give the full id.
- A truncated id would become the row's `msgid:` key. That means a wrong key and a duplicate row, and the HEADER lookups and dedup would miss it.
- Copying thousands of base64 characters by hand into a heredoc can also flip a character inside the id.

**Fix (one replacement):**
- "no complete id (one ending ">"), append the next 8000 to the same file and run it again".
- "Either way, check the id: email_read search with query HEADER Message-ID "<id>" must return this message, else it is not its id". A failed check falls under r5's existing rule: pend `mcp:<id>` and go on.
- That check is one cheap search, and it catches truncation and copying errors on both paths.

## Unchanged and correct in r5

- A message with no Message-ID pends `mcp:<id>` and never stops the run.
- The one-liner prints NONE when no header is found.
- The `mcp:` retry is by id.
