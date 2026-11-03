# Cleanup verdict: Apify socials step for 8 skills (4fdbe69, decision 458), 4 Nov ~09:00 JST

**Accepted. No blocker.**

## Rebuild

`build.py` on the installed skills synced to this session (`/root/.claude/skills/synced/.../`), twice. All eight patched SKILL.md files are byte-identical to the handoff's hashes:
- ft-guest-eval fc0f87bf;
- un-guest-eval 0d33fefd;
- bts-guest-eval ef0f6361;
- hbd-guest-eval a5d8c885;
- ft-host-dossier a08e867d;
- un-dossier cc5f94d0;
- bts-host-dossier 29109130;
- hbd-host-dossier 93b63532.

`build.py` inserts the step once, before each anchor (each asserted once), and refuses a file that already says "Apify".

## The step

**What it reads:**
- LinkedIn: the last 20 posts, or the last 12 months.
- X and Instagram: only where the profile clearly belongs to the guest, never a guessed handle.

**How it's used:**
- Research input only. It's never quoted to the guest or PR (mail, prep note, guest-facing page), and the output never says their socials were read.
- A post is the guest's own claim until another source confirms it.
- With no connector, or a failed actor, the output says so in one line and the run carries on. The step never blocks.

**Should-fix:** "never write that you read their socials" is meant for guest-facing text. In Akshay's own eval or dossier, citing "their LinkedIn post, <date>" is required. Say "in anything guest-facing" so the two lines don't read as contradicting each other.

## Notes

- Akshay's UI steps remain: add the Apify connector to both tasks, and upload the eight files.
- The repo's `skills/` drift is real and worth a refresh after contact details are removed. It doesn't block this.

Nothing deployed by Cleanup.
