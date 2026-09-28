#!/usr/bin/env bash
# Serve build/web locally on :8060. build/web_test/shim.html drives frames from a MessageChannel instead of
# requestAnimationFrame, so the game keeps running in a hidden/background tab (browser automation).
set -euo pipefail
cd "$(dirname "$0")/../build"
rm -rf web_test && mkdir web_test
for f in web/*; do ln -s "../$f" "web_test/$(basename "$f")"; done
SHIM='<script>(()=>{const ch=new MessageChannel();let q=[],last=0;ch.port1.onmessage=()=>{const now=performance.now();if(now-last>=16){last=now;const c=q;q=[];c.forEach(f=>f(now));}if(q.length)ch.port2.postMessage(0);};window.requestAnimationFrame=cb=>{q.push(cb);ch.port2.postMessage(0);return 1;};})();</script>'
sed "s|<head>|<head>$SHIM|" web/index.html > web_test/shim.html
exec python3 -m http.server -d web_test 8060
