"""Autumn finds for the atlas: mushrooms (edible and poisonous), berries, nuts and fruit of the Brdy woods."""
import math, random
from lib import C, Col, ell, bez
from style3 import *

W = LINE
CX = 60

SHINE = Col(1.0, "#ffffff", alpha=0.8)
BLOOM = Col(0.7, "#aab4e0", alpha=0.55)
MOSS = Col(0.55, "#86a94c")
MOSS_DARK = Col(0.4, "#5f8033")
GRASS = Col(0.6, "#a3bf5c")
FALLEN = Col(0.6, "#e0913a")
FALLEN2 = Col(0.5, "#c0612c")
WHITE = Col(0.97, "#fffcf2")
GILL = Col(0.95, "#f7f1e2")
GILL_LINE = Col(0.7, "#cbbd9f")
TWIG = Col(0.4, "#7a4f33")
TWIG_DARK = Col(0.3, "#4a3326")
LEAF = Col(0.55, "#6fa044")
LEAF_VEIN = Col(0.4, "#4e7a2e")
LEAF_YELLOW = Col(0.75, "#e8c140")
LEAF_ORANGE = Col(0.6, "#e5892f")
LEAF_RED = Col(0.45, "#c9472e")

FLY_RED = Col(0.4, "#e2372a")
FLY_WART = Col(0.97, "#fdf8ea")
TYL_CAP = Col(0.65, "#c89b6a")
TYL_PORE = Col(0.85, "#f1cfc8")
TYL_PORE_DOT = Col(0.65, "#d49c93")
TYL_STEM = Col(0.85, "#eadbb8")
TYL_NET = Col(0.35, "#6e4e33")
DEATH_CAP = Col(0.7, "#b3bd72")
DEATH_CENTRE = Col(0.55, "#8d9a4e")
DEATH_FIBRE = Col(0.5, "#7c8a44")
DEATH_STEM = Col(0.95, "#f4f5e6")
DEATH_BAND = Col(0.85, "#dfe3c6")
BUN = Col(0.45, "#8e5430")
BUN_RIM = Col(0.7, "#d3a877")
BUN_PORE = Col(0.9, "#f1e6b4")
BUN_PORE_DOT = Col(0.75, "#d6c47e")
BUN_STEM = Col(0.85, "#e8d7ae")
BUN_NET = Col(1.0, "#fffaf0")
CHANT = Col(0.8, "#f5b81f")
CHANT_TOP = Col(0.85, "#fbc93a")
CHANT_DEEP = Col(0.7, "#e39c14")
CHANT_RIDGE = Col(0.6, "#c98410")
BIRCH_CAP = Col(0.5, "#a06b42")
BIRCH_PORE = Col(0.92, "#ece6d8")
BIRCH_STEM = Col(0.95, "#f3efe6")
SCABER = Col(0.15, "#33291f")
HONEY = Col(0.65, "#d19a45")
HONEY_DARK = Col(0.45, "#8f5d29")
HONEY_GILL = Col(0.9, "#f2e4bd")
HONEY_STEM = Col(0.85, "#eed8a6")
HONEY_RING = Col(0.97, "#fbf5e1")
PUFF = Col(0.95, "#f6f1e1")
PUFF_WART = Col(0.8, "#ddd2b6")
JACK = Col(0.3, "#6d3a1c")
JACK_PORE = Col(0.8, "#eecb36")
JACK_PORE_DOT = Col(0.6, "#c9a320")
JACK_STEM = Col(0.9, "#f2e5a8")
JACK_RING = Col(0.8, "#dcd0e2")
JACK_RING_DARK = Col(0.45, "#8c6a86")
PARA_CAP = Col(0.9, "#f1e3c7")
PARA_SCALE = Col(0.45, "#9a6a45")
PARA_UMBO = Col(0.3, "#6e4326")
PARA_STEM = Col(0.9, "#efe2c6")
PARA_SNAKE = Col(0.55, "#a67c56")
SAFF = Col(0.65, "#ee8a3c")
SAFF_RING = Col(0.5, "#d0602a")
SAFF_GILL = Col(0.7, "#f4a456")
SAFF_STAIN = Col(0.5, "#6f9656")

HIP = Col(0.45, "#e2412a")
ROWAN = Col(0.5, "#f05a24")
SLOE = Col(0.25, "#3e3a78")
LINGON = Col(0.4, "#d4202c")
LINGON_LEAF = Col(0.35, "#2f6b3c")
BILBERRY = Col(0.2, "#2c3a74")
BILBERRY_STEM = Col(0.55, "#5f9a3c")
BLACKBERRY = Col(0.1, "#241a2e")
BLACKBERRY_HI = Col(0.4, "#5a3f6e")
RASP_RED = Col(0.4, "#cc2a3c")
UNRIPE = Col(0.7, "#b9c860")
ACORN = Col(0.55, "#b9862f")
ACORN_GREEN = Col(0.65, "#a9a64a")
CUP = Col(0.5, "#8c6a3f")
CUP_SCALE = Col(0.35, "#5f4527")
OAK = Col(0.65, "#b3a93f")
BEECH = Col(0.55, "#d37a2c")
BEECH_VEIN = Col(0.4, "#9d4f1c")
HUSK = Col(0.5, "#9a6c3e")
HUSK_IN = Col(0.8, "#e6cb98")
BEECHNUT = Col(0.35, "#7b4726")
BEECHNUT_LIT = Col(0.5, "#a9683a")
WALNUT_HUSK = Col(0.55, "#7ea443")
WALNUT_HUSK_IN = Col(0.4, "#5c5a2c")
WALNUT = Col(0.7, "#c89b5d")
WALNUT_LINE = Col(0.45, "#8d6533")
APPLE = Col(0.8, "#f0c63f")
APPLE_RED = Col(0.45, "#d8412f", alpha=0.55)
APPLE_BLUSH = Col(0.5, "#d8412f", alpha=0.32)
CONKER = Col(0.3, "#83391b")
CONKER_LIT = Col(0.45, "#b25a2c")
HILUM = Col(0.85, "#ead3a4")
CHEST_SHELL = Col(0.6, "#93b44c")
CHEST_LINING = Col(0.95, "#f4efd9")
CONE = Col(0.5, "#9a6436")
CONE_DARK = Col(0.3, "#5c3a20")
CONE_EDGE = Col(0.65, "#c28a52")


class clip:
    def __init__(self, pts): self.p = pts
    def __enter__(self): C.saveState(); C.clipPath(poly(self.p), stroke=0, fill=0)
    def __exit__(self, *e): C.restoreState()


def inside(pts, x, y):
    c = False; j = len(pts) - 1
    for i in range(len(pts)):
        (xi, yi), (xj, yj) = pts[i], pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi)*(y - yi)/(yj - yi) + xi: c = not c
        j = i
    return c


def scatter(pts, n, seed, margin=2, mind=5, tries=3000):
    r = random.Random(seed); x0, y0, x1, y1 = bbox(pts); out = []
    for _ in range(tries):
        if len(out) >= n: break
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        if all(inside(pts, x+dx, y+dy) for dx, dy in ((margin, 0), (-margin, 0), (0, margin), (0, -margin))) \
                and all(math.hypot(x-a, y-b) > mind for a, b in out):
            out.append((x, y))
    return out


