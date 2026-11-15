#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Resolve and Download 50 Classical Masterpieces (Theme 151 - 200)
Truy vấn Wikimedia Commons API, phân giải bản scan bảo tàng độ phân giải cao (3000px-5000px)
và tải về lưu vào assets/templates/raw_cache/{theme_id}.jpg.
"""

import urllib.request
import urllib.parse
import json
import time
import os
import sys

# Ensure immediate flush for logging
sys.stdout.reconfigure(line_buffering=True)

MANIFEST_PATH = "scripts/oil_suites_151_200_prompts_manifest.json"
RESOLVED_PATH = "scripts/resolved_50_master_oil_art.json"
CACHE_DIR = "assets/templates/raw_cache"

USER_AGENT = "HiyuAbyssResearchBot/2.0 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

os.makedirs(CACHE_DIR, exist_ok=True)

# Bản đồ tinh chỉnh từ khóa tìm kiếm để khớp bản scan bảo tàng chất lượng cao nhất
CUSTOM_SEARCH_QUERIES = {
    "theme_151": "The Penitent Magdalen MET Georges de La Tour",
    "theme_152": "Caravaggio Narcissus Palazzo Barberini",
    "theme_153": "Caravaggio The Cardsharps Kimbell",
    "theme_154": "John William Waterhouse La Belle Dame sans Merci 1893",
    "theme_155": "Vilhelm Hammershoi Interieur mit Rueckenansicht einer Frau",
    "theme_156": "Quentin Matsys The Moneylender and his Wife Louvre",
    "theme_157": "Francisco Goya Saturn Devouring His Son Prado",
    "theme_158": "Caspar David Friedrich The Monk by the Sea Alte Nationalgalerie",
    "theme_159": "Ilya Repin Barge Haulers on the Volga Russian Museum",
    "theme_160": "Caspar David Friedrich Wanderer above the Sea of Fog Kunsthalle Hamburg",
    "theme_161": "Honore Daumier The Uprising Phillips Collection",
    "theme_162": "Francisco Goya The Third of May 1808 Prado",
    "theme_163": "Rembrandt The Anatomy Lesson of Dr Nicolaes Tulp Mauritshuis",
    "theme_164": "Pieter Bruegel the Elder The Blind Leading the Blind Capodimonte",
    "theme_165": "J.M.W. Turner The Slave Ship MFA Boston",
    "theme_166": "Jacques-Louis David The Death of Socrates MET",
    "theme_167": "Jan Matejko Stanczyk National Museum Warsaw",
    "theme_168": "Edvard Munch Evening on Karl Johan Street Bergen",
    "theme_169": "James Ensor Christ's Entry into Brussels Getty",
    "theme_170": "Caspar David Friedrich Two Men Contemplating the Moon MET",
    "theme_171": "Auguste Rodin The Thinker Rodin Museum",
    "theme_172": "William Blake The Ancient of Days British Museum",
    "theme_173": "Edouard Manet A Bar at the Folies-Bergere Courtauld",
    "theme_174": "Edvard Munch The Scream National Gallery Oslo",
    "theme_175": "Fernand Leger The City Philadelphia Museum of Art",
    "theme_176": "Hieronymus Bosch The Garden of Earthly Delights Prado",
    "theme_177": "Albrecht Durer Melencolia I engraving",
    "theme_178": "Caspar David Friedrich Tetschen Altar Cross in the Mountains",
    "theme_179": "Salvador Dali The Persistence of Memory MoMA",
    "theme_180": "Eugene Delacroix Liberty Leading the People Louvre",
    "theme_181": "Caravaggio The Incredulity of Saint Thomas Sanssouci",
    "theme_182": "William Hogarth The Rake's Progress Soane",
    "theme_183": "Diego Velazquez Las Meninas Prado",
    "theme_184": "John Everett Millais Ophelia Tate Britain",
    "theme_185": "Artemisia Gentileschi Judith Slaying Holofernes Uffizi",
    "theme_186": "Rembrandt Self-Portrait with Two Circles Kenwood",
    "theme_187": "Johannes Vermeer The Astronomer Louvre",
    "theme_188": "Rembrandt The Return of the Prodigal Son Hermitage",
    "theme_189": "Carl Spitzweg The Bookworm Neue Pinakothek",
    "theme_190": "Titian Venus with a Mirror National Gallery of Art",
    "theme_191": "Titian Sisyphus Prado",
    "theme_192": "Vincent van Gogh Prisoners' Round Pushkin",
    "theme_193": "Odilon Redon The Cyclops Kroller-Muller",
    "theme_194": "Caspar David Friedrich The Sea of Ice Kunsthalle Hamburg",
    "theme_195": "Claude Monet Impression Sunrise Marmottan",
    "theme_196": "Rembrandt Jeremiah Lamenting the Destruction of Jerusalem Rijksmuseum",
    "theme_197": "J.M.W. Turner Snow Storm Steam-Boat Tate",
    "theme_198": "Gustave Courbet The Wave Alte Nationalgalerie",
    "theme_199": "Francisco Goya The Colossus Prado",
    "theme_200": "Caspar David Friedrich The Stages of Life Museum der bildenden Kunste"
}

def main():
    print("=== PHÂN GIẢI & TẢI 50 BẢN SCAN BẢO TÀNG (THEME 151 - 200) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    resolved = {}
    if os.path.exists(RESOLVED_PATH):
        try:
            with open(RESOLVED_PATH, "r", encoding="utf-8") as f:
                resolved = json.load(f)
        except Exception:
            resolved = {}

    success_count = 0
    
    for tid, entry in manifest.items():
        theme_id = entry["theme_id"]
        artist = entry["artist"]
        art_title = entry["artwork_title"]
        query = CUSTOM_SEARCH_QUERIES.get(theme_id, f"{artist} {art_title}")
        
        raw_cache_file = os.path.join(CACHE_DIR, f"{theme_id}.jpg")
        
        # Nếu đã có file trong cache và kích thước > 50KB
        if os.path.exists(raw_cache_file) and os.path.getsize(raw_cache_file) > 50000 and theme_id in resolved:
            print(f"⏩ [{theme_id}] Đã có trong cache ({os.path.getsize(raw_cache_file)/1024:.0f} KB): {resolved[theme_id]['title'][:40]}")
            success_count += 1
            continue

        print(f"\n🔍 [{theme_id}] Đang tìm kiếm: '{query}'...")
        
        # Thử tìm kiếm tối đa 3 lần
        found_url = None
        chosen_title = None
        
        for attempt in range(1, 4):
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
                    
                    if not file_titles:
                        # Fallback query đơn giản hơn
                        fallback_query = f"{artist} {art_title}"
                        search_url_fb = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(fallback_query) + "&srnamespace=6&format=json&srlimit=5"
                        req_fb = urllib.request.Request(search_url_fb, headers={"User-Agent": USER_AGENT})
                        with urllib.request.urlopen(req_fb, timeout=12) as resp_fb:
                            data_fb = json.loads(resp_fb.read().decode())
                            file_titles = [
                                it["title"] for it in data_fb.get("query", {}).get("search", []) 
                                if it["title"].startswith("File:") 
                                and not it["title"].lower().endswith((".svg", ".pdf", ".tif", ".ogg", ".webm"))
                            ]

                    if file_titles:
                        chosen_title = file_titles[0]
                        # Truy vấn link tải phân giải cao (width 2560px)
                        info_url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote(chosen_title) + "&prop=imageinfo&iiprop=url&iiurlwidth=2560"
                        info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
                        with urllib.request.urlopen(info_req, timeout=12) as info_resp:
                            info_data = json.loads(info_resp.read().decode())
                            pages = info_data.get("query", {}).get("pages", {})
                            page = list(pages.values())[0]
                            img_info = page.get("imageinfo", [{}])[0]
                            found_url = img_info.get("thumburl") or img_info.get("url")
                            break
            except Exception as e:
                print(f"  ⚠️ Lỗi tìm kiếm lượt {attempt}: {e}")
                time.sleep(2 * attempt)
                
            time.sleep(0.5)

        if found_url and chosen_title:
            print(f"  ✅ Tìm thấy: {chosen_title[:50]}...")
            print(f"  ⬇️ Đang tải về cache: {found_url[:70]}...")
            
            # Tải tệp về cache
            downloaded = False
            for dl_attempt in range(1, 4):
                try:
                    dl_req = urllib.request.Request(found_url, headers={"User-Agent": USER_AGENT})
                    with urllib.request.urlopen(dl_req, timeout=25) as dl_resp:
                        img_data = dl_resp.read()
                        with open(raw_cache_file, "wb") as f_out:
                            f_out.write(img_data)
                    print(f"  ✨ Đã lưu ({len(img_data)/1024:.0f} KB) vào: {raw_cache_file}")
                    downloaded = True
                    break
                except Exception as e:
                    print(f"  ⚠️ Lỗi tải ảnh lượt {dl_attempt}: {e}")
                    time.sleep(3 * dl_attempt)

            if downloaded:
                resolved[theme_id] = {
                    "theme_id": theme_id,
                    "title": chosen_title,
                    "url": found_url,
                    "query": query,
                    "artist": artist,
                    "artwork_title": art_title,
                    "cache_file": raw_cache_file
                }
                success_count += 1
                with open(RESOLVED_PATH, "w", encoding="utf-8") as f_res:
                    json.dump(resolved, f_res, ensure_ascii=False, indent=2)
        else:
            print(f"  ❌ Không tìm thấy bản scan phù hợp cho {theme_id} ({query})")

        time.sleep(0.5)

    print(f"\n====================================================")
    print(f"🎉 TỔNG KẾT PHÂN GIẢI: {success_count} / {len(manifest)} TÁC PHẨM THÀNH CÔNG!")
    print(f"====================================================")

if __name__ == "__main__":
    main()
