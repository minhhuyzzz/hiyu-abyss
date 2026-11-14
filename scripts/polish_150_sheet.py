import json
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_ID = 0
SHEET_NAME = "Kế Hoạch 150 Bài (TikTok Pipeline)"
TOTAL_ROWS = 152  # 1 header + 150 data rows

requests = [
    # 1. Clear any data validation on columns 0..15 (A to O) for rows 1 to 155
    {
        "setDataValidation": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS + 5,
                "startColumnIndex": 0,
                "endColumnIndex": 15
            }
        }
    },
    # 2. Header styling: Dark background #0F172A, white bold text, centered, middle
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 16
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 15/255, "green": 23/255, "blue": 42/255},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP",
                    "textFormat": {
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                        "bold": True,
                        "fontSize": 10
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,wrapStrategy,textFormat)"
        }
    },
    # 3. All data rows: wrap text, vertical middle
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 0,
                "endColumnIndex": 16
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP"
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,wrapStrategy)"
        }
    },
    # 4. Centered columns in data: STT (0..1), ID (1..2), Author (4..5), Format (6..7), Slot (12..13), Date (13..14), Phôi ảnh (14..15), Trạng thái (15..16)
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 0,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    },
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    },
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 6,
                "endColumnIndex": 7
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    },
    {
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 1,
                "endRowIndex": TOTAL_ROWS,
                "startColumnIndex": 12,
                "endColumnIndex": 16
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat.horizontalAlignment"
        }
    }
]

# Set column widths
widths = [
    (0, 1, 60),    # A: STT
    (1, 2, 95),    # B: Mã ID
    (2, 3, 280),   # C: Tiêu Đề
    (3, 4, 380),   # D: Mô Tả
    (4, 5, 180),   # E: Nguồn Tác Giả
    (5, 6, 230),   # F: Hashtags
    (6, 7, 160),   # G: Định Dạng Slide
    (7, 8, 260),   # H: Trang 1
    (8, 9, 260),   # I: Trang 2
    (9, 10, 260),  # J: Trang 3
    (10, 11, 320), # K: Văn Bản Hoàn Chỉnh
    (11, 12, 200), # L: Chủ Đề Hạt Nhân
    (12, 13, 140), # M: Khung Giờ Vàng
    (13, 14, 130), # N: Lịch Đăng
    (14, 15, 120), # O: Gợi Ý Phôi Ảnh
    (15, 16, 130), # P: Trạng Thái
]

for start, end, size in widths:
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": SHEET_ID,
                "dimension": "COLUMNS",
                "startIndex": start,
                "endIndex": end
            },
            "properties": {
                "pixelSize": size
            },
            "fields": "pixelSize"
        }
    })

batch_payload = {"requests": requests}
batch_json = "scripts/polish_150_batch.json"
with open(batch_json, "w", encoding="utf-8") as f:
    json.dump(batch_payload, f, indent=2)

print("[*] Đang gửi batch format request lên Google Sheet...")
cmd = f'gsheets mutate raw-batch {SPREADSHEET_ID} -f {batch_json}'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Result:", res.stdout, res.stderr)

# Ensure dropdown on Column P (P2:P151)
print("[*] Đang cài đặt Dropdown trạng thái cho Cột P...")
cmd_dv = f'gsheets mutate data-validation {SPREADSHEET_ID} --range "\'{SHEET_NAME}\'!P2:P155" --values "SẴN SÀNG,ĐÃ LÊN LỊCH,ĐÃ ĐĂNG,TẠM HOÃN"'
subprocess.run(cmd_dv, shell=True, capture_output=True)

# Freeze top 1 row and left 2 columns
print("[*] Đang cố định (Freeze) tiêu đề và 2 cột đầu...")
cmd_frz = f'gsheets mutate freeze {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --rows 1 --cols 2'
subprocess.run(cmd_frz, shell=True, capture_output=True)

print("[✓] Hoàn tất định dạng 150 bài trên Google Sheet!")
