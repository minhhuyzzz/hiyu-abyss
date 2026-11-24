import json
import os
from collections import defaultdict
from PIL import Image
import numpy as np

def get_dhash(image_path, hash_size=8):
    try:
        with Image.open(image_path) as img:
            img = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
            pixels = np.asarray(img)
            diff = pixels[:, 1:] > pixels[:, :-1]
            return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except Exception as e:
        return None

with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

slides = []
for key, data in catalog.items():
    stt = int(key.replace("theme_", ""))
    for s_id, s_url in data.get("slides", {}).items():
        p = os.path.join("website", "public", s_url.lstrip("/"))
        if os.path.exists(p):
            dh = get_dhash(p)
            slides.append({"stt": stt, "slide_id": s_id, "url": s_url, "path": p, "dhash": dh})

dhash_map = defaultdict(list)
for s in slides:
    dhash_map[s["dhash"]].append(s)

exact_dups = {k: v for k, v in dhash_map.items() if len(v) > 1}

print(f"Total duplicate groups: {len(exact_dups)}")

duplicates_list = []
for h, group in sorted(exact_dups.items(), key=lambda x: len(x[1]), reverse=True):
    themes = [s["stt"] for s in group]
    duplicates_list.append({
        "dhash": hex(h),
        "count": len(group),
        "themes": themes,
        "slides": group
    })
    print(f"Hash {hex(h)}: Themes {themes}")

with open("scripts/exact_72_duplicates.json", "w", encoding="utf-8") as f:
    json.dump(duplicates_list, f, indent=2, ensure_ascii=False)
