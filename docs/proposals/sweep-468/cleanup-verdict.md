# Cleanup verdict: sweep 468 (recorded guests stay on the FT guest list)

Cleanup session, 6 Nov 2026, about 10:30 JST. Diff-only review, read-only.

## Verdict: accepted, 43,829 / 6e3d66067b4fee83

I diffed the build against the live base (b-round-5nov/sweep.txt, 43,938 / 4ef8998f). Every change falls inside STEP 3g (characters 22,159 to 25,819 of the base), and they are exactly the four from the hand-off:
1. The Episode trigger's exception becomes "every recording counts, Not releasing, Hold and corrupted ones included (Akshay, 6 Nov: ...)".
2. "unless the Episode is Not releasing" leaves the create rule.
3. The bullet that renames a row "REMOVE" and clears Company is gone. The "An Episode now Published" bullet after it is intact.
4. The closing line now reads "never rename, clear or remove a guest's row (Akshay, 6 Nov)", and "rows marked REMOVE" is out of the report.

Nothing outside 3g changed. The em dash count is the same, 1 in the base and 1 in the build. No "REMOVE" is left anywhere in the prompt.

STEP 3k is unchanged and keeps its own exclusion: "except an unusable recording (Not releasing, Hold, or corrupted: Magic Bus stays out)". That's right. 468 is about the public guest list, not the community.

## For the CTO (data, not the prompt)

- **Three rows on the guest list are already named "REMOVE"** with Company cleared (4a94598a13b14ab59ef953eb6b1aa6a7, 906395ecbe9c48dd84c290a70c2b51e6, 40719a301a7f8106b613e45d989da0b6). None changed in the last 7 days. The old 3g bullet renamed only Not-releasing guests, so if that's what these are, today's rule means restoring them: read each row's name from version history before 30 Oct, then restore Guest and Company. Karmendra Kohli and Matthew Spacie are on the list under their own names already.
- **One thing to put to Akshay:** the list's Status is computed as Released when Episode has a link, else "Releasing soon". A Not-releasing or corrupted guest now shows "Releasing soon" on the public page forever. If that matters, the fix is in the database's formula or the public view, not in the sweep.
