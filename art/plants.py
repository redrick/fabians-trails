"""Herbarium specimens of the autumn Brdy: fronds, twigs, sprigs and flowering stems."""
import math, random
from lib import Col, ell, bez, resample
from style3 import *

FERN = Col(0.6, "#5fa83f"); FERN_D = Col(0.45, "#3f8231")
FERN_Y = Col(0.75, "#cdc23e"); FERN_YD = Col(0.6, "#a39a2a")
FERN_O = Col(0.7, "#dba544"); FERN_OD = Col(0.55, "#b57f2c")
STIPE = Col(0.45, "#8f7a3e"); SCALE = Col(0.4, "#8a5a2e")
MOSS = Col(0.6, "#7ab83e"); MOSS_D = Col(0.45, "#4f8a2e"); MOSS_BASE = Col(0.4, "#5f7a30")
SETA = Col(0.4, "#b0503a"); CAPSULE = Col(0.55, "#c08040"); CAPSULE_D = Col(0.45, "#96602c")
CALYPTRA = Col(0.8, "#e6c77e"); CALYPTRA_D = Col(0.65, "#c4a258")
BEECH_TWIG = Col(0.45, "#8c6a4f"); BUD = Col(0.55, "#c08a52"); BUD_D = Col(0.45, "#9a6636")
COPPER = Col(0.5, "#d4702e"); COPPER_D = Col(0.4, "#a8501f")
GOLD = Col(0.7, "#eeae3a"); GOLD_D = Col(0.55, "#c9862a")
GOLDGREEN = Col(0.7, "#c8b842"); GOLDGREEN_D = Col(0.55, "#9e922e")
SPRUCE = Col(0.5, "#3f8a4e"); SPRUCE_D = Col(0.4, "#2c6a3c"); SPRUCE_TWIG = Col(0.55, "#c07a44")
CONE = Col(0.5, "#a8703e"); CONE_D = Col(0.4, "#7a4a26")
FIR = Col(0.45, "#2f7a55"); FIR_D = Col(0.35, "#235f42"); FIR_UNDER = Col(0.6, "#6aa582")
STRIPE = Col(0.95, "#f2faf4"); FIR_TWIG = Col(0.55, "#a08a62")
FIR_CONE = Col(0.55, "#8e9a52"); FIR_CONE_D = Col(0.45, "#6e7a3a"); BRACT = Col(0.65, "#c2b070")
OAK_G = Col(0.6, "#8aa53a"); OAK_GD = Col(0.5, "#67832a")
OAK_Y = Col(0.7, "#d6b43c"); OAK_YD = Col(0.55, "#aa8c2a")
OAK_B = Col(0.55, "#bf7f3c"); OAK_BD = Col(0.45, "#935c28")
ACORN = Col(0.6, "#c98f42"); ACORN_D = Col(0.5, "#9c6a2c"); CUP = Col(0.5, "#9a7a4a"); CUP_D = Col(0.4, "#735a32")
OAK_TWIG = Col(0.45, "#7e5e40")
BIRCH_Y = Col(0.8, "#f6d23a"); BIRCH_YD = Col(0.65, "#d2a82a")
BIRCH_G = Col(0.7, "#bfc83e"); BIRCH_GD = Col(0.55, "#96a02c")
BIRCH_BARK = Col(0.95, "#f7f4ec"); BARK_MARK = Col(0.2, "#3a3530"); BIRCH_TWIG = Col(0.35, "#7e3f2c")
CATKIN = Col(0.5, "#9a6a42"); CATKIN_D = Col(0.4, "#744a2c")
MAPLE = Col(0.6, "#f38a2c"); MAPLE_R = Col(0.45, "#dc472e"); MAPLE_VEIN = Col(0.4, "#b53e26")
SAMARA = Col(0.75, "#e0bb70"); SAMARA_D = Col(0.6, "#bb9450"); NUTLET = Col(0.55, "#b08040")
LARCH = Col(0.8, "#f4c63a"); LARCH_D = Col(0.65, "#dc9a22"); LARCH_G = Col(0.7, "#cdc63e")
LARCH_TWIG = Col(0.45, "#8a6a50"); LARCH_CONE = Col(0.6, "#c08c5c"); LARCH_CONE_D = Col(0.45, "#916238")
PINE = Col(0.5, "#4f9488"); PINE_D = Col(0.4, "#36736a"); PINE_TWIG = Col(0.55, "#b67c4c")
PINE_BUD = Col(0.5, "#c0643c"); PINE_BUD_D = Col(0.4, "#944628")
PINE_CONE = Col(0.5, "#a4825e"); PINE_CONE_D = Col(0.4, "#735a3c")
HEATHER = Col(0.7, "#de80be"); HEATHER_D = Col(0.55, "#b65a9c")
HEATHER_LEAF = Col(0.45, "#58824a"); HEATHER_LEAF_D = Col(0.35, "#3e6236"); WOOD = Col(0.4, "#7a5040")
THYME_LEAF = Col(0.55, "#74a05c"); THYME_LEAF_D = Col(0.45, "#577f44")
THYME = Col(0.75, "#ea94c8"); THYME_D = Col(0.6, "#c86aa6"); THYME_CALYX = Col(0.4, "#8e4a7a"); THYME_STEM = Col(0.4, "#8a4a58")
NETTLE = Col(0.5, "#4f8f3e"); NETTLE_D = Col(0.4, "#3a6e2e"); NETTLE_STEM = Col(0.55, "#6a9440")
NETTLE_FL = Col(0.7, "#b0c86e"); NETTLE_FL_D = Col(0.55, "#88a24a")
TANSY_LEAF = Col(0.5, "#4f8a3e"); TANSY_LEAF_D = Col(0.4, "#386a2e"); TANSY_STEM = Col(0.5, "#6a8a3a")
TANSY = Col(0.8, "#f8c62a"); TANSY_D = Col(0.65, "#dca018"); TANSY_DOT = Col(0.5, "#b87c10")
CHICORY = Col(0.75, "#8cbcf0"); CHICORY_D = Col(0.6, "#6496dc"); CHICORY_EYE = Col(0.35, "#34549e")
CHICORY_STEM = Col(0.5, "#6a9448"); CHICORY_LEAF = Col(0.5, "#5f944a"); CHICORY_LEAF_D = Col(0.4, "#467a36")
CENT = Col(0.75, "#f47eac"); CENT_D = Col(0.6, "#d8588e"); CENT_EYE = Col(0.95, "#fff3c8"); ANTHER = Col(0.85, "#f6d23a")
CENT_LEAF = Col(0.55, "#6fa04c"); CENT_LEAF_D = Col(0.45, "#527e38"); CENT_STEM = Col(0.55, "#74a04c")

