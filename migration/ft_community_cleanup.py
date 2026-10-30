"""Reconcile FT Community (Notion) with the confirmed 14 Oct member list.

Inputs (git-ignored): data/whatsapp/list_2026-10-14.txt, data/whatsapp/ft_network.json.
Output: a Notion AI instruction file (decision 91) with updates, new rows and Left rows.
Re-runnable; prints counts.
"""
import json, re, difflib, sys

LIST = 'data/whatsapp/list_2026-10-14.txt'
NET = 'data/whatsapp/ft_network.json'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'data/whatsapp/ft-community-cleanup.md'

# Same person, spelled differently (checked by hand, 14 Oct)
MANUAL = {
    'Chandra Bhanu': 'Chandrabhanu Pattajoshi', 'Charlie Lee': 'Cheolwon Lee',
    'Md Zeeshan': 'Mohammed Zeeshan', 'Mike Engel': 'Michael Engle',
    'Praveen Shah': 'Praveen Kumar Sah', 'Sreeraman (SMG) Mohan Girija': 'Sreeraman MG',
    'Sreevathsa P': 'Sreevathsa Prabhakar', 'Deepak Uniyal': 'Deepak Bhuvneshwari Uniyal',
    'Sunny Gurpreet Singh': 'Sunny Singh',
}
# Close spellings that are different people
NO_FUZZY = {'Rajat Garg', 'Saurabh Garg'}
INVESTOR = re.compile(r'capital|ventures|venture|vc\b|fund|partners|angels|invest', re.I)


def norm(n):
    n = n.lower()
    n = re.sub(r'^(dr\.?)\s+', '', n)
    n = re.sub(r'\(.*?\)', '', n)
    n = re.sub(r'[^a-z ]', '', n)
    return ' '.join(n.split())


lines = open(LIST).read().strip().split('\n')
lst = [l.split('. ', 1)[1].rsplit(' - ', 1) for l in lines[2:]]
added = [r for r in json.load(open(NET)) if r['Membership'] == 'Added']
akeys = {norm(r['Name']): r for r in added}

used, match = set(), {}
for n, c in lst:
    if norm(n) in akeys:
        used.add(norm(n)); match[n] = akeys[norm(n)]
for n, c in lst:
    if n in match or n in NO_FUZZY:
        continue
    if n in MANUAL:
        r = akeys[norm(MANUAL[n])]
    else:
        m = difflib.get_close_matches(norm(n), [a for a in akeys if a not in used], 1, 0.8)
        if not m:
            continue
        r = akeys[m[0]]
    used.add(norm(r['Name'])); match[n] = r

upd = [(match[n]['url'], n, c) for n, c in lst if n in match]
new = [(n, c) for n, c in lst if n not in match]
left = [r for k, r in akeys.items() if k not in used]
print(f'list {len(lst)}  update {len(upd)}  new {len(new)}  left {len(left)}  (update+new={len(upd)+len(new)})')
assert len(upd) + len(new) == len(lst)

U = lambda u: u.replace('app.notion.com/', 'app.notion.com/p/')
L = ['# FT Community cleanup, 14 Oct 2026\n',
     'Database: FT Community (https://app.notion.com/p/9a1192a5e71b4a2fa6a585e3c3fd36f7), the list of The Founder Thesis Community WhatsApp group. Membership = Added means in the group now. The member list Akshay confirmed on 14 Oct has 511 people; after this cleanup exactly those 511 rows are Added.\n',
     'Do not delete any row. Do not change Person, Blurb, Blurb link, One-liner or LinkedIn.\n',
     f'## Step 1: update {len(upd)} existing rows\n\nOpen each row by its URL. Set Name and Company exactly as written and Membership to Added. Leave everything else.\n',
     '| Row URL | Name | Company |\n|---|---|---|']
L += [f'| {U(u)} | {n} | {c} |' for u, n, c in upd]
L += [f'\n## Step 2: create {len(new)} new rows\n\nOne row per line: Name, Company and Type as written, Membership Added, Source "30 Sep list", Captured 2026-10-14, Needs review ticked, Review note "Created from the 14 Oct member list; link Person".\n',
      '| Name | Company | Type |\n|---|---|---|']
L += [f'| {n} | {c} | {"Investor" if INVESTOR.search(c) else "Founder"} |' for n, c in new]
L += [f'\n## Step 3: mark {len(left)} rows as Left\n\nThese rows say Added but the people are not in the group. Set Membership to Left and Review note to "Not on the 14 Oct member list: left after being added, or never joined". Leave Left on empty.\n',
      '| Row URL | Name | Company |\n|---|---|---|']
L += [f'| {U(r["url"])} | {r["Name"]} | {r["Company"] or ""} |' for r in left]
L += ['\n## Step 4: check\n\nFilter FT Community on Membership = Added. There must be exactly 511 rows, with the names in Step 5. Report any difference.\n',
      '## Step 5: the member list on the kit page\n\nOn the page "FT community invite kit" (https://app.notion.com/p/3f919a301a7f8182809ede95a2cdae19), under the heading "Member list", replace the line starting "List version:" with "List version: 14 Oct 2026, 511 members" and the line starting "Member count at last send:" with "Member count at last send: 511". Then add under that heading a code block containing exactly this text:\n',
      '```\n' + open(LIST).read().strip() + '\n```\n']
open(OUT, 'w').write('\n'.join(L))
print('wrote', OUT)
