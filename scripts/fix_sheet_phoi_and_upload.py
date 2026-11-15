#!/usr/bin/env python3
# scripts/fix_sheet_phoi_and_upload.py
import csv
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch 150 Bài (TikTok Pipeline)"
CSV_PATH = "scripts/tiktok_150_posts.csv"
SEO_CSV_PATH = "scripts/tiktok_150_posts_seo.csv"

def fix_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    phoi_idx = header.index("Gợi Ý Phôi Ảnh")
    stt_idx = header.index("STT")
    
    fixed_count = 0
    for r in rows:
        stt = int(r[stt_idx])
        correct_phoi = f"theme_{stt:02d}"
        if r[phoi_idx] != correct_phoi:
            r[phoi_idx] = correct_phoi
            fixed_count += 1
            
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
        
    print(f"[✓] Đã cập nhật {path}: sửa {fixed_count} dòng phôi ảnh.")

fix_csv(CSV_PATH)
try:
    fix_csv(SEO_CSV_PATH)
except Exception as e:
    print(f"[!] Không thể cập nhật SEO CSV: {e}")

print(f"\n[*] Đang import CSV đã chuẩn hóa phôi ảnh lên Google Sheet tab '{SHEET_NAME}'...")
import_cmd = f'gsheets mutate import-csv {SPREADSHEET_ID} "{CSV_PATH}" --sheet "{SHEET_NAME}"'
res = subprocess.run(import_cmd, shell=True, capture_output=True, text=True)
print("Import stdout:", res.stdout.strip())
if res.stderr:
    print("Import stderr:", res.stderr.strip())

print("\n[*] Đang chạy scripts/polish_150_sheet.py để định dạng lại Google Sheet...")
res_polish = subprocess.run("python scripts/polish_150_sheet.py", shell=True, capture_output=True, text=True)
print("Polish stdout:", res_polish.stdout.strip())

print("\n[*] Đang kiểm tra xác thực trực tiếp trên Google Sheet...")
cmd_read = f'gsheets readonly read {SPREADSHEET_ID} "\'{SHEET_NAME}\'!A1:Q10"'
res_read = subprocess.run(cmd_read, shell=True, capture_output=True, text=True)
print("Sample first rows from Google Sheet:")
for line in res_read.stdout.strip().split("\n")[:4]:
    cols = line.split("\t")
    if len(cols) > 15:
        print(f"Row {cols[0]} | ID: {cols[1]} | Phôi: {cols[15]}")

cmd_read_end = f'gsheets readonly read {SPREADSHEET_ID} "\'{SHEET_NAME}\'!A145:Q152"'
res_read_end = subprocess.run(cmd_read_end, shell=True, capture_output=True, text=True)
print("Sample end rows from Google Sheet:")
for line in res_read_end.stdout.strip().split("\n"):
    cols = line.split("\t")
    if len(cols) > 15:
        print(f"Row {cols[0]} | ID: {cols[1]} | Phôi: {cols[15]}")