def mirror(half, x):
    return half + [(2*x - px, py) for px, py in reversed(half)]


def blade(p0, p1, wd, bulge=0.5, N=40):
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1-x0, y1-y0); ux, uy = (x1-x0)/L, (y1-y0)/L; nx, ny = -uy, ux
    k = math.log(0.5)/math.log(bulge)
    side = lambda s: [(x0+ux*L*i/N+nx*s*wd/2*math.sin(math.pi*(i/N)**k), y0+uy*L*i/N+ny*s*wd/2*math.sin(math.pi*(i/N)**k)) for i in range(N+1)]
    return side(1) + list(reversed(side(-1)))[1:-1]


def glint(x, y, rx, ry, rot=0):
    fill(ell(x, y, rx, ry, 14, rot=rot), SHINE)


def leaf(p0, p1, wd, g, vein=None, serr=0.0, teeth=12, bulge=0.4, veins=4, lobes=0, w=W, sh=0.1):
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1-x0, y1-y0); ux, uy = (x1-x0)/L, (y1-y0)/L; nx, ny = -uy, ux
    k = math.log(0.5)/math.log(bulge); N = 60; sides = []
    for s in (1, -1):
        pts = []
        for i in range(N+1):
            t = i/N
            ww = wd/2*math.sin(math.pi*t**k)
            if lobes: ww *= 0.38 + 0.62*abs(math.sin(math.pi*lobes*t + 0.3))**0.6
            if serr: ww -= serr*((t*teeth) % 1)*math.sin(math.pi*t)
            pts.append((x0+ux*L*t+nx*ww*s, y0+uy*L*t+ny*ww*s))
        sides.append(pts)
    out = sides[0] + list(reversed(sides[1]))
    form(out, g, w, sdx=-nx*wd*0.12 - ux*wd*0.05, sdy=-ny*wd*0.12 + wd*0.08, sh=sh)
    if vein is not None:
        stroke([(x0+ux*L*0.02, y0+uy*L*0.02), (x0+ux*L*0.9, y0+uy*L*0.9)], w*0.6, g=vein)
        for i in range(veins):
            t = 0.18 + 0.66*i/max(1, veins-1)
            mx, my = x0+ux*L*t, y0+uy*L*t
            ww = wd/2*math.sin(math.pi*min(0.99, t+0.12)**k)*0.75
            for s in (1, -1):
                stroke([(mx, my), (mx+ux*L*0.12+nx*ww*s, my+uy*L*0.12+ny*ww*s)], w*0.45, g=vein)
    return out


def tuft(w, h=6, cx=CX, y=8, seed=1, blades=((-0.42, -5), (-0.36, 2), (0.4, 4), (0.45, -3)), fallen=0.28):
    r = random.Random(seed)
    m = mirror(bez((cx-w/2, y), (cx-w/2+w*0.08, y+h*1.25), (cx-w*0.25, y+h), (cx, y+h)), cx)
    for fx, lean in blades:
        bx = cx + fx*w
        leaf((bx, y+h*0.6), (bx+lean, y+h+9+abs(lean)), 2.6, GRASS, w=W*0.8, sh=0)
    form(m, MOSS, sdx=-2, sdy=2.5, sh=0.14)
    with clip(m):
        for _ in range(int(w/2)):
            px, py = cx + r.uniform(-w/2, w/2), y + r.uniform(1, h+1)
            stroke(ell(px, py, 1.4, 1.1, 8, 200, 340), W*0.5, g=MOSS_DARK)
    if fallen:
        fx = cx + fallen*w
        leaf((fx-8, y+h*0.4), (fx+9, y+h*0.9+2), 7, FALLEN, vein=FALLEN2, veins=2)


def stipe(x, y0, y1, wb, wt, mid=None, bot=0.15):
    mid = mid if mid is not None else (wb + wt)/2
    Lf = bez((x-wb/2, y0), (x-mid/2, y0+(y1-y0)*0.35), (x-wt/2, y1-(y1-y0)*0.3), (x-wt/2, y1))
    R = [(2*x-px, py) for px, py in reversed(Lf)]
    return Lf + R + list(reversed(ell(x, y0, wb/2, wb*bot, 16, 180, 360)))[1:-1]


def cap(x, y, r, h, under=3, shoulder=0.75, top=0.6, umbo=0):
    half = bez((x-r, y), (x-r*1.04, y+h*shoulder), (x-r*top, y+h), (x, y+h))
    if umbo:
        half = bez((x-r, y), (x-r*1.04, y+h*shoulder), (x-r*top, y+h), (x-umbo*1.6, y+h)) + \
               bez((x-umbo*1.6, y+h), (x-umbo, y+h+umbo*0.2), (x-umbo*0.6, y+h+umbo), (x, y+h+umbo))
    top_ = mirror(half, x)
    return top_ + bez((x+r, y), (x+r*0.5, y-under), (x-r*0.5, y-under), (x-r, y))[1:-1]


def gills(x, y, r, ry, g=GILL, lg=GILL_LINE, n=26, conv=2, pores=None):
    reg = ell(x, y, r, ry, 40, 180, 360)
    fill(reg, g)
    with clip(reg):
        if pores:
            rr = random.Random(int(r*7))
            for _ in range(int(r*ry*0.9)):
                dot(x + rr.uniform(-r, r), y - rr.uniform(0, ry), 0.55, pores)
        else:
            for i in range(n+1):
                a = math.radians(180 + 180*i/n)
                stroke([(x+math.cos(a)*r*1.02, y+math.sin(a)*ry*1.02), (x, y+conv)], W*0.4, g=lg)
    stroke(reg, W, closed=True)


def shiny(x, y, r, g, sh=0.18, hl=True):
    e = ell(x, y, r, r, 24)
    form(e, g, sdx=-r*0.3, sdy=r*0.3, sh=sh)
    if hl: glint(x-r*0.38, y+r*0.38, r*0.26, r*0.17, 40)
    return e


def net(pts, g, gap=4.5, lw=W*0.5, seed=3):
    r = random.Random(seed); x0, y0, x1, y1 = bbox(pts); H = y1 - y0
    with clip(pts):
        for s in (1, -1):
            xx = x0 - H*0.4
            while xx < x1 + H*0.4:
                line_ = [(xx + s*(t/8)*H*0.35 + r.uniform(-0.5, 0.5), y0 + H*t/8) for t in range(9)]
                stroke(line_, lw, g=g)
                xx += gap


