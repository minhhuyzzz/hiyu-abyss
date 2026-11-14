#!/usr/bin/env python3
"""
Hiyu Abyss — Mass Production of 30 Non-Human Classical Suites (Theme 31 - 60)
Strictly:
- 30 Suites x 3 Slides = 90 full-screen vertical 9:16 (1080x1920) images.
- 100% NON-HUMAN, NON-GHOSTLY, NON-CREEPY.
- Focus: Grand antique libraries, royal palaces, spiral staircases, classical instruments (violin, harp, cello),
  noble flower still lifes (Jan van Huysum, Bosschaert), porcelain tea sets, golden hour seaports & mountain lakes.
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

# 30 Aesthetic Classical Non-Human Masterworks: (center_x, center_y, zoom)
SUITES_CONFIG = [
    # Nhóm 1: Thư viện & Thư phòng học giả (Theme 31 - 38)
    {
        "folder": "theme_31",
        "file": "Dublin Trinity College Library Long Room 02.jpg",
        "title": "Long Room, Trinity College Dublin",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.40, 0.40),
        "s3": (0.28, 0.55, 0.30),
    },
    {
        "folder": "theme_32",
        "file": "Austria - Admont Abbey Library - 1326.jpg",
        "title": "Admont Abbey Library",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.30, 0.42),
        "s3": (0.50, 0.18, 0.30),
    },
    {
        "folder": "theme_33",
        "file": "1601 De Bry and de Veer Map of Nova Zembla and the Northeast Passage - Geographicus - NovaZembla-debry-1601.jpg",
        "title": "1601 Antique Maritime Cartography",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.75, 0.65, 0.28),
    },
    {
        "folder": "theme_34",
        "file": "Prunksaal Österreichische Nationalbibliothek Wien.jpg",
        "title": "State Hall of the Austrian National Library",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.42),
        "s3": (0.50, 0.20, 0.30),
    },
    {
        "folder": "theme_35",
        "file": "Antonio santucci, sfera armillare, firenze 1588-93, 06.JPG",
        "title": "Santucci Renaissance Armillary Sphere (Galileo Museum)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.50, 0.28),
    },
    {
        "folder": "theme_36",
        "file": "Jan Davidsz de Heem - Still Life with Books and a Violin - 613 - Mauritshuis.jpg",
        "title": "Jan Davidsz de Heem — Still Life with Books and Violin",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.45, 0.50, 0.40),
        "s3": (0.35, 0.65, 0.28),
    },
    {
        "folder": "theme_37",
        "file": "Anton Raphael Mengs, The Triumph of History over Time (Allegory of the Museum Clementinum), ceiling fresco in the Camera dei Papiri, Vatican Library, 1772 - M0tty.jpg",
        "title": "Vatican Apostolic Library Ceiling Fresco",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.40, 0.40),
        "s3": (0.50, 0.25, 0.30),
    },
    {
        "folder": "theme_38",
        "file": "Globe Gores Parte 2 - Blaeu, Willem Jansz.jpg",
        "title": "Willem Blaeu — Antique Celestial Constellations",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.35, 0.38),
        "s3": (0.50, 0.65, 0.28),
    },

    # Nhóm 2: Cung điện & Kiến trúc nguy nga (Theme 39 - 46)
    {
        "folder": "theme_39",
        "file": "Spiral staircase in the Vatican Museums from bottom 02.jpg",
        "title": "Bramante Spiral Staircase (Vatican)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.50, 0.45),
        "s3": (0.50, 0.50, 0.28),
    },
    {
        "folder": "theme_40",
        "file": "Chateau Versailles Galerie des Glaces.jpg",
        "title": "Hall of Mirrors, Palace of Versailles",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.38, 0.40),
        "s3": (0.50, 0.25, 0.30),
    },
    {
        "folder": "theme_41",
        "file": "2017-07-29 France, Paris DSC 2711 DxO 2.jpg",
        "title": "Sainte-Chapelle Gothic Stained Glass Windows",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.35, 0.40),
        "s3": (0.50, 0.20, 0.30),
    },
    {
        "folder": "theme_42",
        "file": "Venice, Palazzo Ducale, Arco Foscari 1.jpg",
        "title": "Palazzo Ducale Courtyard & Loggia (Venice)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.35, 0.40),
        "s3": (0.50, 0.20, 0.30),
    },
    {
        "folder": "theme_43",
        "file": "Basílica de San Pedro, Ciudad del Vaticano low light.jpg",
        "title": "St. Peter's Basilica Sunbeam Architecture",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.25, 0.30),
    },
    {
        "folder": "theme_44",
        "file": "Fontana di Trevi - Italy - Roma - Creative Commons by gnuckx (3204230942).jpg",
        "title": "Trevi Fountain Marble Architecture",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.40, 0.40),
        "s3": (0.50, 0.65, 0.30),
    },
    {
        "folder": "theme_45",
        "file": "Gardens and fountains in Villa d'Este (Tivoli) (6).jpg",
        "title": "Villa d'Este Renaissance Fountains (Tivoli)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.40, 0.40),
        "s3": (0.50, 0.60, 0.30),
    },
    {
        "folder": "theme_46",
        "file": "Czech-2013-Prague-Astronomical clock face.jpg",
        "title": "Prague Astronomical Clock Golden Dial",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.50, 0.45),
        "s3": (0.50, 0.50, 0.28),
    },

    # Nhóm 3: Âm nhạc & Tĩnh vật nghệ thuật thanh nhã (Theme 47 - 53)
    {
        "folder": "theme_47",
        "file": "Pieter Claesz - Still life with rummer, wine glass, crab and bread on a platter, with a violin and a flute on a table , 1644 - 68624 L 1.jpg",
        "title": "Pieter Claesz — Still Life with Violin & Flute",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.65, 0.55, 0.40),
        "s3": (0.75, 0.60, 0.28),
    },
    {
        "folder": "theme_48",
        "file": "Musée de la musique Paris 10022019 Harpe 1728 Hochbrucker Détail 1331.jpg",
        "title": "Classical Golden Pedal Harp (Musée de la musique)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.35, 0.40),
        "s3": (0.50, 0.25, 0.30),
    },
    {
        "folder": "theme_49",
        "file": "Bouquet of Flowers in an Urn2.jpg",
        "title": "Jan van Huysum — Bouquet of Flowers in an Urn",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.35, 0.28),
    },
    {
        "folder": "theme_50",
        "file": "Ambrosius Bosschaert the Elder (Dutch - Flower Still Life - Google Art Project.jpg",
        "title": "Ambrosius Bosschaert — Flower Still Life",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.35, 0.28),
    },
    {
        "folder": "theme_51",
        "file": "Amsterdam - Rijksmuseum 1885 - The Gallery of Honour (1st Floor) - Still Life with Silver Ewer 1655-60 by Willem Kalf.jpg",
        "title": "Willem Kalf — Still Life with Silver Ewer & Porcelain",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.35, 0.28),
    },
    {
        "folder": "theme_52",
        "file": "Violonchelo Antonio Stradivari 1700.jpg",
        "title": "Antonio Stradivari 1700 Cello",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.50, 0.42),
        "s3": (0.50, 0.45, 0.28),
    },
    {
        "folder": "theme_53",
        "file": "Sumptuous Still Life with Fruits, Pie and Goblets (SM 1041).png",
        "title": "Sumptuous Classical Still Life with Goblets",
        "s1": (0.50, 0.50, 0.90),
        "s2": (0.50, 0.50, 0.40),
        "s3": (0.65, 0.55, 0.28),
    },

    # Nhóm 4: Thiên nhiên hoàng hôn & Thiên văn cổ (Theme 54 - 60)
    {
        "folder": "theme_54",
        "file": "Claude Lorrain - Seaport with the Embarkation of the Queen of Sheba - WGA05002.jpg",
        "title": "Claude Lorrain — Golden Seaport",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.55, 0.40),
        "s3": (0.45, 0.65, 0.30),
    },
    {
        "folder": "theme_55",
        "file": "Port de mer au soleil couchant (Louvre, RF 4715).jpg",
        "title": "Claude Lorrain — Seaport at Sunset (Louvre)",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.60, 0.30),
    },
    {
        "folder": "theme_56",
        "file": "Albert Bierstadt - Among the Sierra Nevada, California - Google Art Project.jpg",
        "title": "Albert Bierstadt — Mountain Lake at Sunset",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.70, 0.30),
    },
    {
        "folder": "theme_57",
        "file": "Albert Bierstadt - Valley of the Yosemite - Google Art Project.jpg",
        "title": "Albert Bierstadt — Valley of the Yosemite",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.65, 0.30),
    },
    {
        "folder": "theme_58",
        "file": "Claude Lorrain, Landscape with Ruins, Pastoral Figures, and Trees, c. 1650, NGA 55742.jpg",
        "title": "Claude Lorrain — Classical Landscape with Ruins & Sun",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.65, 0.30),
    },
    {
        "folder": "theme_59",
        "file": "Twilight in the Wilderness by Frederic Edwin Church (3).jpg",
        "title": "Frederic Edwin Church — Twilight in the Wilderness",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.45, 0.40),
        "s3": (0.50, 0.65, 0.30),
    },
    {
        "folder": "theme_60",
        "file": "Cellarius Harmonia Macrocosmica - Planisphaerium Arateum.jpg",
        "title": "Cellarius — Harmonia Macrocosmica Celestial Planisphere",
        "s1": (0.50, 0.50, 0.95),
        "s2": (0.50, 0.50, 0.45),
        "s3": (0.50, 0.50, 0.28),
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
        fname = title[5:] if title.startswith("File:") else title
        info = p.get("imageinfo", [{}])[0]
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
    """Computes a 9:16 aspect ratio bounding box centered near (cx_frac, cy_frac)."""
    box_h = int(h * zoom)
    box_w = int(box_h * TARGET_RATIO)
    
    if box_w > w:
        box_w = w
        box_h = int(box_w / TARGET_RATIO)
    
    cx = int(w * cx_frac)
    cy = int(h * cy_frac)
    
    left = cx - box_w // 2
    top = cy - box_h // 2
    
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
    resized = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    sharpened = resized.filter(ImageFilter.UnsharpMask(radius=1.8, percent=140, threshold=2))
    
    arr = np.array(sharpened, dtype=np.float32)
    arr = arr * 0.70  # 30% reduction in luminance for crisp text contrast
    
    noise = np.random.normal(0.0, 1.8, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    
    final_img = Image.fromarray(arr)
    final_img.save(out_path, format="JPEG", quality=95)

def main():
    print("=" * 75)
    print("  HIYU ABYSS — PRODUCTION: 30 ELEGANT NON-HUMAN SUITES (THEME 31 - 60)")
    print("=" * 75)
    
    files_to_fetch = [s["file"] for s in SUITES_CONFIG]
    print(f"[*] Đang lấy danh sách URL độ phân giải cao cho {len(files_to_fetch)} kiệt tác...")
    
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
            
        try:
            src = Image.open(cached_file).convert("RGB")
            w, h = src.size
            print(f"  [i] Kích thước master: {w}x{h} px")
        except Exception as e:
            print(f"  [X] Không mở được file ảnh: {e}")
            continue
            
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
            
    print("\n" + "=" * 75)
    print(f"[✓] HOÀN TẤT TOÀN BỘ: Đã render {total_images_rendered}/90 ảnh đa góc máy đợt 2!")
    print(f"[✓] Thư mục lưu trữ: {OUTPUT_BASE}")
    print("=" * 75)

if __name__ == "__main__":
    main()
