#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Upload Posts 401-450 & Polish Sheet Formatting (Rows 402-451)
1. Writes 50 rows into range A402:Q451 via gsheets mutate batch
2. Standardizes formatting via gsheets mutate raw-batch:
   - Copies cell formatting & data validation from row 204 (index 203) to rows 402-451 (indices 401-451)
   - Enforces wrapStrategy: WRAP, verticalAlignment: MIDDLE, font: Roboto 9pt
"""

import json
import subprocess
import sys

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch Đăng Bài (TikTok Pipeline)"
SHEET_ID = 0

def main():
    print("=== NẠP 50 BÀI LÔ 1 (401-450) VÀ CHUẨN HÓA ĐỊNH DẠNG GOOGLE SHEET ===")

    # 1. Load posts 401-450
    with open('scripts/posts_401_450.json', encoding='utf-8') as f:
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

    print(f"Loaded {len(rows_data)} rows for range A402:Q451.")

    # 2. Build batch write payload
    batch_payload = [
        {
            "op": "write",
            "range": f"'{SHEET_TITLE}'!A402:Q451",
            "data": rows_data
        }
    ]

    batch_file = 'scripts/batch_write_401_450.json'
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
    print("✅ Đã ghi thành công 50 hàng vào A402:Q451!")

    # 3. Build formatting requests
    raw_requests = [
        # Step A: Copy paste FORMAT from row 204 (index 203) to rows 402-451 (indices 401-451)
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
                    "startRowIndex": 401,
                    "endRowIndex": 451,
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
                    "startRowIndex": 401,
                    "endRowIndex": 451,
                    "startColumnIndex": 16,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_DATA_VALIDATION"
            }
        },
        # Step C: Repeat formatting enforcement (WRAP, MIDDLE, Roboto 9pt)
        {
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": 401,
                    "endRowIndex": 451,
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

    polish_file = 'scripts/polish_requests_401_450.json'
    with open(polish_file, 'w', encoding='utf-8') as f:
        json.dump({"requests": raw_requests}, f, ensure_ascii=False, indent=2)

    print("Executing gsheets mutate raw-batch...")
    polish_cmd = f'gsheets mutate raw-batch {SPREADSHEET_ID} -f {polish_file}'
    res_polish = subprocess.run(polish_cmd, shell=True, capture_output=True, text=True)
    print("Polish stdout:", res_polish.stdout)
    if res_polish.stderr:
        print("Polish stderr:", res_polish.stderr)
    if res_polish.returncode != 0:
        print("❌ Polish failed!")
        sys.exit(1)
    print("✅ Đã chuẩn hóa định dạng (WRAP, MIDDLE, Roboto 9pt, dropdown) thành công cho Lô 1!")

if __name__ == '__main__':
    main()
