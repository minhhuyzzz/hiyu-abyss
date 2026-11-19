#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Upload Posts 251-300 & Polish Sheet Formatting (Rows 205-301)
1. Writes 50 new rows into range A252:Q301 via gsheets mutate batch
2. Fixes formatting disparity from row 205 downwards via gsheets mutate raw-batch:
   - Copies cell formatting & data validation from row 204 (index 203) to rows 205-301
   - Enforces wrapStrategy: WRAP, verticalAlignment: MIDDLE, font: Roboto 9pt
   - Auto-resizes row heights so multi-line text wraps cleanly without flattening
3. Verifies live sheet data
"""

import json
import subprocess
import sys

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch 200 Bài (TikTok Pipeline)"
SHEET_ID = 0

def main():
    print("=== NẠP 50 BÀI (251-300) VÀ CHUẨN HÓA ĐỊNH DẠNG GOOGLE SHEET ===")

    # 1. Load posts 251-300
    with open('scripts/posts_251_300.json', encoding='utf-8') as f:
        posts = json.load(f)

    rows_data = []
    for p in posts:
        row = [
            str(p['stt']),
            p['id'],
            p['title'],
            p['caption'],
            p['author'],
            p['hashtags'],
            p['format'],
            p['hook'],
            p['twist'],
            p['mirror'],
            p['deep'],
            p['full_text'],
            p['topic'],
            p['hours'],
            p['schedule'],
            p['concept'],
            "SẴN SÀNG"
        ]
        rows_data.append(row)

    print(f"Loaded {len(rows_data)} rows for range A252:Q301.")

    # 2. Build batch write payload
    batch_payload = [
        {
            "op": "write",
            "range": f"'{SHEET_TITLE}'!A252:Q301",
            "data": rows_data
        }
    ]

    with open('scripts/batch_write_251_300.json', 'w', encoding='utf-8') as f:
        json.dump(batch_payload, f, ensure_ascii=False, indent=2)

    print("Executing gsheets mutate batch...")
    write_cmd = f'gsheets mutate batch {SPREADSHEET_ID} -f scripts/batch_write_251_300.json'
    res_write = subprocess.run(write_cmd, shell=True, capture_output=True, text=True)
    print("Write stdout:", res_write.stdout)
    if res_write.stderr:
        print("Write stderr:", res_write.stderr)
    if res_write.returncode != 0:
        print("❌ Write failed!")
        sys.exit(1)
    print("✅ Đã ghi thành công 50 hàng vào A252:Q301!")

    # 3. Build formatting requests
    # Copy format and data validation from row 204 (index 203) to rows 205-301 (indices 204 to 301)
    # Total data rows: 1 to 301 (index 1 to 301)
    raw_requests = [
        # Step A: Copy paste FORMAT from row 204 (index 203) to rows 205-301 (index 204-301)
        {
            "copyPaste": {
                "source": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 203,
                    "endRowIndex": 204,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "destination": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 204,
                    "endRowIndex": 301,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_FORMAT"
            }
        },
        # Step B: Copy paste DATA VALIDATION (dropdown menu) to column Q (index 16..17)
        {
            "copyPaste": {
                "source": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 203,
                    "endRowIndex": 204,
                    "startColumnIndex": 16,
                    "endColumnIndex": 17
                },
                "destination": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 204,
                    "endRowIndex": 301,
                    "startColumnIndex": 16,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_DATA_VALIDATION"
            }
        },
        # Step C: Guarantee wrapStrategy WRAP and vertical MIDDLE for all data rows 1..301
        {
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 1,
                    "endRowIndex": 301,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "cell": {
                    "userEnteredFormat": {
                        "verticalAlignment": "MIDDLE",
                        "wrapStrategy": "WRAP",
                        "textFormat": {
                            "fontFamily": "Roboto",
                            "fontSize": 9
                        }
                    }
                },
                "fields": "userEnteredFormat(verticalAlignment,wrapStrategy,textFormat)"
            }
        },
        # Step D: Auto resize row heights for rows 204 to 301 so all text wraps with comfortable height
        {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": 204,
                    "endIndex": 301
                }
            }
        }
    ]

    # Step E: Column widths definition
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
        (10, 11, 260), # K: Trang 4
        (11, 12, 320), # L: Văn Bản Hoàn Chỉnh
        (12, 13, 200), # M: Chủ Đề Hạt Nhân
        (13, 14, 140), # N: Khung Giờ Vàng
        (14, 15, 130), # O: Lịch Đăng
        (15, 16, 220), # P: Gợi Ý Phôi Ảnh
        (16, 17, 130), # Q: Trạng Thái
    ]
    for start, end, size in col_widths:
        raw_requests.append({
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

    with open('scripts/polish_sheet_205_301.json', 'w', encoding='utf-8') as f:
        json.dump({"requests": raw_requests}, f, indent=2)

    print("Executing gsheets mutate raw-batch to polish formatting...")
    format_cmd = f'gsheets mutate raw-batch {SPREADSHEET_ID} -f scripts/polish_sheet_205_301.json'
    res_format = subprocess.run(format_cmd, shell=True, capture_output=True, text=True)
    print("Format stdout:", res_format.stdout)
    if res_format.stderr:
        print("Format stderr:", res_format.stderr)
    if res_format.returncode != 0:
        print("❌ Format failed!")
        sys.exit(1)
    print("✅ Đã hoàn tất căn chỉnh định dạng toàn bộ từ hàng 205 đến 301!")

if __name__ == '__main__':
    main()
