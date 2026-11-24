import json
import os
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

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)
        
    print(f"Catalog has {len(catalog)} themes.")
    
    # We want to check all catalog items for themes 1-300
    catalog_slides = [] # (theme_key, stt, slide_id, rel_path, abs_path, dhash)
    
    for key, data in catalog.items():
        # extract stt
        stt_str = key.replace('theme_', '')
        try:
            stt = int(stt_str)
        except:
            continue
            
        slides = data.get('slides', {})
        if isinstance(slides, dict):
            slide_items = slides.items()
        elif isinstance(slides, list):
            slide_items = [(f"slide_{idx+1}", s) for idx, s in enumerate(slides)]
        else:
            slide_items = []
            
        for s_id, s_path in slide_items:
            # relative path starts with /images/themes/...
            # maps to website/public/images/themes/...
            clean_path = s_path.lstrip('/')
            abs_path = os.path.join('website', 'public', clean_path)
            if not os.path.exists(abs_path):
                # try assets/templates/multislides/...
                # e.g. clean_path = images/themes/theme_01/slide_1.jpg -> assets/templates/multislides/theme_01/slide_1.jpg
                parts = clean_path.split('/')
                if len(parts) >= 3:
                    theme_f = parts[2]
                    file_f = parts[3] if len(parts) > 3 else ""
                    alt_path = os.path.join('assets', 'templates', 'multislides', theme_f, file_f)
                    if os.path.exists(alt_path):
                        abs_path = alt_path
                        
            if not os.path.exists(abs_path):
                print(f"MISSING FILE: {s_path} -> {abs_path}")
                continue
                
            dh = get_dhash(abs_path)
            catalog_slides.append({
                "theme_key": key,
                "stt": stt,
                "slide_id": s_id,
                "url": s_path,
                "abs_path": abs_path,
                "dhash": dh
            })
            
    print(f"Total catalog slides resolved: {len(catalog_slides)}")
    
    # Filter for themes 1 to 300
    slides_1_300 = [s for s in catalog_slides if 1 <= s["stt"] <= 300]
    print(f"Total catalog slides in themes 1-300: {len(slides_1_300)}")
    
    # Also check against 301-500 slides to ensure no cross-contamination!
    slides_301_500 = [s for s in catalog_slides if 301 <= s["stt"] <= 500]
    hashes_301_500 = set(s["dhash"] for s in slides_301_500)
    
    # Cluster slides_1_300 by hamming distance <= 2
    n = len(slides_1_300)
    parent = list(range(n))
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for i in range(n):
        dh_i = slides_1_300[i]["dhash"]
        for j in range(i + 1, n):
            dh_j = slides_1_300[j]["dhash"]
            if hamming_distance(dh_i, dh_j) <= 2:
                union(i, j)
                
    clusters = {}
    for i in range(n):
        root = find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(slides_1_300[i])
        
    dup_clusters = [c for c in clusters.values() if len(c) > 1]
    # Filter for clusters that have different themes or different slides
    print(f"\nTotal duplicate clusters in themes 1-300 (catalog): {len(dup_clusters)}")
    
    cross_theme_clusters = []
    intra_theme_clusters = []
    for c in dup_clusters:
        stts = set(s["stt"] for s in c)
        if len(stts) > 1:
            cross_theme_clusters.append(c)
        else:
            intra_theme_clusters.append(c)
            
    print(f"Cross-theme duplicate clusters in 1-300: {len(cross_theme_clusters)}")
    print(f"Intra-theme duplicate clusters in 1-300 (same theme slides reusing image): {len(intra_theme_clusters)}")
    
    # Check if any slide in 1-300 collides with 301-500
    collision_with_301_500 = []
    for s in slides_1_300:
        for s2 in slides_301_500:
            if hamming_distance(s["dhash"], s2["dhash"]) <= 2:
                collision_with_301_500.append((s, s2))
                break
                
    print(f"Slides in 1-300 that collide with themes 301-500: {len(collision_with_301_500)}")
    
    # Save detailed duplicates for themes 1-300
    out_data = {
        "cross_theme_clusters": [
            {
                "count": len(c),
                "themes": sorted(list(set(s["stt"] for s in c))),
                "slides": [{"theme_key": s["theme_key"], "stt": s["stt"], "slide_id": s["slide_id"], "abs_path": s["abs_path"], "url": s["url"], "dhash": hex(s["dhash"])} for s in c]
            } for c in cross_theme_clusters
        ],
        "intra_theme_clusters": [
            {
                "count": len(c),
                "theme": c[0]["stt"],
                "slides": [{"slide_id": s["slide_id"], "url": s["url"]} for s in c]
            } for c in intra_theme_clusters
        ],
        "collision_with_301_500": [
            {
                "slide_1_300": {"theme": s1["stt"], "slide": s1["slide_id"], "url": s1["url"]},
                "slide_301_500": {"theme": s2["stt"], "slide": s2["slide_id"], "url": s2["url"]}
            } for s1, s2 in collision_with_301_500
        ]
    }
    
    with open('scripts/catalog_duplicates_1_to_300.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, indent=2, ensure_ascii=False)
        
    print("Report written to scripts/catalog_duplicates_1_to_300.json")

if __name__ == "__main__":
    main()
