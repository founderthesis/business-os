"""r24 for the non-Zoya routines (CTO, 7 Nov 20:55 and 23:15 JST).
Usage: python3 patch.py <cal|sweep|cap|act|wa> <live input> <out>
Inputs are the live builds: cal r22/calendar.txt (0e755649), sweep r22/sweep.txt (51412bd9), cap r23/capture.txt
(c31d1295), act r22/actions.txt (c17734c2), wa r22/whatsapp.txt (eb41ecdd).
- Cleanup's r23 S1 (cap): RAWID counts a result with no sha256 as NONE.
- Decision 517 (cap): a pitch Saurabh forwards gets the loop-in as a reply on his forward, To him, Cc Zoya.
- Decision 518 (all five): Deals is retired. The Deal paragraphs are cut, not amended: no routine creates, updates,
  flags or links a Deal; a new production-sales conversation is an Engagement on Show PaaS under the PAAS rule.
Each edit is asserted exactly once (a span edit: each marker once, end after start); no new em dash; size cap."""
import sys, hashlib
which, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(src, "rb").read()
BASE = {"cal": "0e755649", "sweep": "51412bd9", "cap": "c31d1295", "act": "c17734c2", "wa": "eb41ecdd"}
assert hashlib.sha256(b).hexdigest().startswith(BASE[which]), "not the live %s" % which
s = b.decode("utf-8")
PAAS_SHOW = "41119a301a7f81ba9373d86fa6f4fea1"
RETIRED = ("A Deal whose Next action starts \"Moved to Engagements\" is retired: never flag, update or link to it; use its Engagement.",
           "DEALS IS RETIRED (decision 518): never create, update, flag or link a Deal; a moved Deal's Engagement is on Show PaaS (its Next action \"Moved to Engagements <link>\"), and a new production-sales conversation is an Engagement on Show PaaS (" + PAAS_SHOW + ").")
