#!/usr/bin/env python3
# scripts/resolve_missing_3_slides.py
import urllib.request
import urllib.parse
import json

MISSING = [
    ("theme_143_slide_1", "File:Den Haag - Mauritshuis - Pieter Claesz (1597-1660) - Vanitas Still Life 1630.jpg", "Pieter Claesz Vanitas 1630"),
    ("theme_146_slide_1", "File:Carl Spitzweg - Der arme Poet (Neue Pinakothek).jpg", "Carl Spitzweg Der arme Poet"),
    ("theme_149_slide_1", "File:Rembrandt Harmensz. van Rijn - Jeremia treurend over de verwoesting van Jeruzalem - Google Art Project.jpg", "Rembrandt Jeremiah Lamenting")
]

with open("scripts/resolved_47_distinct_oil_art.json", "r", encoding="utf-8") as f:
    resolved = json.load(f)

USER_AGENT = "HiyuAbyssResearchBot/2.0 (https://hiyuabyss.local; contact: research@hiyuabyss.org)"

for key, title, query in MISSING:
    info_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&iiurlwidth=1920"
    req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get("query", {}).get("pages", {})
            page = list(pages.values())[0]
            img_info = page.get("imageinfo", [{}])[0]
            dl_url = img_info.get("thumburl") or img_info.get("url")
            resolved[key] = {
                "title": title,
                "url": dl_url,
                "query": query
            }
            print(f"✅ {key} -> {title[:50]}...")
    except Exception as e:
        print(f"❌ {key} Error: {e}")

with open("scripts/resolved_47_distinct_oil_art.json", "w", encoding="utf-8") as f:
    json.dump(resolved, f, ensure_ascii=False, indent=2)

print(f"\nFinal total resolved slides: {len(resolved)} / 47!")
