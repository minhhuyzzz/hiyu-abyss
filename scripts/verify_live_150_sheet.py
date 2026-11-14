# -*- coding: utf-8 -*-
import subprocess
import json

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch 150 Bài (TikTok Pipeline)"

cmd = f'gsheets readonly read {SPREADSHEET_ID} "\'{SHEET_NAME}\'!A1:Q152"'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = res.stdout.strip().split("\n")
print(f"Total lines in live sheet: {len(lines)}")
header = lines[0].split("\t")
print(f"Total columns: {len(header)}")
print("Headers:", header)

# Check some sample rows
for idx in [1, 50, 101, 150]:
    if idx < len(lines):
        cols = lines[idx].split("\t")
        print(f"Row {cols[0]} | ID: {cols[1]} | Tác giả: {cols[4]:<20} | Slide 4: {cols[10]} | Phôi: {cols[15]} | Trạng thái: {cols[16]}")
