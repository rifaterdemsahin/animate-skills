"""Rocket launch emoji GIF, made with the slack-gif-creator skill's core utilities."""
import math, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / ".claude/skills/slack-gif-creator"))
from PIL import Image, ImageDraw
from core.gif_builder import GIFBuilder
from core.easing import interpolate
from core.frame_composer import create_gradient_background
from core.validators import validate_gif

S, N = 128, 24
b = GIFBuilder(width=S, height=S, fps=12)

def rocket(d, cx, cy, ang):
    def rot(x, y):
        c, s = math.cos(ang), math.sin(ang)
        return (cx + x * c - y * s, cy + x * s + y * c)
    body = [rot(0, -30), rot(10, -14), rot(10, 14), rot(-10, 14), rot(-10, -14)]
    d.polygon(body, fill=(236, 240, 255), outline=(40, 44, 80), width=3)
    d.polygon([rot(10, 4), rot(20, 20), rot(10, 14)], fill=(255, 90, 110), outline=(40, 44, 80), width=2)
    d.polygon([rot(-10, 4), rot(-20, 20), rot(-10, 14)], fill=(255, 90, 110), outline=(40, 44, 80), width=2)
    wx, wy = rot(0, -8)
    d.ellipse([wx - 6, wy - 6, wx + 6, wy + 6], fill=(120, 200, 255), outline=(40, 44, 80), width=2)
    return rot(0, 16)

for i in range(N):
    f = create_gradient_background(S, S, (20, 24, 60), (90, 60, 160))
    d = ImageDraw.Draw(f)
    for k in range(14):  # twinkling stars
        x, y = (k * 37) % S, (k * 53 + i * (4 if i > 10 else 0)) % S
        r = 1 + (k + i) % 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 220))
    t = i / (N - 1)
    if t < 0.4:  # wobble on the pad
        y, ang = 76, math.sin(t * 40) * 0.12
    else:        # launch with ease_in
        y, ang = interpolate(76, -50, (t - 0.4) / 0.6, "ease_in"), 0
    fx, fy = rocket(d, 64, y, ang)
    flame = 8 + (i % 3) * 5 + (18 if t >= 0.4 else 0)
    d.polygon([(fx - 7, fy), (fx + 7, fy), (fx, fy + flame)], fill=(255, 190, 60), outline=(255, 110, 40), width=2)
    b.add_frame(f)

out = HERE / "rocket-emoji.gif"
b.save(str(out), num_colors=64, optimize_for_emoji=True)
ok, info = validate_gif(str(out), is_emoji=True, verbose=True)
print("slack-ready:", ok)