OW = 0.6


def at(pts, t):
    d = [0.0]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        d.append(d[-1] + math.hypot(x1-x0, y1-y0))
    s = max(0.0, min(1.0, t))*d[-1]
    for i in range(len(pts)-1):
        if d[i+1] >= s:
            f = (s-d[i])/((d[i+1]-d[i]) or 1)
            (x0, y0), (x1, y1) = pts[i], pts[i+1]
            return x0+(x1-x0)*f, y0+(y1-y0)*f, math.degrees(math.atan2(y1-y0, x1-x0))
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    return x1, y1, math.degrees(math.atan2(y1-y0, x1-x0))


def ray(x, y, ang, r):
    return x + math.cos(math.radians(ang))*r, y + math.sin(math.radians(ang))*r


def pw(t, a, b):
    if t <= 0 or t >= 1: return 0.0
    m = (a/(a+b))**a*(b/(a+b))**b
    return t**a*(1-t)**b/m


def ribbon(pts, w, tip=True, base=False, ext=0.0, tl=0.4, tp=0.75):
    P = resample(list(pts), 0.35)
    if len(P) < 2: P = list(pts)
    if ext:
        (ax, ay), (bx, by) = P[0], P[1]; L = math.hypot(bx-ax, by-ay) or 1
        P.insert(0, (ax-(bx-ax)/L*ext, ay-(by-ay)/L*ext))
        (ax, ay), (bx, by) = P[-2], P[-1]; L = math.hypot(bx-ax, by-ay) or 1
        P.append((bx+(bx-ax)/L*ext, by+(by-ay)/L*ext))
    n = len(P); left, right = [], []
    for i in range(n):
        a = P[max(0, i-1)]; b = P[min(n-1, i+1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1
        t = i/(n-1); k = 1.0
        if tip: k = min(k, ((1-t)/tl)**tp)
        if base: k = min(k, (t/0.4)**0.75)
        h = w/2*k
        left.append((P[i][0]-dy/L*h, P[i][1]+dx/L*h)); right.append((P[i][0]+dy/L*h, P[i][1]-dx/L*h))
    return left + right[::-1]


def rod(pts, w, g, tip=True, base=False):
    fill(ribbon(pts, w+2*OW, tip, base, ext=OW), 0.0)
    fill(ribbon(pts, w, tip, base), g)


def stem(pts, w0, w1, g):
    tube(pts, w0, w1, g)
    (x0, y0), (x1, y1) = pts[0], pts[1]
    L = math.hypot(x1-x0, y1-y0) or 1
    nx, ny = -(y1-y0)/L*w0/2, (x1-x0)/L*w0/2
    stroke([(x0+nx, y0+ny), (x0-nx, y0-ny)], LINE, taper=False)


def blade(L, W, a=0.8, b=1.0, mod=None, cord=0.0, n=160):
    R, Lf = [], []
    for i in range(n+1):
        t = i/n
        w = W/2*pw(t, a, b)*(mod(t) if mod else 1.0)
        y = t*L - (cord*L*math.sin(math.pi*min(t/0.3, 1.0)) if cord else 0)
        R.append((w, y)); Lf.append((-w, y))
    return R, Lf


def leaf(x, y, ang, L, W, g, gd, a=0.8, b=1.0, mod=None, cord=0.0, veins=0, vg=None, stalk=0.0, vang=0.55, lw=LINE):
    with T(x, y, 1, rot=ang-90):
        if stalk: stroke([(0, -0.6), (0, stalk+1.5)], LINE*1.15, taper=False)
        R, Lf = blade(L, W, a, b, mod, cord)
        out = [(px, py+stalk) for px, py in R + Lf[::-1]]
        shape(out, g, lw, shadow=([(px, py+stalk) for px, py in R], gd))
        if vg is not None:
            stroke([(0, stalk+0.5), (0, stalk+L*0.9)], LINE*0.55, g=vg)
            for i in range(veins):
                t = 0.12 + 0.72*(i+0.5)/veins
                t2 = min(0.97, t + vang*0.3)
                for s in (-1, 1):
                    w2 = W/2*pw(t2, a, b)*0.78
                    stroke([(0, stalk+t*L), (s*w2*0.5, stalk+(t+t2)/2*L+0.3), (s*w2, stalk+t2*L)], LINE*0.4, g=vg)


def scallop(k, d=0.45, p=0.5):
    return lambda t: (1-d) + d*abs(math.sin(math.pi*t*k))**p


def serrate(k, d=0.14):
    return lambda t: 1 - d*(1 - (t*k) % 1.0)


def pinnate(pts, n, plen, colours, ang=72, t0=0.1, t1=0.97, wr=0.32, k=4.0, d=0.45, ab=(0.4, 1.0), vein=True):
    for i in reversed(range(n)):
        u = i/(n-1)
        t = t0 + (t1-t0)*u
        Lp = plen(u)
        g, gd = colours(i)
        for s in (-1, 1):
            x, y, a = at(pts, t + (0.008 if s > 0 else 0))
            leaf(x, y, a+s*ang, Lp, max(2.2, Lp*wr), g, gd, ab[0], ab[1], scallop(max(1.5, Lp/k), d), vg=gd if vein and Lp > 8 else None)


def needle(x, y, ang, L, w, g, bend=0.0):
    ex, ey = ray(x, y, ang, L)
    mx, my = ray((x+ex)/2, (y+ey)/2, ang+90, bend)
    rod(bez((x, y), (mx, my), (mx, my), (ex, ey), 8), w, g)


# ------------------------------------------------------------------ ferns & moss
def kapradi(b):
    cx = b.w/2
    rach = bez((cx-2, 8), (cx-6, 45), (cx+2, 82), (cx+12, 112), 40)
    cols = lambda i: (FERN_O, FERN_OD) if i < 1 else (FERN_Y, FERN_YD) if i < 3 else (FERN, FERN_D)
    pinnate(rach, 13, lambda u: 6 + 36*pw(0.06+0.9*u, 0.55, 1.0), cols, ang=62, t0=0.16, t1=0.95, wr=0.22, k=3.0, d=0.62)
    tube(rach[:34], 3.4, 1.2, STIPE)
    stroke([(cx-2-1.7, 8), (cx-2+1.7, 8)], LINE, taper=False)
    for t in (0.03, 0.07, 0.11, 0.14):
        x, y, a = at(rach, t)
        for s in (-1, 1):
            shape(ell(*ray(x, y, a+s*80, 1.9), 1.3, 0.8, 10, rot=a+s*30), SCALE, LINE*0.6)
    x, y, a = at(rach, 1.0)
    leaf(x, y, a, 5, 2.4, FERN, FERN_D, 0.5, 1.0)


def moss_shoot(x, h, lean, rng):
    top = (x + lean, 14 + h)
    pts = bez((x, 12), (x, 12+h*0.4), (x+lean*0.6, 12+h*0.8), top, 14)
    rod(pts, 1.8, MOSS_D, tip=False)
    n = int(h/4.2)
    for i in range(n):
        t = 0.15 + 0.8*i/n
        px, py, a = at(pts, t)
        s = 1 if i % 2 else -1
        needle(px, py, a + s*rng.uniform(35, 55), rng.uniform(5.5, 7.5), 1.5, MOSS if i % 3 else MOSS_D, s*0.6)
    for k, da in enumerate((-80, -50, -22, 0, 22, 50, 80)):
        needle(top[0], top[1], 90 + da + lean, 6.5 + (2.5 if abs(da) < 60 else 0) - abs(da)*0.02, 1.6, MOSS if k % 2 else MOSS_D, 0)


def sporophyte(x, h, lean, cap=True):
    top = (x+lean, h)
    pts = bez((x, 16), (x, h*0.5), (x+lean*0.4, h*0.85), top, 20)
    rod(pts, 1.1, SETA, tip=False)
    with T(top[0], top[1], 1, rot=lean*1.6 - 70):
        caps = rrect(-1.2, -3, 11, 6, 2)
        shape(caps, CAPSULE, shadow=(rrect(-1.2, -3, 11, 3, 1.5), CAPSULE_D))
        if cap:
            hat = bez((-1.5, -3.6), (3, -4.6), (9, -3), (13.5, 0.4)) + bez((13.5, 0.4), (9, 4.8), (3, 4.8), (-1.5, 3.8))
            shape(hat, CALYPTRA, shadow=(bez((-1.5, -3.6), (3, -4.6), (9, -3), (13.5, 0.4)) + [(-1.5, 0)], CALYPTRA_D))
            for yy in (-2.2, 0.4, 2.6):
                stroke([(0.5, yy), (10, yy*0.5)], LINE*0.4, g=CALYPTRA_D)
        else:
            shape(ell(10, 0, 2.2, 3.0, 14), CAPSULE_D, LINE*0.9)
            stroke([(12, 0), (13.5, 0)], LINE*0.9)


def mech(b):
    rng = random.Random(4)
    sporophyte(44, 104, -10); sporophyte(66, 108, 6, cap=False); sporophyte(80, 96, 14)
    shoots = [(22, 34, -8), (33, 46, -6), (44, 55, -3), (56, 62, 0), (67, 56, 3), (78, 50, 5), (89, 40, 8), (98, 30, 10),
              (28, 26, -6), (40, 36, -2), (51, 44, 1), (62, 42, 2), (73, 38, 3), (84, 30, 6), (94, 22, 7)]
    for x, h, lean in shoots:
        moss_shoot(x, h, lean, rng)
    shape(ell(60, 12, 42, 5.5, 40), MOSS_BASE)


# ------------------------------------------------------------------ broadleaf twigs
def buk(b):
    twig = bez((36, 8), (44, 30), (40, 50), (48, 62), 12) + bez((48, 62), (54, 70), (50, 86), (60, 104), 12)[1:]
    specs = [(0.22, 1, COPPER, COPPER_D), (0.4, -1, GOLD, GOLD_D), (0.58, 1, GOLDGREEN, GOLDGREEN_D), (0.76, -1, GOLD, GOLD_D), (0.9, 1, COPPER, COPPER_D)]
    lens = [38, 36, 34, 28, 22]
    stem(twig, 3.4, 1.6, BEECH_TWIG)
    for (t, s, g, gd), L in zip(specs, lens):
        x, y, a = at(twig, t)
        leaf(x, y, a - s*62, L, L*0.6, g, gd, 0.75, 0.95, lambda u: 1 - 0.05*(1 - math.cos(u*6.28*6))/2, veins=7, vg=gd, stalk=3, vang=0.35)
    x, y, a = at(twig, 1.0)
    with T(x, y, 1, rot=a-90):
        bud = bez((0, -1), (2.2, 3), (1.4, 9), (0, 13)) + bez((0, 13), (-1.4, 9), (-2.2, 3), (0, -1))
        shape(bud, BUD, shadow=(bez((0, -1), (2.2, 3), (1.4, 9), (0, 13)), BUD_D))
        for yy in (3, 6, 9):
            stroke(bez((-1.4, yy), (-0.5, yy+1.4), (0.5, yy+1.4), (1.4, yy+2), 6), LINE*0.45)


def acorn(x, y, ang):
    with T(x, y, 1, rot=ang-90):
        nut = ell(0, 8, 4.6, 7.2, 30)
        shape(nut, ACORN, shadow=(ell(1.5, 7.5, 4.6, 7.8, 30), ACORN_D))
        stroke(ell(-1.8, 9, 0.9, 2.8, 10, 100, 250), LINE*0.9, g=0.95)
        shape(ell(0, 14.8, 0.6, 1.2, 8), CUP_D, LINE*0.6)
        cup = ell(0, 2.8, 5.4, 4.2, 30, 180, 360) + bez((5.4, 2.8), (5.6, 4.6), (3, 5.4), (0, 5.2)) + bez((0, 5.2), (-3, 5.4), (-5.6, 4.6), (-5.4, 2.8))
        shape(cup, CUP, shadow=(ell(0, 2.8, 5.4, 4.2, 30, 270, 360) + [(5.6, 4.8), (0, 5.2)], CUP_D))
        C.saveState(); C.clipPath(poly(cup), stroke=0, fill=0)
        for r, yy in enumerate((0, 2, 4)):
            for xx in range(-6, 7, 2):
                stroke(ell(xx + (1 if r % 2 else 0), yy, 1.2, 1.1, 8, 190, 350), LINE*0.4)
        C.restoreState()


def dub(b):
    twig = bez((50, 8), (52, 28), (58, 44), (60, 60), 20)
    stem(twig, 3.6, 2.4, OAK_TWIG)
    ped = bez((54, 30), (64, 30), (76, 28), (86, 22), 12)
    rod(ped, 1.4, OAK_TWIG, tip=False)
    acorn(86, 22, -70); acorn(76, 26, -120)
    lobed = lambda u: (0.22 + 0.78*abs(math.sin(math.pi*(u*4.6 + 0.2)))**0.5)
    x, y, a = at(twig, 1.0)
    for ang, L, g, gd in ((164, 34, OAK_B, OAK_BD), (16, 34, OAK_Y, OAK_YD), (126, 42, OAK_G, OAK_GD), (54, 42, OAK_Y, OAK_YD), (90, 46, OAK_G, OAK_GD)):
        leaf(x, y, ang, L, L*0.6, g, gd, 1.0, 0.62, lobed, cord=0.04, veins=4, vg=gd, stalk=2.5, vang=0.6)
    shape(ell(x, y+0.5, 1.8, 1.8, 12), BUD, LINE*0.8)


def briza(b):
    stem(bez((34, 8), (36, 18), (40, 26), (44, 34), 8), 7, 6, BIRCH_BARK)
    for x, y, w in ((34.5, 13, 3), (38.5, 22, 2.5), (40.5, 29, 3.2)):
        stroke([(x-w/2, y), (x+w/2, y+0.4)], LINE*1.1, g=BARK_MARK)
    twig = bez((44, 33), (54, 64), (70, 92), (98, 94), 30)
    rod(twig, 1.8, BIRCH_TWIG, tip=False)
    x, y, a = at(twig, 1.0)
    for dx, ang in ((0, -40), (0, -80)):
        with T(x, y, 1, rot=ang-90):
            ck = ell(0, 7, 2.4, 7.5, 24)
            shape(ck, CATKIN, shadow=(ell(1, 7, 2.4, 7.8, 24), CATKIN_D))
            for yy in range(1, 14, 2):
                stroke([(-2, yy), (0, yy+1.1), (2, yy)], LINE*0.4)
    toothed = lambda u: serrate(9, 0.13)(u)*serrate(19, 0.05)(u)
    specs = [(0.16, 1, 26, BIRCH_G, BIRCH_GD), (0.3, -1, 28, BIRCH_Y, BIRCH_YD), (0.46, 1, 28, BIRCH_Y, BIRCH_YD),
             (0.62, -1, 26, BIRCH_G, BIRCH_GD), (0.76, 1, 24, BIRCH_Y, BIRCH_YD), (0.88, -1, 20, BIRCH_Y, BIRCH_YD)]
    for t, s, L, g, gd in specs:
        x, y, a = at(twig, t)
        leaf(x, y, a - s*70 - 25, L, L*0.8, g, gd, 0.32, 1.25, toothed, veins=5, vg=gd, stalk=7, vang=0.5)
    for t in (0.08, 0.22, 0.38, 0.54, 0.7, 0.83, 0.94):
        x, y, a = at(twig, t)
        dot(*ray(x, y, a+90, 0.3), 0.45, BIRCH_BARK)


def maple_outline(R, lobes, teeth=0.08, n=540):
    pts = []
    for i in range(n):
        th = 270 + 360*i/n
        r = 0.08
        for la, L, hw in lobes:
            dd = abs((th - la + 180) % 360 - 180)
            if dd < hw:
                r = max(r, L*(1 - dd/hw)**0.62)
        r *= 1 - teeth*((th*0.2) % 1.0 if r > 0.25 else 0)
        pts.append(ray(0, 0, th, r*R))
    return pts


def samara(x, y, rot):
    with T(x, y, 1, rot=rot):
        for s in (-1, 1):
            with T(0, 0, 1, flip=s < 0):
                wing = bez((0, 0), (6, 3), (16, 14), (24, 20)) + bez((24, 20), (28, 24), (22, 30), (16, 26)) + bez((16, 26), (10, 20), (4, 12), (0, 5))
                shape(wing, SAMARA, shadow=(bez((0, 0), (6, 3), (16, 14), (24, 20)) + [(20, 22), (6, 8)], SAMARA_D))
                for k in range(4):
                    stroke(bez((3, 4), (8, 8+k), (14, 14+k*1.5), (20+k*0.5, 20+k*1.6), 8), LINE*0.35, g=SAMARA_D)
                shape(ell(2.2, 3.2, 3.6, 3.0, 18, rot=35), NUTLET)
        rod([(0, 1), (0.5, -6), (2, -12)], 1.3, SAMARA_D, tip=False)


def javor(b):
    bx, by = 56, 46
    rod(bez((bx, by+2), (bx-2, 30), (bx-8, 18), (bx-10, 8), 14), 2.0, MAPLE_R, tip=False)
    lobes = [(90, 1.0, 38), (38, 0.9, 36), (142, 0.9, 36), (-10, 0.55, 30), (190, 0.55, 30)]
    out = [(bx+px, by+py) for px, py in maple_outline(56, lobes)]
    half = [(bx, by)] + [(bx+px, by+py) for px, py in maple_outline(56, lobes) if px >= 0]
    shape(out, MAPLE, shadow=(half, MAPLE_R))
    for la, L, _ in lobes:
        x2, y2 = ray(bx, by, la, 56*L*0.88)
        stroke([(bx, by+1), ray(bx, by, la, 56*L*0.45), (x2, y2)], LINE*0.6, g=MAPLE_VEIN)
        for f in (0.35, 0.6):
            px, py = ray(bx, by, la, 56*L*f)
            for s in (-1, 1):
                stroke([(px, py), ray(px, py, la + s*45, 56*L*0.18)], LINE*0.4, g=MAPLE_VEIN)
    samara(86, 20, -12)


# ------------------------------------------------------------------ conifers
def conifer_shoot(pts, rng, L, w, cols, step=2.0, spread=(40, 75), front_short=True):
    n = int(sum(math.hypot(x1-x0, y1-y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:]))/step)
    back, front = [], []
    for i in range(n):
        t = 0.02 + 0.96*i/n
        x, y, a = at(pts, t)
        s = 1 if rng.random() < 0.5 else -1
        da = rng.uniform(*spread)
        ll = L*rng.uniform(0.85, 1.1)*(0.7 if t > 0.9 else 1)
        (back if rng.random() < 0.55 else front).append((x, y, a + s*da, ll, cols[rng.randrange(len(cols))], s))
    return back, front


def smrk(b):
    rng = random.Random(8)
    main = bez((60, 8), (57, 40), (63, 75), (60, 106), 30)
    sides = [bez(at(main, 0.22)[:2], (48, 36), (32, 46), (16, 54), 16), bez(at(main, 0.4)[:2], (74, 52), (88, 60), (104, 68), 16),
             bez(at(main, 0.6)[:2], (48, 74), (36, 84), (22, 92), 14), bez(at(main, 0.78)[:2], (70, 90), (80, 98), (92, 104), 12)]
    sx, sy, _ = at(sides[1], 0.62)
    rod(bez((sx, sy), (sx+1, sy-4), (sx+2, sy-7), (sx+2, sy-10), 6), 1.6, SPRUCE_TWIG, tip=False)
    with T(sx+2, sy-9, 1, rot=180):
        cone = bez((0, 0), (7, 2), (7, 24), (0, 32)) + bez((0, 32), (-7, 24), (-7, 2), (0, 0))
        shape(cone, CONE, shadow=(bez((0, 0), (7, 2), (7, 24), (0, 32)), CONE_D))
        C.saveState(); C.clipPath(poly(cone), stroke=0, fill=0)
        for r in range(11):
            for c in range(-2, 3):
                cx = c*4 + (2 if r % 2 else 0); cy = 2 + r*3.1
                stroke(ell(cx, cy, 2.2, 2.0, 10, 200, 340), LINE*0.5)
        C.restoreState()
    for pts in sides + [main]:
        back, front = conifer_shoot(pts, rng, 9.5, 1.5, (SPRUCE, SPRUCE_D, SPRUCE), step=1.1, spread=(35, 70))
        for x, y, a, l, g, s in back: needle(x, y, a, l, 1.5, g)
        stem(pts, 3.0 if pts is main else 2.1, 1.3, SPRUCE_TWIG)
        for x, y, a, l, g, s in front[::2]: needle(x, y, a, l*0.7, 1.5, g)
    x, y, a = at(main, 1.0)
    shape(ell(*ray(x, y, a, 2.2), 2.0, 3.0, 14, rot=a-90), BUD, LINE*0.9)


def fir_needle(x, y, ang, L, under):
    ex, ey = ray(x, y, ang, L)
    pts = [(x, y), (ex, ey)]
    fill(ribbon(pts, 2.0+2*OW, True, False, ext=OW, tl=0.2, tp=0.5), 0.0)
    fill(ribbon(pts, 2.0, True, False, tl=0.2, tp=0.5), FIR_UNDER if under else FIR)
    if under:
        for s in (-1, 1):
            px, py = ray(x, y, ang+90, s*0.45); qx, qy = ray(*ray(ex, ey, ang, -1.4), ang+90, s*0.45)
            fill(ribbon([ray(px, py, ang, 1.2), (qx, qy)], 0.42, False, False), STRIPE)
    else:
        stroke([ray(x, y, ang, 1.0), ray(ex, ey, ang, -0.8)], LINE*0.35, g=FIR_D)


def fir_spray(pts, L, under, gap=2.3):
    n = int(sum(math.hypot(x1-x0, y1-y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:]))/gap)
    for i in range(n):
        t = 0.02 + 0.97*i/n
        x, y, a = at(pts, t)
        ll = L*(1 - 0.45*max(0, t-0.8)/0.2)
        for s in (-1, 1):
            fir_needle(x, y, a + s*(78 - 20*t), ll, under)
    stem(pts, 2.4, 1.3, FIR_TWIG)