# ------------------------------------------------------------------ poisonous
def muchomurka(b):
    stem = stipe(CX, 17, 64, 18, 13, mid=15)
    bulb = ell(CX, 20, 14, 9.5, 30)
    gills(CX, 63, 42, 8)
    form(bulb, WHITE, sdx=-3, sdy=2, sh=0.12)
    form(stem, WHITE, sdx=-3, sdy=0, sh=0.1)
    for yy, rx in ((24, 12.5), (19.5, 13.5)):
        stroke(ell(CX, yy, rx, 3, 20, 190, 350), W*0.7)
        for i in range(5):
            ax = CX - rx*0.8 + i*rx*0.4
            stroke([(ax-1.5, yy-2.6), (ax, yy-1.2), (ax+1.5, yy-2.8)], W*0.5, g=GILL_LINE)
    skirt = bez((CX-7, 56), (CX-9, 53), (CX-12, 48), (CX-13, 46)) + bez((CX-13, 46), (CX-6, 43), (CX+6, 43), (CX+13, 46)) + bez((CX+13, 46), (CX+12, 48), (CX+9, 53), (CX+7, 56))
    form(skirt, WHITE, sdx=-2, sdy=1, sh=0.12)
    for sx in (-8, -3, 3, 8):
        stroke([(CX+sx*0.7, 54), (CX+sx, 46)], W*0.4, g=GILL_LINE)
    c = cap(CX, 63, 45, 40, under=3, shoulder=0.7, top=0.62)
    form(c, FLY_RED, sdx=-6, sdy=4, sh=0.16)
    for i, (x, y) in enumerate(scatter(c, 16, 11, margin=4.5, mind=10.5)):
        rr = random.Random(i); s = rr.uniform(2.2, 3.6)
        pts = [(x+math.cos(a)*s*rr.uniform(0.75, 1.25), y+math.sin(a)*s*rr.uniform(0.6, 1.0)) for a in [k*math.pi/3 for k in range(6)]]
        shape(pts, FLY_WART, W*0.6)
    glint(CX-26, 88, 6, 2.2, 45)
    tuft(76, 7, seed=4)


def horcak(b):
    stem = stipe(CX, 14, 66, 34, 21, mid=34)
    gills(CX, 66, 42, 8, TYL_PORE, pores=TYL_PORE_DOT)
    form(stem, TYL_STEM, sdx=-5, sdy=0, sh=0.12)
    net([(x, y) for x, y in stem if y > 16], TYL_NET, gap=4.2, lw=W*0.55)
    stroke(stem, W, closed=True)
    c = cap(CX, 66, 45, 34, under=4, shoulder=0.8, top=0.55)
    form(c, TYL_CAP, sdx=-6, sdy=4, sh=0.14)
    glint(CX-24, 90, 5, 1.8, 40)
    tuft(80, 7, seed=7)


def zelena(b):
    tuft(86, 5, seed=9, fallen=-0.3)
    stem = stipe(CX, 22, 72, 17, 11, mid=13)
    gills(CX, 71, 41, 10, n=30)
    form(stem, DEATH_STEM, sdx=-3, sdy=0, sh=0.1)
    with clip(stem):
        for yy in range(26, 60, 6):
            stroke([(CX-10+k*2.5, yy+(k % 2)*1.6) for k in range(9)], W*0.45, g=DEATH_BAND)
    bulb = ell(CX, 22, 13.5, 9, 30)
    form(bulb, DEATH_STEM, sdx=-3, sdy=2, sh=0.1)
    volva = [(CX-17, 26), (CX-14, 30), (CX-12, 25), (CX-8, 27), (CX-6, 22)] + \
        bez((CX-6, 22), (CX-2, 20), (CX+3, 20), (CX+6, 23)) + [(CX+9, 28), (CX+12, 24), (CX+15, 29), (CX+17, 25)] + \
        bez((CX+17, 25), (CX+19, 16), (CX+12, 11), (CX, 11)) + bez((CX, 11), (CX-12, 11), (CX-19, 16), (CX-17, 26))[1:-1]
    form(volva, WHITE, sdx=-3, sdy=2, sh=0.14)
    for sx in (-10, -4, 4, 10):
        stroke([(CX+sx, 21), (CX+sx*0.9, 14)], W*0.45, g=GILL_LINE)
    skirt = bez((CX-5.5, 64), (CX-8, 60), (CX-12, 56), (CX-14, 51)) + [(CX-10, 49.5), (CX-6, 51.5), (CX-2, 49.5), (CX+3, 51.5), (CX+7, 49.5), (CX+11, 51.5), (CX+14, 51)] + \
        bez((CX+14, 51), (CX+12, 56), (CX+8, 60), (CX+5.5, 64))
    form(skirt, WHITE, sdx=-2, sdy=1, sh=0.12)
    for sx in (-9, -4, 1, 6, 10):
        stroke([(CX+sx*0.5, 62), (CX+sx, 52)], W*0.4, g=GILL_LINE)
    c = cap(CX, 71, 44, 27, under=3, shoulder=0.65, top=0.7)
    form(c, DEATH_CAP, sdx=-6, sdy=3, sh=0.14)
    with clip(c):
        fill(ell(CX, 98, 22, 9, 24), DEATH_CENTRE)
        for i in range(26):
            a = math.radians(200 + i*140/25)
            stroke([(CX+math.cos(a)*8, 98+math.sin(a)*4), (CX+math.cos(a)*50, 98+math.sin(a)*32)], W*0.4, g=DEATH_FIBRE)
    stroke(c, W, closed=True)
    glint(CX-24, 88, 5, 1.8, 40)


# ------------------------------------------------------------------ edible mushrooms
def hrib(b):
    stem = stipe(CX, 13, 64, 40, 26, mid=50)
    gills(CX, 65, 45, 9, BUN_PORE, pores=BUN_PORE_DOT)
    form(stem, BUN_STEM, sdx=-7, sdy=0, sh=0.12)
    net([(x, y) for x, y in stem if y > 42], BUN_NET, gap=3.2, lw=W*0.5)
    stroke(stem, W, closed=True)
    c = cap(CX, 65, 48, 40, under=5, shoulder=0.85, top=0.55)
    form(c, BUN, sdx=-6, sdy=5, sh=0.16)
    with clip(c):
        stroke(bez((CX-49, 64), (CX-20, 57), (CX+20, 57), (CX+49, 64)), W*2.4, g=BUN_RIM, taper=False)
    stroke(c, W, closed=True)
    glint(CX-25, 92, 7, 2.6, 40)
    tuft(84, 7, seed=12)


def chanterelle(x, y, s, seed):
    with T(x, y, s):
        body = bez((-7, 0), (-6, 22), (-10, 34), (-38, 50)) + ell(0, 50, 38, 8, 30, 180, 360)[1:-1] + bez((38, 50), (10, 34), (6, 22), (7, 0))
        form(body, CHANT, sdx=-4, sdy=0, sh=0.12)
        rr = random.Random(seed)
        with clip(body):
            for i in range(15):
                a = math.radians(190 + i*160/14)
                ex, ey = math.cos(a)*38, 50 + math.sin(a)*8
                sx = (ex/38)*6
                pts = bez((ex, ey), (ex*0.6, ey-10), (sx*1.5, 30), (sx, 8))
                stroke(pts, W*0.55, g=CHANT_RIDGE)
                if i % 2:
                    j = rr.randint(3, 6)
                    stroke([pts[j], (pts[j][0]+ex*0.12, pts[j][1]+4)], W*0.5, g=CHANT_RIDGE)
        stroke(body, W, closed=True)
        top = [(math.cos(math.radians(a))*38*(1+0.035*math.sin(math.radians(a)*7)), 51+math.sin(math.radians(a))*10*(1+0.05*math.sin(math.radians(a)*7))) for a in range(0, 360, 6)]
        form(top, CHANT_TOP, sdx=0, sdy=0, sh=0)
        fill(ell(2, 51.5, 20, 4.5, 24), CHANT_DEEP)
        stroke(ell(2, 51.5, 20, 4.5, 24, 190, 350), W*0.6, g=CHANT_RIDGE)


