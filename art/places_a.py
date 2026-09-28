"""Station backgrounds for trails 1-3 and the title screen: autumn Brdy around Hostomice."""
import math, random
import lib
from lib import C, G, Col, ell, bez, rrect
from style3 import *
from scenes3 import cloud

SKY = Col(0.92, "#bcdcee")
SKY_LOW = Col(0.96, "#eef2e2")
SKY_WARM = Col(0.9, "#f8cf92")
SKY_WARM_LOW = Col(0.97, "#fff3cf")
FAR = Col(0.8, "#a9c0d0")
FAR2 = Col(0.76, "#98b2c4")
FAR_GOLD = Col(0.8, "#c3c39a")
FAR_RUST = Col(0.75, "#bfa28c")
HAZE = Col(0.72, "#8fa9a8")
HAZE_GOLD = Col(0.76, "#c4b47c")
HAZE_RUST = Col(0.7, "#b98f70")
MID_SPRUCE = Col(0.5, "#557f69")
MID_GOLD = Col(0.7, "#d6ab52")
MID_RUST = Col(0.6, "#c27b4a")
MID_GREEN = Col(0.6, "#8ea75e")
SPRUCE = Col(0.35, "#2f5f47")
SPRUCE_DK = Col(0.28, "#244c3a")
FIR = Col(0.35, "#2c5a55")
BEECH = Col(0.75, "#eaa83a")
BEECH_LT = Col(0.85, "#f6cf5a")
COPPER = Col(0.55, "#d0692e")
OAK = Col(0.6, "#bb8a33")
MAPLE = Col(0.5, "#dc4b35")
MAPLE_OR = Col(0.65, "#ee8a32")
LEAF_GREEN = Col(0.6, "#7fae4c")
ALDER = Col(0.55, "#6f9a48")
ALDER_LT = Col(0.65, "#a2bd57")
BARK = Col(0.45, "#7a5236")
BEECH_BARK = Col(0.7, "#aeada4")
BEECH_BARK_DK = Col(0.55, "#85867e")
SPRUCE_BARK = Col(0.4, "#6e5240")
ALDER_BARK = Col(0.4, "#5f5852")
MEADOW = Col(0.82, "#cdd489")
MEADOW_GREEN = Col(0.75, "#a9c86c")
MEADOW_GOLD = Col(0.85, "#e0cf7c")
STUBBLE = Col(0.88, "#ecd48c")
PLOUGH = Col(0.5, "#a0714c")
PLOUGH_DK = Col(0.4, "#7f583a")
FIELD_GREEN = Col(0.75, "#a2c46c")
PATH = Col(0.85, "#e3c898")
PATH_DK = Col(0.7, "#c4a473")
FLOOR = Col(0.6, "#cf9550")
FLOOR_DK = Col(0.5, "#b07338")
LITTER = Col(0.75, "#dcb070")
SLOPE = Col(0.65, "#d19a58")
MOSS = Col(0.6, "#8aab4c")
MOSS_DK = Col(0.5, "#658e3d")
MOSS_LT = Col(0.7, "#a6bd62")
NEEDLES = Col(0.5, "#98744c")
ROCK = Col(0.65, "#aba79d")
ROCK_LT = Col(0.75, "#c6c2b5")
ROCK_DK = Col(0.5, "#88847b")
LICHEN = Col(0.8, "#cfd690")
LICHEN2 = Col(0.8, "#e6db9c")
LICHEN_GREY = Col(0.85, "#dde2d4")
WATER = Col(0.6, "#7fbdd8")
WATER_DK = Col(0.5, "#5b9dc1")
WATER_LT = Col(0.75, "#a8d6ea")
FOAM = Col(1.0, "#f4fbff")
BERRY = Col(0.35, "#dc3129")
SLOE = Col(0.25, "#44528a")
ROSEHIP = Col(0.4, "#e0482c")
BRAMBLE = Col(0.2, "#2e2442")
HEATHER = Col(0.7, "#d586bb")
CHICORY = Col(0.7, "#83a8ea")
TANSY = Col(0.85, "#f3c42e")
STEM = Col(0.5, "#6f8f45")
FERN = Col(0.6, "#7aa74a")
FERN_RUST = Col(0.55, "#c9803e")
BUSH = Col(0.55, "#7c9a45")
BUSH_RUST = Col(0.55, "#b8743c")
WOOD = Col(0.55, "#a0703f")
WOOD_DK = Col(0.4, "#6f4a2a")
WOOD_LT = Col(0.7, "#cc9a5e")
ROOF = Col(0.45, "#c4553a")
ROOF_DK = Col(0.35, "#8e3a28")
SHINGLE = Col(0.45, "#7d5a3c")
WINDOW = Col(0.4, "#5d8fb3")
WALLS = [Col(0.92, "#f6e3a6"), Col(0.9, "#f4c7b6"), Col(0.9, "#cfe2c0"), Col(0.94, "#faf1de"), Col(0.88, "#bcd5e6"), Col(0.9, "#f2d28c")]
STONE = Col(0.8, "#cfc8b8")
COBBLE = Col(0.85, "#ddd3bf")
COBBLE_LN = Col(0.78, "#cdc1a8")
MUSH_CAP = Col(0.45, "#a4552e")
MUSH_RED = Col(0.45, "#d9392e")
MUSH_STEM = Col(0.95, "#f5ecd6")
ANTHILL = Col(0.5, "#9c7449")
ANTHILL_DK = Col(0.4, "#7a5634")
MARK_RED = Col(0.4, "#d7322e")
WHITE = Col(1.0, "#ffffff")
DARK = Col(0.0, "#1c1a18")
GLOW = Col(1.0, "#fff6c4")
GLOW2 = Col(0.95, "#ffe38a")
MIST = Col(1.0, "#ffffff", alpha=0.35)
RAY = Col(1.0, "#fff4c8", alpha=0.22)
HALO = Col(1.0, "#fff2a8", alpha=0.3)
SPARK = Col(0.95, "#fff09a")

W = 0.9


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def mix(a, b, t):
    ha, hb = a.hex.lstrip("#"), b.hex.lstrip("#")
    ch = [round(int(ha[i:i+2], 16)*(1-t) + int(hb[i:i+2], 16)*t) for i in (0, 2, 4)]
    return Col(float(a)*(1-t) + float(b)*t, "#%02x%02x%02x" % tuple(ch))


def shade(c, t=0.3): return mix(c, DARK, t)
def tint(c, t=0.3): return mix(c, WHITE, t)


def smooth(pts, it=2):
    for _ in range(it):
        out = []
        for i in range(len(pts)):
            a, b = pts[i], pts[(i+1) % len(pts)]
            out += [(a[0]*0.75+b[0]*0.25, a[1]*0.75+b[1]*0.25), (a[0]*0.25+b[0]*0.75, a[1]*0.25+b[1]*0.75)]
        pts = out
    return pts


def wf(y, amp, seed, per=300):
    r = random.Random(seed); ph = [r.uniform(0, 6.3) for _ in range(3)]
    return lambda x: y + amp*(0.6*math.sin(x/per*6.28+ph[0]) + 0.3*math.sin(x/per*14.4+ph[1]) + 0.1*math.sin(x/per*35.8+ph[2]))


def along(f, x0=-10, x1=970, step=5):
    return [(x, f(x)) for x in range(int(x0), int(x1)+1, step)]


def land(f, col, w=W, x0=-10, x1=970, bottom=-10, ink=None):
    top = along(f, x0, x1)
    fill([(x0, bottom)] + top + [(x1, bottom)], col)
    if w: stroke(top, w, g=ink if ink is not None else 0.0)


def solid(pts, col, line=W, sd=(-3, 2), sh=0.15, deco=None):
    fill(pts, col)
    if deco:
        C.saveState(); C.clipPath(poly(pts), stroke=0, fill=0); deco(); C.restoreState()
    if sh: offset_shadow(pts, sd[0], sd[1], sh)
    if line: stroke(pts, line, closed=True)


def sky(top=SKY, low=SKY_LOW, y0=180, y1=540, n=16):
    fill(rect(0, 0, 960, 540), low)
    for i in range(n):
        fill(rect(0, y0+(y1-y0)*i/n, 960, 540), mix(low, top, (i+1)/n))


def mist(y0, y1, seed=1, col=MIST):
    fill([(-10, y0)] + along(wf(y1, 6, seed, 200)) + [(970, y0)], col)


def rays(x, y, angs, L=700, col=RAY):
    for a, w in angs:
        a0, a1 = math.radians(a-w/2), math.radians(a+w/2)
        fill([(x, y), (x+math.cos(a0)*L, y+math.sin(a0)*L), (x+math.cos(a1)*L, y+math.sin(a1)*L)], col)


# ------------------------------------------------------------------ trees
def blob(cx, cy, rx, ry, seed, n=10):
    r = random.Random(seed); off = r.uniform(0, 6.28); pts = []
    amp = min(1.0, 10/n)
    for i in range(n):
        a0 = off + math.tau*i/n; a1 = off + math.tau*(i+1)/n
        p0 = (cx+math.cos(a0)*rx, cy+math.sin(a0)*ry); p1 = (cx+math.cos(a1)*rx, cy+math.sin(a1)*ry)
        am = (a0+a1)/2; k = 1 + (0.12 + 0.1*r.random())*amp
        m = (cx+math.cos(am)*rx*k, cy+math.sin(am)*ry*k)
        pts += bez(p0, ((p0[0]+m[0])/2+(m[0]-cx)*0.16*amp, (p0[1]+m[1])/2+(m[1]-cy)*0.16*amp),
                   ((p1[0]+m[0])/2+(m[0]-cx)*0.16*amp, (p1[1]+m[1])/2+(m[1]-cy)*0.16*amp), p1, 6)
    return pts


def speckle(x, cy, rx, ry, cols, r, n, size=2.6):
    for _ in range(n):
        a = r.uniform(0, 6.28); d = r.uniform(0.15, 0.92)
        fill(ell(x+math.cos(a)*rx*d, cy+math.sin(a)*ry*d, size, size*0.55, 8, rot=r.uniform(0, 180)), r.choice(cols))


