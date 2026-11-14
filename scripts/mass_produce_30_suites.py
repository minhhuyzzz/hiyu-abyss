#!/usr/bin/env python3
"""
Hiyu Abyss — Mass Production of 30 Cinematic Multi-Slide Suites (90 Images)
Strictly:
- 30 Suites x 3 Slides = 90 full-screen vertical 9:16 (1080x1920) images.
- Master scan resolution (3000px - 30000px) from world-renowned museums.
- Ultra-sharp downsampling (LANCZOS + UnsharpMask) for crisp, museum-grade fidelity.
- Subtle dark wash (30% tint) + organic film grain so overlaid text never drowns out.
- Strictly clean: NO text, NO logos, NO watermarks.
- Standardized slide naming: slide_1_establishing.jpg, slide_2_closeup.jpg, slide_3_macro.jpg.
"""

import os
import io
import json
import time
import urllib.request
import urllib.parse
import numpy as np
from PIL import Image, ImageFilter

OUTPUT_BASE = "c:/hiyuabyss/assets/templates/multislides"
CACHE_DIR = "c:/hiyuabyss/assets/templates/raw_cache"
os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H  # 9/16 = 0.5625

# 30 Masterworks with specific crop targets: (center_x, center_y, zoom)
# zoom is relative fraction of height or width
SUITES_CONFIG = [
    {
        "folder": "theme_01",
        "file": "Narcissus-Caravaggio (1594-96).jpg",
        "title": "Narcissus (Caravaggio)",
        "s1": (0.50, 0.50, 0.95),  # Establishing
        "s2": (0.48, 0.28, 0.40),  # Close face
        "s3": (0.42, 0.65, 0.32),  # Macro water hand
    },
    {
        "folder": "theme_02",
        "file": "The Incredulity of Saint Thomas-Caravaggio (1601-2).jpg",
        "title": "The Incredulity of Saint Thomas (Caravaggio)",
        "s1": (0.50, 0.48, 0.90),
        "s2": (0.60, 0.35, 0.38),
        "s3": (0.52, 0.45, 0.28),
    },
    {
        "folder": "theme_03",
        "file": "The Calling of Saint Matthew-Caravaggo (1599-1600).jpg",
        "title": "The Calling of Saint Matthew (Caravaggio)",
        "s1": (0.45, 0.55, 0.90),
        "s2": (0.38, 0.52, 0.40),
        "s3": (0.82, 0.42, 0.30),
    },
    {
        "folder": "theme_04",
        "file": "Draper Herbert James Mourning for Icarus.jpg",
        "title": "The Mourning for Icarus (Herbert Draper)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.42, 0.40, 0.38),
        "s3": (0.60, 0.30, 0.32),
    },
    {
        "folder": "theme_05",
        "file": "Leonardo da Vinci - Saint John the Baptist C2RMF retouched.jpg",
        "title": "Saint John the Baptist (Leonardo da Vinci)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.35, 0.38),
        "s3": (0.62, 0.32, 0.28),
    },
    {
        "folder": "theme_06",
        "file": "William Bouguereau - Dante and Virgile - Google Art Project.jpg",
        "title": "Dante and Virgil (William Bouguereau)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.48, 0.40, 0.38),
        "s3": (0.75, 0.35, 0.30),
    },
    {
        "folder": "theme_07",
        "file": "Judith Beheading Holofernes - Caravaggio.jpg",
        "title": "Judith Beheading Holofernes (Caravaggio)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.35, 0.35, 0.38),
        "s3": (0.55, 0.50, 0.30),
    },
    {
        "folder": "theme_08",
        "file": "Death of Marat by David.jpg",
        "title": "The Death of Marat (Jacques-Louis David)",
        "s1": (0.50, 0.60, 0.95),
        "s2": (0.45, 0.50, 0.38),
        "s3": (0.35, 0.78, 0.30),
    },
    {
        "folder": "theme_09",
        "file": "Apollo and Daphne (Bernini).jpg",
        "title": "Apollo and Daphne (Gian Lorenzo Bernini)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.52, 0.30, 0.38),
        "s3": (0.58, 0.15, 0.28),
    },
    {
        "folder": "theme_10",
        "file": "Nike of Samothrace, Louvre.jpg",
        "title": "Winged Victory of Samothrace (Louvre)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.48, 0.35, 0.40),
        "s3": (0.65, 0.25, 0.32),
    },
    {
        "folder": "theme_11",
        "file": "Saint Jerome Writing-Caravaggio (1605-6).jpg",
        "title": "Saint Jerome Writing (Caravaggio)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.65, 0.40, 0.38),
        "s3": (0.30, 0.55, 0.30),
    },
    {
        "folder": "theme_12",
        "file": "Psyché ranimée par le baiser de l'Amour, Louvre.jpg",
        "title": "Psyche Revived by Cupid's Kiss (Antonio Canova)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.42, 0.35),
        "s3": (0.50, 0.30, 0.28),
    },
    {
        "folder": "theme_13",
        "file": "Jacques-Louis David, Le Serment des Horaces.jpg",
        "title": "Oath of the Horatii (Jacques-Louis David)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.52, 0.42, 0.38),
        "s3": (0.52, 0.32, 0.28),
    },
    {
        "folder": "theme_14",
        "file": "Caravaggio - Medusa Uffizi - High quality.jpg",
        "title": "Medusa (Caravaggio)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.50, 0.45),
        "s3": (0.50, 0.18, 0.30),
    },
    {
        "folder": "theme_15",
        "file": "JEAN LOUIS THÉODORE GÉRICAULT - La Balsa de la Medusa (Museo del Louvre, 1818-19).jpg",
        "title": "The Raft of the Medusa (Théodore Géricault)",
        "s1": (0.60, 0.50, 0.95),
        "s2": (0.75, 0.35, 0.38),
        "s3": (0.35, 0.70, 0.30),
    },
    {
        "folder": "theme_16",
        "file": "Dying slave Louvre MR 1590, Louvre.jpg",
        "title": "Dying Slave (Michelangelo)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.20, 0.35),
        "s3": (0.50, 0.38, 0.28),
    },
    {
        "folder": "theme_17",
        "file": "Rembrandt van Rijn - Self-Portrait - Google Art Project.jpg",
        "title": "Self-Portrait 1659 (Rembrandt)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.32, 0.38),
        "s3": (0.50, 0.75, 0.30),
    },
    {
        "folder": "theme_18",
        "file": "Rembrandt-Philosophe en méditation-1632-Louvre.jpg",
        "title": "The Philosopher in Meditation (Rembrandt)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.38, 0.55, 0.38),
        "s3": (0.65, 0.38, 0.32),
    },
    {
        "folder": "theme_19",
        "file": "Caspar David Friedrich - Wanderer above the sea of fog.jpg",
        "title": "Wanderer above the Sea of Fog (Caspar David Friedrich)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.38, 0.40),
        "s3": (0.50, 0.75, 0.30),
    },
    {
        "folder": "theme_20",
        "file": "StillLifeWithASkull.jpg",
        "title": "Vanitas (Philippe de Champaigne)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.50, 0.40),
        "s3": (0.80, 0.50, 0.30),
    },
    {
        "folder": "theme_21",
        "file": "Pieter Bruegel the Elder - The Fall of the Rebel Angels - Google Art Project.jpg",
        "title": "The Fall of the Rebel Angels (Bruegel)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.30, 0.38),
        "s3": (0.50, 0.75, 0.30),
    },
    {
        "folder": "theme_22",
        "file": "Francisco de Goya, Saturno devorando a su hijo (1819-1823).jpg",
        "title": "Saturn Devouring His Son (Francisco Goya)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.30, 0.38),
        "s3": (0.50, 0.55, 0.30),
    },
    {
        "folder": "theme_23",
        "file": "David - The Death of Socrates.jpg",
        "title": "The Death of Socrates (Jacques-Louis David)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.40, 0.38),
        "s3": (0.60, 0.65, 0.28),
    },
    {
        "folder": "theme_24",
        "file": "The Garden of Earthly Delights by Bosch High Resolution.jpg",
        "title": "The Garden of Earthly Delights (Hieronymus Bosch)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.78, 0.50, 0.38),
        "s3": (0.80, 0.38, 0.28),
    },
    {
        "folder": "theme_25",
        "file": "Répine Ivan le Terrible et son fils Ivan principale version 1883 - 1885.jpg",
        "title": "Ivan the Terrible and His Son Ivan (Ilya Repin)",
        "s1": (0.50, 0.55, 0.90),
        "s2": (0.48, 0.40, 0.38),
        "s3": (0.52, 0.48, 0.30),
    },
    {
        "folder": "theme_26",
        "file": "Las Meninas, by Diego Velázquez, from Prado in Google Earth.jpg",
        "title": "Las Meninas (Diego Velázquez)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.60, 0.38),
        "s3": (0.20, 0.45, 0.30),
    },
    {
        "folder": "theme_27",
        "file": "Michelangelo-Caravaggio 021 Beheading-of-St-John-the-Baptist cropped.jpg",
        "title": "The Beheading of Saint John the Baptist (Caravaggio)",
        "s1": (0.40, 0.50, 0.90),
        "s2": (0.35, 0.60, 0.38),
        "s3": (0.52, 0.65, 0.30),
    },
    {
        "folder": "theme_28",
        "file": "Henry Fuseli (1741–1825), The Nightmare, 1781.jpg",
        "title": "The Nightmare (Henry Fuseli)",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.45, 0.38),
        "s3": (0.22, 0.35, 0.28),
    },
    {
        "folder": "theme_29",
        "file": "Arnold Böcklin - Die Toteninsel III (Alte Nationalgalerie, Berlin).jpg",
        "title": "The Isle of the Dead (Arnold Böcklin)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.72, 0.38),
        "s3": (0.50, 0.48, 0.32),
    },
    {
        "folder": "theme_30",
        "file": "Michelangelo - Creation of Adam (cropped).jpg",
        "title": "The Creation of Adam (Michelangelo)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.35, 0.55, 0.40),
        "s3": (0.50, 0.48, 0.28),
    }
]

