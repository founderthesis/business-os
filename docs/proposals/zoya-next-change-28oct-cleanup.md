# Cleanup on the 28 Oct quote and handover diagnosis (6ca1042)

**Verdict: diagnosis accepted; proposal agreed with three amendments.** Nothing is built, so there are no hashes yet.

## 1. Quote: agreed

The diagnosis is sound. email_compose "reply" has no switch for the server quote, and "send" would break threading. So Zoya's own quote is redundant at best, and on Sent Mail 715 it broke the live "never paste one in the plain body" rule. Dropping it also settles the deferred SLOW html quote and the date-format item.

Amendments:

1. **Change Rules for Zoya first.** "Quote what you answer" is Akshay's rule (Rules for Zoya, item 14). The fix changes how it's met, not just prompt text, so the Rules page has to say the server quote meets item 14 before the prompt line goes. Otherwise the master and the prompt disagree.
2. **Keep the Gmail clause until the check is done.** Remove it only once a real ad@ reply is read back showing Gmail's own quote in both bodies.
3. **Settle Sent Mail 716 (body_html null) before the build.** If Zoya sent no html_body, that's a live breach of "every mail is sent with html_body" and needs its own fix and test in this change.

## 2. Handover Cc: agreed

Both causes are right. "The mail itself" reads only the latest inbound, and the read-back checks a minimum set, never an exclusion. The proposed wording fixes both: the departed contact is dropped, and the read-back fails if they're still on the draft.

Amendments:

1. **Re-engagement.** "Anyone who handed over anywhere on the thread" would also drop someone who handed over and later wrote again. Add "unless they wrote on the thread after their handover", and add that as a regression test.
2. **Via after a handover is a field write that other routines also make** (the inbox, the sweep).
   - Set Via only when the handover names the new contact and that person matches a People row by PEOPLE MATCH. Otherwise put it in the run report, not on the row.
   - Leave the departed contact in Stakeholders, so history keeps them.

## Tests

The four listed are right. Add two:
- the re-engagement regression above;
- on the Gmail side, an ad@ reply read back after the clause is removed.

Each test names the build's hashes and runs twice.
