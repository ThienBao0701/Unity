#!/usr/bin/env python3
"""Câu 1a - remove the white background of the two exam pictures and save transparent PNGs.

Method (simple and repeatable):
  1. A pixel counts as "background" when it is almost white (all channels >= THRESHOLD).
  2. Flood fill from the image border through background pixels only. White areas that are
     enclosed by the object (e.g. white parts inside the globe) are NOT reached, so they are kept.
  3. Filled pixels get alpha = 0. Pixels on the edge of the object get a partial alpha
     (the lighter they are, the more transparent) so the outline is smooth, not jagged.
  4. Small leftover islands (e.g. watermark specks) are removed; the result is cropped to the object.

Usage:
  python3 remove_background.py input.jpg output.png [--crop x0 y0 x1 y1]
Requires: Pillow, numpy
"""
import sys
from collections import deque

import numpy as np
from PIL import Image

THRESHOLD = 225   # "almost white"
MIN_ISLAND = 400  # opaque blobs smaller than this many pixels are removed


def remove_background(src, dst, crop=None):
    img = Image.open(src).convert("RGB")
    if crop:
        img = img.crop(crop)
    rgb = np.asarray(img).astype(np.int32)
    h, w, _ = rgb.shape
    light = rgb.min(axis=2)
    is_bg_color = light >= THRESHOLD

    # 2. flood fill from the border (4-neighbour BFS)
    bg = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_bg_color[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg_color[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and not bg[ny, nx] and is_bg_color[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))

    # 3. alpha: 0 for background, 255 for object, soft edge for object pixels touching background
    alpha = np.where(bg, 0, 255).astype(np.float32)
    near_bg = np.zeros_like(bg)
    near_bg[1:, :] |= bg[:-1, :]
    near_bg[:-1, :] |= bg[1:, :]
    near_bg[:, 1:] |= bg[:, :-1]
    near_bg[:, :-1] |= bg[:, 1:]
    edge = near_bg & ~bg
    # lighter edge pixel = more transparent (255 -> 0 alpha, <=150 -> fully opaque)
    edge_alpha = np.clip((255 - light) / (255 - 150), 0, 1) * 255
    alpha[edge] = edge_alpha[edge]

    # 4. remove small islands (label opaque regions with a BFS)
    opaque = alpha > 0
    seen = np.zeros_like(opaque)
    for sy in range(h):
        for sx in range(w):
            if opaque[sy, sx] and not seen[sy, sx]:
                comp = [(sy, sx)]
                seen[sy, sx] = True
                i = 0
                while i < len(comp):
                    y, x = comp[i]
                    i += 1
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if 0 <= ny < h and 0 <= nx < w and opaque[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            comp.append((ny, nx))
                if len(comp) < MIN_ISLAND:
                    for y, x in comp:
                        alpha[y, x] = 0

    rgba = np.dstack([rgb, alpha.astype(np.int32)]).astype(np.uint8)
    out = Image.fromarray(rgba, "RGBA")
    bbox = out.getchannel("A").getbbox()
    if bbox:
        pad = 4
        bbox = (max(bbox[0] - pad, 0), max(bbox[1] - pad, 0), min(bbox[2] + pad, w), min(bbox[3] + pad, h))
        out = out.crop(bbox)
    out.save(dst)
    a = np.asarray(out.getchannel("A"))
    print(f"{dst}: {out.size[0]}x{out.size[1]}, transparent pixels = {100.0 * (a == 0).mean():.1f}%")


if __name__ == "__main__":
    args = sys.argv[1:]
    crop = None
    if "--crop" in args:
        i = args.index("--crop")
        crop = tuple(int(v) for v in args[i + 1:i + 5])
        args = args[:i] + args[i + 5:]
    remove_background(args[0], args[1], crop)
