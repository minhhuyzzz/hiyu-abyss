import json

with open('scripts/posts_251_300.json', encoding='utf-8') as f:
    posts = json.load(f)

for p in posts:
    stt = p['stt']
    fmt = p['format']
    h = p['hook'][:30] if p['hook'] != '-' else '-'
    t = p['twist'][:30] if p['twist'] != '-' else '-'
    m = p['mirror'][:30] if p['mirror'] != '-' else '-'
    d = p['deep'][:30] if p['deep'] != '-' else '-'
    print(f"STT {stt}: {fmt} | H: {h} | T: {t} | M: {m}")
