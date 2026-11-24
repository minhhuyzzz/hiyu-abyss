#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Verify Live Rows 452 to 501 on Google Sheet
"""

import subprocess
import json

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch Đăng Bài (TikTok Pipeline)"

def main():
    print("=== KIỂM TRA TRỰC TIẾP DỮ LIỆU GOOGLE SHEET (HÀNG 452 -> 501) ===")
    check_ranges = ["A452:Q452", "A475:Q475", "A501:Q501"]
    
    for r in check_ranges:
        full_range = f"'{SHEET_TITLE}'!{r}"
        cmd = f'gsheets read {SPREADSHEET_ID} "{full_range}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"\n--- Range: {full_range} ---")
        if res.returncode == 0:
            print(res.stdout.strip())
        else:
            print("Error:", res.stderr)

if __name__ == '__main__':
    main()
