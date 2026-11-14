# -*- coding: utf-8 -*-
"""
Script đồng bộ 100 bài đăng đầu tiên từ pipeline sang tệp Markdown chuẩn HYA-04
tại c:/hiyuabyss/editorial/content/TXT-xxxx.md với status: APPROVED.
"""

import csv
import os

CSV_PATH = "c:/hiyuabyss/scripts/tiktok_150_posts.csv"
OUTPUT_DIR = "c:/hiyuabyss/editorial/content"
os.makedirs(OUTPUT_DIR, exist_ok=True)

THEME_CODE_MAP = {
    "HYPOCRISY": "HYPOCRISY",
    "DOUBLE_STANDARD": "DOUBLE_STANDARD",
    "MORALITY": "MORALITY",
    "EGO": "EGO",
    "SELF_DECEPTION": "SELF_DECEPTION",
    "SHADOW": "SHADOW",
    "MASK": "MASK",
    "POWER": "POWER",
    "MANIPULATION": "MANIPULATION",
    "FREEDOM": "FREEDOM",
    "TRUTH": "TRUTH",
    "LOVE": "LOVE",
    "LOYALTY": "LOYALTY",
    "ENVY": "ENVY",
    "CROWD": "CROWD",
    "SUFFERING": "SUFFERING",
    "IDENTITY": "IDENTITY",
    "MEANING": "MEANING",
    "SOLITUDE": "SOLITUDE",
    "STATUS": "STATUS"
}

def determine_quote_type(author):
    author_lower = author.lower()
    if any(k in author_lower for k in ["từ điển", "ghi chép", "tâm lý học đám đông", "triết học hiện sinh"]):
        return "INSPIRED_ORIGINAL"
    if any(k in author_lower for k in ["seneca", "nietzsche", "marcus aurelius", "la rochefoucauld", "carl jung", "montaigne", "erich fromm", "pascal", "schopenhauer"]):
        return "DIRECT_QUOTE"
    return "PARAPHRASE"

def main():
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    print(f"[*] Đọc {len(rows)} bài từ pipeline CSV...")
    count = 0

    for idx in range(min(100, len(rows))):
        row = rows[idx]
        stt = row[0]
        post_id = row[1]
        title = row[2]
        desc = row[3]
        author = row[4]
        hashtags = row[5]
        slide_fmt = row[6]
        slide1 = row[7]
        slide2 = row[8]
        slide3 = row[9]
        slide4 = row[10]
        full_text = row[11]
        raw_theme = row[12]
        time_slot = row[13]
        schedule = row[14]
        image_theme = row[15]

        # Extract theme code
        theme_key = raw_theme.split(" (")[0].strip()
        topic_code = THEME_CODE_MAP.get(theme_key, "PSYCHOLOGY")
        quote_type = determine_quote_type(author)

        md_content = f"""---
id: {post_id}
title: "{title.replace('"', '\\"')}"
content_type: {quote_type}
author_attribution: "{author}"
topic_codes:
  - {topic_code}
image_ref: "{image_theme}"
slide_format: "{slide_fmt}"
status: APPROVED
created_at: "2026-11-14"
updated_at: "2026-11-14"
---

# {title}

> {full_text}

## Diễn Giải & Chiêm Nghiệm Biên Tập
{desc}

## Cấu Trúc Trình Diễn Đa Nhịp (Slides)
- **Trang 1 (Hook):** {slide1}
- **Trang 2 (Cú lật):** {slide2}
- **Trang 3 (Phản tư):** {slide3}
- **Trang 4 (Đúc kết):** {slide4}

## Từ Khóa & Phân Loại
{hashtags}
"""
        file_path = os.path.join(OUTPUT_DIR, f"{post_id}.md")
        with open(file_path, "w", encoding="utf-8") as out_f:
            out_f.write(md_content)
        count += 1

    print(f"[✓] Đã tạo thành công {count} tệp Markdown chuẩn HYA-04 trong {OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
