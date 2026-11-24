import os
import glob
import json
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

def main():
    protected_hashes = {} # dhash -> (theme, filename)
    
    # 1. Themes 1-100
    for stt in range(1, 101):
        for prefix in [f"theme_{stt:02d}", f"theme_{stt}"]:
            folder = os.path.join("website/public/images/themes", prefix)
            if os.path.exists(folder):
                for sf in glob.glob(os.path.join(folder, "*.jpg")):
                    dh = get_dhash(sf)
                    if dh is not None:
                        protected_hashes[dh] = (stt, os.path.basename(sf))
                        
    print(f"Protected hashes from Themes 1-100: {len(protected_hashes)}")
    
    # 2. Themes 301-500
    count_301_500 = 0
    for stt in range(301, 501):
        folder = os.path.join("website/public/images/themes", f"theme_{stt}")
        if os.path.exists(folder):
            for sf in glob.glob(os.path.join(folder, "*.jpg")):
                dh = get_dhash(sf)
                if dh is not None:
                    protected_hashes[dh] = (stt, os.path.basename(sf))
                    count_301_500 += 1
                    
    print(f"Total protected hashes (Themes 1-100 + Themes 301-500): {len(protected_hashes)}")
    
    with open("scripts/protected_hashes_1_100_and_301_500.json", "w", encoding="utf-8") as f:
        json.dump({hex(k): v for k, v in protected_hashes.items()}, f, indent=2)

if __name__ == "__main__":
    main()
