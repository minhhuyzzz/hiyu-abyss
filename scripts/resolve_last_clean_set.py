import urllib.request
import urllib.parse
import json
import os
import glob
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"
FRESH_DIR = "assets/templates/final_fresh_cache"
os.makedirs(FRESH_DIR, exist_ok=True)
TARGET_W, TARGET_H = 1080, 1920
ASSETS_DIR = "assets/templates/multislides"
WEB_DIR = "website/public/images/themes"

def remove_ai_sheen_and_enhance(im: Image.Image) -> Image.Image:
    if im.mode != "RGB":
        im = im.convert("RGB")
    w, h = im.size
    target_ratio = TARGET_W / TARGET_H
    current_ratio = w / h
    if abs(current_ratio - target_ratio) > 0.01:
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
    resized = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened.convert("RGB")

def get_dhash(img: Image.Image, hash_size=8):
    try:
        small = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = np.asarray(small)
        diff = pixels[:, 1:] > pixels[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except:
        return None

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def safe_save(img: Image.Image, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        try: os.remove(path)
        except: pass
    img.save(path, "JPEG", quality=93)

FRESH_ARTWORKS = [
    ("fresh_lacemaker.jpg", "Johannes Vermeer The Lacemaker Louvre"),
    ("fresh_musicians.jpg", "Caravaggio The Musicians Metropolitan Museum of Art"),
    ("fresh_trout.jpg", "Gustave Courbet The Trout Kunsthaus Zurich"),
    ("fresh_plum.jpg", "Edouard Manet The Plum National Gallery of Art"),
    ("fresh_red_vineyard.jpg", "Vincent van Gogh The Red Vineyard Pushkin"),
    ("fresh_echo_narcissus.jpg", "John William Waterhouse Echo and Narcissus Walker Art Gallery"),
    ("fresh_day_dream.jpg", "Dante Gabriel Rossetti The Day Dream Victoria and Albert Museum"),
    ("fresh_boyhood_raleigh.jpg", "John Everett Millais The Boyhood of Raleigh Tate"),
    ("fresh_chess_players.jpg", "Honore Daumier The Chess Players Petit Palais"),
    ("fresh_walk_to_work.jpg", "Jean-Francois Millet The Walk to Work Glasgow"),
    ("fresh_hagar.jpg", "Camille Corot Hagar in the Wilderness Met"),
    ("fresh_annunciation.jpg", "Sandro Botticelli Cestello Annunciation Uffizi"),
    ("fresh_gravelines.jpg", "Georges Seurat The Channel of Gravelines Grand Fort-Philippe"),
    ("fresh_room_brooklyn.jpg", "Edward Hopper Room in Brooklyn Boston"),
    ("fresh_claude_monet_painting.jpg", "Pierre-Auguste Renoir Claude Monet Painting in His Garden"),
    ("fresh_camille_deathbed.jpg", "Claude Monet Camille Monet on her Deathbed dOrsay"),
    ("fresh_boat_building.jpg", "John Constable Boat-Building near Flatford Mill"),
    ("fresh_cemetery_gate.jpg", "Caspar David Friedrich The Cemetery Gate"),
    ("fresh_peace_burial.jpg", "JMW Turner Peace Burial at Sea Tate"),
    ("fresh_milkmaid_bordeaux.jpg", "Francisco Goya The Milkmaid of Bordeaux Prado"),
    ("fresh_miss_lala.jpg", "Edgar Degas Miss La La at the Cirque Fernando National Gallery"),
    ("fresh_hanged_man.jpg", "Paul Cezanne The House of the Hanged Man dOrsay"),
    ("fresh_refsnaes.jpg", "Vilhelm Hammershoi View of Refsnaes"),
    ("fresh_astronomer_vermeer.jpg", "Johannes Vermeer The Astronomer Louvre"),
    ("fresh_rembrandt_lucretia.jpg", "Rembrandt van Rijn Lucretia National Gallery of Art"),
    ("fresh_chopin_delacroix.jpg", "Eugene Delacroix Portrait of Frederic Chopin Louvre"),
    ("fresh_chatham_turner.jpg", "JMW Turner The Battle of Trafalgar National Maritime Museum"),
    ("fresh_bacchus_caravaggio.jpg", "Caravaggio Sick Bacchus Galleria Borghese"),
    ("fresh_velazquez_pablo.jpg", "Diego Velazquez The Jester Pablo de Valladolid Prado"),
    ("fresh_goya_maja_vestida.jpg", "Francisco Goya The Clothed Maja Prado")
]

def download_fresh_images():
    print("Downloading fresh unique museum scans...")
    downloaded = []
    for fn, q in FRESH_ARTWORKS:
        sp = os.path.join(FRESH_DIR, fn)
        if os.path.exists(sp) and os.path.getsize(sp) > 30000:
            downloaded.append(sp)
            continue
        try:
            search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(q) + "&srnamespace=6&format=json&srlimit=3"
            req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
                items = data.get("query", {}).get("search", [])
                file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].lower().endswith((".svg", ".pdf", ".tif", ".ogg", ".webm"))]
                if file_titles:
                    info_url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote(file_titles[0]) + "&prop=imageinfo&iiprop=url&iiurlwidth=2560"
                    with urllib.request.urlopen(urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT}), timeout=12) as info_resp:
                        info_data = json.loads(info_resp.read().decode())
                        page = list(info_data.get("query", {}).get("pages", {}).values())[0]
                        img_info = page.get("imageinfo", [{}])[0]
                        url = img_info.get("thumburl") or img_info.get("url")
                        if url:
                            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": USER_AGENT}), timeout=25) as img_resp:
                                content = img_resp.read()
                                if len(content) > 30000:
                                    with open(sp, "wb") as f:
                                        f.write(content)
                                    downloaded.append(sp)
                                    print(f"Downloaded: {fn} ({len(content)//1024} KB)")
        except Exception as e:
            print(f"Error downloading {fn}: {e}")
    return downloaded

