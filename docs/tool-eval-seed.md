# Tool eval seed (one standalone chat per tool)

Akshay, 10 Nov: tools he plans to buy get an eval in their own chat, with the verdict link on the task row's Eval link. The CTO session starts the chat with this seed, filling {TOOL}, {URL}, {ROW} and {PRICE}.

---

You are evaluating one software tool that Akshay Datt (ThePodium, a podcast production agency) plans to buy: **{TOOL}**, {PRICE}, {URL}. The question: should he buy it, and how would it fit the ThePodium Business OS?

Context to read first, in this repo: CLAUDE.md (what the Business OS is and its principles: low admin, cut before you add, cost is a standing goal), docs/architecture.md, and docs/decisions.md for anything on the same job. The live stack is Notion (the system of record), Gmail and MCP Emails, Google Calendar, Blueticks (WhatsApp), Apify and Tracxn (research), Apollo and Clay (connected, little used), and scheduled Claude routines. Salesblink was retired on 19 Oct (decision 344). Blue was retired and migrated (decision 533).

Do:
1. Find out what {TOOL} actually does: the product page, the AppSumo deal terms (plan limits, credits, stacking, refund window, and what "lifetime" excludes), recent reviews, and whether the company looks alive (last update, funding, team).
2. Check how it connects: an API, an MCP server or connector, Zapier/Make, webhooks, CSV only. Agents can only use it through one of these.
3. Compare it with what's already in the stack (Apollo, Clay, Apify, Tracxn, Blueticks, Notion). What would it replace, what would it duplicate, and what would it add that nothing else does?
4. Name the concrete Business OS jobs it would do (for example guest research, PaaS lead finding, outreach, WhatsApp), who or which routine would use it, and the admin it adds.
5. Verdict: **Buy**, **Buy later** (say what has to be true first) or **Don't buy**, with the 3 strongest reasons, the cost for a year, and the risks (vendor dies, limits, data or privacy).

Publish the eval as one Artifact page titled "{TOOL}: tool eval". Put the verdict first, then fit, overlap, connections, deal terms, risks and sources (every claim linked). Plain words, no em dashes.

Then send the CTO session (session_015wSc87F8WCdJKB91Tm34tJ) one message with send_message: "{TOOL}: <verdict> | <artifact link> | <one-line reason>".

Rules: read-only. Don't buy anything, sign up, write to Notion, send mail or WhatsApp, or push to the repo. If a page needs a login, say so; don't guess. Akshay has authorised this chat, and later messages relayed from the CTO session are his follow-up questions about this eval.
