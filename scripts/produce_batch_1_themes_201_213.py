#!/usr/bin/env python3
# scripts/produce_batch_1_themes_201_213.py
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

BATCH_1_SLIDES = [
    # 201 (Carousel 3 trang)
    ("theme_201_slide_1", "Edgar Degas In a Cafe Absinthe"),
    ("theme_201_slide_2", "Vilhelm Hammershoi Interior with an Estranged Couple"),
    ("theme_201_slide_3", "Georges de La Tour The Penitent Magdalen"),

    # 202 (Carousel 3 trang)
    ("theme_202_slide_1", "Ilya Repin Barge Haulers on the Volga"),
    ("theme_202_slide_2", "Edmund Leighton The Accolade"),
    ("theme_202_slide_3", "Caspar David Friedrich Winter Landscape with Church"),

    # 203 (Carousel 2 trang)
    ("theme_203_slide_1", "Caravaggio The Cardsharps"),
    ("theme_203_slide_2", "Honore Daumier Tartuffe"),

    # 204 (Carousel 3 trang)
    ("theme_204_slide_1", "Pieter Bruegel the Elder The Blind Leading the Blind"),
    ("theme_204_slide_2", "Francisco Goya The Third of May 1808"),
    ("theme_204_slide_3", "Caspar David Friedrich Wanderer above the Sea of Fog"),

    # 205 (Carousel 2 trang)
    ("theme_205_slide_1", "Rembrandt The Anatomy Lesson of Dr. Nicolaes Tulp"),
    ("theme_205_slide_2", "Gustave Courbet The Desperate Man"),

    # 206 (Single-Punch)
    ("theme_206_slide_1", "Quentin Matsys The Moneylender and his Wife"),

    # 207 (Carousel 3 trang)
    ("theme_207_slide_1", "Caravaggio The Incredulity of Saint Thomas"),
    ("theme_207_slide_2", "Francisco Goya Saturn Devouring His Son"),
    ("theme_207_slide_3", "Artemisia Gentileschi Allegory of Inclination"),

    # 208 (Carousel 2 trang)
    ("theme_208_slide_1", "Bouguereau The Broken Pitcher"),
    ("theme_208_slide_2", "Dante Gabriel Rossetti Proserpine"),

    # 209 (Carousel 3 trang)
    ("theme_209_slide_1", "Edward Burne-Jones The Depths of the Sea"),
    ("theme_209_slide_2", "Caspar David Friedrich The Sea of Ice"),
    ("theme_209_slide_3", "Claude Monet Sunflowers"),

    # 210 (Single-Punch)
    ("theme_210_slide_1", "Jacques-Louis David The Death of Marat"),

    # 211 (Carousel 3 trang)
    ("theme_211_slide_1", "Diego Velazquez Las Meninas"),
    ("theme_211_slide_2", "Jan Steen The Dissolute Household"),
    ("theme_211_slide_3", "Johannes Vermeer Woman Holding a Balance"),

    # 212 (Carousel 2 trang)
    ("theme_212_slide_1", "Auguste Rodin The Thinker"),
    ("theme_212_slide_2", "Eugene Delacroix Liberty Leading the People"),

    # 213 (Carousel 3 trang)
    ("theme_213_slide_1", "John William Waterhouse The Lady of Shalott"),
    ("theme_213_slide_2", "Caravaggio Boy with a Basket of Fruit"),
    ("theme_213_slide_3", "Vilhelm Hammershoi Dust Motes Dancing in Sunbeams")
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
    print(f"=== TIẾP TỤC CHẾ TÁC ĐỢT 1: STT 201 - 213 (31 SLIDES ĐỘC BẢN) ===")
    success_count = 0
    fail_count = 0

    for key, query in BATCH_1_SLIDES:
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
    print(f"📊 KẾT QUẢ ĐỢT 1 (STT 201 - 213):")
    print(f"   ✅ Hoàn tất: {success_count} / {len(BATCH_1_SLIDES)} slides")
    print(f"   ❌ Còn thiếu: {fail_count}")
    print(f"==========================================")

if __name__ == '__main__':
    main()
