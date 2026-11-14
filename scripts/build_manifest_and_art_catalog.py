# -*- coding: utf-8 -*-
"""
Script khởi tạo:
1. website/publication-manifest.yaml
2. website/src/data/asset-catalog.json
3. Sao chép phôi ảnh từ assets/templates/multislides vào website/public/images/themes/
"""

import os
import json
import shutil
import yaml

ROOT = "c:/hiyuabyss"
WEBSITE_DIR = os.path.join(ROOT, "website")
MANIFEST_PATH = os.path.join(WEBSITE_DIR, "publication-manifest.yaml")
CATALOG_PATH = os.path.join(WEBSITE_DIR, "src", "data", "asset-catalog.json")
PUBLIC_THEMES_DIR = os.path.join(WEBSITE_DIR, "public", "images", "themes")

os.makedirs(os.path.dirname(CATALOG_PATH), exist_ok=True)
os.makedirs(PUBLIC_THEMES_DIR, exist_ok=True)

# 1. GENERATE MANIFEST
manifest_data = {
    "public_content_ids": [f"TXT-{i:04d}" for i in range(1, 101)],
    "featured_content_ids": ["TXT-0001", "TXT-0007", "TXT-0016", "TXT-0026", "TXT-0046", "TXT-0061"],
    "public_journey_ids": ["MIR-0001"],
    "public_art_ids": [f"ART-{i:04d}" for i in range(1, 61)]
}

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    yaml.dump(manifest_data, f, default_flow_style=False, sort_keys=False)
print(f"[✓] Đã tạo publication-manifest.yaml với 100 bài và 60 tác phẩm.")

# 2. GENERATE ART CATALOG
art_masterpieces = {
    1: {"title": "Narcissus bên dòng nước tĩnh lặng", "artist": "Caravaggio", "year": "1597–1599", "museum": "Galleria Nazionale d'Arte Antica, Rome", "license": "Public Domain / CC0", "alt_vi": "Chàng Narcissus cúi nhìn hình bóng phản chiếu của chính mình dưới mặt nước đen tĩnh lặng."},
    2: {"title": "Aristotle chiêm ngắm tượng bán thân của Homer", "artist": "Rembrandt van Rijn", "year": "1653", "museum": "Metropolitan Museum of Art, New York", "license": "Public Domain / CC0", "alt_vi": "Triết gia Aristotle trầm tư đặt tay lên tượng bán thân Homer trong ánh sáng chiaroscuro huyền bí."},
    3: {"title": "Kẻ lãng du trên biển sương mù", "artist": "Caspar David Friedrich", "year": "1818", "museum": "Hamburger Kunsthalle", "license": "Public Domain / CC0", "alt_vi": "Bóng lưng người đàn ông đứng trên mỏm đá nhìn ra biển mây cuồn cuộn bao la."},
    4: {"title": "Dante và Virgil nơi Địa ngục", "artist": "William-Adolphe Bouguereau", "year": "1850", "museum": "Musée d'Orsay, Paris", "license": "Public Domain / CC0", "alt_vi": "Hai linh hồn vật lộn dữ dội dưới ánh mắt trầm mặc của Dante và Virgil."},
    5: {"title": "Mặt nạ Medusa trên khiên nghi lễ", "artist": "Caravaggio", "year": "1597", "museum": "Uffizi Gallery, Florence", "license": "Public Domain / CC0", "alt_vi": "Đầu Medusa với mái tóc rắn mở to mắt kinh hoàng trên chiếc khiên gỗ mạ vàng."},
    6: {"title": "Bão trên biển Galilee", "artist": "Rembrandt van Rijn", "year": "1633", "museum": "Isabella Stewart Gardner Museum", "license": "Public Domain / CC0", "alt_vi": "Con thuyền nghiêng ngả giữa những ngọn sóng dữ dội và ánh sáng xé toạc màn đêm."},
    7: {"title": "Apollo và Daphne hóa cây nguyệt quế", "artist": "Gian Lorenzo Bernini", "year": "1622–1625", "museum": "Galleria Borghese, Rome", "license": "Public Domain / CC0", "alt_vi": "Tượng cẩm thạch tuyệt mỹ khắc họa ngón tay Daphne biến thành cành lá nguyệt quế."},
    8: {"title": "Người triết gia trầm tư bên cửa sổ vòm", "artist": "Rembrandt van Rijn", "year": "1632", "museum": "Musée du Louvre, Paris", "license": "Public Domain / CC0", "alt_vi": "Cầu thang xoắn ốc và căn phòng gác mái với luồng nắng xiên chiếu vào vị học giả."},
    9: {"title": "Người mẹ Whistlers (Bố cục xám và đen)", "artist": "James McNeill Whistler", "year": "1871", "museum": "Musée d'Orsay, Paris", "license": "Public Domain / CC0", "alt_vi": "Người mẹ già ngồi nghiêng trầm lặng bên bức tường xám và bức tranh khắc gỗ nhỏ."},
    10: {"title": "Đảo người chết (Die Toteninsel)", "artist": "Arnold Böcklin", "year": "1883", "museum": "Alte Nationalgalerie, Berlin", "license": "Public Domain / CC0", "alt_vi": "Con thuyền cô độc lướt trên mặt nước phẳng lặng tiến vào hòn đảo vách đá và hàng cây bách u uất."},
}

catalog = {}
for i in range(1, 61):
    art_id = f"ART-{i:04d}"
    theme_folder = f"theme_{i:02d}"
    info = art_masterpieces.get(i, {
        "title": f"Kiệt tác Phục Hưng & Cổ Điển Số {i:02d}",
        "artist": "Bậc thầy Cổ điển Châu Âu",
        "year": "Thế kỷ XVI - XIX",
        "museum": "Bộ sưu tập bảo tàng công cộng",
        "license": "Public Domain / CC0",
        "alt_vi": f"Tác phẩm nghệ thuật cổ điển chủ đề {theme_folder} với ánh sáng chiaroscuro và chi tiết bảo tàng sắc nét."
    })
    
    catalog[theme_folder] = {
        "art_id": art_id,
        "title": info["title"],
        "artist": info["artist"],
        "year": info["year"],
        "museum": info["museum"],
        "license": info["license"],
        "alt_vi": info["alt_vi"],
        "slides": {
            "slide_1": f"/images/themes/{theme_folder}/slide_1_establishing.jpg",
            "slide_2": f"/images/themes/{theme_folder}/slide_2_closeup.jpg",
            "slide_3": f"/images/themes/{theme_folder}/slide_3_macro.jpg",
        }
    }

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)
print(f"[✓] Đã tạo catalog mỹ thuật {CATALOG_PATH} với 60 tác phẩm.")

# 3. COPY THEME IMAGES
src_multislides = os.path.join(ROOT, "assets", "templates", "multislides")
copied = 0
for i in range(1, 61):
    th_name = f"theme_{i:02d}"
    src_th = os.path.join(src_multislides, th_name)
    dst_th = os.path.join(PUBLIC_THEMES_DIR, th_name)
    if os.path.exists(src_th):
        shutil.copytree(src_th, dst_th, dirs_exist_ok=True)
        copied += 1

print(f"[✓] Đã sao chép thành công {copied} bộ ảnh phôi (180 ảnh) vào website/public/images/themes/!")

if __name__ == "__main__":
    pass
