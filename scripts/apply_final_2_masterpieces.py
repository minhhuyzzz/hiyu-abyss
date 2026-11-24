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

def remove_ai_sheen_and_enhance(im):
    if im.mode != "RGB":
        im = im.convert("RGB")
    enhancer = ImageEnhance.Color(im)
    im = enhancer.enhance(0.96)
    
    w, h = im.size
    np.random.seed(42)
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

def get_dhash(image_path, hash_size=8):
    with Image.open(image_path) as img:
        img = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = np.asarray(img)
        diff = pixels[:, 1:] > pixels[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def main():
    print("=== APPLYING FRESH MASTERPIECES TO 490 & 409 ===")
    
    raw_490 = "assets/templates/raw_cache/aristotle_rembrandt.jpg"
    raw_409 = "assets/templates/raw_cache/caravaggio_calling.jpg"
    
    # Process Theme 490 slide 1
    im_490 = Image.open(raw_490)
    norm_490 = remove_ai_sheen_and_enhance(crop_to_9_16(im_490))
    safe_save_image(norm_490, "assets/templates/multislides/theme_490/slide_1.jpg")
    safe_save_image(norm_490, "website/public/images/themes/theme_490/slide_1.jpg")
    print("Theme 490 slide 1 updated with Aristotle with a Bust of Homer (Rembrandt)")
    
    # Process Theme 409 slide 1
    im_409 = Image.open(raw_409)
    norm_409 = remove_ai_sheen_and_enhance(crop_to_9_16(im_409))
    safe_save_image(norm_409, "assets/templates/multislides/theme_409/slide_1.jpg")
    safe_save_image(norm_409, "website/public/images/themes/theme_409/slide_1.jpg")
    print("Theme 409 slide 1 updated with The Calling of Saint Matthew (Caravaggio)")
    
    # Update asset catalog
    catalog_path = "website/src/data/asset-catalog.json"
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    if "theme_490" in catalog:
        catalog["theme_490"]["artist"] = "Rembrandt van Rijn & các danh họa cổ điển"
        catalog["theme_490"]["title"] = "Bộ kiệt tác sơn dầu độc bản: Aristotle with a Bust of Homer (Rembrandt, 1653, Met), Caspar David Friedrich & Rembrandt"
        catalog["theme_490"]["museum"] = "Metropolitan Museum of Art, New York / HYA-08 Canvas Normalized"
        
    if "theme_409" in catalog:
        catalog["theme_409"]["artist"] = "Caravaggio"
        catalog["theme_409"]["title"] = "Kiệt tác sơn dầu độc bản: The Calling of Saint Matthew (Caravaggio, 1599-1600)"
        catalog["theme_409"]["museum"] = "San Luigi dei Francesi, Rome / HYA-08 Canvas Normalized"
        
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        
    print("Asset catalog updated!")

if __name__ == "__main__":
    main()
