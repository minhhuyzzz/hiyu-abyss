#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Complete 300 Posts Pipeline Synchronizer
- Merges Rows 1-250 (from live Google Sheet) + Rows 251-300 (from posts_251_300.json)
- Updates scripts/tiktok_300_posts.csv and scripts/tiktok_200_posts.csv (301 rows = 1 header + 300 rows)
- Generates missing editorial/content/TXT-0201.md through TXT-0250.md
"""

import csv
import json
import os

def map_topic(t_str):
    t_up = t_str.upper()
    if 'GIAO TIẾP' in t_up: return 'COMMUNICATION'
    if 'KỲ VỌNG' in t_up: return 'EXPECTATION'
    if 'RANH GIỚI' in t_up: return 'BOUNDARIES'
    if 'SỨC HÚT' in t_up: return 'ATTRACTION'
    return 'PSYCHOLOGY'

def main():
    # 1. Read live sheet export (Rows 1-250)
    with open('scripts/live_sheet_current.csv', encoding='utf-8') as f:
        live_rows = list(csv.reader(f))

    header = live_rows[0]
    rows_1_250 = live_rows[1:251]
    print(f"Loaded {len(rows_1_250)} rows (1-250) from live sheet export.")

    # 2. Load posts 251-300
    with open('scripts/posts_251_300.json', encoding='utf-8') as f:
        posts_251_300 = json.load(f)
    print(f"Loaded {len(posts_251_300)} posts (251-300) from JSON.")

    # 3. Format rows 251-300
    rows_251_300 = []
    for p in posts_251_300:
        row = [
            p['stt'], p['id'], p['title'], p['caption'], p['author'],
            p['hashtags'], p['format'], p['hook'], p['twist'], p['mirror'],
            p['deep'], p['full_text'], p['topic'], p['hours'], p['schedule'],
            p['concept'], 'SẴN SÀNG'
        ]
        rows_251_300.append(row)

    total_300 = rows_1_250 + rows_251_300
    print(f"Total combined rows: {len(total_300)}")
    assert len(total_300) == 300, f"Expected 300 rows, got {len(total_300)}"

    # 4. Write CSVs
    for csv_path in ['scripts/tiktok_300_posts.csv', 'scripts/tiktok_200_posts.csv']:
        with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(total_300)
        print(f"✅ Saved {csv_path} with {len(total_300)} rows.")

    # 5. Generate missing markdown files for 201-250
    os.makedirs('editorial/content', exist_ok=True)
    count_201_250 = 0
    for r in rows_1_250[200:250]:
        stt, pid, title, caption, author, hashtags, sformat, hook, twist, mirror, deep, full_txt, topic, hours, sched, concept, status = r
        theme_id = f"theme_{int(stt)}"
        top_code = map_topic(topic)
        
        # Clean title for frontmatter
        clean_title = title.replace('"', '\\"')
        
        md_content = f"""---
id: {pid}
title: "{clean_title}"
content_type: INSPIRED_ORIGINAL
author_attribution: "{author}"
topic_codes:
  - {top_code}
image_ref: "{theme_id}"
slide_format: "{sformat}"
status: APPROVED
created_at: "2026-11-15"
updated_at: "2026-11-15"
---

# {title}

> {hook} {twist}

## Diễn Giải & Chiêm Nghiệm Biên Tập
{caption}

## Cấu Trúc Trình Diễn Đa Nhịp (Slides)
- **Trang 1 (Hook):** {hook}
- **Trang 2 (Cú lật):** {twist}
- **Trang 3 (Phản tư):** {mirror}
- **Trang 4 (Đúc kết):** {deep}

## Từ Khóa & Phân Loại
{hashtags}
"""
        with open(f'editorial/content/{pid}.md', 'w', encoding='utf-8') as mf:
            mf.write(md_content)
        count_201_250 += 1

    print(f"✅ Generated {count_201_250} markdown files for 201-250 in editorial/content/.")

if __name__ == '__main__':
    main()