def jedle(b):
    main = bez((60, 8), (59, 40), (61, 75), (60, 108), 30)
    x0, y0, _ = at(main, 0.25); x1, y1, _ = at(main, 0.52); x2, y2, _ = at(main, 0.76)
    br = [(bez((x0, y0), (46, y0+6), (30, y0+12), (14, y0+18), 16), True), (bez((x0, y0), (74, y0+6), (90, y0+12), (106, y0+18), 16), True),
          (bez((x1, y1), (48, y1+6), (36, y1+12), (22, y1+16), 14), False), (bez((x1, y1), (72, y1+6), (84, y1+12), (98, y1+16), 14), False),
          (bez((x2, y2), (52, y2+6), (44, y2+10), (34, y2+13), 10), False), (bez((x2, y2), (68, y2+6), (76, y2+10), (86, y2+13), 10), False)]
    for pts, under in br:
        fir_spray(pts, 8, under)
    fir_spray(main, 8.5, False)
    cx, cy, _ = at(br[3][0], 0.45)
    cone = rrect(cx-5.5, cy, 11, 25, 5.5)
    shape(cone, FIR_CONE, shadow=(rrect(cx+0.5, cy, 5, 25, 3), FIR_CONE_D))
    C.saveState(); C.clipPath(poly(cone), stroke=0, fill=0)
    for r in range(8):
        for c in range(-2, 3):
            xx = cx + c*3.6 + (1.8 if r % 2 else 0); yy = cy + 1.5 + r*3.2
            stroke(ell(xx, yy, 2.0, 1.8, 10, 200, 340), LINE*0.5)
    C.restoreState()
    for r in range(1, 8):
        for s in (-1, 1):
            yy = cy + 1.5 + r*3.1
            shape([(cx+s*5.2, yy), (cx+s*7.6, yy+1.2), (cx+s*5.0, yy+1.6)], BRACT, LINE*0.5)
    stroke([(cx-5.5, cy+0.5), (cx+5.5, cy+0.5)], LINE, taper=False)


