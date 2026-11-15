import json

posts = json.load(open('scripts/posts_151_200_slides_detail.json', encoding='utf-8'))

for p in posts:
    print(f"\n=== {p['stt']}. {p['title']} ({p['format']}) ===")
    for s in p['slides']:
        print(f"  [Slide {s['index']} - {s['role']}]: {s['text']}")
