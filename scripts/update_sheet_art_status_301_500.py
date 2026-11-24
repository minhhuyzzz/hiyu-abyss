import json
import subprocess
import sys

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_TITLE = "Kế Hoạch Đăng Bài (TikTok Pipeline)"

def main():
    print("=== CẬP NHẬT TRẠNG THÁI 'ĐÃ CÓ ẢNH' TRÊN GOOGLE SHEET (HÀNG 302 - 501) ===")
    
    rows_q = [["ĐÃ CÓ ẢNH"] for _ in range(200)]
    
    batch_payload = [
        {
            "op": "write",
            "range": f"'{SHEET_TITLE}'!Q302:Q501",
            "data": rows_q
        }
    ]
    
    payload_file = "scripts/batch_write_art_status_301_500.json"
    with open(payload_file, "w", encoding="utf-8") as f:
        json.dump(batch_payload, f, ensure_ascii=False, indent=2)
        
    print("Executing gsheets mutate batch...")
    cmd = f'gsheets mutate batch {SPREADSHEET_ID} -f {payload_file}'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("Stdout:", res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)
        
    if res.returncode == 0:
        print("✅ Đã cập nhật thành công 200 hàng sang trạng thái 'ĐÃ CÓ ẢNH' trên Google Sheet!")
    else:
        print("❌ Lỗi cập nhật Google Sheet.")
        sys.exit(1)

if __name__ == '__main__':
    main()
