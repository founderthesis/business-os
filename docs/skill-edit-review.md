# Skill edit review (decision 682)

Akshay, 26 Nov: "Allow Ranjita chat to make changes to the git hub skills. Run edits through cleanup and commit if no clashes. If there is a clash then let Ranjita know."

## The flow

1. Ranjita's chat (the Episode copywriter chat, or any chat she works in) writes the change as a unified diff against the branch tip, `git diff` of skills/<name>/ only, plus one line on why and her words asking for it. It sends both to the CTO session with send_message. It never commits or pushes.
2. The CTO starts one Cleanup chat per edit with the seed below and waits for its verdict.
3. Clear: the CTO applies the diff, adds a dated line to the skill's "## Lessons" section in Ranjita's words, commits ("<skill>: <what> (Ranjita, <date>)"), pushes, and tells her chat the commit.
4. Clash: nothing is committed. The CTO sends Ranjita's chat the clash in plain words (what it collides with, where, and the options), and she decides. A clash with a rule Akshay set goes to him instead.

Anything that changes a verdict, a price, a commercial term or who gets contacted is never committed on her word alone: it goes to Akshay first (CLAUDE.md, Skills).

## Cleanup seed

You are Cleanup, a one-shot read-only reviewer for ThePodium's Business OS. Read CLAUDE.md. Change nothing: no commit, no push, no Notion write, no send. Apply the diff below to your checkout of claude/business-os-structure-k3sqo5 with `git apply --check` and then `git apply` (locally only). Then check it for clashes against: (a) the rest of that skill's own file and its references; (b) any other skill in skills/ that calls it or that it calls, and any skill that sets a rule on the same output (grep the skill names and the key terms); (c) CLAUDE.md, routines/zoya-day.md, docs/engagement-chat-seed.md and any prompt in docs/proposals/rulebook-r1/prompts/ that names this skill; (d) the Notion Decisions database (collection://cfcc0ef3-3e83-4655-98ed-56ed950b02ec): search it for the skill name and the rule's subject, and treat a decision In force as binding; (e) the house writing rules (no em dashes, the banned words). A clash is a rule the edit contradicts, a step another file relies on that the edit removes, or a verdict, price or contact change. Style differences are not clashes. Reply with send_message to {cto session id}, one block: "VERDICT: clear" or "VERDICT: clash", then one line per clash (file or decision, the line, why), then "applies cleanly: yes|no". End with the same block here.

Diff and reason:
{diff}
