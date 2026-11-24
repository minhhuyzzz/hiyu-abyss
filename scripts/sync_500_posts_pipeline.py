#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Complete 500 Posts Pipeline Synchronizer
- Reads posts_301_350.json, posts_351_400.json, posts_401_450.json, posts_451_500.json (200 posts)
- Generates editorial/content/TXT-0301.md through TXT-0500.md
- Updates website/publication-manifest.yaml with all 500 public_content_ids
- Triggers node scripts/build-content-cache.mjs and build-atlas-data.mjs
"""

import json
import os
import subprocess
import yaml

TOPIC_MAP = {
    'TRÍ TUỆ KHẮC KỶ': 'STOIC_SERENITY',
    'TRIẾT HỌC KHẮC KỶ': 'STOIC_SERENITY',
    'XUNG ĐỘT & RANH GIỚI': 'BOUNDARIES',
    'TÂM LÝ HỌC TIỀN BẠC': 'MONEY_PSYCHOLOGY',
    'TRÍ TUỆ CUỘC SỐNG': 'EXISTENCE',
    'THẤU THỊ XÃ HỘI': 'CROWD',
    'TÂM LÝ HỌC CHIỀU SÂU': 'SHADOW',
    'CHỮA LÀNH & TỰ TRẮC ẨN': 'SELF_COMPASSION',
    'MỐI QUAN HỆ & TÌNH CẢM': 'LOVE',
    'THAO TÚNG & ÁI KỶ': 'MANIPULATION',
    'Ý NGHĨA SỐNG': 'MEANING',
    'BẢN LĨNH & NỘI LỰC': 'RESILIENCE',
    'BẢN THÂN & CÁ TÍNH': 'IDENTITY',
    'NỘI TÂM & SANG CHẤN': 'SUFFERING',
    'ĐẠO ĐỨC & NHÂN CÁCH': 'MORALITY',
    'CHĂM SÓC NỘI TÂM': 'SERENITY',
    'MỐI QUAN HỆ ĐỘC HẠI': 'MANIPULATION',
    'TÌNH YÊU & GẮN KẾT': 'AUTHENTIC_CONNECTION',
    'XÃ HỘI & ĐÁM ĐÔNG': 'CROWD',
    'CẢM XÚC & NỘI TÂM': 'SERENITY',
    'TỰ DO Ý CHÍ': 'FREEDOM',
    'GIA ĐÌNH & QUAN HỆ': 'CONNECTION',
    'GIAO TIẾP TINH VI': 'COMMUNICATION',
    'ĐẠO ĐỨC GIẢ & MẶT NẠ': 'HYPOCRISY'
}

def resolve_topic(raw_topic):
    if not raw_topic:
        return 'PSYCHOLOGY'
    for k, v in TOPIC_MAP.items():
        if k in raw_topic:
            return v
    return 'PSYCHOLOGY'

def main():
    post_files = [
        'scripts/posts_301_350.json',
        'scripts/posts_351_400.json',
        'scripts/posts_401_450.json',
        'scripts/posts_451_500.json'
    ]

    all_200 = []
    for pf in post_files:
        with open(pf, encoding='utf-8') as f:
            data = json.load(f)
            all_200.extend(data)

    print(f"Loaded {len(all_200)} posts from 301 to 500.")
    assert len(all_200) == 200, f"Expected 200 posts, got {len(all_200)}"

    os.makedirs('editorial/content', exist_ok=True)
    created_count = 0

    for p in all_200:
        stt = int(p['stt'])
        pid = p.get('id') or f"TXT-{stt:04d}"
        title = p['title']
        caption = p['caption']
        author = p['author']
        hashtags = p.get('hashtags', '')
        sformat = p.get('format', 'Carousel 3 trang')
        hook = p.get('hook', '')
        twist = p.get('twist', '')
        mirror = p.get('mirror', '')
        deep = p.get('deep', '-')
        full_text = p.get('full_text', '')
        topic_raw = p.get('topic', '')
        topic_code = resolve_topic(topic_raw)
        theme_id = f"theme_{stt}"

        # Clean title for frontmatter
        clean_title = title.replace('"', '\\"')

        # Construct quote
        if twist and twist != '-':
            quote_text = f"{hook} {twist}".strip()
        else:
            quote_text = (full_text or hook).strip()

        md_content = f"""---
id: {pid}
title: "{clean_title}"
content_type: INSPIRED_ORIGINAL
author_attribution: "{author}"
topic_codes:
  - {topic_code}
image_ref: "{theme_id}"
slide_format: "{sformat}"
status: APPROVED
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# {title}

> {quote_text}

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
        filepath = f"editorial/content/{pid}.md"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        created_count += 1

    print(f"Generated {created_count} markdown files in editorial/content/ (TXT-0301.md to TXT-0500.md).")

    # Update publication manifest
    manifest_path = 'website/publication-manifest.yaml'
    with open(manifest_path, encoding='utf-8') as f:
        manifest = yaml.safe_load(f)

    full_500_ids = [f"TXT-{i:04d}" for i in range(1, 501)]
    manifest['public_content_ids'] = full_500_ids

    with open(manifest_path, 'w', encoding='utf-8') as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False)

    print(f"Updated {manifest_path} with all {len(full_500_ids)} IDs (TXT-0001 to TXT-0500).")

    # Run cache build
    print("Running scripts/build-content-cache.mjs and build-atlas-data.mjs...")
    res = subprocess.run(['node', 'scripts/build-content-cache.mjs'], capture_output=True, text=True)
    print("build-content-cache stdout:", res.stdout)
    if res.returncode != 0:
        print("build-content-cache stderr:", res.stderr)

    res_atlas = subprocess.run(['node', 'scripts/build-atlas-data.mjs'], capture_output=True, text=True)
    print("build-atlas-data stdout:", res_atlas.stdout)
    if res_atlas.returncode != 0:
        print("build-atlas-data stderr:", res_atlas.stderr)

if __name__ == '__main__':
    main()