def foliage(x, cy, rx, ry, cols, seed, line=W, sh=0.13):
    r = random.Random(seed)
    accents = cols[2:] or cols[1:]
    if rx < 44:
        crown = blob(x, cy, rx, ry, seed, 9)

        def deco():
            if len(cols) > 1:
                fill(blob(x-rx*0.25, cy+ry*0.28, rx*0.6, ry*0.52, seed+1, 8), cols[1])
            if rx > 20:
                speckle(x, cy, rx, ry, accents, r, int(rx*0.5), 2.2)
        solid(crown, cols[0], line, sd=(-rx*0.22, ry*0.2), sh=sh, deco=deco)
        return crown
    crown = blob(x, cy, rx, ry, seed, 12)
    fill(crown, shade(cols[0], 0.12))
    lobes = []
    ring = max(6, int((rx+ry)/28))
    for i in range(ring):
        a = math.tau*i/ring + r.uniform(-0.2, 0.2)
        lobes.append((x+math.cos(a)*rx*0.6, cy+math.sin(a)*ry*0.58, rx*r.uniform(0.4, 0.48), ry*r.uniform(0.42, 0.5)))
    for k in range(max(2, ring//3)):
        lobes.append((x+r.uniform(-rx*0.3, rx*0.3), cy+r.uniform(-ry*0.25, ry*0.2), rx*0.42, ry*0.42))
    lobes.sort(key=lambda l: -l[1] + 0.3*l[0])
    for i, (lx, ly, lrx, lry) in enumerate(lobes):
        pts = blob(lx, ly, lrx, lry, seed+20+i, 8)
        top = (ly-cy)/ry*0.5 - (lx-x)/rx*0.5

        def deco(lx=lx, ly=ly, lrx=lrx, lry=lry, top=top):
            if len(cols) > 1 and top > -0.1:
                fill(blob(lx-lrx*0.25, ly+lry*0.3, lrx*0.55, lry*0.45, seed+60+i, 7), cols[1])
            speckle(lx, ly, lrx, lry, accents, r, int(lrx*0.3), 2.4)
        base = mix(cols[0], cols[2], 0.4) if len(cols) > 2 and r.random() < 0.3 else cols[0]
        solid(pts, base, line, sd=(-lrx*0.3, lry*0.28), sh=sh, deco=deco)
    return crown


def spruce_pts(x, y, w, h, tiers, seed, droop=0.2, blunt=0.0):
    r = random.Random(seed); right = []
    for i in range(tiers):
        t = i/tiers
        yb = y + h*t*0.93
        hw = w/2*(1-t)**0.95*r.uniform(0.88, 1.08)
        right += [(x+hw, yb - h/tiers*droop), (x+hw*0.4, yb + h/tiers*0.6)]
    left = [(2*x-px+r.uniform(-1, 1)*w*0.03, py+r.uniform(-1, 1)*h*0.012) for px, py in right]
    apex = [(x-w*blunt, y+h*0.985), (x, y+h), (x+w*blunt, y+h*0.985)] if blunt else [(x, y+h)]
    return [(x, y+h*0.03)] + right + apex + list(reversed(left))


def spruce(x, g, h, col=SPRUCE, seed=1, w=None, line=W, bark=SPRUCE_BARK, fir=False, sh=0.18):
    w = w or h*(0.5 if fir else 0.42)
    cb = g + h*0.09
    solid(rect(x-w*0.065, g, x+w*0.065, cb+h*0.2), bark, line*0.8, sh=0)
    pts = spruce_pts(x, cb, w, h*0.91, max(4, int(h/(22 if fir else 17))), seed, 0.05 if fir else 0.22, 0.03 if fir else 0.0)
    solid(pts, col, line, sd=(-w*0.2, h*0.02), sh=sh)
    return pts


def leafy(x, g, h, rx, cols, seed, bark=BARK, line=W, ry=None, dots=None, trunk_w=None):
    r = random.Random(seed)
    ry = ry or rx*0.85
    tw = trunk_w or rx*0.16
    cy = g + h - ry
    fork = max(g + (cy-g)*0.45, cy - ry*1.3)
    trunk = bez((x-tw*1.5, g), (x-tw*0.7, g+tw*0.6), (x-tw*0.55, g+(fork-g)*0.4), (x-tw*0.5, fork)) + [(x-tw*0.3, cy), (x+tw*0.3, cy)] + \
        bez((x+tw*0.5, fork), (x+tw*0.55, g+(fork-g)*0.4), (x+tw*0.7, g+tw*0.6), (x+tw*1.5, g))
    solid(trunk, bark, line, sd=(-tw*0.5, 0), sh=0.2)
    for s in (-1, 1):
        tube(bez((x+s*tw*0.2, fork), (x+s*tw*0.8, fork+ry*0.15), (x+s*rx*0.3, cy-ry*0.6), (x+s*rx*0.5, cy-ry*0.35), 10), tw*0.75, tw*0.35, bark, lw=line, cap=False, sh=0)
    crown = foliage(x, cy, rx, ry, cols, seed, line)
    if dots:
        c, n, rad = dots
        for k in range(n):
            a = r.uniform(0, 6.28); d = r.uniform(0.1, 0.85)
            bx, by = x+math.cos(a)*rx*d, cy+math.sin(a)*ry*d
            for dx, dy in ((0, 0), (rad*1.7, -rad*0.6), (rad*0.6, -rad*1.6)):
                shape(ell(bx+dx, by+dy, rad, rad, 8), c, line*0.45)
    return crown


def beech(x, g, h, rx, seed, cols=(BEECH, BEECH_LT, COPPER), line=W, ry=None, trunk_w=None):
    return leafy(x, g, h, rx, list(cols), seed, BEECH_BARK, line, ry or rx*0.95, trunk_w=trunk_w)


def far_trees(xs, g, h, rx, cols, bark, haze, t, seed, line=W*0.6):
    for i, x in enumerate(xs):
        leafy(x, g(x), h, rx, [mix(c, haze, t) for c in cols], seed+i, mix(bark, haze, t), line)


def big_trunk(x, g, w, bark=BEECH_BARK, seed=1, top=560, lean=0, line=W, kind="beech"):
    r = random.Random(seed)
    L = bez((x-w*0.95, g), (x-w*0.55, g+w*0.1), (x-w*0.5, g+w*0.5), (x-w*0.5, g+w*1.4)) + [(x-w*0.45+lean, top)]
    R = [(x+w*0.45+lean, top), (x+w*0.5, g+w*1.4)] + bez((x+w*0.5, g+w*1.4), (x+w*0.5, g+w*0.5), (x+w*0.55, g+w*0.1), (x+w*0.95, g))

    def deco():
        for k in range(int((top-g)/14)):
            yy = g + w*0.5 + k*14 + r.uniform(-4, 4)
            xx = x + r.uniform(-w*0.35, w*0.25) + lean*(yy-g)/(top-g)
            if kind == "beech":
                stroke([(xx-w*0.12, yy), (xx+w*0.12, yy+r.uniform(-1, 1))], line*0.7, g=BEECH_BARK_DK)
            else:
                stroke([(xx, yy), (xx+r.uniform(-1, 1), yy+10)], line*0.6, g=WOOD_DK)
    solid(L + R, bark, line, sd=(-w*0.28, 0), sh=0.18, deco=deco)


def treeline(f, cols, seed, x0=-20, x1=980, step=11, hmin=22, hmax=40, spruce_p=0.5, line=0.45, base=None, rows=1, drop=None):
    r = random.Random(seed)
    drop = drop or hmax*0.45
    if base is not None:
        land(f, base, 0, x0, x1)
    for row in range(rows):
        x = x0 + r.uniform(0, step)
        while x < x1:
            h = r.uniform(hmin, hmax)*(1+0.1*row); c = r.choice(cols); y = f(x) - row*drop
            if r.random() < spruce_p:
                pts = spruce_pts(x, y - h*0.3, h*0.42, h, max(3, int(h/9)), r.randrange(999))
            else:
                pts = blob(x, y + h*0.2, h*0.45, h*0.42, r.randrange(999), 8)
            fill(pts, c)
            if line: stroke(pts, line, closed=True)
            x += step*r.uniform(0.7, 1.3)


# ------------------------------------------------------------------ ground dressing
def rock(x, y, w, h, seed, col=ROCK, line=W, lichen=True, moss=None, facet=True):
    r = random.Random(seed)
    pts = [(x-w/2, y), (x+w/2, y)]
    for i in range(1, 8):
        a = math.pi*i/8
        pts.append((x+math.cos(a)*w/2*r.uniform(0.8, 1.05), y+math.sin(a)*h*r.uniform(0.75, 1.05)))
    pts = smooth(pts, 2)

    def deco():
        fill(blob(x-w*0.22, y+h*0.75, w*0.22, h*0.16, seed+3, 7), tint(col, 0.22))
        if moss:
            fill(blob(x-w*0.05, y+h*1.02, w*0.5, h*0.3, seed, 8), moss)
        if lichen:
            for k in range(max(2, int(w/10))):
                lx, ly = x+r.uniform(-w*0.4, w*0.4), y+r.uniform(h*0.15, h*0.8)
                s = r.uniform(1.2, 2.8)
                fill(ell(lx, ly, s, s*0.65, 10), r.choice((LICHEN, LICHEN_GREY, tint(col, 0.35))))
    solid(pts, col, line, sd=(-w*0.16, h*0.14), sh=0.2, deco=deco)
    if facet:
        stroke(bez((x+w*0.05, y+h*0.85), (x+w*0.1, y+h*0.6), (x+w*0.22, y+h*0.45), (x+w*0.3, y+h*0.3), 8), line*0.6)
    return pts


def outcrop(x, g, w, h, seed, col=ROCK, line=W):
    r = random.Random(seed)
    fr = [0, 0.45, 0.72, 0.68, 1.0, 0.88, 0.62, 0.42, 0]
    xs = [-0.5, -0.46, -0.3, -0.16, -0.02, 0.14, 0.3, 0.44, 0.5]
    pts = [(x+w*a+r.uniform(-1, 1)*w*0.02, g+h*b*r.uniform(0.9, 1.05)) for a, b in zip(xs, fr)]
    pts = smooth(pts[:1] + [(pts[0][0], g)] + pts[1:], 1)
    pts = [(px, max(g, py)) for px, py in pts]

    def deco():
        for k in range(-6, 10):
            x0 = x - w*0.6 + k*13
            stroke([(x0, g), (x0+h*1.4, g+h*1.2)], line*0.5, g=shade(col, 0.25))
        fill(blob(x-w*0.15, g+h*0.9, w*0.2, h*0.1, seed, 7), tint(col, 0.25))
        for k in range(int(w/9)):
            s = r.uniform(1.3, 3.2)
            fill(ell(x+r.uniform(-w*0.4, w*0.4), g+r.uniform(h*0.1, h*0.85), s, s*0.65, 10), r.choice((LICHEN, LICHEN_GREY, LICHEN2)))
        fill(blob(x+w*0.05, g+h*1.02, w*0.25, h*0.07, seed+2, 7), MOSS)
    solid(pts, col, line, sd=(-w*0.2, 0), sh=0.2, deco=deco)


def bush(x, g, w, h, col, seed, berries=None, line=W, cols=()):
    r = random.Random(seed)
    pts = [(px, max(py, g)) for px, py in blob(x, g+h*0.42, w/2, h*0.62, seed, max(7, int(w/16)))]

    def deco():
        fill(blob(x-w*0.15, g+h*0.72, w*0.3, h*0.25, seed+1, 7), tint(col, 0.2))
        if cols:
            speckle(x, g+h*0.45, w*0.5, h*0.55, cols, r, int(w*0.25), 2.2)
    solid(pts, col, line, sd=(-w*0.15, h*0.15), sh=0.14, deco=deco)
    if berries:
        c, n, rad = berries
        for k in range(n):
            bx, by = x+r.uniform(-w*0.4, w*0.4), g+h*r.uniform(0.25, 0.9)
            shape(ell(bx, by, rad, rad, 8), c, line*0.45)
            if r.random() < 0.6:
                shape(ell(bx+rad*1.6, by-rad*0.8, rad, rad, 8), c, line*0.45)


def tuft(x, y, k=1.0, col=MEADOW_GREEN, line=W*0.7):
    pts = [(x-4*k, y), (x-3.4*k, y+5*k), (x-1.8*k, y+1.4*k), (x-0.3*k, y+8*k), (x+1.2*k, y+1.5*k),
           (x+3*k, y+5.5*k), (x+3.8*k, y+0.8*k), (x+4.4*k, y)]
    shape(pts, col, line)


def tufts(n, x0, x1, y0, y1, seed, col=MEADOW_GREEN, k=(0.9, 1.4)):
    r = random.Random(seed)
    for _ in range(n):
        tuft(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(*k), col)


def flower(x, y, kind, s=1.0):
    h = {"chicory": 22, "tansy": 18, "heather": 7}[kind]*s
    if kind == "heather":
        shape(blob(x, y+h*0.5, 7*s, h*0.7, int(x), 7), Col(0.5, "#6e8a4a"), W*0.5)
        r = random.Random(int(x*7))
        for _ in range(9):
            dot(x+r.uniform(-6, 6)*s, y+r.uniform(2, 10)*s, 1.3*s, HEATHER)
        return
    stroke(bez((x, y), (x+1*s, y+h*0.4), (x-1*s, y+h*0.7), (x, y+h)), W*0.8, g=STEM)
    if kind == "chicory":
        for a in range(0, 360, 45):
            ra = math.radians(a)
            shape(ell(x+math.cos(ra)*2.6*s, y+h+math.sin(ra)*2.6*s, 2.2*s, 1.1*s, 8, rot=a), CHICORY, W*0.35)
        dot(x, y+h, 1.1*s, Col(0.3, "#3a5aa0"))
        shape(ell(x+4*s, y+h*0.55, 1.6*s, 1.6*s, 8), CHICORY, W*0.35)
    else:
        for dx, dy in ((-3, 0), (0, 1), (3, 0), (-1.5, 2.6), (1.5, 2.6), (0, -1.6)):
            shape(ell(x+dx*s, y+h+dy*s, 1.7*s, 1.7*s, 10), TANSY, W*0.4)


def fern(x, y, s=1.0, col=FERN, flip=False):
    with T(x, y, s, flip):
        rach = bez((0, 0), (4, 14), (14, 26), (28, 30), 18)
        for i in range(2, 17):
            px, py = rach[i]; t = i/18
            L = 9*(1-t)+2; ax, ay = rach[i+1][0]-px, rach[i+1][1]-py; d = math.hypot(ax, ay) or 1
            nx, ny = -ay/d, ax/d
            for sg in (-1, 1):
                tip = (px+nx*L*sg+ax/d*L*0.4, py+ny*L*sg+ay/d*L*0.4)
                lf = [(px, py), (px+nx*L*0.5*sg+ax/d*1.8, py+ny*L*0.5*sg+ay/d*1.8), tip, (px+nx*L*0.5*sg-ax/d*0.4, py+ny*L*0.5*sg-ay/d*0.4)]
                shape(lf, col, W*0.4)
        stroke(rach, W*0.7)


def fern_clump(x, y, s=1.0, col=FERN):
    fern(x, y, s, col, True); fern(x, y, s*0.85, col); fern(x+2, y, s*0.7, shade(col, 0.12), True)


def mushroom(x, y, s=1.0, cap=MUSH_CAP, spots=False):
    with T(x, y, s):
        shape(bez((-2.2, 0), (-2.8, 4), (-2.2, 7), (-1.8, 9)) + bez((1.8, 9), (2.2, 7), (2.8, 4), (2.2, 0)), MUSH_STEM, W*0.6)
        c = bez((-7, 8), (-6.5, 15), (6.5, 15), (7, 8)) + bez((7, 8), (3, 6.8), (-3, 6.8), (-7, 8))
        shape(c, cap, W*0.7)
        if spots:
            for dx, dy in ((-3.5, 10), (0.5, 12.5), (3.8, 10.2)):
                dot(dx, dy, 0.9, WHITE)


def litter(n, x0, x1, y0, y1, seed, cols=(COPPER, BEECH, FLOOR_DK), size=2.2):
    r = random.Random(seed)
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        k = size*(1.2 - 0.6*(y-y0)/max(1, y1-y0))
        fill(ell(x, y, k*1.4, k*0.6, 8, rot=r.uniform(-40, 40)), r.choice(cols))


def falling(n, seed, x0=440, x1=950, y0=220, y1=520, cols=(BEECH, COPPER, BEECH_LT)):
    r = random.Random(seed)
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        with T(x, y, 1, rot=r.uniform(0, 360)):
            shape(bez((0, -4), (3, -3), (3.5, 1), (0, 4.5)) + bez((0, 4.5), (-3.5, 1), (-3, -3), (0, -4)), r.choice(cols), W*0.5)
            stroke([(0, -5), (0, 3)], W*0.35)


def fg(col, y=196, seed=1, patches=9, edge=None):
    f = wf(y, 3, seed, 300)
    top = along(f)
    fill([(-10, -10)] + top + [(970, -10)], col)
    r = random.Random(seed)
    for i in range(patches):
        px, py = r.uniform(-40, 1000), r.uniform(90, y-14)
        fill(blob(px, py, r.uniform(50, 120), r.uniform(4, 7), seed+i, 9), mix(col, DARK if i % 2 else WHITE, 0.045))
    stroke(top, W*0.8, g=shade(col, 0.6))
    if edge:
        c, n = edge
        for _ in range(n):
            x = r.uniform(0, 960)
            tuft(x, f(x)-2, r.uniform(1.1, 1.7), c)
    return f


def trail(col=PATH, seed=1, yl=84, yr=42, tongue=None, pebbles=26, grass=None):
    wob = wf(0, 3, seed, 220)
    f = lambda x: yr + (yl-yr)*(0.5+0.5*math.cos(math.pi*min(1, max(0, x/960)))) + wob(x)
    xs = range(-10, 971, 5)
    if tongue:
        xa, xb, xv, yv, wv = tongue
        ya, yb = f(xa), f(xb)
        chain = [(x, f(x)) for x in xs if x <= xa] + \
            bez((xa, ya), (xa+(xv-xa)*0.2, ya+(yv-ya)*0.5), (xv-wv-30, yv-(yv-ya)*0.35), (xv-wv, yv)) + \
            bez((xv+wv, yv), (xv+wv-20, yv-(yv-yb)*0.35), (xb+(xv-xb)*0.1, yb+(yv-yb)*0.5), (xb, yb)) + \
            [(x, f(x)) for x in xs if x >= xb]
    else:
        chain = [(x, f(x)) for x in xs]
    fill([(-10, -10)] + chain + [(970, -10)], col)
    stroke(chain, W*0.8)
    r = random.Random(seed)
    for _ in range(pebbles):
        px = r.uniform(0, 960); py = r.uniform(4, f(px)-8)
        fill(ell(px, py, r.uniform(1.2, 2.6), r.uniform(0.8, 1.5), 8), shade(col, 0.15))
    if grass:
        for x in range(10, 960, 38):
            if r.random() < 0.55:
                tuft(x+r.uniform(-10, 10), f(x)-3, r.uniform(0.8, 1.2), grass)
    return f


def star4(x, y, rad, col=SPARK):
    pts = []
    for i in range(8):
        a = math.radians(90 + i*45); rr = rad if i % 2 == 0 else rad*0.3
        pts.append((x+math.cos(a)*rr, y+math.sin(a)*rr))
    shape(pts, col, W*0.5)


def reeds(x, y, n, seed, h=30):
    r = random.Random(seed)
    for i in range(n):
        xx = x + r.uniform(-n*3, n*3); hh = h*r.uniform(0.7, 1.1); lean = r.uniform(-4, 4)
        stroke(bez((xx, y), (xx, y+hh*0.4), (xx+lean*0.5, y+hh*0.8), (xx+lean, y+hh)), W*0.8, g=Col(0.5, "#8a9a4a"))
        if r.random() < 0.5:
            shape(rrect(xx+lean*0.8-1.6, y+hh*0.72, 3.2, hh*0.22, 1.5), Col(0.35, "#7a4a2a"), W*0.5)


def cottage(x, g, w, h, wall, roof=ROOF, seed=1, line=W, chimney=True):
    solid(rect(x-w/2, g, x+w/2, g+h), wall, line, sd=(-w*0.1, 0), sh=0.12)
    rf = [(x-w/2-w*0.08, g+h-1), (x, g+h+w*0.42), (x+w/2+w*0.08, g+h-1)]
    if chimney:
        solid(rect(x+w*0.18, g+h+w*0.1, x+w*0.28, g+h+w*0.36), Col(0.7, "#c98a6a"), line*0.8, sh=0)
    solid(rf, roof, line, sd=(-w*0.12, 0), sh=0.15)
    for wx in (-0.28, 0.12):
        solid(rect(x+w*wx, g+h*0.35, x+w*wx+w*0.16, g+h*0.72), WINDOW, line*0.6, sh=0)


def log(x0, x1, y, rad, seed, col=SPRUCE_BARK):
    r = random.Random(seed)
    body = [(x0, y), (x1, y+rad*0.1), (x1, y+rad*1.9), (x0, y+rad*2.1)]

    def deco():
        for k in range(int((x1-x0)/26)):
            xx = x0 + 10 + k*26 + r.uniform(-6, 6)
            stroke([(xx, y+rad*r.uniform(0.3, 0.8)), (xx+r.uniform(14, 24), y+rad*r.uniform(0.5, 1.4))], W*0.5, g=shade(col, 0.3))
        fill(blob((x0+x1)/2, y+rad*2.1, (x1-x0)*0.45, rad*0.3, seed, 10), MOSS)
    solid(body, col, W, sd=(0, rad*0.5), sh=0.18, deco=deco)
    shape(ell(x1, y+rad, rad*0.45, rad*0.95, 20), WOOD_LT, W)
    stroke(ell(x1, y+rad, rad*0.22, rad*0.5, 14), W*0.4, closed=True)


def stump(x, g, w, h):
    body = [(x-w/2-4, g), (x+w/2+4, g), (x+w/2, g+h), (x-w/2, g+h)]
    solid(body, SPRUCE_BARK, W, sd=(-w*0.2, 0), sh=0.18)
    shape(ell(x, g+h, w/2, w*0.14, 24), WOOD_LT, W)
    for k in (0.3, 0.6):
        stroke(ell(x, g+h, w/2*k, w*0.14*k, 16), W*0.4, closed=True)
    fill(blob(x-w*0.2, g+h*0.5, w*0.2, h*0.3, int(x), 7), MOSS)


# ------------------------------------------------------------------ trail 1
def zator(b):
    sky()
    cloud(640, 492, 1.25); cloud(860, 458, 0.95); cloud(520, 445, 0.6)
    f0 = wf(348, 14, 1, 520)
    treeline(f0, [FAR, FAR, mix(FAR, FAR_GOLD, 0.35), mix(FAR, FAR_RUST, 0.25)], 11, step=7, hmin=12, hmax=18, line=0, base=FAR, rows=3, drop=12)
    f2 = wf(284, 9, 2, 380)
    land(f2, FIELD_GREEN, W*0.6)
    cuts = [-40, 150, 360, 560, 740, 1000]
    cols = [STUBBLE, PLOUGH, MEADOW_GOLD, FIELD_GREEN, STUBBLE]
    for i in range(5):
        xa, xb = cuts[i], cuts[i+1]
        ta, tb = 480+(xa-480)*0.55, 480+(xb-480)*0.55
        pts = [(xa, 236), (xb, 236)] + [(x, f2(x)-2) for x in range(int(tb), int(ta)-1, -5)]
        fill(pts, cols[i])
        stroke([(xb, 236), (tb, f2(tb)-2)], W*0.5)
        if cols[i] is PLOUGH:
            C.saveState(); C.clipPath(poly(pts), stroke=0, fill=0)
            for k in range(-6, 16):
                x0 = xa + k*14
                stroke([(x0, 236), (480+(x0-480)*0.55, f2(480+(x0-480)*0.55))], W*0.45, g=PLOUGH_DK)
            C.restoreState()
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST, MID_GREEN], 21, x0=-20, x1=210, step=10, hmin=20, hmax=32, line=0.45, rows=2, drop=10)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST], 22, x0=760, x1=980, step=10, hmin=20, hmax=32, line=0.45, rows=2, drop=10)
    for i, (hx, hw) in enumerate(((250, 26), (290, 22), (330, 28), (372, 20))):
        cottage(hx, f2(hx)-14, hw, hw*0.6, WALLS[i], seed=i, line=W*0.6, chimney=i % 2 == 0)
    land(wf(236, 2, 3, 300), MEADOW_GREEN, W*0.6)
    for px, py, rx, ry in ((700, 221, 112, 11), (872, 231, 58, 6)):
        e = ell(px, py, rx, ry, 40)
        solid(e, WATER, W*0.8, sd=(0, -ry*0.5), sh=0.12)
        for k in range(3):
            stroke([(px-rx*0.5+k*rx*0.35, py+ry*0.2-k*2), (px-rx*0.3+k*rx*0.35, py+ry*0.2-k*2)], W*0.8, g=FOAM)
        reeds(px-rx*0.92, py-2, 6, int(px), 26); reeds(px+rx*0.9, py-2, 4, int(px)+1, 22)
    f = fg(MEADOW, 200, 4, edge=(MEADOW_GREEN, 14))
    for x, w, h, c, s in ((330, 90, 46, BUSH, 1), (400, 70, 38, BUSH_RUST, 2), (545, 80, 42, BUSH, 3), (920, 110, 50, BUSH_RUST, 4)):
        bush(x, f(x)-3, w, h, c, s, (ROSEHIP, 6, 2.0), cols=(MID_GOLD, LEAF_GREEN))
    leafy(470, f(470)-3, 150, 50, [MAPLE_OR, BEECH, LEAF_GREEN], 5, dots=(BERRY, 9, 2.2))
    leafy(860, f(860)-3, 125, 42, [BEECH, MAPLE_OR, LEAF_GREEN], 6, dots=(BERRY, 7, 2.1))
    trail(seed=1, tongue=(520, 700, 640, 199, 5), grass=MEADOW_GREEN)
    tufts(10, 200, 940, 100, 180, 7)
    for x in (230, 300, 760, 790, 930):
        flower(x, 150+(x % 30), "chicory", 0.9)


