#!/usr/bin/env python3
"""Build entry.png: a 1024x1024 newspaper front page summing up the
world news of Thursday 19 November 2026.

Panels (AI-generated, text-free) live in the sibling work directory;
this script composites them with PIL-drawn headlines into one image.
Run from this directory:  python3 build_image.py
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(os.path.dirname(HERE), "news-image-20261119-work")

PANELS = {
    "p1": "media-generation-panel1-gta6-0-aab87eca-c480-4b90-9acf-f0affe73b38a.webp",
    "p2": "media-generation-panel2-shenzhen-v2-0-9fe7d261-4991-4bf3-9a84-2ddb8a92d5a9.webp",
    "p3": "media-generation-panel3-hormuz-0-47aecba3-3239-4f41-b6c6-dfbc6f43d565.webp",
    "p4": "media-generation-panel4-capitol-0-36250251-582d-4939-86b0-b4d343994703.webp",
    "p5": "media-generation-panel5-hague-0-05626884-f5b2-4d39-913e-54958e37eef7.webp",
}

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BLACK = (12, 12, 12)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)
RED = (178, 34, 34)
INK = (20, 20, 24)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_text(draw, text, fnt, max_w):
    """Shrink the font until the text fits max_w; returns (font, text)."""
    size = fnt.size
    while size > 10 and draw.textlength(text, font=fnt) > max_w:
        size -= 1
        fnt = ImageFont.truetype(fnt.path, size)
    return fnt


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(name, box):
    """Center-crop a panel image into box (x, y, w, h).

    Some panels get a focus crop first, so the key detail (the three
    flags in the summit hall, the Capitol statue) survives the wide
    crop instead of shrinking to a speck: fractions are (left, upper,
    right, lower) of the source image.
    """
    img = Image.open(os.path.join(WORK, PANELS[name])).convert("RGB")
    crop = PANEL_CROPS.get(name)
    if crop:
        w, h = img.size
        img = img.crop((int(w * crop[0]), int(h * crop[1]),
                        int(w * crop[2]), int(h * crop[3])))
    return ImageOps.fit(img, (box[2], box[3]), Image.LANCZOS)


# Focus crops: p2 zooms into the middle of the hall so the US / China /
# Russia flags read at thumbnail size; p4 keeps the top of the dome
# (Statue of Freedom) instead of cutting it off.
PANEL_CROPS = {
    "p2": (0.24, 0.05, 0.76, 0.95),
    "p4": (0.0, 0.0, 1.0, 0.72),
}


def caption(draw, x, y, w, title, sub, title_size, sub_size):
    """Draw a headline (bold, wrapped) and a one-line subhead."""
    tf = font(BOLD, title_size)
    lines = wrap(draw, title, tf, w)
    ty = y + 8
    for line in lines:
        draw.text((x, ty), line, font=tf, fill=BLACK)
        ty += tf.size + 4
    sf = font(REG, sub_size)
    sf = fit_text(draw, sub, sf, w)
    draw.text((x, ty + 2), sub, font=sf, fill=GREY)
    return ty + sf.size + 8


def main():
    page = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(page)

    # ---- Masthead -------------------------------------------------
    title_f = font(BOLD, 62)
    draw.text((W // 2, 16), "19 NOVEMBER 2026", font=title_f,
              fill=INK, anchor="ma")
    sub_f = font(BOLD, 24)
    draw.text((W // 2, 92), "THE WORLD IN ONE DAY  ·  THURSDAY",
              font=sub_f, fill=RED, anchor="ma")
    draw.line([(16, 122), (W - 16, 122)], fill=BLACK, width=4)
    draw.line([(16, 128), (W - 16, 128)], fill=BLACK, width=1)

    # ---- Row A: lead story left, two stories right ----------------
    top = 140
    # P1 lead: image 584x380, caption below
    page.paste(panel("p1", (0, 0, 584, 380)), (16, top))
    caption(draw, 16, top + 380, 584,
            "GTA VI LAUNCHES WORLDWIDE",
            "Vice City returns after 13 years", 38, 22)

    # P2
    page.paste(panel("p2", (0, 0, 396, 185)), (612, top))
    caption(draw, 612, top + 185, 396,
            "SHENZHEN SUMMIT", "Trump, Xi and Putin meet", 26, 19)
    # P3
    p3_y = top + 255
    page.paste(panel("p3", (0, 0, 396, 185)), (612, p3_y))
    caption(draw, 612, p3_y + 185, 396,
            "STRAIT OF HORMUZ", "US strikes Qeshm; tankers hit mines", 26, 19)

    draw.line([(16, 652), (W - 16, 652)], fill=BLACK, width=2)

    # ---- Row B: two stories across the bottom --------------------
    bot = 664
    # P4
    page.paste(panel("p4", (0, 0, 484, 190)), (16, bot))
    caption(draw, 16, bot + 190, 484,
            "FIRST BLACK SPEAKER", "Democrats nominate Jeffries", 30, 20)
    # P5
    page.paste(panel("p5", (0, 0, 484, 190)), (524, bot))
    caption(draw, 524, bot + 190, 484,
            "THE HAGUE", "World Court rules on Myanmar case", 30, 20)

    # ---- Ticker ---------------------------------------------------
    draw.rectangle([(0, 952), (W, H)], fill=INK)
    tick = ("Cyclone Akvan nears India's east coast  ·  "
            "Voyager 1 passes one light-day  ·  "
            "EU unveils \u20ac45bn Ukraine loan")
    tf = font(REG, 20)
    tf = fit_text(draw, tick, tf, W - 32)
    draw.text((W // 2, 952 + (72 - tf.size) // 2), tick, font=tf,
              fill=WHITE, anchor="ma")

    out = os.path.join(HERE, "entry.png")
    page.save(out, "PNG", optimize=True)
    print("wrote", out, page.size,
          os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
