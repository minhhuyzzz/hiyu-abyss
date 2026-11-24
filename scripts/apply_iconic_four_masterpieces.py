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

four_paintings = [
    {
        "stt": 496,
        "slide_name": "slide_1",
        "title": "The Starry Night",
        "artist": "Vincent van Gogh",
        "museum": "Museum of Modern Art, New York",
        "year": "1889",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/cd/VanGogh-starry_night.jpg",
        "raw_fn": "van_gogh_starry_night.jpg"
    },
    {
        "stt": 496,
        "slide_name": "slide_2",
        "title": "Girl with a Pearl Earring",
        "artist": "Johannes Vermeer",
        "museum": "Mauritshuis, The Hague",
        "year": "1665",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/1665_Girl_with_a_Pearl_Earring.jpg",
        "raw_fn": "vermeer_girl_pearl_earring.jpg"
    },
    {
        "stt": 499,
        "slide_name": "slide_2",
        "title": "The Scream",
        "artist": "Edvard Munch",
        "museum": "National Gallery of Norway, Oslo",
        "year": "1893",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg",
        "raw_fn": "munch_the_scream.jpg"
    },
    {
        "stt": 500,
        "slide_name": "slide_4",
        "title": "American Gothic",
        "artist": "Grant Wood",
        "museum": "Art Institute of Chicago",
        "year": "1930",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/71/Grant_DeVolson_Wood_-_American_Gothic.jpg",
        "raw_fn": "grant_wood_american_gothic.jpg"
    }
]

def main():
    print("=== APPLYING 4 ICONIC MASTERPIECES ===")
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    for p in four_paintings:
        stt = p["stt"]
        slide_name = p["slide_name"]
        raw_dest = os.path.join(SAVE_DIR, p["raw_fn"])
        
        print(f"Downloading {p['title']} by {p['artist']}...")
        ok = download_file(p["url"], raw_dest)
        if not ok:
            print(f"[ERROR] Failed to download {p['title']}")
            continue
            
        with Image.open(raw_dest) as raw_im:
            im_916 = crop_to_9_16(raw_im)
            im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 12345)
            
            dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
            dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
            safe_save_image(im_norm, dest_multi)
            safe_save_image(im_norm, dest_web)
            
            theme_key = f"theme_{stt}"
            if theme_key in catalog:
                if stt == 496:
                    catalog[theme_key]["artist"] = "Vincent van Gogh & Johannes Vermeer"
                    catalog[theme_key]["title"] = "Bộ kiệt tác sơn dầu độc bản: The Starry Night (Vincent van Gogh, 1889, MoMA) & Girl with a Pearl Earring (Johannes Vermeer, 1665)"
                    catalog[theme_key]["museum"] = "Museum of Modern Art, New York & Mauritshuis, The Hague / HYA-08 Canvas Normalized"
                elif stt == 499:
                    catalog[theme_key]["artist"] = "Edvard Munch & các danh họa cổ điển"
                    catalog[theme_key]["title"] = "Bộ kiệt tác sơn dầu độc bản: The Scream (Edvard Munch, 1893, National Gallery Oslo)"
                    catalog[theme_key]["museum"] = "National Gallery of Norway, Oslo / HYA-08 Canvas Normalized"
                elif stt == 500:
                    catalog[theme_key]["artist"] = "Grant Wood & các danh họa cổ điển"
                    catalog[theme_key]["title"] = "Bộ kiệt tác sơn dầu độc bản: American Gothic (Grant Wood, 1930, Art Institute of Chicago)"
                    catalog[theme_key]["museum"] = "Art Institute of Chicago / HYA-08 Canvas Normalized"
                    
            print(f"Theme {stt} {slide_name} successfully updated with {p['title']} by {p['artist']}!")
            
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Asset catalog updated successfully!")

if __name__ == "__main__":
    main()
