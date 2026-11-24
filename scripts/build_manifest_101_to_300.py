import json
import os

def main():
    with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)
        
    print(f"Catalog has {len(catalog)} themes.")
    
    # We will build a manifest for themes 101 to 300
    # First, let's load protected hashes and filenames so we never reuse anything already in 1-100 or 301-500
    used_queries = set()
    used_filenames = set()
    
    # Let's see what is already used in 301-500 manifest
    if os.path.exists("scripts/oil_suites_301_500_manifest.json"):
        with open("scripts/oil_suites_301_500_manifest.json", "r", encoding="utf-8") as f:
            m301_500 = json.load(f)
        for theme in m301_500.values():
            for s in theme.get("slides", []):
                q = s.get("search_query")
                if q:
                    used_queries.add(q.lower())
                raw_f = s.get("raw_file")
                if raw_f:
                    used_filenames.add(raw_f.lower())
                    
    print(f"Loaded {len(used_queries)} queries from 301-500 manifest to avoid collisions.")
    
    # Read each TXT file for 101-300
    themes_manifest = []
    
    # Let's prepare a rich pool of curated classical masterpieces categorized by theme
    # We will write a helper script to populate 477 unique masterworks
    
    slide_total = 0
    for stt in range(101, 301):
        key = f"theme_{stt}"
        cat_data = catalog.get(key, {})
        slides_dict = cat_data.get("slides", {})
        if isinstance(slides_dict, dict):
            slide_ids = list(slides_dict.keys())
        elif isinstance(slides_dict, list):
            slide_ids = [f"slide_{i+1}" for i in range(len(slides_dict))]
        else:
            slide_ids = ["slide_1", "slide_2", "slide_3"]
            
        txt_path = f"editorial/content/TXT-{stt:04d}.md"
        title = ""
        author = ""
        topic = ""
        if os.path.exists(txt_path):
            with open(txt_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("title:"):
                        title = line.replace("title:", "").strip().strip("'\"")
                    elif line.startswith("author_attribution:"):
                        author = line.replace("author_attribution:", "").strip().strip("'\"")
                    elif line.startswith("topic_codes:"):
                        pass
                    elif line.strip().startswith("- ") and not topic:
                        topic = line.strip().replace("- ", "")
                        
        themes_manifest.append({
            "stt": stt,
            "theme_key": key,
            "title": title or cat_data.get("title", f"Theme {stt}"),
            "author": author or "Triết gia / Danh họa",
            "topic": topic or "PSYCHOLOGY",
            "slide_count": len(slide_ids),
            "slide_ids": slide_ids
        })
        slide_total += len(slide_ids)
        
    print(f"Themes parsed: {len(themes_manifest)}, Total slides required: {slide_total}")
    
    with open("scripts/themes_101_300_structure.json", "w", encoding="utf-8") as f:
        json.dump(themes_manifest, f, indent=2, ensure_ascii=False)
        
    print("Saved themes_101_300_structure.json")

if __name__ == "__main__":
    main()
