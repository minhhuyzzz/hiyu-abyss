import os
import json
import glob
from PIL import Image
import numpy as np

def get_dhash(image_path, hash_size=8):
    try:
        with Image.open(image_path) as img:
            img = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
            pixels = np.asarray(img)
            diff = pixels[:, 1:] > pixels[:, :-1]
            return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except Exception:
        return None

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    slides = []
    # Sort slides deterministically by stt, then slide_idx
    all_paths = glob.glob("assets/templates/multislides/theme_*/slide_*.jpg")
    
    def sort_key(p):
        parts = p.replace("\\", "/").split("/")
        theme_str = parts[-2]
        slide_str = parts[-1]
        stt = int(theme_str.replace("theme_", ""))
        # extract slide number
        s_num = int("".join([c for c in slide_str if c.isdigit()]))
        return (stt, s_num)

    all_paths.sort(key=sort_key)
    
    print(f"Total slides found: {len(all_paths)}")
    for p in all_paths:
        parts = p.replace("\\", "/").split("/")
        theme_str = parts[-2]
        slide_str = parts[-1]
        stt = int(theme_str.replace("theme_", ""))
        s_num = int("".join([c for c in slide_str if c.isdigit()]))
        h = get_dhash(p)
        slides.append({
            "stt": stt,
            "slide_idx": s_num,
            "slide_name": f"slide_{s_num}",
            "filename": slide_str,
            "path": p,
            "hash": h
        })

    # Group into equivalence classes
    # We will iterate through slides: the first occurrence of an artwork is kept (canonical).
    # Any later slide that is visually equivalent to an already accepted slide is marked DUPLICATE.
    canonical_slides = []
    duplicate_slides = []

    # Pre-resize all images to 64x64 for fast pixel diff comparison
    print("Pre-loading low-res thumbnails for fast comparison...")
    thumbnails = []
    for s in slides:
        try:
            im = Image.open(s["path"]).convert('RGB').resize((64, 64))
            arr = np.array(im, dtype=np.float32)
            thumbnails.append(arr)
        except Exception:
            thumbnails.append(None)

    for i in range(len(slides)):
        s_cur = slides[i]
        arr_cur = thumbnails[i]
        is_dup = False
        dup_of = None
        
        for c_idx in canonical_slides:
            s_can = slides[c_idx]
            arr_can = thumbnails[c_idx]
            
            # Check hash distance first
            dist = hamming_distance(s_cur["hash"], s_can["hash"])
            if dist <= 2:
                # Check mean pixel diff
                if arr_cur is not None and arr_can is not None:
                    diff = np.mean(np.abs(arr_cur - arr_can))
                    if diff < 15.0:
                        is_dup = True
                        dup_of = s_can
                        break
        
        if is_dup:
            duplicate_slides.append({
                "duplicate": s_cur,
                "original": dup_of
            })
        else:
            canonical_slides.append(i)

    print("==================================================")
    print(f"Total canonical distinct slides: {len(canonical_slides)}")
    print(f"Total duplicate slides to replace: {len(duplicate_slides)}")
    print("==================================================")
    
    # Breakdown by theme range
    dups_in_1_100 = [d for d in duplicate_slides if d["duplicate"]["stt"] <= 100]
    dups_in_101_300 = [d for d in duplicate_slides if 101 <= d["duplicate"]["stt"] <= 300]
    dups_in_301_500 = [d for d in duplicate_slides if 301 <= d["duplicate"]["stt"] <= 500]
    
    print(f"Duplicates in Themes 1-100:   {len(dups_in_1_100)}")
    print(f"Duplicates in Themes 101-300: {len(dups_in_101_300)}")
    print(f"Duplicates in Themes 301-500: {len(dups_in_301_500)}")
    
    # Save duplicate list to JSON
    out_data = []
    for d in duplicate_slides:
        out_data.append({
            "stt": d["duplicate"]["stt"],
            "slide_idx": d["duplicate"]["slide_idx"],
            "slide_name": d["duplicate"]["slide_name"],
            "path": d["duplicate"]["path"],
            "dup_of_theme": d["original"]["stt"],
            "dup_of_slide": d["original"]["slide_idx"]
        })
    with open("scripts/visual_duplicates_list.json", "w", encoding="utf-8") as f:
        json.dump(out_data, f, indent=2)
    print("Saved duplicate targets to scripts/visual_duplicates_list.json")

if __name__ == "__main__":
    main()
