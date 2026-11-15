#!/usr/bin/env python3
# scripts/update_oil_catalog_121_150.py - Cập nhật 30 theme mới (121-150) vào asset-catalog.json
import json
import os
import re

CATALOG_PATH = "website/src/data/asset-catalog.json"
MANIFEST_PATH = "scripts/oil_suites_121_150_prompts_manifest.json"
POSTS_PATH = "scripts/posts_121_150_data.json"
RESOLVED_PATH = "scripts/resolved_47_distinct_oil_art.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    prompts = json.load(f)

with open(POSTS_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

with open(RESOLVED_PATH, "r", encoding="utf-8") as f:
    resolved = json.load(f)

def clean_art_name(raw_title: str) -> tuple[str, str]:
    """Tách tên tác giả và tên tác phẩm từ File:Artist - Title.jpg"""
    title = raw_title.replace("File:", "").rsplit(".", 1)[0]
    title = re.sub(r" - Google Art Project", "", title)
    title = re.sub(r",?\s*(ca\.|c\.)\s*\d{4}.*", "", title)
    title = re.sub(r"_\(cleaned\)", "", title)
    title = re.sub(r"MET DT\d+", "", title)
    
    if " - " in title:
        parts = title.split(" - ", 1)
        artist = parts[0].strip()
        work = parts[1].strip()
        return artist, work
    elif " av " in title:
        parts = title.split(" av ", 1)
        return parts[1].strip(), parts[0].strip()
    elif " par " in title:
        parts = title.split(" par ", 1)
        return parts[1].strip(), parts[0].strip()
    elif " by " in title:
        parts = title.split(" by ", 1)
        return parts[1].strip(), parts[0].strip()
    return "Danh họa Cổ điển Châu Âu", title.strip()

for p in posts:
    mid = p["id"]
    stt = int(p["stt"])
    theme_key = f"theme_{stt:02d}"
    slides_def = prompts.get(mid, [])
    
    slides_dict = {}
    slide_artists = []
    slide_works = []
    
    for s in slides_def:
        s_num = s["slide"]
        slide_key = f"{theme_key}_slide_{s_num}"
        slides_dict[f"slide_{s_num}"] = f"/images/themes/{theme_key}/slide_{s_num}.jpg"
        
        if slide_key in resolved:
            artist, work = clean_art_name(resolved[slide_key]["title"])
            slide_artists.append(artist)
            slide_works.append(work)
        else:
            slide_artists.append(f"Hiyu Abyss Atelier (Cảm hứng {p['author']})")
            slide_works.append(p["title"])

    if slide_artists:
        unique_artists = list(dict.fromkeys(slide_artists))
        artist_display = " / ".join(unique_artists)
    else:
        artist_display = f"Hiyu Abyss Atelier (Cảm hứng {p['author']})"
        
    if slide_works:
        work_display = " / ".join(slide_works)
    else:
        work_display = p["title"]

    catalog[theme_key] = {
        "art_id": f"ART-{stt:04d}",
        "title": f"Bộ tranh sơn dầu: {work_display[:80]}",
        "artist": artist_display,
        "year": "Thế kỷ XVII - XIX / Phục dựng 2026",
        "museum": "Bộ sưu tập Kiệt tác Sơn dầu Hiyu Abyss & Wikimedia Public Domain",
        "license": "Public Domain / Hiyu Abyss Canvas Normalized",
        "alt_vi": f"Tranh sơn dầu phong cách cổ điển, vân cọ impasto và toan vải hữu cơ cho chủ đề {p['theme']}.",
        "slides": slides_dict
    }

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Updated {CATALOG_PATH} with {len(posts)} new themes ({len(catalog)} total themes in catalog)!")
