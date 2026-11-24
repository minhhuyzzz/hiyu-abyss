import urllib.request
import urllib.parse
import json
import os
import time

CACHE_DIR = "assets/templates/raw_cache"
USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

EXTRA_QUERIES = [
    ("van_gogh_starry_night.jpg", "Vincent van Gogh The Starry Night MoMA"),
    ("van_gogh_sunflowers.jpg", "Vincent van Gogh Sunflowers National Gallery"),
    ("bruegel_hunters.jpg", "Pieter Bruegel the Elder Hunters in the Snow"),
    ("botticelli_birth_venus.jpg", "Sandro Botticelli The Birth of Venus Uffizi"),
    ("velazquez_meninas.jpg", "Diego Velazquez Las Meninas Prado"),
    ("goya_colossus.jpg", "Francisco Goya The Colossus Prado"),
    ("el_greco_toledo.jpg", "El Greco View of Toledo MET"),
    ("caravaggio_calling.jpg", "Caravaggio The Calling of Saint Matthew Rome"),
    ("tissot_hide_and_seek.jpg", "James Tissot Hide and Seek National Gallery"),
    ("klimt_the_kiss.jpg", "Gustav Klimt The Kiss Belvedere Vienna")
]

for fn, q in EXTRA_QUERIES:
    save_path = os.path.join(CACHE_DIR, fn)
    if os.path.exists(save_path):
        continue
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
                                print(f"Downloaded: {fn} ({len(content)//1024} KB)")
    except Exception as e:
        print(f"Error {fn}: {e}")
    time.sleep(0.3)

print("Done extra 10.")