ACT_SCHEMA = ("Engagement, Deal, Episode, Template", "Engagement, Episode, Template")
DEALS_DB = (("- Deals (selling our production service): collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a\n", "Organisation, From engagement, Source, Source ID\n"), "")
NEW_LEAD = ("when you create a new Engagement (or Deal),", "when you create a new Engagement,")
CHANGE = ("- Every Engagement or Deal you change:", "- Every Engagement you change:")
EDITS = {
"cap": [
 RETIRED, ACT_SCHEMA, DEALS_DB, NEW_LEAD, CHANGE,
 ('if o.get("sha256") and hashlib.sha256(b).hexdigest()!=o["sha256"]:print("NONE sha256 mismatch");sys.exit()',
  'if not o.get("sha256") or hashlib.sha256(b).hexdigest()!=o["sha256"]:print("NONE sha256 missing or mismatch");sys.exit()'),
 ("linked to its Engagement or Deal and its People.", "linked to its Engagement and its People."),
 ("whenever you log an Activity linked to an Engagement or Deal, set", "whenever you log an Activity linked to an Engagement, set"),
 ("linked to an Engagement or Deal: add this Activity's", "linked to an Engagement: add this Activity's"),
 ("- Engagement, Deal, Episode: the ones this mail is about.", "- Engagement, Episode: the ones this mail is about."),
 ("- Then set Last activity on the linked Engagement or Deal (see LAST ACTIVITY).", "- Then set Last activity on the linked Engagement (see LAST ACTIVITY)."),
 # Decision 517: Saurabh's forwards.
 ("A pitch that reached us only through Saurabh or Akshay's other address:", "A pitch Saurabh forwarded goes by STEP 6a; one that reached us only through Akshay's other address:"),
 (("STEP 6a. GUEST PITCHES FORWARDED BY SAURABH GARG (decision 107)", "send a NEW mail to the original sender and the people on the original mail."),
  "STEP 6a. GUEST PITCHES FORWARDED BY SAURABH GARG (decision 517, Akshay, 7 Nov: \"Let Saurabh remain in CC\"; it replaces the new-mail route of decisions 107 and 122 for these forwards)\n"
  "Saurabh Garg (C4E; find his People row by name) often forwards inbound guest pitches he receives. For a mail from him in the last 72 hours that forwards a podcast guest pitch (someone proposing themselves or a client as a guest; not a vendor pitch, writing project or newsletter), where nobody from our side has replied:\n"
  "- The loop-in (LOOP-IN's draft path) is a reply on his forward: To Saurabh, Cc zoya@myunnati.com and the house copies, body \"thanks SG, looping in Zoya\". Zoya then writes to the pitcher on that chain from her inbox, with Saurabh in Cc (her rules).\n"
  "- Capture the forwarded pitch like any new pitch (STEPS 3 to 5): the guest is the person pitched, the original sender goes in Via, and everyone else on the original mail in Stakeholders. Saurabh is Akshay's ex-cofounder, never Via or Stakeholder: note \"forwarded by Saurabh <date>, thread <the forward's Message-ID>\" in the Claude note instead."),
],
"act": [
 RETIRED, ACT_SCHEMA, DEALS_DB, NEW_LEAD,
 ("- Every Engagement or Deal you change:", "- Every Engagement you change:"),
 ("linked to its Engagement or Deal). You act on", "linked to its Engagement). You act on"),
 (("STEP 4. DEALS (selling ThePodium's podcast production to a company)\n", "Deals are only for PaaS, our podcast production service (decision 156). Everything paid on our own shows stays in Engagements:"),
  "STEP 4. PRODUCTION SALES AND BRAND ASKS (decision 518)\nA production-sales conversation (selling ThePodium's podcast production to a company) is an Engagement on Show PaaS (" + PAAS_SHOW + "), found by Organisation, then its People; none: create one, Name \"<main contact> @ <Company>, PaaS\", Guest the main contact, Stakeholders the others, Organisation, Status New, Waiting on Akshay, Next action \"Akshay: <who> at <company>: <what> (<D Mon>)\", Source Agent, Source ID \"gmail:<thread id>\"; PAAS applies from then on. Everything paid on our own shows stays on that show:"),
 ("every Engagement or Deal you touched", "every Engagement you touched"),
 ("On a sponsored row, a Deal or a paid-production thread,", "On a sponsored row or a paid-production thread,"),
 ("or a yes on a Deal or a non-standard price.", "or a non-standard price."),
 ("- A Cold outreach Deal still at Stage New is the target list (decision 89): leave Waiting on blank.\n", ""),
 ("On the Engagement or Deal (or, if there is none,", "On the Engagement (or, if there is none,"),
 (" Deals created and moved.", ""),
],
"sweep": [
 RETIRED,
 ("- Deals: collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a  (Company, Stage, Warm or cold, Next date, Next action, Last activity, Contacts)\n", ""),
 ("You may change Engagement and Deal Status or Stage,", "You may change Engagement Status,"),
 (" Deals have no Claude note; put the reason in Next action.", ""),
 ("with no Engagement and no Deal: link each", "with no Engagement: link each"),
 ("except an Outbound row at New (decision 167) and a Cold outreach Deal:", "except an Outbound row at New (decision 167):"),
 ("or Status Sponsored offered, and every Deal, whose Waiting on", "or Status Sponsored offered whose Waiting on"),
 (("\n- Deals: a Deal at Interested, In conversation or Proposal sent", "Cold Deals at New or Contacted are the outreach list: never flag them."), ""),
],
"wa": [
 RETIRED,
 ("Captured, People, Engagement, Deal, Episode)", "Captured, People, Engagement, Episode)"),
 ("- Deals: collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a\n", ""),
 ("an Engagement that is not closed, or a Contact on a Deal.", "an Engagement that is not closed (Show PaaS included)."),
 ("any company with an open Deal)", "any company with an open Engagement on Show PaaS)"),
 ("- Engagement, Deal, Episode: the ones the messages are about", "- Engagement, Episode: the ones the messages are about"),
 ("On each linked Engagement or Deal:", "On each linked Engagement:"),
],
"cal": [
 RETIRED,
 ("- Deals: collection://1a981c5a-912a-4972-b3fc-8c9f2abb329a\n", ""),
 (" A call whose attendee is a Deal contact also sets that Deal's Next date and Next action (\"Call on <date>\") if they are empty or older.", ""),
],
}
for a, c in EDITS[which]:
    if isinstance(a, tuple):
        st, en = a
        assert s.count(st) == 1 and s.count(en) == 1, (which, st[:50], s.count(st), en[:50], s.count(en))
        i, j = s.index(st), s.index(en)
        assert j > i, (which, "span order", st[:40])
        s = s[:i] + c + s[j + len(en):]
    else:
        assert s.count(a) == 1, (which, a[:70], s.count(a))
        s = s.replace(a, c)
assert s.count(chr(0x2014)) == b.decode("utf-8").count(chr(0x2014)), "new em dash"
ob = s.encode("utf-8"); assert len(ob) <= 65536 - 200, (which, len(ob))
open(out, "wb").write(ob); print(which, len(ob), hashlib.sha256(ob).hexdigest()[:16])
