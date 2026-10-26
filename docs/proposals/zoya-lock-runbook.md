# Zoya lock: setup and manual recovery (CTO only)

The Zoya routine takes `refs/heads/zoya-lock` in founderthesis/business-os before it does anything, and releases it as its last step (routines/zoya/parts/lock.txt).

The routine never expires the lock and never takes it over. A held lock stops every later run, and the work stays due. Only the CTO frees a stuck lock, by this runbook. Until then, the recovery delay is however long the runbook takes.

## Setup, once, at deploy

1. Create the ref with a "free" commit. The routine can't create it, and a branch can't be deleted afterwards, so it lives for good:

        T=$(git hash-object -t tree /dev/null)
        C=$(git -c user.name=zoya -c user.email=zoya-lock@localhost commit-tree "$T" -m "free: created by the CTO <ISO time UTC>")
        git push --porcelain origin "$C:refs/heads/zoya-lock"

2. Read it back: `git ls-remote origin refs/heads/zoya-lock`, and check the message starts "free:".
3. The production routine must have founderthesis/business-os attached. Without the repo the routine ends at once ("no repo, lock not checked") and does nothing.

## Reading the lock

    git fetch origin refs/heads/zoya-lock && git log -1 --format='%H %s' FETCH_HEAD

- "free: ..." means no run holds it.
- "held: <run id> <time>" means that run holds it. The run id is the holder's CLAUDE_CODE_REMOTE_SESSION_ID, or a synthetic "syn-..." id when the session id was empty.

## Recovery: a run holds the lock and has stopped

Work in this order, and stop wherever a step can't be completed.

1. **Name the holder.** It's the run id in the held commit's message, plus its sha (H).

2. **Get positive evidence that the holder has terminated and can't resume.**
   - Read the holder session's events with `list_events` (Claude Code Remote MCP). You need its run result event with a `terminal_reason`.
   - Only that counts. None of these is evidence: silence, the time elapsed, an idle status, a failed or empty lookup, or a missing session.
   - If the holder's id is synthetic ("syn-..."), find its session through the trigger's runs (`get_trigger` last_run, `list_sessions`), and match it by start time and the run record. Then read its events the same way.
   - **Termination uncertain: stop here. The lock stays held.** Tell Akshay that Zoya is paused, and why.

3. **Reconcile its sends.** These come before the release, because a released lock lets the next run act on these rows.
   - List Zoya's Sent from the holder's start onward. Take every message from us whose Message-ID no Activity holds (Activities, Source ID `msgid:...`).
   - Settle each one by decision 414. If exactly one unlogged candidate fits an open action on its row (same recipient and thread, after the action was raised), log it once: an Email out Activity with that Message-ID and the action key, and the action completed.
   - Anything else is held for Akshay: an "Akshay: can't tell which mail completed ..." segment naming the candidates. Never resend it.
   - Writes to Notion go through the CTO's own session (the builder's Notion writes still prompt).

4. **Reconcile its writes.**
   - Read its run record (Source ID `run:zoya:<run id>`): what it reported, and any blocked items.
   - Read the rows edited in its window: Engagements whose Claude note has a line from that date, and Activities created then.
   - A half-written row (a sent mail with no row update, or a segment changed with no Activity) is fixed by hand to match what actually happened, and noted on the row.

5. **Do the guarded release.**

        R=$(git -c user.name=zoya -c user.email=zoya-lock@localhost commit-tree "$H^{tree}" -p "$H" -m "free: released by the CTO after <run id> ended (<terminal_reason>) <ISO time UTC>")
        git push --porcelain origin "$R:refs/heads/zoya-lock" --force-with-lease="refs/heads/zoya-lock:$H"

   - If it is rejected, the ref moved, so read it again and start over.
   - Never push without --force-with-lease, and never release a lock without step 2's evidence.

6. **Record it.** Add a Change log line on the developer page's Zoya routine page: holder, the evidence, what was reconciled, and the release sha.

## What the lock does and doesn't guarantee

**Demonstrated.** One run starts business work at a time. GitHub refuses a second push of the same expected sha server-side; see lock-feasibility.md and split-dryruns/lock-tests.md. Provider dedupe holds within 24 hours of a send that carried an idempotency_key.

**Not guaranteed.** A holder that pauses (a hung tool call) and then resumes is not fenced. Notion writes and MCP Emails sends check no token. So the design is fail-closed. Nothing ever takes the lock from a holder, so a resumed holder can never meet a second writer. The cost is a paused Zoya until the CTO completes this runbook.
