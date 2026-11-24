#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Audit Quality, SEO, Uniqueness & Humanizer Compliance (Posts 301-350)
"""

import json
import os
import re

BANNED_AI_WORDS = [
    "không chỉ",
    "mà còn",
    "tấm bình phong",
    "chất xúc tác",
    "minh chứng rõ nét",
    "bệ phóng",
    "dã tâm",
    "cán cân công lý",
    "hãy nhớ rằng",
    "đây là lời nhắc nhở",
    "chìa khóa vàng",
    "bức tranh toàn cảnh"
]

def audit():
    print("=== KIỂM ĐỊNH TOÀN DIỆN 50 BÀI ĐĂNG (STT 301 - 350) ===")
    
    with open('scripts/posts_301_350.json', encoding='utf-8') as f:
        posts = json.load(f)
        
    errors = []
    titles = set()
    ids = set()
    
    # Check against previous posts 1-300 if available
    prev_titles = set()
    if os.path.exists('scripts/posts_251_300.json'):
        with open('scripts/posts_251_300.json', encoding='utf-8') as f:
            for p in json.load(f):
                prev_titles.add(p['title'].strip())

    format_counts = {}

    for idx, p in enumerate(posts, start=301):
        stt = p['stt']
        pid = p['id']
        title = p['title'].strip()
        fmt = p['format'].strip()
        hook = p['hook'].strip()
        hashtags = p['hashtags'].strip()
        author = p['author'].strip()
        caption = p['caption'].strip()
        
        format_counts[fmt] = format_counts.get(fmt, 0) + 1

        # 1. STT & ID check
        if stt != idx:
            errors.append(f"STT {stt} không khớp index {idx}")
        expected_id = f"TXT-{idx:04d}"
        if pid != expected_id:
            errors.append(f"ID {pid} không khớp {expected_id}")
            
        # 2. Duplicate title check
        if title in titles:
            errors.append(f"Trùng lặp tiêu đề trong bộ 301-350: {title}")
        titles.add(title)
        
        if title in prev_titles:
            errors.append(f"Trùng lặp tiêu đề với bộ 251-300: {title}")
            
        # 3. Format & Slide integrity
        if fmt == "Single-Punch (1 trang)":
            if p['twist'] != "-" or p['mirror'] != "-" or p['deep'] != "-":
                errors.append(f"{pid}: Single-Punch phải có twist, mirror, deep là '-'")
        elif fmt == "Carousel 2 trang":
            if p['twist'] == "-" or p['mirror'] != "-" or p['deep'] != "-":
                errors.append(f"{pid}: Carousel 2 trang phải có twist và mirror='-', deep='-'")
        elif fmt == "Carousel 3 trang":
            if p['twist'] == "-" or p['mirror'] == "-" or p['deep'] != "-":
                errors.append(f"{pid}: Carousel 3 trang phải có twist, mirror và deep='-'")
        elif fmt == "Carousel 4 trang":
            if p['twist'] == "-" or p['mirror'] == "-" or p['deep'] == "-":
                errors.append(f"{pid}: Carousel 4 trang phải có đầy đủ twist, mirror, deep")
        else:
            errors.append(f"{pid}: Định dạng lạ: {fmt}")
            
        # 4. Hook rule check (for Carousels)
        if "Carousel" in fmt:
            if not ("..." in hook or "……" in hook):
                errors.append(f"{pid}: Hook carousel thiếu dấu lửng '...': {hook}")
            clean_hook = hook.replace("...", "").replace("……", "").strip()
            word_count = len(clean_hook.split())
            if word_count > 15:
                errors.append(f"{pid}: Hook quá dài ({word_count} từ): {hook}")
                
        # 5. Hashtag check (5 hashtags)
        tags = [t for t in hashtags.split() if t.startswith('#')]
        if len(tags) != 5:
            errors.append(f"{pid}: Phải có đúng 5 hashtag, hiện có {len(tags)}: {hashtags}")
            
        # 6. Author check
        if not author or len(author) < 3:
            errors.append(f"{pid}: Thiếu tên tác giả học thuật")
            
        # 7. Humanizer check (No banned AI phrases)
        full_text_to_check = f"{title} {caption} {p['full_text']} {p['twist']} {p['mirror']}".lower()
        for banned in BANNED_AI_WORDS:
            if banned in full_text_to_check:
                errors.append(f"{pid}: Vi phạm Humanizer - chứa sáo ngữ AI '{banned}'")

    print("\n--- PHÂN BỔ ĐỊNH DẠNG ---")
    for fmt, count in format_counts.items():
        print(f"  • {fmt}: {count} bài")
        
    print("\n--- KẾT QUẢ KIỂM ĐỊNH ---")
    if errors:
        print(f"❌ Phát hiện {len(errors)} lỗi:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("🎉 100% PASS: Toàn bộ 50 bài đạt chuẩn chất lượng HYA-03, SEO 5 tầng và Humanizer!")
        return True

if __name__ == '__main__':
    audit()
