#!/usr/bin/env python3
# scripts/produce_remaining_10_slides.py
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

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H
USER_AGENT = "HiyuAbyssArtCuration/2.1 (contact: minhhuy868762@gmail.com) Python-urllib"

REMAINING_10_SLIDES = [
    # 223 slide 3 (Ranh giới là thông báo)
    ("theme_223_slide_3", "Rembrandt Man in Armour Glasgow"),

    # 225 slide 3 (Rời bỏ mối quan hệ độc hại)
    ("theme_225_slide_3", "Winslow Homer The Fog Warning"),

    # 230 slide 2 (So sánh ngầm trên mạng xã hội)
    ("theme_230_slide_2", "Edouard Manet The Plum"),

    # 234 slide 3 (Lỗi quy kết cơ bản)
    ("theme_234_slide_3", "Honore Daumier The Lawyers"),

    # 235 slide 2 (Buông bỏ thù hận đã quên)
    ("theme_235_slide_2", "Georges de La Tour Saint Joseph the Carpenter"),

    # 237 slide 3 (Vết mù thiên kiến)
    ("theme_237_slide_3", "Diego Velazquez Las Hilanderas The Spinners"),

    # 239 slide 3 (Nguyên lý kẻ ít quan tâm hơn)
    ("theme_239_slide_3", "Johannes Vermeer Lady Writing a Letter with her Maid"),

    # 242 slide 2 (Không sợ cô độc)
    ("theme_242_slide_2", "Caspar David Friedrich The Solitary Tree"),

    # 242 slide 3 (Làm bạn với sự tĩnh lặng)
    ("theme_242_slide_3", "Odilon Redon Silence"),

    # 244 slide 3 (Tâm hồn như ngôi đền cổ kính)
    ("theme_244_slide_3", "Hubert Robert Ancient Ruins Terrace")
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
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
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
    return None

def main():
    print("=== CHẾ TÁC 10 SLIDES CUỐI CÙNG CHO ĐỦ 115 SLIDES ===")
    success = 0
    for key, q in REMAINING_10_SLIDES:
        parts = key.split("_")
        theme_id = f"{parts[0]}_{parts[1]}"
        slide_name = f"{parts[2]}_{parts[3]}.jpg"

        theme_multislides_dir = os.path.join(OUTPUT_BASE, theme_id)
        theme_website_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
        os.makedirs(theme_multislides_dir, exist_ok=True)
        os.makedirs(theme_website_dir, exist_ok=True)

        cached_file = resolve_and_download(key, q)
        if cached_file and os.path.exists(cached_file):
            with Image.open(cached_file) as raw_im:
                purified = process_and_purify_oil_painting(raw_im.convert("RGB"))
                out1 = os.path.join(theme_multislides_dir, slide_name)
                out2 = os.path.join(theme_website_dir, slide_name)
                purified.save(out1, format="JPEG", quality=92)
                purified.save(out2, format="JPEG", quality=92)
                print(f"✨ Purified & saved {theme_id}/{slide_name}")
                success += 1
        time.sleep(1.2)
    print(f"=== ĐÃ XONG: {success} / {len(REMAINING_10_SLIDES)} slides ===")

if __name__ == '__main__':
    main()
