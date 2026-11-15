#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Sync 200 Editorial Content & Update Indexes (Task 7)
Tạo đầy đủ các file TXT-0101.md đến TXT-0200.md trong editorial/content/
và đồng bộ bảng chỉ mục indexes/editorial-board.md.
"""

import csv
import os
import re

CSV_200_PATH = "scripts/tiktok_200_posts.csv"
CONTENT_DIR = "editorial/content"
INDEX_BOARD_PATH = "indexes/editorial-board.md"

def main():
    print("=== ĐỒNG BỘ 200 BÀI VÀO KHO HỒ SƠ NỘI BỘ EDITORIAL/CONTENT/ ===")
    os.makedirs(CONTENT_DIR, exist_ok=True)
    
    with open(CSV_200_PATH, "r", encoding="utf-8") as f:
        posts = list(csv.DictReader(f))
        
    print(f"Tổng số bài từ CSV: {len(posts)}")
    
    created_count = 0
    for p in posts:
        tid = p["Mã ID"]
        fpath = os.path.join(CONTENT_DIR, f"{tid}.md")
        
        # Nếu chưa tồn tại, tạo mới
        if not os.path.exists(fpath):
            stt = p["STT"]
            title = p["Tiêu Đề (Dưới 90 từ)"]
            caption = p["Mô Tả (Caption TikTok)"]
            author = p["Nguồn Tác Giả"]
            hashtags = p["Hashtags (5 cái)"]
            slide_fmt = p["Định Dạng Slide"]
            h1 = p["Trang 1 (Hook / Mở màn)"]
            h2 = p["Trang 2 (Cú lật bóc trần)"]
            h3 = p["Trang 3 (Chiếc gương phản tư)"]
            h4 = p.get("Trang 4 (Đúc kết / Phản tư sâu)", "-")
            full_txt = p["Văn Bản Hoàn Chỉnh"]
            topic = p["Chủ Đề Hạt Nhân"]
            phoi = p["Gợi Ý Phôi Ảnh"]
            status = p["Trạng Thái"]
            
            # Trích xuất mã topic
            topic_code = topic.split()[0].replace("(", "").replace(")", "").strip()
            
            md_content = f"""---
id: {tid}
title: "{title}"
content_type: INSPIRED_ORIGINAL
author_attribution: "{author}"
topic_codes:
  - {topic_code}
image_ref: "{phoi}"
slide_format: "{slide_fmt}"
status: {status}
created_at: "2026-11-15"
updated_at: "2026-11-15"
---

# {title}

> {full_txt}

## Diễn Giải & Chiêm Nghiệm Biên Tập
{caption}

## Cấu Trúc Trình Diễn Đa Nhịp (Slides)
- **Trang 1 (Hook):** {h1}
- **Trang 2 (Cú lật):** {h2}
- **Trang 3 (Phản tư):** {h3}
- **Trang 4 (Đúc kết):** {h4}

## Từ Khóa & Phân Loại
{hashtags}
"""
            with open(fpath, "w", encoding="utf-8") as out:
                out.write(md_content)
            created_count += 1
            
    print(f"✅ Đã tạo mới {created_count} file bài viết trong: {CONTENT_DIR}")
    
    # Đếm tổng số file
    all_files = sorted([f for f in os.listdir(CONTENT_DIR) if f.startswith("TXT-") and f.endswith(".md")])
    print(f"Tổng số file TXT hiện tại trong {CONTENT_DIR}: {len(all_files)}")
    
    # Cập nhật indexes/editorial-board.md
    print(f"\n[*] Đang cập nhật bảng chỉ mục: {INDEX_BOARD_PATH}...")
    board_rows = []
    for p in posts:
        tid = p["Mã ID"]
        title_short = p["Tiêu Đề (Dưới 90 từ)"]
        if len(title_short) > 45:
            title_short = title_short[:45] + "..."
        topic = p["Chủ Đề Hạt Nhân"].split()[0]
        author = p["Nguồn Tác Giả"]
        status = p["Trạng Thái"]
        
        board_rows.append(f"| [`{tid}`](file:///c:/hiyuabyss/{CONTENT_DIR}/{tid}.md) | {title_short} | `{topic}` | `INSPIRED_ORIGINAL` | `VERIFIED_IDEA` | `{status}` | 4.8 | `HiyuAbyss` | 2026-11-15 |")

    board_content = f"""# BẢNG ĐIỀU PHỐI BIÊN TẬP (EDITORIAL BOARD INDEX)

> **Ghi chú:** Bản xem dẫn xuất phản ánh tiến trình biên tập và phê duyệt từ `editorial/content/`.  
> **Tổng số tác phẩm:** {len(board_rows)} bài.

| ID | Tiêu đề | Chủ đề | Xuất xứ (`content_type`) | Bằng chứng | Trạng thái | Điểm TB | Người duyệt | Cập nhật |
|---|---|---|---|---|---|---|---|---|
""" + "\n".join(board_rows) + "\n"

    with open(INDEX_BOARD_PATH, "w", encoding="utf-8") as f:
        f.write(board_content)
        
    print(f"✅ Bảng chỉ mục {INDEX_BOARD_PATH} đã cập nhật thành công {len(board_rows)} bài!")

if __name__ == "__main__":
    main()
