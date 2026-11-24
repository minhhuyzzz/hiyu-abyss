#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Build Oil Painting Suites Spec & Manifest (Theme 301 - 500)
Generates:
1. docs/12_HIYU_ABYSS_OIL_PAINTING_SUITES_301_500_SPEC.md
2. scripts/oil_suites_301_500_manifest.json (exactly 431 independent slides across 200 themes)
"""

import json
import os
import re

POST_FILES = [
    'scripts/posts_301_350.json',
    'scripts/posts_351_400.json',
    'scripts/posts_401_450.json',
    'scripts/posts_451_500.json'
]
SPEC_PATH = 'docs/12_HIYU_ABYSS_OIL_PAINTING_SUITES_301_500_SPEC.md'
MANIFEST_PATH = 'scripts/oil_suites_301_500_manifest.json'

BASE_MEDIUM = "Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile oil canvas weave texture"
BASE_SAFE_ZONE = "Atmospheric fine art composition with quiet, generous negative space in the middle-to-lower third for elegant editorial reading, strictly clean with NO text, NO lettering, NO watermarks, NO digital CGI rendering, traditional museum oil on canvas"

# Historical master portrait visual signatures for philosophers
AUTHOR_PORTRAIT_ENHANCEMENTS = {
    "Marcus Aurelius": "Featuring the noble Roman philosopher-emperor in classical imperial drapery of crimson and antique gold inspired by Eugène Delacroix's masterworks, dignified contemplative countenance, Roman marble archway bathed in warm golden torchlight",
    "Seneca": "Depicting the aging Stoic philosopher Seneca in flowing white and vermilion Roman tunic inspired by Manuel Domínguez Sánchez and Rubens, calm resolute expression of absolute inner peace, sunlit classical marble atrium",
    "Arthur Schopenhauer": "Featuring the solitary philosopher Arthur Schopenhauer inspired by Jules Lunteschütz's 1855 portrait, wild silver-white side hair, piercing contemplative blue eyes, Prussian black frock coat, crisp ivory cravat, warm Rembrandt chiaroscuro in a book-lined study",
    "Friedrich Nietzsche": "Featuring philosopher Friedrich Nietzsche inspired by Edvard Munch's 1906 portrait, iconic heavy dark mustache, monumental contemplative silhouette standing on an alpine mountain balcony, dramatic fiery sunset sky of amber and violet",
    "Epictetus": "Depicting the humble Stoic teacher Epictetus inspired by classical Baroque engravings, rustic linen cloak, wooden walking crutch leaning beside his desk, quill in hand, warm single-source candlelight illuminating a weathered brow of profound wisdom",
    "Lao Tzu (Lão Tử)": "Depicting ancient sage Laozi inspired by Zhang Lu's Ming Dynasty masterpiece, riding a tranquil water buffalo westward through mountain mist, flowing white beard and serene celestial robes, bathed in golden dawn mist",
    "Lao Tzu": "Depicting ancient sage Laozi inspired by Zhang Lu's Ming Dynasty masterpiece, riding a tranquil water buffalo westward through mountain mist, flowing white beard and serene celestial robes, bathed in golden dawn mist",
    "Niccolò Machiavelli": "Depicting Renaissance statesman Niccolò Machiavelli inspired by Santi di Tito's portrait in Palazzo Vecchio, rich black doublet over luminous scarlet velvet sleeves, sharp calculating gaze, warm Florentine interior lighting",
    "Benjamin Franklin": "Featuring polymath Benjamin Franklin inspired by Joseph Duplessis' 1778 portrait, russet coat with luxurious gray-brown fur collar, shoulder-length natural graying hair, warm Enlightenment candlelight illuminating eyes of shrewd benevolence",
    "Carl Jung": "Depicting psychiatrist Carl Jung seated in his rustic stone Bollingen tower study beside Lake Zurich, warm glowing hearth fire, alchemical manuscripts and books on a dark oak desk, warm amber and Prussian blue tones",
    "Viktor Frankl": "Depicting neurologist and psychiatrist Viktor Frankl in a resilient worn wool coat standing on a rugged alpine ridgeline, serene steadfast gaze greeting a radiant golden sunrise over snowcapped peaks",
    "Erich Fromm": "Depicting humanist psychoanalyst Erich Fromm in a mid-century academic study with leather-bound books, tweed jacket, soft warm lamplight casting an aura of empathetic insight and profound clarity",
    "Alfred Adler": "Depicting Viennese psychologist Alfred Adler in an early 20th-century intellectual salon, warm mahogany woodwork, morning window light illuminating a calm, encouraging expression",
    "Carl Rogers": "Depicting humanistic thinker Carl Rogers in a serene study with natural morning light streaming through sheer curtains, gentle open posture, warm earthy tones and soft pastel ambiance"
}

def get_author_enhancement(author_name):
    if not author_name:
        return ""
    for k, v in AUTHOR_PORTRAIT_ENHANCEMENTS.items():
        if k.lower() in author_name.lower():
            return v
    return ""

def get_luminous_palette(slide_num, total_slides, topic):
    # Ensure warm, radiant, luminous lighting palette
    if total_slides == 1:
        return "Luminous golden hour sunlight, rich amber and warm ochre tones, soft atmospheric glow, peaceful clarity"
    elif slide_num == 1:
        return "Subtle morning chiaroscuro, warm honey light cutting through cool shadows, tactile mineral oil pigments"
    elif slide_num == 2:
        return "Radiant golden sunbeams breaking through mist, warm terracotta and gilded bronze hues, profound emotional resonance"
    elif slide_num == 3:
        return "Vibrant warm golden sunlight, lush emerald greens, rosy pearl highlights and celestial sky, profound tranquility"
    else:
        return "Triumphant golden sunrise, celestial amber and radiant azure heavens, majestic alpine light, transcendent freedom"

def parse_post_slides(post):
    stt = post['stt']
    fmt = post['format']
    concept = post.get('concept', '')
    author = post.get('author', '')
    topic = post.get('topic', '')
    
    expected_slides = 1
    if "2 trang" in fmt:
        expected_slides = 2
    elif "3 trang" in fmt:
        expected_slides = 3
    elif "4 trang" in fmt:
        expected_slides = 4
    elif "1 trang" in fmt or "Single-Punch" in fmt:
        expected_slides = 1
        
    slide_texts = [
        post.get('hook', ''),
        post.get('twist', ''),
        post.get('mirror', ''),
        post.get('deep', '')
    ]
    
    parsed_slides = []
    
    if expected_slides == 1:
        c_clean = re.sub(r'^(Bộ\s+\d+\s+tranh\s+sơn\s+dầu:?|1\s+tranh\s+sơn\s+dầu:?)\s*', '', concept, flags=re.IGNORECASE).strip()
        parts = c_clean.split(' - ', 1)
        artist = parts[0].strip() if len(parts) > 1 else "Classical Master"
        desc = parts[1].strip() if len(parts) > 1 else c_clean
        parsed_slides.append({
            "slide_index": 1,
            "slide_type": "single_punch",
            "page_text": post.get('hook', '') or post.get('full_text', ''),
            "artist": artist,
            "description": desc
        })
    else:
        raw_parts = [part.strip() for part in concept.split('|') if part.strip()]
        for i, raw_s in enumerate(raw_parts, start=1):
            if i > expected_slides:
                break
            s_clean = re.sub(r'^(Bộ\s+\d+\s+tranh\s+sơn\s+dầu:?|Slide\s+\d+:?)\s*', '', raw_s, flags=re.IGNORECASE).strip()
            parts = s_clean.split(' - ', 1)
            artist = parts[0].strip() if len(parts) > 1 else "Classical Master"
            desc = parts[1].strip() if len(parts) > 1 else s_clean
            
            stype = f"slide_{i}_hook" if i == 1 else (f"slide_{i}_twist" if i == 2 else (f"slide_{i}_mirror" if i == 3 else f"slide_{i}_deep"))
            ptext = slide_texts[i - 1] if i - 1 < len(slide_texts) else ""
            
            parsed_slides.append({
                "slide_index": i,
                "slide_type": stype,
                "page_text": ptext,
                "artist": artist,
                "description": desc
            })
            
    # Process each slide into a full Master Prompt
    author_note = get_author_enhancement(author)
    
    result_slides = []
    for s in parsed_slides:
        s_idx = s["slide_index"]
        artist = s["artist"]
        desc = s["description"]
        ptext = s["page_text"]
        
        # Build visual metaphor
        metaphor_parts = [desc]
        if author_note and (s_idx == 1 or expected_slides == 1 or (expected_slides >= 2 and s_idx == 2)):
            # Include author portrait enhancement in slide 1 or 2
            metaphor_parts.append(author_note)
            
        full_metaphor = ". ".join(metaphor_parts)
        lighting = get_luminous_palette(s_idx, expected_slides, topic)
        
        # Build Master Prompt
        prompt = f"{BASE_MEDIUM}. Masterpiece inspired by {artist}. {full_metaphor}. {lighting}. {BASE_SAFE_ZONE}."
        
        result_slides.append({
            "slide_index": s_idx,
            "slide_type": s["slide_type"],
            "page_text": ptext,
            "artist": artist,
            "artwork_title": f"Thematic Study in the Style of {artist}",
            "visual_metaphor": full_metaphor,
            "lighting_palette": lighting,
            "prompt": prompt
        })
        
    return result_slides

def main():
    print("=== BẮT ĐẦU TỔNG HỢP ĐẶC TẢ & MANIFEST 200 BỘ TRANH SƠN DẦU (THEMES 301 - 500) ===")
    
    all_posts = []
    for fpath in POST_FILES:
        with open(fpath, encoding='utf-8') as f:
            all_posts.extend(json.load(f))
            
    print(f"Đã nạp {len(all_posts)} bài viết từ scripts/posts_301_500.")
    
    manifest = {}
    total_slides = 0
    
    for p in all_posts:
        stt = p['stt']
        theme_id = f"THEME_{stt:03d}"
        slides = parse_post_slides(p)
        total_slides += len(slides)
        
        manifest[theme_id] = {
            "stt": stt,
            "theme_id": theme_id,
            "title": p.get('title', ''),
            "topic": p.get('topic', ''),
            "author": p.get('author', ''),
            "format": p.get('format', ''),
            "slide_count": len(slides),
            "slides": slides
        }
        
    print(f"Tổng kết: {len(manifest)} themes, {total_slides} slides độc lập.")
    
    # 1. Ghi file manifest.json
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi thành công manifest: {MANIFEST_PATH}")
    
    # 2. Xây dựng tài liệu đặc tả markdown docs/12_HIYU_ABYSS_OIL_PAINTING_SUITES_301_500_SPEC.md
    lines = []
    lines.append("# ĐẶC TẢ MỸ THUẬT SƠN DẦU HYA-08 & 200 BỘ SUITES (THEME 301–500)")
    lines.append("")
    lines.append("> **Mã quy chuẩn:** `HYA-08` | **Dự án:** Hiyu Abyss Living Library & TikTok Publishing  ")
    lines.append("> **Cương lĩnh cốt lõi:**  ")
    lines.append("> 1. *100% Hội họa sơn dầu cổ điển bảo tàng đích thực (Delacroix, Rubens, Lunteschütz, Munch, Friedrich, Monet, Renoir, Sargent, Daumier, Hammershøi, Rembrandt, Vermeer).*  ")
    lines.append("> 2. *Tích hợp chân dung bảo tàng chuẩn xác của các triết gia lịch sử (Marcus Aurelius, Seneca, Schopenhauer, Nietzsche, Epictetus, Lão Tử, Machiavelli, Benjamin Franklin, Carl Jung, Viktor Frankl).*  ")
    lines.append("> 3. *Khử hoàn toàn dấu vết AI: Không da nhựa sáp 3D, không ánh sáng neon rực rỡ, không chữ giả mạo, tỷ lệ chuẩn dọc 9:16 (1080x1920).*  ")
    lines.append("> 4. *Nguyên tắc tác phẩm độc lập theo từng slide: Mỗi trang trong bài là một tác phẩm hội họa riêng biệt chuyển tải đúng nhịp điệu tư tưởng (Hiện tượng $\\rightarrow$ Cú lật $\\rightarrow$ Chiếc gương $\\rightarrow$ Đúc kết).*  ")
    lines.append(f"> 5. *Tổng quy mô chế tác: Đúng {total_slides} slide tranh sơn dầu độc lập trên {len(manifest)} bộ themes.*  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 1. CÔNG THỨC SƠN DẦU MASTER (THE MASTER OIL FORMULA)")
    lines.append("")
    lines.append("Mọi hình ảnh sinh ra cho bài 301 đến 500 phải tuân thủ tuyệt đối cấu trúc 5 tầng:")
    lines.append("1. **Chất liệu hội họa vật lý (Medium & Texture):** Tỷ lệ dọc `9:16` (1080x1920), sơn dầu cổ điển (*classical fine art oil painting*), vân cọ đắp nổi dày dặn (*heavy impasto brushstrokes*), toan vải dệt hữu cơ (*tactile oil canvas weave texture*).")
    lines.append("2. **Khử hoàn toàn dấu vết AI (Anti-AI Standard):** Tuyệt đối không bề mặt sáp/nhựa 3D, không ánh sáng neon phát sáng ảo, không chữ hay ký tự giả mạo, không dị tật giải phẫu.")
    lines.append("3. **Ý niệm thị giác theo từng slide (Slide-Specific Visual Metaphor):** Chuyển dịch chính xác nhịp điệu tâm lý của trang đó thành hình ảnh hội họa giàu sức gợi và tính biểu tượng.")
    lines.append("4. **Chân dung triết gia bảo tàng:** Tích hợp diện mạo, y phục và bối cảnh chuẩn xác theo danh tác của các bậc thầy hội họa.")
    lines.append("5. **Bảng màu tươi sáng, ấm áp & Vùng an toàn chữ (Text Safe Zone):** Vàng mật ong, xanh Phổ, cam đất nung, ánh nắng mai dát vàng; chừa 40% diện tích thoáng đãng ở 1/3 phía dưới để đặt văn bản TikTok.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 2. DANH MỤC 200 BỘ SUITES CHI TIẾT (STT 301–500 / {total_slides} SLIDES)")
    lines.append("")
    
    for tid, t in manifest.items():
        stt = t["stt"]
        title = t["title"]
        topic = t["topic"]
        author = t["author"]
        fmt = t["format"]
        slides = t["slides"]
        
        lines.append(f"### ❖ Bài {stt}: TXT-{stt:04d} — {tid}")
        lines.append(f"- **Chủ đề hạt nhân:** `{topic}`")
        lines.append(f"- **Nguồn tác giả:** *{author}*")
        lines.append(f"- **Định dạng bài:** `{fmt}` ({len(slides)} slide tranh sơn dầu độc lập)")
        lines.append(f"- **Tiêu đề bài viết:** *\"{title}\"*")
        lines.append("")
        
        for s in slides:
            s_idx = s["slide_index"]
            stype = s["slide_type"]
            ptext = s["page_text"]
            artist = s["artist"]
            metaphor = s["visual_metaphor"]
            lighting = s["lighting_palette"]
            prompt = s["prompt"]
            
            lines.append(f"#### Slide {s_idx}: Trang {s_idx} ({stype})")
            if ptext:
                lines.append(f"- **Nội dung trang:** *\"{ptext}\"*")
            lines.append(f"- **Danh họa / Trường phái:** *{artist}*")
            lines.append(f"- **Ý niệm thị giác:** {metaphor}")
            lines.append(f"- **Bảng màu & Ánh sáng:** {lighting}")
            lines.append(f"- **Master Prompt (9:16):**")
            lines.append("  ```text")
            lines.append(f"  {prompt}")
            lines.append("  ```")
            lines.append("")
            
        lines.append("---")
        lines.append("")
        
    with open(SPEC_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    print(f"✅ Đã xuất bản thành công tài liệu đặc tả: {SPEC_PATH} ({len(lines)} dòng).")

if __name__ == '__main__':
    main()
