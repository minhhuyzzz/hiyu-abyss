import os
from PIL import Image

BASE_DIR = "c:/hiyuabyss/assets/templates/multislides"
EXPECTED_THEMES = [f"theme_{i:02d}" for i in range(61, 91)]

print(f"=== AUDITING 30 CHARMING SUITES (THEME 61 - 90) ===")
total_valid_images = 0
errors = []

for tid in EXPECTED_THEMES:
    tdir = os.path.join(BASE_DIR, tid)
    if not os.path.exists(tdir):
        errors.append(f"Missing directory: {tid}")
        continue
    files = sorted(os.listdir(tdir))
    expected_files = ["slide_1_establishing.jpg", "slide_2_closeup.jpg", "slide_3_macro.jpg"]
    if files != expected_files:
        errors.append(f"{tid} has mismatched files: {files}")
        continue
    for fname in expected_files:
        fpath = os.path.join(tdir, fname)
        size_kb = os.path.getsize(fpath) / 1024
        try:
            with Image.open(fpath) as im:
                w, h = im.size
                if w != 1080 or h != 1920:
                    errors.append(f"{tid}/{fname} invalid dimensions: {w}x{h}")
                elif size_kb < 50:
                    errors.append(f"{tid}/{fname} suspiciously small size: {size_kb:.1f} KB")
                else:
                    total_valid_images += 1
        except Exception as e:
            errors.append(f"{tid}/{fname} corrupted: {e}")

print(f"Total valid 1080x1920 vertical images: {total_valid_images} / 90")
if errors:
    print(f"Found {len(errors)} errors:")
    for err in errors[:10]:
        print(f"  [X] {err}")
else:
    print("[✓] 100% HOÀN HẢO! Cả 30 bộ ảnh (90 ảnh 9:16) đều đạt chuẩn 1080x1920 siêu nét!")
