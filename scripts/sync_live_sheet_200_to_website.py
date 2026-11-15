#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Synchronize 200 posts from Live Google Sheet into editorial/content/ and website.
Updates descriptions of posts 1-100 and publishes posts 101-200.
"""

import csv
import os
import re
import yaml

CSV_PATH = "scripts/live_sheet_200.csv"
EDITORIAL_DIR = "editorial/content"
MANIFEST_PATH = "website/publication-manifest.yaml"
INDEX_BOARD_PATH = "indexes/editorial-board.md"

def map_topic_code(topic_str):
    t_up = topic_str.upper()
    if 'HYPOCRISY' in t_up or 'ĐẠO ĐỨC GIẢ' in t_up: return 'HYPOCRISY'
    if 'DOUBLE_STANDARD' in t_up or 'TIÊU CHUẨN KÉP' in t_up: return 'DOUBLE_STANDARD'
    if 'MORALITY' in t_up or 'LÒNG TỐT' in t_up: return 'MORALITY'
    if 'EGO' in t_up or 'BẢN NGÃ' in t_up: return 'EGO'
    if 'SELF_DECEPTION' in t_up or 'TỰ LỪA DỐI' in t_up: return 'SELF_DECEPTION'
    if 'SHADOW' in t_up or 'BÓNG TỐI' in t_up or 'GÓC KHUẤT' in t_up: return 'SHADOW'
    if 'MASK' in t_up or 'MẶT NẠ' in t_up: return 'MASK'
    if 'POWER' in t_up or 'QUYỀN LỰC' in t_up: return 'POWER'
    if 'MANIPULATION' in t_up or 'THAO TÚNG' in t_up: return 'MANIPULATION'
    if 'FREEDOM' in t_up or 'TỰ DO' in t_up: return 'FREEDOM'
    if 'TRUTH' in t_up or 'SỰ THẬT' in t_up: return 'TRUTH'
    if 'LOVE' in t_up or 'TÌNH YÊU' in t_up: return 'LOVE'
    if 'LOYALTY' in t_up or 'TRUNG THÀNH' in t_up: return 'LOYALTY'
    if 'ENVY' in t_up or 'ĐỐ KỴ' in t_up: return 'ENVY'
    if 'CROWD' in t_up or 'ĐÁM ĐÔNG' in t_up or 'BẦY ĐÀN' in t_up: return 'CROWD'
    if 'SUFFERING' in t_up or 'KHỔ ĐAU' in t_up or 'NGHỊCH CẢNH' in t_up: return 'SUFFERING'
    if 'IDENTITY' in t_up or 'BẢN SẮC' in t_up: return 'IDENTITY'
    if 'MEANING' in t_up or 'Ý NGHĨA' in t_up: return 'MEANING'
    if 'SOLITUDE' in t_up or 'CÔ ĐỘC' in t_up: return 'SOLITUDE'
    if 'STATUS' in t_up or 'DANH VỌNG' in t_up or 'KHIÊM NHƯỜNG' in t_up: return 'STATUS'
    if 'RANH GIỚI' in t_up: return 'BOUNDARIES'
    if 'THANH THẢN' in t_up or 'BÌNH YÊN' in t_up: return 'SERENITY'
    if 'KIÊN CƯỜNG' in t_up: return 'RESILIENCE'
    if 'KẾT NỐI' in t_up or 'TÌNH BẠN' in t_up: return 'CONNECTION'
    if 'VƯỢT PHÁN XÉT' in t_up: return 'TRANSCENDENCE'
    if 'HIỆN SINH' in t_up: return 'EXISTENCE'
    if 'NGỤY TÍN' in t_up: return 'BAD_FAITH'
    if 'THIEN KIEN' in t_up or 'THIÊN KIẾN' in t_up: return 'BIAS'
    return 'PSYCHOLOGY'

def sync_editorial_files():
    print("=== ĐỒNG BỘ 200 BÀI TỪ LIVE SHEET VÀO EDITORIAL/CONTENT/ ===")
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    print(f"Tổng số bài trong Sheet: {len(rows)}")
    updated_count = 0
    created_count = 0

    all_ids = []

    for r in rows:
        tid = r['Mã ID'].strip()
        all_ids.append(tid)
        title = r['Tiêu Đề (Dưới 90 từ)'].strip()
        caption = r['Mô Tả (Caption TikTok)'].strip()
        author = r['Nguồn Tác Giả'].strip()
        hashtags = r['Hashtags (5 cái)'].strip()
        slide_fmt = r['Định Dạng Slide'].strip()
        h1 = r['Trang 1 (Hook / Mở màn)'].strip()
        h2 = r['Trang 2 (Cú lật bóc trần)'].strip()
        h3 = r['Trang 3 (Chiếc gương phản tư)'].strip()
        h4 = r.get('Trang 4 (Đúc kết / Phản tư sâu)', '-').strip()
        full_txt = r['Văn Bản Hoàn Chỉnh'].strip()
        topic_raw = r['Chủ Đề Hạt Nhân'].strip()
        phoi = r['Gợi Ý Phôi Ảnh'].strip()
        
        topic_code = map_topic_code(topic_raw)
        fpath = os.path.join(EDITORIAL_DIR, f"{tid}.md")

        existing_fm = {}
        if os.path.exists(fpath):
            try:
                raw_c = open(fpath, 'r', encoding='utf-8').read()
                parts = raw_c.split('---')
                if len(parts) >= 3:
                    existing_fm = yaml.safe_load(parts[1]) or {}
            except Exception:
                pass

        # Build frontmatter preserving academic citation metadata if present
        fm = {
            'id': tid,
            'title': title,
            'content_type': existing_fm.get('content_type', 'INSPIRED_ORIGINAL'),
            'author_attribution': author,
        }

        # Preserve academic citation keys
        for k in ['source_work', 'source_location', 'verification_status', 'translation_note']:
            if k in existing_fm:
                fm[k] = existing_fm[k]

        fm['topic_codes'] = [topic_code]
        fm['image_ref'] = phoi
        fm['slide_format'] = slide_fmt
        fm['status'] = 'APPROVED'
        fm['created_at'] = existing_fm.get('created_at', '2026-11-14')
        fm['updated_at'] = '2026-11-15'

        fm_yaml = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()

        file_body = f"""---
{fm_yaml}
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
        is_new = not os.path.exists(fpath)
        with open(fpath, 'w', encoding='utf-8') as out:
            out.write(file_body)

        if is_new:
            created_count += 1
        else:
            updated_count += 1

    print(f"✅ Hoàn tất đồng bộ: Đã cập nhật {updated_count} bài, Tạo mới {created_count} bài.")
    return all_ids

