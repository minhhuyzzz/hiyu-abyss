# -*- coding: utf-8 -*-
"""
Script upload 150 bài đăng TikTok SEO lên Google Sheet và định dạng hoàn hảo.
"""

import shutil
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch 150 Bài (TikTok Pipeline)"
SOURCE_CSV = "c:/hiyuabyss/scripts/tiktok_150_posts_seo.csv"
TARGET_CSV = "c:/hiyuabyss/scripts/tiktok_150_posts.csv"

def main():
    print("[*] Đang cập nhật file CSV chính thức...")
    shutil.copyfile(SOURCE_CSV, TARGET_CSV)
    print(f"[✓] Đã ghi đè {TARGET_CSV}")

    print(f"[*] Đang import CSV lên Google Sheet tab '{SHEET_NAME}'...")
    import_cmd = f'gsheets mutate import-csv {SPREADSHEET_ID} "{TARGET_CSV}" --sheet "{SHEET_NAME}"'
    res = subprocess.run(import_cmd, shell=True, capture_output=True, text=True)
    print("Import stdout:", res.stdout)
    if res.stderr:
        print("Import stderr:", res.stderr)

    print("[*] Đang chạy polish_150_sheet.py để căn chỉnh định dạng...")
    res_polish = subprocess.run("python c:/hiyuabyss/scripts/polish_150_sheet.py", shell=True, capture_output=True, text=True)
    print("Polish stdout:", res_polish.stdout)
    if res_polish.stderr:
        print("Polish stderr:", res_polish.stderr)

    print("[*] Đang kiểm tra xác thực trực tiếp trên Google Sheet...")
    res_verify = subprocess.run("python c:/hiyuabyss/scripts/verify_live_150_sheet.py", shell=True, capture_output=True, text=True)
    print("Verify output:\n", res_verify.stdout)

if __name__ == "__main__":
    main()
