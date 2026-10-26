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

The build agent's judgement calls, now fixed rules. They match what `d394-migrate-build.py` does.
1. Rule 2 also covers "<routine> chase", "<routine> follow-up", "chases" and a bare "follow-up": "sponsored chase", "sponsored follow-up", "precall chase", "chases" and bare "follow-up" (by Status) count as rule 2. When the wording names no routine, Status picks it: Sponsored offered 1, Precall requested 2, Booking 3, Recorded 5.
2. Rule 3 also covers revisit, re-approach and LT check-in steps on LT chase rows: LT chase revisit wording counts as rule 3. Rule 3 takes its date from rule 2's chain (the segment's "on <D Mon>", else "original due", else the row's Next date). n comes from Activities only, never from the wording (Mohit Bedi stays n=1).
3. A rule matches the step's own instruction, never a past-tense note inside it ("precall step 3 sent 21 Oct" is history, not the step).
4. Rule 6's date is the newest Claude note line that mentions the step, else the newest line.
5. A reply owed to an ask raised on WhatsApp keys as `reply:call-<WhatsApp Activity page id>:<its Date in +09:00>` (the Activity with Source ID `wa:...:<date>` linked to the row). Mandar's Zoya step is wholly the release-date answer, so ruling 8 applies to it instead.
6. A segment that only points to another row gets no key and stays as it is. "Zoya" named as the person who asked, on a transcript row, is not a step.
7. When rules overlap, the first one that matches wins (1 to 7). Cleanup to confirm, because it decides FAST or SLOW for Mukund, Tanuj and Mekin.

## Rulings from replay 1b (26 Oct)

8. A step that sends a release date once the calendar has one is a SLOW follow-up, not a FAST reply: `followup:seq-6-0:<next Monday>T00:00:00+09:00` (routine 6 release, step 0 = the release-date answer), rechecked weekly. The step keeps its wording plus " (recheck weekly)". This wins over rule 4 and ruling 5.
9. A reply already answered by a later mail (Akshay's or Zoya's) is complete by match: no reply key. If that mail leaves a follow-up for Zoya, it is keyed by rule 2 (routine 4 misc chase when no other routine fits), dated as the step says.
10. A segment whose key is already completed by match is dropped: empty new segment, no key, rule "done by match".
11. Kind Task rows on the AD Personal show are out of scope; FAST never reaches them, so they are not in the migration file.
12. The write also sets Waiting on and Next date where the file says so: `waiting_on_add` adds Zoya to every rule 7 row whose Waiting on lacked her (OWNERS), and `next_date` sets Next date (Ankit Utreja, 2026-10-27).

First build: 155 segments and 144 keys, all unique. 34 are flagged for review. Two builds on the same data gave byte-identical output.

Second build (replay 1b and Cleanup folded in, 26 Oct): 153 segments and 142 keys, all unique. 32 REVIEW flags and 19 notes. Two builds byte-identical. See `split-dryruns/keys-migration.csv` and `keys-migration-notes.md`.

## Drift guard at the write (added after the second build)

Live rows keep changing between the build and the write. Three rows changed on 26 Oct alone:
- Nikita's segment was rewritten.
- SREEPRIYA NS and Kumar Abhishek gained Zoya segments.

So the write never trusts the file blindly. Right before the write, re-read every row:
- Where `old_segment` still matches the live text exactly, write `new_segment`.
- Where it doesn't match, or a live Zoya segment is missing from the file, rebuild that row by these rules, list it, and get Cleanup to look at it before it's written.

The write happens only when nothing is left unreviewed. The counts before and after are checked against the file plus the rebuilt rows.

Open for the next build:
- Drop Zoya from Waiting on where the migration removes her last segment (Ankush).
- Mithun Pangal, Priya Kumar, Gulab Patil, Rick Yvanovich and Dinesh Yadav have Zoya follow-ups but no Zoya in Waiting on. Under OWNERS, add her.
