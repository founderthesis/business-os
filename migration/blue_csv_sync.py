"""Blue CSV exports -> Notion gap fill (Akshay, 11 Nov: "just sync from CSV").

Re-runnable. Reads the three Blue list exports (data/blue_legacy/exports_*/),
normalises the fields that map to Notion, and writes:
  data/blue_csv_source.csv   one row per Blue card: show, guest, mapped fields
Step 2 (`plan` mode) joins that with a Notion snapshot JSON (episodes.json,
people.json, exported by the operator session) and writes:
  data/blue_csv_plan.csv     field writes to make (only where Notion is empty)
  data/blue_csv_review.csv   unmatched cards, ambiguous matches, conflicts
Nothing here writes to Notion; the operator applies the plan and reads back.
No personal data lives in this file.
"""
import csv, glob, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
EXPORTS = sorted(glob.glob(os.path.join(DATA, 'blue_legacy', 'exports_*', '*.csv')))

# Blue column -> Notion Episodes property, per export kind
EP_MAP = {
    'ft': {'Youtube Link': 'YouTube', 'podm.in Short Link': 'Short link', 'Spotify Link': 'Spotify',
           'Amazon Music Link': 'Amazon Music', 'Apple Podcast': 'Apple',
           'Substack Published Page': 'Substack', 'LI Announcement Post': 'LinkedIn',
           'Link to working doc': 'Copywriting doc', 'Date of recording': 'Recording date'},
    'un': {'YouTube Link': 'YouTube', 'short link': 'Short link', 'Spotify Link': 'Spotify',
           'Amazon Music Link': 'Amazon Music', 'Apple Podcast Link': 'Apple',
           'Published Newsletter Link': 'Substack', "Sri's LI Announcement": 'LinkedIn',
           'Link to Working Doc': 'Copywriting doc'},
    'b2s': {'YouTube Link': 'YouTube', 'short link': 'Short link', 'Spotify Link': 'Spotify',
            'Amazon Music Link': 'Amazon Music', 'Apple Podcast Link': 'Apple',
            'Published Newsletter Link': 'Substack', 'Link to Working Doc': 'Copywriting doc'},
}
PEOPLE_MAP = {
    'ft': {'Guest LinkedIn Profile Link': 'LinkedIn', 'Formal Designation of the guest': 'Title',
           'Guest Email ID': 'Email'},
    'un': {'Guest Linkedin Profile': 'LinkedIn', 'Guest Title': 'Title', 'Guest Email ID': 'Email'},
    'b2s': {'Guest Linkedin Profile': 'LinkedIn', 'Guest Title': 'Title', 'Guest Email ID': 'Email'},
}
SHOW = {'ft': 'FT', 'un': 'UN', 'b2s': 'B2S'}


def kind(path):
    b = os.path.basename(path)
    return 'ft' if 'ft-spotlight' in b else 'un' if 'alpha-un' in b else 'b2s' if 'hissa' in b else None


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9 ]+', ' ', s).split()


def first_url(v):
    m = re.search(r'https?://\S+', v or '')
    if m:
        return m.group(0).rstrip(',;)')
    m = re.match(r'\s*([a-z0-9.-]+\.[a-z]{2,}/\S+)', v or '', re.I)
    return 'https://' + m.group(1).rstrip(',;)') if m else ''


def date_iso(v):
    v = (v or '').strip()
    m = re.match(r'(\d{4}-\d{2}-\d{2})', v)
    if m:
        return m.group(1)
    for fmt in ('%d/%m/%Y', '%m/%d/%Y', '%d %b %Y', '%b %d, %Y'):
        try:
            import datetime
            return datetime.datetime.strptime(v, fmt).date().isoformat()
        except ValueError:
            pass
    return ''


def source():
    rows = []
    for p in EXPORTS:
        k = kind(p)
        if not k:
            continue
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            name = (r.get('Guest Name') or '').strip()
            out = {'show': SHOW[k], 'blue_id': r.get('Todo ID', ''), 'title': r.get('Title', '').strip(),
                   'guest': name}
            for col, prop in EP_MAP[k].items():
                v = r.get(col, '')
                out['ep:' + prop] = date_iso(v) if prop == 'Recording date' else first_url(v)
            for col, prop in PEOPLE_MAP[k].items():
                v = (r.get(col) or '').strip()
                out['pp:' + prop] = first_url(v) if prop == 'LinkedIn' else v.split(',')[0].strip()
            rows.append(out)
    keys = sorted({k for r in rows for k in r})
    with open(os.path.join(DATA, 'blue_csv_source.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    print('source rows', len(rows))
    return rows


def match_key(name):
    t = norm(name)
    return (t[0], t[-1]) if len(t) >= 2 else tuple(t)


def plan(episodes_json, people_json):
    rows = list(csv.DictReader(open(os.path.join(DATA, 'blue_csv_source.csv'))))
    eps = json.load(open(episodes_json))   # [{url, show, guestname, fields:{prop: value-or-empty}, guests:[people urls]}]
    ppl = json.load(open(people_json))     # [{url, name, fields:{prop: value-or-empty}}]
    plan_rows, review = [], []
    idx = {}
    for e in eps:
        idx.setdefault((e['show'], match_key(e['guestname'])), []).append(e)
    pidx = {}
    for p in ppl:
        pidx.setdefault(match_key(p['name']), []).append(p)
    for r in rows:
        if not r['guest']:
            review.append({**r, 'why': 'no guest name'})
            continue
        cands = idx.get((r['show'], match_key(r['guest'])), [])
        if len(cands) != 1:
            review.append({'show': r['show'], 'guest': r['guest'], 'why': f'episode matches: {len(cands)}'})
        else:
            e = cands[0]
            for k, v in r.items():
                if k.startswith('ep:') and v:
                    prop = k[3:]
                    cur = (e['fields'].get(prop) or '').strip()
                    if not cur:
                        plan_rows.append({'kind': 'episode', 'url': e['url'], 'name': e['guestname'], 'prop': prop, 'value': v})
                    elif cur.rstrip('/') != v.rstrip('/') and prop != 'Recording date':
                        review.append({'show': r['show'], 'guest': r['guest'], 'why': f'conflict {prop}'})
        pc = pidx.get(match_key(r['guest']), [])
        if len(pc) == 1:
            p = pc[0]
            for k, v in r.items():
                if k.startswith('pp:') and v:
                    prop = k[3:]
                    if not (p['fields'].get(prop) or '').strip():
                        plan_rows.append({'kind': 'person', 'url': p['url'], 'name': p['name'], 'prop': prop, 'value': v})
        elif len(pc) > 1:
            review.append({'show': r['show'], 'guest': r['guest'], 'why': f'people matches: {len(pc)}'})
    for fn, data in (('blue_csv_plan.csv', plan_rows), ('blue_csv_review.csv', review)):
        keys = sorted({k for d in data for k in d}) or ['empty']
        with open(os.path.join(DATA, fn), 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(data)
    print('plan writes', len(plan_rows), 'review', len(review))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'plan':
        plan(sys.argv[2], sys.argv[3])
    else:
        source()
