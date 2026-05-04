"""
Generate PWA icons (192x192 and 512x512) into assets/.

Design: rounded square in theme_color (#3b82f6) with a white wrench mark
roughly evoking the 🛠️ logo used across the site. Pure Pillow, no
network or external assets required, so it can be re-run anywhere.
"""

from __future__ import annotations

import math
import os

from PIL import Image, ImageDraw, ImageFilter


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, 'assets')

THEME = (59, 130, 246)            # #3b82f6
THEME_DARK = (37, 99, 235)        # #2563eb (bottom of gradient)
WHITE = (255, 255, 255)


def gradient_background(size: int) -> Image.Image:
    """Vertical gradient from THEME to THEME_DARK."""
    img = Image.new('RGB', (size, size), THEME)
    top = THEME
    bot = THEME_DARK
    for y in range(size):
        t = y / (size - 1)
        r = round(top[0] * (1 - t) + bot[0] * t)
        g = round(top[1] * (1 - t) + bot[1] * t)
        b = round(top[2] * (1 - t) + bot[2] * t)
        ImageDraw.Draw(img).line([(0, y), (size, y)], fill=(r, g, b))
    return img


def rounded_mask(size: int, radius_ratio: float = 0.22) -> Image.Image:
    """L-mode mask with a rounded square shape."""
    mask = Image.new('L', (size, size), 0)
    r = int(size * radius_ratio)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size, size), radius=r, fill=255)
    return mask


def draw_wrench(size: int) -> Image.Image:
    """White wrench-ish shape on transparent canvas."""
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)

    cx, cy = size / 2, size / 2
    # Wrench handle: rotated rounded rectangle.
    handle_len = size * 0.62
    handle_w = size * 0.13
    head_r = size * 0.16

    # Build the wrench in an oversized canvas, rotate, then paste.
    pad = size
    wrench = Image.new('RGBA', (pad, pad), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wrench)

    px, py = pad / 2, pad / 2
    # Handle aligned diagonally (top-right -> bottom-left).
    wd.rounded_rectangle(
        (px - handle_w / 2, py - handle_len / 2,
         px + handle_w / 2, py + handle_len / 2),
        radius=handle_w / 2,
        fill=WHITE,
    )
    # Wrench head: open jaw at one end (top).
    head_cx, head_cy = px, py - handle_len / 2
    wd.ellipse(
        (head_cx - head_r, head_cy - head_r,
         head_cx + head_r, head_cy + head_r),
        fill=WHITE,
    )
    # Cut the open-jaw notch with a rotated black rectangle.
    notch_w = head_r * 1.05
    notch_h = head_r * 1.6
    notch = Image.new('RGBA', (int(notch_w * 2), int(notch_h * 2)), (0, 0, 0, 0))
    ImageDraw.Draw(notch).rectangle(
        (0, 0, notch.width, notch.height),
        fill=(0, 0, 0, 255),
    )
    notch = notch.rotate(35, resample=Image.BICUBIC, expand=True)
    # Erase from the head with the rotated rect (use alpha_composite-style cut).
    nx = int(head_cx - notch.width / 2)
    ny = int(head_cy - notch.height * 0.85)
    # Build a mask from the rotated black notch's alpha.
    cut_mask = Image.new('L', wrench.size, 0)
    cut_mask.paste(notch.split()[3], (nx, ny))
    transparent = Image.new('RGBA', wrench.size, (0, 0, 0, 0))
    wrench = Image.composite(transparent, wrench, cut_mask)

    # Foot of the handle: small rounded cap (already covered by rounded_rect).
    # Rotate the wrench 35° (so head sits upper-left, handle goes lower-right).
    wrench = wrench.rotate(-35, resample=Image.BICUBIC, expand=False)

    # Crop center back to the icon size.
    left = int((pad - size) / 2)
    top = int((pad - size) / 2)
    wrench = wrench.crop((left, top, left + size, top + size))

    canvas.alpha_composite(wrench)

    # Subtle drop shadow under the wrench for depth.
    shadow_src = canvas.split()[3].point(lambda a: int(a * 0.45))
    shadow = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    shadow.putalpha(shadow_src)
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=size * 0.012))
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    out.alpha_composite(shadow, dest=(int(size * 0.01), int(size * 0.015)))
    out.alpha_composite(canvas)
    return out


def build_icon(size: int) -> Image.Image:
    bg = gradient_background(size).convert('RGBA')
    mask = rounded_mask(size)
    rounded = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    rounded.paste(bg, (0, 0), mask)
    fg = draw_wrench(size)
    rounded.alpha_composite(fg)
    return rounded


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for s in (192, 512):
        img = build_icon(s)
        path = os.path.join(OUT_DIR, f'icon-{s}.png')
        img.save(path, 'PNG', optimize=True)
        print(f'wrote {path} ({img.size[0]}x{img.size[1]})')


if __name__ == '__main__':
    main()
