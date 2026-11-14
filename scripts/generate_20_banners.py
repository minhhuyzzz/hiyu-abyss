#!/usr/bin/env python3
"""
Hiyu Abyss — 20 Bespoke Dark Minimalist Poster Banners (1080x1920, 9:16)
Generates 20 unique, clean, high-resolution background templates using
mathematical Chiaroscuro lighting, volumetric light shafts, film grain,
and atmospheric depth. Strictly NO text or watermarks.
"""

import os
import numpy as np
from PIL import Image, ImageFilter

OUTPUT_DIR = "c:/hiyuabyss/assets/templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920

# Coordinate grid
x = np.linspace(-1.0, 1.0, WIDTH, dtype=np.float32)
y = np.linspace(-1.0, 1.0, HEIGHT, dtype=np.float32)
X, Y = np.meshgrid(x, y)

THEMES = [
    ("theme_01_hypocrisy", "Cold bone-white chiaroscuro slash", [12, 16, 24], [220, 225, 230]),
    ("theme_02_double_standard", "Asymmetrical dual spotlights", [10, 14, 20], [210, 195, 170]),
    ("theme_03_morality", "Descending ethereal filament light", [11, 15, 22], [200, 215, 235]),
    ("theme_04_ego", "Overhead solitary pedestal pool", [13, 14, 18], [230, 210, 180]),
    ("theme_05_self_deception", "Cold misty mirror portal", [9, 13, 19], [170, 190, 215]),
    ("theme_06_shadow", "Backlit elongated shadow gradient", [8, 11, 16], [220, 220, 225]),
    ("theme_07_mask", "Fractured lunar rim light", [12, 15, 21], [215, 225, 235]),
    ("theme_08_power", "Monolithic obsidian vertical shaft", [7, 10, 15], [190, 200, 220]),
    ("theme_09_manipulation", "Subtle vertical tension strings", [10, 13, 18], [200, 210, 225]),
    ("theme_10_freedom", "Open nocturnal horizon mist", [8, 12, 20], [180, 205, 240]),
    ("theme_11_truth", "Point-source flame with stark falloff", [15, 14, 16], [245, 220, 180]),
    ("theme_12_love", "Dual ambient nodes through frosted cold", [14, 12, 17], [220, 190, 200]),
    ("theme_13_loyalty", "Vertical silver-blue blade of light", [10, 14, 22], [195, 220, 245]),
    ("theme_14_envy", "Narrow cold emerald slit beam", [8, 16, 15], [160, 230, 200]),
    ("theme_15_crowd", "Layered horizontal fog with sharp focal point", [9, 13, 19], [205, 215, 230]),
    ("theme_16_suffering", "High-contrast harsh diagonal chiaroscuro", [12, 11, 13], [225, 200, 190]),
    ("theme_17_identity", "Solitary circular pool on void floor", [8, 10, 14], [225, 230, 240]),
    ("theme_18_meaning", "Ascending geometric diagonal planes", [10, 12, 20], [210, 215, 240]),
    ("theme_19_solitude", "Cold indigo minimalist night gradient", [7, 11, 18], [175, 195, 230]),
    ("theme_20_status", "Fading theater cone with dust haze", [12, 14, 18], [225, 210, 175])
]