def chumava(b):
    sky(y0=240)
    cloud(820, 480, 1.0)
    f1 = wf(338, 16, 11, 380)
    treeline(f1, [HAZE, HAZE_GOLD, HAZE_RUST], 12, step=10, hmin=22, hmax=36, line=0, base=HAZE, rows=2)
    f2 = wf(285, 10, 12, 300)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_GREEN, MID_RUST], 13, step=12, hmin=34, hmax=58, line=0.5, base=MID_SPRUCE, rows=2, drop=20)
    land(wf(244, 3, 13, 300), MOSS, W*0.6)
    cliff = smooth([(380, 204), (392, 250), (430, 282), (500, 300), (560, 306), (594, 300), (594, 210),
                    (648, 210), (648, 302), (700, 310), (770, 300), (830, 276), (862, 240), (872, 204)], 2)
    r = random.Random(14)

    def blocks():
        for _ in range(26):
            bx, by = r.uniform(390, 870), r.uniform(205, 300)
            stroke([(bx, by), (bx+r.uniform(12, 30), by+r.uniform(-3, 3)), (bx+r.uniform(20, 36), by+r.uniform(6, 12))], W*0.55, g=shade(ROCK_DK, 0.3))
        for _ in range(30):
            s = r.uniform(1.2, 2.6)
            fill(ell(r.uniform(390, 870), r.uniform(205, 300), s, s*0.6, 8), r.choice((LICHEN, LICHEN_GREY)))
        fill([(370, 278)] + [(x, 290+14*math.sin(x/40)+(0 if x < 590 or x > 652 else -60)) for x in range(370, 890, 8)] + [(890, 330), (370, 330)], MOSS)
    solid(cliff, ROCK_DK, W, sd=(-26, 8), sh=0.18, deco=blocks)
    fall = [(594, 302), (648, 302), (652, 206), (590, 206)]

    def streaks():
        fill(rect(590, 200, 604, 310), WATER_LT)
        for k in range(8):
            xx = 598 + k*6.5
            stroke([(xx, 298), (xx+r.uniform(-1, 1), 212)], W*r.uniform(0.8, 1.4), g=FOAM)
    solid(fall, WATER, W, sh=0, deco=streaks)
    stroke(bez((590, 302), (605, 308), (638, 308), (652, 302)), W*2.2, g=FOAM)
    pool = ell(620, 205, 175, 20, 40)
    solid(pool, WATER, W, sd=(0, -8), sh=0.1)
    fill([(760, 198), (980, 186), (980, 200), (780, 210)], WATER)
    stroke([(760, 198), (980, 186)], W*0.7)
    for k in range(9):
        stroke(ell(560+k*15, 204+(k % 3)*3, 8, 3, 10, 0, 180), W*0.9, g=FOAM)
        dot(575+k*11, 214+(k % 2)*5, 1.4, FOAM)
    for k in range(5):
        stroke([(470+k*40, 196+(k % 2)*4), (490+k*40, 196+(k % 2)*4)], W*0.8, g=WATER_LT)
    rock(420, 194, 90, 42, 6, ROCK, moss=MOSS)
    rock(820, 192, 100, 46, 7, ROCK_LT, moss=MOSS_DK)
    leafy(300, 205, 240, 72, [ALDER, ALDER_LT, MID_GOLD, LEAF_GREEN], 8, ALDER_BARK, trunk_w=12)
    leafy(905, 196, 300, 84, [ALDER, ALDER_LT, BEECH_LT, LEAF_GREEN], 9, ALDER_BARK, trunk_w=14)
    f = fg(MOSS_LT, 192, 14, edge=(MOSS, 12))
    for x, s, c in ((365, 1.3, FERN), (475, 1.1, FERN_RUST), (760, 1.2, FERN_RUST), (865, 1.4, FERN), (210, 1.2, FERN_RUST)):
        fern_clump(x, f(x)-3, s, c)
    trail(Col(0.8, "#d8c08e"), 4, grass=MOSS)
    tufts(8, 200, 950, 100, 180, 15, MOSS)
    litter(30, 200, 950, 60, 185, 16, (ALDER_LT, BEECH, FLOOR_DK))


