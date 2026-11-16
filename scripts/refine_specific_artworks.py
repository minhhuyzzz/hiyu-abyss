#!/usr/bin/env python3
# scripts/refine_specific_artworks.py
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

EXACT_TITLES = [
    ("theme_216_slide_1", "File:Orestes Pursued by the Furies by William-Adolphe Bouguereau (1862) - Google Art Project.jpg"),
    ("theme_228_slide_2", "File:Narcissus by Caravaggio, 1597–1599, Galleria Nazionale d'Arte Antica (21809913606).jpg"),
    ("theme_231_slide_1", "File:Jean Siméon Chardin - Soap Bubbles - Google Art Project.jpg"),
    ("theme_243_slide_1", "File:David with the Head of Goliath (by Guido Reni) - Uffizi Gallery, Florence.jpg"),
    ("theme_248_slide_2", "File:Winslow Homer - The Life Line.jpg")
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

def download_exact(key, exact_title):
    cache_path = os.path.join(CACHE_DIR, f"{key}_refined.jpg")
    info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(exact_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
    content = make_request(info_url)
    if content:
        data = json.loads(content.decode())
        pages = data.get("query", {}).get("pages", {})
        page = list(pages.values())[0]
        img_info = page.get("imageinfo", [{}])[0]
        dl_url = img_info.get("thumburl") or img_info.get("url")
        if dl_url:
            time.sleep(1.0)
            img_bytes = make_request(dl_url)
            if img_bytes:
                with open(cache_path, "wb") as f:
                    f.write(img_bytes)
                print(f"📥 Downloaded {key}: {exact_title[:45]}...")
                return cache_path
    return None

def main():
    print("=== REFINING SPECIFIC MASTERPIECES ===")
    for key, title in EXACT_TITLES:
        parts = key.split("_")
        theme_id = f"{parts[0]}_{parts[1]}"
        slide_name = f"{parts[2]}_{parts[3]}.jpg"

        theme_multislides_dir = os.path.join(OUTPUT_BASE, theme_id)
        theme_website_dir = os.path.join(WEBSITE_PUBLIC, theme_id)

        cached_file = download_exact(key, title)
        if cached_file and os.path.exists(cached_file):
            with Image.open(cached_file) as raw_im:
                purified = process_and_purify_oil_painting(raw_im.convert("RGB"))
                out1 = os.path.join(theme_multislides_dir, slide_name)
                out2 = os.path.join(theme_website_dir, slide_name)
                purified.save(out1, format="JPEG", quality=92)
                purified.save(out2, format="JPEG", quality=92)
                print(f"✨ Refined & replaced {theme_id}/{slide_name}")
        time.sleep(1.2)
    print("=== REFINEMENT COMPLETE ===")

if __name__ == '__main__':
    main()
