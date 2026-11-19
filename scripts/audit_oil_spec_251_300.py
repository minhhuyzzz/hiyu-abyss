#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Visual Uniqueness & Aesthetic Quality Audit for Oil Suites (Theme 251 - 300)
Kiểm tra:
1. Quy mô: Đúng 50 themes và đúng 103 slides độc lập
2. Tính độc bản (Visual Uniqueness): 0 prompt trùng lặp
3. Chuẩn mực HYA-08: Tỷ lệ dọc 9:16, thớ vải toan, vệt cọ impasto, vùng an toàn cho chữ
4. Khử AI tuyệt đối: 0 từ khóa AI slop (3D, CGI, plastic, neon, etc.) trong phần mô tả cảnh
5. Tông màu ấm áp & Ánh sáng: 100% tuân thủ định hướng 'tươi sáng, đừng âm u nữa'
"""

import json
import os
import sys

MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"
SPEC_PATH = "docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md"

POSITIVE_BANNED_AI_KEYWORDS = [
    "3d render", "unreal engine", "octane render", "hyperrealistic", "photorealistic",
    "plastic skin", "smooth airbrushed", "cyberpunk", "neon glow", "vector art",
    "anime style", "digital drawing"
]

LUMINOUS_PALETTE_KEYWORDS = [
    "morning", "sun", "golden", "amber", "warm", "serene", "daylight",
    "twilight", "rose", "pearl", "luminous", "dappled", "radiant", "spring",
    "summer", "azure", "emerald", "peach", "ochre", "celestial", "bliss",
    "clarity", "tranquil", "sunlight", "sunburst", "rainbow", "light",
    "rays", "afternoon", "glowing", "joyful", "soothing", "coral", "calm"
]

def main():
    print("=== KIỂM ĐỊNH MỸ THUẬT & ĐỘC BẢN THỊ GIÁC (THEME 251 - 300 / 103 SLIDES) ===")
    
    if not os.path.exists(MANIFEST_PATH):
        print(f"❌ Không tìm thấy manifest: {MANIFEST_PATH}")
        sys.exit(1)
        
    if not os.path.exists(SPEC_PATH):
        print(f"❌ Không tìm thấy spec markdown: {SPEC_PATH}")
        sys.exit(1)

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        spec_text = f.read()

    errors = []
    warnings = []

    # 1. Kiểm tra quy mô
    theme_count = len(manifest)
    if theme_count != 50:
        errors.append(f"Số lượng theme sai lệch: {theme_count} (kỳ vọng 50)")

    total_slides = sum(len(t["slides"]) for t in manifest.values())
    if total_slides != 103:
        errors.append(f"Tổng số slides sai lệch: {total_slides} (kỳ vọng 103)")

    seen_prompts = set()
    seen_metaphors = set()
    luminous_checked_count = 0

    for tid, t in manifest.items():
        stt = t["stt"]
        slides = t["slides"]
        
        for s in slides:
            s_idx = s["slide_index"]
            prompt = s["prompt"]
            metaphor = s["visual_metaphor"]
            lighting = s["lighting_palette"]
            artist = s["artist"]
            artwork = s["artwork_title"]
            
            # Check Prompt uniqueness
            if prompt in seen_prompts:
                errors.append(f"[{tid} - Slide {s_idx}] Prompt bị trùng lặp!")
            seen_prompts.add(prompt)
            
            # Check Metaphor uniqueness
            if metaphor in seen_metaphors:
                warnings.append(f"[{tid} - Slide {s_idx}] Ý niệm thị giác gần tương tự một slide khác: '{metaphor[:40]}...'")
            seen_metaphors.add(metaphor)
            
            # Check HYA-08 attributes
            p_lower = prompt.lower()
            if "vertical 9:16" not in p_lower:
                errors.append(f"[{tid} - Slide {s_idx}] Thiếu khai báo tỷ lệ 'Vertical 9:16'")
            if "impasto" not in p_lower:
                errors.append(f"[{tid} - Slide {s_idx}] Thiếu thuộc tính vệt cọ đắp nổi 'impasto'")
            if "canvas weave" not in p_lower:
                errors.append(f"[{tid} - Slide {s_idx}] Thiếu thuộc tính toan vải 'canvas weave'")
            if "no text" not in p_lower:
                errors.append(f"[{tid} - Slide {s_idx}] Thiếu vùng an toàn 'NO text'")
            if "no digital cgi rendering" not in p_lower:
                errors.append(f"[{tid} - Slide {s_idx}] Thiếu điều kiện âm tính 'NO digital CGI rendering'")
                
            # Check Positive Banned AI keywords in scene description (excluding the negative safe zone)
            scene_part = f"{metaphor} {lighting}".lower()
            for b_word in POSITIVE_BANNED_AI_KEYWORDS:
                if b_word in scene_part:
                    errors.append(f"[{tid} - Slide {s_idx}] Chứa từ khóa AI bị cấm: '{b_word}'")
                    
            # Check Luminous & Warm keywords
            has_luminous = any(k in lighting.lower() or k in metaphor.lower() for k in LUMINOUS_PALETTE_KEYWORDS)
            if has_luminous:
                luminous_checked_count += 1
            else:
                warnings.append(f"[{tid} - Slide {s_idx}] Bảng màu có thể chưa đủ ấm áp/tươi sáng: '{lighting}'")

    print(f"Tổng số themes kiểm định: {theme_count}/50")
    print(f"Tổng số slides kiểm định: {total_slides}/103")
    print(f"Số slides đạt chuẩn ánh sáng ấm áp/tươi sáng: {luminous_checked_count}/103")
    print(f"Dung lượng tài liệu Spec: {len(spec_text.splitlines())} dòng ({len(spec_text):,} ký tự)")

    print("\n--- KẾT QUẢ KIỂM ĐỊNH ---")
    if warnings:
        print(f"⚠️ Cảnh báo ({len(warnings)}):")
        for w in warnings:
            print("  - " + w)
    else:
        print("✅ 0 Cảnh báo.")

    if errors:
        print(f"❌ Phát hiện {len(errors)} lỗi:")
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    else:
        print("✅ 100% PASS tất cả các tiêu chí mỹ thuật HYA-08 (50 themes / 103 slides độc lập)!")

if __name__ == '__main__':
    main()
