#!/usr/bin/env python3
# scripts/produce_batch_3_themes_227_238.py
import os
import json
import time
import urllib.request
import urllib.parse
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

OUTPUT_BASE = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"
CACHE_DIR = r"c:\hiyuabyss\assets\templates\raw_cache"

os.makedirs(OUTPUT_BASE, exist_ok=True)
os.makedirs(WEBSITE_PUBLIC, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H

USER_AGENT = "HiyuAbyssArtCuration/2.1 (contact: minhhuy868762@gmail.com) Python-urllib"

BATCH_3_SLIDES = [
    # 227 (Carousel 3 trang)
    ("theme_227_slide_1", "Johannes Vermeer Girl Reading a Letter at an Open Window"),
    ("theme_227_slide_2", "Domenico Fetti The Parable of the Mote and the Beam"),
    ("theme_227_slide_3", "Camille Pissarro Boulevard Montmartre at Night"),

    # 228 (Carousel 2 trang)
    ("theme_228_slide_1", "Alfred Stevens The Psyche"),
    ("theme_228_slide_2", "Caravaggio Narcissus"),

    # 229 (Carousel 3 trang)
    ("theme_229_slide_1", "Jean-Baptiste Greuze The Broken Eggs"),
    ("theme_229_slide_2", "William Hogarth Marriage A-la-Mode The Tete a Tete"),
    ("theme_229_slide_3", "Claude Monet Water Lilies"),

    # 230 (Single-Punch)
    ("theme_230_slide_1", "Caspar David Friedrich Chalk Cliffs on Rugen"),

    # 231 (Carousel 3 trang)
    ("theme_231_slide_1", "Jean-Simeon Chardin The Soap Bubble"),
    ("theme_231_slide_2", "Gerrit van Honthorst The Matchmaker"),
    ("theme_231_slide_3", "Pierre-Auguste Renoir Luncheon of the Boating Party"),

    # 232 (Carousel 2 trang)
    ("theme_232_slide_1", "Rembrandt Philosopher in Meditation"),
    ("theme_232_slide_2", "Edouard Manet A Bar at the Folies-Bergere"),

    # 233 (Carousel 3 trang)
    ("theme_233_slide_1", "Lawrence Alma-Tadema The Roses of Heliogabalus"),
    ("theme_233_slide_2", "Gustave Caillebotte Paris Street Rainy Day"),
    ("theme_233_slide_3", "Albert Bierstadt Sierra Nevada"),

    # 234 (Carousel 2 trang)
    ("theme_234_slide_1", "Francisco Goya The Sleep of Reason Produces Monsters"),
    ("theme_234_slide_2", "J.M.W. Turner Rain Steam and Speed"),

    # 235 (Single-Punch)
    ("theme_235_slide_1", "Harmen Steenwijck Vanitas Still Life"),

    # 236 (Carousel 3 trang)
    ("theme_236_slide_1", "Georges de La Tour The Flea Catcher"),
    ("theme_236_slide_2", "Edgar Degas Place de la Concorde"),
    ("theme_236_slide_3", "Claude Monet Impression Sunrise"),

    # 237 (Carousel 2 trang)
    ("theme_237_slide_1", "Diego Velazquez The Waterseller of Seville"),
    ("theme_237_slide_2", "Caravaggio The Entombment of Christ"),

    # 238 (Carousel 3 trang)
    ("theme_238_slide_1", "Thomas Cole Course of Empire Desolation"),
    ("theme_238_slide_2", "Caspar David Friedrich Two Men Contemplating the Moon"),
    ("theme_238_slide_3", "Johannes Vermeer The Milkmaid")
]

def process_and_purify_oil_painting(raw_im: Image.Image) -> Image.Image:
    w, h = raw_im.size
    current_ratio = w / h
    
    if abs(current_ratio - TARGET_RATIO) > 0.01:
        if current_ratio > TARGET_RATIO:
            new_w = int(h * TARGET_RATIO)
            left = (w - new_w) // 2
            im = raw_im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / TARGET_RATIO)
            top = (h - new_h) // 2
            im = raw_im.crop((0, top, w, top + new_h))
    else:
        im = raw_im

    resized = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened

