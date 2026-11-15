#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Mass Production & HYA-08 Normalization for Theme 151 - 200
Tạo 50 bộ kiệt tác sơn dầu dọc 9:16 (1080x1920) chuẩn bảo tàng:
- slide_1.jpg: Establishing Shot (1.0x Toàn cảnh chuẩn bố cục)
- slide_2.jpg: Closeup Shot (1.65x Cận cảnh điểm tựa kịch tính & biểu cảm)
- slide_3.jpg: Macro Texture Shot (2.5x Siêu cận vào thớ toan và vệt cọ impasto)
Áp dụng chuẩn HYA-08 Anti-AI Standard:
- Lanczos 9:16 vertical smart crop
- -4% bão hòa đưa về sắc tố khoáng sơn dầu tự nhiên
- Phủ vi hạt toan vải hữu cơ (Organic Canvas Grain)
- Micro-contrast Unsharp Mask làm nổi gờ sơn dầu vật lý
Lưu đồng thời vào:
- assets/templates/multislides/{theme_id}/
- website/public/images/themes/{theme_id}/
"""

import os
import json
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H  # 9/16 = 0.5625

RAW_CACHE_DIR = r"c:\hiyuabyss\assets\templates\raw_cache"
MULTISLIDES_DIR = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_DIR = r"c:\hiyuabyss\website\public\images\themes"
MANIFEST_PATH = r"c:\hiyuabyss\scripts\oil_suites_151_200_prompts_manifest.json"
RESOLVED_PATH = r"c:\hiyuabyss\scripts\resolved_50_master_oil_art.json"

# Điểm tựa tiêu cự (focal center) được tinh chỉnh theo từng kiệt tác
FOCAL_CENTERS = {
    "theme_151": (0.50, 0.45),  # Georges de La Tour - The Penitent Magdalen (nến & mặt)
    "theme_152": (0.50, 0.48),  # Caravaggio - Narcissus (gương mặt soi bóng nước)
    "theme_153": (0.52, 0.45),  # Caravaggio - The Cardsharps (ba kẻ gian lận bài)
    "theme_154": (0.50, 0.45),  # Waterhouse - La Belle Dame sans Merci (nàng tiên & hiệp sĩ)
    "theme_155": (0.50, 0.50),  # Hammershøi - Interior with Young Woman (lưng người phụ nữ)
    "theme_156": (0.50, 0.50),  # Quentin Matsys - The Moneylender and his Wife (cặp vợ chồng đếm tiền)
    "theme_157": (0.50, 0.45),  # Francisco Goya - Saturn Devouring His Son (thần Saturn điên loạn)
    "theme_158": (0.35, 0.65),  # Friedrich - The Monk by the Sea (nhà sư cô độc bên bờ biển)
    "theme_159": (0.45, 0.52),  # Ilya Repin - Barge Haulers on the Volga (đoàn người kéo thuyền)
    "theme_160": (0.50, 0.40),  # Friedrich - Wanderer above the Sea of Fog (lữ khách trên đỉnh sương mù)
    "theme_161": (0.50, 0.45),  # Daumier - The Uprising (người dẫn đầu khởi nghĩa)
    "theme_162": (0.40, 0.50),  # Goya - The Third of May 1808 (người áo trắng trước họng súng)
    "theme_163": (0.55, 0.52),  # Rembrandt - The Anatomy Lesson (Dr Tulp và thi thể giải phẫu)
    "theme_164": (0.45, 0.55),  # Bruegel - The Blind Leading the Blind (những người mù ngã hố)
    "theme_165": (0.50, 0.50),  # Turner - The Slave Ship (mặt trời bão tố trên biển)
    "theme_166": (0.48, 0.50),  # Jacques-Louis David - The Death of Socrates (Socrates nâng chén độc)
    "theme_167": (0.50, 0.50),  # Jan Matejko - Stańczyk (chú hề âu lo trong phòng hội)
    "theme_168": (0.45, 0.55),  # Munch - Evening on Karl Johan Street (dòng người mắt trừng trắng dã)
    "theme_169": (0.50, 0.50),  # James Ensor - Christ's Entry into Brussels (đoàn người đeo mặt nạ)
    "theme_170": (0.50, 0.52),  # Friedrich - Two Men Contemplating the Moon (hai người ngắm trăng)
    "theme_171": (0.50, 0.45),  # Rodin - The Thinker (người trầm tư)
    "theme_172": (0.50, 0.45),  # William Blake - The Ancient of Days (thượng đế cầm compa)
    "theme_173": (0.50, 0.48),  # Manet - A Bar at the Folies-Bergère (nữ bồi bàn ánh mắt vô định)
    "theme_174": (0.42, 0.65),  # Munch - The Scream (nhân vật thét gào trên cầu)
    "theme_175": (0.50, 0.50),  # Fernand Léger - The City (khối công nghiệp máy móc)
    "theme_176": (0.50, 0.50),  # Bosch - The Garden of Earthly Delights (vườn địa đàng kỳ dị)
    "theme_177": (0.50, 0.48),  # Dürer - Melencolia I (thiên thần ưu uất)
    "theme_178": (0.50, 0.45),  # Friedrich - The Cross in the Mountains (thập giá trên đỉnh núi)
    "theme_179": (0.50, 0.52),  # Dalí - The Persistence of Memory (đồng hồ tan chảy)
    "theme_180": (0.50, 0.40),  # Delacroix - Liberty Leading the People (nữ thần tự do phất cờ)
    "theme_181": (0.50, 0.48),  # Caravaggio - The Incredulity of Saint Thomas (chạm vào vết thương)
    "theme_182": (0.50, 0.50),  # Hogarth - The Rake's Progress (kẻ phóng đãng phá sản)
    "theme_183": (0.50, 0.58),  # Velázquez - Las Meninas (công chúa nhỏ và triều thần)
    "theme_184": (0.50, 0.50),  # Millais - Ophelia (nàng Ophelia trôi sông)
    "theme_185": (0.50, 0.45),  # Artemisia Gentileschi - Judith Slaying Holofernes (nhát kiếm báo thù)
    "theme_186": (0.50, 0.42),  # Rembrandt - Self-Portrait with Two Circles (chân dung tự họa)
    "theme_187": (0.50, 0.48),  # Vermeer - The Astronomer (nhà thiên văn bên quả địa cầu)
    "theme_188": (0.40, 0.50),  # Rembrandt - The Return of the Prodigal Son (người cha ôm con)
    "theme_189": (0.50, 0.45),  # Spitzweg - The Bookworm (ông già mọt sách trên thang)
    "theme_190": (0.50, 0.45),  # Titian - Venus with a Mirror (thần Vệ Nữ trước gương)
    "theme_191": (0.50, 0.50),  # Titian - Sisyphus (Sisyphus đẩy tảng đá núi)
    "theme_192": (0.50, 0.50),  # Van Gogh - Prisoners' Round (vòng tròn tù nhân)
    "theme_193": (0.50, 0.45),  # Odilon Redon - The Cyclops (người khổng lồ một mắt)
    "theme_194": (0.50, 0.50),  # Friedrich - The Sea of Ice (băng trôi vụn vỡ)
    "theme_195": (0.50, 0.45),  # Claude Monet - Impression, Sunrise (mặt trời mọc le lói)
    "theme_196": (0.50, 0.48),  # Rembrandt - Jeremiah Lamenting (tiên tri Jeremiah than khóc)
    "theme_197": (0.50, 0.50),  # Turner - Snow Storm (tàu hơi nước giữa bão tuyết)
    "theme_198": (0.50, 0.50),  # Courbet - The Wave (ngọn sóng biển dữ dội)
    "theme_199": (0.50, 0.40),  # Goya - The Colossus (người khổng lồ trên mây)
    "theme_200": (0.50, 0.50)   # Friedrich - The Stages of Life (các giai đoạn cuộc đời bên bờ biển)
}

def apply_hya08_standard(im: Image.Image) -> Image.Image:
    """
    Quy chuẩn hậu kỳ HYA-08 Anti-AI Standard:
    1. Cân bằng sắc tố khoáng sơn dầu tự nhiên (-4% bão hòa, +4% tương phản).
    2. Phủ vi hạt toan vải hữu cơ (Organic Canvas Grain).
    3. Micro-contrast Unsharp Mask làm nổi rõ thớ vải và gờ impasto.
    """
    # 1. Color tuning (-4% bão hòa, +4% tương phản)
    sat = ImageEnhance.Color(im).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)

    # 2. Phủ hạt toan vải hữu cơ
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 1.8, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)

    # 3. Unsharp mask vi mô
    sharpened = grained.filter(
        ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2)
    )
    return sharpened

def generate_suite_for_theme(theme_id: str, raw_path: str):
    """
    Sinh trọn vẹn 3 slide dọc 9:16 cho một theme:
    - Slide 1: 1.0x Establishing
    - Slide 2: 1.65x Closeup
    - Slide 3: 2.5x Macro
    """
    raw_img = Image.open(raw_path).convert("RGB")
    W, H = raw_img.size

    cx, cy = FOCAL_CENTERS.get(theme_id, (0.50, 0.48))

    # Tính kích thước crop 1.0x (Aspect ratio 9:16)
    if W / H >= TARGET_RATIO:
        # Ảnh ngang: H là cạnh giới hạn
        crop_w_1 = int(H * TARGET_RATIO)
        crop_h_1 = H
        left_1 = int(cx * W - crop_w_1 / 2)
        left_1 = max(0, min(W - crop_w_1, left_1))
        top_1 = 0
    else:
        # Ảnh dọc: W là cạnh giới hạn
        crop_w_1 = W
        crop_h_1 = int(W / TARGET_RATIO)
        left_1 = 0
        top_1 = int(cy * H - crop_h_1 / 2)
        top_1 = max(0, min(H - crop_h_1, top_1))

    # Bố cục 3 slide
    crops = {}

    # Slide 1: 1.0x Establishing Shot
    box_1 = (left_1, top_1, left_1 + crop_w_1, top_1 + crop_h_1)
    crops[1] = box_1

    # Slide 2: 1.65x Closeup Shot (Tập trung điểm tựa kịch tính)
    zoom_2 = 1.65
    crop_w_2 = int(crop_w_1 / zoom_2)
    crop_h_2 = int(crop_h_1 / zoom_2)
    left_2 = int(cx * W - crop_w_2 / 2)
    left_2 = max(0, min(W - crop_w_2, left_2))
    top_2 = int(cy * H - crop_h_2 / 2)
    top_2 = max(0, min(H - crop_h_2, top_2))
    box_2 = (left_2, top_2, left_2 + crop_w_2, top_2 + crop_h_2)
    crops[2] = box_2

    # Slide 3: 2.5x Macro Texture Shot (Tập trung thớ toan và chất sơn impasto)
    zoom_3 = 2.5
    crop_w_3 = int(crop_w_1 / zoom_3)
    crop_h_3 = int(crop_h_1 / zoom_3)
    # Lệch nhẹ tâm tiêu cự để bắt chi tiết bề mặt phong phú
    cx_3 = min(0.9, max(0.1, cx + 0.02))
    cy_3 = min(0.9, max(0.1, cy + 0.02))
    left_3 = int(cx_3 * W - crop_w_3 / 2)
    left_3 = max(0, min(W - crop_w_3, left_3))
    top_3 = int(cy_3 * H - crop_h_3 / 2)
    top_3 = max(0, min(H - crop_h_3, top_3))
    box_3 = (left_3, top_3, left_3 + crop_w_3, top_3 + crop_h_3)
    crops[3] = box_3

    out_dirs = [
        os.path.join(MULTISLIDES_DIR, theme_id),
        os.path.join(WEBSITE_DIR, theme_id)
    ]
    for d in out_dirs:
        os.makedirs(d, exist_ok=True)

    slide_files = []
    for s_idx in [1, 2, 3]:
        box = crops[s_idx]
        region = raw_img.crop(box)
        resized = region.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        normalized = apply_hya08_standard(resized)

        for d in out_dirs:
            out_path = os.path.join(d, f"slide_{s_idx}.jpg")
            normalized.save(out_path, "JPEG", quality=95, optimize=True)
            slide_files.append(out_path)

    return slide_files

def main():
    print("=== CHẾ TÁC VÀ KHỬ AI BỘ 50 KIỆT TÁC SƠN DẦU (THEME 151 - 200) ===")
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    success_themes = 0
    missing_themes = []

    for stt in range(151, 201):
        theme_id = f"theme_{stt}"
        raw_file = os.path.join(RAW_CACHE_DIR, f"{theme_id}.jpg")

        if not os.path.exists(raw_file) or os.path.getsize(raw_file) < 10000:
            missing_themes.append(theme_id)
            continue

        size_kb = os.path.getsize(raw_file) / 1024
        print(f"🎨 Đang chế tác {theme_id} (bản scan {size_kb:.0f} KB)...")
        try:
            files = generate_suite_for_theme(theme_id, raw_file)
            print(f"  ✅ Hoàn tất 3 slide: {theme_id} ({len(files)} tệp đã lưu)")
            success_themes += 1
        except Exception as e:
            print(f"  ❌ Lỗi khi chế tác {theme_id}: {e}")

    print("\n=======================================================")
    print(f"🎉 TỔNG KẾT: {success_themes}/50 bộ ảnh đã hoàn thành ({success_themes * 3} slides)")
    if missing_themes:
        print(f"⚠️ Chưa có file scan cho {len(missing_themes)} themes: {missing_themes}")
    print("=======================================================")

if __name__ == "__main__":
    main()
