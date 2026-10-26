# Keying migration for the split (decision 394), run once at deploy

Why: replay 1 failed because FAST inferred keys from wording at pickup, and two runs disagreed (149 vs 154 keys, different step numbers and types). This migration keys every open old-format Zoya segment once, from fixed rules, before FAST and SLOW go live. After it, FAST only keys a segment written later in the old form, and SLOW keys its own STEP 2 follow-ups (d-split26d).

Input: the open in-scope Engagements, each with Next action, Waiting on, Next date, Chase step, Claude note, Activities and threads. Read-only.

Rules, applied in order to each "Zoya:" segment:
1. "Zoya: back to Akshay on ..." (snooze): no key; it keeps its form.
2. Follow-up wording ("<routine> step n", "sponsored step", "precall step", "recording step", "form chaser n"): `followup:seq-<routine number>-<n>:<date>T00:00:00+09:00`.
   - Routine numbers: 1 sponsored, 2 precall, 3 recording, 4 misc, 5 form, 6 release, 8 revival.
   - n: the number in the wording, else Chase step + 1.
   - Date: the segment's own "on <D Mon>", else "original due <YYYY-MM-DD>", else the row's Next date.
3. Nurture wording: `nurture:seq-7-<n>:<date>T00:00:00+09:00`. n = the "Zoya sent: nurture" Activities since the nurture start, plus 1.
4. A reply or acknowledgement owed to someone who wrote: `reply:msg-<Message-ID of that inbound>:<its Date in JST>`. The Message-ID comes from a Gmail rfc822msgid lookup. If it can't be found, the segment goes on the review list, unkeyed.
5. A step from Akshay's decision or Your call (vendor Your call, billing and payment steps go to rule 6 instead): `decision:call-<id of the Activity that recorded it, else the row id>:<that Claude note date>T00:00:00+09:00`.
6. Anything else (team asks, internal steps): `team:call-<row id>:<Claude note date>T00:00:00+09:00`.
7. A Zoya step inside another owner's segment ("Waiting on X ...; Zoya chases 29 Oct") becomes its own segment. These are listed for review, because they edit text another owner wrote.

Output: one reviewed file, docs/proposals/split-dryruns/keys-migration.csv (row id, old segment, new segment, key, rule, review flag). It is written to Notion in one pass at deploy, with each row read back. Under decision 341 bulk writes go direct.

Gate: the migration runs twice on the same data and produces identical files. Then FAST dry runs twice with the file treated as applied, and both runs must print the same keys and send lists (replay 1).

## Rulings from the first build (26 Oct)

The build agent's judgement calls, now fixed rules. They match what `d394-migrate-build.py` does, except ruling 5.
1. Rule 2 also covers "<routine> chase", "<routine> follow-up", "chases" and a bare "follow-up". When the wording names no routine, Status picks it: Sponsored offered 1, Precall requested 2, Booking 3, Recorded 5.
2. Rule 3 also covers revisit, re-approach and LT check-in steps on LT chase rows. Its date comes from rule 2's chain.
3. A rule matches the step's own instruction, never a past-tense note inside it ("precall step 3 sent 21 Oct" is history, not the step).
4. Rule 6's date is the newest Claude note line that mentions the step, else the newest line.
5. An ask raised on WhatsApp keys its origin as `wa-<message key>`. This one is not in the first build: Mandar is still unkeyed and flagged.
6. A segment that only points to another row gets no key and stays as it is. "Zoya" named as the person who asked, on a transcript row, is not a step.
7. When rules overlap, the first one that matches wins (1 to 7). Cleanup to confirm, because it decides FAST or SLOW for Mukund, Tanuj and Mekin.

First build: 155 segments and 144 keys, all unique. 34 are flagged for review. Two builds on the same data gave byte-identical output. See `split-dryruns/keys-migration.csv` and `keys-migration-notes.md`.
