#!/usr/bin/env python3
"""
Hiyu Abyss — Mass Production of 20 Full-Screen 9:16 (1080x1920) Renaissance Templates
Strictly:
- 100% Full-bleed 9:16 (1080x1920) filling the entire mobile screen from top to bottom.
- World-famous Renaissance, Baroque & Classical fine-art masterworks.
- Authentic full color with subtle dark moody wash (30% tint) so text never drowns out.
- Strictly NO text, NO watermarks, NO logos.
"""

import os
import io
import json
import urllib.request
import urllib.parse
import numpy as np
from PIL import Image

OUTPUT_DIR = "c:/hiyuabyss/assets/templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920

# 20 iconic masterworks perfectly aligned with the 20 core psychological themes
MASTERWORKS = [
    (
        "theme_01_hypocrisy",
        "Caravaggio Narcissus",
        "Narcissus (Caravaggio) — Chàng trai si mê ảo ảnh giả tạo của chính mình trong bóng tối"
    ),
    (
        "theme_02_double_standard",
        "Incredulity of Saint Thomas Caravaggio",
        "Sự Hoài Nghi Của Thánh Thomas (Caravaggio) — Đòi hỏi bằng chứng khắt khe và tiêu chuẩn kép"
    ),
    (
        "theme_03_morality",
        "Calling of Saint Matthew Caravaggio",
        "Lời Kêu Gọi Thánh Matthew (Caravaggio) — Lòng tốt và sự cứu chuộc giữa chốn trần tục"
    ),
    (
        "theme_04_ego",
        "Mourning of Icarus Herbert Draper",
        "Cái Chết Của Icarus (Draper) — Bản ngã bay quá cao và sự rơi rụng cay đắng"
    ),
    (
        "theme_05_self_deception",
        "Leonardo da Vinci Saint John Baptist C2RMF",
        "Thánh John (Leonardo da Vinci) — Nụ cười bí ẩn tự lừa dối trong màn đêm"
    ),
    (
        "theme_06_shadow",
        "Dante and Virgil Bouguereau",
        "Dante và Virgil (Bouguereau) — Góc khuất thú tính và bóng tối nội tâm dữ dội"
    ),
    (
        "theme_07_mask",
        "Judith beheading Holofernes Caravaggio",
        "Judith Chặt Đầu Holofernes (Caravaggio) — Mặt nạ quyến rũ và sự trừng phạt lạnh lùng"
    ),
    (
        "theme_08_power",
        "Death of Marat David",
        "Cái Chết Của Marat (Jacques-Louis David) — Quyền lực chính trị và sự sụp đổ cô độc"
    ),
    (
        "theme_09_manipulation",
        "Apollo and Daphne Bernini Rome",
        "Apollo và Daphne (Bernini) — Thao túng, chiếm đoạt và sự trói buộc hóa đá"
    ),
    (
        "theme_10_freedom",
        "Nike of Samothrace Louvre Paris",
        "Nữ Thần Tự Do Samothrace (Nike) — Sải cánh uy nghi vượt lên mọi gông cùm"
    ),
    (
        "theme_11_truth",
        "Saint Jerome Writing Caravaggio Borghese",
        "Thánh Jerome Trầm Mặc (Caravaggio) — Ngọn đèn chân lý soi rọi đầu lâu hư vô"
    ),
    (
        "theme_12_love",
        "Psyche Revived by Cupid Kiss Canova Louvre",
        "Cupid & Psyche (Canova) — Nụ hôn thức tỉnh tình yêu và ranh giới mong manh"
    ),
    (
        "theme_13_loyalty",
        "Oath of the Horatii David Louvre",
        "Lời Thề Horatii (Jacques-Louis David) — Lòng trung nghĩa tuyệt đối trước cái chết"
    ),
    (
        "theme_14_envy",
        "Medusa Caravaggio Florence",
        "Nữ Thần Medusa (Caravaggio) — Cơn cuồng nộ hủy diệt và ánh mắt đố kỵ hóa đá"
    ),
    (
        "theme_15_crowd",
        "Raft of the Medusa Gericault Louvre",
        "Chiếc Bè Của Chiến Hạm Medusa (Géricault) — Đám đông hỗn loạn giữa cơn giông bão"
    ),
    (
        "theme_16_suffering",
        "Michelangelo Dying Slave Louvre",
        "Người Nô Lệ Hấp Hối (Michelangelo) — Nỗi đau khổ thể xác và sự giải thoát linh hồn"
    ),
    (
        "theme_17_identity",
        "Rembrandt Self-Portrait 1659",
        "Chân Dung Tự Họa (Rembrandt) — Ánh mắt kiên định tìm lại bản sắc khi chỉ có một mình"
    ),
    (
        "theme_18_meaning",
        "Rembrandt Philosophe en meditation Louvre",
        "Nhà Triết Học Trong Trầm Tưởng (Rembrandt) — Bậc hiền triết đi tìm ý nghĩa cuộc đời"
    ),
    (
        "theme_19_solitude",
        "Wanderer above the Sea of Fog Friedrich",
        "Kẻ Lãng Du Trên Biển Sương Mù (Caspar David Friedrich) — Sự cô độc vĩ đại giữa cõi hư vô"
    ),
    (
        "theme_20_status",
        "Philippe de Champaigne Vanitas Louvre",
        "Bức Họa Vanitas (Champaigne) — Đồng hồ cát, hoa tàn và đầu lâu: sự phù du của danh vọng"
    )
]

