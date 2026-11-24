import json
import os

def main():
    with open('scripts/themes_101_300_structure.json', 'r', encoding='utf-8') as f:
        themes = json.load(f)
        
    print(f"Loaded {len(themes)} themes from structure.")
    
    # Load 301-500 queries to avoid collision
    used_301_500_queries = set()
    if os.path.exists("scripts/oil_suites_301_500_manifest.json"):
        with open("scripts/oil_suites_301_500_manifest.json", "r", encoding="utf-8") as f:
            m = json.load(f)
        for t in m.values():
            for s in t.get("slides", []):
                q = s.get("search_query", "")
                if q:
                    used_301_500_queries.add(q.lower())
                    
    print(f"Reserved 301-500 queries: {len(used_301_500_queries)}")
    
    # We will curate 477 unique masterworks
    # Let's generate a structured dictionary with themes 101 to 300
    # Each theme gets its slide entries with artist, artwork_title, museum, year, search_query
    
    # Let's create an external curated database script that provides 500 distinct masterworks
    print("Ready to generate manifest.")

if __name__ == "__main__":
    main()
