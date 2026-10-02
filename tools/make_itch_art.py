"""Compose the itch.io page images from the game art (backdrops, Fabián, Joey, the game font).

Run: art/.venv/bin/python tools/make_itch_art.py  →  docs/itch/
  cover.png       630x500   Edit game → Cover image
  banner.png      960x260   Edit theme → Banner (replaces the page title)
  background.png  2560x1440 Edit theme → Background (no repeat, centred, fixed)
  embed_bg.png    960x540   Edit theme → Embed BG (behind the "Run game" button, same size as the embed)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "game" / "assets"
OUT = ROOT / "docs" / "itch"

SS = 2  # draw at 2x, downscale at the end for smooth edges
BROWN = (122, 62, 29)
GREEN = (93, 107, 88)
CREAM = (255, 250, 240)
FONT = str(ASSETS / "fonts" / "ShantellHandBold.ttf")
TITLE = "Fabiánova stezka"
SUBTITLE = "Fabian's Trail"


def backdrop(name, w, h, anchor_x=1.0, anchor_y=0.0):
    """Scale a 1920x1080 backdrop to cover w x h, cropping around (anchor_x, anchor_y) in 0..1."""
    bg = Image.open(ASSETS / "bg" / f"{name}.png").convert("RGBA")
    scale = max(w / bg.width, h / bg.height)
    bg = bg.resize((round(bg.width * scale), round(bg.height * scale)), Image.LANCZOS)
    left = round((bg.width - w) * anchor_x)
    top = round((bg.height - h) * anchor_y)
    return bg.crop((left, top, left + w, top + h)), scale, left, top


def paste_standing(canvas, name, foot_x, foot_y, scale):
    """Paste a character with its bottom-centre at (foot_x, foot_y), like UI.standing."""
    im = Image.open(ASSETS / "chars" / f"{name}.png").convert("RGBA")
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    canvas.alpha_composite(im, (round(foot_x - im.width / 2), round(foot_y - im.height)))


def outlined_text(canvas, text, size, fill, centre, outline, max_width):
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(FONT, size)
    box = draw.textbbox((0, 0), text, font=font, anchor="mm", stroke_width=outline)
    if box[2] - box[0] > max_width:  # shrink to fit
        return outlined_text(canvas, text, int(size * max_width / (box[2] - box[0])), fill, centre, outline, max_width)
    draw.text(centre, text, font=font, fill=fill, anchor="mm", stroke_width=outline, stroke_fill=CREAM)


def save(canvas, w, h, name):
    out = canvas.resize((w, h), Image.LANCZOS).convert("RGB")
    out.save(OUT / name, optimize=True)
    print(f"wrote docs/itch/{name} ({w}x{h}, {(OUT / name).stat().st_size // 1024} KB)")


def cover():
    W, H = 630, 500
    CW, CH = W * SS, H * SS
    canvas, scale, left, top = backdrop("title", CW, CH)
    # Same spots as the title screen (screens.gd), mapped into the crop.
    def at(x, y):
        return (x * scale - left, y * scale - top)
    fx, fy = at(1560, 1030)
    paste_standing(canvas, "fabian_wave", fx + 40 * SS, fy + 30 * SS, 1.05 * scale * 1.3)
    jx, jy = at(1260, 1040)
    paste_standing(canvas, "joey_stand", jx - 40 * SS, jy + 10 * SS, 0.85 * scale * 1.3)
    outlined_text(canvas, TITLE, 88 * SS, BROWN, (CW / 2, 78 * SS), 7 * SS, CW * 0.94)
    outlined_text(canvas, SUBTITLE, 40 * SS, GREEN, (CW / 2, 140 * SS), 5 * SS, CW * 0.94)
    save(canvas, W, H, "cover.png")


def banner():
    W, H = 960, 260
    CW, CH = W * SS, H * SS
    # The title backdrop's treeline and path, Joey on the left and Fabián on the right, cut off by the bottom edge.
    canvas, *_ = backdrop("title", CW, CH, anchor_x=0.5, anchor_y=0.62)
    paste_standing(canvas, "joey_stand", 88 * SS, CH - 8 * SS, 0.5 * SS)
    paste_standing(canvas, "fabian_wave", 860 * SS, CH + 150 * SS, 0.7 * SS)
    outlined_text(canvas, TITLE, 84 * SS, BROWN, (CW / 2, 105 * SS), 7 * SS, 640 * SS)
    outlined_text(canvas, SUBTITLE, 38 * SS, GREEN, (CW / 2, 175 * SS), 5 * SS, 640 * SS)
    save(canvas, W, H, "banner.png")


def background():
    # Only the sides show around the 960px page column, so keep it quiet: no text, softened, a touch lighter.
    W, H = 2560, 1440
    canvas, *_ = backdrop("hrebeny", W, H, anchor_x=0.5, anchor_y=0.0)
    canvas = canvas.filter(ImageFilter.GaussianBlur(2))
    canvas = ImageEnhance.Color(canvas).enhance(0.85)
    canvas = Image.blend(canvas, Image.new("RGBA", canvas.size, CREAM + (255,)), 0.18)
    save(canvas, W, H, "background.png")


def embed_bg():
    # The "Run game" button sits in the middle, so the centre stays empty: title on top, characters at the sides.
    W, H = 960, 540
    CW, CH = W * SS, H * SS
    canvas, *_ = backdrop("title", CW, CH, anchor_x=0.5)
    paste_standing(canvas, "joey_stand", 150 * SS, CH - 25 * SS, 0.8 * SS)
    paste_standing(canvas, "fabian_wave", 830 * SS, CH - 10 * SS, 0.7 * SS)
    outlined_text(canvas, TITLE, 90 * SS, BROWN, (CW / 2, 80 * SS), 7 * SS, 700 * SS)
    outlined_text(canvas, SUBTITLE, 40 * SS, GREEN, (CW / 2, 150 * SS), 5 * SS, 700 * SS)
    save(canvas, W, H, "embed_bg.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cover()
    banner()
    background()
    embed_bg()


if __name__ == "__main__":
    main()
