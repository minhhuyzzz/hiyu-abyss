#!/usr/bin/env python3
# scripts/resolve_47_distinct_oil_art.py - Tra cứu 47 tác phẩm sơn dầu cổ điển độc bản (Theme 121 - 150)
import urllib.request
import urllib.parse
import json
import time
import os

SLIDES_QUERIES = [
    # 121 - KIÊN CƯỜNG (2 slides)
    ("theme_121_slide_1", "Caspar David Friedrich mist mountain"),
    ("theme_121_slide_2", "Pierre-Auguste Renoir Woman in a Garden"),
    
    # 122 - KIÊN CƯỜNG (1 slide)
    ("theme_122_slide_1", "Caspar David Friedrich The Solitary Tree"),
    
    # 123 - KIÊN CƯỜNG (2 slides)
    ("theme_123_slide_1", "Caspar David Friedrich Winter Landscape"),
    ("theme_123_slide_2", "Georges de La Tour Saint Joseph"),
    
    # 124 - KIÊN CƯỜNG (1 slide)
    ("theme_124_slide_1", "Claude Monet Autumn Seine Argenteuil"),
    
    # 125 - KẾT NỐI (2 slides)
    ("theme_125_slide_1", "Albrecht Durer Great Piece of Turf"),
    ("theme_125_slide_2", "Theodore Rousseau Oak Trees"),
    
    # 126 - KẾT NỐI (1 slide)
    ("theme_126_slide_1", "Winslow Homer Light on the Sea"),
    
    # 127 - KẾT NỐI (2 slides)
    ("theme_127_slide_1", "Camille Pissarro Boulevard Montmartre"),
    ("theme_127_slide_2", "Edouard Manet In the Conservatory"),
    
    # 128 - KẾT NỐI (1 slide)
    ("theme_128_slide_1", "Jean-Simeon Chardin The Silver Goblet"),
    
    # 129 - KẾT NỐI (3 slides)
    ("theme_129_slide_1", "Camille Corot The Roman Campagna"),
    ("theme_129_slide_2", "Honore Daumier The Chess Players"),
    ("theme_129_slide_3", "Claude Monet Fishing Boats"),
    
    # 130 - KẾT NỐI (1 slide)
    ("theme_130_slide_1", "Edouard Manet White Lilacs in a Glass"),
    
    # 131 - KẾT NỐI (2 slides)
    ("theme_131_slide_1", "Hubert Robert Ancient Ruins"),
    ("theme_131_slide_2", "Claude Monet Wheatstacks"),
    
    # 132 - KẾT NỐI (1 slide)
    ("theme_132_slide_1", "Claude Monet Garden Path"),
    
    # 133 - BẢN SẮC (2 slides)
    ("theme_133_slide_1", "Caspar David Friedrich Woman at a Window"),
    ("theme_133_slide_2", "Rembrandt Titus at his Desk"),
    
    # 134 - BẢN SẮC (1 slide)
    ("theme_134_slide_1", "Antonio Canova Psyche Revived"),
    
    # 135 - BẢN SẮC (2 slides)
    ("theme_135_slide_1", "Pieter Claesz Vanitas"),
    ("theme_135_slide_2", "Jan Vermeer The Astronomer"),
    
    # 136 - BẢN SẮC (1 slide)
    ("theme_136_slide_1", "Caspar David Friedrich Chalk Cliffs on Rugen"),
    
    # 137 - BẢN SẮC (2 slides)
    ("theme_137_slide_1", "Pietro Longhi The Masked Ball"),
    ("theme_137_slide_2", "Carl Spitzweg The Bookworm"),
    
    # 138 - BẢN SẮC (1 slide)
    ("theme_138_slide_1", "Albert Bierstadt Mount Corcoran"),
    
    # 139 - BẢN SẮC (3 slides)
    ("theme_139_slide_1", "Rembrandt Aristotle Contemplating Bust"),
    ("theme_139_slide_2", "Philippe de Champaigne Vanitas"),
    ("theme_139_slide_3", "Jean-Simeon Chardin The Basket of Wild Strawberries"),
    
    # 140 - BẢN SẮC (1 slide)
    ("theme_140_slide_1", "J.M.W. Turner Heidelberg Castle"),
    
    # 141 - BẢN SẮC (1 slide)
    ("theme_141_slide_1", "Claude Monet Water Lilies 1906"),
    
    # 142 - VƯỢT PHÁN XÉT (2 slides)
    ("theme_142_slide_1", "Rembrandt Man in Armour"),
    ("theme_142_slide_2", "Caspar David Friedrich Morning in the Riesengebirge"),
    
    # 143 - VƯỢT PHÁN XÉT (1 slide)
    ("theme_143_slide_1", "Pieter Claesz Still Life with Hourglass"),
    
    # 144 - VƯỢT PHÁN XÉT (3 slides)
    ("theme_144_slide_1", "Caravaggio Supper at Emmaus"),
    ("theme_144_slide_2", "Georges de La Tour The Magdalene with the Smoking Flame"),
    ("theme_144_slide_3", "Johannes Vermeer Woman Holding a Balance"),
    
    # 145 - VƯỢT PHÁN XÉT (1 slide)
    ("theme_145_slide_1", "Caravaggio Saint Catherine of Alexandria"),
    
    # 146 - VƯỢT PHÁN XÉT (2 slides)
    ("theme_146_slide_1", "Carl Spitzweg The Bird Catcher"),
    ("theme_146_slide_2", "Bruno Liljefors Sea Eagles"),
    
    # 147 - VƯỢT PHÁN XÉT (1 slide)
    ("theme_147_slide_1", "Anton Mauve Shepherd and Flock"),
    
    # 148 - VƯỢT PHÁN XÉT (2 slides)
    ("theme_148_slide_1", "Joachim Beuckelaer Market Scene"),
    ("theme_148_slide_2", "Vilhelm Hammershoi Sunbeams"),
    
    # 149 - VƯỢT PHÁN XÉT (1 slide)
    ("theme_149_slide_1", "Rembrandt Jeremias beweent de verwoesting"),
    
    # 150 - VƯỢT PHÁN XÉT (1 slide)
    ("theme_150_slide_1", "J.M.W. Turner Chichester Canal")
]

