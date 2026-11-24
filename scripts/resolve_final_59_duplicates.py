import os
import json
import glob
import subprocess
import time
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# Disable PIL decompression bomb limit for ultra-high-res museum scans
Image.MAX_IMAGE_PIXELS = None

CACHE_DIR = "assets/templates/fresh_cache_151"
os.makedirs(CACHE_DIR, exist_ok=True)

def safe_save_image(im, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    if os.path.exists(target_path):
        try:
            os.remove(target_path)
        except Exception:
            pass
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.save(target_path, "JPEG", quality=92)

def remove_ai_sheen_and_enhance(im, seed=None):
    if im.mode != "RGB":
        im = im.convert("RGB")
    enhancer = ImageEnhance.Color(im)
    im = enhancer.enhance(0.96)
    
    w, h = im.size
    if seed is not None:
        np.random.seed(seed)
    noise = np.random.normal(0, 3.5, (h, w, 3)).astype(np.float32)
    img_np = np.array(im, dtype=np.float32) + noise
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)
    im = Image.fromarray(img_np)
    
    im = im.filter(ImageFilter.UnsharpMask(radius=1.5, percent=115, threshold=3))
    return im

def crop_to_9_16(im, target_w=1080, target_h=1920):
    w, h = im.size
    target_ratio = target_w / target_h
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        im_cropped = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 3
        im_cropped = im.crop((0, top, w, top + new_h))
        
    return im_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

def get_dhash(img, hash_size=8):
    try:
        g = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = np.asarray(g)
        diff = pixels[:, 1:] > pixels[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except Exception:
        return None

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def download_file(url, dest_path):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100000:
        return True
    cmd = [
        'curl.exe', '-s',
        '-A', 'HiyuAbyssResearchBot/1.0 (https://hiyuabyss.com; research@hiyuabyss.com)',
        url,
        '-o', dest_path
    ]
    res = subprocess.run(cmd)
    return os.path.exists(dest_path) and os.path.getsize(dest_path) > 100000

def main():
    print("==================================================")
    print("   RESOLVING FINAL 59 VISUAL DUPLICATES           ")
    print("==================================================")
    
    with open("scripts/visual_duplicates_list.json", "r", encoding="utf-8") as f:
        targets = json.load(f)
    print(f"Total targets to replace: {len(targets)}")
    
    # Load candidate pools
    with open("scripts/final_verified_artworks.json", "r", encoding="utf-8") as f:
        pool_final = json.load(f)
    with open("scripts/verified_artworks_download_list.json", "r", encoding="utf-8") as f:
        pool_prev = json.load(f)
        
    # Combine pools, avoiding duplicates
    artworks = list(pool_final)
    seen_titles = set(a['title'] for a in pool_final)
    for a in pool_prev:
        if a['title'] not in seen_titles:
            artworks.append(a)
            seen_titles.add(a['title'])
            
    print(f"Total combined candidate artworks: {len(artworks)}")
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    dup_paths = set(t["path"].replace("\\", "/") for t in targets)
    all_slide_paths = glob.glob("assets/templates/multislides/theme_*/slide_*.jpg")
    canonical_hashes = []
    canonical_thumbs = []
    
    print("Loading active canonical pool...")
    for p in all_slide_paths:
        norm_p = p.replace("\\", "/")
        if norm_p in dup_paths:
            continue
        try:
            with Image.open(p) as img:
                h = get_dhash(img)
                if h is not None:
                    im_thumb = img.convert('RGB').resize((64, 64))
                    canonical_hashes.append(h)
                    canonical_thumbs.append(np.array(im_thumb, dtype=np.float32))
        except Exception:
            pass
            
    print(f"Active canonical pool size: {len(canonical_hashes)}")
    
    art_idx = 0
    success_count = 0
    
    for t_idx, target in enumerate(targets):
        stt = target["stt"]
        slide_name = target["slide_name"]
        print(f"\n[{t_idx+1}/{len(targets)}] Processing Theme {stt} {slide_name}...")
        
        assigned = False
        while art_idx < len(artworks):
            art = artworks[art_idx]
            art_idx += 1
            
            raw_dest = os.path.join(CACHE_DIR, art["safe_filename"])
            print(f"   Fetching: {art['title']} by {art['artist']} ({art['size_kb']} KB)...")
            
            ok = download_file(art["url"], raw_dest)
            if not ok:
                print(f"   [WARN] Download failed, trying next...")
                continue
                
            try:
                with Image.open(raw_dest) as raw_im:
                    im_916 = crop_to_9_16(raw_im)
                    h = get_dhash(im_916)
                    thumb = np.array(im_916.convert('RGB').resize((64, 64)), dtype=np.float32)
                    
                    # Check collision
                    collides = False
                    for ch, c_thumb in zip(canonical_hashes, canonical_thumbs):
                        dist = hamming_distance(h, ch)
                        if dist <= 2:
                            diff = np.mean(np.abs(thumb - c_thumb))
                            if diff < 16.0:
                                collides = True
                                break
                    if collides:
                        print(f"   [COLLISION] Visually too close, skipping...")
                        continue
                        
                    # Apply HYA-08
                    im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 999 + t_idx)
                    h_norm = get_dhash(im_norm)
                    thumb_norm = np.array(im_norm.convert('RGB').resize((64, 64)), dtype=np.float32)
                    
                    dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
                    dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
                    safe_save_image(im_norm, dest_multi)
                    safe_save_image(im_norm, dest_web)
                    
                    canonical_hashes.append(h_norm)
                    canonical_thumbs.append(thumb_norm)
                    
                    # Update metadata in catalog
                    theme_key = f"theme_{stt}"
                    if theme_key in catalog:
                        artist_name = art['artist']
                        art_title = art['title']
                        museum_name = art['museum']
                        
                        catalog[theme_key]["artist"] = f"{artist_name} & các danh họa cổ điển"
                        catalog[theme_key]["title"] = f"Bộ kiệt tác sơn dầu độc bản: {art_title} ({artist_name}, {art['year']})"
                        catalog[theme_key]["museum"] = f"{museum_name} / HYA-08 Canvas Normalized"
                        
                    print(f"   [SUCCESS] Replaced with {art['title']} ({art['artist']}, {art['museum']})")
                    success_count += 1
                    assigned = True
                    break
            except Exception as e:
                print(f"   [ERROR] {e}")
                continue
                
        if not assigned:
            print(f"   [FAILED] Ran out of artworks for Theme {stt} {slide_name}!")
            
    print("\n==================================================")
    print(f"COMPLETED: {success_count} / {len(targets)} duplicate slides replaced!")
    print("==================================================")
    
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Saved updated website/src/data/asset-catalog.json!")

if __name__ == "__main__":
    main()
