import os
import glob
import hashlib
from PIL import Image
import numpy as np

def get_file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

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
    base_dirs = [
        "assets/templates/multislides",
        "website/public/images/themes"
    ]
    
    print("=== AUDITING THEMES 1 TO 300 FOR DUPLICATES ===")
    
    # We will audit assets/templates/multislides
    scan_dir = "assets/templates/multislides"
    
    slides = []
    for theme_idx in range(1, 301):
        theme_folder = os.path.join(scan_dir, f"theme_{theme_idx}")
        if not os.path.exists(theme_folder):
            continue
        slide_files = sorted(glob.glob(os.path.join(theme_folder, "slide_*.jpg")))
        for sf in slide_files:
            slides.append((theme_idx, sf))
            
    print(f"Total slides found in themes 1-300: {len(slides)}")
    
    # 1. Exact SHA-256 hash duplicates
    hash_to_slides = {}
    for theme_idx, sf in slides:
        fhash = get_file_hash(sf)
        if fhash not in hash_to_slides:
            hash_to_slides[fhash] = []
        hash_to_slides[fhash].append((theme_idx, sf))
        
    exact_dups = {k: v for k, v in hash_to_slides.items() if len(v) > 1}
    print(f"\n--- EXACT SHA-256 DUPLICATES ---")
    print(f"Number of distinct duplicate hash groups: {len(exact_dups)}")
    total_exact_dup_slides = sum(len(v) for v in exact_dups.values())
    print(f"Total slide instances sharing duplicate hashes: {total_exact_dup_slides}")
    
    for h, group in sorted(exact_dups.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"Hash {h[:12]}... (count: {len(group)}):")
        for t_idx, sf in group[:10]:
            print(f"   Theme {t_idx}: {os.path.basename(os.path.dirname(sf))}/{os.path.basename(sf)}")
        if len(group) > 10:
            print(f"   ... and {len(group) - 10} more")

    # 2. Perceptual dHash check (near-duplicates, e.g. re-compressed or identical image resized)
    print("\n--- COMPUTING PERCEPTUAL DHASH ---")
    dhashes = []
    for theme_idx, sf in slides:
        dh = get_dhash(sf)
        if dh is not None:
            dhashes.append((theme_idx, sf, dh))
            
    # Check pairwise or cluster with hamming distance <= 2
    near_dups = {}
    for i in range(len(dhashes)):
        t_i, sf_i, dh_i = dhashes[i]
        for j in range(i + 1, len(dhashes)):
            t_j, sf_j, dh_j = dhashes[j]
            dist = hamming_distance(dh_i, dh_j)
            if dist <= 2:
                # Group them
                key = min(dh_i, dh_j)
                if key not in near_dups:
                    near_dups[key] = set()
                near_dups[key].add((t_i, sf_i))
                near_dups[key].add((t_j, sf_j))
                
    print(f"Number of near-duplicate perceptual clusters (hamming dist <= 2): {len(near_dups)}")
    for k, group in list(near_dups.items())[:15]:
        print(f"Cluster dHash {hex(k)} (count: {len(group)}):")
        for t_idx, sf in sorted(list(group))[:8]:
            print(f"   Theme {t_idx}: {os.path.basename(os.path.dirname(sf))}/{os.path.basename(sf)}")

if __name__ == "__main__":
    main()
