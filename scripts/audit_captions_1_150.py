import csv
from collections import Counter
import difflib

CSV_PATH = "scripts/tiktok_200_posts.csv"

with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Tổng số hàng trong CSV: {len(rows)}")

posts_1_150 = rows[:150]

captions = [(r.get("STT"), r.get("Chủ Đề"), r.get("Mô Tả (Caption TikTok)", "").strip()) for r in posts_1_150]

# 1. Kiểm tra trùng khớp 100%
caption_texts = [c[2] for c in captions]
counts = Counter(caption_texts)
exact_dupes = {k: v for k, v in counts.items() if v > 1 and k != ""}

print(f"\n=== [1] KIỂM TRA TRÙNG NGUYÊN VĂN (EXACT DUPLICATES) ===")
print(f"Tổng số bài (1-150): {len(captions)}")
print(f"Số caption độc nhất: {len(counts)}")
print(f"Số mẫu caption bị lặp lại: {len(exact_dupes)}")

if exact_dupes:
    for text, cnt in exact_dupes.items():
        stts = [c[0] for c in captions if c[2] == text]
        print(f"\n⚠️ Lặp {cnt} lần ở các STT: {stts}")
        print(f"   Nội dung: \"{text[:120]}...\"")

# 2. Kiểm tra các câu mở đầu / cấu trúc câu giống nhau (Template repetition)
print(f"\n=== [2] KIỂM TRA CẤU TRÚC / PHRONT-RUNNER TEMPLATES ===")
opening_phrases = []
for c in captions:
    # Lấy câu đầu tiên của caption
    first_sentence = c[2].split(".")[0] if "." in c[2] else c[2]
    opening_phrases.append(first_sentence.strip())

open_counts = Counter(opening_phrases)
common_openings = {k: v for k, v in open_counts.items() if v > 1}
print(f"Số câu mở đầu bị lặp: {len(common_openings)}")
for op, cnt in open_counts.most_common(15):
    if cnt > 1:
        print(f"  • Lặp {cnt} lần: \"{op[:80]}\"")

# 3. In ra 10 caption mẫu từ các khoảng khác nhau (1-20, 50-70, 100-120, 130-150)
print(f"\n=== [3] MẪU CAPTION QUA CÁC GIAI ĐOẠN ===")
sample_stts = ["1", "2", "3", "31", "32", "61", "62", "101", "102", "121", "122", "149", "150"]
for c in captions:
    if c[0] in sample_stts:
        print(f"STT {c[0]} [{c[1]}]:\n   {c[2]}\n")
