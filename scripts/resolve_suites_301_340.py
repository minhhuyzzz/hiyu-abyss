#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Resolve and Download Master Art Scans for Batch 1 (Themes 301 - 340)
Resolves 102 high-resolution master art scans for Themes 301-340 into assets/templates/raw_cache/
"""

import urllib.request
import urllib.parse
import json
import time
import os
import sys
import glob

sys.stdout.reconfigure(line_buffering=True)

MANIFEST_PATH = "scripts/oil_suites_301_500_manifest.json"
RESOLVED_PATH = "scripts/resolved_suites_301_340.json"
CACHE_DIR = "assets/templates/raw_cache"
USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

os.makedirs(CACHE_DIR, exist_ok=True)

def search_wikimedia(query):
    for attempt in range(1, 4):
        try:
            search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(query) + "&srnamespace=6&format=json&srlimit=5"
            req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=10) as resp:
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
                    with urllib.request.urlopen(info_req, timeout=10) as info_resp:
                        info_data = json.loads(info_resp.read().decode())
                        pages = info_data.get("query", {}).get("pages", {})
                        page = list(pages.values())[0]
                        img_info = page.get("imageinfo", [{}])[0]
                        url = img_info.get("thumburl") or img_info.get("url")
                        return chosen, url
        except Exception as e:
            time.sleep(1.0 * attempt)
        time.sleep(0.3)
    return None, None

def download_image(url, save_path):
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
                if len(data) > 30000:
                    with open(save_path, "wb") as f:
                        f.write(data)
                    return True
        except Exception:
            time.sleep(1.0 * attempt)
    return False

def find_cached_fallback(artist, seed_index):
    existing = glob.glob(os.path.join(CACHE_DIR, "*.jpg"))
    if not existing:
        return None
    # Pick a solid high-res masterwork deterministically
    return existing[seed_index % len(existing)]

def main():
    print("=== BẮT ĐẦU PHÂN GIẢI & TẢI 102 BẢN SCAN NGHỆ THUẬT LÔ 1 (THEMES 301 - 340) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    resolved_data = {}
    success_count = 0
    fallback_count = 0
    slide_counter = 0

    for tid, t in manifest.items():
        stt = t["stt"]
        if not (301 <= stt <= 340):
            continue
            
        slides = t["slides"]
        resolved_data[tid] = []
        
        for s in slides:
            slide_counter += 1
            s_idx = s["slide_index"]
            artist = s["artist"]
            metaphor = s["visual_metaphor"]
            target_file = os.path.join(CACHE_DIR, f"theme_{stt}_slide_{s_idx}_raw.jpg")
            
            # Check if file already exists and is healthy
            if os.path.exists(target_file) and os.path.getsize(target_file) > 50000:
                print(f"[{slide_counter}/102] Đã có sẵn: theme_{stt}_slide_{s_idx}_raw.jpg ({os.path.getsize(target_file)//1024} KB)")
                resolved_data[tid].append({
                    "slide_index": s_idx,
                    "artist": artist,
                    "target_file": target_file,
                    "source": "local_cache"
                })
                success_count += 1
                continue
                
            # Build search query
            # Extract main keywords from artist and description
            query_artist = artist.replace("van Rijn", "").strip()
            query = f"{query_artist} oil painting master"
            if "Hammershøi" in artist:
                query = "Vilhelm Hammershoi interior sunshine painting"
            elif "Hopper" in artist:
                query = "Edward Hopper sunlight room painting"
            elif "Friedrich" in artist:
                query = "Caspar David Friedrich landscape painting"
            elif "Sargent" in artist:
                query = "John Singer Sargent portrait oil painting"
            elif "Daumier" in artist:
                query = "Honore Daumier painting"
            elif "Monet" in artist:
                query = "Claude Monet morning landscape painting"
            elif "Rembrandt" in artist:
                query = "Rembrandt self portrait oil painting"
            elif "Vermeer" in artist:
                query = "Johannes Vermeer woman window painting"
                
            title, url = search_wikimedia(query)
            downloaded = False
            if url:
                downloaded = download_image(url, target_file)
                
            if downloaded:
                print(f"[{slide_counter}/102] Tải thành công Wikimedia: theme_{stt}_slide_{s_idx}_raw.jpg ({title[:40]})")
                resolved_data[tid].append({
                    "slide_index": s_idx,
                    "artist": artist,
                    "target_file": target_file,
                    "source": f"wikimedia: {title}"
                })
                success_count += 1
            else:
                # Copy from solid cached masterwork
                fb = find_cached_fallback(artist, slide_counter)
                if fb:
                    with open(fb, "rb") as rf:
                        with open(target_file, "wb") as wf:
                            wf.write(rf.read())
                    print(f"[{slide_counter}/102] Dùng phôi bảo tàng dự phòng: theme_{stt}_slide_{s_idx}_raw.jpg (từ {os.path.basename(fb)})")
                    resolved_data[tid].append({
                        "slide_index": s_idx,
                        "artist": artist,
                        "target_file": target_file,
                        "source": f"fallback_cache: {os.path.basename(fb)}"
                    })
                    fallback_count += 1
                else:
                    print(f"[{slide_counter}/102] ❌ Lỗi phân giải theme_{stt}_slide_{s_idx}!")
                    
    with open(RESOLVED_PATH, "w", encoding="utf-8") as f:
        json.dump(resolved_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n=== KẾT QUẢ PHÂN GIẢI LÔ 1 (THEMES 301 - 340) ===")
    print(f"Tổng số slides: {slide_counter} / 102")
    print(f"Thành công trực tiếp / sẵn có: {success_count}")
    print(f"Phân giải qua bộ đệm dự phòng: {fallback_count}")
    print(f"✅ Đã ghi nhận bản đồ phân giải: {RESOLVED_PATH}")

if __name__ == '__main__':
    main()
