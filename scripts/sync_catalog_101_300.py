import json
import os
import glob

with open("scripts/oil_suites_101_300_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

catalog_path = "website/src/data/asset-catalog.json"
with open(catalog_path, "r", encoding="utf-8") as f:
    catalog = json.load(f)

updated_count = 0
for theme in manifest.values():
    stt = theme["stt"]
    theme_key = f"theme_{stt}"
    
    slide_map = {}
    artists = []
    titles = []
    
    for s in theme["slides"]:
        s_idx = s["slide_index"]
        slide_map[f"slide_{s_idx}"] = f"/images/themes/{theme_key}/slide_{s_idx}.jpg"
        artists.append(s["artist"])
        titles.append(s["artwork_title"])
        
    catalog[theme_key] = {
        "art_id": f"ART-{stt:04d}",
        "title": f"Bộ kiệt tác sơn dầu độc bản: {', '.join(titles[:2])}",
        "artist": f"{', '.join(dict.fromkeys(artists))} & các danh họa bảo tàng",
        "year": "Thế kỷ XVI - XIX / Phục dựng Hiyu Abyss 2026",
        "museum": "Bộ sưu tập Kiệt tác Hội họa Hiyu Abyss & Public Domain Museum Scans",
        "license": "Public Domain / HYA-08 Canvas Normalized",
        "alt_vi": f"Bộ tác phẩm sơn dầu cổ điển bảo tàng độc bản cho chủ đề {theme.get('topic', '')}: {theme.get('title', '')}",
        "slides": slide_map
    }
    updated_count += 1

with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

print(f"Successfully synchronized {updated_count} themes in {catalog_path}.")
print(f"Total themes in catalog: {len(catalog)}")
