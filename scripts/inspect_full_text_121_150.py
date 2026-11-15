# scripts/inspect_full_text_121_150.py
import json

posts = json.load(open("scripts/posts_121_150_data.json", encoding="utf-8"))
for p in posts:
    print(f"[{p['stt']}] {p['id']} - {p['format']} | Tác giả: {p['author']} | Chủ đề: {p['theme']}")
    print(f"   Trang 1: {p['slide_1']}")
    if p['slide_2'] != "-":
        print(f"   Trang 2: {p['slide_2']}")
    if p['slide_3'] != "-":
        print(f"   Trang 3: {p['slide_3']}")
    print(f"   Văn bản: {p['full_quote']}\n")
