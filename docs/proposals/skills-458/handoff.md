# Decision 458: the Apify socials step for the guest-eval and dossier skills (4 Nov)

**What's here:**
- `apify_step.md` is the step text.
- `build.py` inserts it into each installed skill, just before the step that follows research, and asserts each anchor once.
- The patched SKILL.md files themselves aren't committed. One of them (hbd-guest-eval) carries a person's email address and a phone-like number, and this repo holds no contact details. To rebuild the upload files: `python3 build.py <installed skills dir> <out>`. Akshay uploads each out/<skill>/SKILL.md. Built twice, byte-identical, from the installed copies on 4 Nov ~01:40 JST.

| Skill | Inserted before | Bytes / sha256 of the patched SKILL.md |
|---|---|---|
| ft-guest-eval | Step 3: Calibrate against the channel | 35,700 / fc0f87bf5fff6e03 |
| un-guest-eval | Step 3a: score Fit | 51,040 / 0d33fefd41aafef3 |
| bts-guest-eval | Step 3: score Satish Fit | 22,745 / ef0f6361eafa290a |
| hbd-guest-eval | Step 3: Score Audience Fit | 71,824 / a5d8c8853b3db205 |
| ft-host-dossier | Stage 2: Gap-fill | 20,556 / a08e867d3bfd5ccb |
| un-dossier | 1b. Emit the Grok prompt, then STOP | 60,297 / cc5f94d0d8cc6f8d |
| bts-host-dossier | Stage 2: Gap-fill | 28,075 / 29109130811ae691 |
| hbd-host-dossier | Phase 1b: Set the technical depth dial (after 1a's web search) | 25,937 / 93b635329528fd6c |

**The step:** if an Apify connector is loaded, the skill pulls the guest's recent posts:
- LinkedIn: the last 20 posts, or the last 12 months;
- X and Instagram: only where the profile clearly belongs to the guest, never a guessed handle.

The posts are research input only:
- They're never quoted to the guest or PR, in a mail, prep note or guest-facing page, and the output never says their socials were read.
- A fact from a post is cited as the guest's own claim.
- If there's no connector, or the actor fails, the output says so in one line and the run carries on. The step never blocks the run.

**For Akshay (UI steps):**
- Add the Apify connector to the evals task and the "Host dossiers and prep notes" task.
- Upload the eight patched skills.

**Drift to know about:** the repo's `skills/` copies don't match the installed skills. Most installed copies are newer: for example, ft-guest-eval is 34,702 installed against 29,663 in the repo, and un-guest-eval has a Discovery score the repo lacks. hbd-guest-eval has no repo copy at all. Some repo copies carry a "log the dossier in Notion" step the installed copy doesn't: un-dossier, bts-host-dossier and hbd-host-dossier. These patches are built on the installed copies, so uploading them won't undo Akshay's later edits. Those repo-only Notion-log steps aren't added. Say if they should be, and I'll fold them in. `skills/` should then be refreshed from the installed copies, after removing contact details.

**Status:** built. Nothing is uploaded or deployed.