def liska_houba(b):
    chanterelle(34, 10, 0.55, 2)
    chanterelle(CX+10, 10, 1.1, 5)
    tuft(88, 6, seed=14, fallen=-0.3)


def kozak(b):
    stem = stipe(CX, 13, 70, 24, 15, mid=18)
    gills(CX, 70, 38, 7, BIRCH_PORE, pores=GILL_LINE)
    form(stem, BIRCH_STEM, sdx=-4, sdy=0, sh=0.1)
    rr = random.Random(5)
    with clip(stem):
        for _ in range(110):
            y = 14 + 56*rr.random()**1.3
            x = CX + rr.uniform(-13, 13)
            stroke([(x, y), (x+rr.uniform(-0.4, 0.4), y+rr.uniform(1.2, 2.8))], W*0.85, g=SCABER)
    stroke(stem, W, closed=True)
    c = cap(CX, 70, 41, 31, under=4, shoulder=0.8, top=0.55)
    form(c, BIRCH_CAP, sdx=-5, sdy=4, sh=0.15)
    glint(CX-21, 92, 5, 1.8, 40)
    tuft(66, 7, seed=16)


def honey(sx, sy, ex, ey, r, seed):
    tube(bez((sx, sy), (sx, sy+(ey-sy)*0.4), (ex, ey-(ey-sy)*0.5), (ex, ey)), r*0.34, r*0.3, HONEY_STEM, sh=0.1)
    gills(ex, ey, r*0.95, r*0.22, HONEY_GILL, GILL_LINE, n=16)
    ry = ey - r*0.42
    ring = [(ex-r*0.26, ry+2)] + bez((ex-r*0.26, ry+2), (ex-r*0.32, ry-1), (ex-r*0.36, ry-2.5), (ex-r*0.38, ry-3.5)) + \
        [(ex-r*0.15, ry-2.2), (ex, ry-3.5), (ex+r*0.15, ry-2.2), (ex+r*0.38, ry-3.5), (ex+r*0.26, ry+2)]
    shape(ring, HONEY_RING, W*0.8)
    c = cap(ex, ey, r, r*0.5, under=2, shoulder=0.6, top=0.65, umbo=r*0.12)
    form(c, HONEY, sdx=-r*0.14, sdy=r*0.1, sh=0.14)
    with clip(c):
        fill(ell(ex, ey+r*0.62, r*0.45, r*0.2, 20), HONEY_DARK)
        for x, y in scatter(c, int(r*0.9), seed, margin=2, mind=3.6):
            if y > ey + r*0.18:
                stroke([(x-0.7, y-0.4), (x, y+0.4), (x+0.7, y-0.4)], W*0.5, g=HONEY_DARK)
    stroke(c, W, closed=True)


def vaclavka(b):
    honey(62, 12, 64, 88, 19, 1)
    honey(58, 12, 36, 70, 22, 2)
    honey(64, 12, 88, 64, 20, 3)
    honey(60, 12, 58, 40, 15, 4)
    tuft(72, 6, seed=18, fallen=0.33)


def puffball(x, y, s, seed):
    with T(x, y, s):
        body = bez((-10, 0), (-10, 14), (-32, 26), (-32, 44)) + bez((-32, 44), (-32, 60), (-17, 68), (0, 68)) + \
            bez((0, 68), (17, 68), (32, 60), (32, 44)) + bez((32, 44), (32, 26), (10, 14), (10, 0))
        form(body, PUFF, sdx=-6, sdy=3, sh=0.13)
        with clip(body):
            stroke(bez((-26, 30), (-10, 24), (10, 24), (26, 30)), W*0.5, g=PUFF_WART)
            for px, py in scatter(body, 70, seed, margin=3, mind=4.6):
                if py > 28:
                    shape(ell(px, py, 1.3, 1.2, 8), PUFF_WART, W*0.5)
                    dot(px-0.3, py+0.3, 0.45, WHITE)
                elif py > 6:
                    dot(px, py, 0.5, PUFF_WART)
        stroke(body, W, closed=True)
        shape(ell(0, 67.5, 3, 2, 10), PUFF_WART, W*0.7)


def pychavka(b):
    puffball(48, 8, 1.2, 3)
    puffball(94, 8, 0.66, 8)
    tuft(98, 6, seed=20, fallen=0.0)


def klouzek(b):
    stem = stipe(CX, 14, 66, 22, 17, mid=21)
    gills(CX, 66, 42, 8, JACK_PORE, pores=JACK_PORE_DOT)
    form(stem, JACK_STEM, sdx=-4, sdy=0, sh=0.1)
    rr = random.Random(2)
    with clip(stem):
        for _ in range(18):
            dot(CX + rr.uniform(-8, 8), rr.uniform(52, 64), 0.6, JACK_PORE_DOT)
    stroke(stem, W, closed=True)
    ring_under = bez((CX-12, 46), (CX-6, 42), (CX+6, 42), (CX+12, 46)) + bez((CX+12, 46), (CX+10, 49), (CX+4, 50), (CX, 50)) + bez((CX, 50), (CX-4, 50), (CX-10, 49), (CX-12, 46))[1:]
    form(ring_under, JACK_RING_DARK, sh=0)
    ring = bez((CX-8.5, 52), (CX-11, 50), (CX-13, 48), (CX-12, 46)) + bez((CX-12, 46), (CX-6, 49), (CX+6, 49), (CX+12, 46)) + bez((CX+12, 46), (CX+13, 48), (CX+11, 50), (CX+8.5, 52))
    form(ring, JACK_RING, sh=0.1)
    c = cap(CX, 66, 46, 32, under=4, shoulder=0.72, top=0.6)
    form(c, JACK, sdx=-6, sdy=4, sh=0.2)
    with clip(c):
        stroke(bez((CX-38, 78), (CX-34, 88), (CX-22, 95), (CX-8, 97)), W*2.6, g=SHINE)
        glint(CX+2, 97.5, 3, 1.4)
        glint(CX+24, 88, 5, 1.5, -40)
    stroke(c, W, closed=True)
    tuft(80, 7, seed=22)


