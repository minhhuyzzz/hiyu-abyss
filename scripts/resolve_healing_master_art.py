#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Resolve and Download 103 Healing Masterpieces (Theme 251 - 300)
Truy vấn Wikimedia Commons API, phân giải bản scan bảo tàng độ phân giải cao (2560px - 4000px)
cho từng slide độc lập và tải về lưu vào assets/templates/raw_cache/theme_{stt}_slide_{idx}.jpg.
"""

import urllib.request
import urllib.parse
import json
import time
import os
import sys

# Ensure immediate flush for logging
sys.stdout.reconfigure(line_buffering=True)

MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"
RESOLVED_PATH = "scripts/resolved_healing_art.json"
CACHE_DIR = "assets/templates/raw_cache"

USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

os.makedirs(CACHE_DIR, exist_ok=True)

# Tinh chỉnh từ khóa tìm kiếm Wikimedia cho các tác phẩm đặc biệt
CUSTOM_SLIDE_QUERIES = {
    "theme_251_slide_1": "Caspar David Friedrich Woman at a Window Alte Nationalgalerie",
    "theme_251_slide_2": "Claude Monet Morning on the Seine Clear Weather",
    "theme_251_slide_3": "Pierre-Auguste Renoir Woman with a Parasol in a Garden",
    "theme_252_slide_1": "Vilhelm Hammershoi Interior with a Woman Reading",
    "theme_252_slide_2": "John Singer Sargent Carnation Lily Lily Rose Tate",
    "theme_253_slide_1": "Claude Monet Water Lilies Clouds",
    "theme_254_slide_1": "Camille Pissarro The Garden of the Tuileries on a Winter Morning",
    "theme_254_slide_2": "Claude Monet Path through the Corn at Pourville",
    "theme_254_slide_3": "Jean-Baptiste-Camille Corot Souvenir de Mortefontaine Louvre",
    "theme_255_slide_1": "Berthe Morisot The Cradle Musee d'Orsay",
    "theme_255_slide_2": "Mary Cassatt Mother and Child",
    "theme_256_slide_1": "Caspar David Friedrich The Morning Star",
    "theme_257_slide_1": "Thomas Cole The Arcadian State New-York Historical Society",
    "theme_257_slide_2": "Asher Brown Durand Kindred Spirits Crystal Bridges",
    "theme_258_slide_1": "Carl Larsson Breakfast Under the Big Birch",
    "theme_258_slide_2": "Joaquin Sorolla Sunlight in the Garden",
    "theme_258_slide_3": "Claude Monet The Water-Lily Pond 1899",
    "theme_259_slide_1": "John Frederick Kensett Lake George MET",
    "theme_260_slide_1": "Sanford Robinson Gifford A Gorge in the Mountains",
    "theme_260_slide_2": "Jean-Baptiste-Camille Corot A Morning Dance of the Nymphs",
    "theme_261_slide_1": "Camille Pissarro Landscape at Valhermeil",
    "theme_261_slide_2": "Pierre-Auguste Renoir Springtime Landscape",
    "theme_261_slide_3": "Claude Monet Field of Poppies near Giverny",
    "theme_262_slide_1": "Albert Bierstadt Sunlight and Shadow",
    "theme_263_slide_1": "Henri Le Sidaner The Table by the Window",
    "theme_263_slide_2": "Pierre-Auguste Renoir The Reader La Liseuse",
    "theme_264_slide_1": "Caspar David Friedrich Wanderer above the Sea of Fog",
    "theme_264_slide_2": "Thomas Cole Morning over the Kaaterskill Clove",
    "theme_264_slide_3": "Claude Monet Cliffs at Pourville in the Fog",
    "theme_265_slide_1": "J.M.W. Turner Sun Rising through Vapour National Gallery",
    "theme_265_slide_2": "Caspar David Friedrich The Solitary Tree",
    "theme_266_slide_1": "George Inness The Home of the Heron Art Institute Chicago",
    "theme_267_slide_1": "J.M.W. Turner The Fighting Temeraire National Gallery",
    "theme_267_slide_2": "Frederic Edwin Church Twilight in the Wilderness Cleveland",
    "theme_267_slide_3": "Claude Monet Haystacks Sunset",
    "theme_268_slide_1": "John Singer Sargent The Fountain Villa Torlonia Frascati",
    "theme_268_slide_2": "Thomas Cole Home in the Woods",
    "theme_269_slide_1": "Caspar David Friedrich Giant Mountains",
    "theme_270_slide_1": "Vilhelm Hammershoi Sunshine in the Drawing Room",
    "theme_270_slide_2": "Carl Larsson Flowers on the Windowsill",
    "theme_270_slide_3": "Albert Bierstadt Looking Down Yosemite Valley",
    "theme_271_slide_1": "Claude Monet Grainstacks at the End of Summer",
    "theme_271_slide_2": "Camille Pissarro Sunset at Saint-Charles Eragny",
    "theme_272_slide_1": "John Frederick Kensett Sunset on the Sea",
    "theme_273_slide_1": "John Singer Sargent A Gust of Wind",
    "theme_273_slide_2": "Caspar David Friedrich Morning in the Mountains",
    "theme_274_slide_1": "Jean-Baptiste-Camille Corot The Lake at Ville-d'Avray",
    "theme_274_slide_2": "Claude Monet The Artist's Garden at Giverny",
    "theme_274_slide_3": "George Inness Peace and Plenty MET",
    "theme_275_slide_1": "Albert Bierstadt Among the Sierra Nevada Mountains",
    "theme_276_slide_1": "Mary Cassatt The Tea MFA Boston",
    "theme_276_slide_2": "John Singer Sargent A Dinner Table at Night",
    "theme_276_slide_3": "Camille Pissarro The Garden at Eragny",
    "theme_277_slide_1": "Vilhelm Hammershoi Interior Ray of Sunlight",
    "theme_277_slide_2": "Carl Larsson Quiet Afternoon",
    "theme_278_slide_1": "Berthe Morisot Reading in the Garden",
    "theme_279_slide_1": "Pierre-Auguste Renoir The Luncheon of the Boating Party",
    "theme_279_slide_2": "Joaquin Sorolla Walk on the Beach",
    "theme_279_slide_3": "Claude Monet The Garden of Monet at Argenteuil",
    "theme_280_slide_1": "Mary Cassatt Young Woman in a Green Outdoor Vest",
    "theme_280_slide_2": "Henri Le Sidaner The White Tablecloth",
    "theme_281_slide_1": "Carl Larsson The Sun Bath",
    "theme_282_slide_1": "John Singer Sargent Monet Painting by the Edge of a Wood Tate",
    "theme_282_slide_2": "Claude Monet Camille Monet in the Garden at Argenteuil",
    "theme_282_slide_3": "Frederic Edwin Church The Heart of the Andes MET",
    "theme_283_slide_1": "Joaquin Sorolla Valencia Fishermen",
    "theme_283_slide_2": "Pierre-Auguste Renoir A Bouquet of Roses",
    "theme_284_slide_1": "Jean-Baptiste-Camille Corot Morning with Nymphs",
    "theme_285_slide_1": "John Singer Sargent Morning Walk",
    "theme_285_slide_2": "Camille Pissarro Morning Sunlight Eragny",
    "theme_285_slide_3": "Mary Cassatt Breakfast in Bed",
    "theme_286_slide_1": "Pierre-Auguste Renoir The Skiff La Yole",
    "theme_286_slide_2": "Claude Monet Antibes Seen from the Salis Gardens",
    "theme_287_slide_1": "Carl Larsson Around the Lamp",
    "theme_288_slide_1": "Henri Le Sidaner Evening Light in the Courtyard",
    "theme_288_slide_2": "John Singer Sargent Dolce Far Niente",
    "theme_288_slide_3": "Joaquin Sorolla The Bathing Hour",
    "theme_289_slide_1": "Caspar David Friedrich Sunrise over Mountains landscape",
    "theme_289_slide_2": "Caspar David Friedrich The Cross in the Mountains Tetschen",
    "theme_289_slide_3": "Albert Bierstadt A Storm in the Rocky Mountains Mount Rosalie",
    "theme_290_slide_1": "Kintsugi bowl tea ceremony Japanese art",
    "theme_290_slide_2": "Frederic Edwin Church Twilight in the Wilderness",
    "theme_291_slide_1": "J.M.W. Turner Norham Castle Sunrise Tate",
    "theme_292_slide_1": "Claude Monet Poplars on the Epte",
    "theme_292_slide_2": "Thomas Cole The Oxbow MET",
    "theme_292_slide_3": "George Inness Peace and Plenty",
    "theme_293_slide_1": "Sunlight window stone interior painting Vermeer Hammershoi",
    "theme_293_slide_2": "Frederic Edwin Church Aurora Borealis Smithsonian",
    "theme_294_slide_1": "J.M.W. Turner Light and Colour Goethe's Theory Tate",
    "theme_295_slide_1": "Claude Monet The Cliff at Etretat Sunset",
    "theme_295_slide_2": "Albert Bierstadt Emerald Pool",
    "theme_296_slide_1": "Camille Pissarro The Garden of the Tuileries on a Winter Morning",
    "theme_296_slide_2": "Claude Monet Lavacourt under Snow",
    "theme_296_slide_3": "Pierre-Auguste Renoir Bal du moulin de la Galette",
    "theme_297_slide_1": "Frederic Edwin Church Cotopaxi Detroit Institute of Arts",
    "theme_298_slide_1": "Claude Monet San Giorgio Maggiore at Dusk",
    "theme_298_slide_2": "Albert Bierstadt Rainbow in the Sierra Nevada",
    "theme_299_slide_1": "Open birdcage window sunlight oil painting",
    "theme_299_slide_2": "Jean-Baptiste-Camille Corot The Bridge at Narni",
    "theme_299_slide_3": "J.M.W. Turner The Morning after the Deluge Tate",
    "theme_300_slide_1": "Caspar David Friedrich Mountain Landscape with Rainbow",
    "theme_300_slide_2": "Claude Monet Water Lilies 1916",
    "theme_300_slide_3": "Albert Bierstadt Sierra Nevada Sunrise landscape"
}

def search_wikimedia(query):
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
        except Exception as e:
            time.sleep(1.5 * attempt)
        time.sleep(0.5)
    return None, None

def download_image(url, save_path):
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = resp.read()
                with open(save_path, "wb") as f:
                    f.write(data)
                return True
        except Exception as e:
            time.sleep(2.0 * attempt)
    return False

def main():
    print("=== PHÂN GIẢI & TẢI 103 BẢN SCAN BẢO TÀNG (THEME 251 - 300) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    resolved = {}
    if os.path.exists(RESOLVED_PATH):
        try:
            with open(RESOLVED_PATH, "r", encoding="utf-8") as f:
                resolved = json.load(f)
        except Exception:
            resolved = {}

    total_tasks = sum(len(t["slides"]) for t in manifest.values())
    current_idx = 0
    success_count = 0

    for tid, t in manifest.items():
        stt = t["stt"]
        theme_id = t["theme_id"]
        slides = t["slides"]
        
        for s in slides:
            current_idx += 1
            s_idx = s["slide_index"]
            slide_key = f"{theme_id}_slide_{s_idx}"
            artist = s["artist"]
            artwork = s["artwork_title"]
            
            raw_cache_file = os.path.join(CACHE_DIR, f"{slide_key}.jpg")
            
            # Check existing cache
            if os.path.exists(raw_cache_file) and os.path.getsize(raw_cache_file) > 40000 and slide_key in resolved:
                print(f"⏩ [{current_idx}/{total_tasks}] {slide_key} đã có trong cache ({os.path.getsize(raw_cache_file)/1024:.0f} KB)")
                success_count += 1
                continue

            query = CUSTOM_SLIDE_QUERIES.get(slide_key, f"{artist} {artwork}")
            print(f"\n🔍 [{current_idx}/{total_tasks}] Đang tìm {slide_key}: '{query}'...")
            
            title, url = search_wikimedia(query)
            if not url:
                # Fallback to artist and artwork
                fb_query = f"{artist} {artwork}"
                title, url = search_wikimedia(fb_query)

            if title and url:
                print(f"  ✅ Tìm thấy: {title[:45]}...")
                print(f"  ⬇️ Đang tải về ({url[:65]}...)...")
                ok = download_image(url, raw_cache_file)
                if ok:
                    sz_kb = os.path.getsize(raw_cache_file) / 1024
                    print(f"  ✨ Đã lưu thành công ({sz_kb:.0f} KB) vào: {raw_cache_file}")
                    resolved[slide_key] = {
                        "slide_key": slide_key,
                        "theme_id": theme_id,
                        "slide_index": s_idx,
                        "artist": artist,
                        "artwork_title": artwork,
                        "wikimedia_title": title,
                        "url": url,
                        "cache_file": raw_cache_file
                    }
                    success_count += 1
                    with open(RESOLVED_PATH, "w", encoding="utf-8") as f_res:
                        json.dump(resolved, f_res, ensure_ascii=False, indent=2)
                else:
                    print(f"  ❌ Lỗi tải file: {url}")
            else:
                print(f"  ❌ Không tìm thấy bản scan trên Wikimedia: {query}")

            # Throttling to respect Wikimedia guidelines
            time.sleep(1.2)

    print("\n====================================================")
    print(f"🎉 TỔNG KẾT PHÂN GIẢI: {success_count} / {total_tasks} SLIDES THÀNH CÔNG!")
    print("====================================================")

if __name__ == '__main__':
    main()