def brdlavka(b):
    sky(Col(0.9, "#cfe0dc"), Col(0.95, "#eef1e0"), y0=220)
    for i, (y, c, hh) in enumerate(((300, Col(0.8, "#b3c7bd"), (60, 110)), (262, Col(0.65, "#86a595"), (80, 150)))):
        f = wf(y, 10, 30+i, 300)
        land(f, c, 0)
        r = random.Random(40+i); x = -20
        while x < 990:
            h = r.uniform(*hh)
            fill(spruce_pts(x, f(x)-5, h*0.36, h, int(h/10), r.randrange(99)), c)
            x += r.uniform(22, 40)
    rays(640, 560, ((235, 6), (250, 4), (262, 5)), 520)
    land(wf(234, 3, 33, 300), MOSS_LT, W*0.6)
    for x, g, h, s in ((140, 232, 200, 1), (280, 230, 215, 2), (440, 226, 330, 3), (700, 228, 350, 4), (810, 232, 270, 5), (360, 238, 150, 6)):
        spruce(x, g, h, SPRUCE if s % 2 else SPRUCE_DK, s)
    spruce(1000, 176, 600, SPRUCE_DK, 7, w=330)
    f = fg(MOSS, 198, 34, edge=(MOSS_DK, 12))
    x0, g = 560, 208
    solid(rect(x0-72, g-4, x0+72, g+30), ROCK_DK, W, sh=0)
    rr = random.Random(9)
    for row, (yy, hh) in enumerate(((g-4, 17), (g+12, 18))):
        xx = x0 - 72 - (row*10)
        while xx < x0 + 72:
            ww = rr.uniform(20, 30)
            a, b2 = max(xx, x0-72), min(xx+ww, x0+72)
            if b2 - a > 6:
                shape(smooth(rect(a+1, yy+1, b2-1, yy+hh-1), 1), rr.choice((ROCK, ROCK_LT, Col(0.7, "#b6b0a2"))), W*0.6)
            xx += ww
    shape(ell(x0, g+30, 64, 7, 30), WATER_DK, W*0.8)
    stroke([(x0-30, g+31), (x0-6, g+31)], W*0.8, g=WATER_LT)
    for sx in (-56, 56):
        solid(rect(x0+sx-4.5, g+28, x0+sx+4.5, g+118), WOOD, W, sd=(-3, 0), sh=0.15)
    roof = [(x0-92, g+106), (x0, g+168), (x0+92, g+106), (x0+82, g+98), (x0, g+152), (x0-82, g+98)]

    def shingles():
        for k in range(1, 7):
            stroke([(x0-92+k*12, g+106+k*8.1), (x0-4, g+106+k*8.1+3)], W*0.4)
            stroke([(x0+92-k*12, g+106+k*8.1), (x0+4, g+106+k*8.1+3)], W*0.4)
    solid(roof, SHINGLE, W, sh=0.15, deco=shingles)
    solid(rect(x0-4, g+138, x0+4, g+152), WOOD_LT, W*0.6, sh=0)
    solid(rect(x0-10, g+56, x0+10, g+72), Col(0.9, "#efe2bf"), W*0.6, sh=0.1)
    solid([(x0+70, g+14), (x0+116, g+6), (x0+116, g+13), (x0+71, g+21)], WOOD_LT, W*0.8, sh=0.12)
    stroke(bez((x0+116, g+9), (x0+123, g+6), (x0+125, g-2), (x0+125, g-12)), W*1.8, g=WATER)
    solid([(x0+104, g-14), (x0+150, g-14), (x0+146, g-2), (x0+108, g-2)], WOOD, W*0.8, sh=0.12)
    stroke([(x0+110, g-4), (x0+144, g-4)], W*0.8, g=WATER_LT)
    rock(x0-120, f(x0-120)-3, 50, 22, 8, ROCK_DK, moss=MOSS)
    for x, s, cap, sp in ((x0+180, 1.3, MUSH_CAP, False), (x0+196, 0.9, MUSH_CAP, False), (x0-160, 1.1, MUSH_RED, True),
                          (380, 1.0, MUSH_CAP, False), (840, 1.2, MUSH_RED, True)):
        mushroom(x, f(x)-4, s, cap, sp)
    for x, c in ((x0-90, FERN), (300, FERN), (880, FERN_RUST)):
        fern_clump(x, f(x)-3, 1.2, c)
    trail(Col(0.7, "#b99469"), 5, pebbles=0, grass=MOSS_DK)
    litter(40, 180, 950, 70, 185, 17, (NEEDLES, MOSS_DK, FLOOR_DK), 1.6)


