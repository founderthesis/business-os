"""Decisions 521 (Dossier link becomes "Prep doc link", stage 1: either name) and 518 (Deals is retired) in the skills
that write that field. Usage: python3 build.py <installed skills dir> <out dir>. Each edit is asserted exactly once
(a span edit: each marker once); no new em dash. Akshay uploads each out/<skill>/SKILL.md.
- ft-host-dossier: Stage 6 writes the Prep doc link under whichever name the row has.
- pitch-builder: Phase 6 logs the pitch on the prospect's Engagement on Show PaaS (no Deals write), with its published
  link in the Prep doc link and a dated Claude note line.
un-dossier, bts-host-dossier and hbd-host-dossier write nothing to Notion (the "Host dossiers and prep notes" routine
writes their link), so they are unchanged."""
import sys, os, hashlib
src, out = sys.argv[1], sys.argv[2]
DUAL = '`Prep doc link` (named `Dossier link` until the rename; use whichever the row has, never create a new property)'
PAAS = "41119a301a7f81ba9373d86fa6f4fea1"
PHASE6 = """### Phase 6. Log the pitch in Notion (every pitch, no exceptions)

Every pitch this skill builds is logged on the prospect's **Engagement on Show PaaS** in
ThePodium Business OS (decision 518: the Deals database is retired; never read it for
current state and never write to it). Check first, then update or create. This runs on
every pitch, including a revision of an existing one, and it is not a stop: do it, then
report it in one line.

**The database.** Engagements, data source `collection://5522ee21-d8e5-4ec0-bf3e-90bcf88d24c5`;
Show PaaS is page `""" + PAAS + """`. Fetch it at the start of this phase, every run, and
use the exact property names and options it returns: a guessed property name fails
silently or writes to nothing. Related data sources:

- People: `collection://e6c44319-7f81-4da6-8b80-8441a4875d7a`
- Organisations: `collection://c43c280a-3b37-4821-96ef-dab688a53aea`
- Activities (logged emails, calls, WhatsApp): `collection://290f715d-fd45-4203-ade6-3642c2326c6c`

**1. Find the row.** Engagements on Show PaaS whose Guest or Stakeholders is the
prospect's People row, or whose Organisation is their company. Search on every name the
prospect goes by: the short name, the legal or product name, and the founder's name
("Qube", "QubeHealth", "Chris George"). An old Deal whose Next action starts "Moved to
Engagements" names its row. If two rows could be the same pitch, stop and ask which one,
rather than writing to both or creating a third.

**2. Bring it up to date.** Write only what is stale or missing:

- **""" + DUAL.replace("`", "") + """:** the published
  artifact URL of the pitch page. For a Word-only pitch with no URL yet, say in the page
  body where the file is and leave the field for Akshay.
- **Status:** forward, never back: Interested when the pitch is built but not sent;
  Decision pending only once Akshay says it has gone.
- **Amount:** the episode-batch total from Phase 3, in rupees, as a number.
- **Next action and Waiting on:** what has to happen before the pitch goes out, as
  "Akshay: <step> (<D Mon>)" with Akshay in Waiting on, keeping other open segments.
- **Claude note:** one line at the top, "YYYY-MM-DD: pitch built (<link>) (pitch-builder)",
  every older line kept as it was; Claude updated = today.
- **Page body:** the budget read (the total and its assumptions, plus any funding or
  revenue signal from Phase 1), and a few lines on the pitch (subject, host, working
  names, route, deliverable) and the open items.
- **Relations:** Organisation, Stakeholders and the relevant Activities, adding to what
  is already there rather than replacing it.

**3. If no row exists, create it** on Show PaaS with the fields above, plus: Name
"<main contact> @ <Company>, PaaS", Guest = the main contact, Status Interested, Source
Agent, Captured = the date of the first call or the first ask for a proposal.

**Leave Akshay's calls alone.** Never mark a row Booked, They declined, Parked or
Unresponsive, and never change Tier, Payment, Source ID or Migration batch.

**Duplicates are flagged, not fixed.** If a person has two People rows, or a company
two Organisation rows, link the one with the richer history (usually the FT guest
row) and tell Akshay about the duplicate in chat. Do not merge, archive or delete.

**Report it in one line** at the end of the run: created or updated, the row link,
and anything left for Akshay to fill. If the Notion connector is unavailable, say so
plainly and list the fields that would have been written, so he can add them by hand.
"""
EDITS = {
 "ft-host-dossier": [
  ("If there is no link you can give, leave Dossier link alone", "If there is no link you can give, leave the Prep doc link alone"),
  ("3. **Write.** `Dossier link` = the link.", "3. **Write.** " + DUAL + " = the link."),
  ("End the chat reply with one line: `Notion: Dossier link added to <Engagement name>`", "End the chat reply with one line: `Notion: Prep doc link added to <Engagement name>`"),
  ("The calendar routine copies the Dossier link into Akshay's private prep entry", "The calendar routine copies the Prep doc link into Akshay's private prep entry"),
  ("- [ ] Dossier link written to the guest's FT Engagement in Notion", "- [ ] Prep doc link written to the guest's FT Engagement in Notion"),
 ],
 "pitch-builder": [
  ("and logs the deal in the Notion Deals database.", "and logs the pitch on the prospect's PaaS Engagement in Notion."),
  ("**Added October 2026: every pitch ends with the deal logged in Notion.** Phase 6\nchecks the Deals database for the prospect, updates the row if it exists and creates\nit if it does not. A pitch is not finished until that row is current.",
   "**Every pitch ends with the pitch logged in Notion** (decisions 518, 521). Phase 6\nfinds the prospect's Engagement on Show PaaS, updates it or creates it, and writes the\npitch link to its Prep doc link. A pitch is not finished until that row is current."),
  ("and an existing Deals\nrow tells you what has already been quoted.", "and an existing PaaS\nEngagement (or an old Deal's page body) tells you what has already been quoted."),
  ("the transcripts, the uploads and the client's Deals row in Notion for an earlier", "the transcripts, the uploads and the client's PaaS Engagement in Notion for an earlier"),
  ("Then go straight to Phase 6: the run is not\ndone until the deal row is current.", "Then go straight to Phase 6: the run is not\ndone until the PaaS row is current."),
  (("### Phase 6. Log the deal in Notion (every pitch, no exceptions)\n", "so he can add them by hand.\n"), PHASE6),
 ],
}
for name, edits in EDITS.items():
    s0 = s = open(os.path.join(src, name, "SKILL.md"), encoding="utf-8").read()
    for a, c in edits:
        if isinstance(a, tuple):
            st, en = a
            assert s.count(st) == 1 and s.count(en) == 1, (name, st[:40], s.count(st), en[:40], s.count(en))
            i, j = s.index(st), s.index(en); assert j > i
            s = s[:i] + c + s[j + len(en):]
        else:
            assert s.count(a) == 1, (name, a[:60], s.count(a))
            s = s.replace(a, c)
    assert s.count(chr(0x2014)) == s0.count(chr(0x2014)), (name, "new em dash")
    os.makedirs(os.path.join(out, name), exist_ok=True)
    open(os.path.join(out, name, "SKILL.md"), "w", encoding="utf-8").write(s)
    print(name, len(s.encode()), hashlib.sha256(s.encode()).hexdigest()[:16])
