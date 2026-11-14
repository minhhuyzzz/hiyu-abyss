#!/usr/bin/env python3
"""
Hiyu Abyss — Update 100 Authors with Real Philosophers / Classical Sources
No more @hiyuabyss. Replaced with authentic historical thinkers and evocative terms:
- Friedrich Nietzsche, Arthur Schopenhauer, Marcus Aurelius, Seneca, Carl Jung, Sigmund Freud,
  La Rochefoucauld, Fyodor Dostoevsky, Blaise Pascal, Albert Camus, Jean-Paul Sartre,
  Erich Fromm, Gustave Le Bon, Epictetus, Oscar Wilde, Niccolo Machiavelli, Michel de Montaigne...
- 'Từ điển Tâm lý học', 'Ghi chép Khắc kỷ', 'Tâm lý học Đám đông', 'Lời của Seneca', 'Khảo luận Luân lý'...
"""

NEW_AUTHORS = {
    1: "La Rochefoucauld",
    2: "Seneca",
    3: "La Rochefoucauld",
    4: "Từ điển Tâm lý học",
    5: "Friedrich Nietzsche",
    6: "Arthur Schopenhauer",
    7: "Fyodor Dostoevsky",
    8: "Khảo luận Luân lý",
    9: "Từ điển Hành vi",
    10: "René Girard",
    11: "Friedrich Nietzsche",
    12: "Friedrich Nietzsche",
    13: "Ghi chép Khắc kỷ",
    14: "Seneca",
    15: "La Rochefoucauld",
    16: "Arthur Schopenhauer",
    17: "Carl Jung",
    18: "Arthur Schopenhauer",
    19: "Ghi chép Khắc kỷ",
    20: "Sigmund Freud",
    21: "Blaise Pascal",
    22: "Blaise Pascal",
    23: "Từ điển Hiện sinh",
    24: "Jean-Paul Sartre",
    25: "Friedrich Nietzsche",
    26: "Carl Jung",
    27: "Carl Jung",
    28: "Carl Jung",
    29: "Abraham Lincoln",
    30: "Carl Jung",
    31: "Oscar Wilde",
    32: "Carl Jung",
    33: "Từ điển Cảm xúc",
    34: "Arthur Schopenhauer",
    35: "Từ điển Tâm lý học",
    36: "Niccolò Machiavelli",
    37: "Niccolò Machiavelli",
    38: "Sun Tzu",
    39: "Niccolò Machiavelli",
    40: "Marcus Aurelius",
    41: "Từ điển Tâm lý học",
    42: "La Rochefoucauld",
    43: "Sigmund Freud",
    44: "Lời của Seneca",
    45: "Arthur Schopenhauer",
    46: "Søren Kierkegaard",
    47: "Søren Kierkegaard",
    48: "Epictetus",
    49: "Jean-Paul Sartre",
    50: "Ghi chép Khắc kỷ",
    51: "Fyodor Dostoevsky",
    52: "Fyodor Dostoevsky",
    53: "Albert Camus",
    54: "Fyodor Dostoevsky",
    55: "Từ điển Hiện sinh",
    56: "Erich Fromm",
    57: "Từ điển Tâm lý học",
    58: "Lời của Erich Fromm",
    59: "Từ điển Cảm xúc",
    60: "Arthur Schopenhauer",
    61: "Marcus Aurelius",
    62: "Marcus Aurelius",
    63: "Marcus Aurelius",
    64: "Niccolò Machiavelli",
    65: "Seneca",
    66: "Baruch Spinoza",
    67: "Baruch Spinoza",
    68: "Lời của Seneca",
    69: "Baruch Spinoza",
    70: "Baruch Spinoza",
    71: "Gustave Le Bon",
    72: "Friedrich Nietzsche",
    73: "Tâm lý học Đám đông",
    74: "Friedrich Nietzsche",
    75: "Friedrich Nietzsche",
    76: "Sigmund Freud",
    77: "Sigmund Freud",
    78: "Viktor Frankl",
    79: "La Rochefoucauld",
    80: "Friedrich Nietzsche",
    81: "Seneca",
    82: "Seneca",
    83: "Ralph Waldo Emerson",
    84: "Seneca",
    85: "Jean-Paul Sartre",
    86: "Albert Camus",
    87: "Albert Camus",
    88: "Albert Camus",
    89: "Albert Camus",
    90: "Viktor Frankl",
    91: "Blaise Pascal",
    92: "Arthur Schopenhauer",
    93: "Ghi chép Khắc kỷ",
    94: "Erich Fromm",
    95: "Blaise Pascal",
    96: "Lão Tử",
    97: "Khảo luận Luân lý",
    98: "Arthur Schopenhauer",
    99: "Lời của Seneca",
    100: "Albert Camus"
}

import csv
import subprocess

csv_path = "scripts/tiktok_100_posts_v2.csv"
rows = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)
    author_idx = headers.index("Nguồn Tác Giả")
    for r in reader:
        stt = int(r[0])
        r[author_idx] = NEW_AUTHORS.get(stt, r[author_idx])
        rows.append(r)

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[✓] Đã cập nhật file CSV: {csv_path} với 100 tác giả thực tế & nguồn kinh điển.")

# Verify no @hiyuabyss remains
hiyu_count = sum(1 for r in rows if r[author_idx] == "@hiyuabyss")
print(f"Số lượng @hiyuabyss còn lại: {hiyu_count}")

# Import back to Google Sheet
SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch 100 Bài (TikTok Pipeline)"
print(f"[*] Đang đồng bộ lên Google Sheet...")
cmd = f'gsheets mutate import-csv {SPREADSHEET_ID} "{csv_path}" --sheet "{SHEET_NAME}"'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Import output:", res.stdout)
if res.stderr:
    print("Import stderr:", res.stderr)

# Re-apply formatting & ensure column E width is 160px, header dark slate, center align
format_script = "scripts/apply_formatting.py"
subprocess.run(f"python {format_script}", shell=True)
print("[✓] Đã hoàn tất đồng bộ 100 tác giả mới lên Google Sheet!")
