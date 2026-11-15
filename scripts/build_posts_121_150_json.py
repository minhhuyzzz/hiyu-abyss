# scripts/build_posts_121_150_json.py
import csv
import json

with open("scripts/tiktok_150_posts.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

posts_121_150 = []
for r in rows:
    stt = int(r["STT"])
    if 121 <= stt <= 150:
        posts_121_150.append({
            "stt": stt,
            "id": r["Mã ID"].strip(),
            "title": r["Tiêu Đề (Dưới 90 từ)"].strip(),
            "caption": r["Mô Tả (Caption TikTok)"].strip(),
            "author": r["Nguồn Tác Giả"].strip(),
            "hashtags": r["Hashtags (5 cái)"].strip(),
            "format": r["Định Dạng Slide"].strip(),
            "slide_1": r["Trang 1 (Hook / Mở màn)"].strip(),
            "slide_2": r["Trang 2 (Cú lật bóc trần)"].strip(),
            "slide_3": r["Trang 3 (Chiếc gương phản tư)"].strip(),
            "slide_4": r.get("Trang 4 (Đúc kết / Phản tư sâu)", "-").strip(),
            "full_quote": r["Văn Bản Hoàn Chỉnh"].strip(),
            "theme": r["Chủ Đề Hạt Nhân"].strip(),
            "theme_key": f"theme_{stt:02d}"
        })

with open("scripts/posts_121_150_data.json", "w", encoding="utf-8") as f:
    json.dump(posts_121_150, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(posts_121_150)} posts to scripts/posts_121_150_data.json!")
