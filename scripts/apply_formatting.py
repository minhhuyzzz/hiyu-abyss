import json
import subprocess

requests = [
    # Header styling: Dark background #0F172A, white bold text, centered, middle
    {
        "repeatCell": {
            "range": {
                "sheetId": 0,
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
    # All data rows: wrap text, vertical middle
    {
        "repeatCell": {
            "range": {
                "sheetId": 0,
                "startRowIndex": 1,
                "endRowIndex": 102,
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
    # Centered columns in data: STT (0..1), ID (1..2), Author (4..5), Format (6..7), Slot (12..13), Date (13..14), Phôi ảnh (14..15), Trạng thái (15..16)
    {
        "repeatCell": {
            "range": {
                "sheetId": 0,
                "startRowIndex": 1,
                "endRowIndex": 102,
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
                "sheetId": 0,
                "startRowIndex": 1,
                "endRowIndex": 102,
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
                "sheetId": 0,
                "startRowIndex": 1,
                "endRowIndex": 102,
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
                "sheetId": 0,
                "startRowIndex": 1,
                "endRowIndex": 102,
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

batch_payload = {"requests": requests}
with open("c:/hiyuabyss/scripts/format_batch.json", "w", encoding="utf-8") as f:
    json.dump(batch_payload, f, indent=2)

cmd = 'gsheets mutate raw-batch 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY -f c:/hiyuabyss/scripts/format_batch.json'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Format batch result:", res.stdout, res.stderr)
