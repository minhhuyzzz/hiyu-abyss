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

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)
        
    print(f"Catalog has {len(catalog)} themes.")
    
    # 1. Collect all slides for 301-500
    slides_301_500 = []
    for key, data in catalog.items():
        stt_str = key.replace('theme_', '')
        try:
            stt = int(stt_str)
        except:
            continue
        if 301 <= stt <= 500:
            for s_id, s_path in data.get('slides', {}).items():
                p = os.path.join('website', 'public', s_path.lstrip('/'))
                dh = get_dhash(p)
                slides_301_500.append({
                    "stt": stt,
                    "slide_id": s_id,
                    "url": s_path,
                    "path": p,
                    "dhash": dh
                })
                
    print(f"Total slides in 301-500: {len(slides_301_500)}")
    
    # 2. Collect all slides for 1-300
    slides_1_300 = []
    for key, data in catalog.items():
        stt_str = key.replace('theme_', '')
        try:
            stt = int(stt_str)
        except:
            continue
        if 1 <= stt <= 300:
            for s_id, s_path in data.get('slides', {}).items():
                p = os.path.join('website', 'public', s_path.lstrip('/'))
                if not os.path.exists(p):
                    # fallback
                    parts = s_path.lstrip('/').split('/')
                    if len(parts) >= 3:
                        p = os.path.join('assets', 'templates', 'multislides', parts[2], parts[3])
                dh = get_dhash(p)
                slides_1_300.append({
                    "stt": stt,
                    "slide_id": s_id,
                    "url": s_path,
                    "path": p,
                    "dhash": dh
                })
                
    print(f"Total slides in 1-300: {len(slides_1_300)}")
    
    # 3. Analyze duplicates in 1-300
    # Group by similarity:
    # First, let's see which slides in 1-300 collide with 301-500
    # and which slides in 1-300 collide with other slides in 1-300!
    
    # Let's count occurrences
    # We can cluster all slides across 1-500
    all_slides = slides_1_300 + slides_301_500
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
        if dh_i is None:
            continue
        for j in range(i + 1, n):
            dh_j = all_slides[j]["dhash"]
            if dh_j is None:
                continue
            if hamming_distance(dh_i, dh_j) <= 2:
                union(i, j)
                
    clusters = defaultdict(list)
    for i in range(n):
        root = find(i)
        clusters[root].append(all_slides[i])
        
    dup_clusters = [c for c in clusters.values() if len(c) > 1]
    print(f"\nTotal clusters with duplicates across 1-500: {len(dup_clusters)}")
    
    # Categorize clusters:
    # Type A: Duplicates only within 1-300
    # Type B: Duplicates between 1-300 and 301-500
    # Type C: Duplicates within 301-500 (should be 0, we already verified)
    type_a = []
    type_b = []
    type_c = []
    
    for c in dup_clusters:
        has_1_300 = any(1 <= s["stt"] <= 300 for s in c)
        has_301_500 = any(301 <= s["stt"] <= 500 for s in c)
        if has_1_300 and not has_301_500:
            type_a.append(c)
        elif has_1_300 and has_301_500:
            type_b.append(c)
        elif not has_1_300 and has_301_500:
            type_c.append(c)
            
    print(f"Type A (Duplicates purely within 1-300): {len(type_a)} clusters")
    print(f"Type B (Collision between 1-300 and 301-500): {len(type_b)} clusters")
    print(f"Type C (Duplicates within 301-500): {len(type_c)} clusters")
    
    # Let's count how many slides in 1-300 need to be replaced
    # In each cluster:
    # If it's Type A (e.g. Theme 19, 111, 151, 160 all have the same image):
    #   We can keep ONE (e.g. the lowest STT, Theme 19), and replace all others (Theme 111, 151, 160)!
    # If it's Type B (e.g. Theme 6 and Theme 386):
    #   Theme 386 in 301-500 has it. If we replace Theme 6 or Theme 386?
    #   User said: "dò lại các ảnh nào tự trùng của 300 trước thì phải đổi thành các khác"
    #   User specifically wants to fix the duplicates in the previous 300!
    #   Let's check if keeping 301-500 untouched and replacing the colliding ones in 1-300 makes 1-300 completely unique!
    
    slides_to_replace_in_1_300 = []
    
    # In Type A: keep the first one in 1-300, replace the subsequent ones
    for c in type_a:
        # sort by STT
        sorted_c = sorted(c, key=lambda x: (x["stt"], x["slide_id"]))
        # Keep sorted_c[0]
        # Replace sorted_c[1:]
        for s in sorted_c[1:]:
            slides_to_replace_in_1_300.append(s)
            
    # In Type B: all slides from 1-300 in Type B collide with 301-500 (or with each other too)!
    # If 301-500 keeps its image, then ALL slides in 1-300 that collide with 301-500 need new images!
    # Or what if in 1-300, Theme 6 originally owned it?
    # Wait, let's see why 301-500 collided with 1-300!
    for c in type_b:
        # slides in 1-300
        in_1_300 = [s for s in c if 1 <= s["stt"] <= 300]
        for s in in_1_300:
            slides_to_replace_in_1_300.append(s)
            
    print(f"\nTotal slides in 1-300 that need replacement: {len(slides_to_replace_in_1_300)}")
    
    # Themes affected in 1-300:
    themes_affected = sorted(list(set(s["stt"] for s in slides_to_replace_in_1_300)))
    print(f"Themes in 1-300 affected: {len(themes_affected)} / 300")
    print(f"Sample affected themes: {themes_affected[:30]}")
    
    # Save list to file
    with open('scripts/slides_to_replace_in_1_to_300.json', 'w', encoding='utf-8') as f:
        json.dump([
            {
                "stt": s["stt"],
                "slide_id": s["slide_id"],
                "url": s["url"],
                "path": s["path"]
            } for s in slides_to_replace_in_1_300
        ], f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
