"""Decisions 411 to 413 (as amended) and the send-logging order folded into the Zoya split release build (CTO, 26 Oct 20:31 JST).
Usage: python3 docs/proposals/d-split26l.py (repo root), then routines/zoya/build.py. Base: d33ef96 (Cleanup's d-split26k-fix in).
1/ 412: SLOW INTERNAL TASKS c(4) no longer attaches a transcript, never waits for one, and drafts the FT thank-you as a standalone
   new mail To the guests, Cc the PR, every other stakeholder and the house copies (Cleanup's 412 finding on d33ef96).
2/ 411: recording status is settled from our side only; an unclear one goes in Akshay's Notion queue on that Engagement;
   every action due from Akshay goes there, never WhatsApp. Shared part notion-data (FAST and SLOW).
3/ 413: themes and flow come from our side (mail b, FAST and SLOW); the draft read-back checks To and Cc cover everyone on the
   latest inbound (Krsnaa lost Mamatha at 17:40; Sreepriya's reply at 15:41 lost four people). Mamatha: kept where she is on the
   latest inbound, never added; whether the house copies should add her where absent is a question to the CTO, not decided here.
4/ Send logging: every Email out Activity carries the sent body. The 17:40 Krsnaa "double copy" was one send (one Message-ID;
   the provider's IMAP copy at 08:40:20Z and Gmail's SMTP copy at 08:40:41Z), so MESSAGE IDENTITY says copies are not sends."""
def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:60], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
P = "routines/zoya/parts/"
edit(P + "internal.txt", [(
 "(4) Thank-you: if the row has a thank-you draft (\"Zoya drafted: FT thank-you\" or \"Zoya drafted: client thank-you\" Activity), "
 "attach the .txt to that draft in ad@thepodium.in (MCP Emails draft) and read the draft back to confirm the attachment; Founder Thesis "
 "with no draft and no thank-you in Akshay's Sent: create the draft in ad@thepodium.in the way the calendar's STEP 4c does (approved "
 "\"FT thank-you after recording\" wording in Akshay's voice, To the guest and the main PR, Cc every other Stakeholder and the house "
 "copies), the .txt attached, read back, log \"Zoya drafted: FT thank-you for <guest>\". Then make sure Akshay's Next action has "
 "\"Akshay: send the thank-you draft to <guest first name> (transcript attached)\".",
 "(4) Thank-you (decision 412): it never waits for a transcript and carries none; never attach the .txt to a thank-you draft. Founder "
 "Thesis with no \"Zoya drafted: FT thank-you\" Activity and no thank-you in Akshay's Sent: create the draft in ad@thepodium.in as a "
 "standalone new mail, never a reply on the PR thread: approved \"FT thank-you after recording\" wording in Akshay's voice, subject "
 "\"Next Steps | <guests> @ <company> <> Founder Thesis\", To the guests, Cc the PR, every other Stakeholder and the house copies, no "
 "attachment; read back, log \"Zoya drafted: FT thank-you for <guest>\". Then make sure Waiting on has Akshay and Next action has "
 "\"Akshay: send the thank-you draft to <guest first name> (draft ready)\".")])
edit(P + "notion-data.txt", [(
 "Once his Your call answers the ask, hand the step on and take him off.",
 "Once his Your call answers the ask, hand the step on and take him off. Every action due from Akshay goes here, on its Engagement, "
 "never on WhatsApp (decision 411). RECORDING STATUS (decision 411): whether a recording happened is settled from our side only: the "
 "calendar event, Zencastr, a transcript, Akshay's mail or WhatsApp. Never ask the guest, PR or anyone outside the team, and never "
 "write \"Zoya: confirm with <PR>\". Still unclear: once, Akshay in Waiting on and the segment \"Akshay: did the <D Mon> recording "
 "with <guest> happen? Write yes or no in Your call\".")])
edit(P + "mail.txt", [(
 "edit notes, recording logistics, \"any update?\").",
 "edit notes, recording logistics, \"any update?\"). Themes and flow of the conversation come from our side (decision 413): precall "
 "notes, eval and dossier, in the show's angle; PR talking points are input only; no precall notes: a draft to Akshay first; never "
 "revenue figures or call confidences.")])
edit(P + "sending.txt", [
 ("read the draft back (To, Cc and that it is a reply on that thread)",
  "read the draft back (that it is a reply on that thread, and that To and Cc together hold everyone on the latest inbound, To and "
  "Cc, less bounced addresses and Akshay's other addresses, plus Akshay: decision 413)"),
 ("never Mamatha;", "never add Mamatha (keep her only where she is on the latest inbound);"),
])
edit(P + "identity.txt", [(
 "any hit means it is logged, so add only a missing link.",
 "any hit means it is logged, so add only a missing link. Two Sent copies with one Message-ID are one send (the provider files its "
 "own copy). Every Email out Activity carries the sent plain-text body in its page body.")])
print("d-split26l applied")
