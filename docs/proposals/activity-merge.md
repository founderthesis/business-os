# Activity identity: patch and one-time merge (for Cleanup)

CTO, 21 Oct: ingestion reuses the existing Activity for a message id, caps and the 7-day rule count unique ids, and the duplicates from the 20 Oct re-logs are merged with their provenance kept. Prepared, not reviewed, nothing written.

## Prompt patch

`python3 docs/proposals/activity-identity.py <cut-1 out dir> <out>`, composed on Cut 1:
- Inbox STEP 2: one query for every candidate id; an id already logged makes zero rows and is never relabelled (only a missing link is added); Kind follows the From header. 57,002 B / 189b15491740f578.
- Zoya LIMITS: the daily cap and the 7-day rule count unique Source IDs. 48,964 B / 7445e3f84c7da6d7 (on the 10:00 to 23:00 Cut 1 build).

## The duplicates (read-only check, merge-detail.md below)

25 Source IDs, 56 rows, 31 extras: 29 extras from the 20 Oct re-logs (15:07 and 21:05 UTC), Neeti's second 19 Oct row, and one Gemini-notes id from 18/19 Oct. The keeper is the earliest row, except Damsun (the later row has the Engagement and Deal links) and Neeti (the earliest is blank and names the wrong author).

The Activities schema has no field to flag a row, and the connector cannot delete. So the merge is:

