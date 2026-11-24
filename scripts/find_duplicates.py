import json

with open('scripts/oil_suites_301_500_manifest.json', encoding='utf-8') as f:
    manifest = json.load(f)

seen = {}
for tid, t in manifest.items():
    stt = t['stt']
    for s in t['slides']:
        p = s['prompt']
        s_idx = s['slide_index']
        if p in seen:
            prev_stt, prev_idx = seen[p]
            print(f"Duplicate found: STT {stt} slide {s_idx} matches STT {prev_stt} slide {prev_idx}!")
            print(f"  Metaphor: {s['visual_metaphor']}")
        else:
            seen[p] = (stt, s_idx)
