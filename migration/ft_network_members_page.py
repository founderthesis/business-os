"""Render the public "Founder Thesis community: members" page from FT Network rows.

Usage:
  python3 -I migration/ft_network_members_page.py <rows.json> <out.md> [YYYY-MM-DD]

<rows.json> is a JSON list of FT Network rows pulled from Notion with at least
Name, Company, One-liner, LinkedIn, Membership. Only Membership = Added is shown.
Only public-safe fields go on the page: name (linked to LinkedIn), company, one-liner.
Never the Blurb, Review note or Person link. Re-runnable; no Notion writes here.
"""
import json, re, sys

ESC = re.compile(r"([\\*~`$\[\]<>{}|^])")

def esc(s):
    return ESC.sub(r"\\\1", (s or "").strip())

def render(rows, as_of):
    members = sorted((r for r in rows if r.get("Membership") == "Added"), key=lambda r: r["Name"].lower())
    out = [
        "> Founders, VCs and operators in the Founder Thesis WhatsApp group, most of them past guests of the podcast.",
        "For privacy, contact details aren't shared here. If you'd like an intro to anyone, message Akshay and he'll connect you.",
        f"{len(members)} members, as of <mention-date start=\"{as_of}\"/>.",
        "---",
        '<table fit-page-width="true" header-row="true">',
        "\t<tr>", "\t\t<td>**Name**</td>", "\t\t<td>**Company**</td>", "\t\t<td>**What they do**</td>", "\t</tr>",
    ]
    for r in members:
        name = esc(r["Name"])
        if r.get("LinkedIn"):
            name = f"[{name}]({r['LinkedIn']})"
        out += ["\t<tr>", f"\t\t<td>{name}</td>", f"\t\t<td>{esc(r.get('Company'))}</td>",
                f"\t\t<td>{esc(r.get('One-liner'))}</td>", "\t</tr>"]
    out.append("</table>")
    return "\n".join(out) + "\n", len(members)

if __name__ == "__main__":
    rows = json.load(open(sys.argv[1]))
    as_of = sys.argv[3] if len(sys.argv) > 3 else "2026-10-08"
    md, n = render(rows, as_of)
    open(sys.argv[2], "w").write(md)
    print("members", n, "of", len(rows), "rows")
