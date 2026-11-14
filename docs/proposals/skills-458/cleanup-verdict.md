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

## Addendum: decision 459 (4 Nov)

**Finding:** the handoff's "For Akshay (UI steps)" hands work to Akshay in a doc. Under decision 459 it has to be one Kind Task row, which the CTO creates. Proposed row:

- **Name:** "Akshay: Apify socials in the guest-eval and dossier skills (decision 458)"
- **Kind:** Task. **Waiting on:** Akshay. **Task state:** Handed over. **Source ID:** "cto:2026-11-04:apify-skills-458".
- **Next action:** "Akshay: add the Apify connector to two tasks and paste one step into 8 skills. Steps: <this row's link>"

**Page body:**

- **Why:** decision 458. The eval and dossier skills read the guest's own posts as research input. The skill edit is small, so it's pasted by hand: the patched skill files aren't committed, because one carries contact details.

- **Steps:**
  1. Add the Apify connector to the Cowork task "Founder Thesis guest evals" and to the task "Host dossiers and prep notes".
  2. In each of these 8 skills, paste the text below on its own lines, just above the heading named. Change nothing else.
     - ft-guest-eval: "## Step 3: Calibrate against the channel"
     - un-guest-eval: "## Step 3a: score Fit (1 to 10)"
     - bts-guest-eval: "### Step 3: score Satish Fit (1 to 10)"
     - hbd-guest-eval: "### Step 3: Score Audience Fit (1 to 10)"
     - ft-host-dossier: "### Stage 2 — Gap-fill (3-6 targeted searches)"
     - un-dossier: "## 1b. Emit the Grok prompt, then STOP"
     - bts-host-dossier: "### Stage 2 — Gap-fill"
     - hbd-host-dossier: "#### Phase 1b: Set the technical depth dial"
  3. Write "done" in Your call. The CTO checks one eval's output for the "Socials" line and closes the row.

- **Paste text** (from `apify_step.md`, word for word, with Cleanup's wording fix in "anything guest-facing"), in a code block:

  > **Socials (Apify, decision 458).** If an Apify connector is loaded (its tools name Apify actors; find them with ToolSearch "apify"), pull the guest's own recent posts as research input:
  > - LinkedIn: their last 20 posts, or the last 12 months, from the profile URL found above.
  > - X and Instagram: the same, only where a profile clearly belongs to the guest (linked from their site or LinkedIn, or the same name and company). Never guess a handle.
  >
  > Use them to read what the guest talks about now, what they repeat and what they avoid, and any recent news they posted first. They're research input only. Never quote a post to the guest or their PR, in a mail, a prep note or a guest-facing page, and never write in anything guest-facing that you read their socials. A fact from a post is the guest's own claim until another source confirms it, so cite it as "their LinkedIn post, <D Mon YYYY>". No Apify connector, or the actor fails: say so in one line in the output and carry on with web search; never block the run on it.

  If Akshay prefers to upload whole files instead, a session that has the installed skills runs `python3 build.py <installed dir> <out>` (hashes above) and attaches the eight files to the row.

**The other three builds (capture r13, calendar 454, Zoya r16):** none hands work to Akshay outside a row. Their "Akshay: ..." segments on guest rows are decision-inbox asks (decision 325), not builder handovers. Zoya r16's handoff lists Notion edits for the CTO, not for Akshay.
