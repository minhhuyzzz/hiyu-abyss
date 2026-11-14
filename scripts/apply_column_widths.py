import json
import subprocess

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

requests = []
for start, end, size in widths:
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": 0,
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
with open("c:/hiyuabyss/scripts/set_widths.json", "w", encoding="utf-8") as f:
    json.dump(batch_payload, f, indent=2)

cmd = 'gsheets mutate raw-batch 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY -f c:/hiyuabyss/scripts/set_widths.json'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Set widths result:", res.stdout, res.stderr)
