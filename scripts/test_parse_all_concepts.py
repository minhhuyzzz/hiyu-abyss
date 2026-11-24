import json
import re

files = ['scripts/posts_301_350.json', 'scripts/posts_351_400.json', 'scripts/posts_401_450.json', 'scripts/posts_451_500.json']
posts = []
for f in files:
    with open(f, encoding='utf-8') as fp:
        posts.extend(json.load(fp))

print(f"Total posts: {len(posts)}")

failed = 0
parsed_slides_total = 0

for p in posts:
    stt = p['stt']
    fmt = p['format']
    concept = p.get('concept', '')
    
    expected_slides = 1
    if "2 trang" in fmt:
        expected_slides = 2
    elif "3 trang" in fmt:
        expected_slides = 3
    elif "4 trang" in fmt:
        expected_slides = 4
    elif "1 trang" in fmt or "Single-Punch" in fmt:
        expected_slides = 1
        
    slides = []
    if expected_slides == 1:
        # e.g., "1 tranh sơn dầu: Rembrandt van Rijn - Người lữ hành..."
        c_clean = re.sub(r'^(Bộ\s+\d+\s+tranh\s+sơn\s+dầu:?|1\s+tranh\s+sơn\s+dầu:?)\s*', '', concept, flags=re.IGNORECASE).strip()
        parts = c_clean.split(' - ', 1)
        artist = parts[0].strip() if len(parts) > 1 else "Classical Master"
        desc = parts[1].strip() if len(parts) > 1 else c_clean
        slides.append({"slide_num": 1, "artist": artist, "desc": desc})
    else:
        # Multiple slides: split by " | "
        raw_parts = [part.strip() for part in concept.split('|') if part.strip()]
        for i, raw_s in enumerate(raw_parts, start=1):
            s_clean = re.sub(r'^(Bộ\s+\d+\s+tranh\s+sơn\s+dầu:?|Slide\s+\d+:?)\s*', '', raw_s, flags=re.IGNORECASE).strip()
            parts = s_clean.split(' - ', 1)
            artist = parts[0].strip() if len(parts) > 1 else "Classical Master"
            desc = parts[1].strip() if len(parts) > 1 else s_clean
            slides.append({"slide_num": i, "artist": artist, "desc": desc})
            
    if len(slides) != expected_slides:
        print(f"Mismatch STT {stt} ({p['id']}): expected {expected_slides}, got {len(slides)}! Raw: {concept}")
        failed += 1
    else:
        parsed_slides_total += len(slides)

print(f"\nResult: {parsed_slides_total} slides parsed across {len(posts)} posts. Failures: {failed}")
