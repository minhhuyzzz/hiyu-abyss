#!/usr/bin/env python3
# scripts/mass_produce_distinct_oil_suites_121_150.py - Tải và chế tác 47 kiệt tác sơn dầu độc bản (Theme 121 - 150)
import os
import json
import time
import urllib.request
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

OUTPUT_BASE = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"
CACHE_DIR = r"c:\hiyuabyss\assets\templates\raw_cache"

os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(WEBSITE_PUBLIC, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H

def process_and_purify_oil_painting(raw_im: Image.Image) -> Image.Image:
    """
    Quy chuẩn xử lý kiệt tác sơn dầu (HYA-08):
    1. Smart Crop trung tâm theo tỷ lệ 9:16.
    2. Lanczos downsampling về 1080x1920.
    3. Cân bằng sắc tố sơn dầu tự nhiên (mineral ochre/blue).
    4. Phủ vi hạt toan vải hữu cơ (Organic Canvas Grain).
    5. Unsharp mask vi mô nổi rõ vân cọ impasto vật lý.
    """
    w, h = raw_im.size
    current_ratio = w / h
    
    if abs(current_ratio - TARGET_RATIO) > 0.01:
        if current_ratio > TARGET_RATIO:
            new_w = int(h * TARGET_RATIO)
            left = (w - new_w) // 2
            im = raw_im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / TARGET_RATIO)
            top = (h - new_h) // 2
            im = raw_im.crop((0, top, w, top + new_h))
    else:
        im = raw_im

    resized = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # 2. Color tuning (-4% saturation to return to mineral pigments)
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    
    # 3. Organic canvas grain
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    
    # 4. Impasto sharpness
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened

def run_mass_production():
    with open("scripts/resolved_47_distinct_oil_art.json", "r", encoding="utf-8") as f:
        resolved = json.load(f)

    print(f"=== MASS PRODUCING 47 DISTINCT OIL ARTWORKS (HYA-08) ===")
    print(f"Total resolved items to process: {len(resolved)}")
    
    success_count = 0
    fail_count = 0

    for key, data in resolved.items():
        parts = key.split("_")
        theme_id = f"{parts[0]}_{parts[1]}"
        slide_idx = parts[3]
        
        dl_url = data["url"]
        if not dl_url:
            print(f"❌ {key}: No valid URL")
            fail_count += 1
            continue

        raw_path = os.path.join(CACHE_DIR, f"{key}_raw.jpg")
        
        # Download if not cached
        if not os.path.exists(raw_path) or os.path.getsize(raw_path) < 1000:
            print(f"⬇️ Downloading {key} ({data['title'][:35]}...)...")
            try:
                # Strip extraneous query parameters that might confuse CDN
                clean_url = dl_url.split("?")[0] if "?" in dl_url else dl_url
                req = urllib.request.Request(clean_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req, timeout=25) as resp:
                    with open(raw_path, "wb") as f_out:
                        f_out.write(resp.read())
            except Exception as e:
                # Fallback to original URL
                try:
                    req = urllib.request.Request(dl_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                    with urllib.request.urlopen(req, timeout=25) as resp:
                        with open(raw_path, "wb") as f_out:
                            f_out.write(resp.read())
                except Exception as e2:
                    print(f"  ❌ Download failed for {key}: {e2}")
                    fail_count += 1
                    continue
                
        # Process and save
        try:
            raw_im = Image.open(raw_path).convert("RGB")
            processed = process_and_purify_oil_painting(raw_im)
            
            # 1. Save to multislides
            theme_out = os.path.join(OUTPUT_BASE, theme_id)
            os.makedirs(theme_out, exist_ok=True)
            out_file = os.path.join(theme_out, f"slide_{slide_idx}.jpg")
            processed.save(out_file, "JPEG", quality=95, optimize=True)
            
            # 2. Save to website public
            web_out = os.path.join(WEBSITE_PUBLIC, theme_id)
            os.makedirs(web_out, exist_ok=True)
            web_file = os.path.join(web_out, f"slide_{slide_idx}.jpg")
            processed.save(web_file, "JPEG", quality=95, optimize=True)
            
            success_count += 1
            print(f"✅ {key} -> {out_file} (1080x1920, {os.path.getsize(out_file)} bytes)")
        except Exception as e:
            print(f"  ❌ Processing failed for {key}: {e}")
            fail_count += 1

    print(f"\n🎉 Finished: {success_count} succeeded | {fail_count} failed")

if __name__ == "__main__":
    run_mass_production()
