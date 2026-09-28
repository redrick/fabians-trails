"""Mouse cursors: a beech leaf pointer and an acorn for clickable things. Tip at the top-left corner."""
import math
from lib import Col, ell, bez
from style3 import shape, stroke, form, T, LINE

LEAF = Col(0.7, "#e39a2d")
LEAF_VEIN = Col(0.45, "#a8601a")
STEM = Col(0.35, "#6e4524")
NUT = Col(0.6, "#c98a3e")
CUP = Col(0.4, "#7a5230")
CUP_DOT = Col(0.3, "#5a3a20")


def leaf(b):
    with T(2, b.h - 2, 1.0, rot=40):
        pts = bez((0, 0), (-7, -6), (-8, -18), (0, -28)) + bez((0, -28), (8, -18), (7, -6), (0, 0))
        form(pts, LEAF, LINE * 0.9, sh=0.12)
        stroke([(0, -1), (0, -29)], LINE * 0.6, g=LEAF_VEIN)
        for k in range(3):
            y = -7 - k * 6
            stroke([(0, y), (-4.5, y - 3)], LINE * 0.4, g=LEAF_VEIN)
            stroke([(0, y), (4.5, y - 3)], LINE * 0.4, g=LEAF_VEIN)
        stroke([(0, -28), (0, -33)], LINE * 1.3, g=STEM)


def acorn(b):
    with T(b.w - 3, 3, 1.0, rot=218):
        nut = bez((-5.5, -8), (-6.5, -16), (-3, -23), (0, -24)) + bez((0, -24), (3, -23), (6.5, -16), (5.5, -8))
        form(nut, NUT, LINE * 0.9, sh=0.12)
        cup = bez((-6.5, -9), (-7, -3), (-4, 0), (0, 0)) + bez((0, 0), (4, 0), (7, -3), (6.5, -9)) + [(-6.5, -9)]
        shape(cup, CUP, LINE * 0.9)
        for x, y in ((-3.5, -4), (0, -6), (3.5, -4), (-1.8, -2), (1.8, -2)):
            stroke(ell(x, y, 0.8, 0.8, 8), LINE * 0.4, closed=True, g=CUP_DOT)
        stroke([(0, -24), (0.5, -27.5)], LINE * 1.2, g=STEM)


ASSETS = [("cursor", 26, 26, leaf, "ui"), ("cursor_hand", 26, 26, acorn, "ui")]