def render_theme(idx, name, desc, base_rgb, light_rgb):
    # Base dark gradient (darker at bottom for negative space text overlay)
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    for c in range(3):
        # Vertical gradient from darker top to pitch black bottom
        grad = base_rgb[c] * (0.6 - 0.4 * Y)
        base[:, :, c] = np.clip(grad, 2.0, 45.0)

    # Lighting mask
    light_mask = np.zeros((HEIGHT, WIDTH), dtype=np.float32)

    if idx == 0:  # Hypocrisy: stark diagonal slash
        dist_line = np.abs(0.7 * X - 0.7 * Y - 0.4)
        slash = np.exp(-dist_line * 3.5) * np.exp(-((Y + 0.4) ** 2) * 1.5)
        light_mask = slash * 1.1

    elif idx == 1:  # Double standard: asymmetrical dual lights
        spot1 = np.exp(-(((X + 0.35) ** 2) * 4.0 + ((Y + 0.45) ** 2) * 2.5)) * 1.0
        spot2 = np.exp(-(((X - 0.35) ** 2) * 6.0 + ((Y + 0.35) ** 2) * 3.5)) * 0.45
        light_mask = spot1 + spot2

    elif idx == 2:  # Morality: descending vertical streams
        center_glow = np.exp(-(X ** 2) * 2.5) * np.exp(-((Y + 0.4) ** 2) * 2.0)
        lines = np.sin(X * 35.0) ** 6 * np.exp(-((Y + 0.3) ** 2) * 3.0) * 0.25
        light_mask = center_glow + lines

    elif idx == 3:  # Ego: solitary high-contrast pedestal pool
        circle = np.exp(-((X ** 2) * 5.0 + ((Y + 0.4) ** 2) * 3.0)) * 1.2
        pillar = np.exp(-(X ** 2) * 18.0) * (Y > -0.4) * np.exp(-(Y ** 2) * 2.0) * 0.4
        light_mask = circle + pillar

    elif idx == 4:  # Self deception: misty mirror portal
        box = (np.abs(X) < 0.35) & (Y > -0.75) & (Y < -0.05)
        rim = np.exp(-(np.abs(X) - 0.35) ** 2 * 35.0) * np.exp(-((Y + 0.4) ** 2) * 3.0)
        inner = np.exp(-((X ** 2) * 4.0 + ((Y + 0.4) ** 2) * 3.0)) * 0.25
        light_mask = rim * 0.8 + inner * 0.5

    elif idx == 5:  # Shadow: backlight casting long shadow
        backlight = np.exp(-((X ** 2) * 2.0 + ((Y + 0.65) ** 2) * 6.0)) * 1.3
        shadow_wedge = np.clip(1.0 - np.exp(-(np.abs(X) / (Y + 0.7 + 1e-4) * 8.0)), 0, 1)
        light_mask = backlight * np.where(Y > -0.65, shadow_wedge, 1.0)

    elif idx == 6:  # Mask: fractured moonlit shards
        spot = np.exp(-(((X - 0.1) ** 2) * 3.5 + ((Y + 0.5) ** 2) * 2.5))
        shard = np.abs(np.sin(X * 8.0 + Y * 5.0)) * 0.3
        light_mask = spot * (0.8 + shard)

    elif idx == 7:  # Power: monolithic obsidian pillar
        monolith = (np.abs(X) < 0.22) & (Y < 0.2)
        side_light = np.exp(-(X - 0.23) ** 2 * 60.0) * np.exp(-((Y + 0.2) ** 2) * 1.8) * 1.1
        ambient = np.exp(-(X ** 2) * 1.5) * np.exp(-((Y + 0.5) ** 2) * 2.0) * 0.3
        light_mask = side_light + ambient

    elif idx == 8:  # Manipulation: subtle vertical marionette strings
        top_glow = np.exp(-((Y + 0.9) ** 2) * 4.0) * 0.7
        strings = (np.sin(X * 45.0) ** 16) * np.exp(-(Y ** 2) * 1.5) * 0.6
        light_mask = top_glow + strings

    elif idx == 9:  # Freedom: open night horizon
        horizon = np.exp(-((Y + 0.25) ** 2) * 7.0) * np.exp(-(X ** 2) * 1.8) * 1.0
        sky = np.exp(-((Y + 0.6) ** 2) * 2.0) * 0.4
        light_mask = horizon + sky

    elif idx == 10:  # Truth: point source flame
        r = np.sqrt(X ** 2 + (Y + 0.4) ** 2) + 1e-3
        flare = np.exp(-r * 3.8) * 1.5 + np.exp(-r * 1.2) * 0.4
        light_mask = flare

    elif idx == 11:  # Love: dual ambient nodes
        node1 = np.exp(-(((X + 0.3) ** 2) * 4.5 + ((Y + 0.4) ** 2) * 3.0)) * 0.8
        node2 = np.exp(-(((X - 0.3) ** 2) * 4.5 + ((Y + 0.4) ** 2) * 3.0)) * 0.8
        divider = np.exp(-(X ** 2) * 50.0) * 0.7
        light_mask = np.clip(node1 + node2 - divider, 0, 1.5)

    elif idx == 12:  # Loyalty: vertical silver blade
        blade = np.exp(-(X ** 2) * 45.0) * np.exp(-((Y + 0.3) ** 2) * 1.8) * 1.3
        ambient = np.exp(-(X ** 2) * 3.0) * np.exp(-((Y + 0.4) ** 2) * 2.0) * 0.35
        light_mask = blade + ambient

    elif idx == 13:  # Envy: narrow vertical slit
        slit = np.exp(-(X ** 2) * 120.0) * np.exp(-((Y + 0.3) ** 2) * 2.5) * 1.4
        seep = np.exp(-(X ** 2) * 4.0) * np.exp(-((Y + 0.3) ** 2) * 2.0) * 0.25
        light_mask = slit + seep

    elif idx == 14:  # Crowd: layered fog bands
        fog = (np.sin(Y * 18.0) * 0.15 + 0.85) * np.exp(-((Y + 0.4) ** 2) * 2.5)
        spot = np.exp(-(((X + 0.2) ** 2) * 8.0 + ((Y + 0.4) ** 2) * 4.0)) * 0.8
        light_mask = fog * 0.5 + spot

    elif idx == 15:  # Suffering: sharp diagonal chiaroscuro
        diag = np.clip(0.6 * X + 0.8 * Y + 0.2, -1, 1)
        cut = np.exp(-(diag ** 2) * 4.0) * np.exp(-((Y + 0.4) ** 2) * 2.0) * 1.2
        light_mask = cut

    elif idx == 16:  # Identity: circular pool on dark floor
        pool = np.exp(-((X ** 2) * 4.0 + ((Y + 0.35) ** 2) * 5.0)) * 1.2
        light_mask = pool

    elif idx == 17:  # Meaning: ascending diagonal planes
        steps = np.clip(np.sin((X + Y * 0.8) * 10.0), 0, 1) * np.exp(-((Y + 0.4) ** 2) * 2.2) * 0.7
        glow = np.exp(-(((X - 0.2) ** 2) * 3.0 + ((Y + 0.6) ** 2) * 3.0)) * 0.6
        light_mask = steps + glow

    elif idx == 18:  # Solitude: minimalist night mist
        sky = np.exp(-((Y + 0.5) ** 2) * 2.2) * 0.7
        horizon_line = np.exp(-((Y + 0.2) ** 2) * 25.0) * 0.4
        light_mask = sky + horizon_line

    elif idx == 19:  # Status: fading theater spotlight cone
        cone = np.exp(-((X / (Y + 1.2 + 1e-4)) ** 2) * 5.0) * np.exp(-((Y + 0.3) ** 2) * 2.5) * 1.2
        light_mask = cone

    # Apply lighting color
    img_rgb = base.copy()
    for c in range(3):
        img_rgb[:, :, c] += light_mask * (light_rgb[c] - base_rgb[c])

    # Deep vignette: darkens corners and bottom for maximum typography readability
    r_vignette = np.sqrt(X ** 2 + ((Y + 0.15) * 0.85) ** 2)
    vignette = np.clip(1.0 - 0.45 * (r_vignette ** 2), 0.25, 1.0)
    for c in range(3):
        img_rgb[:, :, c] *= vignette

    # Film grain noise (subtle, 1.5% intensity, fine art texture)
    noise = np.random.normal(0.0, 3.2, (HEIGHT, WIDTH, 3)).astype(np.float32)
    img_rgb = np.clip(img_rgb + noise, 0.0, 255.0).astype(np.uint8)

    # Convert to PIL Image
    im = Image.fromarray(img_rgb, mode="RGB")
    # Gentle box blur to blend any harsh math transitions
    im = im.filter(ImageFilter.GaussianBlur(radius=0.8))

    out_path = os.path.join(OUTPUT_DIR, f"{name}.jpg")
    im.save(out_path, format="JPEG", quality=95)
    print(f"[{idx+1:02d}/20] Rendered: {name}.jpg ({desc})")
    return out_path

def main():
    print("=== RENDERING 20 BESPOKE 9:16 DARK MINIMALIST BANNER TEMPLATES ===")
    rendered_files = []
    for idx, (name, desc, base_rgb, light_rgb) in enumerate(THEMES):
        out_path = render_theme(idx, name, desc, base_rgb, light_rgb)
        rendered_files.append(out_path)
    print(f"\n=> THÀNH CÔNG: Đã render toàn bộ 20 phôi ảnh nền chuẩn 9:16 tại '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()
