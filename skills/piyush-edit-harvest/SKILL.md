---
name: piyush-edit-harvest
description: Turn Piyush Goenka's edits on a draft into permanent improvements to the drafting skills, so his editing burden falls over time. Trigger on "/edit-harvest", "harvest this edit", "what did Piyush change", "learn from this revision", "diff Piyush's edit", "Piyush sent back changes", or whenever Akshay pastes a draft that contains Piyush's revised version with the original below it (the agreed "original-below-revised" format). Diffs the revision against the original, categorises every change (fact fix, research gap, voice, structure, compression, India turn), separates one-offs from recurring patterns by reading a running edit log, and proposes concrete patches to the relevant skill file (a new banned phrase, a new research requirement, a known-error entry). The point is the compounding loop Piyush asked for: his corrections feed back into the system instead of evaporating. Sibling to piyush-fact-check and piyush-research-dossier.
---

# Piyush Goenka — Edit-Harvest Loop

Every time Piyush edits a draft, the edit encodes a lesson. This skill captures that lesson and turns it into a skill patch, so the same correction never has to be made twice.

## Why this skill exists (Piyush, June 2026)

> "each one I've made changes to them.. then let that person learn from that, this is what we need, this kind of work, what was missed and what is now coming in, so that my work goes down at least over a period of time."

Piyush's complaint is not only that drafts are cursory. It is that he keeps making the *same kinds* of corrections and his editing load is not falling. He is doing the teaching; nothing is learning. This skill is the learning. It is the single highest-leverage build for the durability of the relationship, because it is the only one that bends the effort curve downward.

## The input: original-below-revised

Akshay and Piyush agreed that revisions will be returned with **Piyush's edited version on top and the original draft below it**, clearly delimited. That format exists so Akshay can spot changes. It doubles as the training input here.

Accept any of:
- A single document with the revised version, a delimiter, then the original below.
- Two pasted blocks (revised + original), in either order — ask which is which only if genuinely ambiguous.
- A tracked-changes or redlined version.

If only one version is present, ask for the other. There is nothing to harvest from a single version.

## Step 1 — Diff semantically, not just textually

Line-by-line text diffing finds *what* characters changed. This skill needs *why*. Read both versions in full, then for each meaningful change ask: what did Piyush fix, and what general rule does it imply?

Group changes; ignore pure typo fixes and trivial re-wordings that carry no rule.

## Step 2 — Categorise every change

Each substantive change lands in one of six buckets. The bucket determines which skill it patches.

| Bucket | What it looks like | Patches |
|---|---|---|
| **1. Fact fix** | He corrected a wrong fact (product truth, number, founder, date, superlative) | `piyush-fact-check` known-error list + flag the missed claim class |
| **2. Research gap** | He *added* a mechanism, a number, a founder detail, a scaling lever that should have been in the draft | `piyush-research-dossier` scorecard (raise the depth requirement) |
| **3. Voice / register** | He cut a hedge, killed an AI tell, swapped a word, changed rhythm, removed a performative turn | The drafting skill's banned-phrase table / Voice DNA |
| **4. Structure** | He reordered the spine, moved the hook, relocated or resized the India turn, changed the open/close | The drafting skill's template / hook-close patterns |
| **5. Compression** | He cut length, removed a restated point, deleted a setup paragraph | Word-budget discipline in the drafting skill |
| **6. India turn** | He sharpened, relocated, or re-weighted the India lesson; changed which Indian names appear | The Indianness rule / brand-to-India split in the drafting skill |

For each change, record: the bucket, the before, the after, and the **rule it implies** stated generally (not "he changed Olipop's date" but "exit dates are being shipped unverified — class-5 fact-check is not firing").

## Step 3 — One-off vs recurring (read the log)

A single edit is noise. The same edit three times is a rule. Before proposing patches, **read the running edit log** (`Piyush_Edit_Log.md` in the project, or wherever Akshay keeps it) and cross-reference this session's changes against past ones.

- **New pattern:** seen once. Record it; do not yet promote it to a hard rule unless it is a fact error (those are promoted on first sight — facts can't be wrong).
- **Recurring (2+):** flag it. "This is the 2nd time he has cut a soft opener."
- **Promote (3+):** recommend it become a standing rule. "3rd time he has removed 'notably' — promote to banned phrase."

Fact fixes (bucket 1) skip the patience: a wrong-fact class is promoted to a standing fact-check requirement immediately, because the downside is the Liquid Death failure.

## Step 4 — Propose patches

For each pattern worth acting on, write a ready-to-apply patch. Name the target skill, the exact section, and the exact text to add or change. Make them copy-paste-able so Akshay can install them (or so they can be applied with a one-line `str_replace`).

```
PROPOSED PATCH 1 — [target skill]
Section: [where it goes]
Change: [add / replace]
Text:
  [the exact line(s) to add]
Reason: [which edit(s) drove this — cite the log if recurring]
Status: [new / recurring 2x / PROMOTE — recurring 3x]
```

Do not over-propose. A clean edit with no general lesson produces no patch — say so. The goal is signal, not a patch for every comma.

## Step 5 — Append to the log

Every harvest appends this session's categorised changes to `Piyush_Edit_Log.md` so patterns accumulate across weeks. Emit the lines to append in a code block for Akshay to paste (the log is canonical and Akshay-maintained; this skill reads and proposes, it does not silently rewrite the record).

Log line format:
```
[date] | [post / brand] | [bucket] | [before → after] | [implied rule] | [count]
```

## Step 6 — Output

```
EDIT HARVEST — [post / brand] — [date]

CHANGES BY BUCKET
1. Fact fix — [before → after] — implies: [rule] — [new / recurring]
2. Voice — ...
   (etc.; omit empty buckets)

RECURRING / PROMOTE
- [pattern] — seen [N]x — recommendation: [promote to X]

PROPOSED PATCHES
[patch blocks]

APPEND TO Piyush_Edit_Log.md
[code block of log lines]
```

## Important behaviours

- **Generalise, don't memorise.** The output is rules, not a list of specific corrections. "Exit prices ship unverified" is useful; "the Olipop number was off" is not.
- **Fact fixes are the priority signal.** They feed `piyush-fact-check` and they promote on first sight. If Piyush is still catching facts, the fact-check gate is not firing or not covering that claim class — say so plainly.
- **Watch for the burden curve.** If the log shows the same buckets recurring month over month, the relevant skill patch is not being applied or not working. Flag that to Akshay directly — the whole point is that his load falls, and if it isn't, the loop is broken.
- **Respect deliberate one-offs.** Piyush sometimes makes a change specific to one brand that should not become a rule. If a change reads as brand-specific rather than general, log it as a one-off and do not propose a patch.
- **Never edit `/mnt/skills/user/` in session.** Propose patches; Akshay installs them (copy to `/home/claude/`, `str_replace`, `present_files` for paste-back).
