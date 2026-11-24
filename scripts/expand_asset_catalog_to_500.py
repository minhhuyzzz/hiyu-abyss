import json
import os

CATALOG_PATH = "website/src/data/asset-catalog.json"
MANIFEST_PATH = "scripts/oil_suites_301_500_manifest.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

print(f"Catalog before expansion: {len(catalog)} themes.")

for tid, t in manifest.items():
    stt = t["stt"]
    if not (301 <= stt <= 500):
        continue
        
    theme_key = f"theme_{stt}"
    slides = t["slides"]
    
    # Build artist summary and title
    slide_summary = []
    primary_artists = []
    slides_dict = {}
    
    for s in slides:
        s_idx = s["slide_index"]
        artist = s["artist"]
        art_title = s.get("artwork_title", f"Kiệt tác phái {artist}")
        slide_summary.append(f"{artist} - {art_title}")
        if artist not in primary_artists:
            primary_artists.append(artist)
        slides_dict[f"slide_{s_idx}"] = f"/images/themes/theme_{stt}/slide_{s_idx}.jpg"
        
    primary_str = ", ".join(primary_artists[:2])
    if len(primary_artists) > 2:
        primary_str += " & các danh họa cổ điển"
        
    catalog[theme_key] = {
        "art_id": f"ART-{stt:04d}",
        "title": f"Bộ kiệt tác sơn dầu độc bản: {', '.join(slide_summary[:3])}",
        "artist": primary_str,
        "year": "Thế kỷ XVII - XIX / Phục dựng Hiyu Abyss 2026",
        "museum": "Bộ sưu tập Kiệt tác Hội họa Hiyu Abyss & Public Domain Museum Scans",
        "license": "Public Domain / HYA-08 Canvas Normalized",
        "alt_vi": f"Bộ tác phẩm sơn dầu cổ điển bảo tàng độc bản cho {t.get('format')} ({t.get('topic')}): {t.get('title')}.",
        "slides": slides_dict
    }

print(f"Catalog after expansion: {len(catalog)} themes.")

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("✅ Đã cập nhật thành công website/src/data/asset-catalog.json lên 500 themes!")
