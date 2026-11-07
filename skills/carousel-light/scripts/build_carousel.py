#!/usr/bin/env python3
"""
carousel-light builder.

Takes a JSON copy spec and renders an Editorial Navy quote carousel:
one 1080x1080 PNG per card via wkhtmltoimage, a contact sheet for
review, and a bound PDF via img2pdf.

Usage:
    python3 build_carousel.py copy.json [workdir]

Outputs (in workdir, default /home/claude/carousel_build):
    card1.png ... cardN.png
    sheet.png                  <- review this with the view tool before shipping
    <Guest_Name> - Editorial Navy (N cards).pdf

JSON spec shape (all copy fields are plain text unless noted _html):

{
  "guest": "Ankit Mehta",
  "accent": "#f04f23",            // optional, default orange
  "bg": "#1a2742",                // optional, default navy
  "logo_html": "h<span class=\"dot\">i</span>ssa",   // top-left brand mark
  "logo_serif": true,             // serif (Lora) or sans (Poppins) logo
  "attribution": "ON BUILT-2-SHARE",                  // quote-card footer, orange line
  "wordmark_html": "BUILT <span class=\"two\">&#8212;2&#8212;</span> SHARE",  // cover+CTA footer
  "wordmark_sub": "WITH SATISH MUGULAVALLI",          // CTA footer second line
  "cover": {
    "name_html": "ANKIT<br>MEHTA",
    "role": "Co-founder & CEO, ideaForge",
    "hook": "He bootstrapped India's largest drone maker for 8 years. On listing day, the stock jumped 93%.",
    "subhook_html": "The wealth landed on the shop floor too.<br>Not just the corner offices.",
    "lessons": "4 lessons on talent, from 18 years of building.",
    "photo": null                 // path to image file, or null for placeholder frame
  },
  "quotes": [
    {"quote": "...", "support_html": "... with <b>one bolded receipt</b> ..."}
  ],
  "cta": {
    "headline": "The full conversation goes deeper.",
    "topics_html": "Topic one &middot; Topic two &middot; Topic three.",
    "label": "WATCH THE FULL EPISODE",
    "link": "built2share.in/ankit"
  }
}
"""
import base64
import json
import os
import subprocess
import sys

CSS = """
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Poppins', sans-serif; }
  .card { width: 1080px; height: 1080px; background: BG_COLOR; position: relative; overflow: hidden; }

  .logo { position: absolute; top: 78px; left: 90px; font-family: LOGO_FONT;
          font-size: 44px; color: #efe9da; letter-spacing: 1px; }
  .logo .dot { color: ACCENT; }
  .pageno { position: absolute; top: 92px; right: 90px; font-size: 24px;
            color: #8b97ab; letter-spacing: 7px; font-weight: 500; }
  .footer { position: absolute; left: 90px; right: 90px; bottom: 70px;
            border-top: 2px solid #efe9da; padding-top: 32px; }
  .footer .fname { font-size: 30px; font-weight: 700; color: #efe9da; }
  .footer .fshow { font-size: 21px; font-weight: 600; color: ACCENT; letter-spacing: 4px; margin-top: 6px; }
  .swipe { position: absolute; right: 0; top: 36px; font-size: 30px; font-weight: 800;
           color: ACCENT; letter-spacing: 2px; }
  .swipe .chev { letter-spacing: -4px; padding-left: 12px; }

  .qmark { position: absolute; top: 175px; left: 84px; font-family: 'Lora', serif;
           font-size: 170px; color: ACCENT; line-height: 1; }
  .content { position: absolute; top: 300px; left: 90px; right: 90px; }
  .quote { font-size: 55px; font-weight: 700; color: #efe9da; line-height: 1.24; }
  .support { margin-top: 48px; font-size: 27px; font-weight: 400; color: #a4afc2; line-height: 1.6; }
  .support b { color: #c9d2e0; font-weight: 600; }

  .cv-name { position: absolute; top: 168px; left: 90px; font-size: 96px; font-weight: 800;
             color: ACCENT; line-height: 1.02; letter-spacing: 1px; }
  .cv-role { position: absolute; top: 400px; left: 90px; font-size: 30px; font-weight: 700;
             color: #efe9da; line-height: 1.4; width: 480px; }
  .cv-hook { position: absolute; top: 505px; left: 90px; width: 480px; font-size: 34px;
             font-weight: 500; color: #efe9da; line-height: 1.4; }
  .cv-subhook { position: absolute; top: 715px; left: 90px; width: 470px; font-size: 27px;
                font-weight: 400; color: #a4afc2; line-height: 1.5; }
  .cv-lessons { position: absolute; top: 832px; left: 90px; width: 480px; font-size: 29px;
                font-weight: 700; color: ACCENT; line-height: 1.4; }
  .cv-photo { position: absolute; top: 160px; right: 90px; width: 380px; height: 730px;
              border: 2px solid #efe9da; background: #223252; }
  .cv-photo img { width: 100%; height: 100%; object-fit: cover; }
  .cv-photo .ph-note { position: absolute; top: 350px; left: 0; right: 0; text-align: center;
                       font-size: 22px; color: #5f6f8d; letter-spacing: 3px; font-weight: 600; }
  .b2s { font-style: italic; font-weight: 800; font-size: 30px; color: #efe9da; letter-spacing: 3px; }
  .b2s .two { color: ACCENT; }
  .b2s-sub { font-size: 21px; font-weight: 600; color: ACCENT; letter-spacing: 4px; margin-top: 8px; }

  .cta-head { position: absolute; top: 250px; left: 90px; right: 90px; font-size: 80px;
              font-weight: 700; color: #efe9da; line-height: 1.2; }
  .cta-topics { position: absolute; top: 500px; left: 90px; right: 90px; font-size: 32px;
                font-weight: 400; color: #a4afc2; line-height: 1.6; }
  .cta-label { position: absolute; top: 720px; left: 90px; font-size: 24px; font-weight: 600;
               color: #8b97ab; letter-spacing: 6px; }
  .cta-link { position: absolute; top: 775px; left: 90px; font-size: 56px; font-weight: 700;
              color: ACCENT; }
"""

PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="card">{body}</div></body></html>"""


def chrome(spec, n, total):
    return (f'<div class="logo">{spec["logo_html"]}</div>'
            f'<div class="pageno">{n:02d} / {total:02d}</div>')


def swipe():
    return '<div class="swipe">SWIPE <span class="chev">&gt;&gt;&gt;</span></div>'


def cover_card(spec, n, total):
    c = spec["cover"]
    if c.get("photo"):
        ext = os.path.splitext(c["photo"])[1].lstrip(".").lower() or "jpeg"
        b64 = base64.b64encode(open(c["photo"], "rb").read()).decode()
        photo = f'<div class="cv-photo"><img src="data:image/{ext};base64,{b64}"></div>'
    else:
        photo = '<div class="cv-photo"><div class="ph-note">GUEST PHOTO</div></div>'
    return (chrome(spec, n, total)
            + f'<div class="cv-name">{c["name_html"]}</div>'
            + f'<div class="cv-role">{c["role"]}</div>'
            + f'<div class="cv-hook">{c["hook"]}</div>'
            + f'<div class="cv-subhook">{c["subhook_html"]}</div>'
            + f'<div class="cv-lessons">{c["lessons"]}</div>'
            + photo
            + f'<div class="footer"><div class="b2s">{spec["wordmark_html"]}</div>{swipe()}</div>')


def quote_card(spec, q, n, total):
    return (chrome(spec, n, total)
            + '<div class="qmark">&ldquo;</div>'
            + f'<div class="content"><div class="quote">{q["quote"]}</div>'
            + f'<div class="support">{q["support_html"]}</div></div>'
            + f'<div class="footer"><div class="fname">{spec["guest"]}</div>'
            + f'<div class="fshow">{spec["attribution"]}</div>{swipe()}</div>')


def cta_card(spec, n, total):
    c = spec["cta"]
    sub = f'<div class="b2s-sub">{spec["wordmark_sub"]}</div>' if spec.get("wordmark_sub") else ""
    return (chrome(spec, n, total)
            + f'<div class="cta-head">{c["headline"]}</div>'
            + f'<div class="cta-topics">{c["topics_html"]}</div>'
            + f'<div class="cta-label">{c["label"]}</div>'
            + f'<div class="cta-link">{c["link"]}</div>'
            + f'<div class="footer"><div class="b2s">{spec["wordmark_html"]}</div>{sub}</div>')


def main():
    spec = json.load(open(sys.argv[1]))
    workdir = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/carousel_build"
    os.makedirs(workdir, exist_ok=True)

    css = (CSS.replace("ACCENT", spec.get("accent", "#f04f23"))
              .replace("BG_COLOR", spec.get("bg", "#1a2742"))
              .replace("LOGO_FONT", "'Lora', serif" if spec.get("logo_serif", True) else "'Poppins', sans-serif"))

    total = len(spec["quotes"]) + 2
    bodies = [cover_card(spec, 1, total)]
    bodies += [quote_card(spec, q, i + 2, total) for i, q in enumerate(spec["quotes"])]
    bodies.append(cta_card(spec, total, total))

    pngs = []
    for i, body in enumerate(bodies, 1):
        html_path = os.path.join(workdir, f"card{i}.html")
        png_path = os.path.join(workdir, f"card{i}.png")
        open(html_path, "w").write(PAGE.format(css=css, body=body))
        subprocess.run(["wkhtmltoimage", "--enable-local-file-access", "--width", "1080",
                        "--height", "1080", "--quality", "95", html_path, png_path],
                       check=True, capture_output=True)
        pngs.append(png_path)

    # contact sheet for review
    from PIL import Image
    cols = 3
    rows = (total + cols - 1) // cols
    sheet = Image.new("RGB", (1080 * cols, 1080 * rows), "white")
    for i, p in enumerate(pngs):
        sheet.paste(Image.open(p), ((i % cols) * 1080, (i // cols) * 1080))
    sheet.resize((450 * cols, 450 * rows)).save(os.path.join(workdir, "sheet.png"))

    import img2pdf
    safe = spec["guest"].replace(" ", "_")
    pdf_path = os.path.join(workdir, f"{safe}_-_Editorial_Navy_({total}_cards).pdf")
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(pngs))

    print(json.dumps({"pdf": pdf_path, "sheet": os.path.join(workdir, "sheet.png"), "cards": total}))


if __name__ == "__main__":
    main()
