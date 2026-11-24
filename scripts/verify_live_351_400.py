#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import json

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch Đăng Bài (TikTok Pipeline)"

def main():
    print("=== KIỂM TRA DỮ LIỆU THỰC TẾ TRÊN GOOGLE SHEET (HÀNG 352 ĐẾN 401) ===")
    
    # Read rows 352, 375, 401
    for r in [352, 375, 401]:
        cmd = f'gsheets readonly read {SPREADSHEET_ID} "\'{SHEET_TITLE}\'!A{r}:Q{r}" --json'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                row_vals = data.get("values", [[]])[0]
                print(f"\n--- HÀNG {r} (STT {row_vals[0]} | {row_vals[1]}) ---")
                print(f"Tiêu đề: {row_vals[2]}")
                print(f"Định dạng: {row_vals[6]}")
                print(f"Trang 1: {row_vals[7]}")
                print(f"Trang 2: {row_vals[8]}")
                print(f"Trang 3: {row_vals[9]}")
                print(f"Trang 4: {row_vals[10]}")
                print(f"Trạng thái: {row_vals[16]}")
            except Exception as e:
                print(f"Error parsing row {r}: {e}")
                print(res.stdout)
        else:
            print(f"Read row {r} failed: {res.stderr}")

if __name__ == '__main__':
    main()
