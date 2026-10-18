# p333 Stage B walkthroughs (CTO-20261018-2 acceptance examples)

These are constructed cases, worked against the Stage B prompt text and the MCP Emails `email_compose` schema. A `reply` goes To the sender of the anchor message and ignores `to`. `reply_all true` adds that message's To and Cc, all into To. `cc` is honoured on a reply (tested 18 Oct 07:59Z, a self-addressed reply: To was the original sender, Cc exactly as passed, `in_reply_to` set). Nothing here was sent to a stakeholder.

Names are placeholders. G = guest, P = PR contact, A = Akshay, Z = Zoya.

## Addressing (Zoya ADDRESSING, calendar TEMPLATES)

| Case | Thread, newest last | Whose move | Anchor chosen | Planned call | Derived To / Cc |
|---|---|---|---|---|---|
| 1. Normal inbound reply | P pitches; A adds Z; P asks for commercials (To A, Cc Z) | P | P's latest message | reply, reply_all false, cc [A, house copies, other stakeholders] | To P; Cc A + others. Mittal under the old rule was To P, A, Adheena with no Cc. |
| 2. Chase where the last mail is ours | P asked a question; Z replied; no answer for 3 days | P | P's latest message (Z's chase is never an anchor) | reply on P's message, reply_all false, cc [A, ...] | To P; Cc A. The old fallback "else the thread's latest message" would have anchored on Z's own mail and sent To Z. |
| 3. Guest never wrote on the thread | P pitched G; G must confirm a slot | G | none (G has no message on the thread) | send: to [G], cc [P, A, ...], subject "Re: <thread subject>", one context line | To G; Cc P, A. Threading is lost for G; context comes from the subject and the opening line. |
| 4. Latest is Akshay's intervention | P wrote; A replied personally (type 2) with Z in Cc; P must answer | P | P's latest message (A's mail is never an anchor) | reply on P's message, reply_all false, cc [A, ...] | To P; Cc A. The old rule would have anchored on A's mail and sent To A. |
| 5. No usable route | G has no address on file; the only messages are ours | G | none | none | Nothing sent; the step stays in Next action with "addressing blocked: no address for G". |

The check before sending: the anchor's From is the person whose move it is, and it is never Z, A or a team address. Logging records the To and Cc the send result returns.

## Closing work (Zoya 0f, daily-sweep 3h a)

| Case | Evidence on the page | Result |
|---|---|---|
| 6. Task left out of the checkpoint | The checkpoint lists 3 other findings; there is no entry about this AR | Stays open (omission is not completion). |
| 7. Deployed repair waiting on a real case | "deployed, read back", acceptance asks for an observed send | Stays open; status "live, awaiting observation". |
| 8. Criteria fully met | An entry cites the observed outcome the row's acceptance names | Done, with the evidence quoted. |
| 9. Authorized cancellation | Akshay or Codex records that it is cancelled | Done (cancelled), quoted. |
| 10. Owner question answered | Akshay answers an owner-mail question | Done (unchanged rule: the answer is the acceptance). |
