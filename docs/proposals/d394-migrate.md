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
5. A step from Akshay's decision or Your call: `decision:call-<id of the Activity that recorded it, else the row id>:<that Claude note date>T00:00:00+09:00`.
6. Anything else (team asks, internal steps): `team:call-<row id>:<Claude note date>T00:00:00+09:00`.
7. A Zoya step inside another owner's segment ("Waiting on X ...; Zoya chases 29 Oct") becomes its own segment. These are listed for review, because they edit text another owner wrote.

Output: one reviewed file, docs/proposals/split-dryruns/keys-migration.csv (row id, old segment, new segment, key, rule, review flag). It is written to Notion in one pass at deploy, with each row read back. Under decision 341 bulk writes go direct.

Gate: the migration runs twice on the same data and produces identical files. Then FAST dry runs twice with the file treated as applied, and both runs must print the same keys and send lists (replay 1).
