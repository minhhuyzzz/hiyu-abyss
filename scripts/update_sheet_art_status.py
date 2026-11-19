#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Update Google Sheet with Oil Artworks & Status
Cập nhật Cột P (Gợi Ý Phôi Ảnh) và Cột Q (Trạng Thái -> ĐÃ CÓ ẢNH) cho hàng 252 - 301.
"""

import json
import subprocess
import sys

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch 200 Bài (TikTok Pipeline)"
MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"

def main():
    print("=== CẬP NHẬT CỘT P & Q TRÊN GOOGLE SHEET (THEME 251 - 300) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    rows_pq = []
    for tid, t in manifest.items():
        stt = t["stt"]
        slides = t["slides"]
        num_slides = len(slides)
        
        art_list = [f"Slide {s['slide_index']}: {s['artist']} - '{s['artwork_title']}'" for s in slides]
        col_p_text = f"Bộ {num_slides} tranh sơn dầu bảo tàng CCO: " + " | ".join(art_list)
        col_q_text = "ĐÃ CÓ ẢNH"
        
        rows_pq.append([col_p_text, col_q_text])

    print(f"Loaded {len(rows_pq)} rows for range P252:Q301.")

    batch_payload = [
        {
            "op": "write",
            "range": f"'{SHEET_TITLE}'!P252:Q301",
            "data": rows_pq
        }
    ]

    with open("scripts/batch_write_art_status.json", "w", encoding="utf-8") as f:
        json.dump(batch_payload, f, ensure_ascii=False, indent=2)

    print("Executing gsheets mutate batch...")
    write_cmd = f'gsheets mutate batch {SPREADSHEET_ID} -f scripts/batch_write_art_status.json'
    res = subprocess.run(write_cmd, shell=True, capture_output=True, text=True)
    print("Stdout:", res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)
    if res.returncode != 0:
        print("❌ Write failed!")
        sys.exit(1)
        
    print("✅ Đã cập nhật thành công Cột P & Q trên Google Sheet cho hàng 252 - 301!")

if __name__ == '__main__':
    main()