def modrin(b):
    rng = random.Random(11)
    twig = bez((40, 8), (40, 40), (62, 70), (82, 104), 30)
    spurs = [(0.16, 1), (0.3, -1), (0.44, 1), (0.58, -1), (0.72, 1), (0.86, -1)]
    cones = [(0.37, -1), (0.65, 1)]
    for t, s in cones:
        x, y, a = at(twig, t)
        cxx, cyy = ray(x, y, a + s*60, 9)
        rod([(x, y), (cxx, cyy)], 1.8, LARCH_TWIG, tip=False)
        with T(cxx, cyy, 1.35, rot=a + s*60 - 90):
            c = ell(0, 5.5, 5.2, 6.8, 30)
            shape(c, LARCH_CONE, shadow=(ell(1.8, 5.5, 5.2, 7.0, 30), LARCH_CONE_D))
            for yy, rx in ((3.0, 4.6), (6.4, 4.8), (9.6, 3.6)):
                for k in range(-1, 2):
                    stroke(ell(k*rx*0.62, yy, rx*0.36, 1.9, 10, 190, 350), LINE*0.5)
    stem(twig, 3.0, 1.6, LARCH_TWIG)
    for t, s in spurs:
        x, y, a = at(twig, t)
        sa = a + s*62
        sx, sy = ray(x, y, sa, 5)
        rod([(x, y), (sx, sy)], 2.6, LARCH_TWIG, tip=False)
        for k in range(23):
            da = -72 + 144*k/22 + rng.uniform(-4, 4)
            L = rng.uniform(14, 19)*(1 - abs(da)/260)
            needle(sx, sy, sa + da, L, 1.15, (LARCH, LARCH_D, LARCH, LARCH_G)[k % 4], rng.uniform(-0.8, 0.8))
        shape(ell(sx, sy, 1.8, 1.8, 10), LARCH_CONE_D, LINE*0.7)
    for t in (0.88, 0.91, 0.94, 0.97):
        x, y, a = at(twig, t)
        for s in (-1, 1):
            needle(x, y, a + s*45, 7, 1.1, LARCH if s > 0 else LARCH_G, 0)


