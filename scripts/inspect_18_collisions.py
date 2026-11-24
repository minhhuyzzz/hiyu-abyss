import json

with open('scripts/catalog_duplicates_1_to_300.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

collisions = d['collision_with_301_500']
t1_100_collisions = [c for c in collisions if c['slide_1_300']['theme'] <= 100]

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

print(f"Total 1-100 vs 301-500 collisions: {len(t1_100_collisions)}")
for c in t1_100_collisions:
    t_old = c['slide_1_300']['theme']
    t_new = c['slide_301_500']['theme']
    old_data = catalog.get(f"theme_{t_old:02d}") or catalog.get(f"theme_{t_old}")
    new_data = catalog.get(f"theme_{t_new}")
    print(f"Theme {t_old} ({old_data.get('artist')} - {old_data.get('title')[:30]})  <--->  Theme {t_new} ({new_data.get('artist')} - {new_data.get('title')[:30]})")
