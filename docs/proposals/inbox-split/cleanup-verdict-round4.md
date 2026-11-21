# Cleanup verdict: inbox split round 4 (849dc1d), 1 Nov

**Not accepted.** There are 4 blocking defects and 6 should-fix. Each blocker is a clause or two. One blocker (V3) is a live fact about the ad@ mailbox that no offline replay could find; it also affects the current single-prompt inbox. Nothing is deployed.

The replays are in `cleanup/round4/`: `closure.json` and `newholes.json`.

## Rebuilt twice, byte-identical, hashes match

| File | Bytes / sha256 |
|---|---|
| capture.txt | 35,848 / 0c7cb3d1a16d13bd |
| actions-v2.txt | 39,354 / 19701651a6c0edf3 |
| yourcall-sections.md | 7,326 / a28b43da3b0aac36 (unchanged) |
| sweep.txt | 39,131 / 6783dd01e396e5ab (unchanged) |

- There are no em-dashes in the prompts. The sweep has one, a pre-existing quoted Notion heading.
- Completeness: the only newly missing unit is STEP 1's old cursor sentence, which is the R2 rewrite.

## Round 3 items

- **R1:** closed for her logged sends. The same rule now appears in STEP 0, STEP 1 and actions.
- **R2:** closed. Capture's CURSOR and STEP 1 both fall back from run:inbox-capture: to run:inbox:, and stamping is limited to rows created since 2026-11-01 12:00 JST.
- **R3:** closed for mail rows. The try line is written before the row is started.
- **R4:** closed. Both prompts get today from `TZ=Asia/Tokyo date +%F`.
- **Should-fix 1 to 8:** closed.
- **Round 2:** B1, B3, B4, B9, S2 and S4 are closed.

## R1b, checked on real rows (read-only)

**Yes: Zoya's routine logs ad@ mail she's only on as a copy recipient.** Her prompt says "Log it if Akshay isn't on To or Cc, or if no Activity has its msgid: Source ID yet". Two real cases:
- Molly Ruland (Heartcast Media), "we decided to pass for now" on Peter Imburg, 30 Oct 00:06Z;
- Archana Jain (Finploy), 30 Oct 10:23Z.

Both are in ad@ All Mail, and both are Activities Zoya logged as Email in with `msgid:` keys. So stamping Email in rows that another routine logged first is needed. Without it, actions would never record Molly's pass.

## Blocking

**V1. RUN RECORD drops the "stamped:" line.**
- STEP 1 adds each late-stamped id "to your record's body line "stamped: <ids>" as you stamp it".
- RUN RECORD's last write sets "page body = a line "pending: ..." ..., the report, ..." and never names "stamped:". A literal rewrite loses the list on every normal run, and actions never sees those rows.
- **Fix:** "page body = the "stamped:" line as built (first line, kept), then the "pending:" line, ...".

**V2. A crash between stamping and listing loses the row. This is Main's open item, and it blocks.**
- After the stamp, the next run skips the row, because the exception covers only rows "without a "capture:" line".
- The row is older than W, on no list, and created after 2 Nov, so no path reaches it again. It's lost silently.
- It could be a guest's "confirms 14 Nov" that Zoya logged first.
- **Fix:** "first add its id to your record's "stamped:" line (write it), then give the row its "capture:" line", in STEP 1 and in STEP 0.

**V3. A text search for a Message-ID finds nothing in ad@ (found live, read-only).**
- ad@ is generic IMAP over Gmail. On that mailbox `email_read search` with text = <Message-ID> returned 0 for two messages that are in All Mail:
  - Molly's, Message-ID beginning "CAN8JMk1W";
  - Archana's, Message-ID ending "@finploy.com".
- The raw query `HEADER Message-ID "<id>"` found Molly's at once.
- Capture relies on the text search in three places:
  - **STEP 0** ("look for its message in ad@ (search text = the Message-ID). Not there: it is Zoya's, add nothing"). Every `msgid:` row would read as Zoya's, so the 84 unlinked rows would never be linked.
  - **The pending retry** ("search text = it"). A pending Message-ID is never found again, and it holds "read to".
  - **The Gmail tool map's rfc822msgid line.**
- **Fix:** in all three, use `email_read search` with query `HEADER Message-ID "<id without angle brackets>"`.
- **Same gap, not blocking:** THREAD's "every message whose headers hold its Message-ID (search text = it)" also finds nothing. `HEADER References "<id>"` returned 0 too, although Zoya's reply to Molly should reference her message. Follow-on replies need another route, such as a subject search ("Re: <subject>") within the thread's people.
- **The live single-prompt inbox has the same text-search rules.**

