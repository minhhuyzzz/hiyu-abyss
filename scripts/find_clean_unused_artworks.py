import json

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog_blob = f.read().lower()

with open('scripts/final_verified_artworks.json', 'r', encoding='utf-8') as f:
    pool_final = json.load(f)

with open('scripts/verified_artworks_download_list.json', 'r', encoding='utf-8') as f:
    pool_prev = json.load(f)

combined = pool_final + pool_prev
unused_artworks = []
seen = set()

for art in combined:
    t = art['title'].lower()
    if t not in seen and t not in catalog_blob:
        seen.add(t)
        unused_artworks.append(art)

print(f"Total artworks never used in catalog: {len(unused_artworks)}")
for i, u in enumerate(unused_artworks[:20]):
    print(f"{i+1}: {u['title']} by {u['artist']} ({u['size_kb']} KB)")
