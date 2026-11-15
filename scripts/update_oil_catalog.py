#!/usr/bin/env python3
# scripts/update_oil_catalog.py - Cập nhật thông tin các bộ tranh sơn dầu mới vào asset-catalog.json
import json
import os

CATALOG_PATH = "website/src/data/asset-catalog.json"
MANIFEST_PATH = "scripts/oil_suites_prompts_manifest.json"
POSTS_PATH = "scripts/posts_91_120_data.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    prompts = json.load(f)

with open(POSTS_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

for p in posts:
    mid = p["id"]
    stt = int(p["stt"])
    theme_key = f"theme_{stt:02d}"
    slides_def = prompts.get(mid, [])
    
    slides_dict = {}
    for s in slides_def:
        s_num = s["slide"]
        slides_dict[f"slide_{s_num}"] = f"/images/themes/{theme_key}/slide_{s_num}.jpg"
        
    catalog[theme_key] = {
        "art_id": f"ART-{stt:04d}",
        "title": f"Tác phẩm sơn dầu: {p['title'][:60]}",
        "artist": f"Hiyu Abyss Atelier (Cảm hứng {p['author']})",
        "year": "2026",
        "museum": "Bộ sưu tập Sơn dầu Hiyu Abyss",
        "license": "Hiyu Abyss Original Oil Art",
        "alt_vi": f"Tranh sơn dầu phong cách cổ điển cho chủ đề {p['theme']}.",
        "slides": slides_dict
    }

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Updated {CATALOG_PATH} with {len(posts)} new themes ({len(catalog)} total themes in catalog)!")
