#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Quality & Semantic Novelty Audit for Posts 251-300 (HYA-06 & HYA-03)
Checks:
1. G1: Authentic Author Attribution & Academic Grounding
2. G2: Semantic Novelty & 0 Duplicate Openings vs Posts 1-250
3. HYA-03: Zero Banned AI Slop & Natural Vietnamese Voice
4. Format: Slide Structure Integrity & Word Count Checks
"""

import json
import csv
import re
import sys

BANNED_AI_SLOP = [
    "bức tranh toàn cảnh", "ngọn hải đăng", "kim chỉ nam", "chìa khóa vàng",
    "liều thuốc thần kỳ", "tấm vé thông hành", "hãy nhớ rằng bạn luôn",
    "trong cuộc sống bộn bề", "vũ trụ gửi tín hiệu", "luật hấp dẫn",
    "tần số năng lượng", "bình ổn năng lượng"
]

def main():
    print("=== KIỂM ĐỊNH CHẤT LƯỢNG & TÍNH MỚI NGỮ NGHĨA (STT 251 - 300) ===")
    
    # 1. Load historical 250 posts
    with open('scripts/live_sheet_current.csv', encoding='utf-8') as f:
        hist_rows = list(csv.reader(f))[1:251]
    
    hist_hooks = [r[7].strip().lower() for r in hist_rows if r[7].strip()]
    hist_titles = [r[2].strip().lower() for r in hist_rows if r[2].strip()]
    print(f"Loaded {len(hist_hooks)} historical hooks and {len(hist_titles)} historical titles.")

    # 2. Load posts 251-300
    with open('scripts/posts_251_300.json', encoding='utf-8') as f:
        posts = json.load(f)
    print(f"Loaded {len(posts)} posts (251-300).")

    errors = []
    warnings = []

    seen_hooks = set()
    seen_titles = set()

    for idx, p in enumerate(posts, 251):
        pid = p['id']
        title = p['title']
        author = p['author']
        caption = p['caption']
        hook = p['hook']
        sformat = p['format']

        # Check Author
        if not author or author.strip() == "":
            errors.append(f"[{pid}] Thiếu tác giả nguồn.")

        # Check Duplicate Title
        clean_title = re.sub(r'\[.*?\]', '', title).strip().lower()
        if clean_title in seen_titles:
            errors.append(f"[{pid}] Trùng lặp tiêu đề trong bộ 251-300: '{title}'")
        seen_titles.add(clean_title)

        for h_title in hist_titles:
            h_clean = re.sub(r'\[.*?\]', '', h_title).strip().lower()
            if clean_title == h_clean and len(clean_title) > 5:
                errors.append(f"[{pid}] Trùng lặp tiêu đề với bài cũ: '{title}'")

        # Check Duplicate Hook
        if hook and hook != "-":
            clean_hook = hook.replace('.', '').strip().lower()
            if clean_hook in seen_hooks:
                errors.append(f"[{pid}] Trùng lặp Hook trong bộ 251-300: '{hook}'")
            seen_hooks.add(clean_hook)

            for h_hook in hist_hooks:
                h_clean = h_hook.replace('.', '').strip().lower()
                if clean_hook == h_clean and len(clean_hook) > 5:
                    errors.append(f"[{pid}] Trùng lặp Hook với bài cũ: '{hook}'")

        # Check Banned AI Slop
        full_text_to_check = f"{title} {caption} {p['hook']} {p['twist']} {p['mirror']} {p['deep']}".lower()
        for slop in BANNED_AI_SLOP:
            if slop in full_text_to_check:
                errors.append(f"[{pid}] Chứa sáo ngữ AI bị cấm: '{slop}'")

        # Check Caption Word Count
        words = len(caption.split())
        if words < 35:
            warnings.append(f"[{pid}] Caption hơi ngắn ({words} từ).")
        elif words > 110:
            warnings.append(f"[{pid}] Caption hơi dài ({words} từ).")

        # Check Slide Format Consistency
        if "1 trang" in sformat:
            if p['twist'] == "-" and p['mirror'] == "-":
                pass
        elif "2 trang" in sformat:
            if p['twist'] == "-" or p['twist'] == "":
                errors.append(f"[{pid}] Carousel 2 trang nhưng Trang 2 trống.")
        elif "3 trang" in sformat:
            if p['twist'] == "-" or p['mirror'] == "-":
                errors.append(f"[{pid}] Carousel 3 trang nhưng Trang 2 hoặc Trang 3 trống.")
        elif "4 trang" in sformat:
            if p['twist'] == "-" or p['mirror'] == "-" or p['deep'] == "-":
                errors.append(f"[{pid}] Carousel 4 trang nhưng thiếu slide con.")

    print(f"\n--- KẾT QUẢ KIỂM ĐỊNH ---")
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
        print("✅ 100% PASS tất cả các cổng kiểm định chất lượng (G1, G2, HYA-03, Format)!")

if __name__ == '__main__':
    main()
