import re, html, sys, json
TPL = '''<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=Public+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Layout: single reading column, verdict strip on top, eval sections below */
:root {{
  --bg:#f7f8fa; --paper:#ffffff; --ink:#1c2230; --muted:#5d6577; --rule:#dde1e8;
  --accent:#2f4f8f; --good:#1f7a4d; --warn:#9a6a00; --bad:#a33a2c;
  --display:"Source Serif 4", Georgia, serif; --body:"Public Sans", system-ui, sans-serif; --mono:"IBM Plex Mono", ui-monospace, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#12151c; --paper:#1a1f29; --ink:#e6e9ef; --muted:#a2a9b8; --rule:#2c3341;
  --accent:#8fb0ee; --good:#5fc795; --warn:#e2b54d; --bad:#ec8a7c; color-scheme:dark; }} }}
:root[data-theme="dark"] {{
  --bg:#12151c; --paper:#1a1f29; --ink:#e6e9ef; --muted:#a2a9b8; --rule:#2c3341;
  --accent:#8fb0ee; --good:#5fc795; --warn:#e2b54d; --bad:#ec8a7c; color-scheme:dark; }}
body {{ background:var(--bg); color:var(--ink); font:16px/1.6 var(--body); }}
.wrap {{ max-width:44rem; margin:0 auto; padding-block:2rem 4rem; padding-inline:16px; }}
.eyebrow {{ font:500 12px/1 var(--mono); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
h1 {{ font:700 clamp(1.7rem,4vw,2.3rem)/1.15 var(--display); margin:.5rem 0 .25rem; text-wrap:balance; }}
.sub {{ color:var(--muted); margin:0 0 1.25rem; }}
.strip {{ display:flex; flex-wrap:wrap; gap:.6rem 1.5rem; align-items:center; background:var(--paper); border:1px solid var(--rule); border-radius:10px; padding:1rem 1.1rem; }}
.chip {{ font:600 14px/1 var(--body); padding:.45rem .7rem; border-radius:999px; border:1.5px solid currentColor; }}
.chip.good {{ color:var(--good); }} .chip.warn {{ color:var(--warn); }} .chip.bad {{ color:var(--bad); }}
.score {{ font:500 13px/1.3 var(--mono); color:var(--muted); font-variant-numeric:tabular-nums; }}
.score b {{ color:var(--ink); font-weight:500; }}
.route {{ flex-basis:100%; margin:0; }}
main {{ display:grid; gap:1.1rem; margin-top:1.5rem; }}
main p, main ul {{ margin:0; max-width:65ch; }}
main ul {{ padding-left:1.2rem; display:grid; gap:.3rem; }}
main strong {{ font-weight:600; }}
.lead {{ font-family:var(--display); font-weight:600; color:var(--accent); }}
footer {{ margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--rule); color:var(--muted); font-size:13px; }}
a {{ color:var(--accent); }}
</style>
<div class="wrap">
  <div class="eyebrow">Founder Thesis guest eval · {date}</div>
  <h1>{guest}</h1>
  <p class="sub">{company}</p>
  <div class="strip">
    <span class="chip {cls}">{verdict}</span>
    <span class="score">Audience fit <b>{af}</b> · Sales fit <b>{sf}</b></span>
    <p class="route">{route}</p>
  </div>
  <main>{body}</main>
  <footer>Prepared for Akshay Datt by the Business OS evals routine. Figures marked uncertain or unverified were not confirmed.</footer>
</div>
'''
def inline(t):
    t = html.escape(t, quote=False)
    t = t.replace('\\$','$').replace('\\~','~')
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return t
def render(md):
    out=[]; ul=[]
    for line in md.strip().splitlines():
        s=line.strip()
        if not s: continue
        if s.startswith('- '):
            ul.append('<li>'+inline(s[2:])+'</li>'); continue
        if ul: out.append('<ul>'+''.join(ul)+'</ul>'); ul=[]
        m=re.match(r'\*\*(.+?)\*\*\s*(.*)', s)
        if m: out.append(f'<p><span class="lead">{inline(m.group(1))}</span> {inline(m.group(2))}</p>')
        else: out.append('<p>'+inline(s)+'</p>')
    if ul: out.append('<ul>'+''.join(ul)+'</ul>')
    return '\n'.join(out)
d=json.load(open(sys.argv[1]))
cls={'Decline':'bad','Strong consider':'good','Book immediately':'good'}.get(d['verdict'],'warn')
open(sys.argv[2],'w').write(TPL.format(title=d['title'],date=d['date'],guest=d['guest'],company=d['company'],verdict=d['verdict'],cls=cls,af=d['af'],sf=d['sf'],route=inline(d['route']),body=render(d['body'])))
