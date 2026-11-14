# -*- coding: utf-8 -*-
"""
Script định dạng thẩm mỹ hoàn hảo cho Google Sheet 150 bài Hiyu Abyss (17 Cột A -> Q):
1. Xóa sạch mọi Data Validation cũ trên cột A -> P.
2. Tiêu đề Dark Slate (#0F172A), chữ trắng (#FFFFFF), in đậm, căn giữa.
3. Độ rộng tối ưu cho từng cột (A -> Q).
4. Căn giữa các cột mã số, ngày giờ, trạng thái.
5. Wrap text toàn bộ bảng.
6. Cài đặt Dropdown chuẩn cho Cột Q (Trạng Thái).
7. Cố định (Freeze) dòng 1 và 2 cột A, B.
"""

import json
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_ID = 0
SHEET_NAME = "Kế Hoạch 150 Bài (TikTok Pipeline)"
TOTAL_ROWS = 152  # 1 header + 150 data rows

requests = [
    # 1. Clear any data validation on columns 0..16 (A to P) for rows 1 to 155
    {
        "setDataValidation": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS + 5,
                "startColumnIndex": 0,
                "endColumnIndex": 16
            }
        }
    },
    # 2. Header style: Dark Slate #0F172A, Bold, White text, Centered
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 17
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.059, "green": 0.090, "blue": 0.165},
                    "textFormat": {
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                        "bold": True,
                        "fontSize": 10,
                        "fontFamily": "Roboto"
                    },
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
        }
    },
    # 3. Data rows style: Wrap text & Middle vertical alignment
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 0,
                "endColumnIndex": 17
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                    "textFormat": {
                        "fontSize": 9,
                        "fontFamily": "Roboto"
                    }
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,wrapStrategy,textFormat)"
        }
    },
    # 4. Center alignments for specific columns:
    # Col 0 (STT), Col 1 (Mã ID), Col 4 (Nguồn Tác Giả), Col 6 (Định Dạng),
    # Col 13 (Khung Giờ), Col 14 (Lịch Đăng), Col 15 (Phôi Ảnh), Col 16 (Trạng Thái)
]

for col_idx in [0, 1, 4, 6, 13, 14, 15, 16]:
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": col_idx,
                "endColumnIndex": col_idx + 1
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    })

# Column widths (17 columns A -> Q)
col_widths = [
    (0, 1, 60),    # A: STT
    (1, 2, 95),    # B: Mã ID
    (2, 3, 280),   # C: Tiêu Đề
    (3, 4, 380),   # D: Mô Tả (Caption)
    (4, 5, 180),   # E: Nguồn Tác Giả
    (5, 6, 230),   # F: Hashtags
    (6, 7, 160),   # G: Định Dạng Slide
    (7, 8, 260),   # H: Trang 1
    (8, 9, 260),   # I: Trang 2
    (9, 10, 260),  # J: Trang 3
    (10, 11, 260), # K: Trang 4 (Đúc kết)
    (11, 12, 320), # L: Văn Bản Hoàn Chỉnh
    (12, 13, 200), # M: Chủ Đề Hạt Nhân
    (13, 14, 140), # N: Khung Giờ Vàng
    (14, 15, 130), # O: Lịch Đăng
    (15, 16, 120), # P: Gợi Ý Phôi Ảnh
    (16, 17, 130)  # Q: Trạng Thái
]

for start, end, size in col_widths:
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": start,
                "endIndex": end
            },
            "properties": {
                "pixelSize": size
            },
            "fields": "pixelSize"
        }
    })

batch_payload = {"requests": requests}
batch_json = "scripts/polish_150_batch.json"
with open(batch_json, "w", encoding="utf-8") as f:
    json.dump(batch_payload, f, indent=2)

print("[*] Đang gửi batch format request lên Google Sheet...")
cmd = f'gsheets mutate raw-batch {SPREADSHEET_ID} -f {batch_json}'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Result:", res.stdout, res.stderr)

# Ensure dropdown on Column Q (Q2:Q155)
print("[*] Đang cài đặt Dropdown trạng thái cho Cột Q...")
range_q = f"'{SHEET_NAME}'!Q2:Q155"
cmd_dv = f'gsheets mutate data-validation {SPREADSHEET_ID} --range "{range_q}" --values "SẴN SÀNG,ĐANG BIÊN TẬP,ĐÃ ĐĂNG,TẠM DỪNG"'
subprocess.run(cmd_dv, shell=True, capture_output=True)

# Freeze top 1 row and left 2 columns
print("[*] Đang cố định (Freeze) tiêu đề và 2 cột đầu...")
cmd_frz = f'gsheets mutate freeze {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --rows 1 --cols 2'
subprocess.run(cmd_frz, shell=True, capture_output=True)

print("[✓] Hoàn tất định dạng 150 bài trên Google Sheet (17 Cột A -> Q)!")
