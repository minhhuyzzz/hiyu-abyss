import json

with open('scripts/catalog_duplicates_1_to_300.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Find all slides in 101-300 that duplicate with:
# 1) Themes 1-100
# 2) Other themes in 101-300
# 3) Themes in 301-500

dup_slides_101_300 = set()

# From cross_theme_clusters:
for c in d['cross_theme_clusters']:
    # All slides in 101-300 in this cluster
    slides_in_101_300 = [s for s in c['slides'] if 101 <= s['stt'] <= 300]
    # Check if there is an earlier owner (stt <= 100, or lowest stt)
    has_owner_in_1_100 = any(s['stt'] <= 100 for s in c['slides'])
    
    if has_owner_in_1_100:
        # ALL slides in 101-300 are copies of 1-100!
        for s in slides_in_101_300:
            dup_slides_101_300.add((s['stt'], s['slide_id'], s['url']))
    else:
        # Lowest stt in 101-300 can keep it, all subsequent are copies
        sorted_s = sorted(slides_in_101_300, key=lambda x: (x['stt'], x['slide_id']))
        for s in sorted_s[1:]:
            dup_slides_101_300.add((s['stt'], s['slide_id'], s['url']))

# Also from collision_with_301_500:
for c in d['collision_with_301_500']:
    s = c['slide_1_300']
    if 101 <= s['theme'] <= 300:
        dup_slides_101_300.add((s['theme'], s['slide'], s['url']))

print(f"Total duplicate slides in 101-300 that need fresh replacement: {len(dup_slides_101_300)}")

# Which themes in 101-300 are affected?
affected_themes = sorted(list(set(s[0] for s in dup_slides_101_300)))
print(f"Total themes in 101-300 affected: {len(affected_themes)} / 200")
print("Sample affected themes:", affected_themes[:30])
