#!/usr/bin/env python3
# scripts/resolve_missing_11_slides.py
import urllib.request
import urllib.parse
import json
import time

with open("scripts/resolved_48_distinct_oil_art.json", "r", encoding="utf-8") as f:
    resolved = json.load(f)

MISSING = [
    ("theme_101_slide_1", "Monet Garden at Vetheuil"),
    ("theme_101_slide_2", "Sargent Villa Torlonia"),
    ("theme_107_slide_1", "Bouguereau L'oiseau"),
    ("theme_109_slide_1", "Turner Snow Storm Steam-Boat"),
    ("theme_109_slide_2", "Carl Larsson Lathörnet"),
    ("theme_110_slide_1", "Chardin Silver Goblet"),
    ("theme_117_slide_1", "Aivazovsky Ninth Wave"),
    ("theme_117_slide_2", "Winslow Homer West Point Prout's Neck"),
    ("theme_118_slide_1", "Caspar David Friedrich Chasm"),
    ("theme_119_slide_1", "Chardin Jar of Apricots"),
    ("theme_119_slide_2", "Kintsugi tea bowl")
]

for key, q in MISSING:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("query", {}).get("search", [])
            file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].endswith(".svg") and not it["title"].endswith(".pdf") and not it["title"].endswith(".tif")]
            if file_titles:
                chosen_title = file_titles[0]
                info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(chosen_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
                info_req = urllib.request.Request(info_url, headers={"User-Agent": "HiyuAbyssBot/1.0"})
                time.sleep(0.5)
                with urllib.request.urlopen(info_req, timeout=15) as info_resp:
                    info_data = json.loads(info_resp.read().decode())
                    pages = info_data.get("query", {}).get("pages", {})
                    page = list(pages.values())[0]
                    img_info = page.get("imageinfo", [{}])[0]
                    dl_url = img_info.get("thumburl") or img_info.get("url")
                    resolved[key] = {
                        "title": chosen_title,
                        "url": dl_url,
                        "query": q
                    }
                    print(f"✅ {key} -> {chosen_title[:45]}...")
            else:
                print(f"⚠️ {key}: No file found for '{q}'")
    except Exception as e:
        print(f"❌ {key} Error: {e}")
    time.sleep(0.8)

with open("scripts/resolved_48_distinct_oil_art.json", "w", encoding="utf-8") as out:
    json.dump(resolved, out, ensure_ascii=False, indent=2)

print(f"\nFinal count in resolved_48_distinct_oil_art.json: {len(resolved)} / 48 slides!")