def borovice(b):
    rng = random.Random(3)
    shoot = bez((62, 8), (59, 35), (62, 65), (60, 90), 30)
    rod(bez((58, 32), (50, 32), (44, 30), (38, 28), 6), 1.8, PINE_TWIG, tip=False)
    with T(38, 28, 1, rot=160):
        cone = bez((0, 0), (8, 0), (9, 14), (0, 22)) + bez((0, 22), (-9, 14), (-8, 0), (0, 0))
        shape(cone, PINE_CONE, shadow=(bez((0, 0), (8, 0), (9, 14), (0, 22)), PINE_CONE_D))
        C.saveState(); C.clipPath(poly(cone), stroke=0, fill=0)
        for k in range(-6, 7):
            stroke([(k*4-12, -2), (k*4+12, 24)], LINE*0.5)
            stroke([(k*4+12, -2), (k*4-12, 24)], LINE*0.5)
        for r in range(6):
            for c in range(-3, 3):
                dot(c*4 + (2 if r % 2 else 0), 1 + r*4.3, 0.55, 0.0)
        C.restoreState()
    pairs = []
    for i in range(38):
        t = 0.12 + 0.82*i/38
        x, y, a = at(shoot, t)
        s = 1 if i % 2 else -1
        da = rng.uniform(22, 50)
        L = rng.uniform(26, 32)*(1 - 0.35*max(0, t-0.75)/0.2)
        pairs.append((x, y, a + s*da, L, s, rng.random() < 0.5))
    for x, y, a, L, s, back in pairs:
        if back:
            needle(x, y, a - 4, L, 1.35, PINE_D, s*1.6); needle(x, y, a + 4, L*0.95, 1.35, PINE, s*1.2)
    stem(shoot, 3.8, 3.0, PINE_TWIG)
    x, y, a = at(shoot, 1.0)
    for da, L in ((-28, 9), (28, 9), (0, 14)):
        with T(x, y-1, 1, rot=a + da - 90):
            bud = bez((0, 0), (2.6, 2), (2.2, L*0.7), (0, L)) + bez((0, L), (-2.2, L*0.7), (-2.6, 2), (0, 0))
            shape(bud, PINE_BUD, shadow=(bez((0, 0), (2.6, 2), (2.2, L*0.7), (0, L)), PINE_BUD_D))
            for yy in (L*0.3, L*0.55):
                stroke(bez((-1.8, yy), (-0.6, yy+1.2), (0.6, yy+1.2), (1.8, yy+0.4), 6), LINE*0.4)
    for x, y, a, L, s, back in pairs:
        if not back:
            needle(x, y, a - 4, L, 1.35, PINE, s*1.6); needle(x, y, a + 4, L*0.95, 1.35, PINE_D, s*1.2)


