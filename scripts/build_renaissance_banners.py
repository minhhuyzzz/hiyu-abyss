#!/usr/bin/env python3
"""
Hiyu Abyss — 20 Authentic Renaissance & Classical Sculpture Banners (1080x1920, 9:16)
Curates 20 world-famous Renaissance sculptures & chiaroscuro masterworks (Michelangelo,
Bernini, Canova, Caravaggio, Rodin, Classical Antiquity) and composites them into
flawless vertical 9:16 mobile backgrounds with deep chiaroscuro and clean negative space.
Strictly NO text, NO watermarks.
"""

import os
import io
import urllib.request
import urllib.parse
import json
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

OUTPUT_DIR = "c:/hiyuabyss/assets/templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920

SCULPTURE_QUERIES = [
    ("theme_01_hypocrisy", "Michelangelo David head Florence", "Tượng David (Michelangelo) - Khắc họa ánh mắt sắc lạnh kiêu hùng"),
    ("theme_02_double_standard", "Ciceron Vaux", "Tượng bán thân Cicero - Cán cân phán xét cổ điển"),
    ("theme_03_morality", "Michelangelo Pieta marble Rome", "Tượng Pieta (Michelangelo) - Lòng vị tha và nỗi đau nén chặt"),
    ("theme_04_ego", "Marcus Aurelius bust marble Louvre", "Tượng Hoàng đế Marcus Aurelius - Bản ngã và sự tự chủ"),
    ("theme_05_self_deception", "Diocletien Vaux", "Tượng Hoàng đế Diocletian - Góc nhìn suy tưởng trĩu nặng"),
    ("theme_06_shadow", "The Thinker Rodin bronze Paris", "Người Suy Tưởng (Rodin) - Bóng tối nội tâm và sự giằng xé"),
    ("theme_07_mask", "Marble comic mask (SK Dresden Hm 224)", "Mặt nạ kịch nghệ cẩm thạch Hy Lạp cổ đại"),
    ("theme_08_power", "Michelangelo Moses San Pietro in Vincoli", "Tượng Moses (Michelangelo) - Quyền lực và uy nghiêm áp chế"),
    ("theme_09_manipulation", "Bernini Apollo Daphne marble Rome", "Apollo và Daphne (Bernini) - Sự giam cầm và thao túng số phận"),
    ("theme_10_freedom", "Nike of Samothrace Louvre", "Nữ thần Chiến thắng Samothrace - Đôi cánh tung bay vượt khỏi xiềng xích"),
    ("theme_11_truth", "Caravaggio Saint Jerome Writing Borghese", "Thánh Jerome (Caravaggio) - Ngọn đèn chân lý và đầu lâu chiêm nghiệm"),
    ("theme_12_love", "Canova Psyche Revived by Cupid Kiss Louvre", "Cupid & Psyche (Canova) - Tình yêu và ranh giới mong manh"),
    ("theme_13_loyalty", "Dying Gaul marble Rome", "Chiến binh Gaul hấp hối - Lòng trung nghĩa và cái chết kiêu hãnh"),
    ("theme_14_envy", "Bernini Medusa marble Rome", "Nữ thần Medusa (Bernini) - Cơn cuồng nộ và ánh nhìn đố kỵ hóa đá"),
    ("theme_15_crowd", "Laocoon and his sons Vatican", "Tượng Laocoön (Vatican) - Cuộc vật lộn tuyệt vọng trước số đông"),
    ("theme_16_suffering", "Michelangelo Dying Slave Louvre", "Người Nô Lệ Hấp Hối (Michelangelo) - Nỗi đau thể xác và sự giải thoát"),
    ("theme_17_identity", "Belvedere Torso Vatican marble", "Khối thân Belvedere Torso - Bản sắc nguyên bản của con người"),
    ("theme_18_meaning", "Bust Homer marble British Museum", "Tượng thi hào Homer - Người mù đi tìm ý nghĩa giữa nhân gian"),
    ("theme_19_solitude", "Venus de Milo Louvre marble", "Tượng Nữ thần Venus de Milo - Vẻ đẹp đơn độc bất biến qua ngàn năm"),
    ("theme_20_status", "Augustus Prima Porta marble Rome", "Tượng Augustus Prima Porta - Vinh quang danh vọng và sự uy nghi")
]

