# Cleanup delta verdict: r24 at e1a60a4 (C1 and S1 to S4), item 9 (4f6857d, decision 522), item 10 (b34639d, docs)

Cleanup session, 8 Nov 2026, about 11:50 JST. Read-only. Item 11 (guest form chasers) isn't pushed yet and is reviewed when it lands.

## Verdict: accepted. C1 is met, and the Zoya part can deploy.

### Builds (each twice, byte-identical, equal to the commit; under 65,536; no new em dash)

Deploy order and hashes. This replaces the table in cleanup-verdict.md.

| # | Routine | Bytes / sha256 |
|---|---|---|
| 1 | Calendar sync (unchanged) | 62,916 / c613af00ddf02c8c |
| 2 | Inbox capture | 50,431 / f64eb54edabe7326 |
| 3 | Inbox actions (+ section6-522.md paste, which supersedes section6-519.md) | 47,204 / 829a8cc8fb21251f |
| 4 | WhatsApp | 32,813 / bec8c1e1acb97e08 |
| 5 | Zoya pin 9a79960: SLOW file | 91,039 / d953cd1c3206a951 (91,035 characters) |
| 5 | Zoya hourly | 62,974 / e959b0476d892c12 (under 63,000) |
| 5 | Zoya SLOW task | 15,949 / 2efa79c08ac2bd41 |
| 6 | Daily sweep | 50,017 / 9eca3bd65011a45c |
| 7 | Host boards (unchanged) | 8,733 / 7f5c87ab1b7883c4 |
| 8 | Host dossiers and prep notes (unchanged) | 6,503 / 67e07a00a19e3c60 |

Zoya episodes (not live): 49,964 / 1d23893375fe9dd2.

The SLOW task fetches 9a799603826c768b72dd71e09d65003317093e01, expects sha prefix d953cd1c3206a951 and 91,035 characters, all matching the file at 9a79960.

### e1a60a4: my condition and should-fixes, all in

- **C1:** the hourly and the SLOW file's 517 sentence now ends "quote only the pitcher's own forwarded mail, never his note or the loop-in". The other Zoya changes are citation cuts only (decisions 421 and 453 shortened) and the version references.
- **S1:** sweep 3p's link comes "from its Prep doc link (named 'Dossier link' until the rename ...)".
- **S2:**
  - 3p finds the row by "Guest or Stakeholders"; a match by Organisation alone is reported and nothing is created (decision 424);
  - the segment is added "unless the row already has it".
- **S3:** capture's pointer reads "inbox actions STEP 5".
- **S4:** WhatsApp 0w's report names the number's source ("number from FT Community" or "number from saved contact").

### Item 9 (decision 522, context-aware chasers): accepted

The CTO's four checks all hold:
- **No new sender.** Inbox actions only reads the person's one-to-one chat through Blueticks, read only, and still only drafts. STEP 0w is still the only sender.
- **486's exact-draft ok is kept.** Section 6's 5/ copies "the message line, never the context line" into "approved text", and only that line is sent.
- **519's matching is unchanged** in 0w's lookup. The chat read for drafting uses the same match ("matched as STEP 0w matches it"), never a group, never anyone else's chat.
- **The context line stays outside the copyable text.** It's on its own line under the draft, excluded from the approved copy, and 0w says "the draft's 'context:' line is never sent".

Also fine:
- A two-part text (" || ") goes in order, the second only after the first.
- The crash check looks for each part in the chat, so a part that already went is never re-sent.
- An already-answered ask gets no draft.
- "No chat found or not sure" is said in the context line, and the draft never pretends to know the chat.

**Should-fix (minor), item 9:**
- **Separator in quoted text.** If Akshay's quoted text itself contains " || ", it would be split into two sends. Say that " || " splits only a text Zoya wrote, or have the quoted form use it on purpose.
- **section6-522.md supersedes section6-519.md.** The CTO pastes only 522 at deploy, replacing the whole WHATSAPP CHASE block.

### Item 10 (docs): fine

architecture.md gets one current map of where work lives:
- Engagements for guests, sponsors, PaaS and Kind Task work;
- Team tasks for post-production;
- Deals and Tasks retired;
- Clairva and the cold list noted as open.

It also marks the 30 Sep tables as history and fixes its three Deals lines. CLAUDE.md names the Team tasks exception (499) and the Deals retirement (518). No address or number was added.
