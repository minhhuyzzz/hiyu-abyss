#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Build Oil Painting Suites Spec & Manifest (Theme 151 - 200)
Tạo tài liệu đặc tả mỹ thuật HYA-08 docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md
và tệp manifest JSON scripts/oil_suites_151_200_prompts_manifest.json.
"""

import json
import os
import re

POSTS_PATH = "scripts/posts_151_200_data.json"
SPEC_PATH = "docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md"
MANIFEST_PATH = "scripts/oil_suites_151_200_prompts_manifest.json"

BASE_MEDIUM = "Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile oil canvas weave texture"
BASE_SAFE_ZONE = "Atmospheric fine art composition with quiet, generous negative space in the middle-to-lower third for elegant editorial reading, strictly clean with NO text, NO lettering, NO watermarks, NO digital CGI rendering, traditional museum oil on canvas"

def main():
    print("=== TẠO ĐẶC TẢ MỸ THUẬT HYA-08 & MANIFEST (THEME 151 - 200) ===")
    
    with open(POSTS_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    manifest = {}
    spec_sections = []
    
    for p in posts:
        stt = int(p["STT"])
        tid = p["Mã ID"]
        theme_id = p["Gợi Ý Phôi Ảnh"]
        title = p["Tiêu Đề (Dưới 90 từ)"]
        author = p["Nguồn Tác Giả"]
        topic = p["Chủ Đề Hạt Nhân"]
        slide_fmt = p["Định Dạng Slide"]
        phoi_info = p["Phôi Chi Tiết"]
        quote = p["Văn Bản Hoàn Chỉnh"]
        
        # Tách Tác giả và Tên tranh từ Phôi Chi Tiết
        # VD: "Georges de La Tour — 'The Penitent Magdalen' (Ánh nến soi rọi...)"
        parts = phoi_info.split("—")
        artist = parts[0].strip() if len(parts) > 0 else "Classical Master"
        rest = parts[1].strip() if len(parts) > 1 else ""
        
        artwork_m = re.search(r"'(.*?)'", rest)
        if artwork_m:
            artwork_title = artwork_m.group(1).strip()
            concept_m = re.search(r"\((.*?)\)", rest)
            concept = concept_m.group(1).strip() if concept_m else rest
        else:
            artwork_title = rest.split("(")[0].strip()
            concept = rest
            
        wikimedia_query = f"{artist} {artwork_title}"
        
        # Xây dựng 3 slide
        slides = [
            {
                "slide_index": 1,
                "role": "Establishing Shot (Toàn cảnh 1.0x)",
                "concept": f"Toàn cảnh kiệt tác '{artwork_title}' của {artist}: {concept}",
                "zoom": 1.0,
                "prompt": f"{BASE_MEDIUM}. Masterpiece '{artwork_title}' by {artist}. {concept}. Classical chiaroscuro lighting, subtle muted mineral pigments, rich historical depth. {BASE_SAFE_ZONE}."
            },
            {
                "slide_index": 2,
                "role": "Closeup Shot (Cận cảnh 1.65x)",
                "concept": f"Cận cảnh 1.65x vào tâm điểm kịch tính và biểu cảm nhân vật của '{artwork_title}'",
                "zoom": 1.65,
                "prompt": f"{BASE_MEDIUM}. Cinematic 1.65x closeup framing on the dramatic focal point and expressive details of '{artwork_title}' by {artist}. Intense emotional resonance, tactile paint layers. {BASE_SAFE_ZONE}."
            },
            {
                "slide_index": 3,
                "role": "Macro Texture Shot (Siêu cận 2.5x)",
                "concept": f"Siêu cận 2.5x vào thớ vải toan dệt hữu cơ, vệt cọ đắp nổi impasto và vết nứt thời gian của '{artwork_title}'",
                "zoom": 2.5,
                "prompt": f"{BASE_MEDIUM}. Extreme 2.5x macro view of physical canvas weave texture, historical craquelure, heavy impasto oil ridges, and deep chiaroscuro brushwork from '{artwork_title}' by {artist}. {BASE_SAFE_ZONE}."
            }
        ]
        
        manifest[tid] = {
            "stt": stt,
            "theme_id": theme_id,
            "title": title,
            "topic": topic,
            "author": author,
            "slide_format": slide_fmt,
            "artist": artist,
            "artwork_title": artwork_title,
            "concept": concept,
            "wikimedia_query": wikimedia_query,
            "slides": slides
        }
        
        # Tạo section markdown cho spec
        sec_md = f"""### ❖ Bài {stt}: {tid} — {theme_id.upper()}
