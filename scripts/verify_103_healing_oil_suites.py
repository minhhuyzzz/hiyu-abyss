#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Verification Suite for 103 Healing Oil Slides (Theme 251 - 300)
Kiểm tra tính toàn vẹn 100% của 103 slides độc lập trên cả 2 thư mục:
- assets/templates/multislides/theme_{stt}/
- website/public/images/themes/theme_{stt}/
"""

import os
import json
import sys
from PIL import Image

MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"
MULTISLIDES_DIR = "assets/templates/multislides"
WEBSITE_DIR = "website/public/images/themes"

TARGET_W, TARGET_H = 1080, 1920

def verify_slide(file_path):
    if not os.path.exists(file_path):
        return False, f"Tệp không tồn tại: {file_path}"
    
    sz = os.path.getsize(file_path)
    if sz < 30000:
        return False, f"Dung lượng tệp quá nhỏ ({sz} bytes): {file_path}"

    try:
        with Image.open(file_path) as im:
            if im.size != (TARGET_W, TARGET_H):
                return False, f"Kích thước sai lệch {im.size} (kỳ vọng {(TARGET_W, TARGET_H)}): {file_path}"
            if im.mode != "RGB":
                return False, f"Chế độ màu sai lệch {im.mode}: {file_path}"
    except Exception as e:
        return False, f"Tệp ảnh bị lỗi không đọc được: {e}"

    return True, sz

def main():
    print("=== KIỂM THỬ TOÀN DIỆN 103 SLIDES SƠN DẦU HYA-08 (THEME 251 - 300) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    errors = []
    total_expected = sum(len(t["slides"]) for t in manifest.values())
    checked_files = 0

    print(f"Tổng số themes cần kiểm tra: {len(manifest)}")
    print(f"Tổng số slides độc lập mỗi thư mục: {total_expected}")

    for tid, t in manifest.items():
        theme_id = t["theme_id"]
        slides = t["slides"]

        for s in slides:
            s_idx = s["slide_index"]
            
            multi_path = os.path.join(MULTISLIDES_DIR, theme_id, f"slide_{s_idx}.jpg")
            web_path = os.path.join(WEBSITE_DIR, theme_id, f"slide_{s_idx}.jpg")

            # Check multislides
            ok_multi, res_multi = verify_slide(multi_path)
            if not ok_multi:
                errors.append(f"[MULTISLIDES] {res_multi}")
            else:
                checked_files += 1

            # Check website
            ok_web, res_web = verify_slide(web_path)
            if not ok_web:
                errors.append(f"[WEBSITE] {res_web}")
            else:
                checked_files += 1

    print(f"\nTổng số tệp ảnh đã kiểm tra: {checked_files} / {total_expected * 2}")

    if errors:
        print(f"\n❌ Phát hiện {len(errors)} lỗi:")
        for e in errors[:15]:
            print("  - " + e)
        if len(errors) > 15:
            print(f"  ... và {len(errors) - 15} lỗi khác.")
        sys.exit(1)
    else:
        print("\n====================================================")
        print("🎉 100% PASS: TẤT CẢ 206 TỆP ẢNH ĐẠT CHUẨN MỸ THUẬT HYA-08 (1080x1920)!")
        print("====================================================")

if __name__ == '__main__':
    main()
