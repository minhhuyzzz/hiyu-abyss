import os
import json
import subprocess
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

Image.MAX_IMAGE_PIXELS = None

SAVE_DIR = "assets/templates/iconic_four"
os.makedirs(SAVE_DIR, exist_ok=True)

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

last_2 = [
    {
        "stt": 496,
        "slide_name": "slide_2",
        "title": "The Sleeping Gypsy",
        "artist": "Henri Rousseau",
        "museum": "Museum of Modern Art, New York",
        "year": "1897",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/The_Sleeping_Gypsy_MoMA%2815%29_%2849581070548%29.jpg",
        "raw_fn": "rousseau_sleeping_gypsy.jpg"
    },
    {
        "stt": 499,
        "slide_name": "slide_2",
        "title": "Whistler's Mother (Arrangement in Grey and Black No. 1)",
        "artist": "James McNeill Whistler",
        "museum": "Musée d'Orsay, Paris",
        "year": "1871",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/James_McNeill_Whistler_-_Photomechanical_reproduction_in_halftone%2C_after_Whistler%27s_portrait_of_his_mother%2C_%22Arrangement_in_G..._-_Google_Art_Project.jpg",
        "raw_fn": "whistlers_mother.jpg"
    }
]

def main():
    print("=== RESOLVING LAST 2 SLIDES FINAL ===")
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    for item in last_2:
        stt = item["stt"]
        slide_name = item["slide_name"]
        raw_dest = os.path.join(SAVE_DIR, item["raw_fn"])
        
        print(f"Downloading {item['title']} by {item['artist']}...")
        ok = download_file(item["url"], raw_dest)
        if not ok:
            print(f"[ERROR] Failed to download {item['title']}")
            continue
            
        with Image.open(raw_dest) as raw_im:
            im_916 = crop_to_9_16(raw_im)
            im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 54321)
            
            dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
            dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
            safe_save_image(im_norm, dest_multi)
            safe_save_image(im_norm, dest_web)
            
            theme_key = f"theme_{stt}"
            if theme_key in catalog:
                if stt == 496:
                    catalog[theme_key]["artist"] = "Vincent van Gogh & Henri Rousseau"
                    catalog[theme_key]["title"] = "Bộ kiệt tác sơn dầu độc bản: The Starry Night (Vincent van Gogh, 1889, MoMA) & The Sleeping Gypsy (Henri Rousseau, 1897, MoMA)"
                    catalog[theme_key]["museum"] = "Museum of Modern Art, New York / HYA-08 Canvas Normalized"
                elif stt == 499:
                    catalog[theme_key]["artist"] = "James McNeill Whistler & các danh họa cổ điển"
                    catalog[theme_key]["title"] = "Bộ kiệt tác sơn dầu độc bản: Whistler's Mother (James McNeill Whistler, 1871, Musée d'Orsay)"
                    catalog[theme_key]["museum"] = "Musée d'Orsay, Paris / HYA-08 Canvas Normalized"
                    
            print(f"Theme {stt} {slide_name} updated successfully with {item['title']} by {item['artist']}!")
            
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Catalog updated successfully!")

if __name__ == "__main__":
    main()
