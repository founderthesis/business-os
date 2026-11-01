# Reconciliation of older mail records: read-only pass, 1 Nov ~18:10 JST

**Not started.** No Notion write was made. Two reasons:
1. **The CTO's precondition hasn't been met.** The inbox backlog hasn't cleared. The latest run record is "Run inbox 2026-11-01 17:03 JST: Partial, read to 2026-10-30T08:41:47Z". Read-to is moving about 2 to 5 hours of mail per run, so it's roughly 10 or more runs from today.
2. **This builder session doesn't write to Notion or send mail** (its standing rule). The asked scope includes business actions: Your call, replies owed and status moves. Some of those are sends. So the write pass needs Akshay's own go-ahead in this session, or it's run by the CTO or main session.

## Counts (Activities, read only)

| What | Count |
|---|---|
| Rows with Source ID `allmail:` | 83 (none linked to an Engagement) |
| ... created per hour (UTC), 1 Nov | 03h: 11, 04h: 12, 05h: 15, 06h: 15, 07h: 15, 08h: 15 |
| ... with the same Date as a `msgid:` row (likely duplicates) | 25 |
| Email in or out Activities dated 29 Oct or later with no Engagement and no Deal | 84 (25 in, 59 out) |

**What the likely duplicates are.** Most are Zoya's own sent mail: replies, acknowledgements, follow-ups and holding replies. Zoya logs them under `msgid:`. The inbox logs them again from ad@'s All Mail, because Akshay is in Cc. Two are Akshay's own mails (Zencastr; BlackRock's loop-in). One is an inbound (Heartcast Media's no to the sponsored route for Peter Imburg).

**Every inbox run from 12:12 to 17:03 kept creating `allmail:` rows,** 15 per run at the cap. The rev Cleanup accepted, live since about 17:35, should stop this. The 18:03 run record will show whether it did. Watch for `allmail:` rows created after 09:00Z.

## Plan for the write pass

It runs once read-to reaches 1 Nov, outside :02 to :20. It's `reconcile-allmail.md`, extended to the unlinked rows:
1. **Inventory:** export each row's Message-ID (one `original` at a time), class and proposed action to `data/` (git-ignored).
2. **Classes:**
   - **A, re-key and link:** no msgid row exists. Set `msgid:` and link the Engagement and People per the inbox's match rules.
   - **B, fold:** a msgid row exists. Carry missing links to it, then Trash (decision 416).
   - **C, unreadable:** no Message-ID. Leave it.
   - **D, unlinked msgid rows:** link only.
3. **Business actions** the newly linked mail implies, each recorded as applied, handed over or blocked:
   - **Status moves:** applied, by the inbox's STEP 3 rules. The Heartcast Media no to the sponsored route, for example, means They declined, with the sponsored steps removed.
   - **Replies owed:** handed to Zoya as "Zoya: <step>". Nothing is sent from the reconciliation.
   - **Your call text:** handed to the inbox's next run, which now takes Your call first.
   - **Decisions only Akshay can make:** go on his list.
4. **Reconcile:**
   - zero `allmail:` rows apart from class C;
   - every Email in or out since 29 Oct linked, or listed with a reason;
   - counts before and after.
