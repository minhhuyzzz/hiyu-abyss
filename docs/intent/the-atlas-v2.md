# Confirmed Statement of Intent — The Atlas V2.1 & Astro 7

> **Dự án:** Hiyu Abyss (`minhhuyzzz/hiyu-abyss`)  
> **Nhánh mục tiêu:** `feat/the-atlas-v2` (phân nhánh từ `main` tại commit baseline `213e0f5dbbdb37e0fa9a732d22c12af0f3348435`)  
> **Tài liệu căn cứ:** `HIYU_ABYSS_THE_ATLAS_MASTER_SPEC_V2_1_ASTRO7_PREMIUM_UIUX.md`  
> **Ngày phê duyệt:** 18/11/2026

---

## 1. Mục tiêu cốt lõi (Outcome)
Thay thế hoàn toàn The Mirror bằng **The Atlas — Bản đồ Tư tưởng**, một trải nghiệm khám phá tri thức tương tác có chất lượng mỹ thuật bảo tàng cao cấp (Antique Celestial Atlas × Renaissance Museum × Interactive Editorial). Bao gồm:
- Bản đồ tương tác 2.5D (SVG/CSS), The Folio biên khảo, 29 điểm vào chủ đề, 8 tuyến khám phá giám tuyển (≥80 nút, ≥110 cạnh giải thích có chứng cứ).
- Hệ thống tìm kiếm không dấu/có dấu, bookmark cá nhân, cầu nối hai chiều giữa Library, Themes và The Agora.
- Nâng cấp toàn bộ hệ thống lên **Astro 7.x stable** cùng `@astrojs/cloudflare` v14 và cấu hình Workers tương thích.

## 2. Đối tượng thụ hưởng (User)
Độc giả của Hiyu Abyss muốn tự do khám phá mạng lưới tư tưởng, mỹ thuật và triết học đa chiều theo tiêu chuẩn bảo tàng, không bị ép vào kịch bản trắc nghiệm A/B hay đồ thị mạng nhện công nghiệp.

## 3. Lý do thực hiện (Why Now)
The Mirror trước đây mang tính tuyến tính giả lập; dự án cần một tính năng khám phá tư tưởng xứng tầm với kho 200 kiệt tác hội họa và giải quyết dứt điểm nợ kỹ thuật của Astro 5.

## 4. Tiêu chí thành công (Success)
- Đạt trọn vẹn 13 tiêu chí nghiệm thu định lượng (AC-01 đến AC-13).
- Chuẩn mỹ thuật độc bản cả hai theme: Obsidian Archive (Dark) và Ivory Cartographer (Light), thiết kế responsive chuẩn mực cho Desktop, Tablet và Mobile.
- `npm run build` trên Astro 7 thành công sạch lỗi 100%.
- Bàn giao đầy đủ `ATLAS_DATA_AUDIT.md`, `ATLAS_QA_REPORT.md`, ảnh chụp kiểm thử và Pull Request sạch.

## 5. Ràng buộc bất biến (Constraints)
- Tuyệt đối không tự merge vào `main` hay deploy production khi chưa có sự phê duyệt.
- Duy trì kiến trúc $0/tháng trên Cloudflare (D1, Workers, Static Assets).
- Không bịa đặt nguồn tranh, không gán ghép quan hệ học thuật giả mạo.
- Không lạm dụng WebGL hay 3D physics nặng nề; ưu tiên hiệu năng và khả năng truy cập (WCAG 2.2 AA).

## 6. Phạm vi loại trừ (Out of Scope)
- Không viết lại toàn bộ diễn đàn Agora (chỉ xử lý các chốt an toàn P0 và liên kết).
- Không can thiệp cấu hình DNS production hoặc tích hợp API trả phí.
