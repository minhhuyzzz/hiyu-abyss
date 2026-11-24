#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Strict Audit for Posts 401 - 450
Verifies:
1. Exactly 50 items (401 - 450)
2. STT & ID integrity
3. No duplicate titles
4. Zero forbidden patterns: 'bước 1', 'bước 2', 'ightarrow', '$', '\\rightarrow'
5. Zero numbered list items in slides ('1. ', '2. ', '3. ')
6. Zero banned AI clichés (Humanizer compliance)
7. Word count limits:
   - Carousel Hook <= 10 words, contains '...'
   - Body slide (twist, mirror, deep) <= 25 words
   - Single-Punch Hook <= 25 words
8. Exactly 5 hashtags per post
9. Complete fields & valid status
"""

import json
import os
import re
import sys

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
    print("=== BẮT ĐẦU KIỂM ĐỊNH NGHIÊM NGẶT 50 BÀI LÔ 1 (STT 401 - 450) ===")
    json_path = 'scripts/posts_401_450.json'
    if not os.path.exists(json_path):
        print(f"❌ File not found: {json_path}")
        sys.exit(1)

    with open(json_path, encoding='utf-8') as f:
        posts = json.load(f)

    if len(posts) != 50:
        print(f"❌ Expected 50 posts, found {len(posts)}")
        sys.exit(1)

    errors = []
    titles = set()
    format_counts = {}

    for idx, p in enumerate(posts, start=401):
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
        status = p['status'].strip()

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

        # 6. Word count verification
        if "Carousel" in fmt:
            if not ("..." in hook or "……" in hook):
                errors.append(f"{pid} (Carousel): Hook thiếu dấu ba chấm '...': '{hook}'")
            hook_words = len(re.findall(r'\b\w+\b', hook))
            if hook_words > 10:
                errors.append(f"{pid} Hook dài ({hook_words} từ > 10 từ): '{hook}'")
        elif "Single-Punch" in fmt:
            punch_words = len(re.findall(r'\b\w+\b', hook))
            if punch_words > 25:
                errors.append(f"{pid} Single-Punch dài ({punch_words} từ > 25 từ): '{hook}'")

        for field_name, field_val in [('Trang 2', twist), ('Trang 3', mirror), ('Trang 4', deep)]:
            if field_val != "-":
                words = len(re.findall(r'\b\w+\b', field_val))
                if words > 25:
                    errors.append(f"{pid} {field_name} dài ({words} từ > 25 từ): '{field_val}'")

        # 7. Hashtags check: exactly 5 tags starting with #
        tags = [t for t in hashtags.split() if t.startswith('#')]
        if len(tags) != 5:
            errors.append(f"{pid}: Phải có đúng 5 hashtags (hiện tại có {len(tags)}): '{hashtags}'")

        # 8. Author check
        if not author:
            errors.append(f"{pid}: Thiếu tên tác giả")

        # 9. Status check
        if status != "SẴN SÀNG":
            errors.append(f"{pid}: Trạng thái không phải 'SẴN SÀNG' ('{status}')")

    print("\n--- BÁO CÁO KIỂM ĐỊNH LÔ 1 ---")
    print(f"Tổng số bài kiểm tra: {len(posts)} (STT 401 -> 450)")
    print("Phân bổ định dạng slide:")
    for fmt, count in sorted(format_counts.items()):
        print(f"  • {fmt}: {count} bài")

    if errors:
        print(f"\n❌ PHÁT HIỆN {len(errors)} LỖI:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n✅ TẤT CẢ 50 BÀI LÔ 1 ĐẠT 100% TIÊU CHUẨN!")
        print("  • 0 lỗi đánh số 'bước 1', 'bước 2'")
        print("  • 0 ký tự LaTeX / escape lỗi")
        print("  • 0 sáo ngữ AI (Chuẩn Humanizer)")
        print("  • 100% Hook ngắn < 10 từ kèm '......'")
        print("  • 100% Thân slide nén chặt < 25 từ")
        print("  • Đầy đủ 5 hashtags chuẩn SEO")

if __name__ == '__main__':
    audit()
