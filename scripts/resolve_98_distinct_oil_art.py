import urllib.request
import urllib.parse
import json
import time
import os

USER_AGENT = "HiyuAbyssResearchBot/2.0 (https://hiyuabyss.local; contact: research@hiyuabyss.org)"

def resolve_artworks():
    with open('scripts/curated_98_distinct_oil_art.json', 'r', encoding='utf-8') as f:
        curated_list = json.load(f)

    json_out_path = 'scripts/resolved_98_distinct_oil_art.json'
    if os.path.exists(json_out_path):
        with open(json_out_path, 'r', encoding='utf-8') as f:
            resolved = json.load(f)
    else:
        resolved = {}

    print(f"Total curated slides: {len(curated_list)} | Already resolved: {len(resolved)}")

    for item in curated_list:
        theme_id = item['theme_id']
        slide_idx = item['slide']
        key = f"{theme_id}_slide_{slide_idx}"
        q = item['query']

        if key in resolved and resolved[key].get('url'):
            print(f"⏩ {key} already resolved: {resolved[key].get('title', '')[:35]}...")
            continue

        # Retry search up to 3 times
        success = False
        for attempt in range(1, 4):
            url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&format=json&srlimit=5"
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=12) as resp:
                    data = json.loads(resp.read().decode())
                    items = data.get("query", {}).get("search", [])
                    file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not any(it["title"].lower().endswith(ext) for ext in [".svg", ".pdf", ".tif", ".webm", ".ogg"])]
                    if file_titles:
                        chosen_title = file_titles[0]
                        # Fetch direct image URL
                        info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(chosen_title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
                        info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
                        with urllib.request.urlopen(info_req, timeout=12) as info_resp:
                            info_data = json.loads(info_resp.read().decode())
                            pages = info_data.get("query", {}).get("pages", {})
                            page = list(pages.values())[0]
                            img_info = page.get("imageinfo", [{}])[0]
                            dl_url = img_info.get("thumburl") or img_info.get("url")
                            resolved[key] = {
                                "theme_id": theme_id,
                                "slide": slide_idx,
                                "role": item['role'],
                                "title": chosen_title,
                                "url": dl_url,
                                "query": q,
                                "artwork_name": item['artwork'],
                                "justification": item['justification']
                            }
                            print(f"✅ [{len(resolved)}/98] {key} -> {chosen_title[:45]}...")
                            success = True
                            with open(json_out_path, 'w', encoding='utf-8') as out:
                                json.dump(resolved, out, ensure_ascii=False, indent=2)
                            break
                    else:
                        print(f"⚠️ {key}: No file found for '{q}'")
                        break
            except Exception as e:
                print(f"❌ {key} (Attempt {attempt}): {e}")
                time.sleep(2 * attempt)
            time.sleep(0.3)
        time.sleep(0.3)

    print(f"\n🎉 Finished resolution: {len(resolved)} / {len(curated_list)} slides resolved!")

if __name__ == '__main__':
    resolve_artworks()