def baba(b):
    sky(y0=260)
    cloud(560, 500, 0.8)
    slope = lambda x: 246 + 150*(max(0, x-300)/660)**1.3
    treeline(lambda x: slope(x)+70, [HAZE_GOLD, HAZE_RUST, HAZE], 41, x0=240, step=12, hmin=36, hmax=56, spruce_p=0.2, line=0, base=HAZE_GOLD, rows=2)
    treeline(lambda x: slope(x)+22, [MID_GOLD, MID_RUST, MID_GOLD, MID_SPRUCE], 42, x0=-20, step=14, hmin=44, hmax=66, spruce_p=0.15, line=0.5, base=MID_GOLD, rows=3, drop=18)
    land(lambda x: slope(x)-22, SLOPE, W*0.6)
    far_trees((300, 380, 760, 830), lambda x: slope(x)-26, 150, 34, [BEECH, BEECH_LT, COPPER], BEECH_BARK, HAZE_GOLD, 0.2, 43)
    beech(170, 226, 200, 52, 1, trunk_w=10)
    f = fg(LITTER, 204, 43, edge=(FLOOR, 10))
    g = 212
    beech(600, g, 320, 172, 7, (BEECH, BEECH_LT, COPPER, MAPLE_OR), ry=122, trunk_w=24)
    for sx in (-60, -30, 30, 60):
        solid(rect(600+sx-2.5, g-8, 600+sx+2.5, g+22), WOOD, W*0.8, sh=0)
    for yy in (g+8, g+18):
        stroke([(534, yy), (666, yy)], W*2.6); stroke([(534, yy), (666, yy)], W*1.2, g=WOOD_LT)
    solid(rect(700, g-10, 704, g+10), WOOD, W*0.6, sh=0)
    solid(rect(686, g+6, 718, g+30), Col(0.85, "#e9dcb8"), W*0.7, sh=0.1)
    for k in range(3):
        stroke([(691, g+24-k*6), (713, g+24-k*6)], W*0.5, g=WOOD_DK)
    big_trunk(935, 190, 30, BEECH_BARK, 9)
    foliage(955, 520, 110, 70, [BEECH, BEECH_LT, COPPER], 44)
    trail(Col(0.85, "#ecc98f"), 6, grass=FLOOR)
    litter(70, 0, 960, 70, 198, 19)
    litter(30, 0, 960, 4, 60, 20, (COPPER, BEECH), 2.6)
    falling(14, 21)


def loze(b):
    sky(SKY_WARM, SKY_WARM_LOW, y0=200)
    f1 = wf(312, 14, 50, 380)
    treeline(f1, [Col(0.8, "#d9b98a"), Col(0.78, "#c9a57a"), Col(0.75, "#b7a888")], 51, step=10, hmin=24, hmax=40, spruce_p=0.4, line=0, base=Col(0.8, "#d4b48a"), rows=2)
    f2 = wf(264, 10, 52, 320)
    treeline(f2, [MID_GOLD, MID_RUST, MID_SPRUCE, BEECH], 53, step=13, hmin=40, hmax=66, spruce_p=0.3, line=0.5, base=MID_GOLD, rows=2, drop=18)
    land(lambda x: 222 + 22*math.exp(-((x-520)/200)**2), Col(0.75, "#b6b865"), W*0.6)
    spruce(250, 224, 200, SPRUCE, 55); beech(150, 220, 180, 52, 56)
    beech(860, 220, 270, 78, 57, (COPPER, BEECH, BEECH_LT)); spruce(770, 226, 190, SPRUCE_DK, 58)
    cx, cy = 517, 240
    rays(cx, cy, ((40, 9), (62, 7), (84, 10), (106, 7), (128, 9), (150, 6)), 250)
    for k, (rx, ry) in enumerate(((220, 170), (160, 120), (110, 80))):
        fill(ell(cx, cy+20, rx, ry, 40), HALO)
    hole = smooth([(474, 204), (560, 204), (566, 244), (552, 280), (488, 284), (466, 246)], 2)
    fill(ell(cx, cy, 60, 50, 30), GLOW2)
    shape(hole, GLOW, W)
    fill(ell(cx, 226, 34, 20, 20), WHITE)
    rock(410, 204, 210, 176, 61, ROCK, moss=MOSS)
    rock(630, 204, 220, 190, 62, ROCK_DK, moss=MOSS_DK)
    rock(527, 290, 200, 116, 63, ROCK_LT, moss=MOSS)
    shape(ell(cx, 290, 40, 4, 16, 180, 360), shade(ROCK_LT, 0.2), 0)
    rock(380, 196, 150, 70, 64, ROCK_LT)
    rock(672, 196, 160, 84, 65, ROCK)
    rock(517, 192, 120, 16, 66, ROCK_DK, lichen=False, facet=False)
    rock(780, 196, 70, 36, 67, ROCK)
    rock(290, 196, 60, 30, 68, ROCK_LT)
    f = fg(Col(0.72, "#b0b566"), 198, 55, edge=(Col(0.6, "#8e9a4a"), 10))
    for x in (300, 350, 700, 820, 880, 240, 430, 600):
        flower(x, f(x)-3, "heather", 1.4)
    for x, y, rr in ((517, 318, 5), (470, 300, 3.5), (575, 305, 4), (540, 350, 3), (452, 232, 3), (590, 250, 3.5), (420, 360, 2.6), (640, 380, 3)):
        star4(x, y, rr)
    r = random.Random(59)
    for _ in range(16):
        dot(r.uniform(300, 760), r.uniform(200, 440), r.uniform(1.0, 2.0), GLOW2)
    trail(Col(0.85, "#e9cf98"), 7, grass=Col(0.6, "#8e9a4a"))
    tufts(8, 200, 950, 100, 185, 22, Col(0.7, "#a6ad5a"))
    litter(30, 200, 950, 60, 185, 23, (COPPER, BEECH, HEATHER))


