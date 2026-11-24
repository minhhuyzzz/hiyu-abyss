import json

with open('website/src/data/asset-catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

pairs = [
    (330, 1, 490, 1),
    (409, 1, 431, 1),
    (100, 2, 321, 3),
    (100, 3, 451, 1),
    (102, 2, 398, 2),
    (106, 1, 439, 1),
    (107, 2, 350, 1),
    (107, 3, 500, 4),
    (110, 2, 211, 1),
    (211, 1, 392, 1)
]

for t1, s1, t2, s2 in pairs:
    c1 = catalog.get(str(t1), {}).get("slides", [])
    c2 = catalog.get(str(t2), {}).get("slides", [])
    m1 = c1[s1-1] if len(c1) >= s1 else {}
    m2 = c2[s2-1] if len(c2) >= s2 else {}
    print(f"Theme {t1} s{s1}: {m1.get('artwork_title')} by {m1.get('artist')}")
    print(f"Theme {t2} s{s2}: {m2.get('artwork_title')} by {m2.get('artist')}")
    print("-" * 50)
