import urllib.request
import urllib.parse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"
RAW_CACHE = "assets/templates/raw_cache_101_300"

with open("scripts/missing_downloads_101_300.json", "r", encoding="utf-8") as f:
    missing = json.load(f)

print(f"Total missing to download: {len(missing)}")

def download_one(item):
    raw_fn = item["raw_filename"]
    save_path = os.path.join(RAW_CACHE, raw_fn)
    if os.path.exists(save_path) and os.path.getsize(save_path) > 30000:
        return raw_fn, "CACHED", save_path
        
    artist = item["artist"]
    title = item["title"]
    
    # Try cleaner queries
    queries_to_try = [
        f"{artist} {title}",
        f"{artist} {title.split('(')[0].strip()}",
        f"{title} oil painting"
    ]
    
    for q in queries_to_try:
        try:
            search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(q) + "&srnamespace=6&format=json&srlimit=3"
            req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
                items = data.get("query", {}).get("search", [])
                file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].lower().endswith((".svg", ".pdf", ".tif", ".ogg", ".webm"))]
                if file_titles:
                    chosen = file_titles[0]
                    info_url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote(chosen) + "&prop=imageinfo&iiprop=url&iiurlwidth=2560"
                    info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
                    with urllib.request.urlopen(info_req, timeout=12) as info_resp:
                        info_data = json.loads(info_resp.read().decode())
                        page = list(info_data.get("query", {}).get("pages", {}).values())[0]
                        img_info = page.get("imageinfo", [{}])[0]
                        url = img_info.get("thumburl") or img_info.get("url")
                        if url:
                            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": USER_AGENT}), timeout=25) as img_resp:
                                content = img_resp.read()
                                if len(content) > 30000:
                                    with open(save_path, "wb") as f:
                                        f.write(content)
                                    return raw_fn, "OK", save_path
        except Exception as e:
            pass
        time.sleep(0.1)
        
    return raw_fn, "FAILED", None

start = time.time()
with ThreadPoolExecutor(max_workers=8) as ex:
    futures = [ex.submit(download_one, m) for m in missing]
    completed = 0
    for fut in as_completed(futures):
        fn, status, path = fut.result()
        completed += 1
        if completed % 25 == 0 or completed == len(missing):
            print(f"[{completed}/{len(missing)}] processed ({time.time() - start:.1f}s)...")

# Count how many files are now in cache
all_cached = [f for f in os.listdir(RAW_CACHE) if f.endswith(".jpg") and os.path.getsize(os.path.join(RAW_CACHE, f)) > 30000]
print(f"Total valid cached files in {RAW_CACHE}: {len(all_cached)} / 477")
