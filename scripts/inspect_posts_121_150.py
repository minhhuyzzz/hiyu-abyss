# scripts/inspect_posts_121_150.py
import csv
import json

with open("scripts/tiktok_150_posts.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

posts = [r for r in rows if 121 <= int(r["STT"]) <= 150]

print(f"=== PHÂN TÍCH 30 BÀI ĐĂNG (STT 121 -> 150) ===")
print(f"Tổng số bài: {len(posts)}")

format_counts = {}
theme_counts = {}
total_slides = 0

for p in posts:
    fmt = p["Định Dạng Slide"].strip()
    theme = p["Chủ Đề Hạt Nhân"].strip()
    format_counts[fmt] = format_counts.get(fmt, 0) + 1
    theme_counts[theme] = theme_counts.get(theme, 0) + 1
    
    # Calculate slides
    if "Single-Punch" in fmt:
        s_count = 1
    elif "2 trang" in fmt:
        s_count = 2
    elif "3 trang" in fmt:
        s_count = 3
    elif "4 trang" in fmt:
        s_count = 4
    else:
        s_count = 1
    total_slides += s_count
    
    print(f"STT {p['STT']:<3} | {p['Mã ID']} | {fmt:<16} | Slide count: {s_count} | {theme:<35} | {p['Nguồn Tác Giả']}")

print("\n--- TỔNG KẾT ĐỊNH DẠNG ---")
for fmt, cnt in format_counts.items():
    print(f"- {fmt}: {cnt} bài")
print(f"👉 TỔNG SỐ SLIDE CẦN CHẾ TÁC: {total_slides} slides độc bản")

print("\n--- PHÂN BỔ CHỦ ĐỀ HẠT NHÂN ---")
for thm, cnt in theme_counts.items():
    print(f"- {thm}: {cnt} bài")
