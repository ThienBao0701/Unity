"""Draws PLACEHOLDER source pictures (white background, JPG) that imitate the two exam icons.
Used only because dreamstime.com is blocked in the cloud session."""
import math
import sys
from PIL import Image, ImageDraw, ImageFont

out_dir = sys.argv[1]
SS = 4  # supersampling


def finish(img, name, size):
    img = img.resize((size, size), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.text((8, size - 20), "PLACEHOLDER - replace with the dreamstime image", fill=(150, 150, 150))
    img.save(f"{out_dir}/{name}", quality=92)


# ---------------- globe (planet)
N = 800 * SS
img = Image.new("RGB", (N, N), "white")
d = ImageDraw.Draw(img)
c, r = N / 2, N * 0.40
d.ellipse([c - r, c - r, c + r, c + r], fill=(95, 99, 105))
# continents: light grey blobs clipped to the sphere
land = Image.new("L", (N, N), 0)
ld = ImageDraw.Draw(land)
blobs = [
    [(-0.55, -0.55), (-0.1, -0.7), (0.05, -0.45), (-0.2, -0.2), (-0.35, 0.1), (-0.6, -0.1)],   # "americas" top
    [(-0.3, 0.1), (-0.05, 0.15), (0.0, 0.45), (-0.2, 0.8), (-0.35, 0.45)],                     # south
    [(0.15, -0.65), (0.6, -0.55), (0.75, -0.2), (0.45, -0.1), (0.3, -0.3), (0.1, -0.35)],      # "eurasia"
    [(0.2, -0.05), (0.5, 0.0), (0.55, 0.35), (0.35, 0.65), (0.2, 0.35)],                       # "africa"
    [(0.6, 0.35), (0.85, 0.35), (0.8, 0.55), (0.6, 0.55)],                                     # "australia"
]
for b in blobs:
    ld.polygon([(c + x * r, c + y * r) for x, y in b], fill=255)
sphere = Image.new("L", (N, N), 0)
ImageDraw.Draw(sphere).ellipse([c - r * 0.93, c - r * 0.93, c + r * 0.93, c + r * 0.93], fill=255)
land = Image.composite(land, Image.new("L", (N, N), 0), sphere)
img.paste((200, 204, 208), mask=land)
# meridian/parallel lines (like a globe icon)
for k in (-0.5, 0, 0.5):
    d.arc([c - r * abs(k) - 2, c - r, c + r * abs(k) + 2, c + r], 0, 360, fill=(70, 74, 80), width=3 * SS) if k else \
        d.line([c, c - r, c, c + r], fill=(70, 74, 80), width=3 * SS)
    d.line([c - r * math.sqrt(1 - k * k), c + k * r, c + r * math.sqrt(1 - k * k), c + k * r], fill=(70, 74, 80), width=3 * SS)
finish(img, "source_placeholder_globe.jpg", 800)

# ---------------- rocket (drawn upright, then rotated so the nose points up-right = 45 degrees)
R = Image.new("RGBA", (N, N), (255, 255, 255, 0))
d = ImageDraw.Draw(R)
grey, dark = (95, 99, 105, 255), (60, 63, 68, 255)
cx = N / 2
body_top, body_bot, bw = N * 0.14, N * 0.66, N * 0.13
d.polygon([(cx, body_top - N * 0.06), (cx + bw, body_top + N * 0.14), (cx + bw, body_bot),
           (cx - bw, body_bot), (cx - bw, body_top + N * 0.14)], fill=grey)            # body + nose
d.ellipse([cx - bw * 0.55, N * 0.30, cx + bw * 0.55, N * 0.30 + bw * 1.1], fill=(255, 255, 255, 255))  # window
d.ellipse([cx - bw * 0.35, N * 0.30 + bw * 0.2, cx + bw * 0.35, N * 0.30 + bw * 0.9], fill=dark)
d.polygon([(cx - bw, N * 0.46), (cx - bw * 2.1, N * 0.66), (cx - bw * 2.1, N * 0.74), (cx - bw, N * 0.64)], fill=dark)  # fins
d.polygon([(cx + bw, N * 0.46), (cx + bw * 2.1, N * 0.66), (cx + bw * 2.1, N * 0.74), (cx + bw, N * 0.64)], fill=dark)
d.rectangle([cx - bw * 0.7, body_bot, cx + bw * 0.7, body_bot + N * 0.03], fill=dark)                               # nozzle
d.polygon([(cx - bw * 0.65, body_bot + N * 0.03), (cx + bw * 0.65, body_bot + N * 0.03), (cx + bw * 0.3, N * 0.80),
           (cx, N * 0.90), (cx - bw * 0.3, N * 0.80)], fill=(120, 124, 130, 255))                                   # flame
d.polygon([(cx - bw * 0.3, body_bot + N * 0.05), (cx + bw * 0.3, body_bot + N * 0.05), (cx, N * 0.82)],
          fill=(255, 255, 255, 255))                                                                                # flame core
R = R.rotate(-45, resample=Image.BICUBIC, center=(cx, N / 2))
img = Image.new("RGB", (N, N), "white")
img.paste(R, mask=R)
finish(img, "source_placeholder_rocket.jpg", 800)
print("placeholders drawn")
