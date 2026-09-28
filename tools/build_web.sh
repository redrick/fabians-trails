#!/usr/bin/env bash
# Export the single-threaded web build to build/web/. Deploy: butler push build/web redricko/fabians-trail:html5
set -euo pipefail
cd "$(dirname "$0")/.."
GD=${GD:-~/apps/godot-4.6/Godot_v4.6.3-stable_linux.x86_64}
mkdir -p build/web
$GD --headless --import --path game >/dev/null 2>&1 || true
$GD --headless --path game --export-release Web ../build/web/index.html
ls -la build/web