# ------------------------------------------------------------------ heath & meadow
def vres(b):
    rng = random.Random(6)
    stems = [bez((58, 8), (52, 40), (32, 70), (20, 96), 24), bez((58, 8), (60, 40), (60, 70), (62, 110), 24),
             bez((58, 8), (66, 36), (88, 62), (100, 88), 24)]
    for pts in stems:
        stem(pts, 3.0, 1.2, WOOD)
    for pts in stems:
        n = 48
        for i in range(n):
            t = 0.06 + 0.94*i/n
            x, y, a = at(pts, t)
            s = 1 if i % 2 else -1
            if t < 0.35 or t > 0.85:
                needle(x, y, a + s*32, 3.6, 1.3, HEATHER_LEAF if i % 3 else HEATHER_LEAF_D)
        for i in range(18):
            t = 0.36 + 0.48*i/18
            x, y, a = at(pts, t)
            s = 1 if i % 2 else -1
            fa = a + s*rng.uniform(60, 100)
            px, py = ray(x, y, fa, 2.2)
            stroke([(x, y), (px, py)], LINE*0.7)
            with T(px, py, 1, rot=fa - 90):
                bell = bez((-1.2, 0), (-2.8, 1), (-2.8, 3.8), (-1.6, 5)) + [(-0.6, 4.4), (0, 5.2), (0.6, 4.4)] + bez((1.6, 5), (2.8, 3.8), (2.8, 1), (1.2, 0))
                shape(bell, HEATHER, LINE*0.8, shadow=(bez((0, 0), (0, 2), (0, 4), (0, 5.2)) + bez((1.6, 5), (2.8, 3.8), (2.8, 1), (1.2, 0)), HEATHER_D))


def thyme_head(x, y, rng):
    shape(ell(x, y+2, 8, 5.5, 24), THYME_CALYX)
    spots = [(-6.5, 3), (6.5, 3), (-3.2, 2), (3.2, 2), (0, 3.4), (-5, 7), (5, 7), (-1.7, 7.2), (1.8, 7.4), (-3.4, 11), (3.4, 11), (0, 11.6), (0, 15)]
    for dx, dy in spots:
        fx, fy = x+dx, y+dy
        fl = bez((fx-2.6, fy+0.6), (fx-2.6, fy+3.4), (fx+2.6, fy+3.4), (fx+2.6, fy+0.6), 8) + bez((fx+2.6, fy+0.6), (fx+2.4, fy-2.6), (fx-2.4, fy-2.6), (fx-2.6, fy+0.6), 8)[1:]
        shape(fl, THYME, LINE*0.75, shadow=(ell(fx+0.9, fy-1.1, 2.6, 2.2, 14), THYME_D))
        stroke([(fx-1.2, fy-0.6), (fx, fy-1.3), (fx+1.2, fy-0.6)], LINE*0.4, g=THYME_CALYX)