def search_wikimedia_image(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=5&prop=imageinfo&iiprop=url|size&gsrnamespace=6"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (admin@hiyuabyss.local)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                title = pdata.get("title", "")
                if any(title.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
                    img_info = pdata.get("imageinfo", [{}])[0]
                    u = img_info.get("url")
                    if u and "thumb" not in u and img_info.get("width", 0) > 600:
                        return u
    except Exception as e:
        print(f"Error searching for {query}: {e}")
    return None

def download_image(url):
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (admin@hiyuabyss.local)"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()

def process_banner(img_data, out_path, theme_code):
    src = Image.open(io.BytesIO(img_data)).convert("RGB")

    # Base canvas 1080x1920 (Dark Charcoal Obsidian #080C14)
    canvas = Image.new("RGB", (WIDTH, HEIGHT), color=(8, 12, 20))

    # Calculate optimal resize & crop for upper half
    # We want the sculpture prominently featured in upper 45% - 60%
    target_w = WIDTH
    scale = target_w / src.width
    scaled_h = int(src.height * scale)

    if scaled_h < 950:
        # If too short, scale by height
        scale = 1050 / src.height
        scaled_w = int(src.width * scale)
        scaled_h = 1050
        resized = src.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
        # Center horizontally
        offset_x = (WIDTH - scaled_w) // 2
        canvas.paste(resized, (offset_x, 0))
    else:
        resized = src.resize((target_w, scaled_h), Image.Resampling.LANCZOS)
        canvas.paste(resized, (0, 0))

    # Convert to array for chiaroscuro color grading and gradient blending
    arr = np.array(canvas, dtype=np.float32)

    # 1. Subtle moody color grading (desaturate slightly, boost cold shadows)
    luminance = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    # Tint towards museum cold marble
    arr[:, :, 0] = arr[:, :, 0] * 0.75 + luminance * 0.22
    arr[:, :, 1] = arr[:, :, 1] * 0.78 + luminance * 0.22
    arr[:, :, 2] = arr[:, :, 2] * 0.85 + luminance * 0.20

    # 2. Boost Chiaroscuro Contrast: crush darks, pop highlights
    arr = np.clip((arr - 25.0) * 1.35 + 20.0, 0.0, 255.0)

    # 3. Create seamless downward fade into pitch black / dark charcoal
    # Top 30% fully visible, mid 30%-55% fades smoothly, bottom 45% is 100% clean dark negative space
    y_norm = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    fade = np.clip((y_norm - 0.32) / 0.28, 0.0, 1.0)
    target_dark = np.array([8, 12, 18], dtype=np.float32)

    arr = arr * (1.0 - fade) + target_dark * fade

    # 4. Vignette on top edges
    x_norm = np.linspace(-1.0, 1.0, WIDTH)[None, :, None]
    vignette = np.clip(1.0 - 0.35 * (x_norm ** 2), 0.5, 1.0)
    arr = arr * vignette

    # 5. Fine art film grain noise (2.0 intensity)
    noise = np.random.normal(0.0, 2.2, arr.shape).astype(np.float32)
    arr = np.clip(arr + noise, 0.0, 255.0).astype(np.uint8)

    final_img = Image.fromarray(arr)
    # Save with high quality
    final_img.save(out_path, format="JPEG", quality=95)
    print(f"Saved: {out_path}")

def main():
    print("=== BUILDING 20 AUTHENTIC RENAISSANCE & CLASSICAL POSTER BANNERS ===")
    success_count = 0

    for idx, (code, query, desc) in enumerate(SCULPTURE_QUERIES):
        print(f"\n[{idx+1:02d}/20] Tìm kiếm: {query} ({desc})")
        img_url = search_wikimedia_image(query)
        if not img_url:
            # Fallback to broader query
            broader = query.split()[0] + " marble statue"
            img_url = search_wikimedia_image(broader)

        if img_url:
            try:
                data = download_image(img_url)
                out_file = os.path.join(OUTPUT_DIR, f"{code}.jpg")
                process_banner(data, out_file, code)
                success_count += 1
            except Exception as e:
                print(f"Lỗi xử lý {code}: {e}")
        else:
            print(f"Không tìm thấy ảnh cho {query}")

    print(f"\n=> HOÀN TẤT: Đã xây dựng thành công {success_count}/20 banner Phục Hưng tại '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()
