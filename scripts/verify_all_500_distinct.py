import json
import os
import glob
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

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    print("==================================================")
    print("   HIYU ABYSS - GLOBAL 500 THEMES DISTINCT AUDIT   ")
    print("==================================================")
    
    catalog_path = "website/src/data/asset-catalog.json"
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    print(f"Total catalog themes: {len(catalog)}")
    
    # Collect all slides
    all_slides = []
    
    for key, data in catalog.items():
        stt_str = key.replace("theme_", "")
        try:
            stt = int(stt_str)
        except:
            continue
            
        slides = data.get("slides", {})
        if isinstance(slides, dict):
            slide_items = slides.items()
        elif isinstance(slides, list):
            slide_items = [(f"slide_{idx+1}", p) for idx, p in enumerate(slides)]
        else:
            slide_items = []
            
        for s_id, s_url in slide_items:
            clean_url = s_url.lstrip("/")
            web_path = os.path.join("website", "public", clean_url)
            if not os.path.exists(web_path):
                # try assets
                parts = clean_url.split("/")
                if len(parts) >= 3:
                    web_path = os.path.join("assets", "templates", "multislides", parts[2], parts[3])
                    
            if not os.path.exists(web_path):
                print(f"ERROR: Slide missing on disk! Theme {stt} {s_id}: {s_url}")
                continue
                
            dh = get_dhash(web_path)
            all_slides.append({
                "stt": stt,
                "slide_id": s_id,
                "url": s_url,
                "path": web_path,
                "dhash": dh
            })
            
    print(f"Total active slides resolved across all 500 themes: {len(all_slides)}")
    
    # 1. Exact dHash check
    dhash_map = defaultdict(list)
    for s in all_slides:
        dhash_map[s["dhash"]].append(s)
        
    exact_dups = {k: v for k, v in dhash_map.items() if len(v) > 1}
    print(f"\n--- EXACT DHASH AUDIT ---")
    print(f"Total unique slide image hashes: {len(dhash_map)} / {len(all_slides)}")
    print(f"Duplicate hash groups: {len(exact_dups)}")
    
    if exact_dups:
        print("WARNING: Some exact duplicates detected:")
        for h, group in list(exact_dups.items())[:10]:
            print(f"  Hash {hex(h)} ({len(group)} slides):")
            for s in group:
                print(f"    Theme {s['stt']} {s['slide_id']}: {s['url']}")
    else:
        print("PERFECT: 0 EXACT DUPLICATES ACROSS ALL 500 THEMES!")

    # 2. Perceptual clusters (hamming distance <= 1)
    n = len(all_slides)
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
        dh_i = all_slides[i]["dhash"]
        for j in range(i + 1, n):
            dh_j = all_slides[j]["dhash"]
            if hamming_distance(dh_i, dh_j) <= 1:
                union(i, j)
                
    clusters = defaultdict(list)
    for i in range(n):
        root = find(i)
        clusters[root].append(all_slides[i])
        
    near_dups = [c for c in clusters.values() if len(c) > 1]
    # Filter out intra-theme multi-slide crops (like Theme 1 slide 1, 2, 3 from same painting)
    cross_theme_near_dups = []
    for c in near_dups:
        stts = set(s["stt"] for s in c)
        if len(stts) > 1:
            cross_theme_near_dups.append(c)
            
    print(f"\n--- CROSS-THEME PERCEPTUAL AUDIT (HAMMING DISTANCE <= 1) ---")
    print(f"Cross-theme near-duplicate clusters: {len(cross_theme_near_dups)}")
    if cross_theme_near_dups:
        for c in cross_theme_near_dups[:10]:
            print(f"  Cluster across themes {[s['stt'] for s in c]}:")
            for s in c:
                print(f"    Theme {s['stt']} {s['slide_id']}")
    else:
        print("PERFECT: 0 CROSS-THEME DUPLICATES DETECTED!")
        
    print("\n==================================================")
    print("                  AUDIT COMPLETE                  ")
    print("==================================================")

if __name__ == "__main__":
    main()
