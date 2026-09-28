"""Fabian's Trail backgrounds for trails 4-6 (Plešivec, Šemík, Hradec), the world map and the atlas book."""
import math, random
import lib
from lib import C, G, Col, ell, bez, rrect
from style3 import *
from scenes3 import leaf, planks

SKY = Col(0.9, "#b9dcef")
SKY_LOW = Col(0.95, "#eef1e6")
CLOUD = Col(0.99, "#fdfcf6")
FAR = Col(0.8, "#a9bdd3")
FAR2 = Col(0.85, "#c3cfdb")
FAR_WOOD = Col(0.7, "#8fa58f")
MID_WOOD = Col(0.6, "#6f8f5e")

GOLD = Col(0.75, "#e9b13a")
GOLD_L = Col(0.85, "#f6d468")
COPPER = Col(0.6, "#d06d2e")
COPPER_L = Col(0.7, "#e58e45")
RUST = Col(0.5, "#b2502b")
OLIVE = Col(0.65, "#a2a646")
OLIVE_L = Col(0.75, "#c3c465")
GREENY = Col(0.6, "#7fa651")
GREENY_L = Col(0.72, "#a2c166")
SPRUCE = Col(0.4, "#3f6c4f")
SPRUCE_DK = Col(0.3, "#2d523d")
PINE = Col(0.45, "#4c7a51")
PINE_L = Col(0.55, "#669463")
PINE_BARK = Col(0.55, "#c1703f")
LARCH = Col(0.75, "#e7b640")
LARCH_DK = Col(0.6, "#c88a2a")
BARK = Col(0.45, "#7b5638")
BARK_DK = Col(0.35, "#5e3f29")
BEECH_BARK = Col(0.75, "#b9bcbd")
BEECH_FAR = Col(0.82, "#d6ccb0")
BIRCH = Col(0.95, "#f4f1e7")
WILLOW = Col(0.7, "#b4bd76")
WILLOW_L = Col(0.8, "#d3d897")

FG = Col(0.75, "#bfc36c")
FG_DK = Col(0.65, "#a2a855")
MEADOW = Col(0.75, "#c9c776")
MEADOW_DK = Col(0.65, "#aeac5c")
STUBBLE = Col(0.85, "#ead08a")
STUBBLE_DK = Col(0.7, "#cfae62")
PLOUGH = Col(0.5, "#a67552")
PLOUGH_DK = Col(0.4, "#86593c")
WINTER = Col(0.65, "#9dbb62")
ROAD = Col(0.85, "#dcd2bb")
TRACK = Col(0.8, "#d8c29a")
LITTER = Col(0.6, "#c98a45")
LITTER_DK = Col(0.5, "#a96a35")

ROCK = Col(0.7, "#a9a59c")
ROCK_L = Col(0.8, "#c6c1b5")
ROCK_DK = Col(0.55, "#86817a")
QUARRY = Col(0.7, "#b9a68b")
QUARRY_DK = Col(0.55, "#96826a")
LICHEN = Col(0.8, "#d3cf88")
EMERALD = Col(0.55, "#2aa58d")
EMERALD_L = Col(0.75, "#7fd6bd")
EMERALD_DK = Col(0.4, "#1c7c6f")
POND = Col(0.65, "#72a9c6")
POND_L = Col(0.85, "#b6d9e8")
HEATHER = Col(0.6, "#c7669a")
HEATHER_L = Col(0.75, "#e493bf")
BILBERRY = Col(0.45, "#b3402f")
MOSS = Col(0.55, "#6f9a3c")
MOSS_L = Col(0.7, "#9bc25a")
FERN = Col(0.7, "#cf9a45")

WALL = Col(0.95, "#f5efe1")
WALL_SH = Col(0.85, "#ddd3bd")
ROOF = Col(0.5, "#c4553a")
ROOF_DK = Col(0.4, "#9c3f2b")
WINDOW = Col(0.4, "#566f86")
APPLE = Col(0.5, "#d8413a")
APPLE_Y = Col(0.8, "#f0c53d")
ROSEHIP = Col(0.45, "#dc3b2a")
SLOE = Col(0.3, "#4d527e")
BERRY = Col(0.5, "#e2452f")
WOOD = Col(0.55, "#a8743f")
WOOD_DK = Col(0.4, "#744b27")
WOOD_L = Col(0.7, "#c89a61")
STONE = Col(0.8, "#cfc9bb")
STONE_DK = Col(0.65, "#aaa393")
SILVER = Col(0.9, "#e4e8ee")
CHEST = Col(0.45, "#8e5a2e")
CHEST_BAND = Col(0.55, "#6f6a60")
DUCK = Col(0.95, "#f6f3ea")
DUCK_BILL = Col(0.8, "#f0a63a")
DRAKE = Col(0.5, "#2f7a55")
SPARK = Col(0.97, "#fff6c4")
BEAM = Col(0.98, "#fff4cf", alpha=0.22)

MAP_LAND = Col(0.85, "#dcd79c")
MAP_EDGE = Col(0.6, "#a79a6a")
MAP_ROAD = Col(0.95, "#f7f0da")
MAP_TRAIL = Col(0.35, "#b0413a")
MAP_WATER = Col(0.65, "#78b3d2")
MAP_WOOD = Col(0.55, "#8a9e5c")
FOG = Col(1.0, "#f4f2ec", alpha=0.55)
FOG_HILL = Col(0.8, "#b6c3d0")

TABLE = Col(0.5, "#9c663a")
PAPER = Col(0.95, "#f7eed6")
PAPER_EDGE = Col(0.8, "#dcc79d")
PAPER_SH = Col(0.3, "#8a6a3a", alpha=0.10)
GRID = Col(0.8, "#c9b58b")
COVER = Col(0.4, "#3f6b4f")
COVER_DK = Col(0.3, "#2e5039")
RIBBON = Col(0.45, "#c63d3a")
PENCIL = Col(0.8, "#f2c14e")
PENCIL_WOOD = Col(0.85, "#f0d3a2")

W = 0.9
AUTUMN = ((GOLD, GOLD_L), (COPPER, COPPER_L), (OLIVE, OLIVE_L), (GREENY, GREENY_L), (RUST, COPPER))


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def smooth(pts, it=2, closed=True):
    for _ in range(it):
        out = []; n = len(pts)
        for i in range(n if closed else n-1):
            a = pts[i]; b = pts[(i+1) % n]
            out += [(a[0]*0.75+b[0]*0.25, a[1]*0.75+b[1]*0.25), (a[0]*0.25+b[0]*0.75, a[1]*0.25+b[1]*0.75)]
        pts = out if closed else [pts[0]] + out + [pts[-1]]
    return pts


def wave(y, amps, seed, x0=-10, x1=970, step=8):
    r = random.Random(seed); ph = [r.random()*6.28 for _ in amps]
    n = int((x1-x0)/step) + 1
    return [(x0+i*step, y+sum(a*math.sin((x0+i*step)/L*6.28+p) for (a, L), p in zip(amps, ph))) for i in range(n)]


def yat(line, x):
    for (xa, ya), (xb, yb) in zip(line, line[1:]):
        if xa <= x <= xb:
            return ya + (yb-ya)*(x-xa)/max(1e-6, xb-xa)
    return line[0][1] if x < line[0][0] else line[-1][1]


def land(top, col, w=W, bottom=-10):
    fill(top + [(top[-1][0], bottom), (top[0][0], bottom)], col)
    if w: stroke(top, w)


def clip(pts):
    C.saveState(); C.clipPath(poly(pts), stroke=0, fill=0)


def unclip():
    C.restoreState()


def inside(pt, pts):
    x, y = pt; c = False; n = len(pts)
    for i in range(n):
        (xa, ya), (xb, yb) = pts[i], pts[(i+1) % n]
        if (ya > y) != (yb > y) and x < xa + (xb-xa)*(y-ya)/(yb-ya):
            c = not c
    return c


# ------------------------------------------------------------------ sky & distance
def sky(horizon=300, top=SKY, low=SKY_LOW):
    fill(rect(0, 0, 960, 540), top)
    for i in range(24):
        fill(rect(0, 0, 960, horizon + 170 - i*8), low, 0.07)


def cloud(x, y, s=1.0, w=0.6):
    with T(x, y, s):
        pts = bez((-30, 0), (-34, 10), (-22, 15), (-16, 11)) + bez((-16, 11), (-13, 22), (5, 24), (8, 15)) + \
              bez((8, 15), (15, 22), (30, 17), (27, 6)) + bez((27, 6), (34, 3), (32, -4), (25, -4)) + [(-26, -4)] + \
              bez((-26, -4), (-33, -4), (-33, 0), (-30, 0))
        fill(pts, CLOUD)
        clip_fill(pts, [(x_, y_-5) for x_, y_ in pts], Col(0.9, "#e6edf2"))
        stroke(pts, w, closed=True)


def ridge(y, amp, col, seed, w=0.5, wl=420):
    top = wave(y, ((amp, wl), (amp*0.4, wl*0.37)), seed)
    land(top, col, w)
    return top


def bumps(y, seed, rmin, rmax, x0=-20, x1=980, jit=4, hk=0.55):
    r = random.Random(seed); pts = []; x = x0
    while x < x1:
        d = r.uniform(rmin, rmax)*2; b = y + r.uniform(-jit, jit)
        pts += ell(x+d/2, b, d/2, d*hk*r.uniform(0.8, 1.2), 8, 180, 0)
        x += d
    return pts


def woods(y, seed, col, patches=(), rmin=8, rmax=16, w=0.6, bottom=-10, jit=5, n=60, x0=-20, x1=980):
    top = bumps(y, seed, rmin, rmax, x0, x1, jit)
    pts = top + [(top[-1][0], bottom), (top[0][0], bottom)]
    fill(pts, col)
    if patches:
        r = random.Random(seed+99)
        clip(pts)
        for i in range(n):
            px = r.uniform(x0, x1); py = r.uniform(y - 40, y + rmax)
            rr = r.uniform(rmin, rmax)*1.1
            fill(blob(px, py, rr, rr*0.8, seed+i, 7, 0.2), patches[i % len(patches)])
        unclip()
    stroke(top, w)
    return top


def fields(y0, y1, seed, cols, rows=3, w=0.55, x0=-10, x1=970, base=MEADOW):
    r = random.Random(seed)
    fill(rect(x0, -10, x1, y0 + 5), base)
    ys = [y1] + [y1 - (y1-y0)*((i+1)/rows)**1.25 for i in range(rows)]
    lines = [wave(yy, ((3, 330), (1.5, 120)), seed+i) for i, yy in enumerate(ys)]
    last = None
    for i in range(rows):
        top, bot = lines[i], lines[i+1]
        xs = [x0 - 40]; sl = [0]
        while xs[-1] < x1:
            xs.append(xs[-1] + r.uniform(150, 330)*(1+i*0.35)); sl.append(r.uniform(-30, 30)*(i+1))
        for j in range(len(xs)-1):
            xa, xb = xs[j], xs[j+1]
            tp = [(xa, yat(top, xa))] + [p for p in top if xa < p[0] < xb] + [(xb, yat(top, xb))]
            ba, bb = xa + sl[j], xb + sl[j+1]
            bp = [(ba, yat(bot, ba))] + [p for p in bot if ba < p[0] < bb] + [(bb, yat(bot, bb))]
            pts = tp + list(reversed(bp))
            col = r.choice([c for c in cols if c is not last] or cols); last = col
            fill(pts, col)
            if col in (PLOUGH, STUBBLE, WINTER):
                clip(pts)
                dk = {PLOUGH: PLOUGH_DK, STUBBLE: STUBBLE_DK, WINTER: GREENY}[col]
                n = int((xb-xa)/9)
                for k in range(1, n):
                    t = k/n
                    stroke([(xa+(xb-xa)*t, yat(top, xa+(xb-xa)*t)+2), (ba+(bb-ba)*t, yat(bot, ba+(bb-ba)*t)-2)], 0.45, g=dk)
                unclip()
            stroke(pts, w, closed=True)
    return lines


def fg(y=188, col=FG, seed=1, w=W, dk=FG_DK, marks=40):
    top = wave(y, ((2.5, 260), (1.2, 90)), seed)
    land(top, col, w)
    fill(wave(y*0.42, ((3, 300),), seed+9) + [(970, -10), (-10, -10)], dk, 0.22)
    r = random.Random(seed+5)
    for _ in range(marks):
        x = r.uniform(0, 960); yy = r.uniform(8, y-12)
        k = 0.6 + 0.8*(1 - yy/y)
        stroke([(x, yy), (x+7*k, yy+0.6)], 0.5*k+0.2, g=dk)
    return top


def tuft(x, y, k=1.0, col=GREENY, w=0.6):
    pts = [(x-4*k, y), (x-3.2*k, y+5*k), (x-1.8*k, y+1.2*k), (x-0.3*k, y+8*k), (x+1.2*k, y+1.3*k),
           (x+3*k, y+5.5*k), (x+3.6*k, y+0.8*k), (x+4.2*k, y)]
    shape(pts, col, w)