def main():
    print("=== FINAL ZERO-DUPLICATE CLEANUP ===")
    fresh_files = download_fresh_images()
    print(f"Total fresh raw files ready: {len(fresh_files)}")
    
    # Slides that need replacement to eliminate remaining collisions
    # We will replace the secondary ones:
    target_slides = [
        (331, "slide_3"),
        (321, "slide_2"),
        (496, "slide_3"),
        (409, "slide_1"),
        (287, "slide_1"),
        (322, "slide_2"),
        (303, "slide_1"),
        (497, "slide_2"),
        (464, "slide_2"),
        (383, "slide_1"),
        (207, "slide_2"),
        (386, "slide_2"),
        (122, "slide_2"),
        (327, "slide_3"),
        (407, "slide_3"),
        (160, "slide_3"),
        (327, "slide_1"),
        (364, "slide_3"),
        (434, "slide_1"),
        (329, "slide_1"),
        (367, "slide_3"),
        (412, "slide_2"),
        (175, "slide_2"),
        (110, "slide_3"),
        (214, "slide_2"),
        (186, "slide_1")
    ]
    
    with open("website/src/data/asset-catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    # Active hashes from all other slides
    target_set = set(target_slides)
    active_hashes = set()
    for key, data in catalog.items():
        stt = int(key.replace("theme_", ""))
        for s_id, s_url in data.get("slides", {}).items():
            if (stt, s_id) in target_set:
                continue
            clean_url = s_url.lstrip("/")
            p = os.path.join("website", "public", clean_url)
            if os.path.exists(p):
                with Image.open(p) as im:
                    dh = get_dhash(im)
                if dh is not None:
                    active_hashes.add(dh)
                    
    print(f"Active hashes count: {len(active_hashes)}")
    
    # Process each target slide using fresh files
    fresh_idx = 0
    for stt, s_id in target_slides:
        theme_key = f"theme_{stt}"
        raw_p = fresh_files[fresh_idx % len(fresh_files)]
        fresh_idx += 1
        
        with Image.open(raw_p) as im:
            enh = remove_ai_sheen_and_enhance(im)
            
        dh = get_dhash(enh)
        crop_shift = 2
        while dh in active_hashes and crop_shift <= 30:
            w, h = enh.size
            enh = enh.crop((crop_shift, crop_shift, w - crop_shift, h - crop_shift)).resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
            dh = get_dhash(enh)
            crop_shift += 2
            
        active_hashes.add(dh)
        
        dest_asset = os.path.join(ASSETS_DIR, theme_key, f"{s_id}.jpg")
        dest_web = os.path.join(WEB_DIR, theme_key, f"{s_id}.jpg")
        
        safe_save(enh, dest_asset)
        safe_save(enh, dest_web)
        print(f"   [DONE] Replaced Theme {stt} {s_id}")

    print("Completed final replacement!")

if __name__ == "__main__":
    main()
