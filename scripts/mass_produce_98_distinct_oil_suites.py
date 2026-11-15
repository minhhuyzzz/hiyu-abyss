#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/mass_produce_98_distinct_oil_suites.py
Chế tác 98 kiệt tác sơn dầu độc bản (Theme 151 - 200) theo chuẩn HYA-08:
- Mỗi slide là 1 kiệt tác độc lập hoàn toàn, khớp chính xác với nội dung từng nhịp tư tưởng.
- Tải file độ phân giải cao từ Wikimedia Commons vào raw_cache.
- Áp dụng chuẩn HYA-08 Anti-AI Standard:
  + Cắt cúp tỷ lệ 9:16 dọc (1080x1920) chuẩn tiêu cự nghệ thuật.
  + Cân bằng màu khoáng tự nhiên (-4% bão hòa khử chói kỹ thuật số).
  + Phủ vi hạt toan vải hữu cơ (Organic Canvas Grain).
  + Micro-contrast Unsharp Mask làm nổi gờ sơn dầu impasto vật lý.
- Lưu đồng thời vào:
  + assets/templates/multislides/{theme_id}/slide_{idx}.jpg
  + website/public/images/themes/{theme_id}/slide_{idx}.jpg
- Xóa các file crop thừa của các bài Single-Punch (chỉ giữ slide_1) và Carousel 2 trang (chỉ giữ slide_1, slide_2).
"""

import os
import json
import time
import urllib.request
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

OUTPUT_BASE = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"
CACHE_DIR = r"c:\hiyuabyss\assets\templates\raw_cache"
RESOLVED_PATH = r"c:\hiyuabyss\scripts\resolved_98_distinct_oil_art.json"

os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(WEBSITE_PUBLIC, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H

USER_AGENT = "HiyuAbyssResearchBot/2.0 (https://hiyuabyss.local; contact: research@hiyuabyss.org)"

def download_raw_image(url: str, cache_path: str) -> bool:
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 20000:
        return True
    
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = resp.read()
                if len(data) > 10000:
                    with open(cache_path, 'wb') as f:
                        f.write(data)
                    return True
        except Exception as e:
            time.sleep(2 * attempt)
    return False

def process_and_purify_oil_painting(raw_im: Image.Image) -> Image.Image:
    """
    Quy chuẩn xử lý kiệt tác sơn dầu (HYA-08):
    1. Smart Crop trung tâm theo tỷ lệ 9:16.
    2. Lanczos downsampling về 1080x1920.
    3. Cân bằng sắc tố sơn dầu tự nhiên.
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

    # Khử chói kỹ thuật số: giảm nhẹ 4% bão hòa
    enhancer = ImageEnhance.Color(resized)
    toned = enhancer.enhance(0.96)

    # Tinh chỉnh độ tương phản nhẹ
    contrast_enhancer = ImageEnhance.Contrast(toned)
    contrasted = contrast_enhancer.enhance(1.02)

    # Thêm vi hạt toan vải hữu cơ (Organic Canvas Grain)
    img_array = np.array(contrasted, dtype=np.float32)
    noise = np.random.normal(loc=0.0, scale=3.5, size=img_array.shape)
    noisy_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    canvas_im = Image.fromarray(noisy_array)

    # Micro-contrast Unsharp Mask làm nổi gờ sơn dầu
    purified = canvas_im.filter(ImageFilter.UnsharpMask(radius=1.5, percent=125, threshold=3))

    return purified

def main():
    if not os.path.exists(RESOLVED_PATH):
        print(f"Error: {RESOLVED_PATH} does not exist!")
        return

    with open(RESOLVED_PATH, 'r', encoding='utf-8') as f:
        resolved = json.load(f)

    print(f"Loaded {len(resolved)} resolved artworks.")

    # Nhóm theo theme để dọn dẹp file crop thừa
    theme_slides_processed = {}

    success_count = 0
    fail_count = 0

    for key, info in resolved.items():
        theme_id = info['theme_id']
        slide_idx = info['slide']
        dl_url = info.get('url')
        art_title = info.get('artwork_name', 'Masterpiece')

        if not dl_url:
            print(f"⚠️ {key}: No URL found")
            fail_count += 1
            continue

        # Đặt tên file cache an toàn
        safe_cache_name = f"{key}.jpg"
        cache_file = os.path.join(CACHE_DIR, safe_cache_name)

        if not download_raw_image(dl_url, cache_file):
            print(f"❌ Failed to download {key} from {dl_url}")
            fail_count += 1
            continue

        try:
            with Image.open(cache_file) as raw_im:
                processed_im = process_and_purify_oil_painting(raw_im.convert('RGB'))

                # Lưu vào assets/templates/multislides
                theme_out_dir = os.path.join(OUTPUT_BASE, theme_id)
                os.makedirs(theme_out_dir, exist_ok=True)
                out_path_1 = os.path.join(theme_out_dir, f"slide_{slide_idx}.jpg")
                processed_im.save(out_path_1, 'JPEG', quality=95, optimize=True)

                # Lưu vào website/public/images/themes
                web_theme_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
                os.makedirs(web_theme_dir, exist_ok=True)
                out_path_2 = os.path.join(web_theme_dir, f"slide_{slide_idx}.jpg")
                processed_im.save(out_path_2, 'JPEG', quality=95, optimize=True)

                if theme_id not in theme_slides_processed:
                    theme_slides_processed[theme_id] = set()
                theme_slides_processed[theme_id].add(slide_idx)

                success_count += 1
                if success_count % 10 == 0 or success_count == len(resolved):
                    print(f"✅ Processed {success_count}/{len(resolved)} slides -> {key}: {art_title}")
        except Exception as e:
            print(f"❌ Error processing {key}: {e}")
            fail_count += 1

    # Dọn dẹp file crop cũ thừa
    print("\n🧹 Cleaning up old duplicate crops for single/2-slide themes...")
    cleaned_count = 0
    for theme_id, slides in theme_slides_processed.items():
        max_slide = max(slides)
        # Các slide lớn hơn max_slide là slide crop cũ thừa
        for old_idx in [2, 3]:
            if old_idx > max_slide:
                for base in [OUTPUT_BASE, WEBSITE_PUBLIC]:
                    old_path = os.path.join(base, theme_id, f"slide_{old_idx}.jpg")
                    if os.path.exists(old_path):
                        os.remove(old_path)
                        cleaned_count += 1

    print(f"🎉 Production Complete! Success: {success_count} | Failed: {fail_count} | Cleaned old crops: {cleaned_count}")

if __name__ == '__main__':
    main()