def search_wikimedia_thumb(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=5&prop=imageinfo&iiprop=url&iiurlwidth=1280&gsrnamespace=6"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (admin@hiyuabyss.local)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get("query", {}).get("pages", {})
            for pid, pdata in pages.items():
                title = pdata.get("title", "")
                if any(title.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
                    img_info = pdata.get("imageinfo", [{}])[0]
                    thumb = img_info.get("thumburl")
                    if thumb:
                        return thumb
    except Exception as e:
        print(f"Error querying {query}: {e}")
    return None

def download_data(url):
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (admin@hiyuabyss.local)"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()

def process_fullscreen_9_16(img_data, out_path):
    src = Image.open(io.BytesIO(img_data)).convert("RGB")

    # Aspect Fill to completely cover 1080x1920 with NO letterboxing or borders
    scale = max(WIDTH / src.width, HEIGHT / src.height)
    new_w = int(src.width * scale)
    new_h = int(src.height * scale)
    resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)

    left = (new_w - WIDTH) // 2
    top = (new_h - HEIGHT) // 2
    cropped = resized.crop((left, top, left + WIDTH, top + HEIGHT))

    # Dark moody wash (preserve rich colors, deepen shadows for text legibility)
    arr = np.array(cropped, dtype=np.float32)
    arr = arr * 0.70

    # Fine organic film grain noise for authentic museum oil painting feel
    noise = np.random.normal(0.0, 1.8, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)

    final_img = Image.fromarray(arr)
    final_img.save(out_path, format="JPEG", quality=95)
    print(f"Saved: {out_path} (1080x1920)")

def main():
    print("=== BẮT ĐẦU SẢN XUẤT HÀNG LOẠT: 20 PHÔI FULL-SCREEN 9:16 PHỤC HƯNG ===")
    success_count = 0

    for idx, (code, query, desc) in enumerate(MASTERWORKS):
        print(f"\n[{idx+1:02d}/20] Đang tải: {desc}")
        thumb_url = search_wikimedia_thumb(query)
        if not thumb_url:
            # Fallback broader query
            fallback_q = query.split()[0] + " painting"
            thumb_url = search_wikimedia_thumb(fallback_q)

        if thumb_url:
            try:
                data = download_data(thumb_url)
                out_path = os.path.join(OUTPUT_DIR, f"{code}.jpg")
                process_fullscreen_9_16(data, out_path)
                success_count += 1
            except Exception as e:
                print(f"Lỗi xử lý {code}: {e}")
        else:
            print(f"Không tìm thấy ảnh cho: {query}")

    print(f"\n=> SẢN XUẤT HOÀN TẤT: {success_count}/20 phôi 9:16 Full-screen đã sẵn sàng tại '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()