**V4. STEP 0's "add nothing" rows stall it.**
- STEP 0 says "Every row this step touches gets Captured today ... so it is never taken twice". But its two "add nothing" branches ("an Email out whose Summary starts "Zoya" is hers", and "Not there: it is Zoya's") don't count as touched.
- Those rows keep their old Captured date. Ordered "oldest Captured first", they fill the 8 `msgid:` slots every run, so the class never drains.
- With V3 unfixed, that's every `msgid:` row.
- **Fix:** leave Email out rows whose Summary starts "Zoya" out of the query. For a "Not there" row, set Captured today and the body line "capture: n/a (not in ad@)", and select only rows without a "capture" line.

## Should-fix

1. **Zoya's rule depends on Kind.** If capture logs a copy of her send before she does ("Zoya to X"), Kind is Email out only if her People row is tagged Team; otherwise it's Email in and actions works it. **Fix:** drop "Email out" from the rule (a Summary starting "Zoya" is hers), or confirm her People row is Team before cutover. 6e's "our side" also depends on that tag.
2. **Akshay's mail can be logged by Zoya as Email in.** When Akshay writes with Zoya on To or Cc and her routine sees it first, she logs it Kind Email in, but STEP 2b only takes Email out. I found no such row since 30 Oct, so it's a prompt risk, not observed. **Fix:** 2b takes any row whose sender is Akshay, whatever its Kind.
3. **Your call can crash-loop and cost hours.**
   - Your call rows have no try limit: a row that crashes STEP 0 crashes every run. Add "yourcall: try <n>", and leave a row after 3 tries.
   - Every crashed run leaves a Started record, so the 90-minute guard makes the next run a No-op and Your call skips that hour. Use 50 minutes, or let Your call run even under the guard.
4. **A per-message 5xx can reset its own tries.** "Not one tied to a row ... removes its own try lines" lets a 5xx that one message triggers clear its tries every run, so the row never goes stuck. **Fix:** a failure while a row is open counts against that row.
5. **The clocks are mixed.** "read to <ISO time>" and "worked to <ISO>" have no offset, and "created before 2026-11-02" has no zone, while TIME says JST. **Fix:** write ISO times with "Z", and say "2026-11-02 00:00 JST".
6. **Write the "capture:" line last,** after linking, so actions at :25 never takes a row capture is still linking.

**Nit:** a "Zoya sending:" row whose message Blueticks shows went is never renamed. Rename it then.

## Cutover

- Paste sections 6 to 8 of the Controls page and read them back before actions is enabled. Actions fails closed without the three headings and the end line, confirmed in round 3.
- Capture can be enabled any time on or after 2 Nov JST now that today is JST, but only once V1 to V4 are in.
- **Separately, V3 affects the live single-prompt inbox (disabled) and the rollback build** 65,227 / 3bb46f9332241e3b: its pending retry and THREAD lookups use the same text search. If the inbox is re-enabled before the split, the same one-line fix applies.

## Addendum: the four blockers as a ready patch (CTO, 1 Nov ~22:20: inbox live tonight, blockers only)

`cleanup/round4/capture_fix.py` applies V1 to V4 to Main's capture.txt (0c7cb3d1a16d13bd) with seven exact replacements.

**Output:** `cleanup/round4/capture.txt`, **36,007 / 60ee33adf4659c03**. Built twice, byte-identical, with no em-dashes added. Actions-v2, yourcall and sweep are unchanged.

**What each replacement does:**
- **V1:** RUN RECORD's body is now "the "stamped:" line as built (first line, kept), then" the pending line.
- **V2:**
  - In STEP 1, the id is written to "stamped:" before the row is stamped.
  - In STEP 0's ad@ branch, the "capture:" line and Captured today go in one write. Actions reaches those rows through its Captured window.
- **V3:** the rfc822msgid map, the pending retry and STEP 0's lookup now use query `HEADER Message-ID "<id>"`.
- **V4:** both "add nothing" branches now "only set Captured today". The row leaves STEP 0's queue, which takes only rows Captured before 2026-11-02. It gets no "capture:" line, so actions skips it.

**With this patch, capture is accepted on the blockers**, as `cleanup/round4/capture.txt` 36,007 / 60ee33adf4659c03, with actions-v2 39,354 / 19701651a6c0edf3. If Main folds the same seven edits into split.py instead, its output must match this file byte for byte.

**Follow-ups, not reasons to reject:** should-fix 1 to 6 above, and THREAD's forward search ("search text = it", which finds nothing in ad@). That last one is already in the live prompt today. The most worthwhile of them before or soon after cutover is confirming Zoya's People row is tagged Team (should-fix 1), because a send that capture logs before Zoya does turns into Email in otherwise.
