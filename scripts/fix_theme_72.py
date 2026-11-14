import urllib.request
import urllib.parse
import json
import os
from PIL import Image, ImageFilter, ImageEnhance

# Query Wikimedia for clean URL of Chardin House of Cards
url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=File:Jean-Baptiste-Sim%C3%A9on%20Chardin%2C%20The%20House%20of%20Cards%2C%201736-37.jpg&prop=imageinfo&iiprop=url&iiurlwidth=1920"
req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = json.loads(resp.read().decode())
    pages = data.get("query", {}).get("pages", {})
    info = list(pages.values())[0].get("imageinfo", [{}])[0]
    dl_url = info.get("thumburl") or info.get("url")
    print("Resolved URL:", dl_url)

raw_path = "c:/hiyuabyss/assets/templates/raw_cache/theme_72_raw.jpg"
req2 = urllib.request.Request(dl_url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})
with urllib.request.urlopen(req2, timeout=20) as resp:
    with open(raw_path, "wb") as f:
        f.write(resp.read())
print("Downloaded theme_72 successfully! Size:", os.path.getsize(raw_path))

# Render theme_72 (3 slides)
TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H

def smart_crop_and_enhance(im, center_x, center_y, zoom):
    orig_w, orig_h = im.size
    crop_h = int(orig_h * zoom)
    crop_w = int(crop_h * TARGET_RATIO)
    if crop_w > orig_w:
        crop_w = int(orig_w * zoom)
        crop_h = int(crop_w / TARGET_RATIO)
    crop_w = min(crop_w, orig_w)
    crop_h = min(crop_h, orig_h)
    cx, cy = int(orig_w * center_x), int(orig_h * center_y)
    x1 = max(0, min(cx - crop_w // 2, orig_w - crop_w))
    y1 = max(0, min(cy - crop_h // 2, orig_h - crop_h))
    cropped = im.crop((x1, y1, x1 + crop_w, y1 + crop_h))
    resized = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    pass1 = resized.filter(ImageFilter.UnsharpMask(radius=1.8, percent=140, threshold=2))
    pass2 = pass1.filter(ImageFilter.UnsharpMask(radius=0.7, percent=80, threshold=1))
    enh = ImageEnhance.Contrast(pass2)
    return enh.enhance(1.05)

im = Image.open(raw_path).convert("RGB")
theme_dir = "c:/hiyuabyss/assets/templates/multislides/theme_72"
os.makedirs(theme_dir, exist_ok=True)

s1 = smart_crop_and_enhance(im, 0.50, 0.50, 0.95)
s1.save(os.path.join(theme_dir, "slide_1_establishing.jpg"), "JPEG", quality=95)

s2 = smart_crop_and_enhance(im, 0.50, 0.45, 0.42)
s2.save(os.path.join(theme_dir, "slide_2_closeup.jpg"), "JPEG", quality=95)

s3 = smart_crop_and_enhance(im, 0.50, 0.40, 0.28)
s3.save(os.path.join(theme_dir, "slide_3_macro.jpg"), "JPEG", quality=95)

print("[✓] Đã tạo thành công 3 slide cho theme_72!")
