import json
import os
import glob

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

themes_info = []
for stt in range(101, 301):
    key = f"theme_{stt}"
    cat_entry = catalog.get(key, {})
    slides = cat_entry.get("slides", {})
    if isinstance(slides, dict):
        slide_count = len(slides)
        slide_keys = list(slides.keys())
    elif isinstance(slides, list):
        slide_count = len(slides)
        slide_keys = [f"slide_{i+1}" for i in range(len(slides))]
    else:
        slide_count = 0
        slide_keys = []
        
    # Read editorial content
    txt_path = f"editorial/content/TXT-{stt:04d}.md"
    title_line = ""
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("# ") or line.startswith("title:"):
                    title_line = line.strip()
                    break
                    
    themes_info.append({
        "stt": stt,
        "slide_count": slide_count,
        "slide_keys": slide_keys,
        "catalog_title": cat_entry.get("title", ""),
        "txt_title": title_line
    })

print(f"Themes 101-300 count: {len(themes_info)}")
total_slides_101_300 = sum(t["slide_count"] for t in themes_info)
print(f"Total slides across themes 101-300: {total_slides_101_300}")

# Check breakdown of slide counts (how many 1-slide, 2-slide, 3-slide, 4-slide)
from collections import Counter
counts = Counter(t["slide_count"] for t in themes_info)
print(f"Slide count breakdown: {dict(counts)}")
