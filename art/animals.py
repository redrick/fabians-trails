"""Fabian's Trail animals of the Brdy woods: one 120x120 atlas picture per species."""
import math, random
from lib import C, Col, ell, bez, rrect, resample
from style3 import T, LINE, poly, shape, form, stroke, fill, tube, dot, offset_shadow


def K(h, a=None):
    r, g, b = (int(h[i:i+2], 16)/255 for i in (1, 3, 5))
    return Col(round(0.3*r + 0.59*g + 0.11*b, 2), h, a)


INK = K("#1d1a1a")
WHITE = K("#fbfaf4")
CREAM = K("#f1e3c2")
PINK = K("#e9a0a0")
TWIG = K("#8a6240")
TWIG_DARK = K("#5e4028")
LEAF = K("#e0902c")
HORN = K("#d8cfb4")
BEAK_Y = K("#f2b632")
FOOT_PINK = K("#c99a86")
EYE_AMBER = K("#d98d2a")
EYE_GOLD = K("#e8b73a")
EYE_PALE = K("#cfe0ea")

HARE = K("#b98552"); HARE_DARK = K("#7a5230"); HARE_LIGHT = K("#ead2ab")
DUCK_GREY = K("#c9c6bd"); DUCK_HEAD = K("#1f7a4c"); DUCK_BREAST = K("#7b3f2a"); DUCK_WING = K("#9a8c7a")
DUCK_BLUE = K("#3a57b8"); DUCK_BILL = K("#e9c23a"); DUCK_FOOT = K("#f08a2a")
PHEAS = K("#c0692c"); PHEAS_DARK = K("#6e3418"); PHEAS_WING = K("#c7a06a"); PHEAS_HEAD = K("#1f4a52")
PHEAS_RED = K("#d8303a"); PHEAS_TAIL = K("#b58a55"); LEG_GREY = K("#8d8778")
PART_GREY = K("#aeb0aa"); PART_BROWN = K("#8a6a48"); PART_FACE = K("#e08a3c"); PART_CHEST = K("#6a3a22")
HERON = K("#a9b2ba"); HERON_DARK = K("#5b6168"); HERON_NECK = K("#e9ecee"); HERON_LEG = K("#c9a860")
HERON_BILL = K("#eba23a")
FROG = K("#a08a4e"); FROG_DARK = K("#5a4426"); FROG_BELLY = K("#efe2b8"); FROG_SPOT = K("#6e5a32")
TOAD = K("#8f6240"); TOAD_WART = K("#6e4a2e"); TOAD_BELLY = K("#e3d3b0"); TOAD_EYE = K("#d9772a")
TROUT_BACK = K("#6f6436"); TROUT_SIDE = K("#d4b45e"); TROUT_BELLY = K("#f3e6bf"); TROUT_FIN = K("#c9a458")
TROUT_RED = K("#d8392e"); TROUT_HALO = K("#f4e2c0")
DART_RED = K("#d5352b"); DART_DARK = K("#8a2a1c"); DART_EYE = K("#9a3a24"); WING = K("#e6f3fb", 0.55)
WING_VEIN = K("#9ab4c4"); WING_BASE = K("#f0b44a", 0.6)
SQ = K("#c65a26"); SQ_DARK = K("#8a3a16"); NUT = K("#9a6232"); NUT_CAP = K("#c9a36a")
JAY = K("#c79c86"); JAY_BLUE = K("#3a78c8"); JAY_CROWN = K("#ece2da")
BB = K("#2a282d"); BB_EDGE = K("#4a4852"); BB_BILL = K("#f2a52a"); WORM = K("#d98a8a")
TIT_YEL = K("#f2d23a"); TIT_BACK = K("#90a452"); TIT_WING = K("#6f86a2")
WP = K("#222126"); WP_RED = K("#d8262b"); WP_BILL = K("#e9dfbb"); BARK = K("#8b7a64"); BARK_DARK = K("#5e5040")
BUZ = K("#7a5234"); BUZ_DARK = K("#553620"); BUZ_PALE = K("#eadbbf"); BUZ_FOOT = K("#efc234")
ROE = K("#a57656"); ROE_DARK = K("#7a5238"); HOOF = K("#2e2622")
STAG = K("#9a5a32"); STAG_MANE = K("#6a3e24"); STAG_RUMP = K("#e3c894"); ANTLER = K("#d8c49a")
FOX = K("#dc6a2a"); FOX_DARK = K("#3a2a22")
BADGER = K("#a3a29c"); BADGER_DARK = K("#2a2828")
BOAR = K("#5e4c3e"); BOAR_DARK = K("#3c3028"); SNOUT = K("#b9938a")
HOG_SPINE = K("#6e5238"); HOG_TIP = K("#e6d4b4"); HOG_FACE = K("#d8b88c")
ANT_RED = K("#c04a26"); ANT_BLACK = K("#221c1a")
LIZ_GREEN = K("#7fb33e"); LIZ_BROWN = K("#8e6a42"); LIZ_BELLY = K("#e8dc8a")
SLOW = K("#b9824a"); SLOW_DARK = K("#6e4424"); SLOW_SHINE = K("#fff2d8", 0.55)
SAL = K("#232226"); SAL_YEL = K("#f5c21a")
OWL = K("#8a6a4a"); OWL_DARK = K("#5e4632"); OWL_FACE = K("#cdb698")
BAT = K("#b8783a"); BAT_WING = K("#4e3a2c"); BAT_DARK = K("#33261e"); BAT_BONE = K("#7a5e48")

ASSETS = []


def animal(s=1.0, dx=0, dy=0):
    def reg(fn):
        def draw(b):
            with T(b.w/2 + dx, 8 + dy, s): fn()
        ASSETS.append((fn.__name__, 120, 120, draw, "atlas"))
        return fn
    return reg