def bedla(b):
    stem = stipe(CX, 18, 84, 11, 8, mid=8)
    gills(CX, 84, 47, 7, n=34)
    form(stem, PARA_STEM, sdx=-2.5, sdy=0, sh=0.1)
    with clip(stem):
        for yy in range(20, 62, 5):
            zz = [(CX-6+k*1.5, yy+(1.6 if k % 2 else 0)) for k in range(9)]
            fill(zz + [(CX+7, yy+3.2), (CX-7, yy+3.2)], PARA_SNAKE)
    stroke(stem, W, closed=True)
    bulb = ell(CX, 20, 10, 7.5, 24)
    form(bulb, PARA_STEM, sdx=-2, sdy=1, sh=0.1)
    fill(ell(CX, 22, 7, 2.5, 16, 180, 360), PARA_SNAKE)
    ring = mirror(bez((CX-5, 70), (CX-8, 69), (CX-9, 67), (CX-8.5, 63)), CX) + bez((CX+8.5, 63), (CX+3, 61), (CX-3, 61), (CX-8.5, 63))[1:-1]
    form(ring, PARA_CAP, sh=0.1)
    stroke(bez((CX-8.7, 66), (CX-3, 64), (CX+3, 64), (CX+8.7, 66)), W*0.6)
    c = cap(CX, 84, 50, 14, under=3, shoulder=0.4, top=0.72, umbo=6)
    form(c, PARA_CAP, sdx=-6, sdy=2, sh=0.12)
    with clip(c):
        for x, y in scatter(c, 60, 6, margin=1.5, mind=4.5):
            d = abs(x - CX)/50
            s = 1.2 + 1.6*(1-d)
            pts = [(x-s, y), (x, y-s*0.6), (x+s, y), (x+s*0.2, y+s*0.4)]
            fill(pts, PARA_SCALE)
        fill(ell(CX, 101, 13, 5.5, 24), PARA_UMBO)
        for i in range(9):
            a = math.radians(180 + i*180/8)
            fill(ell(CX+math.cos(a)*16, 99.5+math.sin(a)*4, 3, 1.4, 10), PARA_SCALE)
    stroke(c, W, closed=True)
    tuft(52, 6, seed=24, fallen=0.4)


def ryzec(b):
    stem = stipe(CX, 13, 52, 22, 20, mid=23)
    under = ell(CX, 64, 46, 25, 40, 180, 360)
    fill(under, SAFF_GILL)
    with clip(under):
        for i in range(40):
            a = math.radians(180 + i*180/39)
            stroke([(CX+math.cos(a)*47, 64+math.sin(a)*26), (CX, 50)], W*0.45, g=SAFF_RING)
    stroke(under, W, closed=True)
    form(stem, SAFF, sdx=-4, sdy=0, sh=0.12)
    rr = random.Random(9)
    with clip(stem):
        for _ in range(7):
            fill(ell(CX+rr.uniform(-8, 8), rr.uniform(16, 46), 2.2, 1.4, 10), SAFF_RING)
    stroke(stem, W, closed=True)
    rim = [(math.cos(math.radians(a))*46*(1+0.02*math.sin(math.radians(a)*5)), math.sin(math.radians(a))*17) for a in range(0, 360, 5)]
    form([(CX+x, 62+y) for x, y in rim], SAFF_RING, sh=0)
    top = [(CX+x, 66+y) for x, y in rim]
    form(top, SAFF, sdx=0, sdy=0, sh=0)
    with clip(top):
        for k, f in enumerate((0.84, 0.64, 0.44)):
            stroke(ell(CX+1, 67, 46*f, 17*f, 30), W*(1.6 - k*0.3), g=SAFF_RING, closed=True)
        fill(ell(CX+1, 68, 12, 4.2, 20), SAFF_RING)
        for x, y, s in ((CX-30, 57, 5), (CX+24, 58, 4), (CX+38, 67, 3), (CX-12, 53, 3)):
            fill([(x+math.cos(a)*s*(1+0.3*math.sin(a*3)), y+math.sin(a)*s*0.55) for a in [i*math.pi/8 for i in range(16)]], SAFF_STAIN)
    stroke(top, W, closed=True)
    tuft(74, 7, seed=26)


# ------------------------------------------------------------------ fruit, nuts, cones
def thorn(x, y, ang, l=5, hook=0.5):
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); nx, ny = -uy, ux
    tip = (x+ux*l+nx*l*hook*0.4, y+uy*l+ny*l*hook*0.4)
    shape([(x-nx*1.6, y-ny*1.6), tip, (x+nx*1.6, y+ny*1.6)], TWIG, W*0.7)


def pinnate(base, ang, n, ll, lw, cols, rachis=TWIG, serr=0.6):
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a)
    L = n*ll*0.55 + ll*0.4
    tip = (base[0]+ux*L, base[1]+uy*L)
    stroke([base, tip], W*1.2, g=rachis)
    for i in range(n):
        t = (i+1)/(n+0.3)
        px, py = base[0]+ux*L*t*0.95, base[1]+uy*L*t*0.95
        for s in (1, -1):
            b2 = a + s*math.radians(62)
            leaf((px, py), (px+math.cos(b2)*ll, py+math.sin(b2)*ll), lw, cols[(i+(s > 0)) % len(cols)], vein=LEAF_VEIN, serr=serr, teeth=9, veins=0)
    leaf(tip, (tip[0]+ux*ll, tip[1]+uy*ll), lw, cols[0], vein=LEAF_VEIN, serr=serr, teeth=9, veins=0)


def hip(x, y, rot):
    with T(x, y, 1, rot=rot):
        body = bez((0, 15), (-7, 15), (-12, 6), (-12, -4)) + bez((-12, -4), (-12, -14), (-6, -19), (0, -19)) + \
            bez((0, -19), (6, -19), (12, -14), (12, -4)) + bez((12, -4), (12, 6), (7, 15), (0, 15))[1:-1]
        form(body, HIP, sdx=-3, sdy=3, sh=0.16)
        glint(-5, 3, 2.6, 5.5, 10)
        for k in range(5):
            a = math.radians(-90 + (k-2)*30)
            stroke([(0, -18), (math.cos(a)*7, -18+math.sin(a)*6 - 1)], W*1.1, g=TWIG_DARK)
        shape(ell(0, -18.5, 3.2, 1.7, 10), TWIG_DARK, W*0.6)


def sipek(b):
    twig = bez((4, 84), (34, 98), (80, 100), (116, 88))
    pinnate((30, 94), 150, 1, 12, 7.5, (LEAF_YELLOW, LEAF))
    pinnate((90, 96), 30, 1, 12, 7.5, (LEAF, LEAF_ORANGE))
    tube(bez((58, 98), (58, 90), (60, 78), (60, 68)), 4, 3, TWIG, sh=0)
    hips = ((31, 44, -40), (60, 34, 0), (89, 44, 40))
    for hx, hy, rot in hips:
        a = math.radians(rot - 90)
        stroke(bez((60, 68), (60, 60), (hx - math.cos(a)*24, hy - math.sin(a)*24), (hx - math.cos(a)*14, hy - math.sin(a)*14)), W*1.4, g=TWIG)
    tube(twig, 6, 3.5, TWIG, sh=0.12)
    P = resample(twig, 2)
    for i in range(6, len(P)-4, 9):
        x, y = P[i]
        thorn(x, y+2.5, 150 - i*0.9, 6)
    for hx, hy, rot in hips:
        hip(hx, hy, rot)


