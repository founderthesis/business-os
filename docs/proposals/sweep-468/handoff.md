# Sweep 3g: recorded guests are never removed from the guest list (Akshay, 6 Nov)

Akshay on the FT guest list audit page, 6 Nov: "not releasing folks continue to be in the guest list - as a rule. Don't remove them. As long as I recorded - they count as past guests." and "keep them in the list. The list is a flex" (Karmendra Kohli, Not releasing; Matthew Spacie, Magic Bus, corrupted recording).

Base: live sweep 43,938 / 4ef8998f (b-round-5nov/sweep.txt). Four exact replacements in STEP 3g only:
1. The exception "except an unusable recording (Not releasing, Hold, corrupted: Magic Bus stays out)" becomes "every recording counts, Not releasing, Hold and corrupted ones included".
2. "unless the Episode is Not releasing" dropped from the create rule.
3. The "rename that row REMOVE and clear Company" bullet deleted.
4. Report line: "never rename, clear or remove a guest's row"; "rows marked REMOVE" dropped.
STEP 3k (FT Community) is unchanged: its exclusion is about the community, not the guest list.

Build: docs/proposals/sweep-468/sweep.txt, 43,829 / 6e3d66067b4fee83. Deploy before the 14:00 JST Part B run.
