# Zoya next change: two findings from the first live FAST run (28 Oct)

Read only, from Zoya's Sent Mail 715 (TCI) and 716 (Candour). Nothing was sent or changed. These go on the next-change list with the items deferred from 49ba2fe:
- the SLOW file's html quote;
- an explicit "drop the departed contact" clause;
- one date format for both quotes;
- Via after a handover.

This change also settles three of them, as set out below.

## 1. Quote

**What MCP Emails does.** The email_compose schema for action "reply" has no option to turn off the server's quote. Its parameters are body, html_body, cc, bcc, include_signature, reply_all, include_attachments and the rest; none controls quoting. On a reply, the server appends the whole chain to both bodies:
- Sent Mail 715: the plain body is 33,387 characters and the html body 40,712. The html copy is the chain as "&gt;" lines joined by `<br>`.
- That contradicts the 26 Oct finding ("plain body only, never html_body"). That test thread was a single message, so the html quote may simply not have shown there.

The only way to avoid the server quote is action "send". But "send" takes no In-Reply-To or References, so the reply would leave the thread. That isn't acceptable.

**What Zoya did on top.**
- Mail 715 has her own "On <date>, Urbashree Bayan wrote:" quote in both bodies. The rule says never paste one in the plain body, so the plain body breaks a rule that is already live.
- Her html quote holds only the latest inbound ("Please share the tentative timeline"). It doesn't hold the 23 Oct message that raised the ask ("Please let us know the episode's release date").

**Proposed:** drop Zoya's own quote entirely, as the CTO directed when the server quote can't be turned off.
- Remove QUOTE WHAT YOU ANSWER from the FAST prompt's sending rules (it isn't in the SLOW file) and replace it with one line: "MCP Emails quotes the thread below your reply itself; add no quote of your own to either body."
- Gmail replies from ad@thepodium.in are short and link-free, and Gmail's reply adds its own quote, so drop the Gmail clause too. This needs a check: confirm Gmail's reply quotes the thread before removing it.
- **What this settles:** the SLOW file's html quote and the single date format go away, because there's no quote of ours left. Akshay still sees what was asked, because the server's quote carries the whole chain, including the message that raised the ask.
- **Cost:** the chain is long (33k characters on TCI). That's what any mail client sends on reply-all, so it's acceptable.

**Open question (Sent Mail 716):** `body_html` reads back null. Either Zoya sent no html_body on that reply, or the server stored text only. This needs one look at Zoya's run record before the next change is built, since the rule is "every mail is sent with html_body".

## 2. Handover Cc (Candour, Sent Mail 716)

**What happened.**
- Saloni handed over to George on the thread (27 Oct). George's latest message (27 Oct 07:17Z, "Will check and circle back soon") doesn't mention it.
- Zoya replied To George, Cc Priyamvada, Saloni and Akshay.

**Why the read-back missed it.** There are two issues with the wording, and no step-order problem:
1. **It reads one message only.** The rule removes "anyone **the mail itself** says has handed over". "The mail itself" means the latest inbound, which is George's. The handover was in Saloni's earlier message, so it was never in scope.
2. **It sets a lower bound only.** The read-back checks that "To and Cc together hold everyone on the latest inbound ... less <exclusions>". That is a minimum set. Nothing says an excluded person must *not* be on the mail. So a read-back that finds Saloni still in Cc passes.

**Proposed wording (replaces the clause):**

> ... less your own address, bounced addresses, Akshay's other addresses, Mamatha, on un# Sri, and anyone who handed over anywhere on the thread (a message saying a new contact takes over, the new contact being on the thread since); those are dropped from To and Cc, and the read-back fails if any of them is still on the draft.

**Same change:** "Via after a handover" (deferred). When the handover names the new contact, set Via to that person on the row.

## Tests for the next change (offline, twice)

- **TCI:** a reply carries no quote of Zoya's in either body. The draft's read-back doesn't add one.
- **Candour:** the latest inbound has no handover, an earlier one does. Saloni is dropped, George is in To, Priyamvada and Akshay in Cc, and Via is George.
- **Regression:** a thread with no handover keeps everyone on the latest inbound, as now.
- **Regression:** a handover where the new contact is not on the thread drops no one. Nobody can be dropped with no one to take over.
