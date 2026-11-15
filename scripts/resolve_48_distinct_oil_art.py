#!/usr/bin/env python3
# scripts/resolve_48_distinct_oil_art.py - Tra cứu 48 tác phẩm sơn dầu độc bản từ Wikimedia Commons
import urllib.request
import urllib.parse
import json
import time

SLIDES_QUERIES = [
    # 93 - SOLITUDE (1 slide)
    ("theme_93_slide_1", "Caspar David Friedrich Moonrise"),
    
    # 94 - SOLITUDE (2 slides)
    ("theme_94_slide_1", "Alfred Stevens The Mirror"),
    ("theme_94_slide_2", "Carl Larsson Blomsterfonstret"),
    
    # 95 - SOLITUDE (3 slides)
    ("theme_95_slide_1", "Gustave Caillebotte Paris Street"),
    ("theme_95_slide_2", "Rembrandt Philosopher in Meditation"),
    ("theme_95_slide_3", "Jean-Leon Gerome Pygmalion"),
    
    # 96 - STATUS (1 slide)
    ("theme_96_slide_1", "Harmen Steenwijck Vanitas"),
    
    # 97 - STATUS (2 slides)
    ("theme_97_slide_1", "Pietro Longhi Ridotto"),
    ("theme_97_slide_2", "Caravaggio David with the Head of Goliath"),
    
    # 98 - STATUS (1 slide)
    ("theme_98_slide_1", "Thomas Cole Course of Empire Desolation"),
    
    # 99 - STATUS (2 slides)
    ("theme_99_slide_1", "Edgar Degas The Curtain"),
    ("theme_99_slide_2", "Edgar Degas Green Room"),
    
    # 100 - STATUS (3 slides)
    ("theme_100_slide_1", "Anthony van Dyck Charles I"),
    ("theme_100_slide_2", "Philippe de Champaigne Vanitas"),
    ("theme_100_slide_3", "Camille Pissarro The Gardener"),
    
    # 101 - RANH GIỚI (2 slides)
    ("theme_101_slide_1", "Claude Monet Garden at Vetheuil"),
    ("theme_101_slide_2", "John Singer Sargent Villa Torlonia"),
    
    # 102 - RANH GIỚI (1 slide)
    ("theme_102_slide_1", "Winslow Homer Coast of Maine"),
    
    # 103 - RANH GIỚI (2 slides)
    ("theme_103_slide_1", "Rembrandt Man in Armour"),
    ("theme_103_slide_2", "John Constable Flatford Mill"),
    
    # 104 - RANH GIỚI (1 slide)
    ("theme_104_slide_1", "John Constable The Hay Wain"),
    
    # 105 - RANH GIỚI (3 slides)
    ("theme_105_slide_1", "Caspar David Friedrich Eldena"),
    ("theme_105_slide_2", "Jean-Simeon Chardin Brioche"),
    ("theme_105_slide_3", "Claude Monet Garden at Giverny"),
    
    # 106 - RANH GIỚI (1 slide)
    ("theme_106_slide_1", "Bruno Liljefors Sea Eagle"),
    
    # 107 - RANH GIỚI (2 slides)
    ("theme_107_slide_1", "Bouguereau The Empty Birdcage"),
    ("theme_107_slide_2", "Caspar David Friedrich The Lone Tree"),
    
    # 108 - RANH GIỚI (1 slide)
    ("theme_108_slide_1", "Thomas Eakins The Chess Players"),
    
    # 109 - THANH THẢN (2 slides)
    ("theme_109_slide_1", "J.M.W. Turner Snow Storm"),
    ("theme_109_slide_2", "Carl Larsson Lathornet"),
    
    # 110 - THANH THẢN (1 slide)
    ("theme_110_slide_1", "Jean-Simeon Chardin Silver Goblet"),
    
    # 111 - THANH THẢN (3 slides)
    ("theme_111_slide_1", "Caspar David Friedrich Wanderer above the Sea of Fog"),
    ("theme_111_slide_2", "Thomas Cole Mountain Ford"),
    ("theme_111_slide_3", "Albert Bierstadt Sierra Nevada"),
    
    # 112 - THANH THẢN (1 slide)
    ("theme_112_slide_1", "Jean-Simeon Chardin Plums"),
    
    # 113 - THANH THẢN (2 slides)
    ("theme_113_slide_1", "Pieter de Hooch Mother and Child"),
    ("theme_113_slide_2", "Johannes Vermeer Girl reading a letter"),
    
    # 114 - THANH THẢN (1 slide)
    ("theme_114_slide_1", "Joseph Wright of Derby Orrery"),
    
    # 115 - THANH THẢN (2 slides)
    ("theme_115_slide_1", "Georges de La Tour Flea Catcher"),
    ("theme_115_slide_2", "Joseph Wright of Derby Iron Forge"),
    
    # 116 - THANH THẢN (1 slide)
    ("theme_116_slide_1", "John Constable The White Horse"),
    
    # 117 - KIÊN CƯỜNG (2 slides)
    ("theme_117_slide_1", "Ivan Aivazovsky The Ninth Wave"),
    ("theme_117_slide_2", "Winslow Homer West Point Prout"),
    
    # 118 - KIÊN CƯỜNG (1 slide)
    ("theme_118_slide_1", "Caspar David Friedrich Rocky Chasm"),
    
    # 119 - KIÊN CƯỜNG (3 slides)
    ("theme_119_slide_1", "Jean-Simeon Chardin Jar of Apricots"),
    ("theme_119_slide_2", "Kintsugi"),
    ("theme_119_slide_3", "Sevres vase"),
    
    # 120 - KIÊN CƯỜNG (1 slide)
    ("theme_120_slide_1", "Joseph Wright of Derby Blacksmith Shop")
]

print(f"Total slides to resolve: {len(SLIDES_QUERIES)}")

resolved = {}

for key, q in SLIDES_QUERIES:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("query", {}).get("search", [])
            file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].endswith(".svg") and not it["title"].endswith(".pdf") and not it["title"].endswith(".tif")]
            if file_titles:
                chosen_title = file_titles[0]
                # Now resolve file direct URL with thumbwidth 1920
                info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(chosen_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
                info_req = urllib.request.Request(info_url, headers={"User-Agent": "HiyuAbyssBot/1.0"})
                with urllib.request.urlopen(info_req, timeout=10) as info_resp:
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
    time.sleep(0.1)

with open("scripts/resolved_48_distinct_oil_art.json", "w", encoding="utf-8") as out:
    json.dump(resolved, out, ensure_ascii=False, indent=2)

print(f"\nSuccessfully resolved {len(resolved)} / {len(SLIDES_QUERIES)} slides!")
