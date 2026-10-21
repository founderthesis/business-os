#!/bin/sh
# Composite of decisions 377 (with 376 live), 378 and 379 on the live prompts, one file per routine (CTO, 21 Oct ~21:15 JST).
# Usage: sh composite-377-379.sh <live dir> <out dir>. Live bases are checked by hash inside each script.
set -e
L=$1; O=$2; T=$(mktemp -d)
mkdir -p "$O"
python3 docs/proposals/d378.py "$L" "$T/378" 0           # WhatsApp (booking off)
python3 docs/proposals/d377.py "$L" "$T/377"             # calendar, sweep, Zoya
cp "$L"/trig_0189eZvAD8x4357cfevgZ3No.txt "$T/377/"      # inbox is not in 377
python3 docs/proposals/d379.py "$T/377" "$T/379"         # inbox, Zoya, sweep on top of 377
cp "$T/378"/trig_01MnmJYorWrd61K7b5BCqXr1.txt "$O/"
cp "$T/377"/trig_01Voiz5YsK2SnVf2STF8PoSH.txt "$O/"
cp "$T/379"/trig_0189eZvAD8x4357cfevgZ3No.txt "$T/379"/trig_01UPT8LDrBDL5JQqW91Awgbo.txt "$T/379"/trig_01MdfUFg2qrebDWgiHwncgnd.txt "$O/"
for f in "$O"/*.txt; do printf '%s %s %s\n' "$(basename $f .txt)" "$(wc -c <$f)" "$(sha256sum $f | cut -c1-16)"; done
