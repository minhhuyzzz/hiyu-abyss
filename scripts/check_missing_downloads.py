import json
import os

with open("scripts/oil_suites_101_300_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

raw_cache = "assets/templates/raw_cache_101_300"
missing = []

for theme in manifest.values():
    stt = theme["stt"]
    for s in theme["slides"]:
        raw_fn = s["raw_filename"]
        p = os.path.join(raw_cache, raw_fn)
        if not os.path.exists(p) or os.path.getsize(p) < 30000:
            missing.append({
                "stt": stt,
                "slide_index": s["slide_index"],
                "raw_filename": raw_fn,
                "query": s["search_query"],
                "artist": s["artist"],
                "title": s["artwork_title"]
            })

print(f"Total missing: {len(missing)} / 477")
print("First 10 missing:")
for m in missing[:10]:
    print(f"  Theme {m['stt']} slide {m['slide_index']}: {m['artist']} - {m['title']} | Query: {m['query']}")

with open("scripts/missing_downloads_101_300.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, indent=2, ensure_ascii=False)
