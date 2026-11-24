import os
import json
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

final_3 = [
    {
        "stt": 496,
        "slide_name": "slide_1",
        "raw_file": "assets/templates/fresh_cache_151/final_art_011_still_life_with_a_chinese.jpg",
        "artist": "Willem Kalf",
        "title": "Still Life with a Chinese Bowl",
        "museum": "Gemäldegalerie, Berlin",
        "year": "1662"
    },
    {
        "stt": 496,
        "slide_name": "slide_2",
        "raw_file": "assets/templates/fresh_cache_151/final_art_024_approaching_thunder_storm.jpg",
        "artist": "Martin Johnson Heade",
        "title": "Approaching Thunder Storm",
        "museum": "Metropolitan Museum of Art, New York",
        "year": "1859"
    },
    {
        "stt": 499,
        "slide_name": "slide_2",
        "raw_file": "assets/templates/fresh_cache_151/final_art_027_the_lackawanna_valley.jpg",
        "artist": "George Inness",
        "title": "The Lackawanna Valley",
        "museum": "National Gallery of Art, Washington",
        "year": "1855"
    }
]

def main():
    print("=== APPLYING THE FINAL 3 SLIDES ===")
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    for item in final_3:
        stt = item["stt"]
        slide_name = item["slide_name"]
        raw_path = item["raw_file"]
        
        with Image.open(raw_path) as raw_im:
            im_916 = crop_to_9_16(raw_im)
            im_norm = remove_ai_sheen_and_enhance(im_916, seed=stt * 9999)
            
            dest_multi = f"assets/templates/multislides/theme_{stt}/{slide_name}.jpg"
            dest_web = f"website/public/images/themes/theme_{stt}/{slide_name}.jpg"
            safe_save_image(im_norm, dest_multi)
            safe_save_image(im_norm, dest_web)
            
            theme_key = f"theme_{stt}"
            if theme_key in catalog:
                catalog[theme_key]["artist"] = f"{item['artist']} & các danh họa cổ điển"
                catalog[theme_key]["title"] = f"Bộ kiệt tác sơn dầu độc bản: {item['title']} ({item['artist']}, {item['year']})"
                catalog[theme_key]["museum"] = f"{item['museum']} / HYA-08 Canvas Normalized"
                
            print(f"Theme {stt} {slide_name} updated successfully with {item['title']} by {item['artist']}!")
            
    with open("website/src/data/asset-catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print("Catalog updated successfully!")

if __name__ == "__main__":
    main()