# ------------------------------------------------------------------ helpers
def sm(pts, closed=True, n=7):
    m = len(pts); out = []
    for i in range(m if closed else m - 1):
        p0 = pts[(i-1) % m] if closed else pts[max(i-1, 0)]
        p1, p2 = pts[i], pts[(i+1) % m]
        p3 = pts[(i+2) % m] if closed else pts[min(i+2, m-1)]
        for k in range(n):
            t = k/n; t2 = t*t; t3 = t2*t
            out.append(tuple(0.5*(2*p1[j] + (-p0[j]+p2[j])*t + (2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2 + (-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0, 1)))
    if not closed: out.append(pts[-1])
    return out


class body:
    """fill, then draw markings clipped inside (the with-block), then crisp shadow and outline"""
    def __init__(self, pts, g, sh=0.13, sdx=-1.8, sdy=1.6, w=LINE):
        self.a = (pts, g, sh, sdx, sdy, w)
    def __enter__(self):
        pts, g = self.a[:2]
        form(pts, g, 0, sh=0)
        C.saveState(); C.clipPath(poly(pts), stroke=0, fill=0)
        return pts
    def __exit__(self, *e):
        C.restoreState()
        pts, g, sh, sdx, sdy, w = self.a
        if sh: offset_shadow(pts, sdx, sdy, sh)
        if w: stroke(pts, w, closed=True)


def line(pts, w=LINE*0.6, g=INK, closed=False):
    stroke(sm(pts, False) if len(pts) > 2 else pts, w, g=g)


def eye(x, y, r, iris=None, slit=False, lid=False):
    if iris is not None:
        shape(ell(x, y, r, r, 22), iris, LINE*0.6)
        if slit: fill(ell(x + r*0.08, y, r*0.72, r*0.4, 18), INK)
        else: fill(ell(x + r*0.12, y, r*0.6, r*0.64, 18), INK)
    else:
        shape(ell(x, y, r*0.88, r, 22), INK, LINE*0.4)
    dot(x + r*0.3, y + r*0.36, r*0.3, 1.0)
    dot(x - r*0.3, y - r*0.4, r*0.12, 1.0)
    if lid: line([(x - r*1.1, y + r*0.9), (x, y + r*1.25), (x + r*1.1, y + r*0.9)], LINE*0.55)


def smile(x, y, w, g=INK):
    stroke(bez((x - w, y + w*0.35), (x - w*0.4, y - w*0.35), (x + w*0.4, y - w*0.35), (x + w, y + w*0.35)), LINE*0.65, g=g)


def zig(pts, amp, step=3.2):
    P = resample(pts, step, True); out = []
    for i, p in enumerate(P):
        a = P[i-1]; b = P[(i+1) % len(P)]
        dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1
        k = amp if i % 2 else 0
        out.append((p[0] + dy/L*k, p[1] - dx/L*k))
    return out


def twig(x0, x1, y, leaf=True):
    tube([(x0, y - 1), ((x0+x1)/2, y + 1.5), (x1, y + 2.5)], 5, 3.6, TWIG, sh=0.15)
    if leaf:
        lf = sm([(x1 - 10, y + 2), (x1 - 4, y - 5), (x1 + 2, y - 9), (x1 - 2, y - 2)])
        shape(lf, LEAF, LINE*0.8); line([(x1 - 9, y + 1.5), (x1 - 4, y - 3), (x1 + 1, y - 8)], LINE*0.4, TWIG_DARK)


def toes(x, y, n=3, dx=2.4, g=INK):
    for k in range(n):
        line([(x, y), (x + dx*(k - (n-1)/2) + 1.5, y - 2.8)], LINE*0.9, g)


def bird_foot(x, y, g=FOOT_PINK):
    tube([(x, y + 7), (x, y + 1)], 2.2, 2.0, g, lw=LINE*0.7, sh=0)
    for d in (-2.4, 0.6, 3.2):
        tube([(x, y + 1), (x + d, y - 1.8)], 1.8, 1.4, g, lw=LINE*0.6, sh=0)


def spots(pts_xy, r, g, ring=None):
    for x, y in pts_xy:
        if ring is not None: fill(ell(x, y, r*1.7, r*1.6, 14), ring)
        fill(ell(x, y, r, r*0.9, 12, rot=(x*37) % 180), g)


# ------------------------------------------------------------------ mammals
@animal(1.05, dx=2)
def zajic():
    far_ear = sm([(12, 54), (4, 70), (0, 88), (4, 94), (10, 86), (16, 70), (20, 56)])
    shape(far_ear, HARE_DARK)
    tube([(20, 26), (22, 12), (24, 2)], 5.4, 4.2, HARE_DARK, sh=0)
    b = sm([(-40, 14), (-42, 30), (-34, 44), (-16, 50), (4, 50), (16, 44), (22, 30), (22, 14), (12, 4), (-20, 2), (-34, 5)])
    with body(b, HARE):
        fill(ell(6, 8, 20, 10, 24), HARE_LIGHT)
        for x, y in ((-24, 40), (-10, 44), (-30, 30), (4, 42)):
            line([(x, y), (x + 3, y + 2), (x + 6, y + 1)], LINE*0.45, HARE_DARK)
    line([(-8, 6), (-10, 22), (-22, 32), (-36, 26)], LINE*0.8)
    shape(sm([(-42, 1), (-40, 7), (-22, 7), (-8, 4), (-8, 0.5), (-38, -0.5)]), HARE)
    tail = ell(-42, 30, 5.5, 7, 20)
    with body(tail, WHITE, sh=0): fill(ell(-40, 38, 6, 5, 16), HARE_DARK)
    tube([(16, 30), (18, 14), (19, 3)], 6.4, 5, HARE, sh=0.1)
    shape(ell(21, 1.8, 4.5, 2.2, 14), HARE)
    head = sm([(8, 44), (12, 58), (24, 64), (36, 58), (44, 48), (44, 42), (36, 38), (20, 36)])
    with body(head, HARE):
        fill(ell(38, 41, 9, 5, 18), HARE_LIGHT)
        fill(ell(29, 53, 7, 6, 18), HARE_LIGHT)
    eye(29, 53, 3.6, EYE_AMBER)
    shape(ell(44, 44, 1.6, 1.3, 10), PINK, LINE*0.5)
    line([(44, 42.6), (43.5, 40.5), (41, 39.5)], LINE*0.6)
    for k in (-1, 0, 1): line([(40, 42 + k), (52, 43 + k*3)], LINE*0.35)
    ear = sm([(16, 58), (12, 76), (13, 96), (19, 102), (24, 94), (24, 76), (24, 60)])
    with body(ear, HARE):
        fill(sm([(15, 66), (15, 84), (18, 94), (21, 84), (21, 66)]), HARE_LIGHT)
        fill(ell(19, 101, 8, 7, 18), INK)


@animal(1.0, dx=-4)
def srna():
    for lg in ([(-24, 36), (-22, 22), (-26, 12), (-25, 2)], [(12, 36), (14, 20), (13, 2)]):
        tube(lg, 5, 3, ROE_DARK, sh=0); shape(ell(lg[-1][0] + 0.6, lg[-1][1] + 0.5, 1.8, 2.2, 10), HOOF, LINE*0.6)
    b = sm([(-34, 42), (-30, 55), (-12, 59), (8, 58), (20, 56), (26, 46), (20, 34), (0, 32), (-20, 32), (-32, 34)])
    with body(b, ROE):
        fill(ell(-4, 30, 26, 6, 20), CREAM)
        fill(ell(-35, 45, 6, 9, 18), WHITE)
    for lg in ([(-20, 38), (-17, 22), (-21, 12), (-19, 2)], [(16, 38), (19, 20), (18, 2)]):
        tube(lg, 5.5, 3.2, ROE, sh=0.1); shape(ell(lg[-1][0] + 0.6, lg[-1][1] + 0.5, 1.9, 2.3, 10), HOOF, LINE*0.6)
    neck = sm([(8, 52), (16, 64), (24, 74), (36, 78), (38, 68), (30, 52), (24, 46)])
    shape(neck, ROE)
    with T(34, 76, 1.2):
        shape(sm([(-6, 6), (-13, 15), (-13, 23), (-7, 19), (-2, 9)]), ROE_DARK)
        head = sm([(-10, -4), (-8, 6), (0, 10), (10, 6), (18, -2), (20, -7), (16, -9), (4, -9), (-6, -8)])
        with body(head, ROE):
            fill(ell(19, -5.5, 3.6, 3.2, 14), INK)
            fill(ell(12, -9.5, 5, 2.6, 14), WHITE)
        ear = sm([(-3, 8), (-5, 19), (-1, 27), (5, 21), (4, 10)])
        with body(ear, ROE): fill(sm([(-2, 12), (-2, 19), (0, 24), (3, 19), (2, 12)]), CREAM)
        eye(4, 1, 3)
        smile(12, -6.5, 1.8)


@animal(0.9, dx=-2)
def jelen():
    for lg in ([(-24, 32), (-22, 18), (-26, 10), (-25, 2)], [(12, 32), (14, 16), (13, 2)]):
        tube(lg, 6, 3.8, STAG_MANE, sh=0); shape(ell(lg[-1][0] + 0.6, lg[-1][1] + 0.5, 2.2, 2.4, 10), HOOF, LINE*0.6)
    b = sm([(-34, 36), (-30, 51), (-12, 56), (8, 56), (20, 52), (26, 42), (20, 30), (0, 27), (-20, 27), (-32, 30)])
    with body(b, STAG):
        fill(ell(-4, 25, 26, 6, 20), STAG_MANE)
        fill(ell(-35, 40, 6, 9, 18), STAG_RUMP)
    for lg in ([(-20, 34), (-17, 18), (-21, 10), (-19, 2)], [(16, 34), (19, 16), (18, 2)]):
        tube(lg, 6.5, 4, STAG, sh=0.1); shape(ell(lg[-1][0] + 0.6, lg[-1][1] + 0.5, 2.3, 2.5, 10), HOOF, LINE*0.6)
    neck = zig(sm([(4, 50), (10, 60), (20, 68), (34, 68), (34, 58), (28, 44), (20, 38)]), 1.2, 2.6)
    with body(neck, STAG_MANE): pass

    def antler(g):
        tube(sm([(-2, 7), (-7, 18), (-10, 30), (-7, 40)], False), 3.6, 2.4, g, sh=0)
        for p, m, q in (((-3, 10), (4, 12), (9, 17)), ((-5, 15), (1, 18), (5, 23)), ((-9, 27), (-5, 30), (-2, 35)), ((-10, 33), (-13, 37), (-14, 42))):
            tube([p, m, q], 2.6, 1.6, g, sh=0)
    with T(32, 66, 1.2):
        with T(-9, -1, 1, rot=8): antler(HORN)
        shape(sm([(-5, 5), (-13, 10), (-14, 14), (-8, 13), (-2, 8)]), STAG)
        head = sm([(-10, -4), (-8, 6), (0, 9), (10, 5), (19, -3), (21, -8), (17, -10), (4, -10), (-6, -9)])
        with body(head, STAG):
            fill(ell(20, -6.5, 3.6, 3.2, 14), INK)
            fill(ell(13, -10.5, 5, 2.6, 14), CREAM)
        eye(4, 0, 3)
        smile(13, -7.5, 1.8)
        antler(ANTLER)


@animal(0.95)
def liska():
    tail = sm([(-22, 38), (-34, 40), (-46, 34), (-56, 22), (-54, 14), (-44, 16), (-32, 26), (-20, 30)])
    with body(tail, FOX): fill(ell(-55, 15, 8, 7, 18), WHITE)
    for lg in ([(-18, 28), (-20, 14), (-22, 2)], [(14, 28), (16, 14), (17, 2)]):
        o = tube(lg, 5.5, 4, FOX_DARK, sh=0)
    b = sm([(-26, 34), (-22, 48), (-4, 52), (14, 50), (24, 44), (26, 32), (16, 25), (-4, 24), (-20, 26)])
    with body(b, FOX): fill(ell(18, 30, 10, 9, 18), WHITE)
    for lg in ([(-14, 30), (-14, 14), (-17, 2)], [(18, 30), (20, 14), (22, 2)]):
        o = tube(lg, 6.5, 4.5, FOX, sh=0.1)
        C.saveState(); C.clipPath(poly(o), stroke=0, fill=0); fill(rrect(lg[-1][0] - 8, -2, 16, 16, 1), FOX_DARK); C.restoreState()
        stroke(o, LINE, closed=True)
        shape(ell(lg[-1][0] + 1.5, lg[-1][1] + 0.3, 3.8, 2, 12), FOX_DARK)
    shape(sm([(22, 62), (18, 76), (26, 70)]), FOX_DARK)
    head = sm([(16, 46), (18, 60), (26, 68), (36, 68), (44, 62), (54, 58), (54, 54), (42, 50), (30, 44)])
    with body(head, FOX):
        fill(sm([(30, 44), (42, 50), (54, 53), (52, 49), (38, 44), (26, 42)]), WHITE)
        fill(sm([(16, 46), (22, 54), (30, 54), (32, 46)]), WHITE)
    ear = sm([(28, 64), (32, 82), (38, 66)])
    with body(ear, FOX): fill(sm([(30, 74), (32, 84), (36, 74), (33, 78)]), FOX_DARK)
    shape(ell(54, 55.5, 2, 1.7, 12), INK, LINE*0.5)
    eye(38, 60, 3.2)
    smile(46, 52, 2.4)
    for k in (-1, 1): line([(48, 54 + k), (58, 55 + k*2.5)], LINE*0.3)


@animal(1.0, dx=-2)
def jezevec():
    for lg in ([(-28, 18), (-30, 2)], [(16, 18), (18, 2)]):
        tube(lg, 7, 6, BADGER_DARK, sh=0)
    shape(sm([(-40, 30), (-48, 28), (-46, 24), (-40, 24)]), BADGER)
    b = sm([(-42, 16), (-42, 32), (-30, 44), (-10, 50), (10, 48), (24, 40), (30, 28), (26, 14), (-30, 10)])
    with body(b, BADGER):
        fill(sm([(-44, 20), (-20, 18), (10, 18), (32, 20), (32, 0), (-44, 0)]), BADGER_DARK)
        for x in range(-34, 20, 7):
            line([(x, 44 - abs(x)*0.25), (x - 2, 34 - abs(x)*0.2)], LINE*0.4, K("#6e6d68"))
    for lg in ([(-22, 18), (-24, 2)], [(20, 18), (22, 2)]):
        tube(lg, 8, 7, BADGER_DARK, sh=0.1)
        for k in range(3): line([(lg[-1][0] + 1 + k*1.6, 1), (lg[-1][0] + 2.2 + k*1.6, -0.6)], LINE*0.6, WHITE)
    head = sm([(16, 42), (22, 48), (34, 46), (46, 36), (54, 26), (52, 21), (40, 22), (24, 26), (16, 32)])
    with body(head, WHITE):
        fill(sm([(22, 49), (30, 48), (40, 40), (50, 30), (54, 26), (52, 24), (44, 30), (34, 36), (24, 40), (16, 42)]), BADGER_DARK)
        fill(sm([(40, 22), (46, 26), (52, 24), (52, 21), (44, 20)]), BADGER_DARK)
    shape(ell(22, 46, 4.2, 3.6, 14), BADGER_DARK); fill(ell(22, 48, 2.6, 1.5, 10), WHITE)
    shape(ell(53, 23, 2.4, 2.2, 12), INK, LINE*0.5)
    shape(ell(37, 37, 2.5, 2.6, 14), K("#4a4646"), LINE*0.35)
    dot(37.8, 37.9, 0.9, 1.0)
    smile(46, 22, 2, INK)


@animal(1.0, dx=-3)
def divocak():
    for lg in ([(-28, 22), (-30, 2)], [(18, 22), (20, 2)]):
        tube(lg, 7, 5.5, BOAR_DARK, sh=0)
    tl = sm([(-40, 40), (-46, 36), (-48, 28)], False)
    stroke(tl, LINE*1.4, g=INK); shape(ell(-48, 26, 1.8, 3, 10), BOAR_DARK, LINE*0.6)
    top = zig(sm([(-40, 20), (-42, 38), (-28, 54), (-6, 62), (14, 58), (28, 50), (34, 34), (30, 18), (-34, 16)]), 1.4, 2.6)
    with body(top, BOAR):
        for x in range(-34, 26, 5):
            line([(x, 52 - abs(x + 6)*0.28), (x - 2, 42 - abs(x)*0.2)], LINE*0.45, BOAR_DARK)
        fill(ell(-4, 16, 40, 8, 24), BOAR_DARK)
    for lg in ([(-22, 22), (-24, 2)], [(24, 22), (26, 2)]):
        tube(lg, 8, 6, BOAR, sh=0.1)
        shape([(lg[-1][0] - 3, 3), (lg[-1][0] + 3.2, 3), (lg[-1][0] + 3.6, -0.5), (lg[-1][0] - 3.4, -0.5)], HOOF, LINE*0.6)
    head = sm([(20, 50), (32, 52), (44, 42), (52, 32), (56, 26), (52, 20), (38, 22), (24, 26), (18, 36)])
    with body(head, BOAR):
        for k in range(4): line([(26 + k*5, 48 - k*4), (24 + k*5, 42 - k*4)], LINE*0.4, BOAR_DARK)
    ear = zig(sm([(24, 50), (22, 64), (32, 54)]), 0.8, 2.4)
    with body(ear, BOAR_DARK, sh=0): fill(sm([(25, 52), (24, 60), (29, 54)]), SNOUT)
    shape(ell(55.5, 26, 3, 5.2, 16, rot=-10), SNOUT, LINE*0.8)
    dot(55, 27.5, 0.8, INK); dot(56, 24.3, 0.8, INK)
    shape(ell(38, 39, 2.6, 2.6, 14), WHITE, LINE*0.5); eye(38.3, 39, 2)
    smile(47, 23, 2.4)


@animal(1.05, dx=-2)
def veverka():
    tail = sm([(-4, 12), (-24, 10), (-38, 26), (-40, 50), (-34, 72), (-22, 90), (-6, 100), (6, 96), (-2, 90), (-16, 82), (-22, 64), (-18, 44), (-10, 28), (-2, 20)])
    tail = zig(tail, 1.0, 2.8)
    with body(tail, SQ):
        for k in range(9):
            a = k*0.35
            x, y = -24 + 8*math.sin(a*1.4), 20 + k*9
            line([(x - 6, y - 2), (x, y + 3), (x + 5, y + 1)], LINE*0.45, SQ_DARK)
    b = sm([(-12, 8), (-14, 26), (-6, 44), (6, 54), (18, 50), (22, 36), (20, 18), (12, 6)])
    with body(b, SQ): fill(ell(18, 30, 7, 18, 18), CREAM)
    line([(0, 6), (-6, 18), (-2, 28), (10, 30)], LINE*0.8)
    shape(sm([(-10, 1), (-8, 5), (10, 5), (16, 2), (14, -0.5), (-8, -0.5)]), SQ)
    shape(ell(34, 50, 6.5, 6, 18), NUT)
    with body(sm([(28, 52), (30, 58), (36, 58), (40, 54), (38, 51)]), NUT_CAP, sh=0): pass
    dot(35.5, 47.5, 1, CREAM)
    head = sm([(8, 62), (10, 74), (22, 80), (32, 76), (38, 66), (34, 58), (18, 56)])
    with body(head, SQ): fill(ell(30, 58, 10, 5, 16), CREAM)
    for sx, g in ((4, SQ_DARK), (0, SQ)):
        ear = sm([(10 + sx, 74), (8 + sx, 88), (12 + sx, 98), (16 + sx, 90), (20 + sx, 78)])
        shape(zig(ear, 0.8, 2.2) if sx == 0 else ear, g)
    for p in ([(20, 50), (26, 52), (30, 50)], [(18, 46), (26, 46), (30, 45)]):
        tube(p, 4.5, 3.8, SQ, sh=0)
    eye(26, 69, 3.4)
    shape(ell(37.5, 64.5, 1.5, 1.2, 10), INK, LINE*0.4)
    smile(34, 61, 1.8)
    for k in (-1, 1): line([(35, 63 + k), (44, 64 + k*3)], LINE*0.3)


@animal(1.08, dx=-3)
def jezek():
    for x in (-18, 18): tube([(x, 10), (x + 1, 2)], 5, 4, HOG_FACE, sh=0)
    dome = sm([(-40, 10), (-42, 24), (-32, 40), (-12, 48), (8, 46), (22, 38), (26, 22), (22, 10), (-10, 6)])
    spikes = zig(dome, 3.2, 2.8)
    with body(spikes, HOG_SPINE, sh=0.1):
        r = random.Random(4)
        for _ in range(110):
            x, y = r.uniform(-42, 24), r.uniform(8, 48)
            a = math.atan2(y - 8, x + 12)
            L = r.uniform(4, 6)
            line([(x, y), (x + math.cos(a)*L, y + math.sin(a)*L)], LINE*0.45, HOG_TIP if r.random() < 0.6 else INK)
    for x in (-24, 10): tube([(x, 10), (x + 1.5, 2)], 5.5, 4.4, HOG_FACE, sh=0.1); toes(x + 2.5, 2.5, 3, 1.4)
    face = sm([(14, 8), (12, 24), (22, 34), (34, 28), (46, 16), (52, 12), (50, 8), (36, 4), (22, 4)])
    with body(face, HOG_FACE): fill(ell(34, 8, 16, 5, 16), CREAM)
    shape(ell(20, 30, 3.6, 3.4, 14), HOG_FACE); fill(ell(20, 30, 1.8, 1.7, 10), PINK)
    shape(ell(51.5, 11, 2.2, 2, 12), INK, LINE*0.5)
    eye(34, 20, 2.7)
    smile(44, 8.5, 2.2)
    for k in (-1, 1): line([(46, 11 + k), (55, 12 + k*3)], LINE*0.3)


# ------------------------------------------------------------------ birds
@animal(1.08, dx=-2)
def kachna():
    for x in (-6, 6):
        tube([(x, 14), (x, 3)], 2.6, 2.2, DUCK_FOOT, lw=LINE*0.7, sh=0)
        shape(sm([(x - 3, 0), (x + 8, 0), (x + 4, 3.5), (x, 4)]), DUCK_FOOT, LINE*0.7)
    b = sm([(-46, 36), (-36, 44), (-14, 48), (8, 47), (22, 44), (30, 34), (28, 20), (16, 12), (-12, 11), (-32, 16), (-42, 26)])
    with body(b, DUCK_GREY):
        fill(ell(28, 32, 14, 18, 20), DUCK_BREAST)
        fill(ell(-46, 32, 13, 17, 20), WHITE)
        fill(ell(-49, 32, 12, 16, 20), INK)
        for x in range(-26, 16, 6): line([(x, 18), (x + 2, 24)], LINE*0.35, K("#9d998f"))
    stroke(sm([(-38, 42), (-39, 48), (-36, 50.5), (-33.5, 48.5), (-35, 46.5)], False), LINE*1.6)
    wing = sm([(-36, 40), (-20, 46), (6, 44), (14, 38), (2, 31), (-24, 29)])
    with body(wing, DUCK_WING, sh=0.08):
        fill([(-26, 29), (-6, 29), (-8, 36), (-28, 36)], WHITE)
        fill([(-25, 30.5), (-7.5, 30.5), (-9, 34.5), (-27, 34.5)], DUCK_BLUE)
    neck = sm([(14, 42), (18, 58), (20, 70), (28, 78), (38, 76), (40, 66), (34, 56), (30, 42)])
    with body(neck, DUCK_HEAD):
        fill([(0, 49), (40, 49), (40, 52), (0, 52)], WHITE)
        fill([(0, 40), (40, 40), (40, 49), (0, 49)], DUCK_BREAST)
        stroke(bez((22, 74), (26, 77), (32, 77), (35, 74)), LINE*1.4, g=K("#4fb07a", 0.7))
    bill = sm([(37, 70), (48, 69), (55, 65), (53, 62), (44, 63), (37, 64)])
    shape(bill, DUCK_BILL, LINE*0.9)
    dot(53.5, 64, 0.9, INK); dot(43, 67.5, 0.6, INK)
    eye(32, 70, 2.8)


@animal(1.0, dx=8)
def bazant():
    for dy, g in ((5, PHEAS_TAIL), (0, K("#c79a62"))):
        f = sm([(-8, 46 + dy), (-30, 56 + dy), (-54, 74 + dy), (-58, 74 + dy), (-34, 54 + dy), (-10, 38 + dy)])
        with body(f, g, sh=0.08):
            for k in range(1, 9):
                x = -8 - k*5.5; y = 44 + dy + k*3.6
                line([(x - 2, y + 4), (x + 2, y - 4)], LINE*0.6, PHEAS_DARK)
    tube([(2, 16), (0, 3)], 2.8, 2.4, LEG_GREY, lw=LINE*0.7, sh=0); toes(0, 3, 3, 2.4, LEG_GREY)
    b = sm([(-20, 42), (-4, 50), (14, 50), (24, 42), (26, 28), (16, 16), (-2, 14), (-16, 22), (-24, 32)])
    with body(b, PHEAS):
        r = random.Random(2)
        for i in range(-24, 28, 5):
            for j in range(14, 52, 5):
                x = i + (j % 10)*0.5 + r.uniform(-0.6, 0.6)
                line([(x - 1.4, j + 1), (x, j - 0.6), (x + 1.4, j + 1)], LINE*0.45, PHEAS_DARK)
    wing = sm([(-22, 38), (-6, 48), (10, 48), (12, 38), (-4, 32), (-18, 32)])
    with body(wing, PHEAS_WING, sh=0.08):
        for x, y in ((-14, 40), (-6, 43), (2, 42), (-8, 36), (4, 36)):
            fill(ell(x, y, 3, 2, 10), PHEAS_DARK)
    tube([(10, 16), (12, 3)], 2.8, 2.4, LEG_GREY, lw=LINE*0.7, sh=0); toes(12, 3, 3, 2.4, LEG_GREY)
    neck = sm([(12, 44), (16, 58), (20, 68), (28, 72), (34, 68), (32, 58), (26, 44)])
    with body(neck, PHEAS_HEAD):
        fill([(0, 44), (40, 44), (40, 48), (0, 48)], WHITE)
        stroke(bez((18, 60), (20, 64), (22, 66), (26, 68)), LINE*1.6, g=K("#3a8a6a", 0.7))
    shape(sm([(22, 70), (15, 76), (18, 72), (20, 68)]), PHEAS_HEAD, LINE*0.8)
    shape(sm([(24, 68), (30, 70), (34, 66), (32, 58), (26, 58), (23, 63)]), PHEAS_RED, LINE*0.8)
    shape(sm([(33, 67), (40, 66), (41, 64), (33, 63)]), HORN, LINE*0.8)
    eye(29, 65, 2.2)


@animal(1.15, dx=-2)
def koroptev():
    shape(sm([(-36, 20), (-46, 22), (-44, 28), (-34, 28)]), K("#b0602a"))
    for x in (-8, 6): tube([(x, 10), (x, 2)], 2.8, 2.4, FOOT_PINK, lw=LINE*0.7, sh=0); toes(x, 2, 3, 2.4, FOOT_PINK)
    b = sm([(-38, 20), (-36, 36), (-24, 46), (-4, 50), (14, 50), (26, 42), (30, 28), (24, 14), (8, 8), (-20, 8), (-32, 12)])
    with body(b, PART_GREY):
        for x in range(-30, 30, 3):
            for y in range(12, 50, 3): dot(x + (y % 6)*0.5, y, 0.35, K("#8e908a"))
        for x in (-26, -18, -10):
            fill(ell(x + 3, 24, 2.6, 8, 16, rot=-8), K("#a85a2e"))
            fill(ell(x + 6.5, 24, 1.1, 7, 12, rot=-8), CREAM)
        fill(sm([(10, 18), (16, 24), (24, 22), (22, 14), (14, 12)]), PART_CHEST)
    back = sm([(-40, 22), (-30, 42), (-12, 50), (4, 50), (-8, 42), (-26, 32)])
    with body(back, PART_BROWN, sh=0.08):
        for x, y in ((-30, 34), (-22, 40), (-14, 44), (-24, 32), (-6, 46)):
            line([(x - 3, y - 1), (x + 3, y + 1.5)], LINE*0.9, CREAM)
    head = ell(28, 50, 12, 11, 30)
    with body(head, PART_BROWN):
        fill(sm([(16, 50), (22, 44), (30, 38), (40, 44), (42, 54), (32, 56), (22, 56)]), PART_FACE)
    shape(sm([(38, 52), (44, 50), (39, 47)]), K("#9aa0a0"), LINE*0.8)
    eye(31, 52, 2.8)


@animal(1.0, dx=-6)
def volavka():
    tube([(-4, 44), (-6, 24), (-8, 3)], 3.2, 2.6, K("#a88c4c"), lw=LINE*0.8, sh=0); toes(-7, 3, 3, 3.5, K("#a88c4c"))
    wing_tip = sm([(-36, 44), (-40, 36), (-26, 38), (-12, 44)])
    shape(wing_tip, HERON_DARK)
    b = sm([(-34, 44), (-22, 58), (0, 66), (14, 64), (20, 56), (14, 44), (0, 38), (-20, 38)])
    with body(b, HERON):
        fill(sm([(4, 42), (12, 46), (18, 54), (22, 50), (16, 40)]), INK)
        for y in (54, 50, 46):
            line([(-28, y - 4), (-10, y + 2), (6, y + 4)], LINE*0.45, HERON_DARK)
    tube([(6, 42), (6, 24), (4, 3)], 3.4, 2.8, HERON_LEG, lw=LINE*0.8, sh=0.1); toes(5, 3, 3, 3.5, HERON_LEG)
    neck = sm([(10, 60), (18, 70), (16, 80), (18, 90), (26, 96), (32, 94), (26, 86), (24, 76), (26, 64), (22, 54)])
    with body(neck, HERON_NECK):
        for y in range(62, 88, 5): line([(23 - (y - 60)*0.1, y), (24.5 - (y - 60)*0.1, y - 2.5)], LINE*0.8, INK)
    head = ell(27, 95, 7.5, 6.5, 24)
    with body(head, WHITE):
        fill(sm([(29, 97), (22, 101), (14, 100), (18, 97), (24, 94)]), INK)
    stroke(sm([(20, 100), (10, 101), (0, 98)], False), LINE*1.9)
    stroke(sm([(18, 98), (8, 97),

(2, 94)], False), LINE*1.3)
    bill = sm([(32, 98), (44, 95), (54, 92), (44, 91), (32, 91)])
    shape(bill, HERON_BILL, LINE*0.8)
    eye(29.5, 96, 2, EYE_GOLD)


@animal(1.05, dx=2)
def sojka():
    twig(-44, 44, 8)
    shape(sm([(-14, 30), (-44, 16), (-48, 22), (-16, 40)]), INK)
    for x in (-2, 8): bird_foot(x, 10)
    b = sm([(-22, 34), (-10, 50), (10, 58), (26, 58), (32, 48), (28, 32), (16, 20), (0, 14), (-16, 22)])
    with body(b, JAY):
        fill(ell(-18, 28, 7, 6, 14), WHITE)
        fill(ell(16, 28, 14, 12, 18), K("#dcc2b2"))
    wing = sm([(-30, 32), (-12, 48), (6, 52), (14, 42), (4, 28), (-14, 26)])
    with body(wing, JAY, sh=0.08):
        fill(sm([(-32, 30), (-16, 32), (-6, 30), (-10, 24)]), INK)
        fill(sm([(-14, 34), (-4, 38), (0, 30), (-12, 28)]), WHITE)
        fill(sm([(0, 36), (6, 46), (14, 48), (16, 38), (6, 30)]), JAY_BLUE)
        for k in range(5): line([(2 + k*2.6, 32 + k*0.5), (5 + k*2.6, 46 - k*0.3)], LINE*0.9, INK)
        fill(sm([(-16, 38), (-10, 46), (-4, 44), (-8, 38)]), INK)
    head = sm([(14, 50), (16, 64), (22, 72), (32, 70), (40, 62), (38, 52), (28, 48)])
    with body(head, JAY):
        fill(sm([(14, 62), (18, 72), (28, 74), (36, 68), (28, 64)]), JAY_CROWN)
        for x in (19, 23, 27, 31): line([(x, 71), (x - 1.5, 66)], LINE*0.6, INK)
        fill(sm([(38, 56), (32, 52), (26, 48), (28, 46), (36, 51)]), INK)
    shape(sm([(38, 62), (46, 59), (48, 56), (38, 56)]), K("#3c3a3a"), LINE*0.8)
    eye(32, 61, 2.9, EYE_PALE)


@animal(1.05, dx=0)
def kos():
    tail = sm([(-16, 32), (-46, 22), (-48, 28), (-18, 42)])
    with body(tail, BB, sh=0): line([(-18, 36), (-44, 25)], LINE*0.5, BB_EDGE)
    for x in (-2, 8):
        tube([(x, 16), (x - 1, 3)], 2.4, 2.1, K("#4a3a30"), lw=LINE*0.7, sh=0); toes(x - 1, 3, 3, 2.6, K("#4a3a30"))
    b = sm([(-24, 36), (-10, 50), (10, 58), (24, 56), (30, 44), (26, 28), (14, 18), (-2, 16), (-16, 24)])
    with body(b, BB, sh=0.2): pass
    wing = sm([(-30, 34), (-12, 48), (6, 50), (12, 40), (2, 28), (-16, 26)])
    with body(wing, BB, sh=0.15):
        for k in range(4): line([(-26 + k*6, 30 + k*1.5), (-6 + k*4, 44 - k*1)], LINE*0.6, BB_EDGE)
    head = sm([(12, 52), (14, 66), (22, 74), (32, 72), (38, 62), (34, 52), (24, 48)])
    with body(head, BB, sh=0.15): pass
    worm = sm([(40, 60), (44, 54), (40, 46), (46, 40), (44, 34)], False)
    tube(worm, 3.2, 2.4, WORM, lw=LINE*0.7, sh=0)
    shape(sm([(36, 66), (48, 62), (50, 60), (36, 59)]), BB_BILL, LINE*0.8)
    shape(ell(29, 64, 4.4, 4.4, 20), BB_BILL, LINE*0.5)
    eye(29.3, 64, 3)


@animal(1.12, dx=0)
def sykora():
    twig(-42, 40, 6)
    tail = sm([(-14, 26), (-40, 16), (-42, 22), (-14, 34)])
    with body(tail, TIT_WING): line([(-16, 26), (-40, 17)], LINE*1.2, WHITE)
    for x in (-2, 8): bird_foot(x, 8, K("#7a8a9a"))
    b = sm([(-20, 30), (-12, 46), (6, 56), (22, 54), (30, 44), (28, 28), (16, 14), (-2, 10), (-16, 18)])
    with body(b, TIT_YEL):
        fill(sm([(-22, 30), (-12, 48), (4, 56), (-2, 42), (-10, 28)]), TIT_BACK)
        fill(sm([(24, 50), (22, 38), (16, 24), (8, 12), (12, 12), (20, 24), (28, 38), (30, 48)]), INK)
    wing = sm([(-26, 28), (-12, 42), (2, 46), (8, 38), (0, 26), (-14, 22)])
    with body(wing, TIT_WING, sh=0.08):
        line([(-2, 42), (-8, 32), (-14, 26)], LINE*1.3, WHITE)
        for k in range(3): line([(-22 + k*5, 27 + k), (-12 + k*4, 38 - k)], LINE*0.6, K("#4e627a"))
    head = sm([(10, 50), (12, 64), (20, 72), (32, 70), (38, 60), (34, 48), (22, 44)])
    with body(head, INK):
        fill(ell(26, 57, 8, 5.5, 18, rot=10), WHITE)
        fill(ell(14, 60, 3, 2.2, 10), K("#f4eed2"))
    shape(sm([(36, 63), (43, 61), (36, 58)]), K("#3a3a3a"), LINE*0.8)
    shape(ell(30, 64, 3.2, 3.2, 16), K("#3a3636"), LINE*0.3)
    dot(30.8, 64.9, 1.0, 1.0)


@animal(1.0, dx=4)
def datel():
    trunk = [(-46, 1)] + sm([(-46, 1), (-45, 60), (-46, 96), (-40, 104), (-35, 99), (-30, 106), (-24, 98), (-23, 60), (-22, 1)], False)
    with body(trunk, BARK):
        for x in (-41, -35, -29):
            line([(x, 2), (x + 1, 30), (x - 1, 60), (x + 1, 96)], LINE*0.6, BARK_DARK)
        for y in (16, 58, 84): shape(ell(-34, y, 1.8, 3.5, 10), BARK_DARK, LINE*0.4)
    shape(sm([(-14, 22), (-21, 4), (-16, 3), (-6, 18)]), WP)
    b = sm([(-20, 24), (-22, 50), (-16, 70), (-4, 80), (10, 78), (16, 62), (16, 42), (10, 24), (-4, 14), (-14, 14)])
    with body(b, WP, sh=0.25):
        stroke(sm([(10, 30), (14, 46), (13, 60)], False), LINE*1.4, g=K("#4a4852", 0.8))
    wing = sm([(-22, 28), (-22, 56), (-14, 72), (-6, 66), (-6, 40), (-12, 26)])
    with body(wing, WP, sh=0.2):
        for k in range(4): line([(-19 + k*3, 64 - k*3), (-17 + k*3, 32)], LINE*0.6, BB_EDGE)
    for y in (30, 48):
        tube([(-10, y + 3), (-18, y)], 2.8, 2.4, K("#6a6a70"), lw=LINE*0.7, sh=0)
        for d in (-3.5, 0, 3.5): stroke(sm([(-18, y), (-21, y + d), (-23, y + d*1.3 - 0.8)], False), LINE*1.1)
    head = sm([(-8, 76), (-8, 90), (2, 98), (14, 98), (22, 90), (20, 78), (8, 72)])
    with body(head, WP, sh=0.2):
        fill(sm([(-10, 88), (-4, 98), (8, 102), (20, 98), (24, 90), (12, 92), (0, 90)]), WP_RED)
    shape(sm([(-4, 96), (-14, 101), (-2, 100), (2, 98)]), WP_RED, LINE*0.8)
    shape(sm([(20, 90), (36, 87), (42, 85), (20, 81)]), WP_BILL, LINE*0.8)
    line([(22, 85.5), (38, 85.5)], LINE*0.4, K("#9a9070"))
    eye(11, 87, 3.4, K("#f2eed4"))


@animal(1.0, dx=0, dy=3)
def kane():
    twig(-40, 40, 10, leaf=False)
    tail = sm([(-10, 40), (-18, 4), (-8, 0), (2, 36)])
    with body(tail, BUZ_PALE):
        for y in range(6, 40, 6): line([(-20, y), (4, y + 3)], LINE*0.9, BUZ)
    b = sm([(-18, 30), (-20, 52), (-12, 72), (4, 80), (18, 72), (22, 52), (18, 30), (8, 20), (-8, 20)])
    with body(b, BUZ_PALE):
        for y in range(24, 42, 5):
            for x in range(-12, 22, 6): line([(x - 2, y), (x + 2, y + 1)], LINE*1.1, BUZ)
        fill(sm([(-4, 62), (4, 70), (18, 70), (24, 62), (22, 80), (0, 84)]), BUZ)
        for x in range(0, 20, 5): line([(x, 60), (x + 1, 54)], LINE*0.8, BUZ)
    wing = sm([(-24, 22), (-22, 54), (-14, 72), (-4, 70), (0, 50), (-4, 28)])
    with body(wing, BUZ, sh=0.1):
        for y in range(30, 70, 7): line([(-20, y), (-12, y + 3), (-4, y)], LINE*0.6, BUZ_PALE)
        fill([(-26, 20), (-6, 20), (-6, 30), (-26, 30)], BUZ_DARK)
    for x in (2, 12):
        tube([(x, 22), (x, 13)], 3.6, 3, BUZ_FOOT, lw=LINE*0.7, sh=0)
        for d in (-3, 0, 3): stroke(sm([(x, 13), (x + d, 10), (x + d + 0.8, 8)], False), LINE*1.2)
    head = ell(8, 84, 14, 12.5, 32)
    with body(head, BUZ):
        fill(ell(12, 78, 9, 5, 16), BUZ_PALE)
    shape(sm([(18, 86), (24, 85), (26, 82), (20, 80)]), BUZ_FOOT, LINE*0.7)
    shape(sm([(23, 86), (29, 84), (30, 78), (27, 76), (25, 80), (22, 82)]), K("#3a3434"), LINE*0.7)
    eye(13, 87, 3.2, K("#8a4a1e"))
    line([(8, 91), (13, 92.5), (17, 91)], LINE*0.9, BUZ_DARK)


@animal(1.0, dx=0)
def kulisek():
    twig(-40, 40, 8)
    tail = sm([(-6, 16), (-10, 2), (-2, 1), (4, 16)])
    with body(tail, OWL):
        for y in (3, 8, 13): fill(ell(-3, y, 3, 1, 10), WHITE)
    b = sm([(-22, 22), (-24, 44), (-18, 62), (0, 68), (18, 62), (24, 44), (22, 22), (12, 12), (-12, 12)])
    with body(b, OWL):
        fill(ell(2, 30, 15, 20, 24), WHITE)
        for x in (-6, 0, 6, 11):
            for y in (20, 30, 40): line([(x, y + 3), (x - 0.3, y - 2)], LINE*1.1, OWL)
    wing = sm([(-26, 20), (-26, 48), (-18, 60), (-12, 44), (-12, 22)])
    with body(wing, OWL_DARK, sh=0.08):
        for x, y in ((-22, 50), (-18, 42), (-22, 34), (-16, 30), (-20, 24), (-16, 52)):
            fill(ell(x, y, 1.5, 1.3, 10), WHITE)
    for x in (-5, 7):
        shape(ell(x, 12, 3.5, 3, 12), K("#e8dcc0"), LINE*0.7)
        for d in (-2, 0, 2): stroke(sm([(x + d, 11), (x + d*1.3, 8), (x + d*1.3 + 0.8, 6.5)], False), LINE*1.0)
    head = sm([(-24, 78), (-20, 94), (0, 100), (20, 94), (24, 78), (18, 64), (0, 60), (-18, 64)])
    with body(head, OWL):
        r = random.Random(3)
        for _ in range(26):
            x, y = r.uniform(-20, 20), r.uniform(84, 98)
            fill(ell(x, y, 1.1, 1.0, 8), WHITE)
        fill(ell(0, 76, 19, 13, 30), OWL_FACE)
        fill(ell(0, 64, 10, 5, 20), WHITE)
    for sx in (-1, 1):
        stroke(sm([(sx*2, 80), (sx*8, 86), (sx*16, 84)], False), LINE*2.0, g=WHITE)
        eye(sx*8.5, 77, 5.2, EYE_GOLD)
    shape(sm([(-2.2, 74), (2.2, 74), (0, 68.5)]), BEAK_Y, LINE*0.7)


@animal(1.0, dy=6)
def netopyr():
    for sx in (-1, 1):
        with T(0, 0, 1, flip=sx < 0):
            wing = sm([(6, 50), (18, 66), (32, 74), (54, 64), (46, 56), (48, 44), (38, 42), (34, 30), (22, 34), (10, 28)])
            with body(wing, BAT_WING, sh=0.1):
                for q in ((54, 64), (47, 45), (35, 31)):
                    line([(32, 72), q], LINE*0.7, BAT_BONE)
                line([(8, 52), (20, 66), (32, 72)], LINE*1.0, BAT_BONE)
            shape(sm([(31, 74), (30, 79), (34, 76)]), BAT_DARK, LINE*0.6)
            tube([(8, 30), (10, 22)], 2.6, 2, BAT_DARK, lw=LINE*0.6, sh=0)
    b = ell(0, 44, 12, 18, 30)
    with body(b, BAT): fill(ell(0, 34, 8, 10, 20), K("#c99060"))
    for sx in (-1, 1):
        ear = sm([(sx*4, 68), (sx*8, 80), (sx*14, 76), (sx*12, 64)])
        with body(ear, BAT_DARK): fill(ell(sx*9.5, 72, 2, 4, 10, rot=-sx*20), K("#6e4a36"))
    head = ell(0, 64, 12, 10.5, 30)
    with body(head, BAT): fill(ell(0, 59, 7.5, 5, 18), BAT_DARK)
    for sx in (-1, 1): eye(sx*5, 65, 2.6)
    fill(ell(-1.2, 61, 0.8, 0.6, 8), INK); fill(ell(1.2, 61, 0.8, 0.6, 8), INK)
    smile(0, 58, 2.4, K("#f0d0c0"))


# ------------------------------------------------------------------ amphibians, reptiles, fish, insects
@animal(1.18, dx=-4)
def zaba():
    b = sm([(-30, 12), (-32, 26), (-20, 38), (0, 46), (18, 48), (32, 44), (42, 34), (40, 26), (26, 18), (4, 12), (-14, 8)])
    with body(b, FROG):
        fill(ell(10, 14, 30, 10, 24), FROG_BELLY)
        for x, y in ((-18, 30), (-6, 38), (6, 42), (-10, 30), (-24, 24)): fill(ell(x, y, 2.4, 1.6, 10, rot=x*7), FROG_SPOT)
        fill(sm([(20, 40), (10, 36), (8, 28), (18, 26), (28, 32)]), FROG_DARK)
    line([(18, 48), (0, 44), (-18, 36)], LINE*0.8, K("#d8c48a"))
    thigh = ell(-20, 20, 18, 11, 30, rot=15)
    with body(thigh, FROG):
        for x in (-30, -22, -14, -6): fill(sm([(x, 10), (x + 2, 20), (x + 4, 30), (x + 5, 20), (x + 3, 10)]), FROG_DARK)
    shin = sm([(-36, 12), (-34, 6), (-10, 4), (0, 8), (-4, 12), (-24, 12)])
    with body(shin, FROG):
        for x in (-28, -18): fill([(x, 0), (x + 3, 0), (x + 3, 14), (x, 14)], FROG_DARK)
    foot = sm([(-10, 5), (6, 5), (22, 3), (26, 0), (22, -1), (-8, 0)])
    shape(foot, FROG)
    for x in (12, 18, 23): line([(x - 5, 2), (x, 0.5)], LINE*0.4)
    tube([(28, 26), (30, 12), (32, 2)], 5, 4, FROG, sh=0.1)
    for d in (-3, 0, 3): tube([(32, 2), (32 + d*1.3, 0)], 1.8, 2.2, FROG, lw=LINE*0.6, sh=0)
    shape(ell(24, 48, 7.5, 7, 22), FROG)
    eye(24.5, 49, 5.2, EYE_GOLD, slit=True)
    stroke(sm([(42, 32), (34, 28), (24, 28), (16, 30)], False), LINE*0.7)
    dot(40, 37, 0.7, INK)


@animal(1.2, dx=-2)
def ropucha():
    shin = sm([(-36, 8), (-34, 2), (-14, 1), (-8, 5), (-14, 8)])
    shape(shin, TOAD)
    b = sm([(-32, 8), (-38, 22), (-28, 38), (-8, 46), (14, 46), (30, 40), (38, 30), (36, 20), (24, 12), (0, 6), (-20, 4)])
    with body(b, TOAD):
        fill(ell(10, 10, 28, 9, 24), TOAD_BELLY)
        r = random.Random(11)
        for _ in range(38):
            x, y = r.uniform(-34, 30), r.uniform(16, 46)
            rr = r.uniform(1.2, 2.4)
            fill(ell(x, y, rr, rr*0.85, 12), TOAD_WART); dot(x + rr*0.3, y + rr*0.3, rr*0.35, K("#b88a60"))
    thigh = ell(-20, 16, 14, 10, 28, rot=10)
    with body(thigh, TOAD):
        r = random.Random(5)
        for _ in range(8):
            x, y = r.uniform(-30, -10), r.uniform(10, 24); fill(ell(x, y, 1.4, 1.2, 10), TOAD_WART)
    shape(sm([(-12, 4), (4, 4), (10, 1), (6, -0.5), (-10, 0)]), TOAD)
    shape(ell(10, 36, 10, 4.5, 24, rot=-12), K("#a47450"), LINE*0.8)
    for x in (4, 8, 12, 16): dot(x, 36 - (x - 10)*0.2, 0.6, TOAD_WART)
    tube([(26, 22), (27, 10), (27, 2)], 6.5, 5.5, TOAD, sh=0.1)
    for d in (-3, 0, 3): tube([(27, 2), (27 + d*1.2, 0)], 2.4, 2.4, TOAD, lw=LINE*0.6, sh=0)
    shape(ell(24, 40, 7, 6, 22), TOAD)
    eye(24.5, 41, 4.6, TOAD_EYE, slit=True)
    stroke(sm([(38, 26), (30, 24), (20, 26)], False), LINE*0.7)
    dot(36, 32, 0.7, INK)


@animal(0.97, dx=4, dy=16)
def pstruh():
    with T(0, 0, 1, rot=6):
        for fin in (sm([(-2, 44), (4, 56), (16, 52), (14, 44)]), sm([(-24, 42), (-22, 48), (-16, 46), (-18, 42)])):
            with body(fin, TROUT_FIN, sh=0): fill(ell(-19, 48, 5, 2, 10), TROUT_RED)
        for fin in (sm([(4, 18), (0, 8), (10, 10), (12, 18)]), sm([(-20, 22), (-24, 12), (-14, 14), (-12, 22)])):
            with body(fin, TROUT_FIN, sh=0): fill(ell(0, 12, 20, 3, 10), WHITE)
        tail = sm([(-38, 32), (-50, 46), (-56, 48), (-52, 34), (-56, 20), (-50, 20), (-38, 28)])
        with body(tail, TROUT_FIN):
            for y in (24, 30, 36, 42): line([(-40, 32), (-52, y)], LINE*0.4, K("#a88040"))
        b = sm([(-40, 30), (-26, 40), (0, 46), (24, 44), (40, 38), (48, 32), (44, 26), (24, 20), (0, 18), (-24, 22)])
        with body(b, TROUT_SIDE):
            fill(sm([(-44, 30), (-24, 42), (0, 50), (30, 48), (50, 36), (30, 38), (0, 38), (-24, 34)]), TROUT_BACK)
            fill(sm([(-40, 26), (-20, 25), (0, 23), (30, 23), (50, 28), (40, 16), (0, 14), (-30, 18)]), TROUT_BELLY)
            spots([(-20, 38), (-8, 40), (4, 42), (16, 40), (26, 40), (-14, 34), (10, 36), (-2, 35), (32, 36), (20, 35)], 1.2, INK)
            spots([(-24, 31), (-10, 29), (4, 30), (18, 30), (-17, 27), (10, 26)], 1.3, TROUT_RED, TROUT_HALO)
        line([(34, 40), (31, 32), (33, 24)], LINE*0.8)
        eye(40, 34, 3.2, EYE_GOLD)
        smile(46, 28, 2.2)
        fin = sm([(22, 28), (14, 22), (12, 26), (18, 30)])
        shape(fin, TROUT_FIN, LINE*0.8)


@animal(1.0, dx=6, dy=10)
def vazka():
    for sy in (1, -1):
        for x0, lx, w, tip in ((12, 2, 9, (4, 44)), (4, -12, 12, (-10, 42))):
            with T(0, 46, 1):
                pts = [(x0 - 3, 0), (x0 - 2 + lx*0.2, sy*16), (tip[0] + 2, sy*tip[1]), (tip[0] - 4, sy*(tip[1] - 2)), (x0 - w + lx*0.4, sy*18), (x0 - w*0.6, sy*2)]
                wing = sm(pts)
                fill(wing, WING)
                C.saveState(); C.clipPath(poly(wing), stroke=0, fill=0)
                fill(ell(x0 - 5, 0, 6, 8, 12), WING_BASE)
                for k in (-0.35, 0.0, 0.35):
                    stroke(sm([(x0 - 4, 0), (x0 - 4 + (tip[0] - x0)*0.5 + k*w, sy*tip[1]*0.5), (tip[0] + k*w*0.6, sy*tip[1])], False), LINE*0.35, g=WING_VEIN)
                fill(ell(tip[0] - 0.5, sy*(tip[1] - 5), 1.6, 3, 10), DART_DARK)
                C.restoreState()
                stroke(wing, LINE*0.8, closed=True)
    with T(0, 46, 1):
        ab = tube(sm([(8, 0), (-10, 0.5), (-30, 0), (-48, -1)], False), 6.5, 4.2, DART_RED, sh=0.1)
        for x in range(-6, -48, -6): line([(x, 2.6), (x, -2.6)], LINE*0.5, DART_DARK)
        for x in range(-10, -48, -6): fill(ell(x, -2.2, 1.3, 0.8, 8), INK)
        th = ell(12, 0, 9, 6.5, 24)
        with body(th, K("#b0482c")):
            for y in (-3, 3): line([(6, y), (18, y*1.2)], LINE*0.9, DART_DARK)
        head = ell(24, 0, 6, 9, 24)
        shape(head, K("#b8603a"))
        for sy in (1, -1):
            shape(ell(25, sy*4.5, 5.2, 4.8, 20), DART_EYE)
            dot(26.5, sy*4.5 + 1.8, 1.4, 1.0)
            dot(24.5, sy*4.5 - 1.6, 0.6, 1.0)
        smile(30, 0, 1.4)


@animal(1.0, dy=8)
def mravenec():
    with T(0, 0, 1):
        for lg in ([(0, 24), (-10, 34), (-18, 0)], [(6, 24), (4, 36), (2, 0)], [(12, 26), (22, 34), (30, 0)]):
            tube(sm(lg, False), 3.2, 2.2, K("#4a3a32"), lw=LINE*0.7, sh=0)
        gaster = ell(-26, 30, 18, 14, 36, rot=-10)
        with body(gaster, ANT_BLACK, sh=0.2):
            stroke(ell(-24, 34, 11, 7, 16, 60, 150), LINE*1.6, g=K("#6a6060"))
            for x in (-30, -22, -14): line([(x, 42 - (x + 22)*0.1), (x - 2, 18)], LINE*0.5, K("#4a4242"))
        shape(ell(-8, 28, 3.5, 4.5, 14), ANT_RED)
        th = sm([(-6, 28), (-2, 36), (8, 40), (16, 36), (16, 28), (6, 24)])
        with body(th, ANT_RED): fill(ell(4, 40, 8, 4, 14), ANT_BLACK)
        for lg in ([(-2, 26), (-12, 30), (-24, 0)], [(6, 26), (8, 32), (10, 0)], [(12, 28), (24, 30), (38, 0)]):
            tube(sm(lg, False), 3.6, 2.4, ANT_BLACK, lw=LINE*0.8, sh=0)
        head = ell(26, 38, 12, 11, 32, rot=-15)
        with body(head, ANT_RED): fill(ell(22, 48, 10, 5, 18), ANT_BLACK)
        for dx, g in ((-4, K("#5a4032")), (0, INK)):
            stroke(sm([(24 + dx, 46), (30 + dx, 62), (46 + dx, 70), (50 + dx, 64)], False), LINE*1.3, g=g)
        eye(28, 41, 4)
        shape(sm([(36, 34), (40, 30), (36, 30)]), K("#7a2c18"), LINE*0.6)
        smile(33, 31, 2)


@animal(1.0, dy=10)
def jesterka():
    tail = sm([(-14, 18), (-30, 14), (-46, 18), (-52, 30), (-46, 38)], False)
    t = tube(tail, 10, 2, LIZ_BROWN, sh=0.1)
    for lg in ([(-12, 16), (-8, 8), (-6, 2)], [(14, 16), (20, 10), (24, 4)]):
        tube(lg, 4, 3, K("#5a8a2a"), sh=0)
    b = sm([(-18, 14), (-14, 26), (0, 30), (14, 28), (26, 24), (22, 12), (8, 8), (-12, 8)])
    with body(b, LIZ_GREEN):
        fill(sm([(-20, 20), (0, 26), (22, 22), (22, 34), (-20, 34)]), LIZ_BROWN)
        fill(ell(4, 7, 22, 4, 18), LIZ_BELLY)
        spots([(-12, 25), (-2, 27), (8, 26), (18, 24)], 1.6, INK)
        for x, y in ((-12, 25), (-2, 27), (8, 26), (18, 24)): dot(x, y, 0.6, 1.0)
        spots([(-8, 18), (4, 19), (14, 17)], 1.2, K("#3e6a1e"))
    for lg in ([(-8, 14), (-14, 8), (-20, 2)], [(18, 14), (16, 8), (14, 2)]):
        tube(lg, 5, 3.5, LIZ_GREEN, sh=0.1)
        for d in (-3, -1, 1, 3): line([lg[-1], (lg[-1][0] + d*1.2, lg[-1][1] - 2.6)], LINE*0.7)
    head = sm([(20, 14), (24, 28), (36, 30), (48, 26), (52, 21), (44, 16), (30, 13)])
    with body(head, LIZ_GREEN): fill(sm([(24, 28), (36, 31), (48, 27), (40, 24), (28, 24)]), LIZ_BROWN)
    eye(38, 24, 2.8)
    smile(47, 19, 2)


@animal(1.0, dx=-2.5, dy=12)
def slepys():
    path = sm([(-52, 18), (-40, 8), (-24, 6), (-10, 16), (4, 28), (20, 26), (30, 14), (40, 12), (46, 20)], False)
    o = tube(path, 3, 13, SLOW, sh=0.14)
    C.saveState(); C.clipPath(poly(o), stroke=0, fill=0)
    stroke(path, LINE*0.9, g=SLOW_DARK)
    stroke([(x - 1, y + 2.2) for x, y in path], LINE*1.5, g=SLOW_SHINE)
    C.restoreState()
    head = sm([(38, 16), (40, 24), (48, 27), (56, 24), (58, 20), (52, 15), (44, 13)])
    with body(head, SLOW): stroke(sm([(38, 23), (46, 25.5), (54, 24)], False), LINE*1.4, g=SLOW_SHINE)
    eye(48, 21, 2.2, K("#c05a2a"), lid=True)
    smile(54, 17.5, 1.6)


@animal(1.0, dy=12)
def mlok():
    tail = sm([(-14, 18), (-30, 16), (-44, 10), (-54, 12)], False)
    t = tube(tail, 11, 3, SAL, sh=0.15)
    C.saveState(); C.clipPath(poly(t), stroke=0, fill=0)
    spots([(-24, 18), (-38, 14), (-48, 12)], 2.4, SAL_YEL); C.restoreState()
    for lg in ([(-10, 14), (-6, 6), (-4, 2)], [(14, 14), (20, 8), (24, 3)]):
        tube(lg, 5, 4, SAL, sh=0)
    b = sm([(-20, 12), (-18, 24), (-4, 28), (14, 28), (24, 22), (22, 10), (6, 6), (-12, 6)])
    with body(b, SAL, sh=0.2):
        for p in (sm([(-16, 24), (-8, 29), (-4, 24), (-12, 20)]), sm([(2, 28), (10, 30), (14, 25), (6, 22)]), sm([(-10, 14), (-4, 16), (-2, 11), (-8, 10)]), sm([(10, 14), (16, 17), (18, 12), (12, 10)])):
            fill(p, SAL_YEL)
    for lg in ([(-8, 12), (-14, 6), (-18, 1)], [(18, 12), (18, 6), (16, 1)]):
        o = tube(lg, 6, 4.6, SAL, sh=0.1)
        C.saveState(); C.clipPath(poly(o), stroke=0, fill=0); fill(ell(lg[1][0], lg[1][1] + 3, 3, 2.5, 10), SAL_YEL); C.restoreState()
        for d in (-2.4, 0, 2.4): tube([lg[-1], (lg[-1][0] + d, lg[-1][1] - 1.6)], 2, 2, SAL, lw=LINE*0.6, sh=0)
    head = sm([(20, 12), (22, 26), (32, 32), (44, 28), (50, 20), (44, 12), (30, 9)])
    with body(head, SAL, sh=0.2):
        fill(sm([(22, 26), (28, 32), (34, 32), (30, 26)]), SAL_YEL)
        fill(sm([(24, 20), (28, 24), (32, 20), (28, 17)]), SAL_YEL)
    shape(ell(38, 25, 4.4, 4.2, 20), K("#3a383e"), LINE*0.6)
    eye(38.4, 25.2, 3.4)
    smile(45, 16, 2, K("#8a8a90"))


ORDER = "zajic kachna bazant koroptev volavka zaba ropucha pstruh vazka veverka sojka kos sykora datel kane srna jelen liska jezevec divocak jezek mravenec jesterka slepys mlok kulisek netopyr".split()
ASSETS.sort(key=lambda a: ORDER.index(a[0]))