def jerabina(b):
    pinnate((56, 92), 172, 4, 14, 6, (LEAF, LEAF_YELLOW, LEAF_ORANGE))
    pinnate((64, 92), 8, 4, 14, 6, (LEAF_ORANGE, LEAF, LEAF_YELLOW))
    dome = mirror(bez((CX-44, 50), (CX-44, 30), (CX-26, 12), (CX, 12)), CX) + bez((CX+44, 50), (CX+30, 64), (CX-30, 64), (CX-44, 50))[1:-1]
    pos = scatter(dome, 40, 4, margin=4, mind=11.2)
    for x, y in pos:
        stroke(bez((60, 90), (60, 78), (x*0.6+24, y*0.5+40), (x, y+4)), W*0.8, g=TWIG)
    tube(bez((60, 90), (60, 96), (58, 104), (54, 114)), 3.5, 3, TWIG, sh=0)
    for x, y in sorted(pos, key=lambda p: -p[1]):
        shiny(x, y, 6.6, ROWAN, sh=0.16)
        for k in range(5):
            a = math.radians(-90 + k*72)
            stroke([(x+0.6, y-3.5), (x+0.6+math.cos(a)*1.2, y-3.5+math.sin(a)*1.0)], W*0.55, g=TWIG_DARK)


def trnka(b):
    twig = bez((4, 36), (40, 60), (76, 86), (116, 104))
    spur = bez((52, 68), (64, 60), (78, 48), (96, 42))
    for (bx, by), (ex, ey) in (((24, 49), (18, 78)), ((70, 82), (66, 110)), ((96, 42), (114, 34)), ((96, 96), (106, 76))):
        tube([(bx, by), (ex, ey)], 3.2, 1.0, TWIG_DARK, sh=0)
    leaf((40, 60), (22, 96), 14, LEAF_YELLOW, vein=LEAF_VEIN, serr=0.5, veins=3)
    leaf((86, 91), (70, 116), 12, LEAF, vein=LEAF_VEIN, serr=0.5, veins=3)
    berries = ((36, 34, 13, (38, 56)), (60, 50, 12, (58, 70)), (80, 26, 13, (78, 49)), (104, 72, 12, (100, 96)), (58, 20, 11.5, (66, 60)))
    for x, y, r, (ax, ay) in berries:
        stroke(bez((ax, ay), (ax, ay-4), (x, y+r+4), (x, y+r-2)), W*1.3, g=TWIG_DARK)
    tube(spur, 4, 2.5, TWIG_DARK, sh=0.1)
    tube(twig, 5.5, 3.5, TWIG_DARK, sh=0.1)
    berries = [(x, y, r) for x, y, r, _ in berries]
    for x, y, r in sorted(berries, key=lambda p: -p[1]):
        e = shiny(x, y, r, SLOE, sh=0.2, hl=False)
        with clip(e):
            fill(ell(x-r*0.35, y+r*0.3, r*0.75, r*0.6, 20), BLOOM)
        stroke(e, W, closed=True)
        glint(x-r*0.4, y+r*0.45, r*0.18, r*0.1, 40)
        stroke([(x+r*0.2, y-r*0.9), (x+r*0.35, y-r*0.2)], W*0.5, g=BLOOM)


def brusinka(b):
    for stem, n, s0 in ((bez((34, 8), (30, 40), (34, 70), (48, 100)), 11, 1), (bez((40, 8), (48, 30), (62, 44), (78, 52)), 6, -1)):
        tube(stem, 3.4, 2.4, TWIG, sh=0)
        P = resample(stem, 2)
        for j in range(n):
            i = int(4 + j*(len(P)-6)/n)
            x, y = P[i]
            s = s0 if j % 2 else -s0
            (ax, ay), (bx, by) = P[i-1], P[i+1]
            base = math.atan2(by-ay, bx-ax)
            a = base + s*math.radians(58)
            l = 19
            leaf((x, y), (x+math.cos(a)*l, y+math.sin(a)*l), 11, LINGON_LEAF, vein=LEAF_VEIN, veins=0, bulge=0.5)
            glint(x+math.cos(a)*l*0.5 - 1.5, y+math.sin(a)*l*0.5 + 1.5, 2.6, 0.9, math.degrees(a))
    berries = ((70, 96), (82, 102), (94, 94), (78, 84), (92, 80), (104, 84), (86, 68), (100, 66))
    tube(bez((48, 100), (60, 108), (76, 110), (86, 104)), 2.2, 1.8, TWIG, sh=0)
    for x, y in berries:
        stroke(bez((86, 104), (86, 100), (x, y+10), (x, y+4)), W*0.8, g=TWIG)
    for x, y in sorted(berries, key=lambda p: -p[1]):
        shiny(x, y, 8.4, LINGON, sh=0.18)
        dot(x+0.5, y-6.6, 1.0, TWIG_DARK)


def boruvka(b):
    main = bez((56, 6), (56, 36), (48, 60), (30, 100))
    side = bez((55, 40), (66, 56), (82, 72), (98, 104))
    for s in (main, side):
        tube(s, 3.2, 2.2, BILBERRY_STEM, sh=0.1)
    for s, idx in ((main, (8, 14, 20, 26, 32)), (side, (6, 12, 18, 24))):
        P = resample(s, 2)
        for j, i in enumerate(idx):
            x, y = P[min(i, len(P)-1)]
            sgn = 1 if j % 2 else -1
            a = math.radians(90 + sgn*60 + (15 if s is side else -15))
            col = (LEAF, LEAF_RED, LEAF, LEAF_ORANGE, LEAF)[j]
            leaf((x, y), (x+math.cos(a)*16, y+math.sin(a)*16), 10, col, vein=LEAF_VEIN, serr=0.45, teeth=10, veins=2, bulge=0.45)
    for x, y, r, ax, ay in ((34, 44, 9, 50, 54), (58, 22, 9.5, 56, 34), (82, 42, 9, 70, 58), (100, 70, 8, 88, 82)):
        stroke(bez((ax, ay), (ax, ay-4), (x, y+r+4), (x, y+r-1)), W*0.9, g=BILBERRY_STEM)
        e = shiny(x, y, r, BILBERRY, sh=0.2, hl=False)
        with clip(e):
            fill(ell(x-r*0.3, y+r*0.3, r*0.8, r*0.7, 20), BLOOM)
        stroke(e, W, closed=True)
        shape(ell(x+r*0.1, y-r*0.55, r*0.32, r*0.2, 12), BILBERRY, W*0.7)
        glint(x-r*0.4, y+r*0.4, r*0.2, r*0.11, 40)


def drupe(x, y, rx, ry, g, hi, rot=0):
    with T(x, y, 1, rot=rot):
        e = ell(0, 0, rx, ry, 24)
        form(e, g, sdx=-2, sdy=2, sh=0.18)
        rr = random.Random(int(rx*10))
        for row in range(-3, 4):
            yy = row*ry*0.28
            half = rx*math.sqrt(max(0, 1-(yy/ry)**2))
            n = max(1, int(half*2/5.2))
            for k in range(n):
                xx = -half + 2*half*(k+0.5)/n + (1.3 if row % 2 else 0)
                if abs(xx) < half:
                    shape(ell(xx, yy, 2.9, 2.7, 10), g, W*0.55)
                    dot(xx-0.9, yy+0.9, 0.7, hi)
        stroke(e, W, closed=True)
        for k in range(5):
            a = math.radians(90 + (k-2)*30)
            leaf((0, ry-1), (math.cos(a)*7, ry-1+math.sin(a)*5), 2.8, LEAF, w=W*0.6, sh=0)


