import os
import glob
import json
from PIL import Image
import numpy as np

def get_dhash(img, hash_size=8):
    try:
        small = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = np.asarray(small)
        diff = pixels[:, 1:] > pixels[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except:
        return None

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    with open("scripts/protected_hashes_1_100_and_301_500.json", "r", encoding="utf-8") as f:
        protected_hex_map = json.load(f)
    protected_hashes = set(int(h, 16) for h in protected_hex_map.keys())
    print(f"Loaded {len(protected_hashes)} protected hashes.")
    
    # Check assets/templates/raw_cache/ files
    old_cache_files = glob.glob("assets/templates/raw_cache/*.jpg")
    print(f"Found {len(old_cache_files)} files in raw_cache/")
    
    # Check which ones do NOT collide with protected hashes
    clean_old_files = []
    for cf in old_cache_files:
        if os.path.getsize(cf) < 30000:
            continue
        try:
            with Image.open(cf) as im:
                dh = get_dhash(im)
            if dh is not None:
                # Check collision with distance <= 2
                is_collision = False
                for ph in protected_hashes:
                    if hamming_distance(dh, ph) <= 2:
                        is_collision = True
                        break
                if not is_collision:
                    clean_old_files.append((cf, dh))
        except:
            pass
            
    print(f"Clean non-colliding files in old cache: {len(clean_old_files)}")

if __name__ == "__main__":
    main()
