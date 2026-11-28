#!/bin/bash
# Render an FT infographic HTML file to a retina PNG using headless Chrome.
# The logo is injected automatically: put the token {{FT_LOGO}} in the <img src>
# and this script replaces it with the bundled logo as a base64 data URI, so the
# HTML is self-contained and path-independent.
#
# Usage:  scripts/render.sh <input.html> <output.png> [WIDTH] [HEIGHT]
# Example: scripts/render.sh charts/nasher-bars.html out/nasher-bars.png 1200 860
#
# Requires Google Chrome (macOS path below; edit CHROME for other OSes).

set -e
IN="$1"; OUT="$2"; W="${3:-1200}"; H="${4:-860}"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOGO="$SKILL_DIR/assets/ft-logo.png"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
EXTRA=""; [ "$(uname)" = "Linux" ] && EXTRA="--no-sandbox"

[ -f "$IN" ] || { echo "input html not found: $IN"; exit 1; }
[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME  (set CHROME=/path/to/chrome)"; exit 1; }

TMP="$(mktemp -d)"
DATAURI="data:image/png;base64,$(base64 < "$LOGO" | tr -d '\n')"
# inject the logo data URI wherever the {{FT_LOGO}} token appears (python replace
# so the long data URI never trips sed)
cp "$IN" "$TMP/render.html"
python3 - "$TMP/render.html" "{{FT_LOGO}}" "$DATAURI" <<'PY'
import sys; f,t,v=sys.argv[1:4]; s=open(f).read().replace(t,v); open(f,'w').write(s)
PY

"$CHROME" --headless=new --disable-gpu --hide-scrollbars $EXTRA \
  --force-device-scale-factor=2 --window-size="$W,$H" \
  --screenshot="$OUT" "file://$TMP/render.html" >/dev/null 2>&1

rm -rf "$TMP"
[ -f "$OUT" ] && echo "rendered: $OUT (${W}x${H} @2x)" || { echo "render failed"; exit 1; }