def ostruzina(b):
    cane = bez((4, 70), (30, 98), (80, 108), (116, 96))
    for ang, col in ((-105, LEAF), (-140, LEAF_RED), (-70, LEAF)):
        a = math.radians(ang)
        leaf((30, 88), (30+math.cos(a)*34, 88+math.sin(a)*30), 19, col, vein=LEAF_VEIN, serr=0.9, teeth=12, veins=4)
    stroke(bez((30, 88), (30, 92), (32, 95), (34, 96)), W*1.2, g=TWIG)
    fr = ((58, 40, 13, 16, BLACKBERRY, BLACKBERRY_HI, -8), (86, 34, 13, 16, BLACKBERRY, BLACKBERRY_HI, 6),
          (100, 64, 10, 13, RASP_RED, SHINE, 14), (72, 66, 7, 9, UNRIPE, WHITE, 0))
    for x, y, rx, ry, *_ in fr:
        stroke(bez((80, 106), (80, 92), (x, y+ry+14), (x, y+ry)), W*1.2, g=TWIG)
    tube(cane, 5, 3.5, Col(0.45, "#8a3b3f"), sh=0.12)
    P = resample(cane, 2)
    for i in range(4, len(P)-4, 7):
        x, y = P[i]
        thorn(x, y+2, 100 + (i % 3)*20, 4.5)
    for x, y, rx, ry, g, hi, rot in sorted(fr, key=lambda p: -p[1]):
        drupe(x, y, rx, ry, g, hi, rot)


def acorn(x, y, rot, g):
    with T(x, y, 1, rot=rot):
        nut = bez((-11, 8), (-12, -8), (-6, -22), (0, -25)) + bez((0, -25), (6, -22), (12, -8), (11, 8))
        form(nut, g, sdx=-3, sdy=2, sh=0.16)
        stroke([(0, -25), (0.4, -28)], W*1.6)
        glint(-5.5, -6, 1.8, 6)
        c = ell(0, 8, 13.5, 10, 30, 180, 360) + bez((13.5, 8), (13, 13), (7, 16), (0, 16)) + bez((0, 16), (-7, 16), (-13, 13), (-13.5, 8))[1:]
        form(c, CUP, sdx=-3, sdy=1.5, sh=0.16)
        with clip(c):
            for row in range(5):
                yy = 14 - row*4
                for k in range(-4, 5):
                    xx = k*3.4 + (1.7 if row % 2 else 0)
                    stroke(ell(xx, yy, 1.7, 1.6, 8, 180, 360), W*0.55, g=CUP_SCALE)
        stroke(c, W, closed=True)


def zalud(b):
    leaf((104, 114), (10, 22), 58, OAK, vein=LEAF_VEIN, lobes=4.5, bulge=0.62, veins=5)
    with T(60, 60, 1.25):
        stroke(bez((0, 30), (0, 20), (-10, 10), (-12, 9)), W*1.6, g=TWIG)
        stroke(bez((0, 26), (2, 18), (10, 8), (14, 6)), W*1.6, g=TWIG)
        tube([(0, 40), (0, 26)], 3.4, 3, TWIG, sh=0)
        acorn(-13, -6, 12, ACORN)
        acorn(15, -9, -14, ACORN_GREEN)


def bukvice(b):
    leaf((64, 70), (112, 114), 34, BEECH, vein=BEECH_VEIN, serr=0.6, teeth=7, veins=6, bulge=0.45)
    rr = random.Random(5)
    base = (60, 24)

    def valve(tip, wd, face, hairs):
        out = blade(base, tip, wd, 0.6)
        c = ((base[0]+tip[0])/2, (base[1]+tip[1])/2)
        for i in range(2, len(out), 2):
            px, py = out[i]
            if math.hypot(px-base[0], py-base[1]) < 6: continue
            ox, oy = px - c[0], py - c[1]; d = math.hypot(ox, oy) or 1
            stroke([(px, py), (px+ox/d*3.4+rr.uniform(-1, 1), py+oy/d*3.4+rr.uniform(-1, 1))], W*0.6, g=CUP_SCALE)
        form(out, face, sdx=-2, sdy=1.5, sh=0.14)
        if hairs:
            with clip(out):
                for px, py in scatter(out, 30, int(tip[0]), margin=1, mind=3):
                    stroke([(px, py), (px+rr.uniform(-1.5, 1.5), py+2.2)], W*0.5, g=CUP_SCALE)
    valve((32, 84), 22, HUSK_IN, False)
    valve((88, 84), 22, HUSK_IN, False)
    for tx, ty, lean in ((47, 90, -1), (73, 90, 1)):
        bx, by = 60 + lean*3, 26
        h = ty - by
        lft = [(bx, by), (tx - 11, by + h*0.32), (tx, ty)]
        rgt = [(bx, by), (tx, ty), (tx + 11, by + h*0.32)]
        shape(lft, BEECHNUT_LIT if lean < 0 else BEECHNUT)
        shape(rgt, BEECHNUT if lean < 0 else BEECHNUT_LIT)
        glint(tx - lean*2 - 3, by + h*0.55, 1.2, 5, -8*lean)
    valve((10, 46), 24, HUSK, True)
    valve((110, 46), 24, HUSK, True)
    tube([(60, 8), (60, 26)], 6, 6, HUSK, sh=0.12)


def walnut(x, y, s, rot=0):
    with T(x, y, s, rot=rot):
        nut = bez((0, -26), (-18, -26), (-22, -8), (-22, 0)) + bez((-22, 0), (-22, 16), (-12, 26), (0, 28)) + \
            bez((0, 28), (12, 26), (22, 16), (22, 0)) + bez((22, 0), (22, -8), (18, -26), (0, -26))[1:-1]
        form(nut, WALNUT, sdx=-4, sdy=3, sh=0.15)
        rr = random.Random(int(x))
        with clip(nut):
            for k in range(14):
                sx = -1 if k % 2 else 1
                y0 = -22 + k*3.3
                x0 = sx*rr.uniform(3, 6)
                stroke(bez((x0, y0), (x0+sx*6, y0+rr.uniform(-4, 4)), (x0+sx*10, y0+rr.uniform(-4, 4)), (x0+sx*rr.uniform(14, 20), y0+rr.uniform(-3, 3))), W*0.6, g=WALNUT_LINE)
        stroke(bez((0, -25), (-1.5, -8), (-1.5, 10), (0, 29)), W*1.5)
        stroke([(0, 28), (0, 31)], W*1.4)


