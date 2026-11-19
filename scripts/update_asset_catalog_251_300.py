#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Expand Asset Catalog for Themes 251 - 300
Cập nhật website/src/data/asset-catalog.json với đầy đủ 50 theme mới và đường dẫn 103 slides.
"""

import json
import os

CATALOG_PATH = "website/src/data/asset-catalog.json"
MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"

def main():
    print("=== CẬP NHẬT ASSET CATALOG CHO THEMES 251 - 300 ===")
    
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    for tid, t in manifest.items():
        stt = t["stt"]
        theme_id = t["theme_id"]
        art_id = f"ART-{stt:04d}"
        topic = t["topic"]
        slide_fmt = t["slide_format"]
        slides = t["slides"]
        
        artworks_str = ", ".join([f"{s['artist']} - {s['artwork_title']}" for s in slides])
        primary_artist = slides[0]["artist"]
        
        slides_dict = {}
        for s in slides:
            s_idx = s["slide_index"]
            slides_dict[f"slide_{s_idx}"] = f"/images/themes/{theme_id}/slide_{s_idx}.jpg"

        catalog[theme_id] = {
            "art_id": art_id,
            "title": f"Bộ kiệt tác sơn dầu độc bản: {artworks_str}",
            "artist": f"{primary_artist} & các bậc thầy Ấn tượng/Lãng mạn",
            "year": "Thế kỷ XIX / Phục dựng Hiyu Abyss 2026",
            "museum": "Bộ sưu tập Kiệt tác Hội họa Hiyu Abyss & Wikimedia Public Domain",
            "license": "Public Domain / HYA-08 Canvas Normalized",
            "alt_vi": f"Bộ tác phẩm sơn dầu cổ điển bảo tàng độc bản cho {slide_fmt} ({topic}): {artworks_str}.",
            "slides": slides_dict
        }

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã cập nhật {len(manifest)} theme mới vào {CATALOG_PATH}.")
    print(f"Tổng số themes trong catalog hiện tại: {len(catalog)}")

if __name__ == '__main__':
    main()
