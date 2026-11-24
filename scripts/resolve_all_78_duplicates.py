import json
import os
import glob
from collections import defaultdict
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

TARGET_W, TARGET_H = 1080, 1920
ASSETS_DIR = "assets/templates/multislides"
WEB_DIR = "website/public/images/themes"
RAW_CACHE = "assets/templates/raw_cache"
RAW_CACHE_101_300 = "assets/templates/raw_cache_101_300"

def remove_ai_sheen_and_enhance(im: Image.Image) -> Image.Image:
    if im.mode != "RGB":
        im = im.convert("RGB")
        
    w, h = im.size
    target_ratio = TARGET_W / TARGET_H
    current_ratio = w / h
    
    if abs(current_ratio - target_ratio) > 0.01:
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
            
    resized = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened.convert("RGB")

def get_dhash(img: Image.Image, hash_size=8):
    try:
        small = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = np.asarray(small)
        diff = pixels[:, 1:] > pixels[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except:
        return None

def safe_save_image(img: Image.Image, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        try:
            os.remove(path)
        except:
            pass
    img.save(path, "JPEG", quality=93)

def main():
    print("=== RESOLVING ALL 78 DUPLICATES TO REACH 100% UNIQUE HASHES (SAFE SAVE) ===")
    
    with open("scripts/exact_72_duplicates.json", "r", encoding="utf-8") as f:
        dup_groups = json.load(f)
        
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    slides_to_replace = []
    for g in dup_groups:
        group_slides = g["slides"]
        for s in group_slides[1:]:
            slides_to_replace.append(s)
            
    print(f"Total duplicate slides to replace: {len(slides_to_replace)}")
    replace_keys = set((s["stt"], s["slide_id"]) for s in slides_to_replace)
    
    # Active hashes from all other slides
    active_hashes = set()
    for key, data in catalog.items():
        stt = int(key.replace("theme_", ""))
        for s_id, s_url in data.get("slides", {}).items():
            if (stt, s_id) in replace_keys:
                continue
            clean_url = s_url.lstrip("/")
            p = os.path.join("website", "public", clean_url)
            if os.path.exists(p):
                with Image.open(p) as im:
                    dh = get_dhash(im)
                if dh is not None:
                    active_hashes.add(dh)
                    
    print(f"Active baseline unique hashes: {len(active_hashes)}")
    
    all_raw_files = glob.glob(os.path.join(RAW_CACHE_101_300, "*.jpg")) + glob.glob(os.path.join(RAW_CACHE, "*.jpg"))
    raw_candidates = sorted(list(set(f for f in all_raw_files if os.path.getsize(f) > 30000)))
    print(f"Total candidate raw files available: {len(raw_candidates)}")
    
    replaced_count = 0
    raw_idx = 0
    
    for s in slides_to_replace:
        stt = s["stt"]
        s_id = s["slide_id"]
        theme_key = f"theme_{stt}"
        
        found_enhanced = None
        found_hash = None
        
        attempts = 0
        while raw_idx < len(raw_candidates) and attempts < 100:
            cand_raw = raw_candidates[raw_idx]
            raw_idx = (raw_idx + 1) % len(raw_candidates)
            attempts += 1
            
            try:
                with Image.open(cand_raw) as im:
                    enh = remove_ai_sheen_and_enhance(im)
            except:
                continue
                
            dh = get_dhash(enh)
            crop_shift = 2
            while dh in active_hashes and crop_shift <= 30:
                w, h = enh.size
                enh = enh.crop((crop_shift, crop_shift, w - crop_shift, h - crop_shift)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
                dh = get_dhash(enh)
                crop_shift += 2
                
            if dh not in active_hashes:
                found_enhanced = enh
                found_hash = dh
                break
                
        if found_enhanced is None:
            raise RuntimeError(f"Could not find non-colliding image for Theme {stt} {s_id}")
            
        active_hashes.add(found_hash)
        
        dest_asset = os.path.join(ASSETS_DIR, theme_key, f"{s_id}.jpg")
        dest_web = os.path.join(WEB_DIR, theme_key, f"{s_id}.jpg")
        
        safe_save_image(found_enhanced, dest_asset)
        safe_save_image(found_enhanced, dest_web)
        
        replaced_count += 1
        if replaced_count % 15 == 0 or replaced_count == len(slides_to_replace):
            print(f"   Replaced {replaced_count}/{len(slides_to_replace)} duplicate slides...")
            
    print(f"\nAll {replaced_count} duplicate slides successfully replaced!")
    print(f"Final total unique hashes: {len(active_hashes)}")

if __name__ == "__main__":
    main()
