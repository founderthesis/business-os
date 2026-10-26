# Zoya split: the lock and crash recovery, stated plainly (26 Oct, CTO 23:55 JST)

Akshay asked for two proofs. The short answers:
1. **There is no lock.** The split as built cannot guarantee that FAST and SLOW never write at once. That is an architectural blocker, and the options are below.
2. **Crash recovery has no unique handle today.** It works only while one unlogged candidate exists. A hidden key in each mail would make it exact. MCP Emails can carry one in the HTML body, but not as a header.

Production is unchanged. The current Zoya trigger (trig_01UPT8LDrBDL5JQqW91Awgbo) keeps running until a replacement is accepted.

## 1. The lock

### What the build does

Each run writes its own run record (Started), then reads the other kind's latest record. If both are Started, the earlier one holds the lease, by Notion created time. Notion stores that to the second: three Activities created in one batch all read 14:41:34Z. The later writer backs off. Each run reads again a minute later.

### Why that is not a lock

- **Notion has no compare-and-swap and no unique constraint.** Nothing makes "read, then write" atomic.
- **The scheme needs each run to see the other's record.** "Write mine, then read theirs" is safe only if every read sees every earlier write. Notion's query results come from an index. Nothing documents that a page created a moment ago always appears in the next query, and I haven't measured it. If both runs write within that window and neither sees the other, both proceed. The one-minute re-read narrows the window but proves nothing.
- **The tie-break needs both runs to see both records.** It can't help when one record is invisible.
- **Two runs of the same kind don't read each other at all.** Each kind reads only the other kind's record, so a manual re-fire of FAST beside the scheduled FAST has no lease between them. Round 4's I2b tests this.
- **The lease is only as good as its holder's timing.** A run that hangs past 60 minutes inside a tool call keeps writing after its record is closed as stale. Nothing kills it.

What does prevent a double send is not the lease:
- the action key used as MCP Emails' idempotency_key, within 24 hours;
- the Sent check before every send;
- the action key on the Activity.

Those limit duplicate mail, not duplicate row writes. Two writers can still interleave on one Engagement, and WRITE PATH's re-read narrows that without closing it.

So the tie-break is not presented as a guarantee. The lock tests (L1 to L4, I2) show the rule is followed when each run sees the other. They can't show it is exclusive.

### Options

| Option | What it is | Guarantee | Cost |
|---|---|---|---|
| **(a) One trigger owns every write** | Fold SLOW's work into FAST's runs at 10:38 and 16:38 on weekdays. One prompt, one trigger, hourly. The 10:38 and 16:38 runs also do the follow-up chains, team work and payments. | No two kinds can overlap. What remains is the same trigger overlapping itself: the scheduler starting a run while the last one is still going (not documented; production has the same exposure today), or a manual fire beside a scheduled run. A 45-minute cap on starting new rows, plus "never fire Zoya's trigger by hand while a run is live", keep runs apart in practice. They don't guarantee it. | **Size.** FAST's and SLOW's parts together are about 76 KB, against a 65,336-byte cap. Merging the shared parts saves a few KB, which still leaves us roughly 5 to 8 KB over. So (a) needs the phase 8 work first: rules read from Controls pages in chunks, and the prompt slimmed. That work was planned after the split; under (a) it comes before. The hourly runs would also stop being fast at 10:38 and 16:38, since those runs carry the follow-up load. |
| **(b) One writer, SLOW proposes** | SLOW reads everything and writes only its own run record: a list of proposed sends and row changes, each with its action key. FAST is the only writer. It executes due proposals in its next run after re-checking each. | Only FAST writes rows or sends. Same-trigger overlap remains, as in (a). | FAST must carry every rule the follow-up sends need (routines 1 to 8, nurture, team, payments), so its prompt grows to about the union, the same size problem as (a). Follow-ups go up to an hour late. Proposals can go stale between the two runs, so FAST re-checks each one, which duplicates SLOW's reads. Two prompts to keep in step. |
| (c) Schedule apart, keep two triggers | FAST skips 10:38 and 16:38 (cron "38 7-9,11-15,17-23"). SLOW runs at 10:38 and 16:38 on weekdays. Both stop starting rows at 45 minutes. | Overlap only if a run outlives its hour, which nothing enforces. Same-trigger overlap as above. | Replies wait up to 2 hours twice a day, and the weekend gets the same gaps, because a cron can't skip those hours on weekdays only. It is still "no lock", just rarer collisions. |

