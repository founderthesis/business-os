# r27 (f491eda, pin 582ad08): Cleanup verdict

Cleanup, 12 Nov. This review is read-only.

**Accepted. Deploy.**

## Builds

I built every file twice and got byte-identical results each time. They match the repo copies and Main's table. The Zoya builds came from a fresh worktree at f70901f with r27/zoya/build_one.patch, pinned at 582ad08c0473dd56beb9ab794e5220f1acc72b1c.

The SLOW task carries:
- `git show 582ad08…`;
- `must start ce4d0b3f22ec8daf`;
- `total = 95,041 characters`.

All three match the file at the pin. No em dash appears in any build.

## Delta against the live r26

The delta is only three things plus their bytes. No other rule changed.

### 1. SLOW releases the lock before the :38 hourly. Meets the goal.

SLOW BATCH 3/ now defines minute 22 as "the earlier of 22 minutes after the start and :28 JST of the hour you started in, checked with `date -u` before every item, never only between chunks; no new item after it". That fixes both causes in the three runs:
- **The chunk-level check.** 14:08 and 17:10 stopped at minutes 39 and 28.
- **A late start using its full 22 minutes.** 20:12 ended at 20:35.

The stop line's python and the OUTCOME CHECK both say "minute 22 as 3/ defines it". So a :28 stop before minute 22 counts as a valid "unfinished (minute 22)", not as an unexplained stop. They agree.

**The worst case.** The last item starts by :28, and the slowest row seen is about 1.9 minutes. The record write plus RELEASE took 0.6 to 2.4 minutes. That puts the release around :32 to :33, 5 minutes ahead of the hourly.

**One edge, by intent.** A run that starts after :28 does no work: it writes its record with carryover and releases. That only happens on a start 20 or more minutes late.

LOCK and RELEASE are unchanged.

### 2. N2 no longer accepts a database read. Meets the goal, with a limit.

"After the write re-fetch the row" becomes "after the write read it again that way". "That way" points back to the first read, which already bans "SQL results, a full column included, rows mode, a preview or any slice". So the ban now covers the re-read too, with no new list. The change is in all four prompts.

In SLOW, the chk: marker must end "fetch". OUTCOME CHECK fails a chk: ending "sql", which is exactly what 20:12's S04 to S14 wrote, and marks the item unfinished.

**The limit.** The marker is what the run says about itself, so it catches an honest "sql" but not a run that does a SQL read and writes "fetch" anyway. A stronger version, worth considering later and not a blocker: N2's python prints the length of the re-fetched note, and chk: carries it.

The hourly has no chk: marker, so for it the wording change is the whole fix.

### 3. OUTCOME CHECK reads the record exactly. Meets the goal, with the same limit.

The new wording is "the fetch's text exactly, never a condensed, unwrapped or retyped copy". It names 20:12's deviation directly. It's also self-reported, so it can't be checked from inside the run.

### Bytes

The hourly's two cuts are:
- "properties from its fetch" becomes "fields from its fetch";
- "negotiation reply" becomes "negotiation" in an example list.

Neither loses anything.

## Size

All three are under the 65,536 cap.

| Build | Bytes | Headroom |
|---|---|---|
| Hourly | 62,992 | 8 under the 63,000 target |
| SLOW task | 15,652 | |
| SLOW file | 95,045 | read from git, not a prompt |

## Deploy table (after r26, which is live)

| Order | File | Bytes | sha256 | Trigger |
|---|---|---|---|---|
| 1 | Pin refs/heads/zoya-slow-pin to 582ad08c0473dd56beb9ab794e5220f1acc72b1c. The SLOW file there is 95,041 characters | 95,045 | ce4d0b3f22ec8dafe930064be39ac1eee7f8566cf09e14a324f32d01a3facd89 | ref move |
| 1 | Zoya SLOW task: r27/zoya/zoya-slow.txt | 15,652 | 856318d36558128db6028b0dd215661e4df3a89d1ad72aa469d6f1ec9468e909 | trig_015i1JzfyNDoYfrgTfbqDSXu |
| 2 | Zoya hourly: r27/zoya/zoya-one.txt | 62,992 | 839117217edc49ed1a1100bf34d261e9165bf7233dc12d1af46b62c5dcfbbfca | trig_01UPT8LDrBDL5JQqW91Awgbo |

Deploy rows 1 and 2 together. Keep the SLOW cron.

**Timing.** Deploy between a SLOW run's release and the next run's start, not while a run holds the lock. A run that started on the old pin keeps the old file until it ends.

Nothing else changes: capture, actions, WhatsApp and the calendar stay as they are. Zoya episodes isn't live.
