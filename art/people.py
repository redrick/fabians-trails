"""The rangers (Alica, Hanka, Tonda) and Joey the dog, reused from the detective-game drawings."""
from style3 import alica, hanka, joey
from chars3 import tonda

S = 2.2


def kid(fn, mood="happy", arms="down", legs="stand", **kw):
    return lambda b: fn(b.w/2, 8, S, left=arms, right=arms, mood=mood, legs=legs, shadow=False, **kw)


ASSETS = []
for name, fn, w, h, extra in (("alica", alica, 130, 245, {}), ("hanka", hanka, 120, 205, {"monkey": False}), ("tonda", tonda, 130, 250, {})):
    ASSETS += [
        (f"{name}_happy", w, h, kid(fn, **extra), "chars"),
        (f"{name}_cheer", w + 20, h + 10, kid(fn, "grin", "up", **extra), "chars"),
        (f"{name}_walk", w, h, kid(fn, legs="walk", **extra), "chars"),
    ]
ASSETS += [
    ("joey_stand", 180, 150, lambda b: joey(70, 8, S, mood="happy", shadow=False), "chars"),
    ("joey_sniff", 190, 150, lambda b: joey(70, 8, S, mood="calm", pose="sniff", shadow=False), "chars"),
    ("joey_bark", 180, 150, lambda b: joey(70, 8, S, mood="bark", shadow=False), "chars"),
]
