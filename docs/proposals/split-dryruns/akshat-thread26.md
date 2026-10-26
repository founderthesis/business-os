# Akshat dry run on d-thread26 (26 Oct, read only)

Row: Akshat Khandelwal @ NuFlower and GoEarnest (3f019a301a7f81ef81a4c4780c92fee2), Sponsored offered.
Segments: A "Waiting on Jheel (Impactkey PR): reply to the sponsored commercials (sent 26 Oct)" (Guest or PR); B
"Akshay: confirm your India travel plans with Akshat ... (original due 2026-10-29 ...)" (Akshay). Next date 2 Nov.

| Simulated run | Selected | Send | Row writes |
| --- | --- | --- | --- |
| Today 26 Oct | nothing (Next date 2 Nov) | none | none |
| 29 Oct | B, only through OWNER MAIL's age rule (raised 25 Oct, over 3 days) | owner mail to Akshay | "mailed" line; A untouched |
| 2 Nov | A, routine 1 step 1 (reply on the commercials thread, To Jheel, Cc Akshay; draft, read back, send) | one | Chase step 1, Zoya added, A replaced, B kept verbatim |

Verdict: FAIL, narrowly. Segments stay separate and completing one keeps the other (AFTER SEND, OWNERS, STEP 2's
independent-ask rule), but no rule gives B its own date: selection is row-level and only snoozes carry segment dates.
Fixed in d-segdates26.py (dated segments, Next date = earliest open segment date). Re-run after the fix: pending.
