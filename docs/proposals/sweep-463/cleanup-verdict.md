# Cleanup verdict: daily sweep 463c (decisions 463, 465, 456)

Cleanup session, 4 Nov 2026, about 21:40 JST. Read-only.

## Verdict: 463c accepted, 42,406 / 76b49956eea00a03

The live sweep came back inline from get_trigger, so I used the committed base, inbox-split/sweep.txt. It's 6783dd01, the hash patch.py asserts, and the trigger was last updated 1 Nov, after round 4's deploy. Running patch.py twice gives the same bytes both times, equal to sweep.txt.

The diff covers:
- 3g: the Episode trigger since 1 Sep (Not releasing, Hold and corrupted left out), and matching by LinkedIn, else exact full name plus company.
- 3k: FT Community rows by Person only, one invite ask, and blurb report lines only for To invite, Invited or Added.
- STEP 4: the "No owner" flag.
- 3i: the transcript rows name Mamatha.
- The report lines.
3k never writes a blurb, and it caps at 15 creates a run.

## Should-fix (not blocking)

- S1. Avoid duplicate Community rows. 3k creates a row whenever no row has the guest as Person. An older row for the same person with Person empty and the same company is a name-only hit, so 3k reports it and still creates a second row. A duplicate there spreads to the public mirror and to Akshay's invite asks. Add: a name-only hit with Person empty and the same company is reported and not created; one with another Person is a different person, so create. In the 30-guest audit this only touches Saket Saurabh, where creating is right. Not urgent.
- S2. The "In WhatsApp group" checkbox that the audit flags is owned by no routine. Retiring it is Akshay's call, under decision 459.