- **Chủ đề hạt nhân:** `{topic}`
- **Nguồn tác giả:** *{author}*
- **Định dạng:** `{slide_fmt}` (Chuẩn bộ 3 slide: Toàn cảnh $\\rightarrow$ Cận cảnh $\\rightarrow$ Siêu cận)
- **Tác phẩm bảo tàng giám tuyển:** *{artwork_title}* — **{artist}**
- **Ý niệm thị giác:** *{concept}*
- **Truy vấn nguồn scan bảo tàng:** `{wikimedia_query}`
- **Trích dẫn chiêm nghiệm:** *"{quote}"*

#### Slide 1: {slides[0]['role']}
- **Mô tả:** {slides[0]['concept']}
- **Prompt Master:**
  ```text
  {slides[0]['prompt']}
  ```

#### Slide 2: {slides[1]['role']}
- **Mô tả:** {slides[1]['concept']}
- **Prompt Master:**
  ```text
  {slides[1]['prompt']}
  ```

#### Slide 3: {slides[2]['role']}
- **Mô tả:** {slides[2]['concept']}
- **Prompt Master:**
  ```text
  {slides[2]['prompt']}
  ```
"""
        spec_sections.append(sec_md)
        
    # Ghi file Manifest JSON
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo Manifest JSON thành công: {MANIFEST_PATH} ({len(manifest)} themes)")
    
    # Ghi file Spec Markdown
    spec_full = f"""# ĐẶC TẢ MỸ THUẬT SƠN DẦU HYA-08 & 50 BỘ SUITES (THEME 151–200)

> **Mã quy chuẩn:** `HYA-08` | **Dự án:** Hiyu Abyss Living Library & TikTok Publishing  
> **Cương lĩnh cốt lõi:**  
> 1. *100% Hội họa sơn dầu bảo tàng đích thực (Caravaggio, Rembrandt, Friedrich, Titian, Goya, Monet, Turner...).*  
> 2. *Khử hoàn toàn dấu vết AI: Không da nhựa sáp 3D, không hào quang neon rực rỡ, không ký tự giả mạo.*  
> 3. *Mỗi theme sở hữu trọn vẹn bộ 3 slide thu phóng nghệ thuật (1.0x Toàn cảnh $\\rightarrow$ 1.65x Cận cảnh $\\rightarrow$ 2.5x Siêu cận thớ toan & impasto).*  
> 4. *Tổng quy mô chế tác: Đúng 150 slide chất lượng cao (50 themes x 3 slides = 150 slides).*

---

## 1. CÔNG THỨC SƠN DẦU MASTER (THE MASTER OIL FORMULA)

Mọi hình ảnh sinh ra cho bài 151 đến 200 phải tuân thủ tuyệt đối cấu trúc 5 tầng:
1. **Chất liệu hội họa vật lý (Medium & Texture):** Tỷ lệ dọc `9:16` (1080x1920), sơn dầu cổ điển (*classical fine art oil painting*), vân cọ đắp nổi dày dặn (*heavy impasto brushstrokes*), toan vải dệt hữu cơ (*tactile oil canvas weave*).
2. **Khử hoàn toàn dấu vết AI (Anti-AI Standard):** Không da nhựa sáp 3D, không hào quang neon rực rỡ, không chữ hay ký tự giả nguệch ngoạc.
3. **Ý niệm thị giác đặc thù (Visual Metaphor):** Bám sát linh hồn từng bài viết, chuyển dịch triết lý tâm lý học thành hình ảnh ẩn dụ giàu sức gợi.
4. **Bảng màu theo cụm tư tưởng (Palette):**
   - **Thao túng tâm lý (151–160):** Ánh sáng Chiaroscuro u tối, ánh nến lẻ loi, xanh đêm Prussian, vàng đồng cổ điển.
   - **Tâm lý đám đông (161–170):** Khói bụi giông bão, xám than chì, đỏ bầm thảm khốc, ánh đèn quảng trường lạnh lẽo.
   - **Ngụy tín & Tự do (171–180):** Đất son trầm mặc, nâu sồi cổ, xanh sương mù hiện sinh, vàng nhạt hoài niệm.
   - **Thiên kiến nhận thức (181–190):** Đỏ nhung thẫm, hổ phách ấm, xanh rêu sâu, ánh sáng phản chiếu gương.
   - **Nghịch lý hiện sinh (191–200):** Xanh đại dương bão táp, băng tuyết bắc cực, vàng hoàng hôn rực rỡ, ánh sáng thức tỉnh.
5. **Vùng an toàn cho chữ (Text Safe Zone):** Chừa 40% diện tích thoáng đãng, sắc độ êm dịu ở trung tâm/dưới để biên tập chữ TikTok.

---

## 2. DANH MỤC 50 BỘ SUITES CHI TIẾT (STT 151–200)

""" + "\n---\n\n".join(spec_sections)

    with open(SPEC_PATH, "w", encoding="utf-8") as f:
        f.write(spec_full)
    print(f"✅ Đã tạo Đặc tả Mỹ thuật thành công: {SPEC_PATH}")

if __name__ == "__main__":
    main()
