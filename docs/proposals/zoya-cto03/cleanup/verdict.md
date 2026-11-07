# Cleanup verdict: Zoya CTOA-03 build b (99cc04e), 2 Nov ~17:10 JST

This covers the changed behaviour only.

**Accepted. No blocker.** Deploy `zoya-cto03/zoya-one.txt`, **43,999 / 775b9ed879af33db**. The SLOW pin stays at f70901f.

## Rebuild and base

- **The rebuild works with one patch, not two.** I built in a worktree at f70901f with `build_one.py <dir> refs/heads/zoya-slow-pin f70901f6f07d4a6610fda60132b4cdbb5ac43979`, twice. It came out 43,999 / 775b9ed879af33db, byte-identical to the repo.
  - That's with `zoya-cto03/build_one.patch` alone. The handoff's two-patch step fails: `git apply` rejects the second patch, because the cto03 patch already contains the rules-read hunk.
- **Base:**
  - The unpatched build at f70901f is 42,109 / 23551dc5bb4a0d12.
  - The rules-read patch alone gives 42,427 / b59636bece095323.
  - The live Zoya trigger (trig_01UPT8LDrBDL5JQqW91Awgbo), read back at about 16:45, carries deployment reference "zoya-one ec22d74d84be" and has no rules-read lines. That's consistent with live = ec22d74d. I checked the content; the JSON-wrapped prompt wasn't byte-hashed.
- **SLOW pin unchanged.** `refs/heads/zoya-slow-pin` is at f70901f6f07d4a6610fda60132b4cdbb5ac43979, its file is 63,617 / fae90990931445db, and the build's SLOW output is identical.
- **The diff against rules-read** holds only the intended items:
  - PRE-SEND CHECKS;
  - GUEST EXAMPLES;
  - BOOKING LINKS;
  - the Sri and host exceptions (scope and read-back);
  - the "works" exception in PLAIN ENGLISH;
  - the deployment reference.

## The changed behaviour

**Pre-send checks 1 to 6: OK.** I looked for anything that could block sends by accident.
- **Check 5 (D8)** is now "ACTIONS' Sent check (your inbox, and ad@ less loop-ins) finds no mail that already did this action". The loop-in can't match, and ACTIONS' existing check already drops anything that "plainly does something else". The ad@ part only stops a mail that Akshay's own ad@ mail already did, which is right.
- **Check 2 (D9)** says "no inbound yet: the row and the thread's last message". A first mail or a chase has a source, so nothing blocks.
- **Check 4** reads only the row's Your call, Next action and Waiting on.
- **Check 1** is the one to watch.
  - Rules for Zoya now fetches at **64,920 characters** (measured today), which the connector saves to a file. The new "read each page in full ... from that file in slices" covers that.
  - But if a run decides the page wasn't loaded in full, every action that page governs is blocked, and that's nearly every send.
  - It isn't a blocker: the rule tells the model how to read the file, and the run record will now name each page and its size.
  - **After deploy:** the first run's record should list Rules for Zoya with a size near 65,000 characters, and no "rules not loaded".
  - Splitting the page (`docs/proposals/rules-for-zoya-split.md`) would remove this risk.

**Sri kept, or added back, when he wrote: OK.**
- The read-back now excludes "on un#, Sri unless he wrote on the thread himself (Akshay, 2 Nov: then he is added back if missing)".
- The un# scope line agrees ("unless he wrote on that thread himself: then he stays in Cc"), and the host line does the same for Satish and Arjun.
- Bounces, handovers and Akshay's other addresses are unchanged.

**GUEST EXAMPLES inside SHOW CHECK: OK.**
- "on a client show only names its pitch sheet allows (SHOW CHECK)".
- No "recent" unless released in the last 90 days.
- "none verified: name none" means it can drop an example but never blocks a send.

**BOOKING LINKS inline: OK.**
- The link sits in the same `<p>` and plain-text line ("any open slot here works: podm.in/30min").
- The PLAIN ENGLISH ban on "works" has the matching exception, and the hard rule holds "whatever PLAIN ENGLISH says".
- The wording page edit (item 8) is still the CTO's to make in Notion.

## D1 (SLOW text): not a blocker

The SLOW file still has the old Sri and "works" text, and it wins on SLOW work. FAST work never reads it, so FAST isn't made worse: SLOW follow-ups behave as they do today until the SLOW rebuild and pin move.

## Nits

- Fix the handoff's build step: apply only `zoya-cto03/build_one.patch`.

Nothing deployed by Cleanup.