JSON_PATH = "scripts/resolved_47_distinct_oil_art.json"

if os.path.exists(JSON_PATH):
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        resolved = json.load(f)
else:
    resolved = {}

print(f"Total slides: {len(SLIDES_QUERIES)} | Already resolved: {len(resolved)}")

USER_AGENT = "HiyuAbyssResearchBot/2.0 (https://hiyuabyss.local; contact: research@hiyuabyss.org)"

for key, q in SLIDES_QUERIES:
    if key in resolved and resolved[key].get("url"):
        print(f"⏩ {key} already resolved: {resolved[key]['title'][:40]}...")
        continue

    # Attempt resolution with retry
    for attempt in range(1, 4):
        url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
                items = data.get("query", {}).get("search", [])
                file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].endswith(".svg") and not it["title"].endswith(".pdf") and not it["title"].endswith(".tif")]
                if file_titles:
                    chosen_title = file_titles[0]
                    # Now resolve file direct URL with thumbwidth 1920
                    info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(chosen_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
                    info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
                    with urllib.request.urlopen(info_req, timeout=12) as info_resp:
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
                        # Save periodically
                        with open(JSON_PATH, "w", encoding="utf-8") as out:
                            json.dump(resolved, out, ensure_ascii=False, indent=2)
                        break
                else:
                    print(f"⚠️ {key}: No file found for '{q}'")
                    break
        except Exception as e:
            print(f"❌ {key} (Attempt {attempt}): {e}")
            time.sleep(2.5 * attempt)
            
        time.sleep(0.5)
    time.sleep(0.5)

with open(JSON_PATH, "w", encoding="utf-8") as out:
    json.dump(resolved, out, ensure_ascii=False, indent=2)

print(f"\n🎉 Finished resolution: {len(resolved)} / {len(SLIDES_QUERIES)} slides resolved!")
