#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Supplementary Fallback Resolver for Missing Slides
Tìm kiếm bản scan bảo tàng độ phân giải cao cho các slide chưa tải được ở lượt 1 bằng từ khóa mở rộng.
"""

import urllib.request
import urllib.parse
import json
import time
import os
import sys

MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"
CACHE_DIR = "assets/templates/raw_cache"
RESOLVED_PATH = "scripts/resolved_healing_art.json"

USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

BROAD_QUERIES = {
    "theme_254_slide_1": "Pissarro Jardin Tuileries matin",
    "theme_263_slide_1": "Henri Le Sidaner table",
    "theme_264_slide_2": "Thomas Cole Kaaterskill Clove",
    "theme_289_slide_1": "Caspar David Friedrich Sunrise",
    "theme_290_slide_1": "Japanese Kintsugi ceramic tea",
    "theme_293_slide_1": "sunlight window stone interior painting",
    "theme_296_slide_2": "Claude Monet Lavacourt neige",
    "theme_299_slide_1": "birdcage window sunlight painting",
    "theme_300_slide_1": "Caspar David Friedrich Mountain Rainbow"
}

def search_wikimedia(query):
    for attempt in range(1, 3):
        try:
            search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(query) + "&srnamespace=6&format=json&srlimit=5"
            req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
                items = data.get("query", {}).get("search", [])
                file_titles = [
                    it["title"] for it in items 
                    if it["title"].startswith("File:") 
                    and not it["title"].lower().endswith((".svg", ".pdf", ".tif", ".ogg", ".webm"))
                ]
                if file_titles:
                    chosen = file_titles[0]
                    info_url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote(chosen) + "&prop=imageinfo&iiprop=url&iiurlwidth=2560"
                    info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
                    with urllib.request.urlopen(info_req, timeout=12) as info_resp:
                        info_data = json.loads(info_resp.read().decode())
                        pages = info_data.get("query", {}).get("pages", {})
                        page = list(pages.values())[0]
                        img_info = page.get("imageinfo", [{}])[0]
                        url = img_info.get("thumburl") or img_info.get("url")
                        return chosen, url
        except Exception:
            time.sleep(1.0)
    return None, None

def download_image(url, save_path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
            with open(save_path, "wb") as f:
                f.write(data)
            return True
    except Exception:
        return False

def main():
    print("=== CHẠY FALLBACK RESOLVER CHO CÁC SLIDE CÒN THIẾU ===")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    resolved = {}
    if os.path.exists(RESOLVED_PATH):
        try:
            with open(RESOLVED_PATH, "r", encoding="utf-8") as f:
                resolved = json.load(f)
        except Exception:
            pass

    recovered = 0
    for tid, t in manifest.items():
        theme_id = t["theme_id"]
        for s in t["slides"]:
            s_idx = s["slide_index"]
            slide_key = f"{theme_id}_slide_{s_idx}"
            cache_file = os.path.join(CACHE_DIR, f"{slide_key}.jpg")

            if not os.path.exists(cache_file) or os.path.getsize(cache_file) < 40000:
                query = BROAD_QUERIES.get(slide_key, f"{s['artist']} landscape oil")
                print(f"🔍 Thử tìm lại {slide_key} với: '{query}'...")
                title, url = search_wikimedia(query)
                if url:
                    ok = download_image(url, cache_file)
                    if ok:
                        sz_kb = os.path.getsize(cache_file) / 1024
                        print(f"  ✨ Đã cứu thành công ({sz_kb:.0f} KB): {title[:40]}")
                        resolved[slide_key] = {
                            "slide_key": slide_key,
                            "theme_id": theme_id,
                            "slide_index": s_idx,
                            "artist": s["artist"],
                            "artwork_title": s["artwork_title"],
                            "wikimedia_title": title,
                            "url": url,
                            "cache_file": cache_file
                        }
                        recovered += 1
                        with open(RESOLVED_PATH, "w", encoding="utf-8") as f_res:
                            json.dump(resolved, f_res, ensure_ascii=False, indent=2)
                time.sleep(1.0)

    print(f"🎉 Cứu thành công thêm {recovered} slides!")

if __name__ == '__main__':
    main()
