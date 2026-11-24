import json
import os
import glob

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

print(f"Total entries in catalog: {len(catalog)}")

# Look at theme keys
keys = list(catalog.keys())
print("First 10 keys:", keys[:10])
print("Keys around 100:", keys[95:105])
print("Keys around 300:", keys[295:305])

# Check how slides are structured in theme_01 vs theme_101 vs theme_251
print("\ntheme_01 slides:", catalog.get('theme_01', {}).get('slides'))
print("\ntheme_101 slides:", catalog.get('theme_101', {}).get('slides'))
print("\ntheme_251 slides:", catalog.get('theme_251', {}).get('slides'))
