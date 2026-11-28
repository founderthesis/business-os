# Cleanup: Zoya d420 build, re-pinned to f70901f

**Verdict: ACCEPTED for deploy, on one condition: move `refs/heads/zoya-slow-pin` to f70901f before the prompt goes live.**

- Prompt (zoya-one): 42,109 B, sha256 23551dc5bb4a0d12.
- SLOW file at f70901f6f07d4a6610fda60132b4cdbb5ac43979: 63,617 B, sha256 fae90990931445db.

## Reproduced

- `build_one.py <out> refs/heads/zoya-slow-pin f70901f6f07d...` gives 42,109 / 23551dc5bb4a0d12 twice, byte-identical, and equal to `docs/proposals/d420/zoya-one.txt`.
- The SLOW file built from today's parts is byte-identical to the file at the pin. Its hash is the one the prompt checks.
- No em dashes, no leftover `@@`, and the prompt is 23,427 B under the cap.

## The condition: the pin branch

The prompt runs `git fetch origin refs/heads/zoya-slow-pin`, then `git show f70901f...:routines/zoya/release/zoya-slow-work.txt`.

Today, `git ls-remote` shows zoya-slow-pin at e20647b, which doesn't contain f70901f. A fresh routine checkout would fail the fetch-and-show, and every 10:38 and 16:38 run would end "slow work file unavailable", with no SLOW work at all.

e20647b is an ancestor of f70901f, so the fix is a plain fast-forward, with no "+" and no --force:

    git push origin f70901f6f07d4a6610fda60132b4cdbb5ac43979:refs/heads/zoya-slow-pin

Then read it back with `git ls-remote origin refs/heads/zoya-slow-pin`, which must show f70901f6..., and confirm `git show <that>:routines/zoya/release/zoya-slow-work.txt | sha256sum` starts fae90990931445db. Deploy the prompt only after that.

## Change set reviewed (e20647b to f70901f, every parts edit read)

- **Measured time:** start and end come from `date -u`. SLOW starts no new step or row at 40 measured minutes, then the run ends Partial. FAST stops at 25. Nothing else (a guess, size, context) ends a run.
- **420:** reads go only through MCP Emails. From ad@ the only send is the loop-in, through MCP Emails: no link, ad@ never in To or Cc, Zoya in Cc, an idempotency key, and none if a loop-in Activity is already on the thread. Zoya's own mail follows from her inbox.
- **421:** the loop-in wording is context-aware.
- **422:** UN# SPONSORED gets at most 2 follow-ups, counting everyone's chases. Then Unresponsive, with no nurture, revival or routine 8. Disinterest gets one thank-you and They declined.
- **424:** Zoya's attach and fold. Two Eval links: the kept row's stays, and the other goes to a Claude note.
- **Quote:** Zoya adds no quote of her own. MCP Emails quotes the thread.
- **Handover:** anyone who handed over anywhere on the thread is excluded, and the read-back fails if they're still on.

## Independent replay on this exact build (offline, no earlier verdicts shown)

- Q1 to Q5 (time), U1 and its variant (422), L1 (loop-in from ad@) and H1 (handover): all pass.
- X, with quotes:
  - no Gmail-connector call;
  - no mark-read or flag ("Never mark mail read or archive in ad@thepodium.in");
  - the only ad@ send is the loop-in (the FT thank-you in ad@ is a draft);
  - no own quote.

## Follow-ups for the next Zoya change (none blocks this deploy)

1. **M2, time stop versus holds.** Say "the 40-minute stop, like a cap, is never a hold and moves nothing" beside SLOW ORDER, the "every due row ends sent, held or blocked" line, and AFTER SEND. Otherwise a model may move leftover rows' Next date. The live prompt has the same gap.
2. **M1.** Check `date -u` before each row as well as each step. Today a run can overrun 40 minutes inside STEP 2. That's the safe direction, because the lock makes the next run skip.
3. **M4, handover.** Limit it to a PR or agency contact who handed over and hasn't written on the thread since. Never the guest, and never the latest sender. This is my 6ca1042 re-engagement amendment, which isn't in yet. Also set Via only on a PEOPLE MATCH, the other 6ca1042 amendment that's missing.
4. **M3.** Put the UN# SPONSORED disinterest rule into the prompt's UN# section and exempt it from decision 404's emoji reply. A FAST-only hour can otherwise answer "not for us" with an emoji. The 16:38 run then closes the row.
5. **L-a.** Key the loop-in on the thread's original Message-ID, not the latest, and include ad@'s Sent in the Sent sweep for loop-ins. Otherwise a failed Activity write can lead to a second loop-in.
6. **Smaller items:**
   - "stop" in STEP 0b.2 and INTERNAL c(3) should say "stop this item";
   - FAST's 25-minute stop should say Partial;
   - the 2-follow-up rule's "Cadences wins" makes the 2 configurable;
   - "Source Gmail" labels on MCP Emails sends;
   - Drive isn't in the ToolSearch list;
   - the house-copies wording against the loop-in's "ad@ never in To or Cc".

Checks:
- Less text and fewer writers: still one writer.
- Selection by prefix or wording: none added.
- Retry double-send: covered by the lock, action keys and the Sent check, apart from L-a.
- Bytes and hashes: above.