def tufts(n, x0, x1, y0, y1, seed, col=GREENY, k=1.0):
    r = random.Random(seed)
    for _ in range(n):
        tuft(r.uniform(x0, x1), r.uniform(y0, y1), k*r.uniform(0.8, 1.3), col)


def leaves_on_ground(n, x0, x1, y0, y1, seed, cols=(GOLD, COPPER, RUST, GOLD_L)):
    r = random.Random(seed)
    for i in range(n):
        leaf(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(3.2, 4.8), r.uniform(0, 360), cols[i % len(cols)])


def beams(xs, top=540, bottom=150, dx=-160, wd=40):
    for x in xs:
        fill([(x, top), (x+wd, top), (x+wd*1.8+dx, bottom), (x+dx, bottom)], BEAM)


# ------------------------------------------------------------------ trees
def blob(cx, cy, rx, ry, seed, n=11, bump=0.16):
    r = random.Random(seed)
    f = [r.uniform(0.86, 1.08) for _ in range(n)]
    V = [(cx+math.cos(math.tau*i/n)*rx*f[i], cy+math.sin(math.tau*i/n)*ry*f[i]) for i in range(n)]
    pts = []
    for i in range(n):
        p0 = V[i]; p1 = V[(i+1) % n]
        am = math.tau*(i+0.5)/n; k = 1 + bump + 0.06*r.random()
        fm = (f[i] + f[(i+1) % n])/2
        m = (cx+math.cos(am)*rx*fm*k, cy+math.sin(am)*ry*fm*k)
        c1 = ((p0[0]+m[0])/2+(m[0]-cx)*0.15, (p0[1]+m[1])/2+(m[1]-cy)*0.15)
        c2 = ((p1[0]+m[0])/2+(m[0]-cx)*0.15, (p1[1]+m[1])/2+(m[1]-cy)*0.15)
        pts += bez(p0, c1, c2, p1, 6)[:-1]
    return pts


def crown(cx, cy, rx, ry, col, light, seed, w=W, n=11, curls=3):
    pts = blob(cx, cy, rx, ry, seed, n)
    fill(pts, col)
    clip_fill(pts, blob(cx-rx*0.2, cy+ry*0.24, rx*0.78, ry*0.72, seed+5, n), light)
    stroke(pts, w, closed=True)
    r = random.Random(seed+3)
    for _ in range(curls):
        ax = cx + r.uniform(-0.45, 0.5)*rx; ay = cy + r.uniform(-0.55, 0.15)*ry
        stroke(ell(ax, ay, rx*0.17, ry*0.13, 8, 200, 330), w*0.6)
    return pts


def trunk(x, y, h, w0, w1, col=BARK, lean=0, w=W, flare=0.3):
    pts = [(x-w0/2-w0*flare, y)] + bez((x-w0/2, y+w0*0.35), (x-w0/2+lean*0.3, y+h*0.45), (x-w1/2+lean*0.7, y+h*0.75), (x-w1/2+lean, y+h)) + \
          bez((x+w1/2+lean, y+h), (x+w1/2+lean*0.7, y+h*0.75), (x+w0/2+lean*0.3, y+h*0.45), (x+w0/2, y+w0*0.35)) + [(x+w0/2+w0*flare, y)]
    form(pts, col, w, sdx=-w0*0.3, sdy=0, sh=0.16)
    return pts


def dtree(x, y, s, cols, seed, h=60, tw=12, rx=45, ry=36, lean=0, w=W, bark=BARK):
    with T(x, y, s):
        trunk(0, 0, h+ry*0.3, tw, tw*0.55, bark, lean, w)
        crown(lean, h+ry*0.75, rx, ry, cols[0], cols[1], seed, w)


def spruce(x, y, h, seed=1, col=SPRUCE, dark=SPRUCE_DK, w=W, wk=0.28, bark=BARK_DK):
    r = random.Random(seed)
    n = max(4, int(h/16))
    fill(rect(x-h*0.025, y, x+h*0.025, y+h*0.14), bark); stroke(rect(x-h*0.025, y, x+h*0.025, y+h*0.14), w*0.7, closed=True)
    side = []
    for k in range(1, n+1):
        t = k/n; yb = y + h*0.12 + h*0.88*(1-t)
        ww = h*wk*t + 2
        side.append((ww*r.uniform(0.9, 1.1), yb - h*0.02))
        if k < n: side.append((ww*0.5, yb + h*0.035))
    L = [(x, y+h)] + [(x-a, b) for a, b in side] + [(x, y+h*0.1)]
    R = [(x+a*r.uniform(0.92, 1.08), b) for a, b in reversed(side)]
    pts = L + R
    fill(pts, col)
    clip_fill(pts, rect(x+h*0.02, y, x+h, y+h*1.1), dark)
    stroke(pts, w, closed=True)


def pine(x, y, h, seed=1, w=W, lean=None):
    r = random.Random(seed)
    lean = r.uniform(-0.12, 0.12)*h if lean is None else lean
    top = (x+lean, y+h*0.8)
    tube(bez((x, y), (x, y+h*0.3), (x+lean*0.6, y+h*0.6), top, 12), h*0.06, h*0.03, PINE_BARK, lw=w, sh=0.15)
    for sx in (-1, 1):
        b0 = (x+lean*0.8, y+h*0.7); b1 = (x+lean*0.8+sx*h*0.16, y+h*0.74)
        tube([b0, b1], h*0.022, h*0.015, PINE_BARK, lw=w*0.8, sh=0)
    crown(x+lean*0.8-h*0.17, y+h*0.73, h*0.13, h*0.065, PINE, PINE_L, seed+1, w, 8, 1)
    crown(x+lean*0.8+h*0.18, y+h*0.77, h*0.12, h*0.06, PINE, PINE_L, seed+2, w, 8, 1)
    crown(top[0], top[1]+h*0.06, h*0.2, h*0.1, PINE, PINE_L, seed+3, w, 9, 2)


def birch(x, y, h, seed=1, w=W, cols=(GOLD, GOLD_L), lean=None):
    r = random.Random(seed)
    lean = r.uniform(-0.1, 0.1)*h if lean is None else lean
    spine = bez((x, y), (x, y+h*0.35), (x+lean*0.7, y+h*0.6), (x+lean, y+h*0.92), 14)
    at = lambda t: spine[min(14, int(t*14))]
    blobs = []
    for k in range(6):
        t = 0.5 + 0.09*k; px, py = at(t)
        sd = -1 if k % 2 else 1
        blobs.append((px + sd*h*r.uniform(0.05, 0.1), py + h*0.04, h*(0.13 - 0.012*k), h*(0.085 - 0.006*k), k))
    for bx, by, rx, ry, k in blobs[::2]:
        crown(bx, by, rx, ry, cols[0], cols[1], seed*5+k, w, 9, 0)
    tube(spine, h*0.045, h*0.022, BIRCH, lw=w, sh=0.12)
    for i in range(2, 13):
        px, py = spine[i]; ww = h*0.045*(1 - i/16)
        stroke([(px-ww*0.5, py+r.uniform(-1, 1)), (px+ww*r.uniform(-0.1, 0.4), py+r.uniform(-1, 1))], w*1.3)
    for bx, by, rx, ry, k in blobs[1::2]:
        crown(bx, by, rx*0.85, ry*0.85, cols[0], cols[1], seed*5+k, w, 9, 0)


def willow(x, y, s=1.0, seed=1, w=W):
    with T(x, y, s):
        pts = [(-14, 0), (14, 0)] + bez((14, 0), (10, 14), (12, 26), (16, 34)) + bez((-15, 34), (-11, 24), (-11, 12), (-14, 0))
        form(pts, BARK, w, sdx=-5, sdy=0, sh=0.16)
        r = random.Random(seed)
        for i in range(9):
            a = math.radians(40 + i*12.5)
            stroke(bez((0, 32), (math.cos(a)*14, 32+math.sin(a)*20), (math.cos(a)*30, 32+math.sin(a)*40), (math.cos(a)*38, 30+math.sin(a)*52), 8), w*0.9, g=BARK_DK)
        c = crown(0, 68, 44, 34, WILLOW, WILLOW_L, seed, w, 12, 2)
        clip(c)
        for i in range(14):
            xx = r.uniform(-40, 40); yy = r.uniform(40, 80)
            stroke([(xx, yy), (xx+1, yy-12)], w*0.5, g=OLIVE)
        unclip()


def oak_crown(x, y, lobes, w=W):
    for (dx, dy, rx, ry, ci, sd) in lobes:
        crown(x+dx, y+dy, rx, ry, AUTUMN[ci][0], AUTUMN[ci][1], sd, w, 10, 2)


def bush(x, y, wd, ht, cols, seed, w=W, dots=None, n=10):
    pts = blob(x, y+ht*0.45, wd/2, ht*0.55, seed, 10, 0.2)
    pts = [(px, max(py, y)) for px, py in pts]
    fill(pts, cols[0])
    clip_fill(pts, blob(x-wd*0.1, y+ht*0.62, wd*0.42, ht*0.42, seed+2, 10), cols[1])
    stroke(pts, w, closed=True)
    if dots:
        r = random.Random(seed+1)
        for i in range(n):
            px = x + r.uniform(-0.38, 0.38)*wd; py = y + r.uniform(0.2, 0.85)*ht
            d = dots[i % len(dots)]
            dot(px, py, 2.1, 0.0); dot(px, py, 1.5, d); dot(px-0.5, py+0.5, 0.45, 1.0)


# ------------------------------------------------------------------ rocks
def boulder(x, y, wd, ht, seed=1, col=ROCK, w=W, lichen=True):
    r = random.Random(seed); n = 8
    pts = [(x-wd/2, y)]
    for i in range(1, n):
        a = math.pi*(1 - i/n)
        pts.append((x+math.cos(a)*wd/2*r.uniform(0.85, 1.05), y+math.sin(a)*ht*r.uniform(0.75, 1.05)))
    pts.append((x+wd/2, y))
    pts = smooth(pts, 2)
    pts = [(px, max(py, y)) for px, py in pts]
    form(pts, col, w, sdx=-wd*0.16, sdy=ht*0.14, sh=0.2)
    cx = x + r.uniform(-0.2, 0.2)*wd
    stroke([(cx, y+ht*0.85), (cx+wd*0.05, y+ht*0.6), (cx-wd*0.02, y+ht*0.45)], w*0.6)
    if lichen:
        for _ in range(3):
            dot(x + r.uniform(-0.3, 0.2)*wd, y + r.uniform(0.4, 0.8)*ht, r.uniform(1.2, 2.4), LICHEN)
    return pts


def slab(x, y, wd, ht, seed=1, col=ROCK, w=W, sh=0.2):
    r = random.Random(seed)
    j = lambda: r.uniform(-0.06, 0.06)
    pts = [(x-wd/2*(1+j()), y), (x+wd/2*(1+j()), y+ht*j()), (x+wd/2*(1+j()), y+ht*(0.5+j())), (x+wd/2*(0.9+j()), y+ht),
           (x+wd*j(), y+ht*(1.05+j())), (x-wd/2*(0.92+j()), y+ht*(0.98+j())), (x-wd/2*(1.02+j()), y+ht*(0.5+j()))]
    pts = smooth(pts, 2)
    form(pts, col, w, sdx=-wd*0.12, sdy=ht*0.1, sh=sh)
    return pts


def moss_cap(pts, dy=10, seed=1):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    top = max(ys)
    cap = [(px, py) for px, py in pts if py > top - dy]
    if len(cap) < 3: return
    clip(pts)
    r = random.Random(seed)
    lo = wave(top-dy, ((2, 20),), seed, min(xs), max(xs), 4)
    fill(lo + [(max(xs), top+5), (min(xs), top+5)], MOSS)
    fill([(px, py+2) for px, py in lo] + [(max(xs), top+5), (min(xs), top+5)], MOSS_L)
    unclip()
    stroke(lo, 0.5, g=Col(0.35, "#4a6e2a"))


def heather(x, y, wd, seed=1, w=0.6):
    r = random.Random(seed)
    n = int(wd/6)
    for i in range(n):
        px = x - wd/2 + wd*(i+0.5)/n + r.uniform(-2, 2)
        ht = r.uniform(7, 13)
        stroke([(px, y), (px+r.uniform(-2, 2), y+ht)], 0.6, g=Col(0.4, "#6e5a3a"))
        for k in range(4):
            dot(px + r.uniform(-1.8, 1.8), y + ht*0.45 + k*ht*0.16, r.uniform(1.4, 2.1), HEATHER if k % 2 else HEATHER_L)
    base = bez((x-wd/2, y), (x-wd/2+3, y+6), (x+wd/2-3, y+6), (x+wd/2, y))
    fill(base + [(x-wd/2, y)], Col(0.5, "#7d8a45"))
    stroke(base, w*0.8)


