#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Upload Posts 301-350 & Polish Sheet Formatting (Rows 302-351)
1. Writes 50 new rows into range A302:Q351 via gsheets mutate batch
2. Standardizes formatting via gsheets mutate raw-batch:
   - Copies cell formatting & data validation from row 204 (index 203) to rows 302-351 (indices 301-351)
   - Enforces wrapStrategy: WRAP, verticalAlignment: MIDDLE, font: Roboto 9pt
3. Verifies live sheet data
"""

import json
import subprocess
import sys

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch Đăng Bài (TikTok Pipeline)"
SHEET_ID = 0

def main():
    print("=== NẠP 50 BÀI LƯU ĐỒ (301-350) VÀ CHUẨN HÓA ĐỊNH DẠNG GOOGLE SHEET ===")

    # 1. Load posts 301-350
    with open('scripts/posts_301_350.json', encoding='utf-8') as f:
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
            p['status']
        ]
        rows_data.append(row)

    print(f"Loaded {len(rows_data)} rows for range A302:Q351.")

    # 2. Build batch write payload
    batch_payload = [
        {
            "op": "write",
            "range": f"'{SHEET_TITLE}'!A302:Q351",
            "data": rows_data
        }
    ]

    batch_file = 'scripts/batch_write_301_350.json'
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(batch_payload, f, ensure_ascii=False, indent=2)

    print("Executing gsheets mutate batch...")
    write_cmd = f'gsheets mutate batch {SPREADSHEET_ID} -f {batch_file}'
    res_write = subprocess.run(write_cmd, shell=True, capture_output=True, text=True)
    print("Write stdout:", res_write.stdout)
    if res_write.stderr:
        print("Write stderr:", res_write.stderr)
    if res_write.returncode != 0:
        print("❌ Write failed!")
        sys.exit(1)
    print("✅ Đã ghi thành công 50 hàng vào A302:Q351!")

    # 3. Build formatting requests
    # Copy format and data validation from row 204 (index 203) to rows 302-351 (indices 301 to 351)
    raw_requests = [
        # Step A: Copy paste FORMAT from row 204 (index 203) to rows 302-351 (indices 301-351)
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
                    "startRowIndex": 301,
                    "endRowIndex": 351,
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
                    "startRowIndex": 301,
                    "endRowIndex": 351,
                    "startColumnIndex": 16,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_DATA_VALIDATION"
            }
        },
        # Step C: Guarantee wrapStrategy WRAP and vertical MIDDLE for all data rows 301..351
        {
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 301,
                    "endRowIndex": 351,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "cell": {
                    "userEnteredFormat": {
                        "wrapStrategy": "WRAP",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Roboto",
                            "fontSize": 9
                        }
                    }
                },
                "fields": "userEnteredFormat.wrapStrategy,userEnteredFormat.verticalAlignment,userEnteredFormat.textFormat.fontFamily,userEnteredFormat.textFormat.fontSize"
            }
        }
    ]

    format_file = 'scripts/format_req_301_350.json'
    with open(format_file, 'w', encoding='utf-8') as f:
        json.dump({"requests": raw_requests}, f, indent=2)

    print("Executing gsheets mutate raw-batch for formatting...")
    fmt_cmd = f'gsheets mutate raw-batch {SPREADSHEET_ID} -f {format_file}'
    res_fmt = subprocess.run(fmt_cmd, shell=True, capture_output=True, text=True)
    print("Fmt stdout:", res_fmt.stdout)
    if res_fmt.stderr:
        print("Fmt stderr:", res_fmt.stderr)
    if res_fmt.returncode != 0:
        print("❌ Format request failed!")
        sys.exit(1)
    print("✅ Đã chuẩn hóa định dạng (WRAP, MIDDLE, Roboto 9pt) cho toàn bộ hàng 302-351!")

if __name__ == '__main__':
    main()
