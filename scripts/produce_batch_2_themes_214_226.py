#!/usr/bin/env python3
# scripts/produce_batch_2_themes_214_226.py
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

BATCH_2_SLIDES = [
    # 214 (Carousel 3 trang)
    ("theme_214_slide_1", "Lord Frederic Leighton Solitude"),
    ("theme_214_slide_2", "J.M.W. Turner The Slave Ship"),
    ("theme_214_slide_3", "Camille Corot Souvenir de Mortefontaine"),

    # 215 (Carousel 3 trang)
    ("theme_215_slide_1", "Paul Cezanne The Card Players"),
    ("theme_215_slide_2", "Francisco Goya Duel with Cudgels"),
    ("theme_215_slide_3", "Rembrandt The Return of the Prodigal Son"),

    # 216 (Carousel 2 trang)
    ("theme_216_slide_1", "Saturn Devouring His Son Goya"),
    ("theme_216_slide_2", "Winslow Homer The Gulf Stream"),

    # 217 (Carousel 3 trang)
    ("theme_217_slide_1", "Honore Daumier The Third-Class Carriage"),
    ("theme_217_slide_2", "Edvard Munch The Scream"),
    ("theme_217_slide_3", "Albrecht Durer Saint Jerome in His Study"),

    # 218 (Single-Punch)
    ("theme_218_slide_1", "Theodore Gericault The Raft of the Medusa"),

    # 219 (Carousel 2 trang)
    ("theme_219_slide_1", "Waterhouse Circe Offering the Cup to Ulysses"),
    ("theme_219_slide_2", "Claude Monet Rocks at Belle-Ile"),

    # 220 (Carousel 3 trang)
    ("theme_220_slide_1", "Peter Paul Rubens The Fall of Phaeton"),
    ("theme_220_slide_2", "Hieronymus Bosch The Ship of Fools"),
    ("theme_220_slide_3", "Caspar David Friedrich Abbey in the Oak Forest"),

    # 221 (Single-Punch)
    ("theme_221_slide_1", "Jean-Leon Gerome Pollice Verso"),

    # 222 (Carousel 2 trang)
    ("theme_222_slide_1", "Marinus van Reymerswaele The Moneychanger and his Wife"),
    ("theme_222_slide_2", "Caravaggio David with the Head of Goliath"),

    # 223 (Carousel 2 trang)
    ("theme_223_slide_1", "Titian The Flaying of Marsyas"),
    ("theme_223_slide_2", "Jacques-Louis David The Death of Socrates"),

    # 224 (Carousel 3 trang)
    ("theme_224_slide_1", "Theodore Chasseriau The Toilette of Esther"),
    ("theme_224_slide_2", "Degas Little Dancer Aged Fourteen"),
    ("theme_224_slide_3", "Henri Fantin-Latour White Roses"),

    # 225 (Carousel 2 trang)
    ("theme_225_slide_1", "John Everett Millais Ophelia"),
    ("theme_225_slide_2", "Winslow Homer Breezing Up A Fair Wind"),

    # 226 (Single-Punch)
    ("theme_226_slide_1", "Caspar David Friedrich The Monk by the Sea")
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
    print(f"=== BẮT ĐẦU CHẾ TÁC ĐỢT 2: STT 214 - 226 (29 SLIDES ĐỘC BẢN) ===")
    success_count = 0
    fail_count = 0

    for key, query in BATCH_2_SLIDES:
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
    print(f"📊 KẾT QUẢ ĐỢT 2 (STT 214 - 226):")
    print(f"   ✅ Hoàn tất: {success_count} / {len(BATCH_2_SLIDES)} slides")
    print(f"   ❌ Còn thiếu: {fail_count}")
    print(f"==========================================")

if __name__ == '__main__':
    main()
