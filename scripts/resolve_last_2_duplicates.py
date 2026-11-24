import os
import json
import urllib.request
import urllib.parse
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

def search_and_download_commons(query, filename):
    cache_path = os.path.join("assets/templates/raw_cache", filename)
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 50000:
        return cache_path
        
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size&gsrsearch={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'HiyuAbyssArtCuration/2.0 (contact@hiyuabyss.org)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            best_url = None
            max_size = 0
            for pid, pdata in pages.items():
                if 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                    info = pdata['imageinfo'][0]
                    u = info.get('url', '')
                    sz = info.get('size', 0)
                    if sz > max_size and ('.jpg' in u.lower() or '.jpeg' in u.lower() or '.png' in u.lower()):
                        max_size = sz
                        best_url = u.split('?')[0] # strip query params
            if best_url:
                print(f"Downloading {filename} from {best_url} ({max_size//1024} KB)...")
                d_req = urllib.request.Request(best_url, headers={'User-Agent': 'HiyuAbyssArtCuration/2.0'})
                with urllib.request.urlopen(d_req, timeout=30) as d_res:
                    with open(cache_path, 'wb') as out_f:
                        out_f.write(d_res.read())
                print(f"Downloaded: {cache_path}")
                return cache_path
    except Exception as e:
        print(f"Failed to download {query}: {e}")
    return None

def main():
    print("=== RESOLVING FINAL 2 DUPLICATES ===")
    
    # 1. Henri Rousseau The Sleeping Gypsy for Theme 490 slide 1
    raw_490 = search_and_download_commons("Henri Rousseau The Sleeping Gypsy MoMA", "raw_sleeping_gypsy.jpg")
    if not raw_490 or not os.path.exists(raw_490):
        raw_490 = search_and_download_commons("Henri Rousseau The Sleeping Gypsy", "raw_sleeping_gypsy.jpg")
        
    # 2. Edgar Degas L'Absinthe for Theme 409 slide 1
    raw_409 = search_and_download_commons("Edgar Degas L'Absinthe Musee d'Orsay", "raw_absinthe.jpg")
    if not raw_409 or not os.path.exists(raw_409):
        raw_409 = search_and_download_commons("Edgar Degas L'Absinthe", "raw_absinthe.jpg")
        
    print(f"Raw 490: {raw_490}")
    print(f"Raw 409: {raw_409}")
    
    # Process 490 slide 1
    if raw_490 and os.path.exists(raw_490):
        im = Image.open(raw_490)
        im_916 = crop_to_9_16(im)
        im_norm = remove_ai_sheen_and_enhance(im_916)
        safe_save_image(im_norm, "assets/templates/multislides/theme_490/slide_1.jpg")
        safe_save_image(im_norm, "website/public/images/themes/theme_490/slide_1.jpg")
        print("Updated Theme 490 slide 1!")
        
    # Process 409 slide 1
    if raw_409 and os.path.exists(raw_409):
        im = Image.open(raw_409)
        im_916 = crop_to_9_16(im)
        im_norm = remove_ai_sheen_and_enhance(im_916)
        safe_save_image(im_norm, "assets/templates/multislides/theme_409/slide_1.jpg")
        safe_save_image(im_norm, "website/public/images/themes/theme_409/slide_1.jpg")
        print("Updated Theme 409 slide 1!")
        
    # Update catalog
    catalog_path = "website/src/data/asset-catalog.json"
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    if "theme_490" in catalog:
        catalog["theme_490"]["artist"] = "Henri Rousseau, Rembrandt & Caspar David Friedrich"
        catalog["theme_490"]["title"] = "Bộ kiệt tác sơn dầu độc bản: The Sleeping Gypsy (Henri Rousseau, 1897), Rembrandt & Caspar David Friedrich"
        
    if "theme_409" in catalog:
        catalog["theme_409"]["artist"] = "Edgar Degas"
        catalog["theme_409"]["title"] = "Kiệt tác sơn dầu độc bản: L'Absinthe (Edgar Degas, 1876, Musée d'Orsay)"
        catalog["theme_409"]["museum"] = "Musée d'Orsay, Paris / HYA-08 Canvas Normalized"
        
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        
    print("Catalog updated successfully!")

if __name__ == "__main__":
    main()