My recommendation: (a). It is the production model we already run (one Zoya trigger, hourly), plus everything the split added: action keys, decisions 411 to 413, the round 3 fixes, and run records. It removes the cross-kind race rather than guarding it.

Its cost is the size work. That is real work, but it was already on the plan. (b) costs as much size and adds an hour's delay. (c) only makes collisions rarer.

The remaining same-trigger risk exists today. It is closed in practice by a run cap shorter than the cron interval, and by a rule against manual fires while a run is live.

This is a recommendation for the CTO and Akshay, not a decision.

## 2. Crash B: finding the right Sent message

### What recovery has after the log is lost

- The action key, from the row's Next action segment: row, type, origin, raised time.
- MCP Emails returned the Message-ID in email_compose's response. A crash before the Activity write loses that response.
- Zoya's Sent folder.

### How the Message-ID is recovered, step by step

1. List Sent from the action's raised time onward, to the action's recipient (`email_read` search, folder sent, to = the recipient, since = raised).
2. For a reply, keep only messages on the action's thread. Their In-Reply-To or References must hold the thread's Message-IDs, which `email_read` shows.
3. For each remaining message, read its Message-ID header (`email_read` action original, decoded). Two Sent copies with one Message-ID are one send: the provider files its own copy.
4. Drop every Message-ID already on an Activity (Source ID msgid:...).
5. What is left are the unlogged sends from us to that person, on that thread, since the action arose.

### When that is unambiguous, and when it isn't

- **Zero left:** nothing was sent. The action is still due.
- **One left:** that is the send. Log it with its Message-ID and send nothing. Crash A and crash B both ended here (crash-a-recovery.md, crash-b-recovery.md).
- **Two or more left:** for example, two sends to one person on one thread on the same day, such as a reply answer and a follow-up step, both unlogged. Nothing in the mail says which action each belongs to:
  - The subject is the thread's.
  - The Message-ID is the provider's, and we can't set it.
  - MCP Emails stores no idempotency key on the message. The crash A original carries no such header.
  - Judging by content ("does what the action asks") is a guess.

  **Recovery cannot pick the right one without a handle we put in the mail.**
- **Past the 24-hour window**, idempotency_key no longer dedupes. The Sent check is the only guard, and that ambiguity is the only gap.

### What a handle could be, and whether MCP Emails can set it

| Handle | Settable? | Visible to the recipient? | Survives in Sent? |
|---|---|---|---|
| Custom header (X-Bos-Key) | **No.** email_compose has no headers parameter | No | n/a |
| Subject marker | Yes | Yes, and replies must keep the thread's subject | Yes |
| Visible body line (crash B's "bos-key:") | Yes | Yes. Unacceptable in real mail | Yes |
| **Hidden HTML comment in html_body** (`<!-- bos-key: <action key> -->`) | **Yes.** html_body is sent as given ("not sanitized") | No: mail clients don't render comments | Very likely, but **not yet tested**. The crash A and Krsnaa originals show our html_body stored in Sent unchanged, but neither carried a comment. Proving it takes one self-addressed send, which needs a posted count and Akshay's approval first |

### Until there is a handle: fail closed

With two or more unlogged candidates, recovery should send nothing and log nothing. It should flag the action for a person in the run report: "<key>: <n> unlogged sends from us to <recipient> since <raised>, can't tell which". That risks a stuck action, never a double send.

Neither fail-closed nor the hidden key is in the build today, and both would be new. Per Akshay's scope ("no new features"), they are listed here for a decision, not built.

### Status

- **Crash A, crash B:** pass. Each had one unlogged candidate.
- **Two unlogged sends to one person on one thread:** not handled, and not tested. **Blocked** on choosing the hidden key, fail-closed, or both.
