# Zoya: read the split Rules for Zoya pages in full (CTO, 1 Nov 18:00)

This is a small patch on the **live** zoya-one: 42,109 / 23551dc5bb4a0d12, deployment reference ec22d74d84be. It's separate from the Next action build, which stays out of this deployment, as Akshay asked.

**What changes**, in THE RULES ARE IN NOTION, FAST only:
1. A new line: "SLOW work only: Rules for Zoya: follow-ups 40b19a301a7f81999c1acd8350d59a54 (the follow-up routines and 5a nurture and revival)".
2. "Read each page in full: a fetch saved to a file for its size is read completely from that file in slices (Bash or python), never skipped; the run record names each page read and its size."

**What doesn't change:**
- The SLOW file is untouched: 63,617 / fae90990931445db at f70901f.
- So the pin stays at f70901f.

## File

| Routine | File | Bytes / sha256 | Pinned SLOW |
|---|---|---|---|
| Zoya | `zoya-one.txt` | 42,427 / b59636bece095323, reference c916797a1be9 | f70901f6f07d4a6610fda60132b4cdbb5ac43979 / fae90990931445db |

**How it was built** (twice, byte-identical):
1. `git worktree add <dir> f70901f`.
2. Check that `python3 routines/zoya/build_one.py <out> refs/heads/zoya-slow-pin f70901f6f07d4a6610fda60132b4cdbb5ac43979` reproduces the live 23551dc5bb4a0d12 there.
3. Apply `build_one.patch`, which adds the change as a FAST-only VARIANT, and build again.

The diff against live is the two lines plus the deployment reference.

**Deadline:** this has to be live before Monday's 10:38 SLOW run, which Akshay will use to verify it.

**Note:** the main page is still about 64k characters. A fetch of that size can also come back saved to a file, so the second sentence covers the main page too, not just the child page.
