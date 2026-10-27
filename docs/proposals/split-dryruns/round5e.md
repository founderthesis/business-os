# Round 5e: "Quote what you answer" and the SLOW pin (27 Oct)

Two independent offline runs, A and B. Nothing was sent, written or pushed.

**Inputs:**
- Prompt: zoya-one 9dcc16aca3660687 (02f0ebe).
- SLOW work file: dedea9f8eb7af561.
- Scenarios: round5e/scenarios.json (ba74c4ab1b372120).

The release build is 49ba2fe (56953088cc0ddf82). It differs from 02f0ebe only in the SLOW fetch line and the version stamp, and these 11:38 scenarios never read that line.

| Scenario | A | B | Outcome both runs gave |
|---|---|---|---|
| R3 | PASS | PASS | To Sreya; Cc Akshay, Mala, Rajmohan, Santhosh; read-back passes. One quote in each body: the plain one added by MCP Emails, the html one added by Zoya at read-back. In-Reply-To and References from the inbound |
| R3H | PASS | PASS | To Sreya; Cc Akshay, Mala, Santhosh. Rajmohan is left off under the handover clause; quotes and threading as in R3 |

**Pin check (49ba2fe):** in a fresh shallow clone of the working branch, `git fetch origin refs/heads/zoya-slow-pin` gives e20647b. `git show e20647b:routines/zoya/release/zoya-slow-work.txt` hashes to dedea9f8eb7af561. PASS.

**Draft re-read and the plain quote:** both runs asked whether adding the html quote could duplicate the server's plain quote. The MCP Emails draft tool states that "a new body replaces only your text: a reply's quoted original stays below it (quote_kept)". So no.

## Open, for the CTO (not changed: the SLOW file is pinned)

The SLOW work file's SENDING doesn't carry QUOTE WHAT YOU ANSWER, and the prompt says that file wins on SLOW work. So a SLOW-work reply that answers an inbound would get only the server's plain quote, with no html quote. Examples are decision 404's emoji reply to a payment notice, and the payment thank-you.

Adding the four sentences moves the file's hash, which needs a new pin branch: a push outside this session. Choices:
- (a) Ship as is and fix it in the next change.
- (b) The CTO moves zoya-slow-pin, or adds a new pin branch, to a commit with the line, and I rebuild.

**Noted, unchanged:**
- **"Hold" against "hold exactly":** the handover clause excuses the departed contact, but nothing orders them removed. Both runs dropped Rajmohan.
- **The `<date>` format** in the two quotes may differ.
- **Via** isn't updated after a handover (round 5d note).
- **The server's plain quote** can embed an older chain.