def materidouska(b):
    rng = random.Random(9)
    creep = bez((14, 16), (38, 6), (76, 20), (106, 12), 40)
    shoots = [(0.06, 30, -6, True), (0.2, 46, -6, True), (0.36, 58, -3, True), (0.54, 52, 4, True), (0.72, 60, 8, True),
              (0.9, 38, 6, True), (0.28, 26, -8, False), (0.46, 30, 2, False), (0.63, 24, 6, False), (0.82, 28, 12, False)]
    paths = []
    for t, h, lean, fl in shoots:
        x, y, a = at(creep, t)
        paths.append((bez((x, y), (x, y+h*0.4), (x+lean*0.6, y+h*0.8), (x+lean, y+h), 16), fl))
    for pts, fl in paths:
        rod(pts, 1.6, THYME_STEM, tip=False)
    stem(creep, 2.8, 2.0, THYME_STEM)
    for pts, fl in sorted(paths, key=lambda p: -p[0][-1][1]):
        L = sum(math.hypot(x1-x0, y1-y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:]))
        n = int(L/6)
        for i in range(1, n + (0 if fl else 1)):
            x, y, a = at(pts, i/n*(0.86 if fl else 1.0))
            for s in (-1, 1):
                leaf(x, y, a + s*(50 + 10*(i % 2)), 7, 5.2, THYME_LEAF, THYME_LEAF_D, 0.8, 0.8, lw=LINE*0.85)
        if fl:
            thyme_head(pts[-1][0], pts[-1][1], rng)
    for t in (0.13, 0.44, 0.62, 0.97):
        x, y, a = at(creep, t)
        for s in (-1, 1):
            leaf(x, y, a + 90 + s*55, 6.5, 4.8, THYME_LEAF, THYME_LEAF_D, 0.8, 0.8, lw=LINE*0.85)


def nettle_string(x, y, s, L):
    pts = bez((x, y), (x + s*8, y - 1), (x + s*14, y - L*0.5), (x + s*16, y - L), 16)
    stroke(pts, LINE*0.9)
    for i in range(1, 8):
        px, py, a = at(pts, i/7.2)
        for k in (-1, 1):
            qx, qy = ray(px, py, a + k*70, 1.2)
            shape(ell(qx, qy, 1.4, 1.1, 10), NETTLE_FL, LINE*0.6, shadow=(ell(qx+0.6, qy-0.5, 1.4, 1.1, 10), NETTLE_FL_D))


def kopriva(b):
    main = bez((60, 8), (59, 40), (61, 72), (60, 104), 30)
    nodes = [(0.2, 40), (0.46, 34), (0.7, 26), (0.88, 16)]
    tooth = serrate(10, 0.18)
    stem(main, 3.6, 1.8, NETTLE_STEM)
    for i in range(24):
        t = 0.03 + 0.94*i/24
        x, y, a = at(main, t)
        s = 1 if i % 2 else -1
        px, py = ray(x, y, a + s*90, 1.4 - 0.5*t)
        stroke([(px, py), ray(px, py, a + s*50, 2.2)], LINE*0.45)
    for t, L in nodes:
        x, y, a = at(main, t)
        for s in (-1, 1):
            leaf(x, y, a + s*(70 if L > 20 else 40), L, L*0.62, NETTLE, NETTLE_D, 0.38, 1.05, tooth, cord=0.07, veins=4, vg=NETTLE_D, stalk=6 if L > 20 else 2, vang=0.6)
    x, y, a = at(main, 1.0)
    leaf(x, y, a, 8, 4, NETTLE, NETTLE_D, 0.5, 1.0, serrate(4, 0.2))
    for t, _ in nodes[1:3]:
        x, y, a = at(main, t)
        for s in (-1, 1):
            nettle_string(x + s*1.5, y - 1, s, 24)


def vratic(b):
    main = bez((60, 8), (58, 40), (62, 60), (60, 78), 24)
    for t, s, L in ((0.18, 1, 40), (0.42, -1, 38), (0.64, 1, 30)):
        x, y, a = at(main, t)
        ang = a - s*62
        ex, ey = ray(x, y, ang, L)
        rach = bez((x, y), ray(x, y, ang, L*0.4), ray(ex, ey, ang - 90*s, -3), (ex, ey), 20)
        pinnate(rach, 7, lambda u: 5 + 9*pw(0.1+0.8*u, 0.5, 1.2), lambda i: (TANSY_LEAF, TANSY_LEAF_D), ang=60, t0=0.12, t1=0.92, wr=0.3, k=3.2, d=0.55, vein=False)
        rod(rach, 1.3, TANSY_STEM, tip=True)
    heads = [(24, 92), (34, 99), (44, 94), (54, 102), (64, 96), (74, 103), (84, 96), (94, 91), (38, 88), (58, 90), (78, 89), (48, 104), (68, 106), (88, 102), (30, 104)]
    hubs = [(40, 84), (60, 86), (80, 84)]
    for hx, hy in hubs:
        rod([(60, 76), (60 + (hx-60)*0.5, 80), (hx, hy)], 1.6, TANSY_STEM, tip=False)
    for x, y in heads:
        hx, hy = min(hubs, key=lambda h: abs(h[0]-x))
        rod([(hx, hy), ((hx+x)/2, (hy+y)/2 - 1), (x, y - 2)], 1.1, TANSY_STEM, tip=False)
    stem(main, 3.2, 2.4, TANSY_STEM)
    for x, y in sorted(heads, key=lambda h: -h[1]):
        btn = ell(x, y, 6, 4.4, 26)
        shape(btn, TANSY, shadow=(ell(x+1.5, y-1.5, 6, 4.4, 26), TANSY_D))
        stroke(ell(x, y+0.8, 3.2, 1.6, 14, 200, 340), LINE*0.45, g=TANSY_DOT)
        for dx, dy in ((-2, 1.5), (1.8, 1.8), (0, -0.8), (-3.4, -1), (3.2, -0.6)):
            dot(x+dx, y+dy, 0.42, TANSY_DOT)