def fetch_wikimedia_image_urls(files):
    """Batch-fetches high-resolution image URLs from Wikimedia Commons API."""
    titles = '|'.join(['File:' + f for f in files])
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(titles)}&prop=imageinfo&iiprop=url|size&iiurlwidth=3840"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (https://github.com/minhhuyzzz/hiyu-abyss; contact@hiyuabyss.com)"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode())
    
    pages = data.get("query", {}).get("pages", {})
    mapping = {}
    for pid, p in pages.items():
        title = p.get("title", "")
        # Remove 'File:' prefix
        fname = title[5:] if title.startswith("File:") else title
        info = p.get("imageinfo", [{}])[0]
        # Prefer 3840px thumbnail if present, fallback to original URL
        dl_url = info.get("thumburl") or info.get("url")
        if dl_url:
            mapping[fname] = dl_url
    return mapping

def download_file(url, target_path):
    """Downloads an image file with custom User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (https://github.com/minhhuyzzz/hiyu-abyss; contact@hiyuabyss.com)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        with open(target_path, "wb") as f:
            f.write(resp.read())

def get_crop_box(w, h, cx_frac, cy_frac, zoom):
    """
    Computes a 9:16 aspect ratio bounding box centered near (cx_frac, cy_frac).
    zoom is the fraction of dimension used.
    """
    # Desired box height
    box_h = int(h * zoom)
    box_w = int(box_h * TARGET_RATIO)
    
    # If width exceeds image width, clamp and recalculate height
    if box_w > w:
        box_w = w
        box_h = int(box_w / TARGET_RATIO)
    
    cx = int(w * cx_frac)
    cy = int(h * cy_frac)
    
    left = cx - box_w // 2
    top = cy - box_h // 2
    
    # Boundary clamps
    if left < 0:
        left = 0
    elif left + box_w > w:
        left = w - box_w
        
    if top < 0:
        top = 0
    elif top + box_h > h:
        top = h - box_h
        
    return (left, top, left + box_w, top + box_h)

def process_and_save_slide(src_img, crop_box, out_path):
    """Crops, scales to 1080x1920, sharpens, applies dark moody wash and film grain."""
    cropped = src_img.crop(crop_box)
    
    # Ultra-sharp downsampling to 1080x1920
    resized = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # Professional unsharp mask for fine-art texture (keeps brushstrokes crisp)
    sharpened = resized.filter(ImageFilter.UnsharpMask(radius=1.8, percent=140, threshold=2))
    
    # Dark moody wash (preserve rich colors, deepen shadow areas so text has high contrast)
    arr = np.array(sharpened, dtype=np.float32)
    arr = arr * 0.70  # 30% reduction in luminance
    
    # Fine organic film grain to eliminate digital banding
    noise = np.random.normal(0.0, 1.8, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    
    final_img = Image.fromarray(arr)
    final_img.save(out_path, format="JPEG", quality=95)

def main():
    print("=" * 70)
    print("  HIYU ABYSS — MASS PRODUCTION: 30 MULTI-SLIDE SUITES (90 IMAGES)")
    print("=" * 70)
    
    files_to_fetch = [s["file"] for s in SUITES_CONFIG]
    print(f"[*] Đang lấy danh sách URL độ phân giải cao cho {len(files_to_fetch)} kiệt tác...")
    
    # Fetch in 2 batches of 15
    url_map = {}
    for i in range(0, len(files_to_fetch), 15):
        batch = files_to_fetch[i:i+15]
        res = fetch_wikimedia_image_urls(batch)
        url_map.update(res)
        time.sleep(1.0)
        
    print(f"[+] Đã tìm thấy {len(url_map)}/{len(files_to_fetch)} liên kết ảnh chất lượng cao.")
    
    total_images_rendered = 0
    
    for idx, cfg in enumerate(SUITES_CONFIG):
        folder_name = cfg["folder"]
        fname = cfg["file"]
        title = cfg["title"]
        suite_dir = os.path.join(OUTPUT_BASE, folder_name)
        os.makedirs(suite_dir, exist_ok=True)
        
        print(f"\n[{idx+1:02d}/30] Xử lý bộ: {folder_name} — {title}")
        
        # Check cache or download
        cached_file = os.path.join(CACHE_DIR, fname)
        if not os.path.exists(cached_file) or os.path.getsize(cached_file) < 50000:
            dl_url = url_map.get(fname)
            if not dl_url:
                print(f"  [!] Không có URL tải cho: {fname}")
                continue
            print(f"  [↓] Đang tải ảnh gốc master: {dl_url[:65]}...")
            try:
                download_file(dl_url, cached_file)
                time.sleep(0.5)
            except Exception as e:
                print(f"  [X] Lỗi tải file: {e}")
                continue
        else:
            print(f"  [✓] Sử dụng file cache đã có: {cached_file}")
            
        # Open source master
        try:
            src = Image.open(cached_file).convert("RGB")
            w, h = src.size
            print(f"  [i] Kích thước master: {w}x{h} px")
        except Exception as e:
            print(f"  [X] Không mở được file ảnh: {e}")
            continue
            
        # Generate 3 slides
        slides = [
            ("slide_1_establishing.jpg", cfg["s1"], "Slide 1 (Establishing Shot)"),
            ("slide_2_closeup.jpg", cfg["s2"], "Slide 2 (Intense Close-up)"),
            ("slide_3_macro.jpg", cfg["s3"], "Slide 3 (Macro Detail)")
        ]
        
        for slide_fname, (cx, cy, zoom), desc in slides:
            out_path = os.path.join(suite_dir, slide_fname)
            crop_box = get_crop_box(w, h, cx, cy, zoom)
            process_and_save_slide(src, crop_box, out_path)
            file_kb = os.path.getsize(out_path) // 1024
            print(f"    -> Đã render {slide_fname} ({file_kb} KB) — {desc}")
            total_images_rendered += 1
            
    print("\n" + "=" * 70)
    print(f"[✓] HOÀN TẤT TOÀN BỘ: Đã render {total_images_rendered}/90 ảnh đa góc máy!")
    print(f"[✓] Thư mục lưu trữ: {OUTPUT_BASE}")
    print("=" * 70)

if __name__ == "__main__":
    main()
