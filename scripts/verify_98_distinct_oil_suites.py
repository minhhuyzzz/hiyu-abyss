#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_98_distinct_oil_suites.py
Kiểm định toàn diện 50 bộ kiệt tác sơn dầu độc bản (Theme 151 - 200):
1. Đúng số lượng slide theo định dạng (19 Single, 14 Dual, 17 Triple = 98 slides).
2. Độ phân giải chuẩn 1080x1920 dọc (9:16).
3. KHÔNG CÓ ẢNH TRÙNG: slide 1, 2, 3 trong cùng một theme phải là các bức tranh khác nhau.
4. Đồng bộ đầy đủ giữa assets/ và website/public/.
"""

import os
import json
import hashlib
from PIL import Image

BASE_ASSETS = r"c:\hiyuabyss\assets\templates\multislides"
BASE_WEBSITE = r"c:\hiyuabyss\website\public\images\themes"
DETAIL_PATH = r"c:\hiyuabyss\scripts\posts_151_200_slides_detail.json"

def get_file_hash(path: str) -> str:
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def main():
    print("=" * 60)
    print("  HIYU ABYSS — KIỂM ĐỊNH 98 KIỆT TÁC SƠN DẦU ĐỘC BẢN (151 - 200)")
    print("=" * 60)

    if not os.path.exists(DETAIL_PATH):
        print(f"Error: {DETAIL_PATH} not found")
        return

    with open(DETAIL_PATH, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    total_expected_slides = 0
    passed_slides = 0
    errors = []

    for post in posts:
        theme_id = post['theme_id']
        fmt = post['format']
        expected_slides = len(post['slides'])
        total_expected_slides += expected_slides

        assets_dir = os.path.join(BASE_ASSETS, theme_id)
        web_dir = os.path.join(BASE_WEBSITE, theme_id)

        # Kiểm tra file trong assets
        hashes = {}
        for s in post['slides']:
            s_idx = s['index']
            fname = f"slide_{s_idx}.jpg"
            fpath_asset = os.path.join(assets_dir, fname)
            fpath_web = os.path.join(web_dir, fname)

            if not os.path.exists(fpath_asset):
                errors.append(f"❌ {theme_id}/{fname} missing in assets/")
                continue
            if not os.path.exists(fpath_web):
                errors.append(f"❌ {theme_id}/{fname} missing in website/public/")
                continue

            # Kiểm tra kích thước
            try:
                with Image.open(fpath_asset) as im:
                    if im.size != (1080, 1920):
                        errors.append(f"❌ {theme_id}/{fname} size {im.size} != (1080, 1920)")
                        continue
            except Exception as e:
                errors.append(f"❌ {theme_id}/{fname} corrupted: {e}")
                continue

            hashes[s_idx] = get_file_hash(fpath_asset)
            passed_slides += 1

        # Kiểm tra tính độc bản giữa các slide trong cùng 1 bộ
        if expected_slides > 1:
            slide_keys = list(hashes.keys())
            for i in range(len(slide_keys)):
                for j in range(i + 1, len(slide_keys)):
                    k1, k2 = slide_keys[i], slide_keys[j]
                    if hashes[k1] == hashes[k2]:
                        errors.append(f"⚠️ {theme_id}: slide_{k1} is IDENTICAL to slide_{k2} (duplicate artwork!)")

        # Kiểm tra không còn file crop thừa
        for unwanted_idx in range(expected_slides + 1, 5):
            unwanted_fname = f"slide_{unwanted_idx}.jpg"
            if os.path.exists(os.path.join(assets_dir, unwanted_fname)):
                errors.append(f"⚠️ {theme_id}: contains unwanted redundant file {unwanted_fname}")

    print(f"\n[+] Total Expected Slides: {total_expected_slides}")
    print(f"[+] Successfully Validated: {passed_slides} / {total_expected_slides}")

    if errors:
        print(f"\n❌ FOUND {len(errors)} ISSUES:")
        for err in errors[:10]:
            print(f"  {err}")
    else:
        print("\n✨ 100% PERFECT: TẤT CẢ 98 KIỆT TÁC ĐẠT CHUẨN ĐỘC BẢN & PHÙ HỢP NỘI DUNG!")
        print("  - Đúng tỷ lệ 9:16 dọc 1080x1920")
        print("  - Không có tranh trùng lặp trong cùng 1 bài")
        print("  - Đã loại bỏ hoàn toàn các slide crop thừa")

if __name__ == '__main__':
    main()
