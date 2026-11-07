# Skills for decisions 521 and 518 (7 Nov)

**What's here:** `build.py` patches the installed skills, asserting each edit once. The patched SKILL.md files aren't committed, like skills-458. To rebuild the upload files, run `python3 build.py <installed skills dir> <out>`. Akshay then uploads each out/<skill>/SKILL.md on claude.ai.

Built twice, byte-identical, from the copies synced to this session on 7 Nov (about 15:00 UTC). No new em dash, and no email address in either output.

| Skill | What changes | Bytes / sha256 of the patched SKILL.md |
|---|---|---|
| ft-host-dossier | Stage 6 writes the Prep doc link under whichever name the row has (dual-name wording); its reply line, the calendar note and the checklist say Prep doc link | 19,663 / 6739b98f16645bc5 |
| pitch-builder | Phase 6 logs the pitch on the prospect's **Engagement on Show PaaS**, not the retired Deals database (decision 518). The published pitch link goes in the Prep doc link (dual-name), with a dated Claude note line "pitch built (<link>) (pitch-builder)". The description, the Phase 0 Notion check, the pricing gate's earlier-quote search and the Phase 5 hand-off now point to the PaaS row | 57,404 / 4be1c84ec544471a |

**pitch-builder Phase 6 in short:**
- **Find:** look for the row by Guest, Stakeholders or Organisation on Show PaaS. An old Deal's "Moved to Engagements" names its row, and two candidates means it stops and asks.
- **Status:** forward only. Interested while the pitch is built, Decision pending once Akshay says it went.
- **What it writes:** Amount; "Akshay: <step>" with Akshay in Waiting on; and the budget read and pitch summary in the page body, since Engagements has no Budget read field.
- **Create:** if there's no row, it creates one on Show PaaS at Interested. It never marks a row Booked, declined, Parked or Unresponsive.

**Unchanged:** un-dossier, bts-host-dossier and hbd-host-dossier. None of the three writes to Notion; the "Host dossiers and prep notes" routine writes their link, and that routine's r24 build uses the dual-name wording.

**Worth knowing:** the synced ft-host-dossier has no Apify step, so the decision 458 upload (skills-458, ft-host-dossier 20,556 / a08e867d) hasn't reached the installed copy. This build starts from what's installed now, so uploading it leaves 458 still missing. If Akshay wants both, he uploads 458 first and this build is re-run on that copy.

**For Akshay (UI steps):** upload the two patched SKILL.md files. The CTO renames the Notion property only after this upload and the r24 deploy (stage 2).
