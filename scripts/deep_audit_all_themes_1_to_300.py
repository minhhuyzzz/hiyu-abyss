import os
import glob
from PIL import Image
import numpy as np
import json
import re

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
    print("=== DEEP AUDIT OF THEMES 1 TO 300 ===")
    
    catalog_path = "website/src/data/asset-catalog.json"
    catalog_data = {}
    if os.path.exists(catalog_path):
        with open(catalog_path, 'r', encoding='utf-8') as f:
            catalog_data = json.load(f)
            
    print(f"Catalog contains {len(catalog_data)} theme entries.")
    
    web_dir = "website/public/images/themes"
    assets_dir = "assets/templates/multislides"
    
    # We want to find all slides for themes 1 to 300
    all_slides = []
    
    for stt in range(1, 301):
        # find matching folder: theme_{stt}, theme_{stt:02d}, theme_{stt:03d}
        candidates = [f"theme_{stt}", f"theme_{stt:02d}", f"theme_{stt:03d}"]
        
        folder_web = None
        for c in candidates:
            p = os.path.join(web_dir, c)
            if os.path.exists(p) and os.path.isdir(p):
                folder_web = p
                break
                
        folder_assets = None
        for c in candidates:
            p = os.path.join(assets_dir, c)
            if os.path.exists(p) and os.path.isdir(p):
                folder_assets = p
                break
                
        chosen_folder = folder_web or folder_assets
        if not chosen_folder:
            print(f"Theme {stt} NOT found in web or assets!")
            continue
            
        files = sorted(glob.glob(os.path.join(chosen_folder, "*.jpg")))
        slide_files = [f for f in files if "slide" in os.path.basename(f).lower()]
        if not slide_files:
            slide_files = files
            
        for sf in slide_files:
            dh = get_dhash(sf)
            if dh is not None:
                all_slides.append({
                    "stt": stt,
                    "folder": os.path.basename(chosen_folder),
                    "filename": os.path.basename(sf),
                    "path": sf,
                    "dhash": dh
                })
                
    print(f"Total slides found and hashed across themes 1-300: {len(all_slides)}")
    
    dhash_map = {}
    for s in all_slides:
        dh = s["dhash"]
        if dh not in dhash_map:
            dhash_map[dh] = []
        dhash_map[dh].append(s)
        
    exact_dhash_dups = {k: v for k, v in dhash_map.items() if len(v) > 1}
    print(f"\nExact dHash duplicate groups: {len(exact_dhash_dups)}")
    total_exact_dups = sum(len(v) for v in exact_dhash_dups.values())
    print(f"Total slides with exact dHash duplicates: {total_exact_dups}")
    
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
            if hamming_distance(dh_i, dh_j) <= 2:
                union(i, j)
                
    clusters = {}
    for i in range(n):
        root = find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(all_slides[i])
        
    duplicate_clusters = [c for c in clusters.values() if len(c) > 1]
    duplicate_clusters.sort(key=lambda x: len(x), reverse=True)
    
    print(f"\nTotal duplicate clusters (distance <= 2): {len(duplicate_clusters)}")
    total_in_clusters = sum(len(c) for c in duplicate_clusters)
    print(f"Total slides belonging to duplicate clusters: {total_in_clusters}")
    
    report = []
    for idx, c in enumerate(duplicate_clusters):
        report.append({
            "cluster_id": idx + 1,
            "count": len(c),
            "slides": [{"stt": s["stt"], "folder": s["folder"], "filename": s["filename"], "path": s["path"], "dhash": hex(s["dhash"])} for s in c]
        })
        
    with open("scripts/duplicates_1_to_300_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print(f"Saved duplicate report to scripts/duplicates_1_to_300_report.json")
    
    for r in report[:25]:
        print(f"\n[Cluster #{r['cluster_id']} - {r['count']} slides]:")
        for s in r['slides']:
            print(f"   Theme {s['stt']} ({s['folder']}): {s['filename']}")

if __name__ == "__main__":
    main()