def fern(x, y, s=1.0, flip=False, col=FERN):
    with T(x, y, s, flip):
        spine = bez((0, 0), (4, 14), (14, 26), (28, 30), 12)
        for i in range(2, 12):
            px, py = spine[i]; k = 1 - i/13
            for sd in (1, -1):
                tip = (px - sd*6*k + 3, py + sd*7*k + 2)
                shape([(px, py), ((px+tip[0])/2 - 1, (py+tip[1])/2 + 1.5*sd), tip, ((px+tip[0])/2 + 1.5, (py+tip[1])/2 - 0.5*sd)], col, 0.45)
        stroke(spine, 0.7)


# ------------------------------------------------------------------ buildings & props
def cottage(x, y, s=1.0, roof=ROOF, flip=False, w=W, chimney=True):
    with T(x, y, s, flip):
        gable = [(-20, 0), (20, 0), (20, 26), (0, 46), (-20, 26)]
        side = [(20, 0), (66, 0), (66, 26), (20, 26)]
        shape(side, WALL_SH, w); shape(gable, WALL, w)
        rf = [(0, 47), (46, 47), (69, 23), (22, 23)]
        shape(rf, roof, w)
        clip(rf)
        for k in range(1, 5): stroke([(-5, 23+k*5), (80, 23+k*5)], w*0.45)
        unclip()
        stroke([(-22, 23.5), (0, 47.5), (22, 23.5)], w*2.6, g=ROOF_DK); stroke([(-22, 23.5), (0, 47.5), (22, 23.5)], w)
        if chimney:
            shape(rect(34, 38, 40, 54), Col(0.6, "#b0634a"), w)
        for wx in (-12, 5):
            shape(rect(wx, 9, wx+7, 18), WINDOW, w*0.8)
            stroke([(wx+3.5, 9), (wx+3.5, 18)], w*0.5, g=1.0)
        shape(rect(-4, 29, 4, 36), WINDOW, w*0.7)
        shape(rect(28, 0, 37, 17), WOOD, w*0.8)
        for wx in (44, 55):
            shape(rect(wx, 9, wx+7, 18), WINDOW, w*0.8)


def church(x, y, s=1.0, w=W):
    with T(x, y, s):
        shape(rect(0, 0, 70, 34), WALL_SH, w)
        shape([(-2, 32), (72, 32), (60, 52), (8, 52)], ROOF, w)
        for wx in (22, 40, 58):
            shape(ell(wx, 18, 3.5, 8, 14), WINDOW, w*0.7)
        tw = rect(-20, 0, 6, 70)
        shape(tw, WALL, w)
        shape(ell(-7, 50, 4, 6, 14), WINDOW, w*0.7)
        shape(rect(-12, 0, -2, 20) + [], WOOD, w*0.8)
        onion = bez((-22, 70), (-24, 78), (-14, 80), (-12, 86)) + bez((-12, 86), (-8, 88), (-8, 94), (-7, 104)) + \
                bez((-7, 104), (-6, 94), (-6, 88), (-2, 86)) + bez((-2, 86), (0, 80), (10, 78), (8, 70))
        shape(onion, Col(0.4, "#4f7a6a"), w)
        stroke([(-7, 104), (-7, 114)], w); stroke([(-11, 110), (-3, 110)], w)


def post_fence(x0, x1, y, h=16, step=16, w=W):
    for yy in (y+h*0.35, y+h*0.75):
        shape(rect(x0-4, yy, x1+4, yy+2.6), WOOD_L, w*0.7)
    x = x0
    while x <= x1:
        shape(rect(x-2, y, x+2, y+h+2), WOOD, w*0.7)
        x += step


def bench(x, y, s=1.0, w=W):
    with T(x, y, s):
        for lx in (-22, 22):
            shape(rect(lx-2, 0, lx+2, 14), WOOD_DK, w)
            shape(rect(lx-1.5, 14, lx+1.5, 30), WOOD_DK, w)
        shape(rect(-30, 13, 30, 17), WOOD, w)
        shape(rect(-30, 22, 30, 26), WOOD, w)
        shape(rect(-30, 27, 30, 31), WOOD, w)


def sign(x, y, s=1.0, w=W, board=WOOD_L):
    with T(x, y, s):
        shape(rect(-2, 0, 2, 30), WOOD_DK, w)
        form(rrect(-15, 24, 30, 18, 2), board, w, sdx=-2, sdy=0, sh=0.12)
        for k in range(3):
            stroke([(-10, 29+k*4.5), (10 - 6*(k == 2), 29+k*4.5)], 0.6, g=WOOD_DK)


def chest(x, y, s=1.0, w=W, open_=True):
    with T(x, y, s):
        base = rrect(-22, 0, 44, 22, 3)
        form(base, CHEST, w, sdx=0, sdy=-3, sh=0.15)
        for i in range(8):
            shape(ell(-15+i*4.3, 23+(i % 3)*1.5, 3.4, 3.4, 12), SILVER, 0.6)
        lid = [(-23, 22), (21, 22), (27, 38), (-17, 40)] if open_ else [(-22, 22)] + bez((-22, 22), (-22, 36), (22, 36), (22, 22))
        shape(lid, Col(0.35, "#744624"), w)
        for bx in (-14, 14):
            shape(rect(bx-2.5, 0, bx+2.5, 22), CHEST_BAND, w*0.7)
        shape(rrect(-4, 12, 8, 9, 1.5), CHEST_BAND, w*0.7)
        dot(0, 16, 1.1, 0.0)


def duck(x, y, s=1.0, drake=False, flip=False, w=0.8):
    with T(x, y, s, flip):
        body = bez((-12, 0), (-14, 8), (-6, 10), (4, 8)) + bez((4, 8), (10, 8), (12, 4), (12, 0))
        shape(body + [(-12, 0)], Col(0.7, "#b58a5c") if drake else DUCK, w)
        shape(ell(8, 14, 4.6, 4.6, 14), DRAKE if drake else DUCK, w)
        shape([(12, 15), (18, 13.5), (12, 11.5)], DUCK_BILL, w*0.7)
        dot(9.5, 15.5, 0.8, 0.0)
        stroke(bez((-8, 5), (-4, 8), (0, 7), (3, 4)), w*0.6)
        stroke([(-16, -0.5), (16, -0.5)], w*0.6, g=POND_L)


def horse_head(x, y, s=1.0, col=STONE, w=W):
    pts = [(12, -22), (13, -8), (11, 4), (7, 13), (6, 15), (8, 23), (3, 17), (0, 16), (-6, 11), (-14, -1), (-17, -6),
           (-16, -10), (-12, -11), (-9, -9), (-5, -8), (0, -6), (3, -9), (2, -15), (0, -22)]
    with T(x, y, s):
        p = smooth(pts, 1)
        form(p, col, w, sdx=-1.5, sdy=1.2, sh=0.18)
        dot(-5, 6, 1.1, 0.0); dot(-14, -5, 0.8, 0.0)
        for k in range(4):
            stroke(bez((12-k*0.5, 8-k*7), (9-k*0.5, 7-k*7), (8-k*0.4, 3-k*7), (9-k*0.3, -1-k*7), 6), w*0.6)
        stroke(bez((-11, -9), (-9, -12), (-4, -8), (0, -10), 6), w*0.5)


def palisade(x0, x1, y, h, seed=1, w=W, gap=None):
    r = random.Random(seed); x = x0
    while x < x1:
        lw = r.uniform(11, 14)
        if gap and gap[0] < x + lw/2 < gap[1]:
            x += lw; continue
        hh = h*r.uniform(0.94, 1.04)
        pts = [(x, y), (x+lw, y), (x+lw, y+hh), (x+lw/2, y+hh+lw*0.9), (x, y+hh)]
        form(pts, WOOD_L if r.random() < 0.5 else WOOD, w, sdx=-lw*0.35, sdy=0, sh=0.16)
        stroke([(x+lw*0.4, y+hh*0.2), (x+lw*0.45, y+hh*0.5)], w*0.45)
        x += lw
    shape(rect(x0-2, y+h*0.62, x1+2, y+h*0.62+5), WOOD_DK, w*0.8)


def crag(x, y, wd, ht, seed=1, col=ROCK, w=W, n=4, moss=False):
    r = random.Random(seed)
    ws = [r.uniform(0.7, 1.3) for _ in range(n)]
    tot = sum(ws); xx = x - wd/2; blocks = []
    for i, k in enumerate(ws):
        bw = wd*k/tot
        mid = 1 - abs((i + 0.5)/n - 0.5)*1.2
        blocks.append((xx + bw/2, bw*1.12, ht*mid*r.uniform(0.75, 1.05)))
        xx += bw
    tops = []
    for i in sorted(range(n), key=lambda i: blocks[i][2]):
        bx, bw, bh = blocks[i]
        p = slab(bx, y, bw, bh, seed*7 + i, col if i % 2 else ROCK_L if col is ROCK else col, w, 0.22)
        clip(p)
        for k in range(1, int(bh/26) + 1):
            cy = y + k*26 + r.uniform(-5, 5)
            stroke([(bx - bw*0.6, cy), (bx + bw*0.1, cy + r.uniform(-3, 3)), (bx + bw*0.6, cy + r.uniform(-4, 2))], w*0.55)
        unclip()
        if moss: moss_cap(p, min(14, bh*0.2), seed + i)
        tops.append((bx, y + bh))
    return tops


def oak(x, y, s=1.0, seed=1, pal=(2, 1, 0, 4), w=W, bark=BARK_DK):
    r = random.Random(seed)
    col = lambda: AUTUMN[pal[r.randrange(len(pal))]]
    with T(x, y, s):
        for (dx, dy, rx, ry) in ((-40, 172, 58, 40), (42, 176, 58, 40), (0, 200, 62, 38)):
            c = col(); crown(dx, dy, rx, ry, c[0], c[1], seed*11 + dx, w, 10, 2)
        trunk(0, 0, 80, 32, 20, bark, 0, w)
        for pts, w0, w1 in ((bez((-4, 72), (-20, 92), (-45, 106), (-72, 118)), 13, 5),
                            (bez((4, 72), (22, 92), (46, 106), (74, 116)), 13, 5),
                            (bez((0, 74), (-3, 100), (4, 125), (2, 150)), 12, 5)):
            tube(pts, w0, w1, bark, lw=w, sh=0.12)
        stroke(bez((-6, 10), (-4, 30), (-8, 48), (-5, 64)), w*0.6)
        for (dx, dy, rx, ry) in ((-86, 128, 44, 30), (88, 126, 46, 30), (-30, 150, 36, 24), (34, 150, 36, 24)):
            c = col(); crown(dx, dy, rx, ry, c[0], c[1], seed*13 + dx, w, 10, 2)


def canopy_band(y, seed, cols, w=W, r0=45, r1=70, rows=2, calm=430):
    r = random.Random(seed)
    fill(rect(-10, y + 30, 970, 560), cols[0][0])
    for row in range(rows):
        x = -30 + r.uniform(0, 40)
        yy = y + (rows - 1 - row)*38
        while x < 1000:
            rr = r.uniform(r0, r1)
            c = cols[r.randrange(len(cols))] if x > calm else cols[0]
            crown(x, yy + r.uniform(-12, 12), rr, rr*0.62, c[0], c[1], seed + int(x), w, 11, 2)
            x += rr*r.uniform(1.2, 1.5)


def larch2(x, y, h, seed=1, w=W, col=(LARCH, GOLD_L)):
    r = random.Random(seed)
    n = max(5, int(h/12))
    side = []
    for k in range(1, n+1):
        t = k/n; yb = y + h*0.14 + h*0.86*(1-t)
        ww = h*0.2*t**0.9 + 3
        side.append((ww*r.uniform(0.8, 1.15), yb - h*0.03))
        if k < n: side.append((ww*0.62, yb + h*0.01))
    pts = [(x, y+h)] + [(x-a, b) for a, b in side] + [(x, y+h*0.12)] + [(x+a*r.uniform(0.85, 1.1), b) for a, b in reversed(side)]
    pts = smooth(pts, 1)
    tube([(x, y), (x, y+h*0.3)], h*0.035, h*0.03, BARK, lw=w*0.8, sh=0.1)
    fill(pts, col[0])
    clip(pts)
    fill(rect(x - h*0.02, y, x + h, y + h*1.1), LARCH_DK)
    for _ in range(int(h*0.5)):
        px = x + r.uniform(-0.2, 0.2)*h; py = y + r.uniform(0.15, 0.95)*h
        stroke(bez((px - 3, py + 1), (px - 1, py + 2), (px + 1, py + 2), (px + 3, py), 4), 0.8, g=col[1])
    stroke([(x, y + h*0.12), (x, y + h*0.9)], w*0.5, g=BARK)
    unclip()
    stroke(pts, w, closed=True)


