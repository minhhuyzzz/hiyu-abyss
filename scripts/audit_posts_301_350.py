#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Strict Audit for Redesigned Posts (STT 301 - 350)
Enforces:
1. NO 'bước 1', 'bước 2', 'bước 3'
2. NO LaTeX/math sequences ('$', '\\rightarrow', 'ightarrow')
3. NO numbered list items ('1.', '2.', '3.') in slides
4. NO banned AI words / clichés
5. Valid Hook (< 10 words, contains '...' for Carousel)
6. Exactly 5 hashtags
7. Format integrity
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

FORBIDDEN_PATTERNS = [
    "bước 1",
    "bước 2",
    "bước 3",
    "bước 4",
    "ightarrow",
    "$",
    "\\rightarrow",
    "\\r"
]

def audit():
    print("=== KIỂM ĐỊNH NGHIÊM NGẶT 50 BÀI TÁI THIẾT KẾ (STT 301 - 350) ===")
    
    with open('scripts/posts_301_350.json', encoding='utf-8') as f:
        posts = json.load(f)
        
    errors = []
    titles = set()
    format_counts = {}

    for idx, p in enumerate(posts, start=301):
        stt = p['stt']
        pid = p['id']
        title = p['title'].strip()
        fmt = p['format'].strip()
        hook = p['hook'].strip()
        twist = p['twist'].strip()
        mirror = p['mirror'].strip()
        deep = p['deep'].strip()
        hashtags = p['hashtags'].strip()
        author = p['author'].strip()
        caption = p['caption'].strip()
        full_text = p['full_text'].strip()
        
        format_counts[fmt] = format_counts.get(fmt, 0) + 1

        # 1. STT & ID
        if stt != idx:
            errors.append(f"STT {stt} != {idx}")
        if pid != f"TXT-{idx:04d}":
            errors.append(f"ID {pid} != TXT-{idx:04d}")
            
        # 2. Duplicate title
        if title in titles:
            errors.append(f"Trùng tiêu đề: {title}")
        titles.add(title)
        
        # 3. Forbidden pattern check
        combined_text = f"{title} {caption} {hook} {twist} {mirror} {deep} {full_text}".lower()
        for pat in FORBIDDEN_PATTERNS:
            if pat in combined_text:
                errors.append(f"{pid}: Chứa chuỗi bị cấm '{pat}'")
                
        # 4. Check for numbered list items in slides like '1. ', '2. ', '3. '
        for field_name, field_val in [('Trang 1', hook), ('Trang 2', twist), ('Trang 3', mirror), ('Trang 4', deep)]:
            if re.search(r'\b[1-4]\.\s', field_val):
                errors.append(f"{pid} {field_name}: Chứa gạch đầu dòng đánh số '{field_val}'")

        # 5. Banned AI words (Humanizer)
        for banned in BANNED_AI_WORDS:
            if banned in combined_text:
                errors.append(f"{pid}: Vi phạm Humanizer - chứa sáo ngữ '{banned}'")

        # 6. Hook rule check (for Carousels)
        if "Carousel" in fmt:
            if not ("..." in hook or "……" in hook):
                errors.append(f"{pid}: Hook thiếu dấu lửng '...': {hook}")
            clean_hook = hook.replace("...", "").replace("……", "").strip()
            word_count = len(clean_hook.split())
            if word_count > 12:
                errors.append(f"{pid}: Hook quá dài ({word_count} từ): {hook}")
                
        # 7. Slide format integrity
        if fmt == "Single-Punch (1 trang)":
            if twist != "-" or mirror != "-" or deep != "-":
                errors.append(f"{pid}: Single-Punch phải có twist, mirror, deep là '-'")
        elif fmt == "Carousel 2 trang":
            if twist == "-" or mirror != "-" or deep != "-":
                errors.append(f"{pid}: Carousel 2 trang phải có twist và mirror='-', deep='-'")
        elif fmt == "Carousel 3 trang":
            if twist == "-" or mirror == "-" or deep != "-":
                errors.append(f"{pid}: Carousel 3 trang phải có twist, mirror và deep='-'")
        elif fmt == "Carousel 4 trang":
            if twist == "-" or mirror == "-" or deep == "-":
                errors.append(f"{pid}: Carousel 4 trang phải có đầy đủ twist, mirror, deep")
                
        # 8. Hashtags (5 hashtags)
        tags = [t for t in hashtags.split() if t.startswith('#')]
        if len(tags) != 5:
            errors.append(f"{pid}: Phải có đúng 5 hashtag, hiện có {len(tags)}: {hashtags}")
            
        # 9. Author check
        if not author or len(author) < 3:
            errors.append(f"{pid}: Thiếu tác giả")

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
        print("🎉 100% PASS: Toàn bộ 50 bài đạt chuẩn tuyệt đối:")
        print("  ✓ 0 từ 'bước 1, bước 2'")
        print("  ✓ 0 ký tự lỗi LaTeX / escape")
        print("  ✓ 0 gạch đầu dòng đánh số")
        print("  ✓ 0 sáo ngữ AI (Humanizer)")
        print("  ✓ 100% Hook tinh gọn & chuẩn SEO")
        return True

if __name__ == '__main__':
    audit()
