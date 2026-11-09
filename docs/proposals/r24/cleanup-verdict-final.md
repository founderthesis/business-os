# Cleanup final verdict: r24 accepted for deploy. Last delta (cdd4036, cd8bf35, 1556243, 3f784a6) meets every open condition

Cleanup session, 9 Nov 2026, about 18:20 JST. Read-only. 118e054 is r25 notes only and isn't reviewed here.

## The last delta, checked

- **Item 11 S1 (Next date at the earliest open segment):**
  - inbox actions 2b c sets it, through its NEXT DATE case;
  - the sweep's Form backstop sets it, as HARD's second Next date exception.
- **Item 11 S2 (no catch-up burst):**
  - routine 5 mail n is "counted from the day mail n-1 actually went (its Email out Activity), never from its due date";
  - "at most one routine 5 mail per row per run";
  - in 2b c, "a D already past becomes the next working day".
- **523 C1 (never resume):**
  - the two-week stop now removes the seq-5 segment and writes "form chasers stopped (decision 523, two weeks before release <D Mon>)";
  - "a row with that line never gets another routine 5 mail, whatever its release date does later";
  - the sweep's Form backstop and inbox actions 2b c both skip any row with that line.
- **523 S1 (one Guest forms row):** FORM PHOTO first looks for Zoya's Guest forms row on this Engagement and reuses it ("a retry never makes a second"). The note line carries the formphoto:<Message-ID> key.

Every build reproduces twice, byte for byte, equal to its commit. No em dash was added; the sweep's one is the live base's. Every prompt is under 65,536 bytes, and the hourly is 62,978, under 63,000.

## Final deploy table for r24 (in order)

| # | Routine | Bytes / sha256 |
|---|---|---|
| 1 | Calendar sync | 62,916 / c613af00ddf02c8c |
| 2 | Inbox capture | 50,431 / f64eb54edabe7326 |
| 3 | Inbox actions (with the section6-522.md paste, replacing the whole WHATSAPP CHASE block) | 48,213 / 845d0a410ce74f30 |
| 4 | WhatsApp | 32,813 / bec8c1e1acb97e08 |
| 5a | zoya-slow-pin, moved to **155624318e025766e213b8dacf62d6a632032e53** | SLOW file 93,319 bytes / **b6d1c52b86f49805**, **93,315 characters** |
| 5b | Zoya hourly | 62,978 / 459d1dd19f1b4d8a |
| 5c | Zoya SLOW task (fetches the pin sha above, expects prefix b6d1c52b86f49805 and total 93,315) | 15,949 / 595f107ffc3245e8 |
| 6 | Daily sweep | 50,569 / 2203cc3f38c60836 |
| 7 | Host boards | 8,733 / 7f5c87ab1b7883c4 |
| 8 | Host dossiers and prep notes | 6,503 / 67e07a00a19e3c60 |

Not live: Zoya episodes 49,964 / 1d23893375fe9dd2.

Skills, for Akshay to upload (skills-521):
- ft-host-dossier: 19,663 / 6739b98f16645bc5;
- pitch-builder: 57,404 / 4be1c84ec544471a.

## At deploy (CTO)

- **Read every prompt back byte for byte.** Byte-compare host boards' live base (r24/live/host-boards.txt, 5819ccf7) before pasting; I took it from the repo.
- **Section 6:** paste section6-522.md only (it supersedes section6-519.md).
- **After deploy:**
  - Notion: Deals to "Dead databases" (518).
  - The "Rules for Zoya" Saurabh exception (517).
  - The routine 5 page and Cadences already carry 523, as the CTO said; I didn't re-read them.
  - Then Akshay uploads skills-521, and stage 2 renames the property.
- **First-run checks:**
  - the first SLOW record shows "slow file: 93315 of 93315 ... sha b6d1c52b86f49805";
  - the first capture run shows RAWID ids, not NONE;
  - the first sweep Part B shows step 3p and Form backstop lines.
