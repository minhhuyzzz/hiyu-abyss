import os
import json
import glob
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

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

def main():
    print("==================================================")
    print("   RESOLVING ALL 208 VISUAL DUPLICATE SLIDES      ")
    print("==================================================")
    
    # 1. Load targets
    with open("scripts/visual_duplicates_list.json", "r", encoding="utf-8") as f:
        targets = json.load(f)
    print(f"Total targets to replace: {len(targets)}")
    
    dup_paths = set(t["path"].replace("\\", "/") for t in targets)
    
    # 2. Load all 1000 canonical slides
    all_slide_paths = glob.glob("assets/templates/multislides/theme_*/slide_*.jpg")
    canonical_hashes = []
    canonical_thumbs = []
    
    print("Loading canonical slides into active pool...")
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
        except Exception as e:
            print(f"Error loading {p}: {e}")
            
    print(f"Active canonical pool size: {len(canonical_hashes)}")
    
    # 3. Load metadata from manifest 101-300
    with open("scripts/oil_suites_101_300_manifest.json", "r", encoding="utf-8") as f:
        m_101_300 = json.load(f)
    raw_meta_101_300 = {}
    for t_id, t_val in m_101_300.items():
        for s_val in t_val.get("slides", []):
            rfn = s_val.get("raw_filename")
            if rfn:
                raw_meta_101_300[rfn] = {
                    "artist": s_val.get("artist", "Danh họa Cổ điển Châu Âu"),
                    "title": s_val.get("artwork_title", "Kiệt tác Sơn dầu"),
                    "museum": s_val.get("museum", "Bảo tàng Quốc tế"),
                    "year": s_val.get("year", "Thế kỷ XVII - XIX")
                }
                
    # 4. Gather all available raw files
    raw_candidates = []
    # Prefer raw_cache_101_300 first because they have precise museum metadata
    c1 = glob.glob("assets/templates/raw_cache_101_300/*.jpg")
    c2 = glob.glob("assets/templates/raw_cache/*.jpg")
    
    for rf in c1 + c2:
        if os.path.exists(rf) and os.path.getsize(rf) > 60000:
            raw_candidates.append(rf)
            
    print(f"Total raw candidates ready: {len(raw_candidates)}")
    
    # 5. Load asset catalog for updates
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # 6. Process each duplicate target
    replaced_count = 0
    candidate_idx = 0
    used_raw_paths = set()
    
    for t_idx, target in enumerate(targets):
        stt = target["stt"]
        slide_name = target["slide_name"]
        print(f"\n[{t_idx+1}/{len(targets)}] Finding replacement for Theme {stt} {slide_name} (was dup of Theme {target['dup_of_theme']})...")
        
        found = False
        while candidate_idx < len(raw_candidates):
            raw_path = raw_candidates[candidate_idx]
            candidate_idx += 1
            
            if raw_path in used_raw_paths:
                continue
                
            try:
                with Image.open(raw_path) as raw_im:
                    im_916 = crop_to_9_16(raw_im)
                    h = get_dhash(im_916)
                    if h is None:
                        continue
                        
                    # Check distance against ALL currently active slides in pool
                    min_dist = min([hamming_distance(h, ch) for ch in canonical_hashes])
                    if min_dist <= 2:
                        # Check pixel diff against those close hashes
                        im_thumb = np.array(im_916.convert('RGB').resize((64, 64)), dtype=np.float32)
                        collides = False
                        for ch, c_thumb in zip(canonical_hashes, canonical_thumbs):
                            if hamming_distance(h, ch) <= 2:
                                diff = np.mean(np.abs(im_thumb - c_thumb))
                                if diff < 16.0:
                                    collides = True
                                    break
                        if collides:
                            # Visually too close to an existing slide, skip
                            continue
                            
                    # SUCCESS: Candidate is visually distinct!
                    used_raw_paths.add(raw_path)
                    
                    # Apply HYA-08 physical oil normalization
                    im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 100 + t_idx)
                    h_norm = get_dhash(im_norm)
                    thumb_norm = np.array(im_norm.convert('RGB').resize((64, 64)), dtype=np.float32)
                    
                    # Save image files
                    dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
                    dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
                    safe_save_image(im_norm, dest_multi)
                    safe_save_image(im_norm, dest_web)
                    
                    # Add to active pool
                    canonical_hashes.append(h_norm)
                    canonical_thumbs.append(thumb_norm)
                    
                    # Update metadata
                    fn = os.path.basename(raw_path)
                    meta = raw_meta_101_300.get(fn, {})
                    artist = meta.get("artist")
                    title = meta.get("title")
                    if not artist:
                        # Clean basename for artist/title
                        clean_name = fn.replace(".jpg", "").replace("_raw", "").replace("fresh_", "").replace("raw_", "")
                        artist = clean_name.replace("_", " ").title()
                        title = f"Kiệt tác sơn dầu độc bản ({artist})"
                        
                    theme_key = f"theme_{stt}"
                    if theme_key in catalog:
                        # Append or update artist in catalog
                        cur_artist = catalog[theme_key].get("artist", "")
                        if artist and artist not in cur_artist:
                            catalog[theme_key]["artist"] = f"{artist} & {cur_artist}"[:150]
                            
                    print(f"   --> REPLACED with: {os.path.basename(raw_path)} ({artist} - {title})")
                    replaced_count += 1
                    found = True
                    break
            except Exception as e:
                print(f"Error testing {raw_path}: {e}")
                continue
                
        if not found:
            print(f"WARNING: Ran out of candidates for Theme {stt} {slide_name}!")
            
    print("\n==================================================")
    print(f"REPLACEMENT COMPLETED: {replaced_count} / {len(targets)} duplicate slides replaced!")
    print("==================================================")
    
    # Save updated catalog
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Saved updated website/src/data/asset-catalog.json")

if __name__ == "__main__":
    main()
