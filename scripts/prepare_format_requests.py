import json

req = {
    "requests": [
        {
            "copyPaste": {
                "source": {
                    "sheetId": 0,
                    "startRowIndex": 203,
                    "endRowIndex": 204,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "destination": {
                    "sheetId": 0,
                    "startRowIndex": 204,
                    "endRowIndex": 251,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_FORMAT",
                "pasteOrientation": "NORMAL"
            }
        },
        {
            "copyPaste": {
                "source": {
                    "sheetId": 0,
                    "startRowIndex": 203,
                    "endRowIndex": 204,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "destination": {
                    "sheetId": 0,
                    "startRowIndex": 204,
                    "endRowIndex": 251,
                    "startColumnIndex": 0,
                    "endColumnIndex": 17
                },
                "pasteType": "PASTE_DATA_VALIDATION",
                "pasteOrientation": "NORMAL"
            }
        },
        {
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": 0,
                    "dimension": "ROWS",
                    "startIndex": 204,
                    "endIndex": 251
                }
            }
        }
    ]
}

with open("scripts/format_requests.json", "w", encoding="utf-8") as f:
    json.dump(req, f, indent=2)

print("Created scripts/format_requests.json")
