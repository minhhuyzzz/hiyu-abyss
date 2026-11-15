#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/update_oil_catalog_151_200_distinct.py
Cập nhật website/src/data/asset-catalog.json cho 50 bộ kiệt tác Theme 151 - 200
với danh sách các tác phẩm độc bản thực sự cho từng slide, loại bỏ các slide crop giả.
"""

import json
import os

CATALOG_PATH = "website/src/data/asset-catalog.json"
RESOLVED_PATH = "scripts/resolved_98_distinct_oil_art.json"
SLIDES_DETAIL_PATH = "scripts/posts_151_200_slides_detail.json"

def main():
    if not os.path.exists(RESOLVED_PATH):
        print(f"Error: {RESOLVED_PATH} not found!")
        return

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    with open(RESOLVED_PATH, "r", encoding="utf-8") as f:
        resolved = json.load(f)

    with open(SLIDES_DETAIL_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)

    updated_count = 0

    for post in posts:
        stt = post['stt']
        theme_id = post['theme_id']
        art_id = f"ART-{stt:04d}"
        topic = post['topic']
        fmt = post['format']
        slides_info = post['slides']

        slides_dict = {}
        artworks_list = []

        for s in slides_info:
            s_idx = s['index']
            key = f"{theme_id}_slide_{s_idx}"
            s_data = resolved.get(key, {})
            art_name = s_data.get('artwork_name', 'Masterpiece')
            artworks_list.append(art_name)
            slides_dict[f"slide_{s_idx}"] = f"/images/themes/{theme_id}/slide_{s_idx}.jpg"

        primary_art = artworks_list[0] if artworks_list else "Classical Oil Painting"
        primary_artist = primary_art.split(' - ')[0] if ' - ' in primary_art else "Master Artist"

        catalog[theme_id] = {
            "art_id": art_id,
            "title": f"Bộ kiệt tác sơn dầu độc bản: {', '.join(artworks_list)}",
            "artist": primary_artist if len(artworks_list) == 1 else f"{primary_artist} & các bậc thầy cổ điển",
            "year": "Thế kỷ XV - XIX / Phục dựng Hiyu Abyss 2026",
            "museum": "Bộ sưu tập Kiệt tác Hội họa Hiyu Abyss & Wikimedia Public Domain",
            "license": "Public Domain / HYA-08 Canvas Normalized",
            "alt_vi": f"Bộ tác phẩm sơn dầu cổ điển bảo tàng độc bản cho {fmt} ({topic}): {', '.join(artworks_list)}.",
            "slides": slides_dict
        }
        updated_count += 1

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"🎉 Updated {updated_count} themes in {CATALOG_PATH} with distinct artworks.")

if __name__ == '__main__':
    main()
