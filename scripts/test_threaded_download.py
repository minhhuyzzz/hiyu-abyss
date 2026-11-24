import urllib.request
import urllib.parse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"
TEST_CACHE = "assets/templates/fresh_cache_test"
os.makedirs(TEST_CACHE, exist_ok=True)

TEST_PAINTINGS = [
    ("monet_water_lilies_1906.jpg", "Claude Monet Water Lilies 1906 Ryerson Chicago"),
    ("vermeer_milkmaid.jpg", "Johannes Vermeer The Milkmaid Rijksmuseum"),
    ("friedrich_monk_by_the_sea.jpg", "Caspar David Friedrich The Monk by the Sea Alte Nationalgalerie"),
    ("rembrandt_night_watch.jpg", "Rembrandt van Rijn The Night Watch Rijksmuseum"),
    ("turner_rain_steam_speed.jpg", "J.M.W. Turner Rain Steam and Speed National Gallery"),
    ("cezanne_mont_sainte_victoire.jpg", "Paul Cezanne Mont Sainte-Victoire Courtauld"),
    ("homer_breezing_up.jpg", "Winslow Homer Breezing Up National Gallery of Art"),
    ("sargent_el_jaleo.jpg", "John Singer Sargent El Jaleo Isabella Stewart Gardner"),
    ("waterhouse_lady_shalott.jpg", "John William Waterhouse The Lady of Shalott Tate Britain"),
    ("hammershoi_interior_strandgade.jpg", "Vilhelm Hammershoi Interior Strandgade 30")
]

def download_one(item):
    filename, query = item
    save_path = os.path.join(TEST_CACHE, filename)
    if os.path.exists(save_path) and os.path.getsize(save_path) > 30000:
        return filename, "CACHED", os.path.getsize(save_path)
        
    try:
        search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(query) + "&srnamespace=6&format=json&srlimit=3"
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
                                return filename, "OK", len(content)
        return filename, "NOT_FOUND", 0
    except Exception as e:
        return filename, f"ERROR: {e}", 0

start = time.time()
with ThreadPoolExecutor(max_workers=5) as ex:
    futures = [ex.submit(download_one, p) for p in TEST_PAINTINGS]
    for fut in as_completed(futures):
        fn, status, size = fut.result()
        print(f"[{status}] {fn}: {size // 1024} KB")

print(f"Elapsed: {time.time() - start:.2f}s")
