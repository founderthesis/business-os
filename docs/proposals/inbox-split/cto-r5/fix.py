"""CTO r5 (2 Nov 00:30 JST): capture's first live run (00:02) logged nothing: it could not get Message-IDs out of
email_read original (base64 .eml, inline or saved to a file) and stopped. Make the extraction an exact Bash recipe,
and make a failure pend the message instead of stopping the run. Usage: python3 fix.py <capture 60ee33ad> <out>"""
import hashlib, sys
s = open(sys.argv[1], encoding="utf-8").read()
assert hashlib.sha256(s.encode()).hexdigest()[:16] == "60ee33adf4659c03"
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
rep('RAW: email_read original (decode it in Bash, keep only the Message-ID line);',
    'RAW: email_read original, then the Message-ID comes from Bash, never by eye or by hand. The result saved to a file: '
    'python3 -c "import re,sys,base64;s=open(sys.argv[1]).read();b=re.search(r\'data\\W{1,8}([A-Za-z0-9+/=]{100,})\',s).group(1);'
    'm=re.search(rb\'(?im)^Message-ID:\\s*<?([^>\\s]+)\',base64.b64decode(b));print(m.group(1).decode() if m else \'NONE\')" <file>. '
    'Returned inline: copy the data value\'s first 8000 characters into a file in Bash (a heredoc), then '
    'base64 -d <file> 2>/dev/null | grep -aim1 -A1 \'^Message-ID:\'; not there, the next 8000 (offsets multiples of 4). '
    'A message whose Message-ID this does not give is pended as "mcp:<its id>" (STEP 2) and the run goes on; it never stops or ends the run;')
rep('email_read read has no Message-ID: get it from RAW, one call at a time,',
    'email_read read has no Message-ID: get it from RAW (the Bash recipe in MAILBOX), one call at a time,')
out = s.encode()
assert len(out) <= 65536 - 200 and s.count(chr(0x2014)) == 0
open(sys.argv[2], "wb").write(out)
print(len(out), hashlib.sha256(out).hexdigest()[:16])