def update_manifest(all_ids):
    print(f"\n[*] Đang cập nhật {MANIFEST_PATH} với {len(all_ids)} tác phẩm...")
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = yaml.safe_load(f) or {}

    manifest['public_content_ids'] = all_ids
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(manifest, f, sort_keys=False, allow_unicode=True)
    print("✅ Đã cập nhật publication-manifest.yaml thành công!")

def update_indexes():
    print(f"\n[*] Đang cập nhật bảng chỉ mục: {INDEX_BOARD_PATH}...")
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    lines = [
        "# BẢNG CHỈ MỤC BIÊN TẬP (EDITORIAL BOARD INDEX)",
        "",
        "> Cập nhật tự động từ Google Sheet Pipeline: 200 tác phẩm.",
        "",
        "| STT | Mã ID | Tác giả | Chủ đề | Định dạng | Trạng thái |",
        "|---|---|---|---|---|---|",
    ]

    for r in rows:
        stt = r['STT']
        tid = r['Mã ID']
        author = r['Nguồn Tác Giả']
        topic = map_topic_code(r['Chủ Đề Hạt Nhân'])
        fmt = r['Định Dạng Slide']
        lines.append(f"| {stt} | `{tid}` | {author} | `#{topic}` | {fmt} | `APPROVED` |")

    with open(INDEX_BOARD_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    print("✅ Đã cập nhật editorial-board.md thành công!")

if __name__ == '__main__':
    ids = sync_editorial_files()
    update_manifest(ids)
    update_indexes()
