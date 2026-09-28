"""Joey's games props: the big apple tree for the orchard game."""
import math, random
from lib import Col, ell, bez
from style3 import shape, stroke, form, T, LINE

BARK = Col(0.4, "#7a5230")
BARK_DARK = Col(0.3, "#5a3a20")
LEAF = Col(0.6, "#6fa64a")
LEAF_DARK = Col(0.5, "#4f8a3a")
LEAF_GOLD = Col(0.75, "#c9b23e")


def apple_tree(b):
    r = random.Random(4)
    cx = b.w / 2
    with T(cx, 4, 1.0):
        trunk = bez((-22, 0), (-14, 60), (-18, 110), (-10, 150)) + [(12, 150)] + bez((12, 150), (18, 110), (14, 60), (24, 0))
        form(trunk, BARK, LINE * 1.2, sdx=3, sdy=0, sh=0.15)
        for dx in (-6, 5):
            stroke(bez((dx, 20), (dx + 2, 50), (dx - 2, 80), (dx + 1, 110)), LINE * 0.6, g=BARK_DARK)
        for side in (-1, 1):
            stroke(bez((0, 140), (side * 30, 165), (side * 60, 185), (side * 85, 200)), LINE * 4.2)
            stroke(bez((0, 140), (side * 30, 165), (side * 60, 185), (side * 85, 200)), LINE * 2.6, g=BARK)
        blobs = [(0, 250, 110, 80)]
        for i in range(12):
            a = math.radians(15 + i * 150 / 11)
            blobs.append((math.cos(a) * 118, 228 + math.sin(a) * 68, 48, 42))
        for i in range(5):
            blobs.append((-100 + i * 50, 186, 44, 34))
        for (x, y, rx, ry) in blobs:
            form(ell(x, y, rx, ry, 30), LEAF_DARK, LINE, sdx=-3, sdy=2, sh=0.1)
        for (x, y, rx, ry) in blobs:
            shape(ell(x + 3, y + 4, rx * 0.82, ry * 0.8, 30), LEAF, 0)
        for i in range(26):
            x, y = r.uniform(-130, 130), r.uniform(185, 300)
            if (x / 140) ** 2 + ((y - 240) / 80) ** 2 < 0.8:
                a = r.uniform(0, 360)
                shape(ell(x, y, 6, 3, 10, rot=a), LEAF_GOLD, LINE * 0.5)


ASSETS = [("apple_tree", 400, 350, apple_tree, "props")]
