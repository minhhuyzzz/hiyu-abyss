import os
import json
import subprocess
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

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

assignments = [
    {
        "stt": 496,
        "slide_name": "slide_1",
        "title": "Joseph the Carpenter",
        "artist": "Georges de La Tour",
        "museum": "Louvre Museum, Paris",
        "year": "1642",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Saint_Joseph_charpentier_-_Georges_de_La_Tour_-_Mus%C3%A9e_du_Louvre_Peintures_INV_1991.jpg",
        "fn": "last4_joseph_carpenter.jpg"
    },
    {
        "stt": 496,
        "slide_name": "slide_2",
        "title": "The Swing",
        "artist": "Jean-Honoré Fragonard",
        "museum": "Wallace Collection, London",
        "year": "1767",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Joean_Honore_Fragonard_The_Swing.jpg",
        "fn": "last4_the_swing.jpg"
    },
    {
        "stt": 499,
        "slide_name": "slide_2",
        "title": "The Desperate Man",
        "artist": "Gustave Courbet",
        "museum": "Private Collection",
        "year": "1843-1845",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/94/Gustave_Courbet_-_Le_D%C3%A9sesp%C3%A9r%C3%A9_%281843%29.jpg",
        "fn": "last4_desperate_man.jpg"
    },
    {
        "stt": 500,
        "slide_name": "slide_4",
        "title": "L'Absinthe",
        "artist": "Edgar Degas",
        "museum": "Musée d'Orsay, Paris",
        "year": "1876",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/28/In_a_Cafe_aka_Absinthe_by_Edgar_Degas_%2852256229739%29.jpg",
        "fn": "last4_absinthe.jpg"
    }
]

def main():
    print("=== RESOLVING THE FINAL 4 SLIDES ===")
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    for item in assignments:
        stt = item["stt"]
        slide_name = item["slide_name"]
        raw_path = os.path.join(CACHE_DIR, item["fn"])
        
        print(f"Downloading {item['title']} by {item['artist']}...")
        ok = download_file(item["url"], raw_path)
        if not ok:
            print(f"Failed to download {item['title']}")
            continue
            
        with Image.open(raw_path) as raw_im:
            im_916 = crop_to_9_16(raw_im)
            im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 888)
            
            dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
            dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
            safe_save_image(im_norm, dest_multi)
            safe_save_image(im_norm, dest_web)
            
            theme_key = f"theme_{stt}"
            if theme_key in catalog:
                catalog[theme_key]["artist"] = f"{item['artist']} & các danh họa cổ điển"
                catalog[theme_key]["title"] = f"Bộ kiệt tác sơn dầu độc bản: {item['title']} ({item['artist']}, {item['year']})"
                catalog[theme_key]["museum"] = f"{item['museum']} / HYA-08 Canvas Normalized"
                
            print(f"Theme {stt} {slide_name} updated successfully with {item['title']}!")
            
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Catalog updated successfully!")

if __name__ == "__main__":
    main()
