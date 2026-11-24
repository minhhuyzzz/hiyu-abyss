import json

files = ['scripts/posts_301_350.json', 'scripts/posts_351_400.json', 'scripts/posts_401_450.json', 'scripts/posts_451_500.json']
posts = []
for f in files:
    with open(f, encoding='utf-8') as fp:
        posts.extend(json.load(fp))

print(f'Total posts: {len(posts)}')
sample_indices = [0, 10, 50, 75, 100, 125, 150, 175, 199]
for idx in sample_indices:
    p = posts[idx]
    print(f"\n--- STT {p['stt']} ({p['id']}) | Format: {p['format']} | Author: {p['author']} ---")
    print(f"Concept: {p.get('concept')}")
