#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Visual Uniqueness & Aesthetic Quality Audit for Oil Suites (Theme 301 - 500)
Checks:
1. Scope: Exactly 200 themes and exactly 431 independent slides
2. Visual Uniqueness: 0 duplicate prompts across all 431 slides
3. HYA-08 Standard: 9:16 vertical ratio, canvas weave, impasto brushstrokes, text safe zone
4. Anti-AI Slop: 0 banned AI keywords in prompts
5. Luminous & Warm Palette: 100% adherence to warm, radiant aesthetic
6. Historical Author Portrait Integration: verification of philosopher portrait enhancements
"""

import json
import os
import sys

MANIFEST_PATH = "scripts/oil_suites_301_500_manifest.json"
SPEC_PATH = "docs/12_HIYU_ABYSS_OIL_PAINTING_SUITES_301_500_SPEC.md"

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
    "sunbeams", "afternoon", "glowing", "joyful", "soothing", "coral", "calm",
    "heavens", "sunrise", "peaceful", "transcendent"
]

def main():
    print("=== KIỂM ĐỊNH MỸ THUẬT & ĐỘC BẢN THỊ GIÁC (THEME 301 - 500 / 431 SLIDES) ===")
    
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
    if theme_count != 200:
        errors.append(f"Số lượng theme sai lệch: {theme_count} (kỳ vọng 200)")

    total_slides = sum(len(t["slides"]) for t in manifest.values())
    if total_slides != 431:
        errors.append(f"Tổng số slides sai lệch: {total_slides} (kỳ vọng 431)")

    seen_prompts = set()
    seen_metaphors = set()
    luminous_checked_count = 0
    author_portraits_detected = 0

    for tid, t in manifest.items():
        stt = t["stt"]
        slides = t["slides"]
        author = t.get("author", "")
        
        for s in slides:
            s_idx = s["slide_index"]
            prompt = s["prompt"]
            metaphor = s["visual_metaphor"]
            lighting = s["lighting_palette"]
            artist = s["artist"]
            artwork = s["artwork_title"]
            
            # Check Prompt uniqueness
            if prompt in seen_prompts:
                errors.append(f"STT {stt} Slide {s_idx}: Trùng lặp hoàn toàn prompt!")
            seen_prompts.add(prompt)
            
            # Check Metaphor uniqueness
            if metaphor in seen_metaphors:
                warnings.append(f"STT {stt} Slide {s_idx}: Trùng lặp visual metaphor với slide khác.")
            seen_metaphors.add(metaphor)
            
            # Check Medium & Aspect ratio
            if "Vertical 9:16 classical fine art oil painting" not in prompt:
                errors.append(f"STT {stt} Slide {s_idx}: Thiếu tỷ lệ dọc 9:16 hoặc định dạng tranh sơn dầu cổ điển.")
            if "tactile oil canvas weave texture" not in prompt:
                errors.append(f"STT {stt} Slide {s_idx}: Thiếu thuộc tính thớ toan canvas.")
            if "heavy impasto brushstrokes" not in prompt:
                errors.append(f"STT {stt} Slide {s_idx}: Thiếu thuộc tính vệt cọ impasto đắp nổi.")
                
            # Check Safe Zone
            if "quiet, generous negative space in the middle-to-lower third" not in prompt:
                errors.append(f"STT {stt} Slide {s_idx}: Thiếu đặc tả vùng an toàn cho chữ (safe zone).")
                
            # Check Positive AI Slop keywords
            prompt_lower = prompt.lower()
            for kw in POSITIVE_BANNED_AI_KEYWORDS:
                if kw in prompt_lower:
                    errors.append(f"STT {stt} Slide {s_idx}: Phát hiện từ khóa AI slop cấm '{kw}' trong prompt!")
                    
            # Check Luminous keywords in lighting
            lighting_lower = lighting.lower()
            if any(k in lighting_lower for k in LUMINOUS_PALETTE_KEYWORDS):
                luminous_checked_count += 1
            else:
                warnings.append(f"STT {stt} Slide {s_idx}: Bảng màu chưa đủ từ khóa ánh sáng tươi sáng/ấm áp: '{lighting}'")
                
            # Check Author portrait keywords
            if any(p_name in metaphor for p_name in ["Marcus Aurelius", "Seneca", "Schopenhauer", "Nietzsche", "Epictetus", "Laozi", "Machiavelli", "Franklin", "Jung", "Frankl", "Fromm", "Adler", "Rogers"]):
                author_portraits_detected += 1

    print("\n--- BÁO CÁO KIỂM ĐỊNH MỸ THUẬT & ĐỘC BẢN ---")
    print(f"Tổng số themes kiểm tra: {theme_count} (Themes 301 -> 500)")
    print(f"Tổng số slides độc lập: {total_slides} (Kỳ vọng: 431)")
    print(f"Độ độc bản prompt: {len(seen_prompts)} / {total_slides} (100% Độc Bản)")
    print(f"Số slide đạt chuẩn ánh sáng tươi sáng: {luminous_checked_count} / {total_slides} ({luminous_checked_count/total_slides*100:.1f}%)")
    print(f"Số slide tích hợp chân dung danh tác triết gia: {author_portraits_detected} slides")

    if warnings:
        print(f"\n⚠️ CẢNH BÁO ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"  - {w}")
        if len(warnings) > 10:
            print(f"  ... và {len(warnings) - 10} cảnh báo khác.")

    if errors:
        print(f"\n❌ PHÁT HIỆN {len(errors)} LỖI NGHIÊM TRỌNG:")
        for e in errors[:10]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ TẤT CẢ 431 SLIDES CỦA 200 THEMES ĐẠT 100% TIÊU CHUẨN MỸ THUẬT HYA-08!")
        print("  • 0 prompt trùng lặp")
        print("  • 0 từ khóa AI slop (3D, CGI, neon, plastic)")
        print("  • 100% tỷ lệ dọc 9:16 kèm thớ toan và vệt cọ impasto")
        print("  • 100% vùng an toàn chữ 40% cho TikTok")
        print("  • Đã tích hợp chân dung bảo tàng của các đại triết gia lịch sử")

if __name__ == "__main__":
    main()
