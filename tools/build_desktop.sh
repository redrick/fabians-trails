#!/usr/bin/env bash
# Export Linux and Windows builds to build/linux and build/windows, zipped for itch.io.
# Needs the full 4.6.3 export templates (Editor → Manage Export Templates → Download and Install).
set -euo pipefail
cd "$(dirname "$0")/.."
GD=${GD:-~/apps/godot-4.6/Godot_v4.6.3-stable_linux.x86_64}
mkdir -p build/linux build/windows
$GD --headless --import --path game >/dev/null 2>&1 || true
$GD --headless --path game --export-release Linux ../build/linux/fabians-trail.x86_64
$GD --headless --path game --export-release Windows ../build/windows/FabiansTrail.exe
(cd build/linux && rm -f ../fabians-trail-linux.zip && zip -q ../fabians-trail-linux.zip *)
(cd build/windows && rm -f ../fabians-trail-windows.zip && zip -q ../fabians-trail-windows.zip *)
ls -la build/*.zip
