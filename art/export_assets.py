"""Export Fabian's Trail art as transparent PNGs into ../game/assets/<folder>/<name>.png.

Usage:  .venv/bin/python export_assets.py [--module animals] [name-filter ...]
Then:   Godot --headless --import --path ../game   (the running game does not reimport)

Every art module lists ASSETS = [(name, w_pt, h_pt, draw(box), folder), ...].
"""
import os, sys, zlib, importlib, traceback
from reportlab.pdfgen import canvas
import pymupdf
import lib
lib.MODE = "color"
import style3

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "game", "assets")
SCALE = 2.0
MODULES = ["games", "cursor", "people", "fabian", "animals", "fungi", "plants", "places_a", "places_b"]


class Box:
    def __init__(self, w, h): self.x, self.y, self.w, self.h = 0, 0, w, h
    def X(self, f): return self.w*f
    def Y(self, f): return self.h*f


def render(name, w, h, draw, folder):
    os.makedirs(os.path.join(OUT, folder), exist_ok=True)
    tmp = os.path.join(OUT, "_tmp_%s.pdf" % name)
    cv = canvas.Canvas(tmp, pagesize=(w, h)); lib.set_canvas(cv)
    style3._R.seed(zlib.crc32(name.encode()))
    lib.RND.seed(zlib.crc32(name.encode()))
    draw(Box(w, h)); cv.showPage(); cv.save()
    doc = pymupdf.open(tmp)
    pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), alpha=True)
    path = os.path.join(OUT, folder, name + ".png"); pix.save(path); doc.close(); os.remove(tmp)
    print("wrote", os.path.relpath(path, HERE))


if __name__ == "__main__":
    args = sys.argv[1:]
    mods = MODULES
    if "--module" in args:
        i = args.index("--module")
        mods = [args[i + 1]]
        args = args[:i] + args[i + 2:]
    failed = []
    for m in mods:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError as e:
            if e.name == m:
                continue
            raise
        for name, w, h, fn, folder in mod.ASSETS:
            if args and not any(a in name for a in args):
                continue
            try:
                render(name, w, h, fn, folder)
            except Exception:
                traceback.print_exc()
                failed.append(name)
    if failed:
        print("FAILED:", " ".join(failed))
        sys.exit(1)
