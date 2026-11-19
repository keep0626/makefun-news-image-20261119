#!/usr/bin/env python3
"""Build 1024x1024 news infographic for 19 Nov 2026. Deterministic, no network."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W, H = 1024, 1024
BG = (13, 20, 36)
PANEL = (24, 33, 56)
PANEL2 = (30, 41, 66)
WHITE = (255, 255, 255)
MUTED = (203, 213, 225)
ACCENTS = [(239, 68, 68), (249, 115, 22), (234, 179, 8), (34, 197, 94), (59, 130, 246), (168, 85, 247)]

def font(name, size):
    p = f"/usr/share/fonts/truetype/dejavu/{name}"
    return ImageFont.truetype(p, size)

F_TITLE = font("DejaVuSans-Bold.ttf", 44)
F_SUB = font("DejaVuSans-Bold.ttf", 20)
F_TAG = font("DejaVuSans-Bold.ttf", 17)
F_HEAD = font("DejaVuSans-Bold.ttf", 26)
F_BODY = font("DejaVuSans.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 15)

stories = [
    ("1  SUMMIT IN SHENZHEN", "Trump, Xi & Putin meet",
     "First US-China-Russia trilateral summit opens in Shenzhen. Leaders announce a 'peace declaration' after 90-minute talks."),
    ("2  IRAN WAR ESCALATES", "Tankers on fire in Hormuz",
     "Iran widens attacks on Kuwait and Bahrain. Three oil tankers catch fire after hitting mines east of the Strait of Hormuz."),
    ("3  UKRAINE", "Kerch Bridge hit again",
     "Third Ukrainian strike in four days halts rail traffic on Russia's Kerch Bridge to Crimea."),
    ("4  MIDDLE EAST", "Riyadh tower hit",
     "Houthi missile damages Saudi wealth-fund tower in Riyadh. Israeli forces launch an operation near Gaza's Nuseirat camp despite the ceasefire."),
    ("5  WORLD COURT", "Myanmar: genocide ruling",
     "UN court rules Myanmar committed state-sponsored genocide against the Rohingya — the first ruling of its kind."),
    ("6  GTA VI LAUNCHES", "After a 13-year wait",
     "Grand Theft Auto VI launches worldwide on PS5 and Xbox. Pre-orders top $1.6bn; 17m copies sold. Price $79.99."),
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
# header
d.rectangle([0, 0, W, 118], fill=(185, 28, 28))
d.text((28, 18), "WORLD NEWS", font=F_TITLE, fill=WHITE)
d.text((28, 72), "THURSDAY  19  NOVEMBER  2026  •  6 STORIES IN ONE IMAGE", font=F_SUB, fill=(254, 215, 170))
d.text((W-28, 28), "19 NOV", font=font("DejaVuSans-Bold.ttf", 30), fill=WHITE, anchor="ra")

# grid 2x3
mx, my = 24, 138
gw, gh = 476, 258
gapx, gapy = 24, 18
for i, (tag, head, body) in enumerate(stories):
    col, row = i % 2, i // 2
    x = mx + col * (gw + gapx)
    y = my + row * (gh + gapy)
    accent = ACCENTS[i]
    d.rounded_rectangle([x, y, x+gw, y+gh], radius=14, fill=PANEL, outline=(51, 65, 85), width=1)
    d.rounded_rectangle([x, y, x+gw, y+10], radius=5, fill=accent)
    d.text((x+18, y+22), tag, font=F_TAG, fill=accent)
    # headline wrapped
    lines = textwrap.wrap(head, width=24)
    yy = y + 52
    for ln in lines[:2]:
        d.text((x+18, yy), ln, font=F_HEAD, fill=WHITE)
        yy += 32
    # body wrapped
    blines = textwrap.wrap(body, width=38)
    yy += 6
    for ln in blines[:4]:
        d.text((x+18, yy), ln, font=F_BODY, fill=MUTED)
        yy += 26

# footer
d.text((28, H-38), "Sources: AP • Reuters • WSJ • NDTV • Just Security  |  19 Nov 2026", font=F_FOOT, fill=(148, 163, 184))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), img.size)