# ------------------------------------------------------------------ trail 2
def lsten(b):
    sky()
    cloud(600, 478, 1.3); cloud(820, 500, 0.9); cloud(470, 436, 0.7)
    f1 = wf(334, 20, 70, 520)
    treeline(f1, [FAR, FAR, mix(FAR, FAR_GOLD, 0.35), mix(FAR, FAR_RUST, 0.25)], 71, step=7, hmin=12, hmax=18, line=0, base=FAR, rows=3, drop=12)
    f2 = wf(275, 16, 72, 420)
    land(f2, MEADOW_GOLD, W*0.6)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST], 73, x0=-20, x1=260, step=10, hmin=24, hmax=36, line=0.45, rows=2, drop=12)
    for x, g, w, c in ((600, 262, 44, 0), (650, 258, 36, 1), (705, 262, 48, 3), (760, 256, 34, 4), (805, 262, 40, 5)):
        cottage(x, g, w, w*0.6, WALLS[c], seed=c, line=W*0.7)
    for x in (570, 735, 840):
        leafy(x, 256, 44, 15, [MID_GOLD, MID_GREEN], x, line=W*0.6)
    f3 = wf(240, 5, 74, 360)
    land(f3, MEADOW, W*0.6)
    for x, w, h, s in ((180, 110, 44, 1), (300, 70, 34, 2), (900, 120, 50, 3), (420, 60, 30, 4)):
        bush(x, f3(x)-8, w, h, Col(0.45, "#5f7a45"), s, (SLOE, 12, 2.1), cols=(BUSH_RUST, MID_GOLD))
    f = fg(MEADOW_GREEN, 202, 75, edge=(Col(0.6, "#86a852"), 14))
    trail(seed=8, tongue=(560, 760, 690, 240, 5), grass=Col(0.6, "#86a852"))
    stroke(bez((672, 70), (676, 140), (686, 200), (690, 236)), W*2.4, g=Col(0.6, "#86a852"))
    for x, k in ((230, "chicory"), (260, "tansy"), (330, "chicory"), (520, "tansy"), (548, "chicory"),
                 (820, "tansy"), (848, "chicory"), (900, "tansy"), (930, "chicory"), (440, "tansy")):
        flower(x, f(x)-4, k, 1.1)
    tufts(10, 190, 950, 100, 190, 24, Col(0.6, "#86a852"))


def chlumec(b):
    sky()
    cloud(560, 492, 1.0); cloud(470, 440, 0.6)
    f1 = wf(300, 14, 80, 420)
    treeline(f1, [FAR, FAR, mix(FAR, FAR_GOLD, 0.35)], 81, x0=-20, x1=560, step=7, hmin=12, hmax=18, line=0, base=FAR, rows=3, drop=10)
    hill = lambda x: 256 + 170*max(0, 1-((x-830)/380)**2)
    treeline(hill, [MID_GOLD, MID_RUST, MAPLE_OR, MID_SPRUCE, OAK], 82, x0=440, step=13, hmin=40, hmax=60, spruce_p=0.15, line=0.5, base=MID_RUST, rows=5, drop=32)
    land(wf(238, 5, 83, 360), MEADOW, W*0.6)
    leafy(560, 230, 170, 50, [OAK, MID_GOLD, COPPER], 84, trunk_w=9)
    leafy(690, 232, 220, 62, [MAPLE, MAPLE_OR, BEECH_LT], 85, trunk_w=9)
    leafy(830, 228, 250, 70, [OAK, BEECH, MID_GREEN], 86, trunk_w=11)
    leafy(945, 224, 210, 58, [MAPLE_OR, MAPLE, BEECH], 87, trunk_w=9)
    f = fg(MEADOW_GREEN, 206, 84, edge=(Col(0.6, "#86a852"), 12))
    for x, w, s in ((625, 100, 1), (765, 120, 2), (905, 90, 3)):
        bush(x, f(x)-3, w, 40, Col(0.45, "#6e5a3a"), s, (BRAMBLE, 12, 1.8), cols=(MAPLE, LEAF_GREEN))
    bx, g = 380, f(380)-2
    for sx in (-30, 30):
        solid(rect(bx+sx-3, g, bx+sx+3, g+16), WOOD_DK, W*0.8, sh=0)
        solid(rect(bx+sx-2.5, g+16, bx+sx+2.5, g+40), WOOD_DK, W*0.8, sh=0)
    solid(rect(bx-40, g+14, bx+40, g+20), WOOD, W*0.8, sh=0.1)
    for yy in (g+26, g+34):
        solid(rect(bx-38, yy, bx+38, yy+5), WOOD_LT, W*0.8, sh=0.1)
    solid(rect(466, g, 471, g+56), WOOD, W*0.8, sh=0.1)
    solid([(471, g+42), (505, g+42), (512, g+47), (505, g+52), (471, g+52)], Col(0.9, "#f4e7c3"), W*0.7, sh=0)
    solid([(466, g+28), (432, g+28), (425, g+33), (432, g+38), (466, g+38)], Col(0.9, "#f4e7c3"), W*0.7, sh=0)
    stroke([(478, g+47), (500, g+47)], W*1.6, g=Col(0.4, "#3a8a4a"))
    stroke([(436, g+33), (460, g+33)], W*1.6, g=Col(0.4, "#3a8a4a"))
    trail(seed=9, grass=Col(0.6, "#86a852"))
    tufts(10, 200, 950, 100, 195, 25, Col(0.6, "#86a852"))
    litter(25, 450, 950, 150, 200, 26, (MAPLE, OAK, BEECH))
    falling(8, 27, 520, 950, 230, 440, (MAPLE, OAK, MAPLE_OR))


def palouky(b):
    sky(y0=240)
    cloud(650, 488, 1.1); cloud(860, 460, 0.8)
    f1 = wf(345, 12, 90, 420)
    treeline(f1, [FAR, FAR2], 91, step=7, hmin=12, hmax=18, line=0, base=FAR, rows=2, drop=10)
    f2 = wf(266, 10, 92, 300)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_SPRUCE, MID_RUST], 93, step=12, hmin=46, hmax=76, spruce_p=0.55, line=0.5, base=MID_SPRUCE, rows=2, drop=16)
    land(wf(242, 3, 94, 300), MEADOW_GOLD, W*0.6)
    hx, g = 700, 246
    for dx0, dx1 in ((-16, -9), (16, 9)):
        stroke([(hx+dx0, g), (hx+dx1, g+62)], W*3.2); stroke([(hx+dx0, g), (hx+dx1, g+62)], W*1.6, g=WOOD)
    for k in range(6):
        yy = g+6+k*9
        stroke([(hx-13+k*0.6, yy), (hx+13-k*0.6, yy)], W*1.8); stroke([(hx-13+k*0.6, yy), (hx+13-k*0.6, yy)], W*0.7, g=WOOD_LT)
    solid(rect(hx-14, g+62, hx+14, g+84), WOOD, W*0.8, sh=0.15)
    solid(rect(hx-8, g+70, hx+8, g+79), Col(0.2, "#2f2a26"), W*0.5, sh=0)
    solid([(hx-19, g+83), (hx+19, g+83), (hx+14, g+96), (hx-14, g+96)], SHINGLE, W*0.8, sh=0.1)
    mist(236, 262, 95)
    far_trees((500, 580), lambda x: 244, 140, 36, [BEECH, BEECH_LT, COPPER], BEECH_BARK, HAZE_GOLD, 0.2, 97)
    for x, h, s in ((60, 225, 1), (160, 200, 2), (850, 300, 3), (770, 230, 4)):
        spruce(x, 226, h, SPRUCE if s % 2 else SPRUCE_DK, s)
    beech(310, 228, 190, 52, 4)
    beech(935, 222, 260, 72, 6)
    f = fg(MEADOW, 206, 96, edge=(MEADOW_GOLD, 16))
    trail(Col(0.85, "#e3cd9a"), 10, grass=MEADOW_GOLD)
    tufts(14, 190, 950, 100, 200, 28, MEADOW_GOLD)
    for x in (270, 520, 880):
        mushroom(x, f(x)-5, 1.1, MUSH_CAP)


def hrebeny(b):
    sky(y0=240)
    cloud(620, 495, 1.0)
    for i, (y, c) in enumerate(((306, FAR), (276, FAR2), (250, Col(0.7, "#88a3b4")))):
        land(wf(y, 12, 100+i, 320), c, 0, -10, 560)
    ridge = lambda x: 256 + max(0, x-380)*0.22
    treeline(ridge, [MID_SPRUCE, MID_GOLD, FIR, MID_RUST], 105, x0=330, step=12, hmin=50, hmax=84, spruce_p=0.45, line=0.5, base=MID_SPRUCE, rows=4, drop=22)
    land(wf(234, 4, 106, 300), SLOPE, W*0.6)
    far_trees((380, 610), lambda x: 236, 190, 44, [BEECH, BEECH_LT, COPPER], BEECH_BARK, HAZE_GOLD, 0.2, 107)
    spruce(560, 228, 290, FIR, 1, fir=True)
    beech(690, 230, 290, 72, 2)
    spruce(800, 228, 330, FIR, 3, fir=True)
    beech(230, 222, 190, 50, 4, (COPPER, BEECH, BEECH_LT))
    tx = 455
    leafy(tx, 214, 250, 64, [BEECH, BEECH_LT, COPPER], 8, BEECH_BARK, ry=58, trunk_w=13)
    for k, c in enumerate((WHITE, MARK_RED, WHITE)):
        solid(rect(tx-8, 266-k*5.5, tx+8, 271.5-k*5.5), c, W*0.5, sh=0)
    big_trunk(925, 190, 36, BEECH_BARK, 9)
    foliage(960, 500, 115, 80, [BEECH_LT, BEECH, COPPER], 10)
    f = fg(LITTER, 200, 107, edge=(FLOOR, 10))
    for x in (320, 620, 760):
        rock(x, f(x)-3, 40, 18, x, ROCK, W*0.8)
    trail(Col(0.82, "#e3c38e"), 11, grass=FLOOR)
    for pts in (bez((150, 30), (240, 44), (300, 22), (380, 30)), bez((700, 20), (760, 36), (820, 30), (880, 14))):
        stroke(pts, W*3.4); stroke(pts, W*1.8, g=WOOD)
    litter(60, 0, 960, 70, 195, 30)
    falling(10, 31)