def make_request(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = (attempt + 1) * 4
                print(f"⏳ Rate limited (429). Backing off for {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise e
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                raise e
    return None

def resolve_and_download(key, q):
    cache_path = os.path.join(CACHE_DIR, f"{key}.jpg")
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 50000:
        return cache_path

    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
    try:
        content = make_request(url)
        if not content:
            return None
        data = json.loads(content.decode())
        items = data.get("query", {}).get("search", [])
        file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].endswith(".svg") and not it["title"].endswith(".pdf") and not it["title"].endswith(".tif")]
        
        if not file_titles:
            simplified_q = " ".join(q.split()[:3])
            url_fb = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(simplified_q)}&srnamespace=6&format=json&srlimit=5"
            content_fb = make_request(url_fb)
            if content_fb:
                fb_data = json.loads(content_fb.decode())
                items = fb_data.get("query", {}).get("search", [])
                file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].endswith(".svg") and not it["title"].endswith(".pdf") and not it["title"].endswith(".tif")]

        if file_titles:
            chosen_title = file_titles[0]
            info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(chosen_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
            time.sleep(0.8)
            info_content = make_request(info_url)
            if info_content:
                info_data = json.loads(info_content.decode())
                pages = info_data.get("query", {}).get("pages", {})
                page = list(pages.values())[0]
                img_info = page.get("imageinfo", [{}])[0]
                dl_url = img_info.get("thumburl") or img_info.get("url")
                
                if dl_url:
                    time.sleep(0.8)
                    img_bytes = make_request(dl_url)
                    if img_bytes:
                        with open(cache_path, "wb") as f_out:
                            f_out.write(img_bytes)
                        print(f"📥 Downloaded {key}: {chosen_title[:45]}...")
                        return cache_path
    except Exception as e:
        print(f"❌ Error downloading {key} ('{q}'): {e}")
    return None

def main():
    print(f"=== BẮT ĐẦU CHẾ TÁC ĐỢT 3: STT 227 - 238 (27 SLIDES ĐỘC BẢN) ===")
    success_count = 0
    fail_count = 0

    for key, query in BATCH_3_SLIDES:
        parts = key.split("_")
        theme_id = f"{parts[0]}_{parts[1]}"
        slide_name = f"{parts[2]}_{parts[3]}.jpg"

        theme_multislides_dir = os.path.join(OUTPUT_BASE, theme_id)
        theme_website_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
        os.makedirs(theme_multislides_dir, exist_ok=True)
        os.makedirs(theme_website_dir, exist_ok=True)

        out_path_1 = os.path.join(theme_multislides_dir, slide_name)
        out_path_2 = os.path.join(theme_website_dir, slide_name)

        if os.path.exists(out_path_1) and os.path.getsize(out_path_1) > 50000:
            print(f"⏩ Đã tồn tại {theme_id}/{slide_name}")
            success_count += 1
            continue

        cached_file = resolve_and_download(key, query)
        if cached_file and os.path.exists(cached_file):
            try:
                with Image.open(cached_file) as raw_im:
                    purified = process_and_purify_oil_painting(raw_im.convert("RGB"))
                    purified.save(out_path_1, format="JPEG", quality=92)
                    purified.save(out_path_2, format="JPEG", quality=92)
                    print(f"✨ Purified & saved {theme_id}/{slide_name}")
                    success_count += 1
            except Exception as e:
                print(f"❌ Processing error for {key}: {e}")
                fail_count += 1
        else:
            print(f"⚠️ Failed to obtain image for {key}")
            fail_count += 1
        
        time.sleep(1.2)

    print(f"\n==========================================")
    print(f"📊 KẾT QUẢ ĐỢT 3 (STT 227 - 238):")
    print(f"   ✅ Hoàn tất: {success_count} / {len(BATCH_3_SLIDES)} slides")
    print(f"   ❌ Còn thiếu: {fail_count}")
    print(f"==========================================")

if __name__ == '__main__':
    main()