def chicory_flower(x, y, r, n=17, rot=0):
    for i in range(n):
        th = rot + 360*i/n
        wt = 2*math.pi*r/n*1.05; wb = 1.4
        ray_pts = [(1.5, -wb/2), (r-0.6, -wt/2)]
        for j in range(1, 6):
            ray_pts.append((r + (0.9 if j % 2 else 0.1), -wt/2 + wt*j/6))
        ray_pts += [(r-0.6, wt/2), (1.5, wb/2)]
        with T(x, y, 1, rot=th):
            shape(ray_pts, CHICORY, LINE*0.85, shadow=([(1.5, 0), (r+1, 0)] + ray_pts[:2], CHICORY_D))
            stroke([(r*0.45, 0), (r*0.82, 0)], LINE*0.35, g=CHICORY_D)
    shape(ell(x, y, r*0.2, r*0.2, 16), CHICORY_D, LINE*0.8)
    for k in range(9):
        dot(*ray(x, y, k*40, r*0.2), 0.8, CHICORY_EYE)
    dot(x, y, r*0.08, CHICORY_EYE)


def cekanka(b):
    main = bez((56, 8), (58, 40), (60, 70), (60, 92), 24)
    left = bez(at(main, 0.4)[:2], (48, 50), (38, 56), (30, 60), 12)
    right = bez(at(main, 0.6)[:2], (70, 66), (82, 70), (92, 74), 12)
    leaf(54, 12, 150, 38, 12, CHICORY_LEAF, CHICORY_LEAF_D, 0.8, 1.0, lambda u: 1 - 0.5*(1 - (u*4) % 1.0)**2 if u < 0.8 else 1, veins=0, vg=CHICORY_LEAF_D)
    for pts in (left, right):
        rod(pts, 1.8, CHICORY_STEM, tip=False)
    stem(main, 2.8, 1.8, CHICORY_STEM)
    for t, s in ((0.4, 1), (0.6, -1), (0.2, 1)):
        x, y, a = at(main, t)
        leaf(x, y, a + s*38, 14, 4.2, CHICORY_LEAF, CHICORY_LEAF_D, 0.3, 1.2, cord=0.08, vg=CHICORY_LEAF_D)
    for pts, t in ((main, 0.78), (left, 0.5), (right, 0.45)):
        x, y, a = at(pts, t)
        with T(x, y, 1, rot=a - 90 + 30):
            bud = bez((0, 0), (3, 1), (2.6, 6), (0, 8)) + bez((0, 8), (-2.6, 6), (-3, 1), (0, 0))
            shape(bud, CHICORY_LEAF, LINE*0.85, shadow=(bez((0, 0), (3, 1), (2.6, 6), (0, 8)), CHICORY_LEAF_D))
            shape([(-0.8, 7.4), (0, 9.6), (0.8, 7.4)], CHICORY, LINE*0.6)
    chicory_flower(*right[-1], 12, rot=8)
    chicory_flower(*left[-1], 11, rot=3)
    chicory_flower(*main[-1], 15.5)


def centaury_flower(x, y, r, rot=0):
    for i in range(5):
        th = rot + 72*i + 90
        leaf(x, y, th, r, r*0.52, CENT, CENT_D, 0.9, 0.7, lw=LINE*0.85)
    for i in range(5):
        stroke([(x, y), ray(x, y, rot + 72*i + 90, r*0.55)], LINE*0.35, g=CENT_D)
    shape(ell(x, y, r*0.24, r*0.24, 14), CENT_EYE, LINE*0.6)
    for i in range(5):
        dot(*ray(x, y, rot + 72*i + 126, r*0.12), 0.65, ANTHER)
    dot(x, y, 0.5, CENT_D)


def zemezluc(b):
    rng = random.Random(2)
    for ang, L in ((172, 22), (140, 24), (8, 22), (40, 24), (112, 18), (70, 18)):
        leaf(60, 11, ang, L, L*0.46, CENT_LEAF, CENT_LEAF_D, 1.0, 0.7, veins=0, vg=CENT_LEAF_D)
    fork = (60, 66)
    main = bez((60, 10), (59, 30), (61, 50), fork, 20)
    tips = [(28, 92), (40, 101), (54, 106), (66, 104), (80, 100), (92, 91), (46, 88), (74, 88), (60, 94)]
    hubs = [(44, 80), (60, 82), (76, 80)]
    for hx, hy in hubs:
        rod([fork, ((fork[0]+hx)/2, (fork[1]+hy)/2 + 1), (hx, hy)], 1.4, CENT_STEM, tip=False)
    for x, y in tips:
        hx, hy = min(hubs, key=lambda h: math.hypot(h[0]-x, h[1]-y))
        rod([(hx, hy), ((hx+x)/2, (hy+y)/2), (x, y)], 1.1, CENT_STEM, tip=False)
    for hx, hy in hubs:
        for s in (-1, 1):
            leaf(hx, hy, 90 + s*40, 6, 2.2, CENT_LEAF, CENT_LEAF_D, 0.6, 1.0, lw=LINE*0.8)
    stem(main, 2.4, 1.8, CENT_STEM)
    for t in (0.35, 0.68):
        x, y, a = at(main, t)
        for s in (-1, 1):
            leaf(x, y, a + s*38, 12, 4.2, CENT_LEAF, CENT_LEAF_D, 0.8, 0.9, vg=CENT_LEAF_D)
    for x, y, ang in ((36, 96, 110), (70, 100, 70), (86, 94, 60)):
        with T(x, y, 1, rot=ang - 90):
            bud = bez((0, 0), (2, 1), (1.8, 6), (0, 9)) + bez((0, 9), (-1.8, 6), (-2, 1), (0, 0))
            shape(bud, CENT, LINE*0.8, shadow=(bez((0, 0), (2, 1), (1.8, 6), (0, 9)), CENT_D))
            shape(bez((-1.9, 0), (-1.6, 2.4), (1.6, 2.4), (1.9, 0)) + [(0, -1)], CENT_LEAF, LINE*0.6)
    for (x, y) in sorted(tips, key=lambda p: -p[1]):
        centaury_flower(x, y, 9.5, rng.uniform(-15, 15))


ASSETS = [(n, 120, 120, f, "atlas") for n, f in (
    ("kapradi", kapradi), ("mech", mech), ("buk", buk), ("smrk", smrk), ("jedle", jedle), ("dub", dub),
    ("briza", briza), ("javor", javor), ("modrin", modrin), ("borovice", borovice), ("vres", vres),
    ("materidouska", materidouska), ("kopriva", kopriva), ("vratic", vratic), ("cekanka", cekanka), ("zemezluc", zemezluc))]
