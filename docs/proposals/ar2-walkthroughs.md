# AR-20261018-2 commitment preservation: replay walkthroughs

The patch is docs/proposals/ar2-commitments-2026-10-18.patch. It applies after p333 Stage B v2 and AR-8 v2. It changes:
- the inbox, Zoya, calendar, WhatsApp and daily-sweep prompts: one shared WORK FIELDS and Show rule after the KIND sentence;
- the eval caller (routines/cowork-evals.md, a Cowork task on Akshay's Mac);
- the live ft-guest-eval and hbd-guest-eval skills (claude.ai account skills).

The cases below are read-only replays of Puneet Garg (Damsun Group, Founder Thesis) as of 18 Oct. Nothing was written to his row and no mail was sent.

## What happened (the failure)

- **16 Oct.** Precall. Community invite agreed on WhatsApp the next day (FT Community Invited).
- **18 Oct 02:27 JST.** Akshay's instruction was done by hand: Deal "Damsun Group" created (In conversation, Waiting on Chaandini); Zoya mailed Chaandini for a BD pitch; "don't reply to the PR contact" recorded; the verdict ask was dropped because the Deal carries it.
- **Later.** The evals caller's post-precall rerun (item 0) set Waiting on Akshay and wrote the whole Next action as "Akshay: final call after the 16 Oct precall ...". That replaced the row's other asks. The PR restriction survived only under the eval's Watch-outs, a replaceable section.

## Replays with the patch

| Case | Before the patch | With the patch |
|---|---|---|
| Eval refresh after Akshay's answer | Re-raises "Akshay: final call ..." and replaces Next action | The Claude note "Your call cleared" and the open Deal mean Akshay already answered. No verdict ask; a Claude note line records the new eval. Other segments, owners and Next date stay. |
| Eval refresh with a changed verdict | Same overwrite | Replaces only its own eval segment ("Akshay: final call after ...") and keeps the others. |
| PR restriction | Only under Watch-outs, lost on the next refresh | The caller copies "Don't reply to the PR contact; speak to Puneet directly (Akshay, 18 Oct, WhatsApp)" into "## Standing", which the skill never edits. Zoya, the inbox and the calendar read it before any mail on the row. |
| Community add | An ask segment that a refresh could drop | Its own Task row (owner Akshay, a WhatsApp addition), so a refresh cannot drop it. The FT Community row keeps Membership. |
| BD pitch | On the Deal, Waiting on Chaandini; fine | Unchanged. Its follow-up Task row links to the Deal; the guest row carries no second copy. |
| One of several asks completed | A writer could rewrite the whole field | Only the completed segment is removed, after a re-read; Waiting on keeps every other owner. |
| Same-pitch sibling | Second row "Same pitch as ..." | Unchanged, and that segment is the caller's own, so it is replaced, not added. |
| Concurrent unrelated update (e.g. WhatsApp adds a Scheduling line mid-run) | Last writer wins | Re-read just before writing; the other change stays. |
| Partial failure, then retry | The Activity exists, so a retry may skip unfinished work | Capture dedupe is per Activity; the work field is merged on retry, and the send dedupe ("Zoya sent") still blocks a resend. |
| Already-sent recovery (the Chaandini mail of 18 Oct) | n/a | Its Activity exists, so it is not sent again. |
| New Task row from WhatsApp | Show empty | Show AD Personal unless the task names a show. |

## Data repair for Puneet (after deploy, not before)

- Add "## Standing" with the PR restriction.
- Move the community add to a Task row if it is not there.
- Restore Next action to the guest-conversation step.

At most 3 writes on one row and one Task create, so no bulk action.

## Deploy path

| Part | How it deploys | Who |
|---|---|---|
| inbox, Zoya, calendar, WhatsApp, sweep prompts | update_trigger with readback by hash, after Stage B and AR-8 | main |
| cowork-evals | the Cowork task on Akshay's Mac; main cannot edit it | Akshay pastes the new prompt, or Codex sends it via the owner-email gate |
| ft-guest-eval and hbd-guest-eval | claude.ai account skills; main cannot upload | Akshay uploads, or the Skills repository flow (decision 311) if it syncs |

Inbox bytes after Stage B v2, AR-8 v2 and AR-2: 65,178, so 358 spare. This is too tight to ship alone. The inbox hunk ships together with the simplification task's inbox trim, or Codex accepts 358 B.

| Prompt | Bytes after all three |
|---|---|
| inbox | 65,178 |
| zoya | 40,904 |
| calendar | 49,771 |
| whatsapp | 23,221 (repo copy with placeholders) |
| daily-sweep | 34,297 |
| cowork-evals | 18,179 |