def vrch(b):
    sky(Col(0.9, "#c7dff0"), Col(0.97, "#fbf0d6"), y0=200)
    cloud(820, 480, 1.1); cloud(470, 450, 0.7)
    for i, (y, c) in enumerate(((330, Col(0.85, "#bccde0")), (300, FAR), (268, FAR2))):
        f = wf(y, 16, 110+i, 360)
        treeline(f, [c], 120+i, step=7, hmin=8, hmax=13, line=0, base=c)
    f2 = wf(242, 8, 113, 300)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST, MID_GOLD], 114, step=11, hmin=36, hmax=58, spruce_p=0.4, line=0.5, base=MID_GOLD, rows=2, drop=14)
    land(wf(228, 3, 115, 300), Col(0.7, "#b4b36a"), W*0.6)
    spruce(400, 222, 200, SPRUCE, 1); beech(320, 218, 170, 48, 2); spruce(170, 224, 170, SPRUCE_DK, 6)
    x, g, tw = 540, 214, 36
    tower = [(x-tw-2, g), (x+tw+2, g), (x+tw, g+200), (x-tw, g+200)]

    def stones():
        r = random.Random(116)
        yy = g; row = 0
        while yy < g+200:
            hh = r.uniform(11, 15); xx = x-tw-6 - (row % 2)*9
            while xx < x+tw+6:
                ww = r.uniform(14, 22)
                shape(rrect(xx+1, yy+1, ww-2, hh-2, 3), r.choice((STONE, Col(0.75, "#c2b9a4"), Col(0.82, "#d8d0bd"))), W*0.45)
                xx += ww
            yy += hh; row += 1
    solid(tower, STONE, W, sd=(-18, 0), sh=0.16, deco=stones)
    solid(bez((x-10, g), (x-10, g+30), (x+10, g+30), (x+10, g)), WOOD_DK, W*0.8, sh=0)
    for wy in (g+90, g+150):
        solid(bez((x-5, wy), (x-5, wy+16), (x+5, wy+16), (x+5, wy)), Col(0.2, "#2f2a26"), W*0.6, sh=0)
    solid(rect(x-tw-8, g+196, x+tw+8, g+206), STONE, W, sh=0.1)
    for px in range(-tw-4, tw+8, 12):
        solid(rect(x+px-2, g+206, x+px+2, g+240), WOOD, W*0.7, sh=0)
    for yy in (g+218, g+230):
        solid(rect(x-tw-8, yy, x+tw+8, yy+3.5), WOOD_LT, W*0.6, sh=0)
    rf = [(x-tw-22, g+238), (x, g+292), (x+tw+22, g+238)]
    solid(rf, ROOF, W, sd=(-18, 0), sh=0.15)
    for k in range(1, 5):
        yy = g+238+k*10.5
        stroke([(x-tw-22+k*11.2, yy), (x+tw+22-k*11.2, yy)], W*0.5)
    stroke([(x, g+292), (x, g+308)], W*1.2)
    solid([(x, g+308), (x+16, g+303), (x, g+298)], MARK_RED, W*0.6, sh=0)
    beech(760, 222, 270, 78, 3); spruce(870, 220, 300, SPRUCE_DK, 4); beech(950, 216, 220, 60, 5, (COPPER, BEECH))
    f = fg(Col(0.66, "#a9aa60"), 200, 117, edge=(Col(0.55, "#8a9148"), 10))
    for x0 in (420, 690):
        rock(x0, f(x0)-3, 46, 22, x0, ROCK)
    trail(Col(0.85, "#e3c898"), 12, grass=Col(0.55, "#8a9148"))
    tufts(10, 200, 950, 100, 190, 32, Col(0.6, "#9aa050"))
    litter(30, 200, 950, 60, 190, 33)


# ------------------------------------------------------------------ trail 3
def kuchynka(b):
    sky(y0=260)
    cloud(700, 492, 0.9)
    dome = lambda x: 272 + 72*math.exp(-((x-620)/300)**2)
    treeline(lambda x: dome(x)+40, [HAZE_GOLD, HAZE_RUST, HAZE], 130, step=12, hmin=36, hmax=60, spruce_p=0.15, line=0, base=HAZE_GOLD, rows=2)
    treeline(dome, [MID_GOLD, MID_RUST, BEECH, MID_GOLD], 131, step=14, hmin=50, hmax=76, spruce_p=0.1, line=0.5, base=MID_GOLD, rows=3, drop=20)
    land(lambda x: dome(x)-44, SLOPE, W*0.6)
    far_trees((330, 420, 800), lambda x: dome(x)-48, 170, 40, [BEECH, BEECH_LT, COPPER], BEECH_BARK, HAZE_GOLD, 0.2, 132)
    outcrop(470, 232, 150, 100, 1, ROCK)
    outcrop(640, 236, 150, 90, 3, ROCK_DK)
    outcrop(560, 224, 180, 150, 2, ROCK_LT)
    outcrop(390, 222, 80, 46, 4, ROCK_DK)
    outcrop(730, 226, 90, 50, 5, ROCK)
    beech(210, 222, 210, 58, 6, trunk_w=10)
    beech(840, 226, 270, 74, 8, trunk_w=12)
    beech(935, 220, 300, 80, 9, (COPPER, BEECH, BEECH_LT), trunk_w=14)
    f = fg(Col(0.72, "#d3bb86"), 204, 132, edge=(Col(0.55, "#a99a5a"), 10))
    for x in (300, 470, 650, 880):
        rock(x, f(x)-3, 50, 24, x, ROCK)
    trail(Col(0.84, "#e8c894"), 13, grass=FLOOR)
    litter(70, 0, 960, 70, 198, 34)
    falling(12, 35)


def sut(b):
    sky(y0=260)
    cloud(560, 488, 0.9); cloud(800, 505, 0.7)
    slope = lambda x: 236 + 190*(max(0, x-180)/780)**1.1
    treeline(lambda x: slope(x)+30, [MID_SPRUCE, FIR, MID_GOLD], 140, step=12, hmin=50, hmax=80, spruce_p=0.7, line=0.5, base=MID_SPRUCE, rows=2, drop=14)
    land(slope, Col(0.7, "#b4ad98"), W*0.6)
    r = random.Random(141)
    stones = []
    for i in range(70):
        x = r.uniform(200, 980)
        y0 = 205 + (slope(x)-205)*r.uniform(0.0, 0.95)
        k = 1.0 - 0.55*(y0-200)/260
        stones.append((y0, x, r.uniform(34, 62)*k, r.uniform(16, 30)*k, i))
    for y0, x, w, h, i in sorted(stones, reverse=True):
        rock(x, y0, w, h, 200+i, r.choice((ROCK, ROCK_LT, ROCK_DK)), W*(0.6 + 0.4*max(0, (260-y0)/60)))
    for x, h, s, fir in ((120, 225, 1, False), (40, 228, 2, True), (240, 200, 3, True)):
        spruce(x, 222, h, SPRUCE if s % 2 else FIR, s, fir=fir)
    spruce(930, 205, 320, SPRUCE_DK, 4)
    f = fg(MOSS_LT, 198, 142, edge=(MOSS, 10))
    for x in (380, 520, 700, 820):
        rock(x, f(x)-3, 60, 30, x+1, ROCK_LT, moss=MOSS)
    fern_clump(300, f(300)-3, 1.2, FERN_RUST); fern_clump(610, f(610)-3, 1.1, FERN)
    trail(Col(0.8, "#d6c194"), 14, grass=MOSS)
    tufts(8, 200, 950, 100, 185, 36, MOSS)
    litter(30, 200, 950, 60, 190, 37, (NEEDLES, MOSS_DK, BEECH))


def provazec(b):
    sky(Col(0.88, "#c3d6cf"), Col(0.94, "#e7ecd9"), y0=220)
    for i, (y, c, hh) in enumerate(((300, Col(0.75, "#a3bab0"), (70, 130)), (258, Col(0.6, "#7b9887"), (90, 170)))):
        f = wf(y, 10, 150+i, 300)
        land(f, c, 0)
        r = random.Random(160+i); x = -20
        while x < 990:
            h = r.uniform(*hh)
            fill(spruce_pts(x, f(x)-5, h*0.36, h, int(h/10), r.randrange(99)), c)
            x += r.uniform(20, 36)
    rays(560, 580, ((240, 5), (258, 4)), 520)
    land(wf(234, 3, 152, 300), NEEDLES, W*0.6)
    for x, h, s in ((300, 225, 1), (440, 330, 2), (650, 350, 3), (760, 300, 4), (170, 215, 5), (560, 260, 6)):
        spruce(x, 230, h, SPRUCE_DK if s % 2 else FIR, s, fir=s == 2)
    spruce(1005, 176, 620, SPRUCE_DK, 7, w=340)
    f = fg(Col(0.55, "#7f9a48"), 200, 153, edge=(MOSS_DK, 10))
    log(170, 470, f(300)-4, 14, 170)
    for x, w, h in ((600, 110, 62), (800, 130, 72)):
        g = f(x)-4
        hill = [(x-w/2, g)] + bez((x-w/2, g), (x-w*0.35, g+h*1.3), (x+w*0.35, g+h*1.3), (x+w/2, g))
        r = random.Random(x)

        def grains(x=x, g=g, w=w, h=h, r=r):
            for _ in range(180):
                fill(ell(r.uniform(x-w/2, x+w/2), r.uniform(g, g+h), 1.6, 0.6, 6, rot=r.uniform(0, 180)), r.choice((ANTHILL_DK, WOOD_LT)))
        solid(hill, ANTHILL, W, sd=(-w*0.18, h*0.1), sh=0.16, deco=grains)
        for k in range(6):
            dot(x+r.uniform(-w*0.4, w*0.4), g+r.uniform(3, h*0.8), 0.9, Col(0.1, "#1b1b1b"))
    stump(700, f(700)-4, 34, 26)
    for x in (360, 520):
        mushroom(x, f(x)-4, 1.2, MUSH_RED, True)
    fern_clump(250, f(250)-3, 1.3, FERN); fern_clump(890, f(890)-3, 1.2, FERN)
    trail(Col(0.7, "#b99469"), 15, pebbles=0, grass=MOSS_DK)
    litter(60, 0, 960, 60, 192, 38, (NEEDLES, WOOD_DK, MOSS), 1.6)


