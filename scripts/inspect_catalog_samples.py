import json

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for i in [101, 102, 110, 128, 151, 201, 250, 251, 299, 300]:
    t = d.get(f"theme_{i}", {})
    title = t.get("title", "")[:60]
    artist = t.get("artist", "")
    slides = t.get("slides", {})
    print(f"Theme {i}:")
    print(f"  Title: {title}")
    print(f"  Artist: {artist}")
    print(f"  Slides: {slides}")