def orech(b):
    husk = ell(50, 56, 38, 40, 40)
    form(husk, WALNUT_HUSK, sdx=-5, sdy=4, sh=0.16)
    for x, y in scatter(husk, 40, 3, margin=2, mind=4):
        dot(x, y, 0.8, GRASS)
    hole = [(50+math.cos(a)*30*(1+0.06*math.sin(a*9)), 54+math.sin(a)*32*(1+0.05*math.sin(a*7))) for a in [i*math.pi/24 for i in range(48)]]
    shape(hole, WALNUT_HUSK_IN)
    walnut(52, 54, 0.95)
    tube([(56, 95), (60, 106)], 4, 3, TWIG, sh=0)
    walnut(92, 29, 0.72, rot=-20)


def jablko(b):
    pts = []
    for i in range(72):
        a = math.radians(i*5)
        rx, ry = 42, 38
        x, y = math.cos(a)*rx, math.sin(a)*ry
        y -= 9*math.exp(-((a-math.pi/2)/0.28)**2)
        y += 4*math.exp(-((a-3*math.pi/2)/0.3)**2)
        x *= 1 - 0.08*math.sin(a)
        pts.append((CX+x, 50+y))
    stem = bez((CX, 78), (CX, 88), (CX+2, 96), (CX+6, 102))
    form(pts, APPLE, sdx=-6, sdy=5, sh=0.14)
    with clip(pts):
        for k in range(4):
            fill(ell(CX+20+k*4, 50-k, 44-k*8, 40-k*6, 30), APPLE_BLUSH)
        for k in range(10):
            x0 = CX-22 + k*6.5
            stroke(bez((x0, 86), (x0+k*0.8, 70), (x0+k*1.2, 40), (x0+k*0.4, 14)), W*1.2, g=APPLE_RED)
        rr = random.Random(1)
        for _ in range(40):
            dot(CX + rr.uniform(-38, 38), 50 + rr.uniform(-34, 30), 0.7, APPLE)
        fill(ell(CX-22, 64, 7, 11, 20, rot=30), SHINE)
    stroke(pts, W, closed=True)
    stroke(bez((CX-10, 81), (CX-4, 77), (CX+4, 77), (CX+10, 81)), W*0.8)
    tube(stem, 3.2, 2.6, TWIG, sh=0)
    leaf((CX+5, 99), (CX+44, 108), 17, LEAF, vein=LEAF_VEIN, serr=0.5, veins=4)


def spiky(pts, g, c, every=5, l=5, skip=0):
    P = resample(pts, 1.5)
    for i in range(2, len(P)-2, every):
        (ax, ay), (bx, by) = P[i-1], P[i+1]
        x, y = P[i]
        if math.hypot(x-c[0], y-c[1]) < skip: continue
        d = math.hypot(bx-ax, by-ay) or 1
        nx, ny = (by-ay)/d, -(bx-ax)/d
        if nx*(x-c[0]) + ny*(y-c[1]) < 0: nx, ny = -nx, -ny
        shape([(x-(bx-ax)/d*1.8, y-(by-ay)/d*1.8), (x+nx*l, y+ny*l), (x+(bx-ax)/d*1.8, y+(by-ay)/d*1.8)], g, W*0.7)


def conker(x, y, r, rot=0, hil=(0.45, -0.3)):
    with T(x, y, 1, rot=rot):
        e = [(math.cos(a)*r*(1+0.04*math.sin(a*2)), math.sin(a)*r*0.92) for a in [i*math.pi/20 for i in range(40)]]
        form(e, CONKER, sdx=-r*0.25, sdy=r*0.2, sh=0.2)
        with clip(e):
            for k in range(3):
                stroke(ell(-r*0.15, r*0.05, r*(0.35+k*0.2), r*(0.25+k*0.16), 20, 100, 230, rot=-20), W*0.9, g=CONKER_LIT)
            shape(ell(r*hil[0]*1.6, r*hil[1]*1.6, r*0.55, r*0.42, 20, rot=-30), HILUM, W*0.7)
        stroke(e, W, closed=True)
        glint(-r*0.4, r*0.4, r*0.22, r*0.1, 40)


def kastan(b):
    c = (52, 58)
    for ang, L in ((150, 46), (35, 46), (262, 44)):
        a = math.radians(ang)
        tip = (c[0]+math.cos(a)*L, c[1]+math.sin(a)*L)
        out = blade(c, tip, 38, 0.55)
        mid = (c[0]+math.cos(a)*L*0.5, c[1]+math.sin(a)*L*0.5)
        spiky(out, CHEST_SHELL, mid, every=7, l=6.5, skip=0)
        form(out, CHEST_SHELL, sdx=-3, sdy=2, sh=0.14)
        shape(blade((c[0]+math.cos(a)*4, c[1]+math.sin(a)*4), (c[0]+math.cos(a)*(L-6), c[1]+math.sin(a)*(L-6)), 27, 0.55), CHEST_LINING, W*0.6)
    conker(c[0], c[1]+2, 26, hil=(0.2, 0.25))
    conker(100, 20, 13, rot=15)


def siska(b):
    with T(60, 58, 1, rot=-32):
        L = 52
        prof = lambda t: 18*math.sin(math.pi*min(1, max(0, t)))**0.5*(0.78 + 0.22*t)
        env = [(prof(i/60) + 1.5, -L + 2*L*i/60) for i in range(61)]
        env = [(-x, y) for x, y in env] + [(x, y) for x, y in reversed(env)][1:-1]
        tube([(0, L-4), (1, L+9)], 4.5, 3.4, TWIG, sh=0)
        fill(env, CONE_DARK)
        rows = 15
        with clip(env):
            for r_ in reversed(range(rows)):
                t = (r_ + 0.7)/(rows + 0.4)
                yc = L - 2*L*t
                w = prof(1 - t)
                for k in sorted(range(-3, 4), key=abs, reverse=True):
                    a = math.radians(k*26 + (13 if r_ % 2 else 0))
                    if abs(a) > math.radians(82): continue
                    xc = math.sin(a)*w
                    sw = max(2.0, 6.4*math.cos(a)**0.8*(0.4 + 0.6*w/18))
                    sh_ = 8.6
                    sc = bez((xc-sw, yc+sh_*0.9), (xc-sw*1.05, yc-sh_*0.2), (xc-sw*0.7, yc-sh_*0.8), (xc, yc-sh_*0.8)) + \
                        bez((xc, yc-sh_*0.8), (xc+sw*0.7, yc-sh_*0.8), (xc+sw*1.05, yc-sh_*0.2), (xc+sw, yc+sh_*0.9))
                    form(sc, CONE, w=W*0.75, sdx=sw*0.25, sdy=sh_*0.35, sh=0.2)
                    stroke(bez((xc-sw*0.75, yc-sh_*0.45), (xc-sw*0.35, yc-sh_*0.7), (xc+sw*0.35, yc-sh_*0.7), (xc+sw*0.75, yc-sh_*0.45)), W*0.5, g=CONE_EDGE)
            offset_shadow(env, 5, 2, 0.12)
        stroke(env, W, closed=True)

ASSETS = [(fn.__name__, 120, 120, fn, "atlas") for fn in (
    muchomurka, horcak, zelena, hrib, liska_houba, kozak, vaclavka, pychavka, klouzek, bedla, ryzec,
    sipek, jerabina, trnka, brusinka, boruvka, ostruzina, zalud, bukvice, orech, jablko, kastan, siska)]