def zed(b):
    sky(Col(0.9, "#c9dde6"), Col(0.95, "#eef0dd"), y0=230)
    f1 = wf(310, 12, 170, 320)
    treeline(f1, [Col(0.78, "#b0c3bd"), Col(0.78, "#c9c09a")], 171, step=11, hmin=40, hmax=70, spruce_p=0.5, line=0, base=Col(0.78, "#b0c3bd"))
    f2 = wf(270, 10, 172, 300)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST, MID_SPRUCE], 173, step=13, hmin=50, hmax=86, spruce_p=0.5, line=0.5, base=MID_SPRUCE, rows=2, drop=16)
    mist(250, 300, 174)
    land(wf(244, 3, 175, 300), SLOPE, W*0.6)
    far_trees((420, 620), lambda x: 246, 170, 42, [BEECH, BEECH_LT, COPPER], BEECH_BARK, HAZE, 0.2, 176)
    spruce(520, 244, 200, mix(SPRUCE, HAZE, 0.25), 6, line=W*0.7)
    spruce(760, 244, 230, mix(SPRUCE, HAZE, 0.2), 7, line=W*0.7)
    spruce(880, 240, 260, SPRUCE, 1); spruce(150, 236, 210, SPRUCE_DK, 2)
    beech(960, 232, 290, 74, 5)
    f = fg(Col(0.6, "#8fa24c"), 200, 177, edge=(MOSS_DK, 12))
    x0, x1 = 240, 905
    yb = lambda x: 208 + (x-x0)*0.065
    hw = lambda x: 82 - (x-x0)*0.075
    top = lambda x: yb(x) + hw(x) + 2.5*math.sin(x/23) - int(max(0, 72-(x-x0))/18)*13 - (12 if 545 < x < 585 else 0)
    wall = [(x0, yb(x0))] + [(x, top(x)) for x in range(x0, x1+1, 4)] + [(x1, yb(x1))]
    r = random.Random(176)

    def stones():
        xx0 = x0 - 20
        for row in range(9):
            xx = xx0 - r.uniform(0, 20)
            while xx < x1:
                k = hw(xx)/82
                ww = r.uniform(24, 44)*k
                rh = hw(xx)/7.2
                y0 = yb(xx) + row*rh
                hh = rh*r.uniform(0.75, 1.0)
                j = lambda: r.uniform(-0.12, 0.12)*hh
                pts = [(xx+1, y0+1+j()), (xx+ww-1, y0+1+j()), (xx+ww-1-r.uniform(0, 3)*k, y0+hh-1+j()), (xx+1+r.uniform(0, 3)*k, y0+hh-1+j())]
                shape(smooth(pts, 1), r.choice((ROCK, ROCK_LT, ROCK_DK, Col(0.7, "#b3aa96"), Col(0.62, "#9d998c"))), W*0.55)
                if r.random() < 0.25:
                    fill(blob(xx+ww*0.5, y0+hh*0.75, ww*0.3, hh*0.2, int(xx), 6), r.choice((MOSS, LICHEN, MOSS_DK)))
                xx += ww
    solid(wall, shade(ROCK_DK, 0.3), W, sd=(0, -10), sh=0.18, deco=stones)
    for x in range(x0+50, x1, 22):
        m = blob(x+11, top(x+11)+1, 16*hw(x)/82+4, 4.5, x, 7)
        fill(m, MOSS); stroke(m, W*0.5, closed=True)
    for x, w, h, s in ((x0-6, 44, 30, 1), (x0-40, 30, 18, 2), (x0+10, 26, 14, 3), (565, 30, 12, 4)):
        rock(x, (f(x)-3) if x < 400 else yb(x)-2, w, h, 300+s, ROCK, moss=MOSS)
    bush(x1+10, yb(x1)-6, 90, 50, MID_SPRUCE, 5, cols=(MID_GOLD,))
    for x, s, c, fl in ((330, 1.2, FERN, True), (480, 1.0, FERN_RUST, False), (690, 1.1, FERN, True), (820, 1.2, FERN_RUST, False)):
        fern_clump(x, yb(x)-2, s, c)
    for x, y, rr in ((520, 310, 3.5), (700, 322, 3), (360, 300, 2.8), (610, 296, 2.4)):
        star4(x, y, rr)
    trail(Col(0.8, "#d8bd8c"), 16, grass=MOSS_DK)
    litter(50, 0, 960, 60, 192, 40)
    falling(8, 41)


# ------------------------------------------------------------------ title
def town_house(x, g, w, h, wall, roof=ROOF, kind="gable", seed=1, line=W):
    if kind == "gable":
        body = [(x-w/2, g), (x+w/2, g), (x+w/2, g+h), (x+w*0.3, g+h), (x+w*0.3, g+h+w*0.2), (x+w*0.1, g+h+w*0.42),
                (x-w*0.1, g+h+w*0.42), (x-w*0.3, g+h+w*0.2), (x-w*0.3, g+h), (x-w/2, g+h)]
        solid([(x-w/2-4, g+h-4), (x+w/2+4, g+h-4), (x+w*0.3, g+h+w*0.2), (x-w*0.3, g+h+w*0.2)], roof, line, sh=0.12)
        solid(body, wall, line, sd=(-w*0.08, 0), sh=0.1)
        shape(ell(x, g+h+w*0.22, w*0.07, w*0.07, 14), WINDOW, line*0.6)
        stroke([(x-w*0.1, g+h+w*0.42), (x+w*0.1, g+h+w*0.42)], line*2.4, g=roof)
    else:
        solid([(x-w/2-5, g+h-3), (x+w/2+5, g+h-3), (x+w/2-w*0.12, g+h+w*0.36), (x-w/2+w*0.12, g+h+w*0.36)], roof, line, sh=0.14)
        solid(rect(x-w/2, g, x+w/2, g+h), wall, line, sd=(-w*0.08, 0), sh=0.1)
        solid([(x-8, g+h+w*0.1), (x+8, g+h+w*0.1), (x+8, g+h+w*0.22), (x, g+h+w*0.3), (x-8, g+h+w*0.22)], wall, line*0.7, sh=0)
        shape(rect(x-4, g+h+w*0.12, x+4, g+h+w*0.2), WINDOW, line*0.5)
    stroke([(x-w/2, g+h*0.52), (x+w/2, g+h*0.52)], line*0.6)
    cols = max(2, int(w/22))
    for row, wy in enumerate((g+h*0.62, g+h*0.2)):
        for c in range(cols):
            wx = x - w/2 + w*(c+0.5)/cols
            if row == 1 and c == cols//2:
                solid(bez((wx-6, g), (wx-6, g+h*0.36), (wx+6, g+h*0.36), (wx+6, g)), WOOD, line*0.7, sh=0)
                continue
            solid(rect(wx-5, wy, wx+5, wy+h*0.22), WINDOW, line*0.6, sh=0)
            stroke([(wx, wy), (wx, wy+h*0.22)], line*0.5, g=WHITE)
            stroke([(wx-7, wy-1), (wx+7, wy-1)], line*1.4, g=WHITE)


def title(b):
    sky(y0=200)
    cloud(860, 470, 1.1)
    f1 = wf(270, 14, 180, 420)
    treeline(f1, [FAR, FAR, mix(FAR, FAR_GOLD, 0.35)], 181, step=7, hmin=12, hmax=18, line=0, base=FAR, rows=2, drop=10)
    baba_f = lambda x: 225 + 95*math.exp(-((x-780)/150)**2)
    treeline(baba_f, [HAZE, HAZE_GOLD, HAZE_RUST, MID_SPRUCE], 182, x0=520, step=9, hmin=16, hmax=26, spruce_p=0.5, line=0.4, base=HAZE, rows=4, drop=16)
    f2 = wf(220, 8, 183, 300)
    treeline(f2, [MID_SPRUCE, MID_GOLD, MID_RUST, MID_GREEN], 184, step=11, hmin=26, hmax=40, line=0.45, base=MID_GREEN, rows=2, drop=12)
    land(wf(186, 3, 185, 300), MEADOW, W*0.6)
    cx, cg = 150, 190
    solid([(cx+20, cg+90), (cx+130, cg+90), (cx+110, cg+140), (cx+30, cg+140)], ROOF_DK, W, sh=0.12)
    solid(rect(cx+20, cg, cx+130, cg+90), Col(0.95, "#fbf3e2"), W, sh=0.1)
    for wx in (cx+45, cx+80, cx+112):
        solid(bez((wx-5, cg+30), (wx-5, cg+68), (wx+5, cg+68), (wx+5, cg+30)), WINDOW, W*0.6, sh=0)
    tx, tw = cx, 26
    solid(rect(tx-tw, cg, tx+tw, cg+220), Col(0.95, "#fbf3e2"), W, sd=(-10, 0), sh=0.12)
    for yy in (cg+120, cg+170):
        stroke([(tx-tw, yy), (tx+tw, yy)], W*0.7)
    solid(bez((tx-7, cg+178), (tx-7, cg+205), (tx+7, cg+205), (tx+7, cg+178)), Col(0.2, "#2f2a26"), W*0.6, sh=0)
    shape(ell(tx, cg+140, 11, 11, 24), Col(0.95, "#fff8e6"), W*0.7)
    stroke([(tx, cg+140), (tx, cg+147)], W*0.8); stroke([(tx, cg+140), (tx+5, cg+140)], W*0.8)
    dome = bez((tx-tw-4, cg+220), (tx-tw-6, cg+248), (tx-8, cg+250), (tx-5, cg+262)) + \
        bez((tx-5, cg+262), (tx-14, cg+272), (tx-6, cg+288), (tx, cg+296)) + \
        bez((tx, cg+296), (tx+6, cg+288), (tx+14, cg+272), (tx+5, cg+262)) + \
        bez((tx+5, cg+262), (tx+8, cg+250), (tx+tw+6, cg+248), (tx+tw+4, cg+220))
    solid(dome, Col(0.4, "#4f7f6a"), W, sd=(-8, 0), sh=0.15)
    stroke([(tx, cg+296), (tx, cg+318)], W*1.3)
    stroke([(tx-6, cg+310), (tx+6, cg+310)], W*1.3)
    g = 150
    for x, w, h, c, k in ((-10, 90, 120, 2, "eaves"), (80, 80, 110, 0, "gable"), (160, 90, 96, 1, "eaves"), (248, 76, 104, 3, "gable")):
        town_house(x+w/2, g, w, h, WALLS[c], ROOF if c % 2 else ROOF_DK, k, c)
    for x, w, h, c, k in ((790, 80, 98, 4, "gable"), (872, 96, 112, 5, "eaves")):
        town_house(x+w/2, g, w, h, WALLS[c], ROOF, k, c+10)
    for x in (365, 700):
        leafy(x, 146, 150, 46, [BEECH_LT, BEECH, MID_GREEN], x, trunk_w=7)
    land(lambda x: 150, COBBLE, W)
    for j in range(7):
        yy = 150 - 21*(j+1)
        for i in range(-1, 18):
            stroke(ell(i*60 + (j % 2)*30, yy, 30, 18, 12, 30, 150), W*0.45, g=COBBLE_LN)
    for x in (40, 910):
        bush(x, 146, 60, 30, BUSH, x, cols=(BEECH, MAPLE_OR))
    falling(10, 187, 280, 940, 180, 320)


ASSETS = [(n, 960, 540, fn, "bg") for n, fn in (
    ("zator", zator), ("chumava", chumava), ("brdlavka", brdlavka), ("baba", baba), ("loze", loze),
    ("lsten", lsten), ("chlumec", chlumec), ("palouky", palouky), ("hrebeny", hrebeny), ("vrch", vrch),
    ("kuchynka", kuchynka), ("sut", sut), ("provazec", provazec), ("zed", zed), ("title", title))]
