#!/usr/bin/env python3
# scripts/verify_115_distinct_oil_suites_201_250.py
import os
import csv
import hashlib
from PIL import Image

OUTPUT_BASE = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"
CSV_PATH = r"c:\hiyuabyss\scripts\tiktok_200_posts.csv"

def get_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    print("=" * 60)
    print("🏛️ HIYU ABYSS — KIỂM ĐỊNH 115 KIỆT TÁC SƠN DẦU (THEME 201 - 250)")
    print("=" * 60)

    rows = list(csv.reader(open(CSV_PATH, encoding='utf-8-sig')))
    posts = rows[201:251]

    total_expected = 0
    passed_slides = 0
    errors = []

    for p in posts:
        stt = int(p[0])
        pid = p[1]
        fmt = p[6]
        theme_id = f"theme_{stt}"

        num_slides = 1 if '1 trang' in fmt else (2 if '2 trang' in fmt else 3)
        total_expected += num_slides

        theme_hashes = set()

        for s in range(1, num_slides + 1):
            slide_file = f"slide_{s}.jpg"
            p1 = os.path.join(OUTPUT_BASE, theme_id, slide_file)
            p2 = os.path.join(WEBSITE_PUBLIC, theme_id, slide_file)

            # Check existence
            if not os.path.exists(p1):
                errors.append(f"Missing in multislides: {p1}")
                continue
            if not os.path.exists(p2):
                errors.append(f"Missing in website public: {p2}")
                continue

            # Check dimensions
            with Image.open(p1) as im:
                w, h = im.size
                if (w, h) != (1080, 1920):
                    errors.append(f"Invalid dimensions for {p1}: {w}x{h} (expected 1080x1920)")
                    continue

            # Check distinctness within theme
            h1 = get_hash(p1)
            if h1 in theme_hashes:
                errors.append(f"Duplicate slide detected in {theme_id}: {slide_file}")
                continue
            theme_hashes.add(h1)

            passed_slides += 1

    print(f"\n📊 TỔNG KẾT KIỂM ĐỊNH:")
    print(f"   • Tổng số slide kỳ vọng: {total_expected}")
    print(f"   • Số slide đạt chuẩn:   {passed_slides} / {total_expected}")
    
    if errors:
        print(f"   ❌ Phát hiện {len(errors)} lỗi:")
        for e in errors[:10]:
            print(f"      - {e}")
        return False
    else:
        print(f"   ✨ HOÀN HẢO: 100% KIỆT TÁC ĐẠT CHUẨN 9:16 VÀ ĐỘC BẢN KHÔNG TRÙNG LẶP!")
        return True

if __name__ == '__main__':
    main()
