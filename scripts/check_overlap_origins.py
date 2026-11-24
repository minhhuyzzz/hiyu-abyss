import json

with open('scripts/catalog_duplicates_1_to_300.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

clusters = d['cross_theme_clusters']
print(f"Total cross-theme duplicate clusters in 1-300: {len(clusters)}")

for idx, c in enumerate(clusters[:20]):
    t1_100 = [s for s in c['slides'] if s['stt'] <= 100]
    t101_300 = [s for s in c['slides'] if 101 <= s['stt'] <= 300]
    print(f"Cluster #{idx+1} (Themes: {c['themes']}): in 1-100: {[s['stt'] for s in t1_100]} | in 101-300: {[s['stt'] for s in t101_300]}")