1. **Fix 4 keepers** (exact from the Gmail headers):
   - Damsun keeper 3ff19a301a7f81f0a089f3cffb4713d8: Kind Email in to Email out (sent by Chaandini).
   - Hrithik, Vishnupriya, Palak keepers: Summary "Zoya sent: holding reply ..." to "Akshay to <name>: Zoya loop-in" (sent from Akshay's mailbox with Zoya in Cc).
2. **Neutralise the 31 extras** so no routine counts or follows them, keeping each row for provenance until a person deletes it: Summary becomes "Duplicate of <keeper page id>: <old summary>"; Source ID becomes "dup:<old id>" (so the identity query only ever finds the keeper); the Engagement, Deal, People and Episode relations are cleared (two of them point at a deleted Engagement anyway). Nothing else changes.
3. **Akshay deletes the 31 rows** when convenient (a filtered view "Summary starts Duplicate of"); added to docs/akshay-pending.md. No new property.

Writes: 4 + 31 page updates, one writer, after Cleanup accepts. Read back every row after.

## Risks for review

- Clearing relations on an extra removes nothing the keeper lacks: the check found the extras' relations equal to or fewer than the keepers' (Aanshul's copies point at a 404 Engagement, Amanda's lack the Episode, Hrithik's has one People link of two).
- "dup:" Source IDs are not message ids, so no routine can match them; the AR-8 run-record and due-vs-done selectors use other prefixes (run:zoya:, scorecard:, precall:).

## merge-detail

# Activities duplicate merge plan (read-only research, 21 Oct 2026)

Data source: collection://290f715d-fd45-4203-ade6-3642c2326c6c. Nothing was written anywhere. Page ids are Notion page ids (prefix https://app.notion.com/p/). Times UTC.

## 1. Schema

| Property | Type | Options / notes |
|---|---|---|
| Summary | title | |
| Kind | select | Email in, Email out, Meeting, Call notes, Form, WhatsApp, Note, Draft |
| Source | select | Gmail, Calendar, Gemini notes, Form, Slack, Migration, Manual, WhatsApp |
| Source ID | text | dedupe key (Gmail message id) |
| Link | url | |
| Date | date | |
| Captured | date | |
| Engagement | relation | Engagements (collection://5522ee21-...) |
| Deal | relation | Deals (collection://1a981c5a-...) |
| People | relation | People (collection://e6c44319-...) |
| Episode | relation | Episodes (collection://5d250752-...) |
| Template | relation | Templates (collection://b2976a03-...) |
| Draft ID | text | Gmail draft id a routine created |
| Edit size | select | None, Minor, Major, Rewritten |
| Edit note | text | one line on draft vs sent |
| Draft sent | formula | 1 when an agent draft went out and edits were measured (not SQL-queryable) |
| Clean send | formula | 1 when draft went out with no/minor edits (not SQL-queryable) |
| createdTime | system | |

**No field suits a duplicate flag.** There is no checkbox, status, archive, review or "duplicate of" property, and no Kind or Source option for it. The only free-text candidates are Edit note (has its own meaning for draft measurement) and Summary/Source ID (overwriting them breaks the dedupe key and the record). To flag without deleting, the schema needs a new property, e.g. checkbox "Duplicate" or relation "Duplicate of" (self-relation to the keeper). That is a schema change: propose to Akshay first.

## 2. Duplicates per Source ID

Columns: page id, created, Kind, Summary (short), relations E/D/P/Ep (Engagement/Deal/People/Episode counts), body. Keeper first.

All bodies are one short line except where marked EMPTY.

### In the 24-id set

**1a14fbc892a03516** (Tanuj, pitch form mail)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f817c8bb7f8731cdf2a6a | 19 Oct 07:16 | Email in | Tanuj (Apex Market Intelligence) to Akshay: submitted the pitch form | 0/0/0/0 | yes |
| extra | 3ff19a301a7f814eac25c98e8f01393e | 20 Oct 15:07 | Email in | Tanuj (Wryto) to Akshay: submitted the pitch-to-us form | 0/0/0/0 | yes |

**1a1519cb70911a28** (Akshay thumbs-up to Tanuj)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3ff19a301a7f815084e9ffbd982a3166 | 20 Oct 07:15 | Email out | Akshay to Tanuj (Apex Market Intelligence): thumbs-up | 0/0/1/0 | yes |
| extra | 3ff19a301a7f8145a074dc1a5e79b94d | 20 Oct 15:07 | Email out | Akshay to Tanuj (Wryto): thumbs up | 0/0/0/0 | yes |

**1a1527ce749067db** (Akshay to Aanshul, RedSeer)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81e5b90eed0d01e744ef | 19 Oct 12:15 | Email out | will come back to you | 1/0/0/0 | yes |
| extra | 3ff19a301a7f81949a2dcefbd0186575 | 20 Oct 15:07 | Email out | will come back to him | 1*/0/0/0 | yes |

\* extra links Engagement 3f019a301a7f81a08e66d02c507e0813, which returns 404 (no such page). The keeper links the real Engagement 3ed19a301a7f81a08e66d02c507e0813 (Anil Kumar @ RedSeer), whose Activities list contains only the keeper.

**1a152d1642506511** (Akshay to Vineeta, AppsForBharat)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81f09e1dd208470b3133 | 19 Oct 12:15 | Email out | photo low resolution | 0/0/0/0 | yes |
| extra | 3ff19a301a7f81f2a7b6ce3e25780cc3 | 20 Oct 15:07 | Email out | same | 0/0/0/0 | yes |

**1a1530fc9d935090** (Chaandini: Damsun pitch link live)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| earliest | 3fe19a301a7f81e0b241ebd46018cab2 | 19 Oct 12:15 | Email out | Chaandini to Zoya and Akshay: Damsun pitch link live | 0/0/0/0 | yes |
| KEEPER (exception) | 3ff19a301a7f81f0a089f3cffb4713d8 | 20 Oct 15:07 | Email in (wrong) | Chaandini to Akshay and Zoya: Damsun Group pitch link live | 1/1/0/0 | yes |

Exception: the later row has strictly more relations (Engagement 3f019a301a7f81a6ae05d2426c2d63aa Puneet Garg @ Damsun, Deal 3fc19a301a7f813a898fd2673d2b0502). Either keep the later row and fix its Kind to Email out, or keep the earliest and copy both relations onto it.

**1a1531a34ec804fd** (Akshay to Neeti: why-sponsor)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f8129b41addd3aebaa7be | 19 Oct 12:15 | Email out | points to podm.in/why-sponsor | 1/0/0/0 | yes |
| extra | 3ff19a301a7f8144b947f0660215eec7 | 20 Oct 15:07 | Email out | same | 1/0/0/0 | yes |

**1a1531a61598725a** (Akshay to Neeti: adding Zoya), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| earliest | 3fe19a301a7f81d7a514e7e9b61ad65d | 19 Oct 07:40 | Email out | Zoya sent: Zoya loop-in to Neeti (wrong author; Date empty) | 1/0/0/0 | EMPTY |
| KEEPER (exception) | 3fe19a301a7f81f8be80c64bebc70d83 | 19 Oct 12:15 | Email out | Akshay to Neeti: thanks, adding Zoya to coordinate | 1/0/0/0 | yes |
| extra | 3ff19a301a7f819aab79fb15e5987151 | 20 Oct 15:07 | Email out | Akshay to Neeti: Zoya loop-in | 1/0/0/0 | yes |

Exception: the earliest row has an empty body and empty Date; the 12:15 row has a body, a Date and the correct author. Note the 07:40 and 12:15 copies were both created on 19 Oct, so one of this id's extras predates the 20 Oct re-log.

**1a1533b1b0db3c63** (Chaandini to Jessica, PodcastGuests)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81d2ac49dffa05ac7afa | 19 Oct 12:15 | Email out | three shows submitted | 0/0/0/0 | yes |
| extra | 3ff19a301a7f81448595ea324343deca | 20 Oct 15:07 | Email out | same | 0/0/0/0 | yes |

**1a15344433c1202f** (Hrithik, Byufuel pitch)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81f1bd9dece432056c84 | 19 Oct 12:15 | Email in | pitches Manish Marwaha | 1/0/2/0 | yes |
| extra | 3ff19a301a7f81259208d72bec36e8f5 | 20 Oct 15:07 | Email in | proposes Manish Marwaha | 1/0/2/0 | yes |

**1a15347cffecf261** (Aanshul: WhatsApp number)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81dca83cd8d443fb6237 | 19 Oct 12:15 | Email in | his number is also his WhatsApp | 1/0/0/0 | yes |
| extra | 3ff19a301a7f81c6a828c186a503a61c | 20 Oct 15:07 | Email in | same | 1*/0/0/0 | yes |

\* extra links the non-existent Engagement 3f019a301a7f81a08e66d02c507e0813 (404), as above.

**1a15414f5120037b** (loop-in to Hrithik)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81e1837af3a930db7831 | 19 Oct 12:15 | Email out | Zoya sent: holding reply to Hrithik (Byufuel) (wrong author) | 1/0/2/0 | yes |
| extra | 3ff19a301a7f8138bd00d7c5f81b18f0 | 20 Oct 15:07 | Email out | Akshay to Hrithik (Byufuel): Zoya loop-in | 1/0/1/0 | yes |

Keeper has more People (2 vs 1); fix its Summary (see corrections).

**1a15424891159f17** (Vishnupriya, Mindgrove pitch)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f812e89b6c4bf365cb35f | 19 Oct 15:16 | Email in | pitches Shashwath TR | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81baae06e9216b47806b | 20 Oct 15:07 | Email in | suggests Shashwath TR | 1/0/1/0 | yes |

**1a15426fca608b54** (Palak, QubeHealth pitch)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f8183920accaa5fa6039e | 19 Oct 15:16 | Email in | pitches Chris George | 1/0/1/0 | yes |
| extra | 3ff19a301a7f817eafdec73b24d60f61 | 20 Oct 15:07 | Email in | same | 1/0/1/0 | yes |

**1a15458f279fd4a5** (Ashmita: revised agreement)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f8179a5aff46bb7e8c6ca | 19 Oct 15:16 | Email in | revised Pathfinders agreement | 0/1/0/0 | yes |
| extra | 3ff19a301a7f81a6bb10eb29dc305662 | 20 Oct 15:07 | Email in | same | 0/1/0/0 | yes |

**1a1547191cffc08a** (Akshay to Ashmita: approver)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f8199a2cfde87da261477 | 19 Oct 15:16 | Email out | nominate an approver | 0/1/0/0 | yes |
| extra | 3ff19a301a7f818c8971e305f9f09f3d | 20 Oct 15:07 | Email out | same | 0/1/0/0 | yes |

**1a154738a99fecb9** (Akshay to Ashmita: waive approver)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81588dbdff74c26c431e | 19 Oct 15:16 | Email out | give up approver role | 0/1/0/0 | yes |
| extra | 3ff19a301a7f8183be0ff5e3a247c11a | 20 Oct 15:07 | Email out | same | 0/1/0/0 | yes |

**1a15479f0462dbe0** (Akshay to Merlin, Lemma)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81a6a982d2be7a23df23 | 19 Oct 15:16 | Email out | organic, Friday 6:30 pm | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81eebdecef08f1e7d611 | 20 Oct 15:07 | Email out | same | 1/0/1/0 | yes |

**1a154bc0d42425a3** (loop-in to Vishnupriya)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81329471deae2dc58d4c | 19 Oct 15:16 | Email out | Zoya sent: holding reply to Vishnupriya (wrong author) | 1/0/1/0 | yes |
| extra | 3ff19a301a7f8171bb72e5eacbe771b0 | 20 Oct 15:07 | Email out | Akshay to Vishnupriya (Madchatter): Zoya loop-in | 1/0/1/0 | yes |

**1a154bc17c2ec63d** (loop-in to Palak)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f811bb5e9cbe781da66fd | 19 Oct 15:16 | Email out | Zoya sent: holding reply to Palak (wrong author) | 1/0/1/0 | yes |
| extra | 3ff19a301a7f818495f4cdf8d210318a | 20 Oct 15:07 | Email out | Akshay to Palak (one2en): Zoya loop-in | 1/0/1/0 | yes |

**1a15508f8eeda88e** (Surabhi: 26 Oct slot), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f8158ba8fe7b265dfcf2f | 19 Oct 23:11 | Email in | offers Mon 26 Oct 10:15 pm | 1/0/1/0 | yes |
| extra | 3ff19a301a7f817296eecdcc4fa0de34 | 20 Oct 15:07 | Email in | same | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81d889cbf635794d45d5 | 20 Oct 21:05 | Email in | same | 1/0/1/0 | yes |

**1a155f3b6ac335d6** (Amanda: run date), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81958179c4c1e16f6666 | 19 Oct 23:11 | Email in | asks run date | 1/0/1/1 | yes |
| extra | 3ff19a301a7f8149a474d92e593c2eb4 | 20 Oct 15:07 | Email in | same | 1/0/1/0 | yes |
| extra | 3ff19a301a7f817199d3ca4259d4a19b | 20 Oct 21:05 | Email in | same | 1/0/1/0 | yes |

**1a155ff1f7230684** (Akshay to Amanda: 3+ months), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f816b9f91f4f85c51bf5b | 19 Oct 23:11 | Email out | release 3+ months | 1/0/1/1 | yes |
| extra | 3ff19a301a7f81ac9df5d3c67bf1666b | 20 Oct 15:07 | Email out | same | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81c19cd2d23df82c4377 | 20 Oct 21:05 | Email out | same | 1/0/1/0 | yes |

**1a1560038717dc7a** (Akshay to Amanda: thank-you form), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f816aa8bdec5ab461809e | 19 Oct 23:11 | Email out | assets via thank-you form | 1/0/1/1 | yes |
| extra | 3ff19a301a7f81dab4f9c657c9d6cf0d | 20 Oct 15:07 | Email out | same | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81a5823cee75cdada5af | 20 Oct 21:05 | Email out | same | 1/0/1/0 | yes |

**1a156014a249f711** (Akshay to Surabhi: which time zone), 3 copies
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fe19a301a7f81a99f96e113a3727034 | 19 Oct 23:11 | Email out | which time zone | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81eb8756ee0b72cbfdeb | 20 Oct 15:07 | Email out | same | 1/0/1/0 | yes |
| extra | 3ff19a301a7f81e1bf6cfe93a9700e68 | 20 Oct 21:05 | Email out | same | 1/0/1/0 | yes |

### Not in the set (task 4)

**1a14e5594eb1017d** (Gemini notes, 18 Oct meeting)
| Role | Page id | Created | Kind | Summary | E/D/P/Ep | Body |
|---|---|---|---|---|---|---|
| KEEPER | 3fd19a301a7f813f999ef1ffe411bfa0 | 18 Oct 12:11 | Meeting | Meeting notes 18 Oct: Zoya and Codex automation, revenue dip, HBD guest selection | 0/0/0/0 | yes (real summary) |
| extra | 3fe19a301a7f8101bfd8ca6fe44becbd | 19 Oct 12:15 | Meeting | Gemini notes: meeting of 18 Oct, 5:53 PM JST | 0/0/0/0 | yes ("notes not opened in this run") |

This is the only other Source ID with more than one row touched since 19 Oct. A case- and whitespace-insensitive check found no variant spellings of any Source ID.

## 3. Corrections

Gmail returns sender addresses, not display names. Sender is given here as the owner of the mailbox (names only).

| Page id | Field | Current | Correct | Evidence |
|---|---|---|---|---|
| 3ff19a301a7f81f0a089f3cffb4713d8 (keeper, Damsun) | Kind | Email in | Email out | Gmail 1a1530fc9d935090: sender Chaandini's team mailbox, 19 Oct 07:28 UTC, To Akshay and Zoya, label INBOX. Chaandini is team, so Email out |
| 3fe19a301a7f81e0b241ebd46018cab2 (Damsun earliest) | Engagement, Deal | empty | Engagement 3f019a301a7f81a6ae05d2426c2d63aa, Deal 3fc19a301a7f813a898fd2673d2b0502 | only if this row is kept instead of the later one |
| 3fe19a301a7f81e1837af3a930db7831 (keeper, Hrithik) | Summary | Zoya sent: holding reply to Hrithik (Byufuel) | Akshay to Hrithik (Byufuel): Zoya loop-in | Gmail 1a15414f5120037b: SENT from Akshay's mailbox, 19 Oct 12:13 UTC, body "thanks Hrithik, adding @Zoya to coordinate", Zoya in Cc. Kind Email out is right |
| 3fe19a301a7f81329471deae2dc58d4c (keeper, Vishnupriya) | Summary | Zoya sent: holding reply to Vishnupriya | Akshay to Vishnupriya (Madchatter): Zoya loop-in | Gmail 1a154bc0d42425a3: SENT from Akshay's mailbox, 19 Oct 15:16 UTC, "thanks Vishnupriya, adding @Zoya to coordinate". Kind Email out is right |
| 3fe19a301a7f811bb5e9cbe781da66fd (keeper, Palak) | Summary | Zoya sent: holding reply to Palak | Akshay to Palak (one2en): Zoya loop-in | Gmail 1a154bc17c2ec63d: SENT from Akshay's mailbox, 19 Oct 15:16 UTC, "thanks Palak, adding @Zoya to coordinate". Kind Email out is right |
| 3fe19a301a7f81d7a514e7e9b61ad65d (Neeti, extra) | Summary, Date | Zoya sent: Zoya loop-in to Neeti; Date empty | (extra, flag as duplicate) would be Akshay to Neeti: Zoya loop-in, 19 Oct | Gmail 1a1531a61598725a: SENT from Akshay's mailbox, 19 Oct 07:39 UTC, "thanks Neeti, adding @Zoya to coordinate". Keeper 3fe19a301a7f81f8be80c64bebc70d83 already has the right author |
| 3fe19a301a7f81f8be80c64bebc70d83 (keeper, Neeti) | body | "Second short mail handing the thread to Zoya." | "Short mail handing the thread to Zoya." | it is the same single message, not a second one (optional) |
| 3ff19a301a7f81949a2dcefbd0186575, 3ff19a301a7f81c6a828c186a503a61c (Aanshul extras) | Engagement | 3f019a301a7f81a08e66d02c507e0813 | 3ed19a301a7f81a08e66d02c507e0813 | the 3f019... id returns 404; moot if these extras are removed |
| 3fe19a301a7f817c8bb7f8731cdf2a6a (keeper, Tanuj 1a14fbc892a03516) | company name | Apex Market Intelligence | keep as is | Gmail 18 Oct 15:58 UTC, signature reads "Tanuj Kumar, Apex Market Intelligence"; Wryto is only his mail domain. Optional: add People 3fe19a301a7f81bb865be6a570d0c257 (already on the 1a1519cb70911a28 keeper) |

Authorship note: the Hrithik, Vishnupriya, Palak and Neeti messages were all sent from Akshay's own mailbox with Zoya in Cc, so by the stated rule they are Email out with Akshay as author. "Zoya sent" on the 19 Oct rows is wrong; the 20 Oct re-logs got the author right but are still duplicates.

## 4. Totals

| | Ids | Rows | Extras |
|---|---|---|---|
| The 24-id set | 24 | 54 | 30 (24 created 20 Oct 15:07, 5 at 21:05, 1 on 19 Oct 07:40/12:15 for Neeti 1a1531a61598725a) |
| Other (1a14e5594eb1017d) | 1 | 2 | 1 |
| All | 25 | 56 | 31 |

29 of the 30 extras in the set were created on 20 Oct, which matches section 2c of obs.md. Keeper exceptions: 2 (Damsun 1a1530fc9d935090, Neeti 1a1531a61598725a). Only one page body is empty: 3fe19a301a7f81d7a514e7e9b61ad65d. The extras created on 20 Oct have lost the Episode relation (Amanda x3) and a People link (Hrithik loop-in), and 2 of them point at a non-existent Engagement (Aanshul x2).

Extras to remove or flag (31):
3ff19a301a7f814eac25c98e8f01393e, 3ff19a301a7f8145a074dc1a5e79b94d, 3ff19a301a7f81949a2dcefbd0186575, 3ff19a301a7f81f2a7b6ce3e25780cc3, 3fe19a301a7f81e0b241ebd46018cab2 (or 3ff19a301a7f81f0a089f3cffb4713d8 if the earliest is kept), 3ff19a301a7f8144b947f0660215eec7, 3fe19a301a7f81d7a514e7e9b61ad65d, 3ff19a301a7f819aab79fb15e5987151, 3ff19a301a7f81448595ea324343deca, 3ff19a301a7f81259208d72bec36e8f5, 3ff19a301a7f81c6a828c186a503a61c, 3ff19a301a7f8138bd00d7c5f81b18f0, 3ff19a301a7f81baae06e9216b47806b, 3ff19a301a7f817eafdec73b24d60f61, 3ff19a301a7f81a6bb10eb29dc305662, 3ff19a301a7f818c8971e305f9f09f3d, 3ff19a301a7f8183be0ff5e3a247c11a, 3ff19a301a7f81eebdecef08f1e7d611, 3ff19a301a7f8171bb72e5eacbe771b0, 3ff19a301a7f818495f4cdf8d210318a, 3ff19a301a7f817296eecdcc4fa0de34, 3ff19a301a7f81d889cbf635794d45d5, 3ff19a301a7f8149a474d92e593c2eb4, 3ff19a301a7f817199d3ca4259d4a19b, 3ff19a301a7f81ac9df5d3c67bf1666b, 3ff19a301a7f81c19cd2d23df82c4377, 3ff19a301a7f81dab4f9c657c9d6cf0d, 3ff19a301a7f81a5823cee75cdada5af, 3ff19a301a7f81eb8756ee0b72cbfdeb, 3ff19a301a7f81e1bf6cfe93a9700e68, 3fe19a301a7f8101bfd8ca6fe44becbd.
