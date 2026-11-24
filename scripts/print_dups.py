import json

with open('scripts/visual_duplicates_list.json', 'r', encoding='utf-8') as f:
    dups = json.load(f)

print(f'Total duplicates: {len(dups)}')
for i, d in enumerate(dups[:20]):
    print(f"{i+1}: Theme {d['stt']} {d['slide_name']} (dup of Theme {d['dup_of_theme']} {d['dup_of_slide']})")
