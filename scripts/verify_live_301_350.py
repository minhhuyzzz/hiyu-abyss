# -*- coding: utf-8 -*-
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch Đăng Bài (TikTok Pipeline)"

cmd_cell = f'gsheets readonly inspect-cell {SPREADSHEET_ID} "\'{SHEET_NAME}\'!C302" --json'
res_cell = subprocess.run(cmd_cell, shell=True, capture_output=True, text=True)
print("=== CELL C302 FORMAT ===")
print(res_cell.stdout)
