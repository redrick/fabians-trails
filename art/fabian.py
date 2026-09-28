"""Fabián the Brdy forest spirit, peek-covers, keepsakes and UI icons."""
import math, random
from lib import C, Col, ell, bez, rrect, resample
from style3 import *
from style3 import _SC, curl_outline
import palette as P

FACE = Col(0.92, "#f3cfa6")
CHEEK = Col(0.0, "#ff6f7a", alpha=0.5)
NOSE = Col(0.78, "#eb9b83")
CONE = Col(0.5, "#a86a3a")
CONE_TIP = Col(0.65, "#cf955a")
CONE_LINE = Col(0.3, "#6b3f1f")
SLEEVE = Col(0.42, "#8a5832")
BOOT = Col(0.25, "#4a3222")
BOOT_CUFF = Col(0.35, "#6b4a30")
MOSS = Col(0.55, "#7fa33b")
MOSS_DARK = Col(0.4, "#557a2a")
MOSS_LIGHT = Col(0.75, "#b5cc5a")
HAT = Col(0.4, "#5b7446")
HAT_BAND = Col(0.3, "#6e4524")
FERN = Col(0.55, "#5f9d3c")
FERN_LIGHT = Col(0.7, "#86b84a")
FERN_DARK = Col(0.4, "#3f7430")
FERN_GOLD = Col(0.78, "#d8a33a")
FERN_RUST = Col(0.6, "#c0702e")
ROWAN = Col(0.5, "#e0472c")
LEAF_YEL = Col(0.85, "#f2c14e")
LEAF_ORANGE = Col(0.7, "#e98a2e")
LEAF_RED = Col(0.5, "#c8452e")
LEATHER = Col(0.5, "#a0683a")
LEATHER_FLAP = Col(0.58, "#bb7f4a")
BRASS = Col(0.85, "#e3b94a")
PIPE = Col(0.42, "#7a4424")
PIPE_STEM = Col(0.2, "#3a2a20")
EMBER = Col(0.7, "#ff9a3c")
SMOKE = Col(1.0, "#f4f1ea", alpha=0.85)
WHITE = Col(1.0, "#ffffff")
BUSH_DARK = Col(0.4, "#4f7a36")
BUSH = Col(0.55, "#6c9a3e")
BUSH_LIGHT = Col(0.68, "#8fb44c")
ROCK = Col(0.62, "#a3a6a8")
ROCK_LIGHT = Col(0.78, "#c4c6c4")
ROCK_DARK = Col(0.48, "#83878b")
LICHEN = Col(0.8, "#c9cc5c")
LICHEN_ORANGE = Col(0.7, "#e39a3e")
GRASS_DARK = Col(0.45, "#7f9437")
GRASS = Col(0.65, "#b3bf4a")
GRASS_LIGHT = Col(0.78, "#d4d06a")
GRASS_DRY = Col(0.75, "#d9b45c")
STRAW = Col(0.82, "#e8cf86")
REED_DARK = Col(0.5, "#958a4a")
REED = Col(0.7, "#cdb577")
REED_LIGHT = Col(0.82, "#e4d098")
REED_GREEN = Col(0.6, "#a6a458")
CATTAIL = Col(0.3, "#71431f")
LOG = Col(0.45, "#8a5f3c")
LOG_DARK = Col(0.3, "#5e3e24")
LOG_LIGHT = Col(0.58, "#a97d52")
WOOD_END = Col(0.85, "#e6c58f")
WOOD_RING = Col(0.65, "#c59a5e")
HEATHER_LEAF = Col(0.4, "#5f6b3a")
HEATHER_TWIG = Col(0.35, "#6b4a3a")
HEATHER_PINK = Col(0.7, "#d77fb8")
HEATHER_LIGHT = Col(0.82, "#efb0d8")
HEATHER_DEEP = Col(0.5, "#a64d8e")
RIBBON = Col(0.45, "#d83a3a")
PAPER = Col(0.95, "#f6ecd2")
PAPER_EDGE = Col(0.8, "#d9c49a")
SKY = Col(0.85, "#a9d6ee")
HILL = Col(0.6, "#7fae4c")
HILL_FAR = Col(0.72, "#a7c77a")
TOWER = Col(0.75, "#bdb6aa")
TOWER_DARK = Col(0.55, "#8f877b")
STAMP = Col(0.55, "#d8574a")
SILVER = Col(0.8, "#cfd3d6")
SILVER_DARK = Col(0.6, "#9ea5ab")
SILVER_LIGHT = Col(0.92, "#eef1f2")
IRON = Col(0.6, "#9aa2aa")
GLASS_BLUE = Col(0.45, "#2f7fd0")
GLASS_DEEP = Col(0.3, "#1f5aa0")
GLASS_YEL = Col(0.9, "#ffd84a")
CAM_BODY = Col(0.3, "#5a3a26")
CAM_TOP = Col(0.9, "#efe3c4")
LENS_GLASS = Col(0.3, "#2c4a6e")
BUTTON_RED = Col(0.45, "#d8434e")
WICKER = Col(0.7, "#d6a257")
WICKER_DARK = Col(0.5, "#a8743a")
BOOK_GREEN = Col(0.45, "#4f8a4a")
BOOK_GREEN_DARK = Col(0.32, "#386a36")
BOOK_BROWN = Col(0.4, "#8a5a34")
BOOK_BROWN_DARK = Col(0.28, "#63401f")
SUN = Col(0.9, "#ffd23f")
SUN_RAY = Col(0.75, "#ffae2e")
SUN_LIGHT = Col(0.97, "#fff0a0")
PALE = Col(0.9, "#e4ded4")
PALE_LINE = Col(0.7, "#b3aa9c")
GOLD = Col(0.8, "#eab83a")
GOLD_DARK = Col(0.55, "#b8862a")
PAW = Col(0.2, "#3a2e2a")
PAW_LIGHT = Col(0.3, "#56463f")
WALL = Col(0.95, "#f7ecd8")
ROOF = Col(0.45, "#d0473a")
ROOF_DARK = Col(0.35, "#a8352c")
DOOR = Col(0.4, "#8a5a34")
WINDOW = Col(0.8, "#bfe3f2")
SIGN = Col(0.6, "#c98f55")
SIGN_DARK = Col(0.45, "#9a6636")
SIGN_MARK = Col(0.95, "#fbf3dc")

S = 2.2


def mirror(pts):
    return [(-x, y) for x, y in pts]