def ribbon(line, wd, col, light, w=W, taper_far=None):
    n = len(line); L = []; R = []
    for i in range(n):
        a = line[max(0, i-1)]; b = line[min(n-1, i+1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; d = math.hypot(dx, dy) or 1
        k = wd(line[i]) if callable(wd) else wd
        L.append((line[i][0] - dy/d*k/2, line[i][1] + dx/d*k/2)); R.append((line[i][0] + dy/d*k/2, line[i][1] - dx/d*k/2))
    pts = L + list(reversed(R))
    fill(pts, col)
    if light: stroke([(x, y + 0.8) for x, y in line], 1.4, g=light)
    stroke(L, w); stroke(R, w)
    return pts


# ------------------------------------------------------------------ station backgrounds
def base_sky(horizon, clouds, top=SKY, low=SKY_LOW):
    sky(horizon, top, low)
    for cx, cy, s in clouds:
        cloud(cx, cy, s)


def bestin(b):
    base_sky(320, ((590, 490, 1.4), (850, 450, 1.0), (300, 420, 0.8)))
    ridge(330, 16, FAR, 3, 0.5)
    woods(300, 4, FAR_WOOD, (Col(0.75, "#b8ac6c"), Col(0.7, "#aa8f5f")), 6, 11, 0.5)
    fields(205, 292, 5, (STUBBLE, PLOUGH, WINTER, MEADOW), 3)
    for i, (hx, sc) in enumerate(((770, 0.55), (830, 0.5), (895, 0.55))):
        cottage(hx, 286 - i*2, sc, ROOF if i % 2 else ROOF_DK, i == 1, 0.6)
    dtree(745, 284, 0.45, AUTUMN[0], 31, w=0.6)
    road = wave(205, ((2, 300),), 7)
    land(road, ROAD, W)
    stroke(wave(196, ((1.5, 300),), 8, step=30)[::2], 0.4, g=Col(0.7, "#b9ac90"))
    ox, oy = 550, 212
    trunk_pts = [(ox-40, oy)] + bez((ox-26, oy+8), (ox-24, oy+40), (ox-22, oy+60), (ox-30, oy+92)) + [(ox+26, oy+96)] + \
        bez((ox+22, oy+60), (ox+22, oy+40), (ox+26, oy+8), (ox+42, oy))
    oak_crown(ox, oy, ((-120, 180, 72, 52, 2, 1), (115, 185, 78, 55, 1, 2), (0, 212, 100, 58, 0, 3), (-80, 218, 64, 44, 3, 4),
                       (85, 222, 70, 48, 0, 5)), W)
    form(trunk_pts, BARK, W*1.1, sdx=-14, sdy=0, sh=0.16)
    for pts, w0, w1 in ((bez((ox-18, oy+85), (ox-50, oy+105), (ox-90, oy+120), (ox-130, oy+150)), 18, 7),
                        (bez((ox+16, oy+88), (ox+50, oy+108), (ox+90, oy+125), (ox+128, oy+150)), 18, 7),
                        (bez((ox, oy+92), (ox-4, oy+120), (ox+6, oy+150), (ox+4, oy+180)), 16, 8)):
        tube(pts, w0, w1, BARK, lw=W, sh=0.12)
    stroke(bez((ox-10, oy+14), (ox-8, oy+34), (ox-12, oy+52), (ox-10, oy+70)), 0.6)
    stroke(bez((ox+8, oy+26), (ox+10, oy+46), (ox+6, oy+60), (ox+9, oy+78)), 0.6)
    shape(ell(ox+2, oy+50, 4.5, 6.5, 14), BARK_DK, 0.7)
    oak_crown(ox, oy, ((-150, 140, 62, 44, 0, 6), (150, 145, 64, 44, 3, 7), (-50, 175, 62, 40, 1, 8), (60, 172, 60, 40, 4, 9)), W)
    post_fence(ox-80, ox+82, oy-2, 16, 18)
    sign(ox+118, oy-2, 1.0)
    bench(700, 205, 1.0)
    leaves_on_ground(8, 440, 700, 200, 212, 9, (GOLD, COPPER, OLIVE))
    for i in range(6):
        r = random.Random(40+i); ax, ay = r.uniform(430, 640), r.uniform(199, 210)
        shape(ell(ax, ay, 2.2, 3, 10), Col(0.6, "#b88a3e"), 0.5); shape(ell(ax, ay+2.2, 2.6, 1.4, 10), BARK, 0.5)
    birch(80, 205, 150, 12, cols=(COPPER, COPPER_L))
    for i, bx in enumerate((900, 870)):
        bush(bx, 203, 70, 44, (OLIVE, OLIVE_L) if i else (RUST, COPPER), 60+i, dots=(ROSEHIP,), n=8)
    fg(186, FG, 1)
    tufts(10, 200, 940, 150, 180, 2)
    leaves_on_ground(6, 220, 940, 20, 170, 3)


def radous(b):
    base_sky(330, ((520, 480, 1.2), (800, 500, 0.9), (330, 430, 0.75)))
    ridge(345, 14, FAR2, 11, 0.45)
    hill = wave(300, ((40, 600), (6, 150)), 12)
    land(hill, FAR_WOOD, 0)
    clip(hill + [(970, -10), (-10, -10)])
    woods(345, 13, FAR_WOOD, (Col(0.75, "#c0a966"), Col(0.7, "#b27f55"), MID_WOOD, Col(0.72, "#9aab86")), 6, 10, 0, n=120, jit=30)
    unclip()
    stroke(hill, 0.5)
    fields(215, 290, 14, (STUBBLE, PLOUGH, MEADOW, WINTER), 3)
    for i, (hx, hy, sc, fl) in enumerate(((690, 240, 0.9, False), (805, 252, 0.8, True), (905, 236, 0.95, False))):
        dtree(hx - 40, hy + 4, 0.6, AUTUMN[i % 3], 70+i, w=0.7)
        cottage(hx, hy, sc, ROOF if i % 2 else ROOF_DK, fl, 0.8)
    post_fence(640, 960, 222, 14, 16)
    for i, (tx, ty, sc) in enumerate(((330, 232, 0.95), (470, 238, 0.8), (590, 228, 1.0), (250, 246, 0.6), (420, 256, 0.55))):
        r = random.Random(80+i)
        with T(tx, ty, sc):
            trunk(0, 0, 58, 13, 7, BARK, r.uniform(-8, 8))
            c = crown(0, 82, 52, 38, GREENY if i % 2 else OLIVE, GREENY_L if i % 2 else OLIVE_L, 90+i)
            for k in range(9):
                ax = r.uniform(-40, 40); ay = r.uniform(58, 105)
                if inside((ax, ay), c):
                    shape(ell(ax, ay, 3.5, 3.5, 12), APPLE if k % 3 else APPLE_Y, 0.6)
    hedge = [(160, 200, 90, 58, (OLIVE, OLIVE_L), (ROSEHIP,)), (240, 197, 100, 52, (RUST, COPPER), (SLOE,)),
             (330, 200, 90, 60, (GREENY, GREENY_L), (ROSEHIP, SLOE)), (410, 196, 80, 46, (COPPER, COPPER_L), (ROSEHIP,)),
             (478, 199, 70, 40, (OLIVE, OLIVE_L), (SLOE,))]
    for i, (hx, hy, hw, hh, cols, dots) in enumerate(hedge):
        bush(hx, hy, hw, hh, cols, 100+i, dots=dots, n=12)
    fg(190, FG, 21)
    tufts(10, 200, 940, 150, 182, 22)
    leaves_on_ground(5, 220, 940, 20, 170, 23)


def jezirko(b):
    base_sky(380, ((620, 495, 1.2), (850, 470, 0.9)))
    ridge(400, 10, FAR2, 30, 0.45)
    back = wave(390, ((14, 260), (5, 90), (2.5, 31)), 31)
    back = [(x, y + 30*max(0, 1 - x/300) + 26*max(0, (x-760)/200)) for x, y in back]
    base = 236
    r = random.Random(32)
    tones = (QUARRY, Col(0.78, "#cbbd9f"), Col(0.66, "#ad9a7e"), Col(0.74, "#c0ad8f"))
    x = -10; i = 0; prev = -10
    while x < 970:
        xb = x + r.uniform(45, 95); sl = r.uniform(-12, 12)
        top = [(x, yat(back, x))] + [p for p in back if x < p[0] < xb] + [(xb, yat(back, xb))]
        col_pts = top + [(xb + sl, base), (prev, base)]
        prev = xb + sl
        fill(col_pts, tones[i % len(tones)])
        clip(col_pts)
        fill([(xb - (xb-x)*0.28, base), (xb + 5 + sl, base), (xb + 5, 540), (xb - (xb-x)*0.28 - sl*0.1, 540)], 0.0, 0.1)
        yy = base + r.uniform(8, 24)
        while yy < max(p[1] for p in top) - 6:
            stroke([(x - 2, yy), ((x+xb)/2, yy + r.uniform(-3, 3)), (xb + 2, yy + r.uniform(-4, 4))], 0.55, g=QUARRY_DK)
            yy += r.uniform(14, 30)
        unclip()
        stroke([(xb, yat(back, xb)), (xb + sl*0.5, (yat(back, xb) + base)/2), (xb + sl, base)], 0.7)
        x = xb; i += 1
    rim = [(x, y - 7) for x, y in back]
    fill(back + list(reversed(rim)), OLIVE)
    stroke(back, W)
    stroke(rim, 0.5, g=Col(0.5, "#7f8440"))
    for i, (px, h) in enumerate(((720, 125), (800, 150), (880, 118))):
        pine(px, yat(back, px) - 6, h, 40+i)
    birch(620, yat(back, 620) - 4, 90, 44)
    for i in range(5):
        spruce(470 + i*38, yat(back, 470+i*38) - 5, 50 + (i % 2)*15, 50+i)
    for i, hx in enumerate((90, 200, 320)):
        heather(hx, yat(back, hx) - 4, 40, 47+i)
    water_top = wave(base, ((1.5, 120),), 36)
    water_bot = wave(196, ((9, 520), (3, 130)), 37)
    wpts = water_top + list(reversed(water_bot))
    fill(wpts, EMERALD)
    clip(wpts)
    fill(wave(base - 16, ((4, 70), (2, 25)), 38) + [(970, 270), (-10, 270)], EMERALD_DK)
    for k in range(4):
        fill(ell(180 + k*210, 213, 70, 7, 20), EMERALD_L, 0.45)
    for _ in range(26):
        x = r.uniform(20, 940); y = r.uniform(200, 228)
        stroke([(x, y), (x + r.uniform(12, 30), y)], 0.7, g=EMERALD_L)
    unclip()
    stroke(water_top, 0.6, g=EMERALD_DK)
    shore = [(x, y + 1) for x, y in water_bot]
    land(shore, Col(0.8, "#cdbb8c"), W)
    crag(900, yat(shore, 900) - 12, 150, 120, 61, QUARRY, W, 4)
    for i, (bx, bw, bh) in enumerate(((330, 50, 22), (365, 30, 14), (680, 60, 26), (728, 34, 16))):
        boulder(bx, yat(shore, bx) - 8, bw, bh, 60+i, ROCK)
    birch(120, 196, 175, 61, lean=30)
    leaf(560, 212, 5, 30, GOLD); leaf(610, 206, 4.5, 110, COPPER)
    fg(178, Col(0.78, "#c6bf7c"), 41, dk=Col(0.65, "#a79e62"))
    tufts(9, 200, 940, 140, 170, 42)
    for i in range(12):
        rr = random.Random(90+i)
        dot(rr.uniform(220, 940), rr.uniform(15, 160), rr.uniform(1.2, 2.2), ROCK_DK)
    leaves_on_ground(5, 220, 940, 20, 160, 43)


def boulder_sea(y0, y1, x0, x1, n, seed, big=1.0):
    r = random.Random(seed)
    items = [(r.uniform(x0, x1), r.uniform(y0, y1)) for _ in range(n)]
    for x, y in sorted(items, key=lambda p: -p[1]):
        k = (1.4 - (y-y0)/max(1, y1-y0)*0.7)*big
        boulder(x, y, r.uniform(36, 70)*k, r.uniform(18, 34)*k, int(x*7+y), ROCK if r.random() < 0.6 else ROCK_L, 0.8)


def plesivec(b):
    base_sky(260, ((560, 480, 1.3), (820, 430, 1.0), (430, 380, 0.7)))
    ridge(262, 14, FAR2, 51, 0.45, 520)
    ridge(238, 10, FAR, 52, 0.5, 300)
    plateau = wave(222, ((6, 400), (3, 120)), 53)
    land(plateau, Col(0.7, "#b0a864"), W)
    heather(470, yat(plateau, 470) - 4, 60, 54); heather(640, yat(plateau, 640) - 3, 50, 55)
    crag(560, 214, 100, 70, 66, ROCK, W, 3)
    crag(300, 214, 150, 190, 56, ROCK, W, 4)
    pine(250, 226, 190, 57, lean=-14)
    crag(775, 210, 170, 215, 58, ROCK, W, 5)
    pine(850, 222, 220, 59, lean=18)
    birch(700, 222, 110, 60, cols=(GOLD, GOLD_L))
    boulder_sea(198, 230, 170, 950, 26, 61)
    for i, (bx, bw) in enumerate(((230, 70), (420, 90), (560, 60), (660, 80), (900, 70))):
        bush(bx, 190, bw, 30, (BILBERRY, Col(0.55, "#cf5a3c")), 62+i, dots=(SLOE,), n=5)
    for i, hx in enumerate((350, 500, 620, 760, 850)):
        heather(hx, 190, 44, 70+i)
    fg(188, Col(0.72, "#bcb36e"), 63, dk=Col(0.6, "#9b9055"))
    tufts(8, 200, 940, 150, 180, 64, OLIVE)
    for i in range(10):
        rr = random.Random(120+i)
        dot(rr.uniform(220, 940), rr.uniform(12, 160), rr.uniform(1.2, 2.2), ROCK_DK)
    heather(930, 150, 40, 65)


def sparkle(x, y, s=1.0):
    pts = []
    for i in range(8):
        a = math.pi/2 + i*math.pi/4; rr = 7*s if i % 2 == 0 else 2*s
        pts.append((x + math.cos(a)*rr, y + math.sin(a)*rr))
    shape(pts, SPARK, 0.5)


def zahradka(b):
    base_sky(420, ((720, 500, 1.1),), Col(0.9, "#c5e2ee"), Col(0.95, "#f6efd8"))
    ridge(390, 12, FAR2, 71, 0.45)
    woods(365, 72, MID_WOOD, (Col(0.62, "#8c9a58"), Col(0.62, "#a79653"), Col(0.5, "#5d7f55"), Col(0.62, "#b08650")), 10, 18, 0.6)
    for i, (px, h) in enumerate(((120, 230), (860, 250))):
        pine(px, 230, h, 73+i, lean=(-12, 16)[i])
    ground = wave(232, ((4, 260),), 74)
    land(ground, Col(0.62, "#8fae55"), W)
    crag(290, 226, 200, 175, 75, ROCK, W, 4, True)
    crag(600, 228, 170, 118, 76, ROCK, W, 3, True)
    crag(815, 222, 210, 150, 77, ROCK, W, 4, True)
    spring = slab(455, 205, 120, 70, 90, ROCK_L)
    moss_cap(spring, 22, 91)
    slab(395, 200, 60, 36, 92, ROCK)
    slab(525, 200, 70, 40, 93, ROCK)
    pool = ell(462, 200, 58, 12, 30)
    shape(pool, EMERALD, W)
    fill(ell(452, 202, 38, 6, 24), EMERALD_L, 0.6)
    fall = bez((452, 262), (446, 244), (450, 226), (447, 206), 12)
    stroke(fall, 7, g=Col(0.5, "#4f9fbf")); stroke(fall, 3.5, g=POND_L)
    stroke(bez((452, 262), (455, 250), (449, 238), (453, 214), 10), 1.0, g=1.0)
    shape(ell(451, 262, 8, 4, 14), Col(0.2, "#3c3a36"), 0.6)
    for k in range(3):
        stroke(ell(447, 205, 10+k*7, 2+k*1.4, 16, 200, 340), 0.5, g=1.0)
    chest(350, 200, 1.3)
    for i, (cx, cy) in enumerate(((318, 203), (386, 203), (398, 199))):
        shape(ell(cx, cy, 3.2, 1.6, 12), SILVER, 0.5)
    fill(blob(318, 214, 16, 10, 94, 8), MOSS); stroke(blob(318, 214, 16, 10, 94, 8), 0.6, closed=True)
    for i, (fx, fl) in enumerate(((250, False), (580, True), (730, False), (900, True))):
        fern(fx, 215, 1.1, fl)
    for i, hx in enumerate((200, 285, 520, 760, 880)):
        heather(hx, 196, 46, 95+i)
    for i, (mx, my) in enumerate(((225, 205), (740, 206))):
        shape(bez((mx-5, my), (mx-5, my+6), (mx+5, my+6), (mx+5, my)) + [(mx+5, my)], Col(0.95, "#f3ead6"), 0.6)
        shape(bez((mx-9, my+5), (mx-7, my+15), (mx+7, my+15), (mx+9, my+5)) + [(mx-9, my+5)], APPLE, 0.7)
        for dx, dy in ((-3, 9), (3, 11), (0, 7)): dot(mx+dx, my+dy, 1.1, 1.0)
    beams((620, 760, 880), 540, 190, -230, 38)
    for sx, sy, ss in ((420, 290, 1.0), (505, 250, 0.7), (390, 250, 0.6), (560, 300, 0.8), (470, 320, 0.5)):
        sparkle(sx, sy, ss)
    fg(188, Col(0.68, "#a6b75e"), 76, dk=Col(0.55, "#86984a"))
    tufts(9, 200, 580, 150, 182, 77, MOSS)
    tufts(4, 720, 940, 150, 182, 78, MOSS)
    leaves_on_ground(5, 220, 560, 30, 170, 79)


def pole(b):
    base_sky(320, ((480, 480, 1.3), (760, 500, 1.0), (300, 430, 0.8), (900, 420, 0.6)))
    ridge(335, 18, FAR, 101, 0.5, 520)
    woods(305, 102, FAR_WOOD, (Col(0.75, "#c3ad63"), Col(0.7, "#b0784c"), Col(0.55, "#5f7f5a")), 7, 12, 0.5)
    lines = fields(195, 292, 103, (STUBBLE, PLOUGH, WINTER, STUBBLE), 3)
    for bx, by, s in ((360, 262, 0.7), (400, 259, 0.7), (780, 268, 0.5), (820, 266, 0.5)):
        with T(bx, by, s):
            shape(rrect(-14, 0, 28, 24, 10), STUBBLE, 0.7)
            shape(ell(8, 12, 7, 11, 16), GOLD_L, 0.7)
            stroke(ell(8, 12, 3.5, 6, 12), 0.5)
    stream = bez((-10, 246), (200, 262), (320, 222), (520, 238), 30) + bez((520, 238), (700, 254), (820, 212), (970, 226), 30)[1:]
    ribbon(stream, 7, POND, POND_L, 0.7)
    for i, (wx, sc) in enumerate(((250, 0.85), (410, 0.75), (560, 0.8), (700, 0.7), (860, 0.75))):
        willow(wx, yat(stream, wx) - 8, sc, 110+i)
    track = bez((-10, 178), (300, 200), (520, 192), (600, 230), 30) + bez((600, 230), (640, 250), (660, 270), (690, 292), 16)[1:]
    tl = [(x, y - 16*max(0.1, (292-y)/114)) for x, y in track]
    tr = [(x, y + 16*max(0.1, (292-y)/114)) for x, y in track]
    fill(tl + list(reversed(tr)), TRACK); stroke(tl, 0.7); stroke(tr, 0.7)
    fg(186, FG, 104)
    tufts(10, 200, 940, 150, 182, 105)
    leaves_on_ground(4, 220, 940, 20, 160, 106)
    for bx, by in ((620, 440), (650, 452), (590, 455)):
        stroke(bez((bx-7, by+3), (bx-4, by+5), (bx-2, by+3), (bx, by)) + bez((bx, by), (bx+2, by+3), (bx+4, by+5), (bx+7, by+3))[1:], 1.0)


def apple_tree(x, y, s=1.0, seed=1, cols=(OLIVE, OLIVE_L), n=12, w=W):
    r = random.Random(seed)
    with T(x, y, s):
        lean = r.uniform(-10, 10)
        trunk(0, 0, 55, 16, 8, BARK, lean, w)
        for sd in (-1, 1):
            tube(bez((lean*0.8, 50), (lean+sd*14, 62), (lean+sd*26, 72), (lean+sd*34, 80)), 6, 3, BARK, lw=w, sh=0)
        c = crown(lean, 88, 60, 40, cols[0], cols[1], seed, w, 12)
        for k in range(n):
            ax = lean + r.uniform(-50, 50); ay = r.uniform(58, 118)
            if inside((ax, ay), c):
                shape(ell(ax, ay, 3.8, 3.8, 12), APPLE if k % 3 else APPLE_Y, 0.6)


def fallen_apples(n, x0, x1, y0, y1, seed):
    r = random.Random(seed)
    for k in range(n):
        shape(ell(r.uniform(x0, x1), r.uniform(y0, y1), 3.6, 3.3, 12), APPLE if k % 3 else APPLE_Y, 0.6)


def sady(b):
    base_sky(330, ((600, 490, 1.2), (840, 450, 0.9), (330, 420, 0.8)))
    ridge(340, 14, FAR, 131, 0.5)
    woods(315, 132, FAR_WOOD, (Col(0.75, "#c9b067"), Col(0.7, "#b98450")), 6, 11, 0.5)
    land(wave(285, ((4, 300),), 133), MEADOW, 0.6)
    post_fence(-10, 970, 282, 12, 22, 0.6)
    for i, x in enumerate((90, 250, 420, 600, 760, 900)):
        apple_tree(x, 285, 0.42, 140+i, AUTUMN[(i+2) % 4], 6, 0.6)
    land(wave(255, ((3, 300),), 134), Col(0.8, "#d3c97c"), 0.7)
    for i, x in enumerate((180, 480, 690)):
        apple_tree(x, 250, 0.68, 150+i, AUTUMN[(i+3) % 4], 9, 0.8)
    walnut_x = 830
    with T(walnut_x, 206, 1.0):
        trunk(0, 0, 90, 26, 14, Col(0.6, "#9c8f7e"), 6)
        for (dx, dy, rx, ry, sd) in ((-60, 150, 60, 44, 1), (60, 150, 62, 46, 2), (0, 200, 80, 52, 3), (-30, 125, 50, 34, 4), (40, 118, 52, 34, 5)):
            crown(dx, dy, rx, ry, Col(0.72, "#c2bf57"), Col(0.82, "#e0d777"), 160+sd, W, 10, 2)
    apple_tree(300, 205, 1.0, 170, (GREENY, GREENY_L), 14)
    apple_tree(560, 210, 0.95, 171, (OLIVE, OLIVE_L), 14)
    with T(608, 206, 1):
        for sx in (0, 14):
            stroke([(sx, 0), (sx - 26, 86)], 3.2); stroke([(sx, 0), (sx - 26, 86)], 1.8, g=WOOD_L)
        for k in range(1, 7):
            yy = k*12; stroke([(-yy*0.3, yy), (14 - yy*0.3, yy)], 2.2); stroke([(-yy*0.3, yy), (14 - yy*0.3, yy)], 1.0, g=WOOD_L)
    with T(655, 204, 1):
        fill(rect(-14, 0, 14, 16), WOOD)
        for k in range(8):
            shape(ell(-11+k*3.2, 17+(k % 2)*2, 3.6, 3.6, 12), APPLE if k % 3 else APPLE_Y, 0.6)
        shape([(-15, 18), (15, 18), (12, 0), (-12, 0)], WOOD_L, W)
        for k in range(1, 4): stroke([(-14+k*0.5, k*4.5), (14-k*0.5, k*4.5)], 0.5)
        stroke(bez((-12, 18), (-10, 34), (10, 34), (12, 18)), 1.8); stroke(bez((-12, 18), (-10, 34), (10, 34), (12, 18)), 0.9, g=WOOD_L)
    fallen_apples(9, 230, 720, 196, 214, 172)
    fg(190, Col(0.78, "#cbc673"), 135, marks=0)
    r = random.Random(136)
    for _ in range(110):
        x = r.uniform(0, 960); y = r.uniform(4, 186)
        k = 0.6 + 0.9*(1 - y/190)
        stroke(bez((x, y), (x+1*k, y+5*k), (x+3*k, y+9*k), (x+5*k, y+12*k), 5), 0.6, g=Col(0.6, "#a8a452"))
    fallen_apples(4, 860, 950, 30, 150, 173)
    leaves_on_ground(4, 220, 940, 20, 160, 174, (OLIVE, GOLD))


def ves(b):
    base_sky(330, ((560, 490, 1.2), (820, 470, 1.0)))
    ridge(335, 14, FAR, 201, 0.5)
    woods(310, 202, FAR_WOOD, (Col(0.75, "#c3ad63"), Col(0.7, "#b0784c")), 6, 11, 0.5)
    land(wave(272, ((4, 300),), 203), MEADOW, 0.6)
    church(610, 262, 0.95)
    for i, (hx, hy, s, fl) in enumerate(((380, 238, 0.85, False), (470, 250, 0.7, True), (760, 246, 0.8, False), (880, 234, 0.9, True))):
        cottage(hx, hy, s, ROOF if i % 2 else ROOF_DK, fl)
    dtree(540, 250, 0.55, AUTUMN[0], 204, w=0.7)
    dtree(700, 244, 0.6, AUTUMN[1], 205, w=0.7)
    post_fence(330, 560, 232, 12, 16, 0.7)
    land(wave(232, ((2, 300),), 206), Col(0.72, "#b9c46c"), 0.8)
    pond = smooth([(300, 214), (360, 228), (470, 226), (560, 234), (700, 228), (792, 214), (760, 198), (640, 194), (520, 190), (400, 196)], 3)
    shape(pond, POND, W)
    clip(pond)
    fill(ell(560, 225, 240, 8, 30), POND_L, 0.8)
    r = random.Random(207)
    for _ in range(14):
        x = r.uniform(320, 760); y = r.uniform(198, 222)
        stroke([(x, y), (x+r.uniform(10, 24), y)], 0.6, g=POND_L)
    unclip()
    for k in range(10):
        rx = 300 + (k % 2)*480 + r.uniform(-10, 20); ry = 205 + r.uniform(-5, 5)
        stroke([(rx, ry), (rx+r.uniform(-3, 3), ry+r.uniform(14, 22))], 1.1, g=OLIVE)
        shape(ell(rx, ry+18, 1.8, 4.5, 10), BARK, 0.5)
    duck(460, 204, 1.25, True); duck(505, 212, 1.1); duck(650, 202, 1.2, False, True)
    with T(200, 198, 0.93):
        trunk(0, 0, 120, 30, 16, BARK_DK, 4)
        for (dx, dy, rx, ry, cc, sd) in ((-70, 160, 60, 48, (OLIVE, OLIVE_L), 1), (70, 170, 62, 46, (COPPER, COPPER_L), 2),
                                        (0, 215, 80, 50, (GREENY, GREENY_L), 3), (-50, 132, 48, 32, (RUST, COPPER), 4),
                                        (50, 130, 50, 34, (OLIVE, OLIVE_L), 5)):
            crown(dx, dy, rx, ry, cc[0], cc[1], 210+sd, W, 10, 2)
    fg(186, FG, 208)
    r = random.Random(209)
    for k in range(6):
        cx, cy = r.uniform(215, 330), r.uniform(150, 178)
        shape(ell(cx, cy, 4, 3.6, 12), Col(0.35, "#7a3f1e"), 0.6); dot(cx-1, cy+1, 1.1, Col(0.6, "#c07a4a"))
    tufts(9, 200, 940, 150, 182, 210)
    leaves_on_ground(5, 220, 940, 20, 160, 211)


def semik(b):
    base_sky(330, ((620, 480, 1.3), (860, 440, 0.9), (360, 420, 0.7)))
    ridge(335, 14, FAR, 221, 0.5)
    woods(308, 222, FAR_WOOD, (Col(0.75, "#c3ad63"), Col(0.7, "#b0784c")), 6, 11, 0.5)
    fields(225, 290, 223, (STUBBLE, PLOUGH, MEADOW), 2)
    for i, (tx, s) in enumerate(((290, 1.0), (660, 1.15))):
        with T(tx, 222, s):
            trunk(0, 0, 90, 22, 12, BARK_DK, (-6, 6)[i])
            for (dx, dy, rx, ry, ci, sd) in ((-40, 140, 50, 40, 0, 1), (40, 146, 52, 40, 1, 2), (0, 190, 64, 44, 0, 3), (0, 120, 44, 30, 2, 4)):
                cc = AUTUMN[(ci + i) % 3]
                crown(dx, dy, rx, ry, cc[0], cc[1], 230+sd+i*10, W, 10, 2)
    mound = bez((330, 200), (380, 250), (560, 252), (620, 200), 30)
    fill(mound + [(330, 190)], Col(0.68, "#a9b865")); stroke(mound, W)
    heather(400, 222, 40, 224); heather(550, 222, 36, 225)
    with T(476, 222, 1.0):
        form(rect(-52, 0, 52, 14), STONE_DK, W, sdx=-6, sdy=0, sh=0.15)
        form(rect(-42, 14, 42, 24), STONE, W, sdx=-5, sdy=0, sh=0.15)
        body = [(-32, 24), (32, 24), (32, 110)] + bez((32, 110), (30, 138), (-30, 138), (-32, 110))
        form(body, STONE, W*1.1, sdx=-8, sdy=0, sh=0.16)
        inner = [(-24, 34), (24, 34), (24, 106)] + bez((24, 106), (22, 128), (-22, 128), (-24, 106))
        shape(inner, Col(0.75, "#bfb8a8"), 0.6)
        horse_head(2, 84, 1.45, Col(0.88, "#e3ded2"))
        for k in range(3):
            stroke([(-18, 44+k*6), (18 - 8*(k == 2), 44+k*6)], 0.7, g=STONE_DK)
        shape(ell(0, 19, 6, 3.5, 16) + [], Col(0.6, "#8e8a82"), 0.6)
    with T(476, 236, 1):
        wreath = ell(0, 0, 18, 8, 30)
        stroke(wreath + wreath[:2], 5, g=Col(0.4, "#4f7a3c"))
        r = random.Random(226)
        for k in range(10):
            a = math.tau*k/10
            dot(math.cos(a)*18, math.sin(a)*8, 2.2, (APPLE, GOLD_L, HEATHER_L)[k % 3])
    for sx in (380, 572):
        with T(sx, 206, 1):
            shape(rect(-5, 0, 5, 14), Col(0.4, "#6b5d4b"), 0.7)
            shape([(-6, 14), (6, 14), (6, 20), (-6, 20)], Col(0.9, "#fbeccc"), 0.7)
            shape(ell(0, 24, 2, 3.5, 10), GOLD_L, 0.5)
    sign(760, 204, 1.2)
    for i, bx in enumerate((850, 920)):
        bush(bx, 200, 70, 40, AUTUMN[i+2], 227+i, dots=(ROSEHIP,), n=6)
    fg(188, FG, 228)
    tufts(10, 200, 940, 150, 182, 229)
    leaves_on_ground(6, 220, 580, 20, 170, 230)
    leaves_on_ground(3, 730, 940, 20, 170, 231)


def doubrava(b):
    base_sky(360, (), Col(0.9, "#d3e4e2"), Col(0.95, "#f4ecd2"))
    r = random.Random(303)
    for i in range(26):
        x = r.uniform(-10, 970); wd = r.uniform(6, 12)
        fill(rect(x-wd/2, 230, x+wd/2, 540), Col(0.85, "#d8ccb0"))
    canopy_band(400, 309, ((Col(0.85, "#e4d3a2"), Col(0.9, "#efe2b8")), (Col(0.82, "#dcc79a"), Col(0.88, "#eadbb0")),
                           (Col(0.82, "#d3cd9c"), Col(0.88, "#e3dfb4"))), 0.4, 50, 80, 1)
    land(wave(232, ((3, 300), (2, 90)), 304), Col(0.75, "#c9c07a"), 0.6)
    for i, (x, s_) in enumerate(((150, 0.62), (330, 0.55), (660, 0.58), (815, 0.66))):
        oak(x, 228, s_, 310+i, (2, 1, 0, 4), 0.7, Col(0.5, "#8a6a4c"))
    fill(rect(0, 0, 960, 540), Col(0.95, "#f4ecd2", alpha=0.2))
    beams((480, 590, 700), 540, 200, -170, 44)
    for i, x in enumerate((40, 920)):
        trunk(x, 196, 360, 64, 44, BARK_DK, (8, -8)[i], W*1.1, 0.35)
        stroke(bez((x-10, 230), (x-6, 300), (x-12, 380), (x-6, 460)), 0.6)
        stroke(bez((x+12, 260), (x+14, 330), (x+8, 400), (x+14, 480)), 0.6)
    canopy_band(492, 305, ((COPPER, COPPER_L), (OLIVE, OLIVE_L), (RUST, COPPER), (GOLD, GOLD_L)), W, 55, 85, 2)
    for i, (bx, bw) in enumerate(((290, 80), (700, 90))):
        bush(bx, 212, bw, 36, (OLIVE, OLIVE_L), 330+i)
    fern(420, 205, 1.1); fern(780, 205, 1.0, True)
    for i in range(10):
        ax, ay = r.uniform(240, 900), r.uniform(196, 215)
        shape(ell(ax, ay, 2.4, 3.2, 10), Col(0.6, "#b88a3e"), 0.5); shape(ell(ax, ay+2.3, 2.8, 1.5, 10), BARK, 0.5)
    fg(190, Col(0.7, "#bba35c"), 306, dk=Col(0.55, "#977a40"))
    leaves_on_ground(14, 200, 950, 15, 175, 307, (COPPER, GOLD, OLIVE, RUST))
    tufts(6, 200, 940, 150, 182, 308, OLIVE)


def beech(x, y, h, wd, col=BEECH_BARK, w=W, lean=0):
    pts = trunk(x, y, h, wd, wd*0.8, col, lean, w, 0.4)
    stroke(bez((x-wd*0.15, y+h*0.1), (x-wd*0.1, y+h*0.4), (x-wd*0.2+lean*0.5, y+h*0.6), (x-wd*0.1+lean*0.8, y+h*0.9)), w*0.5, g=Col(0.55, "#8f9394"))
    r = random.Random(int(x))
    for _ in range(3):
        ey = y + r.uniform(0.2, 0.8)*h
        stroke(ell(x + lean*(ey-y)/h + r.uniform(-0.2, 0.2)*wd, ey, wd*0.12, wd*0.06, 8, 20, 160), w*0.5)


def buciny(b):
    fill(rect(0, 0, 960, 540), Col(0.9, "#f3e2a8"))
    r = random.Random(401)
    for i in range(18):
        x = 20 + i*54 + r.uniform(-14, 14)
        fill(rect(x-5, 230, x+5, 540), Col(0.85, "#e6d6a6"))
    land(wave(240, ((3, 200),), 402), Col(0.82, "#e8c77f"), 0)
    for i in range(12):
        x = 30 + i*80 + r.uniform(-20, 20); wd = r.uniform(12, 18)
        shape(rect(x-wd/2, 225, x+wd/2, 560), BEECH_FAR, 0.5)
    land(wave(222, ((3, 200),), 403), Col(0.75, "#dcae62"), 0.5)
    for x, wd in ((160, 24), (390, 28), (470, 20), (610, 30), (770, 24)):
        beech(x, 212, 340, wd, Col(0.8, "#c9c8bd"), 0.7, r.uniform(-6, 6))
    fill(rect(0, 0, 960, 540), Col(0.97, "#fff1c9", alpha=0.18))
    land(wave(205, ((3, 250),), 404), LITTER, 0.8)
    for x, wd, ln in ((60, 60, 10), (270, 44, -6), (700, 52, 8), (900, 66, -10)):
        beech(x, 195, 380, wd, BEECH_BARK, W, ln)
    canopy_band(455, 405, ((GOLD, GOLD_L), (COPPER_L, GOLD_L), (GOLD, GOLD_L), (LARCH, GOLD_L)), W, 50, 78, 2)
    for i in range(16):
        leaf(r.uniform(200, 940), r.uniform(230, 430), r.uniform(4, 5.5), r.uniform(0, 360), (GOLD, COPPER_L, GOLD_L)[i % 3])
    beams((330, 480, 650, 820), 520, 190, -150, 36)
    fg(188, LITTER, 406, dk=LITTER_DK, marks=0)
    leaves_on_ground(40, 0, 960, 8, 180, 407, (COPPER, GOLD, RUST, COPPER_L))
    for i in range(8):
        bx, by = r.uniform(220, 930), r.uniform(192, 200)
        shape([(bx-3, by), (bx, by+4), (bx+3, by)], Col(0.45, "#8a5a2e"), 0.5)


def valy(b):
    base_sky(360, ((680, 500, 1.1),), Col(0.9, "#c5dcea"))
    ridge(335, 12, FAR2, 501, 0.4)
    woods(318, 502, FAR_WOOD, (Col(0.75, "#cfae5e"), Col(0.65, "#6e8a62"), Col(0.7, "#b0784c")), 9, 15, 0.5)
    r = random.Random(503)
    for i in range(8):
        larch2(20 + i*130 + r.uniform(-30, 30), 266, r.uniform(80, 120), 510+i, 0.6)
    land(wave(272, ((5, 400),), 504), Col(0.7, "#b7b26a"), 0.7)
    far_top = bez((200, 268), (380, 300), (760, 302), (980, 288), 40)
    far_foot = bez((200, 268), (420, 274), (800, 272), (980, 266), 40)
    fill(far_top + list(reversed(far_foot)), Col(0.74, "#c2bd72")); stroke(far_top, 0.6)
    for i, bx in enumerate((520, 640, 760)):
        birch(bx, yat(far_top, bx) - 6, 110 + i*8, 520+i)
    top = bez((-10, 316), (250, 310), (600, 272), (980, 262), 40)
    foot = bez((-10, 200), (300, 208), (650, 230), (980, 242), 40)
    slope = top + list(reversed(foot))
    fill(slope, Col(0.72, "#b3bd66"))
    clip(slope)
    fill(top + list(reversed([(x, y - 14) for x, y in top])), Col(0.8, "#d0d386"))
    for k in range(3):
        fill(foot + list(reversed([(x, y + 12 + k*12) for x, y in foot])), Col(0.5, "#6f7e3a"), 0.12)
    for _ in range(90):
        x = r.uniform(0, 960); y0, y1 = yat(foot, x), yat(top, x)
        y = r.uniform(y0 + 4, y1 - 6)
        stroke([(x, y), (x + 1.5, y + 6)], 0.5, g=Col(0.55, "#7f8c45"))
    unclip()
    stroke(top, W); stroke(foot, 0.7)
    crest = [(x, y - 7) for x, y in top]
    ribbon(crest, 5, TRACK, None, 0.4)
    for i, (lx, h) in enumerate(((250, 180), (480, 200), (720, 160))):
        larch2(lx, yat(top, lx) - 8, h, 530+i, W)
    for i, (bx, h) in enumerate(((360, 150), (600, 140))):
        birch(bx, yat(top, bx) - 8, h, 540+i)
    spruce(880, yat(top, 880) - 6, 170, 545)
    fern(120, yat(top, 120) - 60, 1.0); fern(560, yat(top, 560) - 30, 0.9, True)
    land(wave(198, ((3, 240),), 505), Col(0.6, "#8f9a52"), 0.6)
    fg(188, Col(0.72, "#bca864"), 506, dk=Col(0.6, "#9b884a"))
    leaves_on_ground(12, 200, 950, 15, 175, 507, (GOLD, LARCH, COPPER, GOLD_L))
    tufts(8, 200, 940, 150, 182, 508, OLIVE)


def hradec(b):
    base_sky(280, ((600, 490, 1.2), (840, 440, 0.9), (360, 400, 0.6)), Col(0.9, "#b3d6ec"))
    ridge(290, 14, FAR2, 601, 0.4, 600)
    ridge(262, 10, FAR, 602, 0.5, 350)
    fields(228, 262, 603, (Col(0.8, "#d9ce92"), Col(0.7, "#b99a7a"), Col(0.75, "#b8c28a")), 2, 0.4)
    for hx in (140, 170, 820, 850):
        cottage(hx, 240, 0.28, ROOF, False, 0.4, False)
    dtree(110, 238, 0.3, AUTUMN[0], 604, w=0.5)
    hill = bez((-10, 238), (200, 262), (760, 262), (970, 236), 30)
    land(hill, Col(0.7, "#b5b766"), W)
    ring = bez((120, 232), (300, 272), (660, 272), (840, 232), 30)
    fill(ring + list(reversed(bez((120, 222), (300, 250), (660, 250), (840, 222), 30))), Col(0.75, "#c6c779"))
    stroke(ring, 0.7)
    for i, (tx, s, ci) in enumerate(((150, 1.0, 1), (850, 1.05, 0))):
        with T(tx, 215, s):
            trunk(0, 0, 80, 22, 12, BARK_DK, (6, -6)[i])
            for (dx, dy, rx, ry, sd) in ((-40, 130, 50, 38, 1), (40, 136, 52, 40, 2), (0, 176, 62, 42, 3)):
                cc = AUTUMN[(ci+sd) % 4]
                crown(dx, dy, rx, ry, cc[0], cc[1], 610+sd+i*10, W, 10, 2)
    birch(260, 232, 130, 620); birch(760, 232, 120, 621)
    gx0, gx1 = 486, 574
    palisade(300, 780, 246, 92, 622, W, (gx0 - 6, gx1 + 6))
    shape(rect(gx0 + 4, 246, gx1 - 4, 326), Col(0.9, "#dfeef3"), 0.6)
    shape([(gx0 + 4, 246), (gx0 + 26, 254), (gx0 + 26, 320), (gx0 + 4, 326)], WOOD, 0.8)
    shape([(gx1 - 4, 246), (gx1 - 26, 254), (gx1 - 26, 320), (gx1 - 4, 326)], WOOD, 0.8)
    for gx in (gx0 + 15, gx1 - 15):
        stroke([(gx, 254), (gx, 318)], 0.5)
    for px in (gx0 - 8, gx1 - 6):
        form(rect(px, 242, px + 14, 374), WOOD_DK, W, sdx=-4, sdy=0, sh=0.16)
    form(rect(gx0 - 22, 326, gx1 + 22, 344), WOOD, W, sdx=0, sdy=4, sh=0.15)
    for k in range(9):
        xx = gx0 - 18 + k*14
        shape(rect(xx, 344, xx + 3, 362), WOOD_DK, 0.6)
    shape(rect(gx0 - 22, 360, gx1 + 22, 365), WOOD, 0.8)
    roof = [(gx0 - 34, 370), (gx1 + 34, 370), ((gx0 + gx1)/2 + 20, 406), ((gx0 + gx1)/2 - 20, 406)]
    shape(roof, Col(0.6, "#b98f55"), W)
    clip(roof)
    for k in range(9): stroke([(gx0 - 40, 372 + k*4), (gx1 + 40, 372 + k*4)], 0.45)
    unclip()
    front = bez((-10, 196), (260, 214), (700, 214), (970, 196), 30)
    land(front + [], Col(0.72, "#bfc06c"), W)
    ramp = [(200, 198)] + bez((200, 198), (255, 246), (285, 252), (330, 252), 12) + [(750, 252)] + \
        bez((750, 252), (795, 252), (825, 246), (880, 198), 12)
    fill(ramp, Col(0.74, "#b9c26c"))
    clip(ramp)
    fill([(200, 252), (880, 252), (880, 240), (200, 240)], Col(0.82, "#d3d68c"))
    for k in range(3):
        fill([(200, 190), (880, 190), (880, 204 + k*10), (200, 204 + k*10)], Col(0.5, "#6f7e3a"), 0.1)
    r = random.Random(640)
    for _ in range(60):
        x = r.uniform(220, 860); y = r.uniform(202, 238)
        stroke([(x, y), (x + 1.5, y + 5)], 0.5, g=Col(0.55, "#7f8c45"))
    unclip()
    stroke(ramp[1:-1], W)
    path = [(gx0 + 6, 252), (gx1 - 6, 252), (640, 194), (440, 194)]
    shape(smooth(path, 1), TRACK, 0.7)
    for i, bx in enumerate((240, 780)):
        bush(bx, 204, 80, 34, AUTUMN[i+1], 630+i, dots=(ROSEHIP, SLOE), n=6)
    heather(360, 212, 50, 632); heather(720, 212, 44, 633)
    fg(192, FG, 634)
    tufts(10, 200, 940, 150, 184, 635)
    leaves_on_ground(6, 220, 590, 20, 170, 636)
    leaves_on_ground(3, 720, 940, 20, 170, 637)


# ------------------------------------------------------------------ world map
MAP_TREES = ((Col(0.75, "#cfa94c"), Col(0.85, "#e2c46e")), (Col(0.6, "#c47a45"), Col(0.7, "#d99762")),
             (Col(0.65, "#9ea55a"), Col(0.75, "#b9bd74")), (Col(0.6, "#7f9c5a"), Col(0.7, "#9cb876")))


def mtree(x, y, k=1.0, cc=(GOLD, GOLD_L), w=0.55):
    stroke([(x, y), (x, y+6*k)], 1.4*k, g=BARK_DK)
    p = blob(x, y+10*k, 6.5*k, 6*k, int(x*3+y), 7, 0.18)
    fill(p, cc[0]); clip_fill(p, [(px-1.5*k, py+1.5*k) for px, py in p], cc[1]); stroke(p, w, closed=True)


def mspruce(x, y, k=1.0, w=0.55):
    pts = [(x, y+22*k), (x-7*k, y+9*k), (x-4*k, y+10*k), (x-8.5*k, y+2*k), (x+8.5*k, y+2*k), (x+4*k, y+10*k), (x+7*k, y+9*k)]
    fill(pts, SPRUCE); clip_fill(pts, rect(x, y, x+20, y+30), SPRUCE_DK); stroke(pts, w, closed=True)
    stroke([(x, y), (x, y+2*k)], 1.4*k, g=BARK_DK)


def forest_region(pts, seed, dense=21, avoid=(), spruce_share=0.45, k=1.0):
    region = smooth(pts, 3)
    shape(region, MAP_WOOD, 0.8)
    r = random.Random(seed)
    xs = [p[0] for p in region]; ys = [p[1] for p in region]
    items = []
    y = max(ys)
    while y > min(ys) - 5:
        x = min(xs) + r.uniform(0, dense*0.6)
        while x < max(xs):
            px, py = x + r.uniform(-4, 4), y + r.uniform(-3, 3)
            if inside((px, py + 6), region) and not any((px-ax)**2/(arx**2) + (py-ay)**2/(ary**2) < 1 for ax, ay, arx, ary in avoid):
                items.append((px, py))
            x += dense*r.uniform(0.8, 1.2)
        y -= dense*0.62
    for px, py in sorted(items, key=lambda p: -p[1]):
        if r.random() < spruce_share:
            mspruce(px, py, 0.85*k*r.uniform(0.9, 1.1))
        else:
            mtree(px, py, 0.95*k*r.uniform(0.85, 1.1), MAP_TREES[r.randrange(4)])
    return region


def map_fields(seed):
    r = random.Random(seed)
    cols = (Col(0.85, "#e6d18c"), Col(0.62, "#c29a6c"), Col(0.75, "#b9c67a"), Col(0.8, "#d4d493"), Col(0.8, "#e3c77a"))
    nx, ny = 15, 11
    V = {}
    for i in range(nx+1):
        for j in range(ny+1):
            V[i, j] = (-20 + i*1000/nx + (r.uniform(-14, 14) if 0 < i < nx else 0), -20 + j*580/ny + (r.uniform(-10, 10) if 0 < j < ny else 0))
    for i in range(nx):
        for j in range(ny):
            q = [V[i, j], V[i+1, j], V[i+1, j+1], V[i, j+1]]
            col = cols[r.randrange(len(cols))]
            fill(q, col)
            if col in (cols[1], cols[0]):
                clip(q)
                (xa, ya), (xb, yb) = q[0], q[2]
                for t in range(1, 8):
                    x = xa + (xb-xa)*t/8
                    stroke([(x, ya-5), (x+4, yb+5)], 0.4, g=Col(0.5, "#a88256") if col is cols[1] else Col(0.7, "#cdb26a"))
                unclip()
            stroke(q, 0.45, closed=True, g=MAP_EDGE)


def map_road(pts, w=2.4):
    p = smooth(pts, 3, closed=False)
    stroke(p, w+1.4, g=Col(0.5, "#9a8b60")); stroke(p, w, g=MAP_ROAD)


def map_trail(pts):
    p = smooth(pts, 3, closed=False)
    rs = lib.resample(p, 1.0)
    L = 0; last = -99
    for (xa, ya), (xb, yb) in zip(rs, rs[1:]):
        L += math.hypot(xb-xa, yb-ya)
        if L - last > 12:
            last = L
            dot(xa, ya, 3.2, 1.0)
            dot(xa, ya, 2.3, MAP_TRAIL)


def map_bg(b):
    fill(rect(0, 0, 960, 540), MAP_LAND)
    map_fields(701)
    fill(rect(0, 0, 960, 540), Col(0.9, "#efe6b8", alpha=0.18))
    avoid = [(500, 38, 60, 24), (725, 58, 60, 24), (200, 138, 60, 24), (675, 372, 60, 24), (850, 216, 60, 24), (450, 396, 60, 24),
             (500, 92, 62, 40), (725, 110, 56, 34), (675, 430, 56, 44), (850, 270, 56, 38), (200, 190, 58, 42), (450, 452, 50, 40)]
    forest_region([(290, -30), (300, 60), (380, 125), (450, 140), (540, 158), (620, 150), (700, 172), (800, 170), (880, 150), (990, 170), (990, -30)], 702, avoid=avoid)
    forest_region([(80, 170), (120, 110), (220, 100), (300, 130), (320, 200), (290, 265), (200, 290), (110, 268)], 703, avoid=avoid)
    forest_region([(560, 350), (640, 355), (720, 385), (820, 430), (930, 470), (990, 480), (990, 560), (620, 560), (560, 470), (540, 400)], 704, avoid=avoid)
    forest_region([(770, 250), (820, 205), (920, 200), (990, 230), (990, 340), (900, 355), (800, 330)], 705, avoid=avoid, spruce_share=0.1)
    forest_region([(560, 280), (600, 270), (630, 300), (600, 320), (565, 310)], 706, dense=14)
    forest_region([(300, 380), (360, 370), (380, 410), (330, 425), (290, 410)], 707, dense=14)
    forest_region([(640, 200), (690, 195), (700, 225), (650, 232)], 708, dense=14)
    stream = [(565, 150), (545, 190), (520, 215), (505, 240), (490, 262), (470, 300), (455, 340), (430, 380), (445, 420), (430, 470), (420, 560)]
    sp = smooth(stream, 3, closed=False)
    stroke(sp, 4, g=Col(0.4, "#3f7596")); stroke(sp, 2.8, g=MAP_WATER)
    for (px, py, rx, ry) in ((540, 200, 12, 7), (566, 212, 10, 6), (515, 470, 10, 6), (400, 300, 8, 5)):
        shape(ell(px, py, rx, ry, 20), MAP_WATER, 0.7); fill(ell(px-2, py+1.5, rx*0.5, ry*0.3, 12), POND_L)
    map_road([(480, 260), (470, 330), (455, 400), (445, 470), (440, 560)])
    map_road([(480, 260), (400, 250), (330, 230), (250, 260), (140, 300), (-20, 320)])
    map_road([(480, 260), (560, 250), (660, 260), (760, 300), (900, 380), (990, 400)])
    map_road([(480, 260), (430, 200), (380, 160), (330, 60), (300, -20)])
    for hx, hy, fl in ((320, 228, False), (338, 222, True), (252, 262, False)):
        with T(hx, hy, 0.22): cottage(0, 0, 1, ROOF, fl, 0.5, False)
    trails = [
        [(480, 245), (465, 200), (525, 170), (490, 140), (498, 122)],
        [(495, 272), (565, 310), (600, 360), (650, 370), (668, 398)],
        [(500, 250), (590, 225), (640, 180), (700, 170), (718, 138)],
        [(460, 255), (400, 238), (350, 200), (280, 212), (240, 196)],
        [(475, 278), (420, 320), (400, 360), (470, 390), (455, 420)],
        [(505, 262), (600, 300), (700, 240), (760, 280), (806, 272)],
    ]
    for t in trails:
        map_trail(t)
    shape(rrect(455, 244, 50, 32, 6), Col(0.9, "#efe4c8"), 0.7)
    houses = [(452, 282, False), (474, 286, True), (500, 282, False), (522, 272, True), (524, 250, False), (512, 230, True),
              (488, 226, False), (462, 228, True), (440, 236, False), (436, 258, True)]
    for hx, hy, fl in sorted(houses, key=lambda h: -h[1]):
        if (hx, hy) == (474, 286):
            with T(hx, hy - 2, 0.3): church(0, 0, 1, 0.6)
        else:
            with T(hx - 7, hy - 4, 0.24): cottage(0, 0, 1, ROOF if hx % 3 else ROOF_DK, fl, 0.5, False)
    with T(500, 90, 1.45):
        shape(bez((-40, -16), (-26, 22), (26, 22), (40, -16)) + [(40, -16)], Col(0.6, "#7f9658"), 0.8)
        for i, (bx, by, bw, bh) in enumerate(((-12, 0, 20, 13), (10, -1, 22, 15), (-2, 10, 20, 13), (18, 10, 12, 9), (-22, 9, 11, 8))):
            boulder(bx, by, bw, bh, 720+i, ROCK, 0.7, False)
        shape(ell(-2, 5, 3.5, 2.6, 12), Col(0.25, "#3a3530"), 0.4)
        mspruce(-32, -14, 0.8); mspruce(32, -14, 0.8)
    with T(675, 425, 1.4):
        shape(bez((-36, -14), (-22, 16), (22, 16), (36, -14)) + [(36, -14)], Col(0.55, "#6f8a50"), 0.8)
        form(rect(-7, 0, 7, 32), STONE, 0.8, sdx=-4, sdy=0, sh=0.16)
        for k in range(1, 5): stroke([(-7, k*6.4), (7, k*6.4)], 0.4)
        shape(rect(-9, 32, 9, 37), STONE_DK, 0.7)
        for k in range(3): shape(rect(-9 + k*7, 37, -5.5 + k*7, 41), STONE_DK, 0.6)
        shape(rect(-2, 13, 2, 20), WINDOW, 0.5)
        mspruce(-22, -8, 0.65); mspruce(22, -9, 0.7)
    with T(725, 110, 1.4):
        for tx, ty in ((-22, 6), (4, 10), (22, 4), (-8, -10), (14, -12)):
            mtree(tx, ty, 0.7, MAP_TREES[int(tx+30) % 4])
        wall = smooth([(-32, -4), (-16, 2), (0, -2), (16, 4), (32, -1)], 2, closed=False)
        stroke(wall, 6.4, g=0.0); stroke(wall, 4.8, g=STONE)
        for i in range(0, len(wall)-1, 2):
            dot(wall[i][0], wall[i][1]+0.5, 0.8, STONE_DK)
    with T(200, 190, 1.4):
        shape(bez((-38, -14), (-22, 24), (22, 26), (38, -14)) + [(38, -14)], Col(0.65, "#9b9a74"), 0.8)
        for i, (bx, by, bw, bh) in enumerate(((-6, 6, 14, 12), (8, 7, 12, 10), (1, 15, 11, 8), (-18, -2, 12, 8))):
            boulder(bx, by, bw, bh, 730+i, ROCK_L, 0.6, False)
        shape(ell(20, -4, 12, 5.5, 22), EMERALD, 0.7); fill(ell(18, -3, 6, 2, 12), EMERALD_L)
        mspruce(-26, -12, 0.6)
    with T(450, 450, 1.4):
        for hx, hy, fl in ((-26, 6, False), (18, 8, True), (-18, -10, True)):
            with T(hx, hy, 0.2): cottage(0, 0, 1, ROOF_DK if fl else ROOF, fl, 0.5, False)
        shape(rect(-2, -14, 12, -6), STONE_DK, 0.6)
        horse_head(5, 4, 0.45, STONE, 0.6)
    with T(850, 270, 1.3):
        shape(ell(0, 0, 36, 21, 40), Col(0.62, "#8fa45a"), 0.8)
        for rr, g in ((29, Col(0.75, "#bfc57a")), (18, Col(0.7, "#aebb68"))):
            stroke(ell(0, 0, rr, rr*0.55, 40), 4.0, closed=True, g=0.0)
            stroke(ell(0, 0, rr, rr*0.55, 40), 2.6, closed=True, g=g)
        for tx, ty in ((-8, -5), (8, -2), (0, 4)):
            mtree(tx, ty, 0.6, MAP_TREES[int(tx+9) % 4])
    # far Brdy in the fog (future trails)
    for (hx, hy, rx, ry) in ((60, 40, 120, 80), (190, 0, 120, 60), (30, 300, 90, 70), (30, 470, 80, 60)):
        top = ell(hx, hy, rx, ry, 30, 0, 180)
        fill(top + [(hx - rx, hy)], FOG_HILL)
        stroke(top, 0.5)
        for i in range(3, 28, 4):
            px, py = top[i]
            fill([(px, py + 9), (px - 4, py - 1), (px + 4, py - 1)], Col(0.7, "#9aabbd"))
    r = random.Random(740)
    for i in range(26):
        t = i/26
        if t < 0.55:
            x, y = r.uniform(-20, 70), 540 - t/0.55*540
        else:
            x, y = (t-0.55)/0.45*340, r.uniform(-20, 60)
        fill(blob(x, y, r.uniform(50, 90), r.uniform(30, 50), 750+i, 9, 0.2), FOG)
    stroke(rect(6, 6, 954, 534), 1.4, closed=True, g=Col(0.4, "#6e5a36"))


# ------------------------------------------------------------------ atlas
def maple(x, y, s, rot, col):
    pts = []
    for i in range(80):
        a = math.tau*i/80; t = a - math.pi/2
        rr = 0.42 + 0.58*((1 + math.cos(5*t))/2)**2.2
        rr *= 0.75 + 0.25*math.sin(a)
        rr += 0.05*((i % 4) < 2)
        pts.append((math.cos(a)*rr, math.sin(a)*rr))
    with T(x, y, s, rot=rot):
        shape(pts, col, 0.8)
        for k in range(5):
            stroke([(0, -0.1), (math.cos(math.pi/2 + (k-2)*1.26)*0.8, math.sin(math.pi/2 + (k-2)*1.26)*0.8)], 0.4, g=Col(0.4, "#8a3a1e"))
        stroke([(0, -0.1), (0.05, -0.7)], 0.8)


def oak_leaf(x, y, s, rot, col):
    left = []; right = []
    for i in range(41):
        t = i/40
        wd = 0.32*math.sin(math.pi*t)**0.7*(0.62 + 0.38*abs(math.cos(t*math.pi*4.5)))
        left.append((-wd, t)); right.append((wd, t))
    pts = left + list(reversed(right))
    with T(x, y, s, rot=rot):
        shape(pts, col, 0.8)
        stroke([(0, -0.15), (0, 0.95)], 0.5, g=Col(0.4, "#6e4a24"))
        for k in range(1, 5):
            stroke([(0, k*0.2), (-0.2, k*0.2+0.08)], 0.35, g=Col(0.4, "#6e4a24"))
            stroke([(0, k*0.2-0.05), (0.2, k*0.2+0.03)], 0.35, g=Col(0.4, "#6e4a24"))


def atlas_bg(b):
    planks(b, TABLE, 64, 801)
    fill(rect(0, 0, 960, 540), Col(0.2, "#2a1a0c", alpha=0.08))
    maple(62, 505, 46, -25, COPPER); oak_leaf(905, 505, 70, -120, GOLD)
    maple(40, 48, 34, 40, GOLD)
    fill([(x+8, y-8) for x, y in rrect(24, 18, 912, 494, 14)], Col(0.1, "#1a0f06", alpha=0.3))
    form(rrect(24, 18, 912, 494, 14), COVER, W*1.2, sdx=4, sdy=4, sh=0.15)
    for side in (0, 1):
        x0, x1 = (38, 479) if side == 0 else (481, 922)
        for k in (3, 2, 1):
            off = k*2.2
            ox0 = x0 - off if side == 0 else x0
            ox1 = x1 if side == 0 else x1 + off
            shape(rect(ox0, 30 - off, ox1, 500 - off*0.3), PAPER_EDGE, 0.5)
        page = rect(x0, 30, x1, 500)
        shape(page, PAPER, 0.8)
        clip(page)
        for gx in range(int(x0) + 18, int(x1) - 4, 18):
            stroke([(gx, 34), (gx, 496)], 0.35, g=GRID, alpha=0.45, taper=False)
        for gy in range(48, 496, 18):
            stroke([(x0 + 4, gy), (x1 - 4, gy)], 0.35, g=GRID, alpha=0.45, taper=False)
        gut = x1 if side == 0 else x0
        for k in range(7):
            wd = 34 - k*4.6
            fill(rect(gut - wd, 30, gut, 500) if side == 0 else rect(gut, 30, gut + wd, 500), PAPER_SH)
        edge = x0 if side == 0 else x1
        fill(rect(edge, 30, edge + (10 if side == 0 else -10), 500), Col(0.9, "#fff8e6", alpha=0.35))
        unclip()
    stroke([(480, 28), (480, 502)], 1.0)
    rib = bez((486, 500), (492, 516), (474, 528), (486, 546), 16)
    stroke(rib, 7.2); stroke(rib, 5.4, g=RIBBON)
    rib2 = bez((486, 30), (490, 16), (478, 8), (484, -6), 12)
    stroke(rib2, 7.2); stroke(rib2, 5.4, g=RIBBON)
    shape([(478, -6), (490, -6), (484, 1)], TABLE, 0)
    with T(942, 120, 1, rot=78):
        body = rect(0, -4.5, 190, 4.5)
        shape(body, PENCIL, 0.8)
        stroke([(0, -1.5), (190, -1.5)], 0.4); stroke([(0, 1.5), (190, 1.5)], 0.4)
        shape([(190, -4.5), (206, 0), (190, 4.5)], PENCIL_WOOD, 0.8)
        shape([(201.5, -1.3), (206, 0), (201.5, 1.3)], Col(0.25, "#3a3a3a"), 0.5)
        shape(rect(-10, -4.5, 0, 4.5), Col(0.7, "#b8b8b8"), 0.7)
        shape(rrect(-20, -4.5, 12, 9, 3), Col(0.75, "#ef8f9a"), 0.8)
    oak_leaf(876, 468, 36, -35, Col(0.7, "#c8923e"))
    shape(rect(858, 478, 876, 486), Col(0.9, "#f0e6c0", alpha=0.8), 0.4)


ASSETS = [
    ("bestin", 960, 540, bestin, "bg"),
    ("radous", 960, 540, radous, "bg"),
    ("jezirko", 960, 540, jezirko, "bg"),
    ("plesivec", 960, 540, plesivec, "bg"),
    ("zahradka", 960, 540, zahradka, "bg"),
    ("pole", 960, 540, pole, "bg"),
    ("sady", 960, 540, sady, "bg"),
    ("ves", 960, 540, ves, "bg"),
    ("semik", 960, 540, semik, "bg"),
    ("doubrava", 960, 540, doubrava, "bg"),
    ("buciny", 960, 540, buciny, "bg"),
    ("valy", 960, 540, valy, "bg"),
    ("hradec", 960, 540, hradec, "bg"),
    ("map", 960, 540, map_bg, "rooms"),
    ("atlas", 960, 540, atlas_bg, "rooms"),
]
