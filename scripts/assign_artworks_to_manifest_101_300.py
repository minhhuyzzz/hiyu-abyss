import json
import os

def main():
    with open('scripts/themes_101_300_structure.json', 'r', encoding='utf-8') as f:
        themes = json.load(f)
        
    with open('scripts/master_artworks_pool.json', 'r', encoding='utf-8') as f:
        pool = json.load(f)
        
    print(f"Themes to assign: {len(themes)}")
    print(f"Available artworks in pool: {len(pool)}")
    
    # Check 301-500 queries to ensure zero overlap
    used_301_500_queries = set()
    if os.path.exists("scripts/oil_suites_301_500_manifest.json"):
        with open("scripts/oil_suites_301_500_manifest.json", "r", encoding="utf-8") as f:
            m = json.load(f)
        for t in m.values():
            for s in t.get("slides", []):
                q = s.get("search_query", "")
                if q:
                    used_301_500_queries.add(q.lower().strip())
                    
    # Filter pool to ensure no overlap with 301-500
    clean_pool = [art for art in pool if art["query"].lower().strip() not in used_301_500_queries]
    print(f"Clean pool after 301-500 exclusions: {len(clean_pool)}")
    
    # We will build manifest_101_300
    manifest = {}
    pool_idx = 0
    total_assigned_slides = 0
    
    for theme_data in themes:
        stt = theme_data["stt"]
        theme_id = f"THEME_{stt}"
        slide_ids = theme_data["slide_ids"]
        author = theme_data.get("author", "")
        title = theme_data.get("title", "")
        topic = theme_data.get("topic", "")
        
        theme_slides = []
        for s_idx, s_id in enumerate(slide_ids):
            if pool_idx >= len(clean_pool):
                raise ValueError("Ran out of artworks in clean pool!")
                
            art = clean_pool[pool_idx]
            pool_idx += 1
            total_assigned_slides += 1
            
            theme_slides.append({
                "slide_index": s_idx + 1,
                "slide_id": s_id,
                "artist": art["artist"],
                "artwork_title": art["title"],
                "museum": art["museum"],
                "year": art["year"],
                "search_query": art["query"],
                "raw_filename": f"raw_theme_{stt}_slide_{s_idx+1}.jpg"
            })
            
        manifest[theme_id] = {
            "stt": stt,
            "theme_id": theme_id,
            "title": title,
            "topic": topic,
            "author": author,
            "slide_count": len(slide_ids),
            "slides": theme_slides
        }
        
    print(f"Successfully assigned {total_assigned_slides} slides across {len(manifest)} themes.")
    
    # Verify uniqueness of queries
    all_assigned_queries = [s["search_query"].lower().strip() for t in manifest.values() for s in t["slides"]]
    assert len(all_assigned_queries) == len(set(all_assigned_queries)), "DUPLICATE QUERY DETECTED IN ASSIGNMENT!"
    print("Verification PASSED: 100% of queries in manifest are distinct!")
    
    with open("scripts/oil_suites_101_300_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    print("Saved scripts/oil_suites_101_300_manifest.json")

if __name__ == "__main__":
    main()