def wavy(pts, n, amp):
    Q = resample(list(pts), 0.5)
    m = len(Q); out = []
    for i in range(m):
        a = Q[max(0, i-1)]; b = Q[min(m-1, i+1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1
        o = amp*abs(math.sin(math.pi*n*i/(m-1)))
        out.append((Q[i][0]-dy/L*o, Q[i][1]+dx/L*o))
    return out


def scales(clip, x0, x1, y0, y1, sw, sh, g=CONE, tip=CONE_TIP, line=CONE_LINE, lw=0.55):
    C.saveState(); C.clipPath(poly(clip), stroke=0, fill=0)
    j = 0; y = y0
    while y < y1 + sh:
        x = x0 - sw + (j % 2)*sw/2
        while x < x1 + sw:
            u = bez((x-sw/2, y+sh*0.4), (x-sw/2, y-sh*0.8), (x+sw/2, y-sh*0.8), (x+sw/2, y+sh*0.4))
            fill([(x-sw/2, y+sh*1.8)] + u + [(x+sw/2, y+sh*1.8)], g)
            if tip is not None: fill(ell(x, y-sh*0.15, sw*0.26, sh*0.26, 12), tip)
            stroke(u, LINE*lw, g=line)
            x += sw
        y += sh; j += 1
    C.restoreState()


def skin_hand(x, y, ang, r=3.0):
    with T(x, y, 1, rot=ang+90):
        palm = bez((-r*0.8, r*0.3), (-r, -r*0.8), (-r*0.8, -r*1.9), (0, -r*2.0)) + bez((0, -r*2.0), (r*0.8, -r*1.9), (r, -r*0.8), (r*0.8, r*0.3))
        shape(palm, FACE, LINE*0.9)
        stroke(bez((r*0.75, -r*0.2), (r*1.5, -r*0.3), (r*1.6, -r*1.1), (r*1.0, -r*1.3)), LINE*0.8)


def open_hand(x, y, ang, r=3.0, flip=False):
    with T(x, y, 1, flip=flip, rot=ang if not flip else 180-ang):
        thumb = bez((r*0.4, r*0.5), (r*0.6, r*1.6), (r*1.3, r*2.0), (r*1.7, r*1.6)) + bez((r*1.7, r*1.6), (r*1.9, r*1.2), (r*1.3, r*0.9), (r*1.2, r*0.3))
        shape(thumb, FACE, LINE*0.85)
        for k, (dy, L) in enumerate(((0.6, 1.25), (0.2, 1.4), (-0.22, 1.32), (-0.62, 1.1))):
            with T(r*1.5, r*dy, 1, rot=(dy)*14):
                shape(ell(r*L*0.62, 0, r*L*0.72, r*0.26, 16), FACE, LINE*0.8)
        palm = ell(r*0.9, 0, r*0.95, r*0.85, 24)
        shape(palm, FACE, LINE*0.9)


def arm(sx, sy, ua, fa, up=18.5, fo=15.5, w0=7.4, w1=6.4):
    ex, ey = sx + math.cos(math.radians(ua))*up, sy + math.sin(math.radians(ua))*up
    hx, hy = ex + math.cos(math.radians(fa))*fo, ey + math.sin(math.radians(fa))*fo
    tube([(sx, sy), (ex, ey)], w0, w0*0.95, SLEEVE)
    cx, cy = hx - math.cos(math.radians(fa))*2.6, hy - math.sin(math.radians(fa))*2.6
    tube([(ex, ey), (cx, cy)], w0*0.95, w1, SLEEVE)
    for (px, py), a in (((sx + ex)/2, (sy + ey)/2), ua), (((ex + cx)/2, (ey + cy)/2), fa):
        with T(px, py, 1, rot=a+90):
            stroke(ell(0, 0.8, 2.2, 1.6, 10, 200, 340), LINE*0.5, g=CONE_LINE)
    c0 = (cx - math.cos(math.radians(fa))*1.6, cy - math.sin(math.radians(fa))*1.6)
    tube([c0, (cx, cy)], w1+1.8, w1+1.8, MOSS, sh=0)
    return (hx, hy), fa


def pipe(x, y, s=1.0, rot=0, smoke=True, flip=False):
    with T(x, y, s, flip=flip, rot=rot):
        tube(bez((0, 0), (3, -1.3), (5.5, -1.9), (7.6, -1.3), 8), 1.3, 1.6, PIPE_STEM, sh=0)
        bowl = [(6.6, 4.2)] + bez((6.6, 4.2), (6.4, -0.6), (7.4, -2.8), (9, -2.8)) + bez((9, -2.8), (10.6, -2.8), (11.6, -0.6), (11.4, 4.2))
        form(bowl, PIPE, sdx=1.2, sdy=0, sh=0.15)
        shape(ell(9, 4.2, 2.4, 0.8, 16), PIPE_STEM, LINE*0.7)
        fill(ell(9, 4.3, 1.4, 0.45, 12), EMBER)
        if smoke:
            for dx, dy, r in ((9.6, 7.2, 1.3), (11.2, 10.4, 1.7), (10.2, 14.3, 2.1), (12.4, 18.6, 2.5)):
                shape(curl_outline(dx, dy, r, r*0.85, 0, 360, 5, 0.18), SMOKE, LINE*0.55)


# ------------------------------------------------------------------ Fabián
BODY = bez((0, 84), (12, 84.5), (19, 81.5), (21.5, 72)) + bez((21.5, 72), (25, 58), (25.5, 38), (20.5, 28)) + bez((20.5, 28), (15.5, 21), (7, 20.5), (0, 20.5))
BODY = BODY + mirror(list(reversed(BODY)))
HY = 95


def boot(ax, sx):
    shaft = rrect(ax-4.6, 3, 9.2, 9.5, 1.6)
    form(shaft, BOOT, sh=0.12)
    foot = [(x, max(y, 0.0)) for x, y in ell(ax+sx*2.4, 3.6, 7.0, 3.9, 30)]
    form(foot, BOOT, sdx=-sx*1.2, sdy=1, sh=0.14)
    stroke(ell(ax+sx*4.2, 4.6, 2.2, 1.2, 10, 30, 150), LINE*1.4, g=Col(0.5, "#7a5a44"), alpha=0.9)
    shape(rrect(ax-5.1, 10.5, 10.2, 2.8, 1.2), BOOT_CUFF, LINE*0.8)


def fern_frond(p0, p1, p2, p3, W, g, N=9, lw=0.8, rib=True, line=None, veins=False):
    R = bez(p0, p1, p2, p3, 40)
    m = len(R); left, right = [], []
    for i in range(m):
        a = R[max(0, i-1)]; b = R[min(m-1, i+1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1
        t = i/(m-1)
        w = W*(1-t)**0.75*min(1, 0.35+t*4)*(0.3+0.7*abs(math.sin(math.pi*t*N)))
        left.append((R[i][0]-dy/L*w, R[i][1]+dx/L*w)); right.append((R[i][0]+dy/L*w, R[i][1]-dx/L*w))
    shape(left + list(reversed(right)), g, LINE*lw)
    if rib:
        stroke(R[:-3], LINE*lw*0.7, g=line if line is not None else 0.0)
    if veins:
        for k in range(1, N - 1):
            t = (k + 0.5)/N; i = int(t*(m-1))
            j = min(m-1, i + 2)
            for sd in (1, -1):
                q = left[j] if sd > 0 else right[j]
                stroke([R[max(0, i-1)], (R[i][0]*0.3 + q[0]*0.7, R[i][1]*0.3 + q[1]*0.7)], LINE*0.4, g=line if line is not None else 0.0)


def rowan_berries(x, y, r=1.25, n=7):
    pts = [(0, 0), (1.9, 0.6), (-1.9, 0.5), (0.9, 2.0), (-1.0, 2.1), (2.4, 2.4), (-0.1, 3.6), (1.6, 4.0)][:n]
    for dx, dy in sorted(pts, key=lambda p: p[1], reverse=True):
        shape(ell(x+dx*r, y+dy*r, r, r, 14), ROWAN, LINE*0.6)
        dot(x+dx*r+r*0.35, y+dy*r+r*0.35, r*0.25, WHITE)


def rowan_leaf(x, y, ang, L=12, n=4, s=1.0):
    with T(x, y, s, rot=ang):
        stroke([(0, 0), (L, 0)], LINE*0.6, g=FERN_DARK)
        for i in range(n):
            px = L*(0.25 + 0.75*i/(n-1))
            for sd in (-1, 1):
                if i == n-1 and sd == 1: continue
                ang2 = 50*sd if i < n-1 else 0
                with T(px, 0, 1, rot=ang2):
                    shape(ell(2.2, 0, 2.2, 0.9, 12), FERN_LIGHT if i % 2 else FERN, LINE*0.5)


def birch_leaf(x, y, r, rot, g=LEAF_YEL):
    with T(x, y, 1, rot=rot):
        pts = bez((0, 0), (r*0.9, r*0.2), (r*1.1, r*1.3), (0, r*2.1)) + bez((0, r*2.1), (-r*1.1, r*1.3), (-r*0.9, r*0.2), (0, 0))
        shape(pts, g, LINE*0.6)
        stroke([(0, -r*0.4), (0, r*1.7)], LINE*0.45)


def hat():
    crown = [(-12.8, 103)] + bez((-12.8, 103), (-12.5, 112), (-10.5, 119), (-4.5, 120.8)) + bez((-4.5, 120.8), (-2, 119.2), (2, 119.2), (4.5, 120.8)) + \
            bez((4.5, 120.8), (10.5, 119), (12.5, 112), (12.8, 103)) + bez((12.8, 103), (5, 102), (-5, 102), (-12.8, 103))
    fern_frond((6, 106), (10, 112), (14, 118), (21, 121.5), 3.6, FERN, 8)
    fern_frond((7, 106), (12, 109), (17, 110), (23, 108), 3.0, FERN_GOLD, 7, line=FERN_RUST)
    form(crown, HAT, sdx=-2.2, sdy=0.6, sh=0.13)
    clip_fill(crown, [(-20, 103), (20, 103), (20, 107.6), (-20, 107.6)], HAT_BAND)
    stroke(bez((-13, 107.6), (-5, 106.8), (5, 106.8), (13, 107.6)), LINE*0.7)
    stroke(crown, LINE, closed=True)
    stroke(bez((0, 119.4), (-0.6, 117), (0.4, 115), (-0.2, 112.5)), LINE*0.7)
    rowan_leaf(10, 107.5, 150, 11, 4)
    birch_leaf(4.5, 104.5, 2.6, 25)
    rowan_berries(9.5, 105.6, 1.2)
    brim = bez((-21.5, 105.5), (-15, 101), (-8, 99.2), (0, 99.2)) + bez((0, 99.2), (8, 99.2), (15, 101), (21.5, 105.5)) + \
           bez((21.5, 105.5), (15, 104.4), (8, 104.2), (0, 104.3)) + bez((0, 104.3), (-8, 104.2), (-15, 104.4), (-21.5, 105.5))
    form(brim, HAT, sdx=0, sdy=1.2, sh=0.14)


def head(mood):
    for sx in (-1, 1):
        shape(ell(sx*12.6, HY-1, 2.3, 3.3, 16), FACE, LINE*0.9)
        stroke(ell(sx*12.8, HY-1, 1.1, 1.8, 10, 100 if sx > 0 else -80, 260 if sx > 0 else 80), LINE*0.5)
    shape(ell(0, HY, 12.6, 12.4, 40), FACE)
    r_out = bez((13.3, 102.5), (15.8, 93), (15.6, 82), (13.4, 72)) + bez((13.4, 72), (11.5, 62), (6, 53), (0, 50))
    outer = mirror(r_out) + list(reversed(r_out))
    r_in = bez((0, 87.6), (4, 86.6), (8, 85.8), (10.6, 88.5)) + bez((10.6, 88.5), (11.6, 91), (11.2, 97), (11.6, 102.5))
    beard = wavy(outer, 11, -1.5) + list(reversed(r_in)) + mirror(r_in)
    form(beard, MOSS, sdx=-2, sdy=1.2, sh=0.12)
    rr = random.Random(5)
    for (x, y) in ((-8, 76), (6, 72), (-3, 64), (7, 63), (-8, 66), (1, 56), (10, 80), (-11, 84), (12, 90)):
        stroke(ell(x, y, 2.2, 1.6, 10, 200, 340), LINE*0.5, g=MOSS_DARK)
    for i in range(14):
        x, y = rr.uniform(-11, 11), rr.uniform(55, 82)
        if abs(x) < 12 - (82-y)*0.3: dot(x, y, 0.55, MOSS_LIGHT)
    for sx in (-1, 1):
        fill(ell(sx*7.2, 90.5, 3.0, 1.9, 16), CHEEK)
    if mood == "talk":
        m = ell(0, 81.8, 3.2, 3.0, 20)
        shape(m, P.MOUTH, LINE*0.8)
        clip_fill(m, ell(0, 79.4, 2.4, 1.4, 12), P.TONGUE)
    else:
        m = bez((-3.6, 84), (-2, 80.6), (2, 80.6), (3.6, 84)) + [(0, 84.4)]
        shape(m, P.MOUTH, LINE*0.8)
        clip_fill(m, ell(0, 81, 1.8, 0.9, 12), P.TONGUE)
    if mood != "talk":
        pipe(2.2, 82.6, 1.0, rot=-8)
    for sx in (-1, 1):
        mst = bez((0, 87.6), (3, 89.4), (7.5, 88.6), (11, 90)) + bez((11, 90), (10.8, 86), (5, 82.6), (0, 84.8))
        shape(mirror(mst) if sx < 0 else mst, MOSS_LIGHT, LINE*0.9)
    stroke(bez((3, 86.8), (5, 86.4), (7, 86.4), (9, 87.4)), LINE*0.45, g=MOSS_DARK)
    stroke(bez((-3, 86.8), (-5, 86.4), (-7, 86.4), (-9, 87.4)), LINE*0.45, g=MOSS_DARK)
    shape(ell(0, 91.3, 3.0, 2.6, 20), NOSE, LINE*0.9)
    dot(0.9, 92.4, 0.7, WHITE)
    for sx in (-1, 1):
        x = sx*5.0
        shape(ell(x, 96.2, 2.7, 3.2, 20), WHITE, LINE*0.8)
        C.saveState(); C.setFillColor(G(0.0)); C.ellipse(x+0.2-1.8, 95.7-2.2, x+0.2+1.8, 95.7+2.2, fill=1, stroke=0); C.restoreState()
        dot(x+0.8, 96.7, 0.7, WHITE); dot(x-0.4, 94.9, 0.3, WHITE)
        brow = curl_outline(sx*5.3, 100.6, 3.4, 1.2, 0, 360, 6, 0.25)
        shape(brow, MOSS_LIGHT, LINE*0.7)
        stroke(bez((x+sx*2.8, 93.5), (x+sx*3.4, 93.0), (x+sx*3.6, 93.8), (x+sx*3.9, 94.6)), LINE*0.45)
    hat()


def bag():
    stroke(bez((-17.5, 79), (-6, 66), (8, 52), (15.5, 38)), LINE*3.4, g=0.0)
    stroke(bez((-17.5, 79), (-6, 66), (8, 52), (15.5, 38)), LINE*2.0, g=LEATHER)
    fern_frond((19, 37), (20, 42), (23, 46), (27, 49), 2.6, FERN_LIGHT, 6)
    b = rrect(8, 24, 17, 14.5, 2.8)
    form(b, LEATHER, sdx=2, sdy=0.8, sh=0.13)
    flap = [(8, 38.5)] + bez((8, 38.5), (8, 31), (25, 31), (25, 38.5))
    shape(flap, LEATHER_FLAP, LINE*0.9)
    stroke(bez((9.8, 36.8), (10.4, 33.4), (22.6, 33.4), (23.2, 36.8)), LINE*0.4, g=LEATHER)
    shape(rrect(14.9, 30.8, 3.2, 3.4, 0.8), BRASS, LINE*0.7)


def body():
    for sx in (-1, 1):
        tube([(sx*7.4, 26), (sx*7.6, 17), (sx*7.8, 10)], 8.4, 7.4, SLEEVE)
        boot(sx*7.8, sx)
    fill(BODY, CONE)
    scales(BODY, -26, 26, 22, 86, 7.2, 5.6)
    offset_shadow(BODY, -3.5, 1.6, 0.13)
    stroke(BODY, LINE, closed=True)


def fabian(pose):
    def draw(b):
        with T(b.w/2, 8, S):
            body()
            bag()
            shoulder_l, shoulder_r = (-19, 76.5), (19, 76.5)
            if pose == "wave":
                h, fa = arm(*shoulder_l, 128, 97)
                open_hand(h[0], h[1], fa - 180, 3.2, flip=True)
            elif pose == "talk":
                h, fa = arm(*shoulder_l, -106, 132)
                open_hand(h[0], h[1], fa - 180, 3.2, flip=True)
            else:
                h, fa = arm(*shoulder_l, -108, -92)
                skin_hand(h[0], h[1], fa, 3.1)
            if pose != "talk":
                h, fa = arm(*shoulder_r, -72, -88)
                skin_hand(h[0], h[1], fa, 3.1)
            head("talk" if pose == "talk" else "happy")
            if pose == "talk":
                h, fa = arm(*shoulder_r, -68, 150)
                pipe(h[0] - 9.6, h[1] + 0.6, 1.0, rot=0)
                skin_hand(h[0], h[1], fa, 3.1)
    return draw


# ------------------------------------------------------------------ covers
def blade(x0, x1, y1, w, g, bend, lw=0.75, y0=-3):
    mx = (x0 + x1)/2 + bend
    L = bez((x0 - w/2, y0), (mx - w*0.35, (y0 + y1)/2), (x1 - bend*0.15, y1 - (y1 - y0)*0.2), (x1, y1))
    R = bez((x1, y1), (x1 - bend*0.05 + w*0.1, y1 - (y1 - y0)*0.25), (mx + w*0.35, (y0 + y1)/2), (x0 + w/2, y0))
    shape(L + R, g, LINE*lw)


def base_mass(y_lo, y_hi, g, seed, step=9):
    r = random.Random(seed)
    top = []
    x = 204
    while x > -6:
        top.append((x, r.uniform(y_hi - 6, y_hi)))
        top.append((x - step/2, r.uniform(y_lo, y_lo + 5)))
        x -= step
    pts = [(-4, -3), (204, -3)] + top
    shape(pts, g, LINE*0.8)


def bush(b):
    r = random.Random(4)
    rows = ((BUSH_DARK, 7, -14, 36, (56, 76), (20, 28)), (BUSH, 6, 2, 38, (40, 50), (26, 30)), (BUSH_LIGHT, 9, -14, 28, (8, 16), (23, 27)))
    for g, n, x0, dx, yr, rr_ in rows:
        for i in range(n):
            x = x0 + i*dx + r.uniform(-5, 5); y = r.uniform(*yr); rad = r.uniform(*rr_)
            blob = curl_outline(x, y, rad, rad*0.92, r.uniform(0, 40), r.uniform(0, 40) + 360, 8, 0.12)
            form(blob, g, sdx=-5, sdy=4, sh=0.1)
            for k in range(3):
                a = r.uniform(30, 150); d = r.uniform(0.3, 0.7)*rad
                stroke(ell(x + math.cos(math.radians(a))*d, y + math.sin(math.radians(a))*d, 3, 2.2, 10, 200, 340), LINE*0.5, g=BUSH_DARK if g != BUSH_DARK else Col(0.3, "#3b5e28"))
            for k in range(r.choice((1, 2, 2, 3))):
                a = r.uniform(20, 160); d = r.uniform(0.35, 0.85)*rad
                lx, ly = x + math.cos(math.radians(a))*d, y + math.sin(math.radians(a))*d
                with T(lx, ly, 1, rot=r.uniform(0, 360)):
                    leaf = bez((0, -4.4), (3, -3), (3.2, 1.5), (0, 4.4)) + bez((0, 4.4), (-3.2, 1.5), (-3, -3), (0, -4.4))
                    shape(leaf, r.choice((LEAF_YEL, LEAF_ORANGE, LEAF_YEL, LEAF_RED)), LINE*0.6)
                    stroke([(0, -5.2), (0, 3)], LINE*0.4)


def rock(b):
    big = [(-6, -3), (206, -3), (205, 30), (196, 54), (176, 76), (146, 94), (108, 104), (76, 101), (46, 90), (22, 72), (6, 52), (-5, 30)]
    fill(big, ROCK)
    clip_fill(big, [(150, -5), (210, -5), (210, 40), (198, 62), (178, 80), (160, 60), (156, 30)], ROCK_DARK)
    top = [(34, 80), (46, 90), (76, 101), (108, 104), (146, 94), (170, 80), (140, 84), (106, 90), (72, 88), (50, 82)]
    fill(top, ROCK_LIGHT)
    stroke([(34, 80), (50, 82), (72, 88), (106, 90), (140, 84), (170, 80)], LINE*0.7)
    offset_shadow(big, -8, 4, 0.1)
    stroke(big, LINE, closed=True)
    stroke([(156, 30), (160, 60), (178, 80)], LINE*0.7)
    stroke([(96, 60), (104, 50), (100, 38), (108, 28)], LINE*0.7)
    stroke([(60, 70), (66, 62)], LINE*0.6); stroke([(128, 72), (124, 64), (130, 58)], LINE*0.6)
    r = random.Random(8)
    for (x, y, rad, g) in ((70, 94, 6, LICHEN), (84, 97, 3.5, LICHEN_ORANGE), (124, 92, 5, LICHEN), (40, 70, 4.5, LICHEN_ORANGE), (150, 70, 5.5, LICHEN),
                           (120, 50, 4, LICHEN_ORANGE), (30, 44, 5, LICHEN), (178, 50, 4, LICHEN), (84, 48, 3, LICHEN)):
        shape(curl_outline(x, y, rad, rad*0.8, 0, 360, 6, 0.3), g, LINE*0.5)
        for k in range(3): dot(x + r.uniform(-rad, rad)*0.5, y + r.uniform(-rad, rad)*0.4, 0.5, Col(0.5, "#8f8a38"))
    small = [(-6, -3), (64, -3), (62, 20), (50, 36), (30, 42), (10, 38), (-6, 26)]
    form(small, ROCK, sdx=-6, sdy=3, sh=0.12)
    fill([(18, 39), (30, 42), (50, 36), (40, 34), (24, 36)], ROCK_LIGHT)
    stroke([(18, 39), (24, 36), (40, 34), (50, 36)], LINE*0.6)
    shape(curl_outline(38, 22, 4, 3.2, 0, 360, 6, 0.3), LICHEN, LINE*0.5)
    moss = [(-6, -3), (206, -3), (206, 6)] + wavy([(206, 6), (-6, 6)], 22, 3.5)
    shape(moss, MOSS, LINE*0.8)
    for x in (12, 90, 150, 196):
        for k in range(4):
            blade(x + k*2.5, x + k*3.5 - 4 + r.uniform(-2, 2), r.uniform(14, 24), 2.4, GRASS if k % 2 else GRASS_DRY, r.uniform(-3, 3), 0.6)


def grass(b):
    r = random.Random(12)
    base_mass(64, 76, GRASS_DARK, 3)
    for layer, (n, hr, gs) in enumerate(((22, (80, 106), (GRASS, GRASS_DRY, GRASS_DARK)), (26, (60, 86), (GRASS, GRASS_LIGHT, GRASS_DRY)), (20, (34, 60), (GRASS_LIGHT, GRASS)))):
        for i in range(n):
            x0 = -6 + (i + r.random())*212/n
            h = r.uniform(*hr)
            lean = r.uniform(-14, 14)
            blade(x0, x0 + lean, h, r.uniform(5, 7.5), r.choice(gs), lean*0.4, 0.7)
        if layer == 0:
            for x in (18, 52, 96, 138, 176):
                top = r.uniform(94, 106); lean = r.uniform(-6, 6)
                stem = bez((x, -2), (x, 40), (x + lean*0.5, 80), (x + lean, top), 20)
                stroke(stem, LINE*1.9, g=0.0); stroke(stem, LINE*0.8, g=STRAW)
                for k in range(7):
                    t = 0.62 + k*0.052
                    px, py = stem[int(t*20)]
                    sd = 1 if k % 2 else -1
                    with T(px, py, 1, rot=90 + sd*28):
                        shape(ell(2.6, 0, 2.8, 1.25, 12), STRAW, LINE*0.55)


def reeds(b):
    r = random.Random(21)
    base_mass(64, 76, REED_DARK, 5)
    for i in range(20):
        x0 = -6 + (i + r.random())*212/20
        h = r.uniform(78, 100); lean = r.uniform(-10, 10)
        blade(x0, x0 + lean, h, r.uniform(5, 6.5), r.choice((REED, REED_GREEN, REED_DARK)), lean*0.3, 0.7)
    for x, top, lean in ((24, 104, -4), (70, 96, 3), (112, 107, -2), (150, 92, 5), (184, 101, -3)):
        stem = bez((x, -2), (x, 40), (x + lean*0.5, 80), (x + lean, top), 20)
        stroke(stem, LINE*2.6, g=0.0); stroke(stem, LINE*1.3, g=REED_GREEN)
        cx, cy = x + lean*0.9, top - 12
        cap = rrect(cx - 3.8, cy - 10, 7.6, 20, 3.6)
        form(cap, CATTAIL, sdx=-2, sdy=0, sh=0.18)
        stroke(ell(cx + 1.4, cy + 4, 0.8, 4, 10, 60, 120), LINE*0.9, g=Col(0.5, "#a0683a"))
        stroke([(cx, cy + 10), (cx + lean*0.1, cy + 17)], LINE*0.9)
    for i in range(22):
        x0 = -6 + (i + r.random())*212/22
        h = r.uniform(52, 86); lean = r.uniform(-18, 18)
        blade(x0, x0 + lean, h, r.uniform(5, 7), r.choice((REED, REED_LIGHT, REED_GREEN)), lean*0.5, 0.7)


def log(b):
    top = wavy([(-10, 68), (180, 69)], 6, 1.2)
    body = [(-10, -3), (180, -3)] + ell(180, 34, 15, 36, 30, -90, 90) + list(reversed(top))
    fill(body, LOG)
    C.saveState(); C.clipPath(poly(body), stroke=0, fill=0)
    fill([(-12, 54), (180, 54), (180, 72), (-12, 72)], LOG_LIGHT)
    r = random.Random(3)
    for y in (8, 18, 30, 42, 56, 62):
        x = -10
        while x < 175:
            L = r.uniform(24, 50)
            stroke(bez((x, y), (x + L*0.3, y + 1.5), (x + L*0.7, y - 1.5), (x + L, y + r.uniform(-1, 1))), LINE*0.6, g=LOG_DARK)
            x += L + r.uniform(6, 16)
    C.restoreState()
    offset_shadow(body, 0, 12, 0.13)
    stroke(body, LINE, closed=True)
    for kx, ky in ((40, 30), (128, 24)):
        shape(ell(kx, ky, 5, 3.2, 20), LOG_DARK, LINE*0.8)
        shape(ell(kx + 0.5, ky + 0.3, 2.6, 1.6, 14), LOG_LIGHT, LINE*0.5)
    end = ell(180, 34, 15, 36, 40)
    shape(end, LOG_DARK)
    shape(ell(180.6, 34, 12.6, 32.5, 40), WOOD_END, LINE*0.7)
    for k in (0.75, 0.52, 0.3):
        stroke(ell(181, 33, 12.6*k, 32*k, 30), LINE*0.5, closed=True, g=WOOD_RING)
    dot(181, 33, 1.0, WOOD_RING)
    stroke([(181, 33), (186, 52), (185, 60)], LINE*0.6); stroke([(181, 33), (176, 14)], LINE*0.5)
    br = [(84, 64), (90, 80), (96, 96)]
    tube(br, 12, 8, LOG, sh=0.14)
    shape(ell(96, 96, 4.2, 2.2, 16, rot=25), WOOD_END, LINE*0.9)
    stroke([(92, 72), (93, 86)], LINE*0.5, g=LOG_DARK)
    moss = wavy([(-12, 62), (30, 58), (70, 61), (110, 58), (150, 62), (168, 60)], 10, -2.5) + wavy([(168, 60), (150, 72), (110, 76), (70, 74), (30, 76), (-12, 72)], 14, -3.5)
    form(moss, MOSS, sdx=0, sdy=3, sh=0.1)
    for i in range(22):
        dot(r.uniform(-6, 160), r.uniform(64, 72), 0.8, MOSS_LIGHT)
    for x in (18, 60, 132):
        for k in range(4):
            blade(x + k*2.4, x + k*3.5 - 5 + r.uniform(-2, 2), r.uniform(82, 90), 2.6, GRASS if k % 2 else GRASS_DRY, 1.5, 0.6, y0=66)
    for x, y, rot, g in ((110, 77, 30, LEAF_ORANGE), (40, 78, -40, LEAF_YEL), (150, 72, 70, LEAF_RED)):
        with T(x, y, 1, rot=rot):
            leaf = bez((0, -4.4), (3, -3), (3.2, 1.5), (0, 4.4)) + bez((0, 4.4), (-3.2, 1.5), (-3, -3), (0, -4.4))
            shape(leaf, g, LINE*0.6); stroke([(0, -5.2), (0, 3)], LINE*0.4)
    shape([(-4, -3), (204, -3), (204, 4)] + wavy([(204, 4), (-4, 4)], 20, 2.5), MOSS, LINE*0.8)
    for x in range(-4, 206, 7):
        blade(x, x + r.uniform(-4, 4), r.uniform(8, 16), 3.4, r.choice((GRASS, GRASS_DRY, MOSS)), r.uniform(-2, 2), 0.6)


def fern(b):
    r = random.Random(7)
    shape([(-4, -3), (204, -3), (204, 60)] + wavy([(204, 60), (150, 70), (100, 66), (50, 72), (-4, 62)], 12, -5), FERN_DARK, LINE*0.8)
    for x in range(8, 200, 22):
        stroke(ell(x, 50 + (x % 3)*4, 5, 3, 10, 200, 340), LINE*0.5, g=Col(0.3, "#2e5a24"))
    fronds = [(-30, 70, FERN), (190, 66, FERN_GOLD), (30, 96, FERN), (160, 94, FERN_RUST), (70, 104, FERN_LIGHT), (120, 102, FERN),
              (-10, 50, FERN_LIGHT), (210, 52, FERN), (100, 80, FERN_GOLD), (50, 62, FERN), (150, 60, FERN_LIGHT), (100, 50, FERN)]
    for tx, ty, g in fronds:
        bx = 100 + (tx - 100)*0.35 + r.uniform(-8, 8)
        p0 = (bx, -4); p3 = (tx, ty)
        p1 = (bx + (tx - bx)*0.1, ty*0.9)
        p2 = (bx + (tx - bx)*0.6, ty + 12)
        fern_frond(p0, p1, p2, p3, 10 if ty > 60 else 8.5, g, 15, 0.75, line=FERN_DARK if g in (FERN, FERN_LIGHT) else FERN_RUST, veins=True)


def heather(b):
    r = random.Random(17)
    mounds = ((22, 44, 42, 40), (172, 46, 42, 38), (98, 52, 46, 36), (52, 24, 48, 34), (150, 22, 50, 34), (100, 8, 60, 26), (0, 6, 36, 30), (200, 6, 34, 30))
    for cx, cy, rx, ry in mounds:
        m = curl_outline(cx, cy, rx, ry, 0, 360, 16, 0.08)
        form(m, HEATHER_LEAF, sdx=-5, sdy=5, sh=0.12)
        C.saveState(); C.clipPath(poly(m), stroke=0, fill=0)
        for i in range(int(rx*ry/70)):
            a = r.uniform(10, 170); d = r.uniform(0.2, 1.0)
            x = cx + math.cos(math.radians(a))*rx*d; y = cy + math.sin(math.radians(a))*ry*d - 4
            g = r.choice((HEATHER_PINK, HEATHER_PINK, HEATHER_LIGHT, HEATHER_DEEP))
            for k in range(4):
                fill(ell(x + (k % 2 - 0.5)*1.6, y + k*2.1, 1.5 - k*0.2, 1.4, 8), g)
        for i in range(8):
            x = cx + r.uniform(-rx, rx)*0.8; y = cy + r.uniform(-ry, ry)*0.5
            stroke([(x, y), (x + r.uniform(-2, 2), y + 4)], LINE*0.45, g=HEATHER_TWIG)
        C.restoreState()
        stroke(m, LINE, closed=True)
        for k in range(5):
            a = r.uniform(50, 130)
            x = cx + math.cos(math.radians(a))*rx*0.95; y = cy + math.sin(math.radians(a))*ry*0.95
            sprig = bez((x, y - 4), (x, y), (x + r.uniform(-3, 3), y + 5), (x + r.uniform(-4, 4), y + 10))
            stroke(sprig, LINE*0.9, g=HEATHER_TWIG)
            for jj in range(4):
                px, py = sprig[4 + jj*3]
                shape(ell(px + 1.4*(1 if jj % 2 else -1), py, 1.4, 1.2, 8), HEATHER_PINK if jj % 2 else HEATHER_LIGHT, LINE*0.4)


# ------------------------------------------------------------------ keepsakes
def cone_shape(h=64, w=15):
    R = bez((0, h/2), (w*0.55, h/2), (w, h*0.25), (w, -h*0.05)) + bez((w, -h*0.05), (w, -h*0.3), (w*0.5, -h/2), (0, -h/2))
    return R + mirror(list(reversed(R)))


def cone(h=64, w=15, pale=False):
    out = cone_shape(h, w)
    if pale:
        tube([(0, h/2 - 2), (1.2, h/2 + 5)], 2.4, 2.0, PALE, lw=LINE, sh=0)
        fill(out, PALE)
        scales(out, -w, w, -h/2, h/2, w*0.62, h*0.1, PALE, None, PALE_LINE, 0.6)
        stroke(out, LINE, closed=True, g=PALE_LINE)
        return out
    tube([(0, h/2 - 2), (1.2, h/2 + 5)], 2.4, 2.0, SLEEVE, sh=0)
    fill(out, CONE)
    scales(out, -w, w, -h/2, h/2, w*0.62, h*0.1)
    offset_shadow(out, -w*0.3, 1, 0.14)
    stroke(out, LINE, closed=True)
    return out


def k_cone(b):
    with T(b.w/2, b.h/2 - 2, 1, rot=-28):
        cone(66, 15.5)
        tail = bez((0, 25), (-6, 20), (-9, 14), (-8, 8)) + [(-5, 9)] + bez((-5, 9), (-5, 15), (-3, 20), (1, 24))
        shape(tail, RIBBON, LINE*0.8)
        tail2 = bez((1, 25), (6, 20), (9, 16), (10, 10)) + [(7, 11.5)] + bez((7, 11.5), (6, 16), (3, 20), (0, 24))
        shape(tail2, RIBBON, LINE*0.8)
        band = [(-11, 23.5), (11, 23.5), (10, 27.5), (-10, 27.5)]
        shape(band, RIBBON, LINE*0.8)
        for sd in (-1, 1):
            loop = bez((0, 26), (sd*4, 33), (sd*10, 32), (sd*8.5, 27)) + bez((sd*8.5, 27), (sd*7, 24), (sd*3, 24.5), (0, 26))
            shape(loop, RIBBON, LINE*0.8)
            stroke(ell(sd*5, 28.2, 2, 1.2, 10, 30, 150), LINE*0.4, g=Col(0.3, "#8e2626"))
        shape(ell(0, 26, 2.3, 2.3, 14), RIBBON, LINE*0.8)


def k_postcard(b):
    with T(b.w/2, b.h/2, 1, rot=7):
        card = rrect(-37, -26, 74, 52, 2)
        form(card, PAPER, sdx=3, sdy=-2, sh=0.1)
        pic = rrect(-32, -21, 64, 42, 1)
        fill(pic, SKY)
        C.saveState(); C.clipPath(poly(pic), stroke=0, fill=0)
        shape(curl_outline(-16, 12, 7, 3.2, 0, 360, 5, 0.2), WHITE, LINE*0.5)
        shape(bez((-40, -4), (-20, 6), (0, 2), (40, -6)) + [(40, -30), (-40, -30)], HILL_FAR, LINE*0.6)
        shape(bez((-40, -14), (-18, -6), (4, 4), (12, 5)) + bez((12, 5), (22, 5), (30, -4), (40, -10)) + [(40, -30), (-40, -30)], HILL, LINE*0.7)
        tw = rrect(6.5, 2, 9, 17, 0.5)
        form(tw, TOWER, sdx=2.5, sdy=0, sh=0.14)
        for x in (6, 8.6, 11.2, 13.8):
            shape(rrect(x, 18.5, 2.4, 3, 0.3), TOWER, LINE*0.6)
        shape(rrect(9.8, 2, 2.4, 4, 1.1), Col(0.3, "#5a4a3e"), LINE*0.5)
        shape(rrect(10.2, 12, 1.6, 2.6, 0.7), Col(0.3, "#5a4a3e"), LINE*0.4)
        for y in (6.5, 9.5, 15.5):
            stroke([(6.8, y), (15.2, y)], LINE*0.35, g=TOWER_DARK)
        for x, y in ((-24, -12), (-20, -15), (24, -10), (28, -13), (-4, -17), (0, -16)):
            shape(curl_outline(x, y, 3.2, 2.8, 0, 360, 5, 0.2), FERN_GOLD if x % 3 else LEAF_ORANGE, LINE*0.5)
        C.restoreState()
        stroke(pic, LINE*0.8, closed=True)
        st = rrect(20, 10, 10, 12, 0.4)
        shape(st, WHITE, LINE*0.6)
        fill(rrect(21.5, 11.5, 7, 9, 0.3), STAMP)
        birch_leaf(25, 12.6, 2.2, 0, LEAF_YEL)


def k_stone(b):
    with T(b.w/2, b.h/2 - 6, 1):
        st = [(-30, -18), (-10, -22), (18, -21), (31, -14), (33, 4), (26, 16), (4, 19), (-20, 17), (-32, 6)]
        fill(st, ROCK)
        clip_fill(st, [(-34, -24), (36, -24), (36, -8), (10, -12), (-34, -8)], ROCK_DARK)
        fill([(-32, 6), (-20, 17), (4, 19), (26, 16), (33, 4), (14, 6), (-10, 7)], ROCK_LIGHT)
        stroke([(-32, 6), (-10, 7), (14, 6), (33, 4)], LINE*0.6)
        offset_shadow(st, -4, 3, 0.1)
        stroke(st, LINE, closed=True)
        stroke([(-6, -4), (0, -10), (-2, -16)], LINE*0.6)
        stroke([(18, -2), (22, -8)], LINE*0.5)
        for x, y, rad, g in ((-18, -8, 3.2, LICHEN), (22, 8, 2.4, LICHEN_ORANGE), (8, -14, 2.2, LICHEN)):
            shape(curl_outline(x, y, rad, rad*0.8, 0, 360, 6, 0.3), g, LINE*0.45)
        m = wavy([(-28, 12), (-14, 14), (-2, 16)], 2, 0) + wavy([(-2, 16), (-8, 25), (-22, 24), (-30, 14)], 6, -2.2)
        form(m, MOSS, sdx=0, sdy=2, sh=0.12)
        for x, y in ((-18, 19), (-10, 21), (-22, 17)):
            dot(x, y, 0.7, MOSS_LIGHT)
        for x, lean in ((-15, -3), (-12, 2), (-8, 5)):
            stem = bez((x, 23), (x, 27), (x + lean*0.5, 30), (x + lean, 33))
            stroke(stem, LINE*0.7, g=MOSS_DARK)
            shape(ell(x + lean, 33.5, 0.9, 1.3, 10), LEAF_ORANGE, LINE*0.45)


def k_coin(b):
    with T(b.w/2, b.h/2, 1):
        form(ell(0, 0, 32, 32, 60), SILVER_DARK, sdx=3, sdy=-2, sh=0.12)
        shape(ell(0, 0, 28, 28, 60), SILVER)
        fill(ell(-4, 5, 20, 18, 40, 100, 200), SILVER_LIGHT)
        for i in range(36):
            a = math.radians(i*10)
            dot(math.cos(a)*25.2, math.sin(a)*25.2, 0.9, SILVER_DARK)
        hd = [(-8, -14)] + bez((-8, -14), (-12, -6), (-13, 6), (-6, 12)) + bez((-6, 12), (0, 16), (7, 14), (9, 8)) + \
             [(10, 4), (13.5, 0), (10.5, -1)] + bez((10.5, -1), (11.5, -3), (10, -4), (10.5, -5.5)) + bez((10.5, -5.5), (9, -7), (7, -8), (6, -10)) + \
             [(5, -16), (-8, -14)]
        form(hd, SILVER_LIGHT, sdx=1.2, sdy=-1, sh=0.18)
        stroke(bez((-11, 2), (-6, 9), (0, 12.5), (6, 11.5)), LINE*0.7)
        for i in range(5):
            t = 0.15 + i*0.18
            x = -11 + t*17; y = 2 + math.sin(t*math.pi*0.9)*11
            with T(x, y, 1, rot=40 + i*18):
                shape(ell(1.4, 0, 1.8, 0.8, 10), SILVER, LINE*0.5)
        dot(5.2, 4.5, 0.9, 0.0)
        stroke(bez((4, 6.3), (5, 7), (6.2, 6.8), (7, 6.2)), LINE*0.5)
        stroke(bez((6.5, -3.5), (7.5, -4.2), (8.8, -4), (9.5, -3.4)), LINE*0.5)
        stroke(ell(-6, 0, 3, 3, 12, 20, 200), LINE*0.5)
        for sx, sy in ((-17, -18), (18, -16)):
            shape(ell(sx, sy, 1.5, 1.5, 10), SILVER_LIGHT, LINE*0.5)
        stroke(ell(0, 0, 28, 28, 30, 100, 170), LINE*1.6, g=WHITE, alpha=0.7)


def sparkle(x, y, r):
    s = [(x, y + r), (x + r*0.25, y + r*0.25), (x + r, y), (x + r*0.25, y - r*0.25), (x, y - r), (x - r*0.25, y - r*0.25), (x - r, y), (x - r*0.25, y + r*0.25)]
    shape(s, WHITE, LINE*0.6)


def k_horseshoe(b):
    with T(b.w/2, b.h/2 - 2, 1, rot=-12):
        outline = ell(0, 4, 24, 26, 50, -60, 240) + ell(0, 4, 12, 14, 40, 240, -60)
        form(outline, IRON, sdx=-3, sdy=1.5, sh=0.14)
        stroke(ell(0, 4, 18, 20, 40, -40, 220), LINE*0.6, g=SILVER_DARK)
        stroke(ell(0, 4, 21, 23, 30, 100, 170), LINE*2, g=WHITE, alpha=0.75)
        for a in (-35, 5, 45, 135, 175, 215):
            px, py = math.cos(math.radians(a))*18, 4 + math.sin(math.radians(a))*20
            shape(rrect(px - 1.3, py - 1.3, 2.6, 2.6, 0.4), Col(0.25, "#4a5058"), LINE*0.4)
        for a in (5, 175):
            px, py = math.cos(math.radians(a))*18, 4 + math.sin(math.radians(a))*20
            shape(ell(px, py, 2.4, 2.4, 12), SILVER_LIGHT, LINE*0.6)
    sparkle(b.w/2 + 26, b.h/2 + 28, 5); sparkle(b.w/2 - 30, b.h/2 - 22, 3.5)


def k_bead(b):
    with T(b.w/2, b.h/2, 1):
        outer = ell(0, 0, 28, 25, 60)
        form(outer, GLASS_BLUE, sdx=-5, sdy=4, sh=0.15)
        hole = ell(0, 3, 9, 6.5, 30)
        C.saveState(); C.clipPath(poly(outer), stroke=0, fill=0)
        for a0 in (0, 120, 240):
            sw = []
            for i in range(40):
                t = i/39
                a = math.radians(a0 + t*150)
                rr = 22 - t*9
                sw.append((math.cos(a)*rr, math.sin(a)*rr*0.85 + 1))
            stroke(sw, LINE*3.4, g=0.0)
            stroke(sw, LINE*2.1, g=GLASS_YEL)
            ex, ey = sw[0]
            shape(ell(ex, ey, 2.6, 2.6, 14), GLASS_YEL, LINE*0.7)
        C.restoreState()
        shape(hole, GLASS_DEEP)
        fill(ell(0, 1.8, 6.5, 3.8, 24), Col(0.15, "#12305a"))
        stroke(ell(0, 0, 23, 20, 30, 110, 160), LINE*2.2, g=WHITE, alpha=0.8)
        dot(-10, 15, 1.4, WHITE)


# ------------------------------------------------------------------ UI icons
def u_camera(b):
    with T(b.w/2, b.h/2 - 3, 1):
        shape(rrect(-20, 16, 12, 7, 1.5), SILVER_DARK, LINE*0.9)
        shape(rrect(10, 16, 9, 5, 1.5), SILVER, LINE*0.9)
        shape(ell(14.5, 23, 3, 2, 14), BUTTON_RED, LINE*0.8)
        body = rrect(-30, -20, 60, 38, 6)
        form(body, CAM_BODY, sdx=-4, sdy=2, sh=0.14)
        clip_fill(body, [(-32, 5), (32, 5), (32, 20), (-32, 20)], CAM_TOP)
        stroke([(-30, 5.5), (30, 5.5)], LINE*0.8)
        C.saveState(); C.clipPath(poly(body), stroke=0, fill=0)
        for x in range(-28, 30, 4):
            for y in range(-18, 4, 4):
                dot(x + (2 if (y//4) % 2 else 0), y, 0.45, Col(0.2, "#43291a"))
        C.restoreState()
        stroke(body, LINE, closed=True)
        shape(rrect(-25, 9, 11, 6, 1), LENS_GLASS, LINE*0.8)
        dot(-22, 13, 0.9, WHITE)
        form(ell(3, -2, 16, 16, 40), SILVER, sdx=-2, sdy=1, sh=0.15)
        shape(ell(3, -2, 11.5, 11.5, 36), SILVER_DARK, LINE*0.8)
        shape(ell(3, -2, 8.5, 8.5, 30), LENS_GLASS, LINE*0.8)
        stroke(ell(3, -2, 5.5, 5.5, 20, 110, 170), LINE*1.6, g=WHITE, alpha=0.85)
        dot(6.5, -5.5, 1.1, WHITE)


def u_basket(b):
    with T(b.w/2, b.h/2 - 10, 1):
        handle = ell(0, 8, 26, 30, 40, 0, 180)
        stroke(handle, LINE*7.2, g=0.0, taper=False)
        stroke(handle, LINE*5, g=WICKER, taper=False)
        for i in range(8):
            a = math.radians(10 + i*22)
            x, y = math.cos(a)*26, 8 + math.sin(a)*30
            stroke([(x - 1.5, y - 1.5), (x + 1.5, y + 1.5)], LINE*0.5, g=WICKER_DARK)
        bowl = [(-33, 10)] + bez((-33, 10), (-30, -8), (-22, -20), (-14, -22)) + [(14, -22)] + bez((14, -22), (22, -20), (30, -8), (33, 10))
        fill(bowl, WICKER)
        C.saveState(); C.clipPath(poly(bowl), stroke=0, fill=0)
        for j, y in enumerate(range(-22, 12, 5)):
            for i, x in enumerate(range(-36, 40, 8)):
                off = 4 if j % 2 else 0
                shape(ell(x + off, y + 2.5, 4.4, 2.3, 12), WICKER if (i + j) % 2 else Col(0.75, "#dfae66"), LINE*0.5)
        C.restoreState()
        offset_shadow(bowl, -6, 2, 0.14)
        stroke(bowl, LINE, closed=True)
        tube([(-34, 10), (34, 10)], 6, 6, WICKER_DARK, sh=0)
        for x in range(-30, 34, 6):
            stroke([(x - 1.5, 8), (x + 1.5, 12)], LINE*0.5, g=Col(0.35, "#7a5226"))


def book(g, gd, x0=-26, y0=-32, w=52, h=62):
    pages = rrect(x0 + 4, y0 - 3, w - 2, h - 2, 2)
    shape(pages, PAPER, LINE)
    for k in (1.5, 3):
        stroke([(x0 + 6, y0 - 3 + k*0.3), (x0 + w + 1, y0 - 3 + k*0.3 + 0.5)], LINE*0.4, g=PAPER_EDGE)
    cover = rrect(x0, y0, w, h, 3)
    form(cover, g, sdx=-3, sdy=2, sh=0.12)
    clip_fill(cover, [(x0 - 2, y0 - 2), (x0 + 8, y0 - 2), (x0 + 8, y0 + h + 2), (x0 - 2, y0 + h + 2)], gd)
    stroke([(x0 + 8, y0), (x0 + 8, y0 + h)], LINE*0.8)
    stroke(cover, LINE, closed=True)
    for yy in (y0 + 8, y0 + h - 8):
        stroke([(x0 + 1, yy), (x0 + 7, yy)], LINE*1.4, g=GOLD)


def u_herbarium(b):
    with T(b.w/2, b.h/2 + 1, 1):
        book(BOOK_GREEN, BOOK_GREEN_DARK)
        shape(rrect(-10, -22, 26, 42, 1), PAPER, LINE*0.8)
        with T(3, -1, 1, rot=-15):
            lf = []
            for i in range(5):
                a = 90 + (i - 2)*45
                x, y = math.cos(math.radians(a))*13, math.sin(math.radians(a))*13 + 2
                lf += bez((0, 0), (x*0.5 - y*0.25, y*0.5 + x*0.25), (x*0.9 - y*0.15, y*0.9 + x*0.15), (x, y), 6)
                lf += bez((x, y), (x*0.9 + y*0.15, y*0.9 - x*0.15), (x*0.5 + y*0.25, y*0.5 - x*0.25), (0, 0), 6)
            shape(lf, LEAF_ORANGE, LINE*0.8)
            for i in range(5):
                a = 90 + (i - 2)*45
                stroke([(0, 0), (math.cos(math.radians(a))*10, math.sin(math.radians(a))*10 + 2)], LINE*0.5, g=LEAF_RED)
            stroke([(0, 0), (0.5, -9)], LINE*1.1, g=Col(0.4, "#8a5a34"))
        for x, y, rot in ((-10, 20, 30), (16, -22, 30)):
            with T(x, y, 1, rot=rot):
                shape(rrect(-4.5, -1.6, 9, 3.2, 0.4), Col(0.9, "#f2e6c2", alpha=0.9), LINE*0.5)


def u_sun(b):
    with T(b.w/2, b.h/2, 1):
        for i in range(12):
            a = math.radians(i*30 + 15)
            L = 40 if i % 2 else 34
            tip = (math.cos(a)*L, math.sin(a)*L)
            l = (math.cos(a - 0.2)*24, math.sin(a - 0.2)*24); rr = (math.cos(a + 0.2)*24, math.sin(a + 0.2)*24)
            shape(bez(l, (l[0]*1.2, l[1]*1.2), (tip[0]*0.95 - math.sin(a)*1.2, tip[1]*0.95 + math.cos(a)*1.2), tip) + bez(tip, (tip[0]*0.95 + math.sin(a)*1.2, tip[1]*0.95 - math.cos(a)*1.2), (rr[0]*1.2, rr[1]*1.2), rr), SUN_RAY, LINE*0.9)
        form(ell(0, 0, 25, 25, 50), SUN, sdx=-4, sdy=3, sh=0.1)
        fill(ell(-8, 9, 7, 4.5, 20, rot=35), SUN_LIGHT)
        stroke(ell(0, 0, 20, 20, 20, 110, 160), LINE*1.4, g=WHITE, alpha=0.7)


def u_cone(b):
    with T(b.w/2, b.h/2 - 4, 1):
        cone(70, 19)


def u_cone_empty(b):
    with T(b.w/2, b.h/2 - 4, 1):
        cone(70, 19, pale=True)


def u_lock(b):
    with T(b.w/2, b.h/2 - 6, 1):
        tube([(-14.5, 0), (-14.5, 10)] + ell(0, 10, 14.5, 19, 40, 180, 0) + [(14.5, 10), (14.5, 0)], 7, 7, SILVER, sh=0)
        stroke(ell(0, 10, 14.5, 19, 20, 110, 160), LINE*1.4, g=WHITE, alpha=0.8)
        body = rrect(-25, -25, 50, 38, 6)
        form(body, GOLD, sdx=-5, sdy=2, sh=0.13)
        stroke([(-22, 8), (22, 8)], LINE*0.6, g=GOLD_DARK)
        stroke([(-22, -20), (22, -20)], LINE*0.6, g=GOLD_DARK)
        kh = ell(0, -2, 4.2, 4.2, 20, -60, 240) + [(2.6, -13), (-2.6, -13)]
        shape(kh, Col(0.15, "#3a2a16"), LINE*0.8)
        stroke(rrect(-22, -22, 13, 32, 3), LINE*1.3, g=WHITE, alpha=0.4)


def u_paw(b):
    with T(b.w/2, b.h/2 - 4, 1):
        pad = bez((0, 6), (10, 6), (18, -4), (15, -12)) + bez((15, -12), (12, -20), (4, -16), (0, -17)) + \
              bez((0, -17), (-4, -16), (-12, -20), (-15, -12)) + bez((-15, -12), (-18, -4), (-10, 6), (0, 6))
        shape(pad, PAW)
        fill(ell(-5, -1, 4, 2.5, 14, rot=20), PAW_LIGHT)
        for x, y, rot in ((-22, 9, 25), (-8, 20, 8), (8, 20, -8), (22, 9, -25)):
            t = ell(x, y, 6.2, 8.2, 24, rot=rot)
            shape(t, PAW)
            fill(ell(x - 1.5, y + 2.5, 2, 2.6, 12, rot=rot), PAW_LIGHT)


def oak_leaf(g, s=1.0):
    with T(0, 0, s):
        R = []
        lobes = [(0, 22), (6, 18), (5, 14), (10, 10), (7, 5), (12, 0), (8, -5), (11, -10), (5, -13), (3, -18)]
        for i in range(len(lobes) - 1):
            a, bb = lobes[i], lobes[i + 1]
            if i % 2 == 0:
                R += bez(a, (a[0] + 3, a[1]), (bb[0] + 3, bb[1] + 2), bb, 6)
            else:
                R += bez(a, (a[0] - 2, a[1]), (bb[0] - 2, bb[1]), bb, 6)
        leaf = R + mirror(list(reversed(R)))
        shape(leaf, g, LINE*0.9)
        stroke([(0, -24), (0, 20)], LINE*0.7, g=Col(0.35, "#6a4a1e"))
        for y, x in ((12, 5), (4, 8), (-5, 8)):
            stroke([(0, y - 3), (x, y)], LINE*0.5, g=Col(0.35, "#6a4a1e"))
            stroke([(0, y - 3), (-x, y)], LINE*0.5, g=Col(0.35, "#6a4a1e"))


def u_atlas(b):
    with T(b.w/2, b.h/2 + 1, 1):
        rib = [(14, -32), (19, -32), (19, -42), (16.5, -39), (14, -42)]
        shape(rib, RIBBON, LINE*0.8)
        book(BOOK_BROWN, BOOK_BROWN_DARK)
        stroke(rrect(-14, -24, 36, 46, 2), LINE*0.8, closed=True, g=GOLD)
        with T(4, -1, 0.9, rot=-18):
            oak_leaf(Col(0.6, "#8fae3e"))


def u_house(b):
    with T(b.w/2, b.h/2 - 6, 1):
        tube([(-40, -26), (40, -26)], 3, 3, GRASS, sh=0)
        shape(rrect(12, 14, 8, 16, 0.8), Col(0.5, "#b0553f"), LINE)
        shape(rrect(10.8, 28, 10.4, 3, 0.5), Col(0.4, "#8a3e2e"), LINE*0.8)
        for dx, dy, r in ((17, 36, 2.6), (20, 41, 3.2), (17, 46.5, 3.6)):
            shape(curl_outline(dx, dy, r, r*0.85, 0, 360, 5, 0.18), SMOKE, LINE*0.55)
        wall = [(-26, -25), (26, -25), (26, 6), (-26, 6)]
        form(wall, WALL, sdx=-5, sdy=0, sh=0.1)
        roof = [(-35, 2), (-3, 30), (3, 30), (35, 2), (30, -1), (0, 24), (-30, -1)]
        form(roof, ROOF, sdx=0, sdy=-3, sh=0.14)
        C.saveState(); C.clipPath(poly(roof), stroke=0, fill=0)
        for k in range(1, 5):
            stroke([(-40, -1 + k*6), (40, -1 + k*6)], LINE*0.5, g=ROOF_DARK)
        C.restoreState()
        shape(ell(0, 13, 3.4, 3.4, 16), WINDOW, LINE*0.8)
        shape(rrect(-20, -25, 12, 21, 5.5), DOOR, LINE)
        dot(-10.5, -15, 0.9, BRASS)
        win = rrect(4, -16, 15, 13, 1)
        shape(win, WINDOW, LINE*0.9)
        stroke([(11.5, -16), (11.5, -3)], LINE*0.7); stroke([(4, -9.5), (19, -9.5)], LINE*0.7)
        shape(rrect(2.5, -18.5, 18, 2.6, 0.6), Col(0.8, "#e36f6f"), LINE*0.7)
        for x in (5, 9, 14, 18):
            dot(x, -15.4 + 0.2*(x % 3), 1.1, RIBBON if x % 2 else LEAF_YEL)


def u_question(b):
    with T(b.w/2, b.h/2, 1):
        tube([(0, -42), (0, -20)], 8, 8, SIGN_DARK, sh=0.14)
        disc = ell(0, 6, 32, 32, 60)
        form(disc, SIGN, sdx=-4, sdy=2, sh=0.14)
        for k in (0.78, 0.5):
            stroke(ell(-3, 3, 32*k, 30*k, 36, 20, 150), LINE*0.5, g=SIGN_DARK)
        stroke(ell(0, 6, 28, 28, 40, 200, 330), LINE*0.5, g=SIGN_DARK)
        for x, y in ((-22, 14), (22, -6)):
            shape(ell(x, y, 1.4, 1.4, 10), GOLD_DARK, LINE*0.5)
        q = bez((-9, 15), (-9, 24), (9, 26), (9, 16), 16) + bez((9, 16), (9, 9), (0, 9), (0, 1), 12)
        tube(q, 7, 7, SIGN_MARK, sh=0)
        shape(ell(0, -8, 4, 4, 20), SIGN_MARK)


ASSETS = [
    ("fabian_stand", 170, 280, fabian("stand"), "chars"),
    ("fabian_wave", 170, 280, fabian("wave"), "chars"),
    ("fabian_talk", 170, 280, fabian("talk"), "chars"),
] + [(n, 200, 110, f, "covers") for n, f in (
    ("bush", bush), ("rock", rock), ("grass", grass), ("reeds", reeds), ("log", log), ("fern", fern), ("heather", heather))
] + [(n, 90, 90, f, "keepsakes") for n, f in (
    ("cone", k_cone), ("postcard", k_postcard), ("stone", k_stone), ("coin", k_coin), ("horseshoe", k_horseshoe), ("bead", k_bead))
] + [(n, 90, 90, f, "ui") for n, f in (
    ("camera", u_camera), ("basket", u_basket), ("herbarium", u_herbarium), ("sun", u_sun), ("cone_icon", u_cone), ("cone_empty", u_cone_empty),
    ("lock", u_lock), ("paw", u_paw), ("atlas", u_atlas), ("house", u_house), ("question", u_question))
]
