# GitHub lock feasibility (26 Oct 2026)

Test routine "TEST lock feasibility (delete after)", trig_0198DiGddneFcwahiUgg8QXx. Akshay attached founderthesis/business-os in the routine settings with the trigger set to API. The CTO fired it once manually: run cse_01TJiiHWDXYe4sEUo2N8Fcu4, completed 15:20Z, cost USD 0.15 at list price. The routine was disabled afterwards. Its evidence is kept.

**Operation tested** (from inside the routine):

    git push --porcelain origin "+<new>:refs/heads/zoya-lock-test" --force-with-lease="refs/heads/zoya-lock-test:<expected>"

Two pushes ran concurrently in each round, with the same expected sha. Origin was https://github.com/founderthesis/business-os, with no credentials in the URL.

| Round | Expected | Winner (exit 0) | Loser (exit 1) | Final ref |
|---|---|---|---|---|
| 1 | 8c457bb | A 07f0fd5 (forced update) | B 80e50e8: [remote rejected] cannot lock ref ... is at 07f0fd5 but expected 8c457bb | 07f0fd5 |
| 2 | 07f0fd5 | A dcd826f | B 76882db: [remote rejected] ... is at dcd826f but expected 07f0fd5 | dcd826f |
| 3 | dcd826f | A 30068e1 | B b00b28d: [remote rejected] ... is at 30068e1 but expected dcd826f | 30068e1 |

The CTO read the ref back independently: refs/heads/zoya-lock-test = 30068e1 ("routine A3").

**Observations**
- The rejection is server-side ("remote rejected ... but expected"). That is GitHub's compare-and-swap on the ref.
- A won all three rounds, possibly because of launch order. The CTO's own earlier run from a cloud session saw both A and B win.
- Every push printed a harmless "push negotiation failed; proceeding anyway" warning.
- Deleting a branch is refused (HTTP 403 from the CTO session). So the lock ref must persist and flip between free and held commits, each flip guarded the same way.

**Not demonstrated**
- Fencing of a paused holder: Notion writes and MCP Emails sends don't check any token. Hence the fail-closed design, with no automatic expiry or takeover.
- Protection for any routine without this repo attached.
